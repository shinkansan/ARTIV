#!/bin/bash

cd /etc/udev/rules.d
sudo echo 'ACTION=="add", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="AK05MK9T", MODE = "0777", SYMLINK+="artivIMU"' > 50-usb-imu.rules

sudo echo 'ACTION=="add", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A9B69WM5", MODE = "0777", SYMLINK+="artivGPS"' > 51-usb-gps.rules

#udevadm control --reload-rules && udevadm trigger
