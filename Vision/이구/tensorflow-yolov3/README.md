# How can use tensorflow-yolov3 with FLIR camera
Author : 이  구 <br/>
 > reference: https://github.com/YunYang1994/tensorflow-yolov3
 
## Setting
Camera: FLIR Grasshopper3 USB3 (GS3-U3-32S4M-C)
tensorflow-gpu:1.14.0
CUDA: 10.0
cudnn: 7.6.5

## Use
~~~bash
$ git clone https://github.com/YunYang1994/tensorflow-yolov3.git
$ cd tensorflow-yolov3
$ pip install -r ./docs/requirements.txt
$ cd checkpoint
$ wget https://github.com/YunYang1994/tensorflow-yolov3/releases/download/v1.0/yolov3_coco.tar.gz
$ tar -xvf yolov3_coco.tar.gz
$ cd ..
$ python convert_weight.py
$ python freeze_graph.py
$ python3 tensorflow_YOLO_FLIR.py
~~~

## Memory management
tensorflow는 GPU의 전체 memory를 미리 할당한다. per_process_gpu_memory_fraction, allow_growth 옵션을 이용하여 해결할 수 있다.

1. 프로세스가 전체 GPU memory 중, 40%만 사용할 수 있도록 설정
~~~python3
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
sess = tf.Session(config=config) as sess:
~~~

2. 프로세스가 전체 GPU memory를 할당하지 않도록 설정
~~~python3
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess= tf.Session(config=config):
~~~

## Evaluation with original yolo(using darknet)
|  | fps |Memory-Usage|Power(Usage/Cap)|Volatile GPU-Util|
|:--------:|:--------:|:--------:|:--------:|:--------:|
| tensorflow-yolov3 | 측정 필요 | 약 8809 MB | 125W/250W | 35% |
| tensorflow-yolov3(after memory setting)| 측정 필요 | 약 4683 MB | 177W/250W | 29% |
| darknet-yolov3 | 43 fps | 약 1024 MB | 220W/250W | 50% |
| darknet-yolov4 | 35 fps | 약 2048 MB | 262W/250W | 81% |
