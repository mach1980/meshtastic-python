"""Simple program to demo show how to remotly set a parameter without reading status first.
   To run: python examples/blind_set.py
"""

import sys

import meshtastic
import meshtastic.serial_interface

# simple arg check
if len(sys.argv) != 1:
    print(f"usage: {sys.argv[0]}")
    print("Print the hardware model for the local node.")
    sys.exit(3)

iface = meshtastic.serial_interface.SerialInterface()
if iface.nodes:
    for n in iface.nodes.values():
        if n["num"] == iface.myInfo.my_node_num:
            print(n["user"]["hwModel"])
iface.close()
