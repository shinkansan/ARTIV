# Mask RCNN Guide
Author : Eunbin Seo<br/>
Date : 2020.02.05.

## First thing that you have to do
First, install the tensorflow and keras. <br/>
You can install them this link. [Link](Vision/Installation_for_Vision.md)

## Setting for Mask RCNN
You have to follow the link. [Link](https://github.com/matterport/Mask_RCNN) <br/>
And, Find the Installation part.<br/>

I modifed the existing method.
1. Download first pre-trained COCO weights (mask_rcnn_coco.h5) from the [releases page](https://github.com/matterport/Mask_RCNN/releases).
It takes a long time to download because of its large capacity.
2. Clone that repository.
3. Install dependencies.
Go into requirements.txt file.<br/>
Then, __you have to erase tensorflow>=1.3.0 and keras>=2.0.8.<br/>
We already install them in First thing that you have to do part__ <br/>
After the modifying, type the command.
~~~ bash
pip install -r requirements.txt
~~~
4. Run setup from the repository root directory
~~~ bash
python3 setup.py install
~~~

## Execute example code
1. Download all files in this directory(ARTIV/Vision/Mask RCNN/Required files).
2. Execute the test-mrcnn.py <br/>
If you create the virtual environment, you execute the test-mrcnn.py in the virtual environment.<br/>
If it works well, window(like test result.jpg) will be opened.
3. Turn on the car simulation.(we use the lgvsl. If you don't know turning on lgvsl, you can follow the guide in directory(ARTIV/lgvsl-simulator)) 
4. Execute mrcnn.py and enjoy mask-rcnn with simulator in real time!! :)
