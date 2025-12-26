class device():
  def __init__(self, cab=0, rear_facing=True, ru=0):
    self.cab = cab
    self.rear_facing = rear_facing #Face only matters for same cab scenario
    self.ru = ru

#variables
#------
device_1 = device()
device_2 = device()
cable_length = 0

#constants
#------
RU = 1.75
TOP_GAP = 3
FTB_RU = 29
CAB_WIDTH = 31.5
CAB_DEPTH = 47.2
AISLE = 87.5
DMARC_FIBER_PATCH_HEIGHT = 17
DMARC_TO_101 = 45.2

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
#Get cabinet number
def get_cab() -> int:
  while True:
    try:
      cab = int(input("Cabinet # (x01-x04): "))
      if (101 <= cab <= 104) or (201 <= cab <= 204):
        return cab
      print("Invalid cabinet #. Must be between 101-104 or 201-204")
    except ValueError:
      print("Invalid input. Must enter a number")
#
#Get RU
def get_ru() -> int:
  while True:
    try:
      ru = int(input("RU # (1-48): "))
      if 1 <= ru <= 48:
        return ru
      print("Invalid RU. Must be between 1 and 48")
    except ValueError:
      print("Invalid input. Must enter a number")
#
#Output device information
def print_dev_info(dev):
  print(f"Cab: {dev.cab}")
  print(f"Face: {dev.face}")
  print(f"RU: {dev.ru}")
#
#Determine copper or fiber tray and return height x2
def tray_type():
  COPPER_TRAY_HEIGHT = 9.5*2
  FIBER_TRAY_HEIGHT = 22*2
  #
  media_type = yes_no("Copper run (y/n): ")
  if media_type == True:
    return COPPER_TRAY_HEIGHT
  else:
    return FIBER_TRAY_HEIGHT
#
#Calculate and output distance to aisle crossing
def dist_to_aisle_xing():
  device_1_xing = abs(device_1.cab - 103)
  device_2_xing = abs(device_2.cab - 203)
  result = (device_1_xing + device_2_xing)*CAB_WIDTH
  return result
#
#Convert and output imperial measurement
def in_to_ft(inches):
  feet = int(inches // 12)
  remaining_inches = round(inches % 12,2)
  print(f"{feet}ft {remaining_inches}in")
#
#Convert and output metric measurement
def in_to_m(inches):
  meters = round(inches * .0254,2)
  print(f"{meters}m")

#__main__
#device 1 info
device_1.cab = get_cab()
device_1.face = yes_no("Rear facing (y/n): ")
device_1.ru = get_ru()
#
#device 2 info
device_2.cab = get_cab()
device_2.face = yes_no("Rear facing (y/n): ")
device_2.ru = get_ru()
#
print_dev_info(device_1)
print("\n")
print_dev_info(device_2)

if device_1.cab == device_2.cab:
# same cab
# is it the same side?
  if device_1.face == device_2.face:
    #same cab same side
    cable_length = abs(device_1.ru - device_2.ru)*RU
    print("Total Cable length")
    print("------")
    in_to_ft(cable_length)
    in_to_m(cable_length)
  else:
    #same cab diff side
    cable_length = abs(device_1.ru - FTB_RU)*RU
    print(f'step1 = {cable_length}')
    cable_length = abs(device_2.ru - FTB_RU)*RU + cable_length
    print(f'step2 = {cable_length}')
    cable_length = cable_length + CAB_DEPTH
    print(f'step3 = {cable_length}')
    print("Total Cable length")
    print("------")
    in_to_ft(cable_length)
    in_to_m(cable_length)
else:
# diff cabs
  tray_height = tray_type()
  #need to capture distance from cab to aisle crossing which is middle of 103
  #101 would cross 102 and half 103
  #104 would cross 104 and half 103
  if abs(device_1.cab - device_2.cab) >= 100:
    #diff rows
    cable_length = dist_to_aisle_xing()
    cable_length = (48 - device_1.ru)*RU + cable_length
    cable_length = (48 - device_2.ru)*RU + cable_length
    cable_length = TOP_GAP + cable_length
    cable_length = AISLE + cable_length
    cable_length = tray_height + cable_length
    in_to_ft(cable_length)
    in_to_m(cable_length)






#
#scenarios
#  same cab same side   done
#    RU between devices
#  same cab dif sides   done
#    dev1 RU to trough
#    dev2 RU to trough
#    cabinet depth
#  dif cabs same row
#    dev1 48 minus RU + top_gap
#    dev1 distance to tray (c/f)
#    dev2 48 minus RU + top_gap
#    dev2 distance to tray (c/f)
#    distance between cabs
#  dif cabs dif row
#    dev1 48 minus RU + top_gap
#    dev1 distance to tray (c/f)
#    dev2 48 minus RU + top_gap
#    dev2 distance to tray (c/f)
#    distance between cabs
#    aisle distance