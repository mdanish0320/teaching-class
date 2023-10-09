from datetime import date, timedelta

from entities.room import Room
from entities.hotel import Hotel
from entities.account import Account
from entities.room_booking import RoomBooking



def main():
  room_1 = Room("room A", 1, 1000)
  room_2 = Room("room B", 2, 2000)
  room_3 = Room("room C", 3, 3000)

  hotel = Hotel("Five Start Hotel", "Garden West Karachi")
  
  hotel.add_new_rooms(room_1)
  hotel.add_new_rooms(room_2)
  hotel.add_new_rooms(room_3)
  
  
  hotel.stats()
  
  danish = Account("danish", 30)
  
  booking = RoomBooking(
      room_1,
      danish,
      date.today(),
      (date.today() + timedelta(days=2))
  )
  hotel.book_room(booking)
  hotel.stats()
    
  
  booking = RoomBooking(
      room_1,
      danish,
      date.today(),
      (date.today() + timedelta(days=2))
  )
  hotel.book_room(booking)
  hotel.stats()
  
  booking = RoomBooking(
      room_1,
      danish,
      date.today() + timedelta(days=2),
      (date.today() + timedelta(days=4))
  )
  hotel.book_room(booking)
  hotel.stats()

if __name__ == '__main__':
  main()
