import math

#variables to determine
media_type = "u"
end_a_facing = "u"
end_b_facing = "u"
same_cab = "u"
end_a_ru = 0 #range 0 to 48
end_b_ru = 0 #range 0 to 48
cross_aisle = "u"

rack_width_count = 0

#constants
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

while True:
    same_cab = input("Copper or fiber? (c/f): ").strip().lower()
    if same_cab in ("c", "f"):
        break
    print("Please enter 'y' or 'n'.")
while True:
    same_cab = input("Does run leave the cabinet? (y/n): ").strip().lower()
    if same_cab in ("y", "n"):
        break
    print("Please enter 'y' or 'n'.")
while True:
    end_a_facing = input("End-A facing (f/r)?").strip().lower()
    if end_a_facing in ("f", "r"):
        break
    print("Please enter 'f' or 'r'.")
while True:
    end_b_facing = input("End-B facing (f/r)?").strip().lower()
    if end_b_facing in ("f", "r"):
        break
    print("Please enter 'f' or 'r'.")
if(same_cab=="y"):
    while True:
        cross_aisle = input("Does cable cross aisle? (y/n): ").strip().lower()
        if cross_aisle in ("y", "n"):
            break
        print("Please enter 'y' or 'n'.")
else:
    cross_aisle=="n"
#
