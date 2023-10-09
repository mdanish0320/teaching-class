class Room:
  def __init__(self, name, num_beds, fare_per_day):
    self.name = name
    self.num_beds = num_beds
    self.fare = fare_per_day
    self.is_available = True
