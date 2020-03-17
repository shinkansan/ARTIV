# 시작 프로그램으로 한글키 설정 커맨드 자동 실행시키기

  1. 우분투 화면 좌측 하단의 'Show Applications' 클릭 
  2. 보라색 아이콘의 'Startup Applications Preferences' 클릭
  3. Add를 누르고, Name은 Hangul1 command에는 `xmodmap -e 'remove mod1 = Alt_R'` 입력 후 Save
  4. Add를 누르고, Name은 Hangul2 command에는 `xmodmap -e 'keycode 108 = Hangul'` 입력 후 Save
  5. Add를 누르고, Name은 Hangul3 command에는 `xmodmap -e 'remove control = Control_R''` 입력 후 Save
  6. Add를 누르고, Name은 Hangul4 command에는 `xmodmap -e 'keycode 105 = Hangul_Hanja'` 입력 후 Save
  7. Add를 누르고, Name은 Hangul5 command에는 `xmodmap -pke > ~/.Xmodmap` 입력 후 Save
  8. close하고 재부팅하면 이제 한영키를 반영구적으로 사용할 수 있습니다~!
