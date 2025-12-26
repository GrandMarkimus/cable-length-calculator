class device():
  def __init__(self, cab=0, face=None, ru=0):
    self.cab = cab
    self.face = face
    self.ru = ru

#variables to determine
media_type = "u"
cab_a_face = "u"
cab_b_face = "u"
same_cab = False
cab_a_ru = 0 #range 0 to 48
cab_b_ru = 0 #range 0 to 48
cross_aisle = False
dist_x_cabs = 0
total_length = 0
device_1 = device
device_2 = device

rack_width_count = 0

end_a_cab = 0
end_b_cab = 0

#Constants
RU = 1.75
RACK_WIDTH = 31.5
#RACK_HEIGHT = 89.9
RACK_DEPTH = 47.2
OFFSET_R = 15.5
OFFSET_F = 1.5
AISLE = 87.5
CROSS_RU = 29
TOP_GAP = 1.5
COPPER_TRAY_HEIGHT = 9.5
FIBER_TRAY_HEIGHT = 22
R101_TO_DMARC = 45.2
DMARC_TO_FIBER_PATCH = 17

#Function to handle yes/no questions
def yes_no(prompt: str) -> bool:
    while True:
        val = input(f"{prompt} (y/n): ").strip().lower()
        if val in ("y", "n"):
            return val == "y"
        print("Please enter y or n")

#Describe device #1
print("Enter information for device #1")




def facing_and_ru():
  face = input("Front or Rear (f/r): ").strip().lower()
  if face in ("y", "n"):
    return
  ru = int(input("RU (0-48): "))
  return face,ru

def cab():
  cab = int(input("Cabinet (1xx/2xx): "))
  return cab

def media():
  media = input("Copper or fiber (c/f): ")
  return media

def print_all(cab,face,ru):
  print(cab)
  print(face)
  print(ru)

#start
same_cab = input("Does this cable leave the cabinet (y/n): ")
if(same_cab == "n"):
  #cable run doesn't leave the cabinet
  same_cab = True
  cab_a = 101
  cab_b = 101
  print("Enter information for device #1 \n")
  cab_a_face,cab_a_ru = facing_and_ru()
  print("Enter information for device #2 \n")
  cab_b_face,cab_b_ru = facing_and_ru()
  print("cab a:\n")
  print(cab_a_face)
  print(cab_a_ru)
  print("cab b:\n")
  print(cab_b_face)
  print(cab_b_ru)

else:
  #cable run leaves the cabinet
  same_cab = False
  #Add top gap for both cabs
  total_length = TOP_GAP*2
  media_type = media()
  cab_a = cab()
  cab_a_face,cab_a_ru = facing_and_ru()
  cab_b = cab()
  cab_b_face,cab_b_ru = facing_and_ru()
  print("cab a:")
  print_all(cab_a,cab_a_face,cab_a_ru)
  print("\ncab b:")
  print_all(cab_b,cab_b_face,cab_b_ru)
  print(f"Total cable length: {total_length}")

dist_x_cabs = abs(end_a_cab - end_b_cab)
#
