# Cisco-from-file

**Cisco-from-file** is a lightweight tool designed to configure Cisco devices by reading CLI commands from a text file and sending them directly to the device.  
This makes it easy to automate configuration tasks, avoid manual typing, and keep your desired configurations version-controlled.

## Purpose

- Automate Cisco router/switch configuration using command files.  
- Eliminate repetitive copy/paste during deployments or recovery.  
- Store and version your network configuration files in Git.  
- Ensure consistent “desired state” across devices.

## Requirements

- Python (version specified in `requirements.txt`)  
- Network access to the Cisco device (SSH/Telnet depending on implementation)

## Installation

```bash
git clone https://github.com/3vax/Cisco-from-file.git
cd Cisco-from-file
pip install -r requirements.txt
```

## Usage
1. Create a text file (for example commands.txt) containing the Cisco CLI commands you want to run — one per line.

2. Add the command file to the correct folder depending on device type.

3. Connect to the device with a serial cable.

4. Run the script and choose correct selection from menu and provide what com port to use.

5. The script will connect to the device, execute the commands in order.

Tip: Always test your command file in a lab environment before applying changes to production.

## Project Structure
```
.
├── cisco-from-file        # Project folder/
│   ├── data                 # Folder data used/
│   │   ├── routers            # Command folder for routers
│   │   └── switches           # Command folder for switches
│   ├── modules/             # Modules used in main.py
│   └── main.py              # Main script
├── requirements.txt       # Python dependencies
├── LICENSE                # GPL-3.0 license
└── README.md              # Documentation (this file)
```
## Potential Improvements

- Support for running the same command file on multiple devices (batch mode)

- Logging system showing success/error per command

- Encrypted storage of secrets (passwords, tokens, etc.)

- “Dry run” mode to validate syntax without applying changes

## License

This project is licensed under the GPL-3.0 License.
See the full license text in the repository.
