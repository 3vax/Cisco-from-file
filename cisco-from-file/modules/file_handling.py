'''
This module is respoonsible for discovering command files from a specified
directory and then returning a dictionary mapping a file to an index number
so that they can be easily referenced later.
'''
import os
import time
import serial
from tqdm import tqdm
from pathlib import Path
from typing import List, Optional, Dict, Any

parent_directory = Path(__file__).parent.parent
router_directory = parent_directory / 'data' / 'routers'
switch_directory = parent_directory / 'data' / 'switches'
command_files = {}

def discover_command_files(device_type = 'routers'):
    files = {}
    if device_type == 'routers':
        for index, file in enumerate(os.listdir(router_directory), start=1):
            if file.endswith('txt'):
                files[index] = file
    
    elif device_type == 'switches':
        for index, file in enumerate(os.listdir(switch_directory), start=1):
            if file.endswith('txt'):
                files[index] = file   

    return files


def get_commands_for_device(device_type, key_number):
    if device_type == 'routers':
        for key, value in discover_command_files('routers').items():
            if str(key) == str(key_number):
                with open(router_directory/value) as file:
                    commands = file.readlines()
    
    elif device_type == 'switches':
        for key, value in discover_command_files('switches').items():
            if str(key) == str(key_number):
                with open(switch_directory/value) as file:
                    commands = file.readlines()

    serial_port = input("Enter the COM port (e.g., COM4): ").strip()
    ser = serial.Serial(serial_port)  # open serial port
    print(f'The serial port used is {ser.name}')

    for command in commands:
        formatted_command = command.format()
        ser.write(formatted_command.encode())
        if "crypto key generate rsa" in command.strip():
            time.sleep(1) # wait for the device to respond                print(ser.read(ser.in_waiting or 1).decode())
            for i in tqdm(range(40), desc="Waiting for key generation"):
                    time.sleep(0.25)
            print(ser.read(ser.in_waiting or 1).decode())
        else:
            time.sleep(1.5)
            print(ser.read(ser.in_waiting or 1).decode()) # read all characters in buffer
    ser.close() # close port

if __name__ == "__main__":
    print(get_commands_for_device('routers', '4'))
#    print(get_commands_for_device('switches', '2'))
