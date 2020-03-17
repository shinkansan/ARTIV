# 시작 프로그램으로 한글키 설정 커맨드 자동 실행시키기

  __1. 우분투 화면 좌측 하단의 'Show Applications' 클릭__
  
  __2. 보라색 아이콘의 'Startup Applications Preferences' 클릭__
  
  __3.__ Add를 누르고, Name : `Hangul1` , command : `xmodmap -e 'remove mod1 = Alt_R'` 입력 후 Save
  
  __4.__ Add를 누르고, Name : `Hangul2` , command : `xmodmap -e 'keycode 108 = Hangul'` 입력 후 Save
  
  __5.__ Add를 누르고, Name : `Hangul3` , command : `xmodmap -e 'remove control = Control_R''` 입력 후 Save
  
  __6.__ Add를 누르고, Name : `Hangul4` , command : `xmodmap -e 'keycode 105 = Hangul_Hanja'` 입력 후 Save
  
  __7.__ Add를 누르고, Name : `Hangul5` , command : `xmodmap -pke > ~/.Xmodmap` 입력 후 Save
  
  __8. close하고 재부팅하면 이제 한영키를 반영구적으로 사용할 수 있습니다~!__
