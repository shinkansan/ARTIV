## How to use annotation_tool
1. 먼저, annotation_main.py, listing.py 파일들을 다운 받는다.
2. annotation_main.py는 다음 argument를 가지고 있다.
>> 
-i : Path to the image  
-v : Path to the video  
-f : Path to the file  
-n : start the video's frame  
image, video, file path 중 하나는 입력해 주어야한다. video path 를 입력했을 시, n도 추가적으로 입력가능하다. 만약 video를 라벨링 하다 끊었을 경우 n을 통하여 frame에 접근 가능하다. (정확히 frame 수가 같지 않아서 이전 사진과 비교하며 n을 조절해주길 바란다.)
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

## Scenario
앞으로 우리 ARTIV 팀원 전체에게 차선 annotation을 맡길 예정인데요. 어떤 규칙을 따라야하는지, 어떤 경우에 어떻게 annotation해야 하는지 작성하고자 이 파트를 만들었어요. 
#### 1. 규칙 
1. video 이름을 **마음대로 바꾸면 안되요!** video가 날짜로 되어있는 것을 알 수 있는데, 이는 **고유번호**라고 생각할 수 있어요. video이름으로 directory가 생성되기 때문에 이름을 마음대로 막 바꾸었을 시 열심히 annotation한 파일들을 잃어버릴 수 있으니 유의해주세요.
2. 중간에 열심히 하고 영상을 끄고 내일 와서 이어서 하고자 할 때는 n argument를 이용하면 됩니다. culane/video/비디오 파일에 들어가서 마지막으로 저장된 이미지가 몇 번으로 저장되어있는지 확인해보세요. 그 번호가 frame 숫자라고 생각할 수 있어요. 코드에 결함이 있어서 n이 정확한 frame 수를 가리키지 않는데, directory에 저장된 사진과 코드를 실행해 띄워져 있는 창의 사진을 비교하면서 저장된 사진보다 뒤의 시점부터 annotation하면 됩니다.
3. 4개 라인에 대한 annotation을 다 했을 경우 directory를 생성해서 저장하게 만들었지만 혹시 모르니 4개의 라인에 대해 다 annotation을 마무리하고 자리에서 일어났으면 좋을 것 같네요ㅎㅎㅎ
**4. annotation은 사진 맨 밑 끝자락 부터 위로 올라가면서 찍어주세요!**
5. 최대한 차선을 삐져나가지 않도록 점을 찍어주세요. 예쁜 annotation이 필요해요ㅎㅎ 만약 점을 잘못 찍었다면 가차없이 Reset key("R" button)를 이용해주세요

#### 2. 이 상황 애매하네요.. 어떻게 annotation하면 좋을까요?

0. 차선이 저 멀리서 보이네요! 언제부터 annotation을 하면 될까요?
![Screenshot from 2020-07-07 01-15-02](https://user-images.githubusercontent.com/53460541/86615358-4f7e7d00-bfef-11ea-87e5-11b27550258f.png)  
위의 사진처럼, 차선이 밑에서부터 사진의 절반쯤부터 보이기 시작하면 사진 끝자락부터 예측해서 그려주시면 됩니다.

0. 횡단보도는 차선인가요?  
아니요! 횡단보도는 차선이 아닙니다. 사진이 횡단보도로 꽉 차 있다면, 엔터 4번쳐서 넘겨주세요

0. 물건에 가려서 차선이 안보이는데 어떻게 할까요?
![Screenshot from 2020-07-07 01-20-49](https://user-images.githubusercontent.com/53460541/86615959-1eeb1300-bff0-11ea-9d54-8f65715bdd5f.png)  
저희는 사람이기에 차선이 가려져도 차선이 어디쯤 위치에 있는지 알 수 있죠. 예측해서 그려주세요!

0. 차선이 없는데 예측해서 그린다고 했는데 이런 것도 차선이 있다고 생각하고 그리면 되나요?
![Screenshot from 2020-07-07 01-02-24](https://user-images.githubusercontent.com/53460541/86614191-966b7300-bfed-11ea-83ae-18338b8c4960.png)  
이건 차선이 없다고 할 수 있죠! 로터리도 마찬가지입니다. 사진만 보았을 때 사람도 차선이 보이지 않아서 이 차가 어디로 갈지 모른다면 그곳은 annotation하면 안됩니다!

0. 차선이 잘가다가 막 차선이 갈라지는데요??
![Screenshot from 2020-07-07 01-24-29](https://user-images.githubusercontent.com/53460541/86616313-a0db3c00-bff0-11ea-8a43-69c8e9bc3424.png)  
4개의 라인을 잘 annotation하다가 구간 점프를 해주세요. 
![Screenshot from 2020-07-07 01-26-05](https://user-images.githubusercontent.com/53460541/86616476-d849e880-bff0-11ea-8afa-f86a50ffbabc.png)  
이렇게요! 여기는 차선이 인식해야하는 구간인지 hd 맵이 인식해야하는 구간인건지.. 차선 4개만 이용하기 때문에 한 라인에서 두 라인으로 나눠지는 건 저희가 더 연구하고 이 구간을 어떻게 처리할건지 생각해봐야할 것 같네요.

0. 차가 너무 빨리 달려서 차선인지 빛인지 구분이 안가요! 어떻게 해야해요?
앞에서도 이야기했듯이 사람이 차선이라고 인식하지 못한다면 자동차도 차선이라고 인식하기 어려움이 있겠죠? 아무런 annotation 없이 pass하면 된답니다.

0. 여기 예시에 없는 경우가 나왔어요! 어떻게 하면 좋을까요?
저를 찾아주세요. 논의해봅시다ㅎㅎ   
    
    
    
-------------------------

 + 차선이 변경 되는 순간!!에는 어떻게 하는게 좋을까요 ? 예를 들면 오른쪽 차선에서 왼쪽 차선으로 변경할 때의 상황에서,,, 방법 1) 차를 가로지르는 중간 선이 생겨버리니까 중간 선은 그냥 놔두고 왼쪽 선은 left 중간선 비우고 오른쪽 선 right로 하면 되나요? 아니면 방법 2) 차가 반 이상 넘어가기 전까지는 leftleft/ left/ right 차가 반이상 넘어가고 나면  left/right/rightright 로 annotation 하는 방법 중 어떤 걸 선택하는 게 좋나요 은빈 선생님!!! 
