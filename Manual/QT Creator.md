# QT Creator 매뉴얼

* ui 구축을 쉽게하는 방법 with ROS (ubuntu 18.04 환경)

  ##
  ### 1. QT Creator 설치
  
  터미널 창을 키고 아래 코드를 순서대로 입력한다.
  
  `sudo apt-get install qtcreator`
  
  `sudo apt-get install build-essential libgl1-mesa-dev`
  
  [설치 사이트](https://www.qt.io/download)
  
  위의 사이트에서 Downloads for open source users 항목을 찾아 다운로드를 진행한다.
  
  다시 터미널 창으로 돌아와, 아래 코드를 순서대로 입력한다.
  
  `cd ~/Downloads`
  
  `chmod a+x qt-unified-linux-x64-3.2.2-online.run`
  
  `sudo ./qt-unified-linux-x64-3.2.2-online.run`
  
  **!주의사항!** 작성일 기준 qt 설치파일 최신버전이 `qt-unified-linux-x64-3.2.2-online.run`인데,
  
  최신버전은 지속적으로 업데이트될 것이므로, 아래 사진과 같이 버전을 확인하여 위의 코드에서 파일에 해당하는 부분을 고쳐주어야 정상적으로 실행된다.
  
  ![qt_manual1](https://user-images.githubusercontent.com/59792475/77538998-fa0cdd00-6ee3-11ea-9d2e-5f933354d8e3.png)
  
  계정을 만들고 실행하면, tutorial 창을 찾을 수 있다. 목적에 맞는 tutorial을 참고하자.
  
  개인적으로, 4번째 튜토리얼, **Creating a Qt Widget Based Application**이 가장 큰 도움이 되었다.
  
  ![Screenshot from 2020-03-25 22-04-45](https://user-images.githubusercontent.com/59792475/77539458-c088a180-6ee4-11ea-9090-33b406d0f5c9.png)
