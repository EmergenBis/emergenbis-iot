import requests
import json

state = True
zone_confirmation = True

print("EmergenBIS traps")

while state:
    while zone_confirmation:
        print("Which trap do you want to check? \nNorth, South, East, West, Parking, Cafeteria")
        zone = input()
        zone = zone.lower()

        if zone == 'north' or zone == 'south' or zone == 'east' or zone == 'west' or zone == 'parking' or zone == 'cafeteria':
            zone_confirmation = False
        else:
            print("Everything seems to be in order")
            
            print("Would you like to check other traps? [Y/N]")
            _state = input()
            _state = _state.lower()

            if _state == 'y':
                zone_confirmation = True
                print("\n\n\nEmergenBIS traps")
            else:
                zone_confirmation=False
                state=False

    print("Has the trap {zone} been active for some minutes? \n'Yes/No'")
    active = input()

    if active == 'Yes':
        state = "The trap {zone} is active, an inspection is adviced"
    else:
        state = "The trap {zone} is not active"

        print("Would you like to check other traps? [Y/N]")
        _state = input()
        _state = _state.lower()

        if _state == 'y':
            zone_confirmation = False
            print("\n\n\nEmergenBIS traps")
        else:
            state=False

    REQUEST_URL = f"http://127.0.0.1:5000/?trap={zone}&active={state}"
    _request = requests.get(REQUEST_URL)

    print(_request.text)
    data = json.loads(_request.text)

    print("Would you like to check other traps? [Y/N]")
    _state = input()
    _state = _state.lower()

    if _state == 'y':
        zone_confirmation = False
        print("\n\n\nEmergenBIS traps")
    else:
        state=False
