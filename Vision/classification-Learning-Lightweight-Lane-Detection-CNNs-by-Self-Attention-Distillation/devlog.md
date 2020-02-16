# Learning Lightweight Lane Detection CNNs by Self Attention Distillation
[github](https://github.com/cardwing/Codes-for-Lane-Detection) <br/>
[sota paper](https://arxiv.org/abs/1908.00821)

Author : Eunbin Seo <br/>
Date : 2020.02.16. ~ 2020.02.17.

we follow the [github](https://github.com/cardwing/Codes-for-Lane-Detection/tree/master/ERFNet-CULane-PyTorch). So, we need to download the whole dataset about CULane at this [link](https://drive.google.com/drive/folders/1mSLgwVTiaUMAb4AVOWwlCD5JcWdrwpvu).<br/>

## Problems & How to solve the problems
1. No argument --npb
--> we can solve it by erasing this line in test_erfnet.sh.
~~~ bash
--npb\
~~~

2. RuntimeError: cuda runtime error (38) <br/>
--> we can solve it by adding only two lines. <br/>
I got help on this [link](https://www.tensorflow.org/guide/gpu?hl=ko)
~~~ python
import tensorflow as tfs

tfs.config.set_soft_device_placement(True)
tfs.debugging.set_log_device_placement(True)
~~~

3. AttributeError: 'NoneType' object has no attribute 'astype' <br/>
This error happens at cv2.imread(os.path.join(~)) in test_erfnet.py <br/>
--> This error happens because the path is wrong. We have to compare "ERNet_ROOT/list/test_img.txt" file with "os.path.join(self.img_path, self.img_list[idx])".

## Today's outcome
### lane detection
<img width="340" src=".Vision/classification-Learning-Lightweight-Lane-Detection-CNNs-by-Self-Attention-Distillation/img/lanedetection.png"> 






