# Key Points Estimation and Point Instance Segmentation Approach for Lane Detection
[github](
https://github.com/MaybeShewill-CV/lanenet-lane-detection) <br/>
[sota paper](https://arxiv.org/abs/1802.05591)

Author : Eunbin Seo <br/>
Date : 2020.05.21.

we follow the [github](https://github.com/MaybeShewill-CV/lanenet-lane-detection). 

### how to run
영상을 먹는 코드는 /LaneNet/test_lanenet.py 있음!! <br/>
command this in lanenet-lane-detection-master folder
~~~(bash)
python3 tools/test_lanenet.py --weights_path ./model/tusimple_lanenet_vgg/tusimple_lanenet_vgg.ckpt --image_path /home/dgist/Desktop/data/5_14_12_49.avi
~~~

#### But we have to solve some problem....
--> 직접 찍은 영상을 돌려본 결과인데, 끝쪽의 lane과 연석을 인식하는데 어려움이 있다.

## Evaluation
|  | fps |Memory-Usage|Power(Usage/Cap)|Volatile GPU-Util|
|:--------:|:--------:|:--------:|:--------:|:--------:|
| PINet | 약 5~6 fps | 약 1400 MB | 64W/250W | 6% |
| lanenet | 약 10 fps | 약 7511 MB | 100W/250W | 20% |

inference time: 약 0.02s
postprocessing time: 약 0.08s

## To do
1. post processing 확인 (morphological etc..)
2. prob line 생성
3. 성능 및 메모리 사용 개선 필요
