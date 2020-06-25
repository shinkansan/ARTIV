# How to train(to detect our custom objects)
Author: 이  구
date: 2020.06.25
> reference: https://github.com/AlexeyAB/darknet

## Training Yolo v4

0. pre-trained weights 파일을 다운 받는다.[링크](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137)    
1. yolov4-custom.cgf 파일을 복사한 후,아래와 같이 수정한다.(링크 들어가면 몇번째 줄 고쳐야하는지 나와있음)   
    batch=64   
    subdivisions=16   
    max_batches= classes*2000 (but, training image의 수보다 작으면 안됨)   
    steps = max_batches * 0.8 or max_batches * 0.9   
    width = 416 (또는, 32의 배수)   
    height = 416 (또는, 32의 배수)   
    classes = # of class (610, 696, 783 번째 줄)   
    filters = (classes + 5) * 3 (603, 689, 776 번째 줄)   
    Gaussian_yolo layer를 사용하면,   
    filters = (classes + 9) * 3 (604, 696, 789 번째 줄)   
    
2. build\darknet\x64\data\ 폴더에 obj.names 파일을 만든다. 각 line은 object의 이름   

3. build\darknet\x64\data\ 폴더에 obj.data 파일을 만든다.   
  (ex)
  classes= 2   
  train  = data/train.txt   
  valid  = data/test.txt   
  names = data/obj.names   
  backup = backup/ 
  
4. build\darknet\x64\data\obj\ 폴더에 image file을 놓는다.   

5. labeling tool [링크](https://github.com/AlexeyAB/Yolo_mark)
   위의 프로그램은, 각 jpg 파일마다 txt 파일을 만든다.   
  
    Where:   
    <object-class> - integer object number from 0 to (classes-1)   
    <x_center> <y_center> <width> <height> - float values relative to width and height of image, it can be equal from (0.0 to 1.0]   
    for example: <x> = <absolute_x> / <image_width> or <height> = <absolute_height> / <image_height>   
    atention: <x_center> <y_center> - are center of rectangle (are not top-left corner)   
 
6. train.txt 파일을 만든다. 각 line은 object image 파일의 이름이다.   
  (ex)   
  data/obj/img1.jpg   
  data/obj/img2.jpg   
  data/obj/img3.jpg   
  
7. convolutional layer를 위한 pre-trained weights를 다운받는다. [링크](https://pjreddie.com/media/files/darknet53.conv.74)   
(0에서 받은거랑 뭐가 다르지?)

8. To train on Linux use command:   
```(bash)
./darknet detector train data/obj.data yolo-obj.cfg yolov4.conv.137   
```
  (file yolo-obj_last.weights will be saved to the build\darknet\x64\backup\ for each 100 iterations)   
  (file yolo-obj_xxxx.weights will be saved to the build\darknet\x64\backup\ for each 1000 iterations)   
  (to see the mAP & Loss-chart during training on remote server without GUI, use command darknet.exe detector train data/obj.data yolo-obj.cfg yolov4.conv.137 -dont_show -mjpeg_port 8090 -map then open URL http://ip-address:8090 in Chrome/Firefox browser)   

9. 학습이 끝나면, 결과 파일인  yolo-obj_final.weights 는 다음 경로에 있다. path build\darknet\x64\backup\   

   After each 100 iterations you can stop and later start training from this point. For example, after 2000 iterations you can stop training, and later just start training using:   
./darknet detector train data/obj.data yolo-obj.cfg backup\yolo-obj_2000.weights   


**Note: If during training you see nan values for avg (loss) field - then training goes wrong, but if nan is in some other lines - then training goes well.**   

**Note: If you changed width= or height= in your cfg-file, then new width and height must be divisible by 32.**   

**Note: After training use such command for detection: darknet.exe detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights**   

**Note: if error Out of memory occurs then in .cfg-file you should increase subdivisions=16, 32 or 64: link**   

