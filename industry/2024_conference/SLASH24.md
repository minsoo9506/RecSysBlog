- 갯수가 많지 않지만 재밌고 유용하다.
- 20분이라 듣기 딱 좋다.
- 영상에서 발표자가 너무 크다. 녹음된 음성이 아쉬운 경우가 있다.

# 추천
## [토스ㅣSLASH 24 - 기반 데이터가 부족해도 OK! 커머스 추천 시스템 제작기](https://www.youtube.com/watch?v=LAD6LYnkPsA&list=PL1DJtS1Hv1PiGXmgruP1_gM2TSvQiOsFL&index=31)
#### 모델링
- 토스 쇼핑 서비스 2023.03 시작
- 초기 설계 시 고려해야할 점
  - 빠르게 증가하는 유저, 아이템
  - 추천시스템을 위한 유저 피드백 데이터, 리소스, 시간 부족
- SO?
  - cold-start 문제 고려
  - 빠르게 모델이 적용해야함
  - 유의한 피드백 데이터를 잘 모을 수 있어야함
- MAB 적용
  - 성연령 세그먼트 (준개인화)
  - 최근 7일 데이터 사용에서 배치 (Batched Sliding Time Window)
  - (late feedback 일 때 효과적인) Pessimistic Thompson Sampling (prior 를 Beta(1,99))
- MAB 개선
  - Ranking system 효율 증가
    - arm 이 증가 -> thompson sampling 수렴 속도 하락, redis 에 저장해야 할 데이터 증가
    - 그래서 2개의 layer 구조 사용 (filtering, ranking layer)
    - 아이템마다 cvr (conversion / impression) 을 기준으로 ranking 을 했는데 cvr은 노출규모를 고려하지 못함 -> lower confidence bound 를 사용 -> 그래서 LCB 가 높은 아이템을 선택 + (신규상품을 위해) 일부 무작위 추출
  - cohort 체계 고도화
    - warm start user: 유저 임베딩을 만들어서 clustering 해서 m 개의 cohort
    - cold start user: (마이크 이슈있음) 아마 warm start user 들을 성연령 세그먼트로 나누고 이를 이용한다는 것 같음
- 유저 임베딩 모델
  - two-tower model 형태 이용
  - 훈련
    - 일반적으로 positive label 은 구매한 아이템, negative 는 봤지만 구매하지 않은 아이템
    - continual learning 으로 과거 모델의 weight 를 이용해서 매일 학습 진행
    - issue
      - 복잡하고 노이지한 imp data
      - popularity bias
    - solution
      - construct negative label by mixed random sampling
        - uniform random sampling (recall 증가) 과 in-batch random sampling (diversity 증가) 을 섞어서 진행
      - use sampled softmax loss with logQ correction

##### serving architecture
- 서비스에서 고려할 점: 많은 고객 수, 빠른 반응성, 한정된 자원
-  배치
   - 모델 서빙과 흐름
     - 학습/배치: 하둡, 스파크, 에어플로우
     - 저장/관리: redis, 아파치 피닉스
     - 추론/서빙: springboot, java
       - python 안 쓴 이유: JVM 이점, 토스 내 환경
   - 배치 추론
     - 유저가 추천시스템에 접근 -> 코호트에 속하는지 판단 (피닉스) -> 저정되어 있던 추천 결과 전달 (redis)
     - 10M 유저에게 50ms 로 결과 전달 가능, 코호트별 추천, 안정성
     - 근데 코호트별 추천은 아쉽다. 더 개인화하고 싶다.
- 실시간
  - 모델 서빙과 흐름
    - 학습/배치: 하둡, 스파크, 에어플로우
    - 저장/관리: mlflow(모델저장), toss feature store(피처저장)
    - 추론/서빙: springboot, java, onnx
  - 실시간 추론
    - 유저가 접근하면 toss feature store 에서 추론에 필요한 feature 를 가져오고 onnx 로 추론에서 결과 전달
    - 개인화 추천, 실시간성, 10M 유저에게 100ms 로 결과 전달
- 각각 필요한 쪽에서 둘 다 잘 사용하는 중

# 타겟팅
## [토스ㅣSLASH 24 - ML 기반 자동 타겟팅으로 고객 만족과 마케팅 효율 모두 잡기!](https://www.youtube.com/watch?v=sR4P0v0uUhA&list=PL1DJtS1Hv1PiGXmgruP1_gM2TSvQiOsFL&index=3)

- 타겟팅 왜 할까?
  - 사용자 유입, 이탈 방지, 전환
- 어떤 과정 필요?
  - 타겟 사용자 그룹 분석 및 설정 -> 테스트 발송 -> 성과 분석 -> 본 타겟팅
- pain point
  - 긴 세그먼트 생성 시간
  - 쿼리에 익숙해야 함
  - 기존 ML 세그먼트는 다양한 항목과 규모 설정에 난이도 상승
  - 테스트 성과 낮으면, 다시 분석 필요
  - 이 과정으로 타이밍을 놓치거나, 낮은 성과 지속
