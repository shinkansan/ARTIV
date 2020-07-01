# python-imu380
Python driver for Aceinna 380 Series Inertial Products.  Includes local and cloud file logging, and WebSocket server

### pip install:
pyserial  
tornado  
azure-storage-blob

See demo.py for example usage as basic driver
Run server_ui.py to run as a server for Aceinna Navigation Studio (ANS) web app

### imu380.py
This is core driver for the DMU38x family of IMU's.  It can do the following functions:

- automatically discover a DMU38x connected to serial port  TODO: make faster and more reliable
- log data to local file or azure cloud TODO: add system for using user specific access_token and storage location
- parse various ouput packets:  TODO: complete and test all packet types, as well as custom user packet from OpenIMU
- read/write and get/set EEPROM fields
- upgrade firmware of device
- run as a thread in websocket server see below

MAJOR current issues are connection realiability and switching in and out of stream mode in order to reliably read/get and write/set EEPROM fields.

### server.py
Create a web socket server on wss://localhost:8000 that bridges ANS to a locally running imu380 serial port driver.  Places imu380 driver in a thread

- automatically sends data out on wss://localhost:8000 every 33mS encoding packet as JSON.  TODO: consider if packet should be wrapped standard message such as { cmd: {} data: {} err: {} }
- receives messages via on_message handler from ANS currently messages are - status, start_log, stop_log and cmd.  TODO: extend to include update firmware and consider wether should be wrapped in standard message such as   { cmd: {} data: {} err: {} }


### server_ui.py

This is simple UI to control server.py.  Uses Tkinter to build a UI and allow starting and stopping of the server.py dameon. Automatically determines if it is already running.

TODO: extend to show some status information
TODO: use pyinstaller to build a reliable installer executable distribution for MAC and Windows


### file_storage.py / aceina_storage.py

These file store parsed packet data to CSV either locally or on Azure cloud.  Uses Azure Python SDK to write to Azure.  TODO: consider support allowing custom file name
TODO: log meta data like NAV-VIEW does - serial number etc
TODO: use customer access_token to write to customer specific sub-space on azure