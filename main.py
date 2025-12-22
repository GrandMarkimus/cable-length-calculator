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

end_a_cab = 0
end_b_cab = 0

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

media_type = input("Copper or fiber (c/f): ")
end_a_cab = input("End A cabinet (1xx/2xx): ")
end_a_ru = input("End A RU (0-48): ")
end_a_facing = input("End A facing (f/r): ")
end_b_cab = input("End B cabinet (1xx/2xx): ")
end_b_ru = input("End B RU (0-48): ")
end_b_facing = input("End B facing (f/r): ")

#
