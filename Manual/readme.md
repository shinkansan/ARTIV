#  기본 매뉴얼 정리
Author : Juho Song <br/>
date : 2020.03.16.

## 초보자 꿀팁 (좋은 블로그 있으면 자유롭게 추가해주세요)

* 아는 내용이면 넘어가셔도 됩니당! ~~#관준~~

  ### 1. 우분투 18.04 환경에서 한글 사용하기   
  
   우분투가 기본적으로 영어밖에 안되기에, 저또한 검색이나 깃허브 작성 등에 큰 어려움이 있었습니다.
   
  Ibus 한글판도 깔아보고, 커맨드도 고쳐보고 했지만 Ibus는 한영키를 지원하지 않아요..
  
  한글 입력에 성공하더라도 `ㅎㅏㄴㄱㅡㄹ` 처럼 깨져서 입력되었고, 한영키 맵핑과 UIM 패키지 통해 해결할 수 있었습니다!
  
  아래 링크에 상세히 설명되어 있습니다. 
  
  __아래 링크에서 마지막 단계, '한글 및 한자 키 맵핑 코드 터미널에 입력'만 하지말고 다시 여기로 돌아오세요!__
  
  [우분투 18.04 한영키 사용 및 한글 입력하기](https://pangtrue.tistory.com/70) 
  
  한글 및 한자 키 맵핑을 우분투 재실행 때마다 설정해주어야하기에, 프로그램이 시작될 때 커맨드가 자동으로 실행되도록 설정해둡시다.
  
  #### 1. 좌측 하단의 'Show Applications' 클릭 
  #### 2. 보라색 아이콘의 'Startup Applications Preferences' 클릭
  #### 3. Add를 누르고, Name은 Hangul1 command에는 `xmodmap -e 'remove mod1 = Alt_R'` 입력 후 Save
  #### 4. Add를 누르고, Name은 Hangul2 command에는 `xmodmap -e 'keycode 108 = Hangul'` 입력 후 Save
  #### 5. Add를 누르고, Name은 Hangul3 command에는 `xmodmap -e 'remove control = Control_R''` 입력 후 Save
  #### 6. Add를 누르고, Name은 Hangul4 command에는 `xmodmap -e 'keycode 105 = Hangul_Hanja'` 입력 후 Save
  #### 7. Add를 누르고, Name은 Hangul5 command에는 `xmodmap -pke > ~/.Xmodmap` 입력 후 Save
  #### 8. close하고 재부팅하면 이제 한영키를 반영구적으로 사용할 수 있습니다~!
 
 
  ### 2. 사용자 비밀번호를 쉽게쉽게
  
   정말 사소할 수도 있지만, 우분투로 코딩 할 때 sudo를 많이 사용하고 그 때마다 사용자 비밀번호를 입력해야합니다.~~개귀찮음~~
   
  처음 설정했던 복잡한 비밀번호 대신 간단한 사용자 비밀번호를 통해 개발 속도를 조금이나마 향상시킬수 있어요 ㅎㅎ..
  
  
  `passwd 계정명`: 기존 비밀번호 입력 후 새 비밀번호 입력
  
  ### 3. 리눅스 기초 명령어 이해
  
   각 명령어의 자세한 사용 방법을 알고 싶다면, '명령어 --help' 코드를 통해 바로바로 알아 볼 수 있지만, 
  우분투를 사용하기 전 기초 명령어의 원리와 뜻을 알고 시작하면 큰 도움이 됩니다.
  가독성 좋은 링크를 첨부합니다.
  
  [리눅스 기본 명령어/자주 쓰는 명령어](https://itholic.github.io/linux-basic-command/)
  
  [리눅스 명령어 모음 Best 50](https://dora-guide.com/linux-commands/)
  
  ### 4. 마크다운 문법 
  
## RQT 매뉴얼

  to be continue...
