""" Список мероприятий для главной страницы """
from flask import jsonify, request

from server import APP, MONGO
from server.exception.error_data_db import ErrorDataDB


@APP.route("/api/<version>/get_list_events", methods=["GET"])
def get_list_events(version):
    """ Получить список мероприятий """
    if version != "v1":
        return jsonify({"message":"Некорректная версия", "list_events": []})
    try:
        skip = parse_positive_int(request.args.get("offset"))
        limit = parse_positive_int(request.args.get("limit"))
    except ErrorDataDB as error_bd:
        return jsonify({"message": error_bd.message, "list_events": []})
    cursor = MONGO.db.event.find(
        {},
        {
            "_id": 1,
            "title": 1,
            "photo": 1,
            "start_time": 1
        }
    ).sort("start_time").skip(skip).limit(limit)
    events = list(cursor)
    for event in events:
        event["id"] = event.pop("_id")
    return jsonify({"list_events": events})

def parse_positive_int(value):
    """ Преобразовать в положительное целое число """
    if value is None:
        raise ErrorDataDB(f"Отсутствует необходимый параметр.")
    if not value.isdigit():
        raise ErrorDataDB(
            f"Получено некорректное значение '{value}'. Должно быть положительное целое число."
        )
    return int(value)
