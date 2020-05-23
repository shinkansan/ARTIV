# PolyLaneNet: Lane Estimation via Deep Polynomial Regression
[github](
https://github.com/lucastabelini/PolyLaneNet) <br/>
[sota paper](https://arxiv.org/pdf/2004.10924.pdf)

Author : Eunbin Seo <br/>
Date : 2020.05.23.

we follow the [github](https://github.com/MaybeShewill-CV/lanenet-lane-detection). 

### how to run
먼저 training을 시켜 pt file을 만들어줍니다<br/>
command this in PolyLaneNet-master folder
~~~(bash)
python3 train.py --exp_name tusimple --cfg config.yaml
~~~
epoch 2695으로 돌려줍니다.

#### But we have to solve some problem....
--> 수치적 성능만 나오고 lane이 그려진 이미지가 안보인다... 영상으로 넣고도 돌려봐야한다..

## Evaluation
### training
|  | fps |Memory-Usage|Power(Usage/Cap)|Volatile GPU-Util|
|:--------:|:--------:|:--------:|:--------:|:--------:|
| PolyLaneNet | 믿을 수 없음 | 약 8624MB | 227W/250W | 95~100% |

### test
|  | fps |Memory-Usage|Power(Usage/Cap)|Volatile GPU-Util|
|:--------:|:--------:|:--------:|:--------:|:--------:|
| PolyLaneNet |  | 약 MB | W/250W | % |

inference time:
postprocessing time: 

## To do
1. 
2. 
3.
