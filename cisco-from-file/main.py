import modules
from modules.list_com_ports import list_serial_ports
from modules.file_handling import discover_command_files
from modules.file_handling import get_commands_for_device


run = True
while run:
    print(f'''
Welcome, what would you like to configure today?
[1] Check what COM ports are available
[2] Configure a switch
[3] Configure a router
[4] Exit
''')

    choice = input("Enter your choice: ")

    for numbers in range(1,5):
        if choice == str(numbers):
            if numbers == 1: # List COM ports
                list_serial_ports()

            if numbers == 2: # Configure a switch
                for key, value in discover_command_files('switches').items():
                    print(f"[{key}] {value}")
                device_choice = input("Select the device you wish to configure: ")
                commands_for_device = get_commands_for_device('switches', device_choice)
                print(commands_for_device)


            if numbers == 3: # Configure a router
                for key, value in discover_command_files('routers').items():
                    print(f"[{key}] {value}")
                device_choice = input("Select the device you wish to configure: ")
                commands_for_device = get_commands_for_device('routers', device_choice)
                print(commands_for_device)
            
            if numbers == 4: # Exit
                run = False




