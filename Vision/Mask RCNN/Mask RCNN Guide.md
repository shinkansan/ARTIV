# Mask RCNN Guide

## First thing that you have to do
First, install the tensorflow and keras. <br/>
You can install them this link. [Link](Vision/Installation_for_Vision.md)

## Installation 
You have to follow the link. [Link](https://github.com/matterport/Mask_RCNN) <br/>
And, Find the Installation part.<br/>

I modifed the existing method.
1. Download first pre-trained COCO weights (mask_rcnn_coco.h5) from the [releases page](https://github.com/matterport/Mask_RCNN/releases).
It takes a long time to download because of its large capacity.
2. Clone that repository.
3. Install dependencies.
Go into requirements.txt file.<br/>
Then, __you have to erase tensorflow>=1.3.0 and keras>=2.0.8. We already install them in First thing that you have to do part__
After the modifying, type the command.
~~~ bash
pip install -r requirements.txt
~~~
4. Run setup from the repository root directory
~~~ bash
python3 setup.py install
~~~
