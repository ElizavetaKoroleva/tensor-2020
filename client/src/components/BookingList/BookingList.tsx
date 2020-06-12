import React, {useState} from 'react';
import { IBookingList } from '../../types';
import BookingItem from '../BookingItem/BookingItem';

const BookingList: React.SFC<IBookingList> = (props): JSX.Element => {
  const { bookings } = props;

  return (
      <div className="booking-list">
        <ul className="booking-list__list">
          {bookings.map(booking => (
            <li className="booking-list__item" key={booking.id}>
              <BookingItem 
                id={booking.id} 
                event={booking.event} 
                tickets={booking.tickets}/>
            </li>
          ))}
        </ul>
      </div>
  );
};

export default BookingList;
