# Velodyne VLP-16 capture file replay with RVIZ
Level : Too easy

__NOTICE : velodyne driver only support ros1 : ~melodic__

This Docs are targeting ROS1-ROS2 System [HOW TO INSTALL](../ROS)   
and melodic envrionment -> `source /opt/ros/melodic/setup.bash`

## Download Pcap file
[Dual Velodyne 16 pcap](https://drive.google.com/file/d/1vNA009j-tsVVqSeYRCKh_G_tkJQrHvP-/view)

## Install velodyne_points
> `sudo apt-get install ros-melodic-velodyne`

## Execute it
> `roslaunch velodyne_pointcloud VLP16_points.launch pcap:='WHERE_PCAP_LOCATED'`   
> `rviz -f velodyne`
