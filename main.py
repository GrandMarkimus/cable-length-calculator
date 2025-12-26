class device():
  def __init__(self, cab=0, rear_facing=True, ru=0):
    self.cab = cab
    self.rear_facing = rear_facing
    self.ru = ru

#variables
device_1 = device()
device_2 = device()
#------

#constants
#------

#functions
#------
#Handles yes/no questions
def yes_no(prompt: str) -> bool:
    while True:
        val = input(f"{prompt} (y/n): ").strip().lower()
        if val in ("y", "n"):
            return val == "y"
        print("Please enter y or n")
#
def get_cab() -> int:
   while True:
      try:
         cab = int(input("Enter cabinet number between 101 and 104: "))
         if 101 <= cab <= 104:
            return cab
         print("Invalid cabinet #. Must be between 101 and 104")
      except ValueError:
         print("Invalid input. Must enter a number")
#scenarios
#same cab same side
#same cab dif sides
#dif cabs same row
#dif cabs dif row
#double the above (copper/fiber)

#device #1 info
device_1.cab = get_cab()
device_1.face = get_face()
device_1.ru = get_ru()