- ML 세그먼트 자동생성 모듈
  - 목적: 레퍼런스가 있으면 다른 조건 고민없이 쓸 수 있는 세그먼트 생성
  - 조건: 적정 규모이면서 수동보다 좋은 CTR
- 문제 접근 방법
  - 레퍼런스: 과거 데이터 학습으로 타겟 설정
  - 문제 나누기: 다양한 채널 진입 -> 모델링 분리
  - 시뮬레이션/유사유저: 과거 사례와 모델 비교 / 유사유저 추출
  - 결과 합치기

### 시뮬레이터/유사유저 모델
- 서비스/광고 선호도(클릭, 전환) 예측 모델 LightGBM (70개)
- 결제 카테고리 200개 예측 모델 Transformer

#### 시뮬레이터
1. 과거 레퍼런스 (과거 타겟팅 데이터를 의미하는 듯) AND 광고선호 그룹 탐색
   1. 모델을 통해 예측을 하고 과거 데이터를 이용해서 적절한 CTR/CVR 에서 자른다.
   2. 근데 그러면 과거 타겟팅의 bias 가 있을 것 같은데 이에 대한 설명은 없다. 아니면 내가 아예 로직을 잘못 이해한 것일 수도 있다.
2. 모델들을 이용하여 적정 CTR/CVR 이상 집단 추출
3. 결과 조합하여 최종 세그먼트 생성

#### 유사유저모델 (Look-A-Like)
- 메시지에 반응한 사용자를 학습하여 유사 사용자를 예측
  - 클릭(0,1) 데이터로 분류 모델 만들고 확률값으로 잘라서 유사 유저 추출

#### 요청 flow
- 위 결과들을 or 결과로 해서 최대한 전체 수 확보를 위해 노력한다고 함
- 사용자 ML 세그먼트 호출 -> (아마) 과거 데이터 전달 -> LAL, Simulator 호출 -> 결과 전달

### 성과 (최근 4주 기준, 광고 푸시)
- 수동 평균 CTR 대비 90%, CVR 20% 상승

### 실제 사례
- 결론적으로 다 좋아졋다
  - 오늘의 운세
  - 광복적 이벤트
  - 토스페이 가맹점 대상 푸시

### next step
- 여러 종류의 요청 증가
  - 소수의 큰 Deep model 로 대응
  - 메시지 내용, 이미지 feature 사용
  - seed 가 필요없는 방식 연구
  - 샘플 발송 등으로 반복적으로 학습을 하는 방식
- 성과의 우하향
  - 사용자가 받을 수 있는 잠재적 유효 메시지의 수요는 한계가 있음
  - 사용자/메시지 관점에서 공급 관리/최적화 필요
    - 사용자가 받기 적정 메시지 수, 주기
  - 타겟팅 푸시/앱 알람 이외 채널 확장

# 플랫폼
## [토스ㅣSLASH 24 - ML 플랫폼으로 개발 속도와 안정성 높이기](https://www.youtube.com/watch?v=-im8Gzmf3TM&list=PL1DJtS1Hv1PiGXmgruP1_gM2TSvQiOsFL&index=13)

- 초기 단걔의 머신러닝 모델 개발
  - 데이터 가공, 모델 개발, 서비스 적용을 개별로 접근
  - 긴 개발 시간, 온라인 서빙과 운영의 어려움
- 느려지는 개발 속도, 모델 성능과 안정성 저하
  - 대규모 파이프라인
  - 실시간 모델 서빙
  - 표준화된 개발 방법 부재
  - 인력 자원에 비례하는 생산성
  - 데이터/모델/서빙 drift 문제
  - 모니터링의 어려움

### FeatureStore
- 학습, 추론용 피처 데이터 관리
- 데이터 drift 모니터링

### DagBuilder
- Airflow 위에서 동작하는 파이프라인 빌더
- Yaml 로 DAG 작성

### ML Monitoring
- 모델의 전체 주기를 모니터링
  - feature drift, 예측 결과 분포 등
- (우리팀에도 이런 기능이 있으면 좋을 것 같다고 생각듬)

### 플랫폼 사용 효과
- 개발속도와 안정성 증가
  - 피처 재사용
  - dagbuilder 로 편하게 파이프라인 개발
  - 개발자 실수 감소, 개발 시간 감소
  - 모델 훈련, 배포 편리함
  - 전체 프로세스 모니터링

## [토스ㅣSLASH 24 - Feature Store로 유연하게 ML 고도화하기](https://www.youtube.com/watch?v=-u3rhd7k2JQ&list=PL1DJtS1Hv1PiGXmgruP1_gM2TSvQiOsFL&index=20)

- feature store ?
  - 모델 학습, 추론을 위한 feature 를 저장 & 관리하는 시스템
- feature store 가 왜 필요?
  - feature 재사용
  - 모델 serving 시 이점
  - data monitoring
  - feature 접근 권환 관리
- 오픈소스 vs 자체 개발
  - 적합한 오픈소스가 없음, 빠른 추가 기능 개발 등 -> 자체 개발 결정
- feature store 도입 후 결과
  - 사용 과정에 대해 자세히 발표
    - feature 등록 및 사용
    - 모델 serving
    - data monotoring
    - 접근권한