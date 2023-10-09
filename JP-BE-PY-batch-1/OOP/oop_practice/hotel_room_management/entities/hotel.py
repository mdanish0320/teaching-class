from datetime import date

class Hotel:
  def __init__(self, name, address):
    self.__name = name
    self.address = address
    self.rooms = []
    self.room_booking = []

  def get_name(self):
    return self.__name

  def add_new_rooms(self, room):
    self.rooms.append(room)

  def get_room_count(self):
    return len(self.rooms)

  def available_rooms(self):
    available_rooms_count = 0
    for room in self.rooms:
      if room.is_available == True:
        available_rooms_count += 1
    return available_rooms_count

  def occupied_rooms(self):
    occupied_rooms_count = 0
    for room in self.rooms:
      if room.is_available == False:
        occupied_rooms_count += 1
    return occupied_rooms_count
  
  def total_booking(self):
    return len(self.room_booking)

  def is_room_avaiable_now(self, des_room):
    for room in self.rooms:
      if room == des_room:
        if room.is_available == True:
          return True
    return False
  
  def is_booking_available(self, des_room, start_date, end_date):
    reversed_booking = reversed(self.room_booking)
    for booking in reversed_booking:
      if booking.room == des_room:
        if start_date >= booking.booking_end_date:
          return True
        else:
          return False
    return True
  
  def stats(self):
    print(
        "total rooms:", self.get_room_count()
    )
    print(
        "available rooms:", self.available_rooms()
    )
    print(
        "occupied rooms:", self.occupied_rooms()
    )
    print(
        "total booking:", self.total_booking()
    )
    
    print("------------------")

  def make_room_availale():
    pass
  
  def make_room_occupied(self, des_room):
    for room in self.rooms:
      if room == des_room:
        room.is_available = False

  def book_room(self, booking):
    if self.is_booking_available(
      booking.room,
      booking.booking_start_date,
      booking.booking_end_date
    ):
      if booking.booking_start_date == date.today():
        self.make_room_occupied(booking.room)
      self.room_booking.append(booking)
    else:
      print("room not available")
      print("------------------")
