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


def facing_and_ru(face, ru):
  face = input("Front or Rear (f/r): ")
  ru = input("RU (0-48): ")
  return face

def media_and_cab(media, cab):
  media = input("Copper or fiber (c/f): ")
  cab = int(input("Cabinet (1xx/2xx): "))

#start
same_cab = input("Does this cable leave the cabinet (y/n): ")
if(same_cab == "n"):
  #cable run doesn't leave the cabinet
  same_cab = False
  cab_a = 101
  cab_b = 101
  print("Enter information for device #1 \n")
  facing_and_ru(cab_a_face,cab_a_ru)
  print("Enter information for device #2 \n")
  facing_and_ru(cab_b_face,cab_b_ru)
  print("cab a:\n")
  print(cab_a_face)
  print(cab_a_ru)

else:
  #cable run leaves the cabinet
  same_cab = True
  #get media type
  #get cabinet a/b
  #get facing a/b
  #get ru a/b

dist_x_cabs = abs(end_a_cab - end_b_cab)


#
