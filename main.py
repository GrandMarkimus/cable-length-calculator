class Device:
    def __init__(self, cab=0, rear_facing=True, ru=0):
        self.cab = cab
        self.rear_facing = rear_facing
        self.ru = ru
    
    def __str__(self):
        return f"Cab: {self.cab}\nFace: {self.rear_facing}\nRU: {self.ru}"

#Constants
RU = 1.75
TOP_GAP = 3
FTB_RU = 29
CAB_WIDTH = 31.5
CAB_DEPTH = 47.2
AISLE = 87.5
COPPER_TRAY_HEIGHT = 9.5 * 2
FIBER_TRAY_HEIGHT = 22 * 2
DMARC_FIBER_PATCH_HEIGHT = 17
DMARC_TO_101 = 45.2

#Functions
def yes_no(prompt: str) -> bool:
    while True:
        val = input(f"{prompt} (y/n): ").strip().lower()
        if val in ("y", "n"):
            return val == "y"
        print("Please enter y or n")

def get_cab() -> int:
    while True:
        try:
            cab = int(input("Cabinet # (x01-x04): "))
            if (101 <= cab <= 104) or (201 <= cab <= 204):
                return cab
            print("Invalid cabinet #. Must be between 101-104 or 201-204")
        except ValueError:
            print("Invalid input. Must enter a number")

def get_ru() -> int:
    while True:
        try:
            ru = int(input("RU # (1-48): "))
            if 1 <= ru <= 48:
                return ru
            print("Invalid RU. Must be between 1 and 48")
        except ValueError:
            print("Invalid input. Must enter a number")

def get_tray_height() -> float:
    return COPPER_TRAY_HEIGHT if yes_no("Copper run") else FIBER_TRAY_HEIGHT

def format_length(inches: float):
    """Print length in both imperial and metric"""
    feet = int(inches // 12)
    remaining_inches = round(inches % 12, 2)
    meters = round(inches * 0.0254, 2)
    print(f"{feet}ft {remaining_inches}in ({meters}m)")

def get_device_info() -> Device:
    """Gather all device information"""
    return Device(
        cab=get_cab(),
        rear_facing=yes_no("Rear facing"),
        ru=get_ru()
    )

def calculate_cable_length(dev1: Device, dev2: Device) -> float:
    if dev1.cab == dev2.cab:
        #Same cabinet
        if dev1.rear_facing == dev2.rear_facing:
            #Same side
            return abs(dev1.ru - dev2.ru) * RU
        else:
            #Different sides
            return (abs(dev1.ru - FTB_RU) + abs(dev2.ru - FTB_RU)) * RU + CAB_DEPTH
    
    #Different cabinets
    tray_height = get_tray_height()
    base_length = (48 - dev1.ru) * RU + (48 - dev2.ru) * RU + TOP_GAP + tray_height
    
    if abs(dev1.cab - dev2.cab) >= 100:
        #Different rows
        aisle_crossing = (abs(dev1.cab - 103) + abs(dev2.cab - 203)) * CAB_WIDTH
        return base_length + AISLE + aisle_crossing
    else:
        #Same row
        cab_distance = abs(dev1.cab - dev2.cab) * CAB_WIDTH
        return base_length + cab_distance

#Main
if __name__ == "__main__":
    device_1 = get_device_info()
    print()
    device_2 = get_device_info()
    
    print("\n" + str(device_1))
    print("\n" + str(device_2))
    
    cable_length = calculate_cable_length(device_1, device_2)
    
    print("\nTotal Cable Length")
    print("------")
    format_length(cable_length)