## How to use annotation_tool
1. 먼저, annotation_main.py, listing.py 파일들을 다운 받는다.
2. annotation_main.py는 다음 argument를 가지고 있다.
>> 
-i : Path to the image  
-v : Path to the video  
-f : Path to the file  
-n : start the video's frame  
image, video, file path 중 하나는 입력해 주어야한다. video path 를 입력했을 시, n도 추가적으로 입력가능하다. 만약 video를 라벨링 하다 끊었을 경우 n을 통하여 frame에 접근 가능하다.
>>
3. annotation_main.py를 annotation 해야하는 video file을 가지고 실행시켜보자.
~~~ (bash)
python3 annotation_main.py -v (video_path)
python3 annotation_main.py -v (video_path) -n (optional_start_frame)
~~~
실행시키면 다음과 같은 화면을 볼 수 있다.  
![annotation_window](https://user-images.githubusercontent.com/53460541/85832796-af914a00-b7cb-11ea-84e0-4e77ce35949c.png)

- 현재 annotation하고 있는 # of frame을 왼쪽 상단에서 확인할 수 있고, annotation 하고 있는 점의 색깔의 label이 무엇인지 적혀있는 legend는 오른쪽 상단에서 확인할 수 있다. 바로 밑에 현재 내가 어떤 lane을 annotation 해야하는지 알 수 있다.  
- leftleft -> left -> right -> rightright 순서대로 annotation을 요구한다. 각 lane마다 annotation이 끝났을 시에 **Enter key**를 누르면 다음 lane을 annotation할 수 있다.
- annotation을 하다가 틀렸을 시에 **R key**를 누르면 그 frame에 대한 모든 것을 reset시킬 수 있다.
- annotation 된 파일들은 실행시킨 python 파일과 동일한 경로에 culane으로 생성된다. culane에 하위 폴더로 video, laneseg가 생성된다. video내엔 annotation된 파일이 있고 그 내부엔 annotation한 이미지와 txt 파일이 만들어진다. laneseg파일엔 binary image가 들어가 있다. 값이 1~4여서 눈에 보이진 않지만 확인하고 싶다면 check_seg.py를 다운 받아 다음과 같은 확인 이미지를 볼 수 있다.
![seg_image](https://user-images.githubusercontent.com/53460541/85833705-211dc800-b7cd-11ea-8a9e-e8777f0f62e3.png)
4. 이렇게 annotation이 끝났다면 listing.py를 통해 annotation한 파일들과 lane의 exist를 포함한 목록을 txt 파일 두개를 내보낼 수 있다. listing.py는 다음 argument를 가지고 있고 무조건 argument가 필요하다.
>>
-f : annotation한 파일의 경로, (culane/video/)  
-s : laneseg 파일의 경로, (culane/laneseg/)
>>
5. listing.py를 실행시켜보자.
~~~(bash)
python3 listing.py -f culane/video/ -s culane/laneseg/
~~~
그 결과로 culane내에 list파일이 만들어지고 그 안에 train.txt와 train_gt.txt가 생성된다.
![txtfile](https://user-images.githubusercontent.com/53460541/85834340-2891a100-b7ce-11ea-85ac-210a4a08b63a.png)
6. culane 파일이 culane dataset과 같이 만들어졌다.

## culane dataset의 구조
Culane  
 &nbsp;&nbsp; -> video path  
 &nbsp;&nbsp;&nbsp;&nbsp;   ->0000.jpg  
 &nbsp;&nbsp;&nbsp;&nbsp;   ->0000.txt  
 &nbsp;&nbsp; ->list  
 &nbsp;&nbsp;&nbsp;&nbsp;   ->train.txt  
 &nbsp;&nbsp;&nbsp;&nbsp;   ->train_gt.txt  
&nbsp;&nbsp;  ->laneseg  
&nbsp;&nbsp;&nbsp;&nbsp;    ->videopath  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ->0000.png  
