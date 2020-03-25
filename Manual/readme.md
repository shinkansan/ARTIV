#  매뉴얼 정리
Author : Juho Song <br/>
date : 2020.03.16.

## 초보자용 개발 매뉴얼 (자유롭게 추가해주세요)

* 개발 속도 향상에 초점을 두고 작성한 팁으로, 아는 내용이면 넘어가셔도 됩니당! ~~#관준~~

  ##
  ### 1. 우분투 18.04 환경에서 한글 사용하기   
  
  우분투가 기본적으로 영어밖에 안되기에, 저또한 검색이나 깃허브 작성 등에 큰 어려움이 있었습니다.
   
  Ibus 한글판도 깔아보고, 커맨드도 고쳐보고 했지만 Ibus는 한영키를 지원하지 않아요..
  
  한글 입력에 성공하더라도 __`ㅎㅏㄴㄱㅡㄹ`__ 처럼 깨져서 입력되네? ㅋ
  
  결국, UIM 패키지와 시작 명령어를 통한 한영키 맵핑을 통해 해결할 수 있었습니다!
  
  __아래 링크에서 마지막 단계(특정 코드 터미널에 입력) 전까지만 하고 다시 여기로 돌아오세요!__
  
  __[우분투 18.04 한영키 사용 및 한글 입력하기](https://pangtrue.tistory.com/70)__
  
  #### 일련의 과정을 끝냈다면, 아래 매뉴얼을 참고하여 프로그램이 시작될 때 커맨드가 자동으로 실행되도록 설정해줍시다.
  
  __[우분투 시작 명령어 자동 실행 매뉴얼 (abt 한영키)](https://github.com/shinkansan/ARTIV/blob/master/Manual/Startup_Setting_Hangul.md)__
  
  ##
  ### 2. 사용자 비밀번호를 쉽게쉽게
  
   정말 사소할 수도 있지만, 우분투로 코딩 할 때 sudo를 많이 사용하고 그 때마다 사용자 비밀번호를 입력해야합니다.~~개귀찮음~~
   
  처음 설정했던 복잡한 비밀번호 대신 간단한 사용자 비밀번호를 통해 개발 속도를 조금이나마 향상시킬수 있어요 ㅎㅎ..
  
  
  __`passwd 계정명`: 기존 비밀번호 입력 후 새 비밀번호 입력__
  
  ##
  ### 3. 리눅스 기초 명령어 이해
  
   각 명령어의 자세한 사용 방법을 알고 싶다면, `명령어 --help` 코드를 통해 바로바로 알아 볼 수 있지만, 
   
  우분투를 사용하기 전 기초 명령어의 원리와 뜻을 알고 시작하면 큰 도움이 됩니다.
  
  가독성 좋은 링크를 첨부합니다.
  
  __[리눅스 기본 명령어/자주 쓰는 명령어](https://itholic.github.io/linux-basic-command/)__
  
  __[리눅스 명령어 모음 Best 50](https://dora-guide.com/linux-commands/)__
  
  ##
  ### 4. 마크다운 문법 (github 디렉토리 작성법)
  
  마크다운은 우리가 사용하는 깃허브에 사용되는 언어입니다. 미리미리 익혀두면 팀별 코드나 자료를 공유하기 수월하겠죠?
  
  **_우리 깃헙에 업로드된 자료들을 출력화면과 에딧 파일을 비교하면서 공부하니까 비교적 쉽게 익힐 수 있었어욥!_**
  
  가독성 좋은 링크를 첨부합니다.
  
  __[마크다운 사용법](https://gist.github.com/ihoneymon/652be052a0727ad59601)__
  
  ##
  ### 5. To be continued... 
  
  ##

## [rostopic delay 매뉴얼](https://github.com/shinkansan/ARTIV/blob/master/Manual/rostopic_delay.md)

* ros topic을 주고받는 코딩을 할 때 알 수 없는 lack이 걸려서 통신이나 streaming이 원활하지 않을 경우,

delay가 있는지 확인하는 방법에 대한 매뉴얼입니다. __(abt image, video, point clouds)__

## [ROS RQT, RViz 매뉴얼](https://github.com/shinkansan/ARTIV/blob/master/Manual/RQT.md)

## [QT Creator 매뉴얼](https://github.com/shinkansan/ARTIV/blob/master/Manual/QT%20Creator.md)
