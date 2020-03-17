## 우분투 시작 명령어 자동 실행 매뉴얼 (abt 한영키)

  __1. 우분투 화면 좌측 하단의 'Show Applications' 클릭__
  
  __2. 보라색 아이콘의 'Startup Applications Preferences' 클릭__
  
  __3.__ Add를 누르고, __Name : `Hangul1` , command : `xmodmap -e 'remove mod1 = Alt_R'`__ 입력 후 Save
  
  __4.__ Add를 누르고, __Name : `Hangul2` , command : `xmodmap -e 'keycode 108 = Hangul'`__ 입력 후 Save
  
  __5.__ Add를 누르고, __Name : `Hangul3` , command : `xmodmap -e 'remove control = Control_R'`__ 입력 후 Save
  
  __6.__ Add를 누르고, __Name : `Hangul4` , command : `xmodmap -e 'keycode 105 = Hangul_Hanja'`__ 입력 후 Save
  
  __7.__ Add를 누르고, __Name : `Hangul5` , command : `xmodmap -pke > ~/.Xmodmap`__ 입력 후 Save
  
  __8. close하고 재부팅하면 이제 한영키를 반영구적으로 사용할 수 있습니다~!__
  
* __똑같은 원리로, 원하는 시작 프로그램이나 명령어를 구성할 수 있고 적절히 활용하면 개발 속도가 향상됩니다.__
  
  그 방법에 대한 링크도 첨부합니다.
  
  [우분투 시작 프로그램/명령어 자동 실행](https://nonnos11.tistory.com/21)
