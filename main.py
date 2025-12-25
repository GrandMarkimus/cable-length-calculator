import math

#variables to determine
media_type = "u"
cab_a_face = "u"
cab_b_face = "u"
same_cab = False
cab_a_ru = 0 #range 0 to 48
cab_b_ru = 0 #range 0 to 48
cross_aisle = False
dist_x_cabs = 0

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


def facing_and_ru():
  face = input("Front or Rear (f/r): ")
  ru = int(input("RU (0-48): "))
  return face,ru

def cab():
  cab = int(input("Cabinet (1xx/2xx): "))

def media():
  media = input("Copper or fiber (c/f): ")


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
  media_type = media()
  cab_a = cab()
  cab_a_face,cab_a_ru = facing_and_ru()
  cab_b = cab()
  cab_b_face,cab_b_ru = facing_and_ru()
  print("cab a:\n")
  print(cab_a_face)
  print(cab_a_ru)
  print("cab b:\n")
  print(cab_b_face)
  print(cab_b_ru)

dist_x_cabs = abs(end_a_cab - end_b_cab)


#
