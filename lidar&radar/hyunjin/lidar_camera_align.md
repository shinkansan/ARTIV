<https://github.com/swyphcosmo/ros-camera-lidar-calibration>

#### Manual Calibration

```
rosrun image_view image_view image:=/sensors/camera/image_color
```

여기서 계속 에러남...
 
그래서 그냥 bag_tools install 을 찾아서 다음 커맨드를 진행하였으나 에러...

```
python change_camera_info.py peperfect_0703.orig.bag peperfect_0703.cameracalibrator.bag /usb_cam/image_raw=ost.yaml
```

에러 내용..
```
Traceback (most recent call last):
  File "change_camera_info.py", line 35, in <module>
    import roslib; roslib.load_manifest(PKG)
  File "/opt/ros/melodic/lib/python2.7/dist-packages/roslib/launcher.py", line 64, in load_manifest
    sys.path = _generate_python_path(package_name, _rospack) + sys.path
  File "/opt/ros/melodic/lib/python2.7/dist-packages/roslib/launcher.py", line 97, in _generate_python_path
    m = rospack.get_manifest(pkg)
  File "/usr/lib/python2.7/dist-packages/rospkg/rospack.py", line 171, in get_manifest
    return self._load_manifest(name)
  File "/usr/lib/python2.7/dist-packages/rospkg/rospack.py", line 215, in _load_manifest
    retval = self._manifests[name] = parse_manifest_file(self.get_path(name), self._manifest_name, rospack=self)
  File "/usr/lib/python2.7/dist-packages/rospkg/rospack.py", line 207, in get_path
    raise ResourceNotFound(name, ros_paths=self._ros_paths)
rospkg.common.ResourceNotFound: bag_tools
ROS path [0]=/opt/ros/melodic/share/ros
ROS path [1]=/opt/ros/melodic/share
```
