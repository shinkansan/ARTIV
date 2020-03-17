# Vision팀 특화 딥러닝 집중 교육
Author : Gwanjun Shin

2Weeks 계획입니다.

방식 : 
  1. 기반 웹사이트 팁 제공
  2. 제공된 페이지를 기반으로 아래 커리큘럼의 답을 써오기
  3. 각 커리큘럼별 폴더를 만들어서 md 파일 or pdf로 정리해서 업로드
  
> :warning: GPU가 없는 노트북이어도, MNIST 같은 간단한 예제를 연산이 가능하니, 그냥 돌려보것에 의미를 두고 모든 코드 실습에 참여 할 것.

> [Google Colab](https://zzsza.github.io/data/2018/08/30/google-colab/)

#### :loudspeaker: 신관준의 DL101 PPT 자료 (LIVE로 만들고 있음, 실시간으로 진행상황이 업데이트됩니다.) [링크](https://dgistackr-my.sharepoint.com/:p:/g/personal/shinkansan_dgist_ac_kr/EWgcbM-pK89HguSDCcR0b_YBT2YrO-JyVmdz0wE0SqniQQ?e=TvGBHe)
> :shipit: 외부 유출 삼가해주세요~

## 기본 커리큘럼

1. 프레임워크 (케라스, 파이토치) 공부   
  1.1 범위는 CNN을 이용한 검출 모델 설계, 학습, 전처리   
  1.2 딥러닝의 기본 지식   
  1.3 배치사이즈 (까먹었다면 다시)   ==> **위에 까지는 Framework 설명에서 동시에 다룸**   
  1.4 가중치 , pretrained-weights (transfer learning) 개념   ==> **학습 테크닉 설명**   
     
2. 이미지 전처리와 학습 데이터셋 만들기   
  2.1 그냥 사진으로 저장하기 ==> 사진 나란히 불러와서 전처리?!   
  2.2 전처리한 사진을 한 파일에다가 압축해서 담아보기 .npy, .tfrecord, csv 등   
  2.3 전처리에서 생각해 볼 것들.   
  
3. 네트워크에서 많이 사용하는 용어 알기 [encyclopedia.md](encyclopedia.md)

4. HW -> GPU 성능 관계와 최적화를 위한 간단한 개념 정리   
  1. [모델 경량화](model-optimization)
5. 모델 Deploy와 안정적인 사용 방법 예시

## 심화 실습
1. 논문들을 보면서 각 논문의 특징점 및 자체 구현
  1.1 Related work에 나온 논문 네트워크 구현과 주요 모듈 확인
2. 두가지 논문의 기능을 하나의 네트워크로 특징 합쳐보기
  2.1 2가지 특징을 합친 네트워크 만들기.
