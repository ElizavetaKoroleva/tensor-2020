# Билетная касса театра

## Страницы

* Главная с афишей
* Страница с подробным описанием мероприятия и залом
* Страница бронирования
* Список всех броней
* Страница 404
* Страница 500

## БД

### Минимум

    events:
        _id: ObjectId - номер 1, 2, 3
        title: string - название мероприятия
        author: string - автор
        photo: string - ссылка на фото url
        start_time: datetime - день и время начала мероприятия
        end_time: datetime - день и время окончания мероприятия
        description: string - описание мероприятия, аннотация; текст (не html)
        director: string - режиссеры; список текстом
        actors: string - актеры; список текстом

    tickets:
        _id: ObjectId - номер 1, 2, 3
        row: integer - ряд
        seat: integer - место
        event: ObjectId events- мероприятие
        price: integer - цена
        color_zone: string - цвет стоимостной зоны
        is_booked: boolean - забронировано

    bookings: 
        _id: ObjectId - номер 1, 2, 3
        password_to_cancel: hash - пароль для отмены брони
        phone_number: integer - номер телефона
        event: ObjectId events- мероприятие
        tickets: [
            {   
                _id: ObjectId - номер 1, 2, 3
                row: integer - ряд
                seat: integer - место
                price: integer - цена
                color_zone: string - цвет стоимостной зоны  
            } 
        ]


### Максимум

Для создания афиши, нужна админка. 
А иначе как создавать, редактировать, удалять мероприятия?

Новости/объявления:
Спектакль отменен! Карантин


## API

1. Главная страница

**/api/v1/get_events_list?offset=0&limit=1**

    frontend -> backend
    подгрузка
        offset: integer - сколько загружено
        limit: integer - сколько передавать
    frontend <- backend
    список мероприятий
        events_list: 
        [
            { 
                id: ObjectId event
                title: string - название мероприятия
                photo: string - ссылка на фото url
                start_time: datetime - день и время начала мероприятия
            }, ...
        ]
        hasmore: boolean - есть ли еще события

2. Страница мероприятия

**/api/v1/get_event?id=000000000000000000000001**

    frontend -> backend
    переход к подробному описанию
        id: ObjectId event - id мероприятия
    frontend <- backend
    описание мероприятия, информация о билетах
        event:
        {
            id: ObjectId event - id мероприятия
            title: string - название мероприятия
            photo: string - ссылка на фото url
            start_time: datetime - день и время начала мероприятия
            end_time: datetime - день и время окончания мероприятия
            description: string - описание мероприятия, аннотация; текст (не html)
            director: string - режиссеры; список текстом
            actors: string - актеры; список текстом
        }
        tickets:
        [
            {
                id: ObjectId ticket - id билета
                row: integer - ряд
                seat: integer - место
                price: integer - цена
                color_zone: string - цвет стоимостной зоны
                is_booked: boolean - забронировано
            }, ...
        ]

3. Бронирование

**/api/v1/add_booking**

    frontend -> backend
    бронирование
        phone_number: integer - номер телефона
        password_to_cancel: string - пароль для отмены брони
        event: ObjectId event - id мероприятия
        tickets: [
            { 
                id: ObjectId ticket - id билета
            }, ...
        ]
    frontend <- backend
    успешное бронирование
        id: integer - id брони
        is_success: boolean - успешно ли забронировано

4. Просмотр действующих броней

**/api/v1/get_bookings_list?phone_number=88005353535**

    frontend -> backend
    просмотр броней
        phone_number: integer - номер телефона
    frontend <- backend
    список броней
        bookings:
        [
            {   
                id: integer - id брони
                event: {
                    id: ObjectId event - id мероприятия
                    title: string - название мероприятия
                    start_time: datetime - день и время начала мероприятия
                }
                tickets: [
                    {   id: ObjectId - id билета
                        row: integer - ряд
                        seat: integer - место
                        price: integer - цена
                        color_zone: string - цвет стоимостной зоны 
                    }, ...
                ]
            }, ...
        ]

**/api/v1/canсel_booking**

    frontend -> backend
    отмена брони
        id: integer - номер брони 1, 2, 3
        phone_number: integer - номер телефона
        password_to_cancel: string - пароль для отмены брони
    frontend <- backend
    успешное удаление брони
        is_success: boolean - успешно ли
