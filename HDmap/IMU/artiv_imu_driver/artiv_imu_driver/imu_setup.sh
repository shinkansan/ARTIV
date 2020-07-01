#!/bin/bash

cd /etc/udev/rules.d
sudo echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE = "0777"' > 50-usb-imu.rules

#udevadm control --reload-rules && udevadm trigger
