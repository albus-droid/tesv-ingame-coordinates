#!/usr/bin/env python
"""
DISCLAIMER: Use this script only for legal and educational purposes.
Ensure you have permission to access the process memory you intend to read.
"""

import sys
import time
import json
import pymem
import pymem.process

# Offsets for SkyrimSE.exe:
# Tamriel value (4-byte integer): SkyrimSE.exe+3389E14
# Y coordinate (float): SkyrimSE.exe+338A544
# X coordinate (float): SkyrimSE.exe+338A540
TAMRIEL_OFFSET = 0x3196DE8
Y_OFFSET = 0x338A544
X_OFFSET = 0x338A540

# Process name
PROCESS_NAME = "SkyrimSE.exe"

def main():
    try:
        # Attach to the process and get the base address
        pm = pymem.Pymem(PROCESS_NAME)
        module = pymem.process.module_from_name(pm.process_handle, PROCESS_NAME)
        base_address = module.lpBaseOfDll
    except Exception as e:
        print("Failed to attach to the process:", e)
        return

    while True:
        try:
            # Read x and y coordinates as floats
            x_value = pm.read_float(base_address + X_OFFSET)
            y_value = pm.read_float(base_address + Y_OFFSET)
            # Read tamriel as a 4-byte integer
            tamriel_value = pm.read_int(base_address + TAMRIEL_OFFSET)
            
            # Create a JSON object with the data and a timestamp
            data = {
                "timestamp": int(time.time()), "x": round(x_value,2), "y": round(y_value,2), "tamriel": tamriel_value
            }
            print(json.dumps(data))
            sys.stdout.flush()
        except Exception as e:
            print("An error occurred during memory reading:", e)
        time.sleep(1)  # Pause for 1 second

if __name__ == "__main__":
    main()

