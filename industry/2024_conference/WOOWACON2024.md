- https://2024.woowacon.com/sessions/
- https://www.youtube.com/playlist?list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a

# 추천, 검색
### 그래프, 텍스트 인코더를 활용한 실시간 추천 검색어 모델링
- https://www.youtube.com/watch?v=FPdJ24JfKmw&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=41&pp=iAQB
- 퀵 커머스: 1시간 이내 원하는 장소에서 다양한 상품군 & 입점
  - B마트, 홈플러스 , CU 등등
- 퀵 커머스 특징
  - explore, real-time, search
- 2 종류의 모델
  - Batch
    - long term history, batch inference
  - Real time
    - short term feedback, real-time inference
- 앱 진입 초반에는 batch 결과를 사용하고 유저액션이 있으면 real time 결과를 사용
- batch model
  - user-keyword non-negative matrix factorization (NMF) 진행해서 user vector 생성
  - 이를 MLP 를 통해서 top 500개 keyword 클릭 예측 모델 만듬
  - 후처리에서 확률값을 keyword 인기도로 보정함
    - $pred_k * \frac{pop_k^m}{pop_k^n + \alpha}$
- real-time model
  - 상품(id, text), 검색어(id, text) 정보 사용
  - id 는 graph encoder, text 는 text encoder 로 임베딩 생성
  - sequence model
- graph encoder
  - 카테고리, 상품, 검색어 3종류 node 를 갖는 가중치 양방향 그래프 생성
  - 검색 이후 상품 클릭 N:M 매핑, 상품에 매핑된 카테고리 1:1 매핑
  - random walk 사용해서 node2vec
    - networkx 쓰다가 성능이슈로 직접 구현한 로직 사용
    - 원래 two tower 썼었음
      - two tower 는 단일 매칭에 초점, 상대적으로 높은 코드 복잡도
- text encoder
  - 상품 텍스트, positive 검색어, negative 검색어
    - 검색어 이후 클릭한 상품 (유저 액션 데이터)
  - positive 검색어에서 sampling 해서 negative label 생성
  - transformer encoder layer 사용, triplet loss 사용
- sequence model
  - 검색어 -> 상품 -> 검색어,,, 유저액션을 사용
  - 각 id, text 임베딩을 dense 넣어서 sequence embedding 만들고 타겟 키워드를 예측하는 모델
    - sequence embedding, keyword embedding 으로 triplet loss 사용

### 취향 저격 맛집 추천, 더 똑똑하게: 추천 모델 성장 일지
- https://www.youtube.com/watch?v=zRLS3_vD1FM&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=9&pp=iAQB
- (2022년) two-tower 모델
  - user: user id, 위치, 요일 / shop: shop id, category
  - 위경도 S2Cell (구글에서 개발) 변환
  - in-batch negative sampling
  - 1700만 사용자, 50만 가게 -> warmstart training, 이전 학습 모델의 parameter 를 신규 모델의 parameter 초기화
- 근데 시간대별로 추천 결과 만들고 싶어 -> user-tower 에 시간 feature 추가 -> 시간별 추론
- 매시간 inference 하지말고 시간대를 clustering 해서 쓰자 -> 5개 시간대
  - 시간대 embedding 만들어서 진행
- 실시간 추천 레츠고
  - 실시간 행동 이력 임베딩, 가게 임베딩 만들어서 실시간 추천
  - 그럼 content-based 인코더 이용하면 어떨까? 유저가 클릭한 가게와 유사한 가게 추천
- content-based 인코더
  - 메뉴 정보(메뉴명, 메뉴가격), 가게명으로 가게 임베딩 생성 (구조는 발표자료)
  - Bi-Encoder 구성 (가게 인코더 - 검색어 인코더)
    - 검색을 통해 주문으로 이어진 가게-검색어 쌍 데이터
    - Triplet loss (Anchor: 가게, Pos: 주문으로 이전 검색어, Neg: 인기기반 랜덤 샘플링 검색어)
  - 그래서 검색어 임베딩, 가게 임베딩 생성됨
- 실시간 반응형 로직 고려사항
  - 사용자의 어떤 행동이력 사용?
    - 클릭한 가게 + 검색 쿼리
    - 1시간 이내 발생한 행동 이력
    - 최근 행동 이력 3개 사용 (탐색형, 목적형 유저 둘 다 고려 AB test 해보니 3개가 좋음)
  - 어떤 후보 가게를 추천에 사용?
    - 사용자 위치 기반 모든 가게 후보 vs two-tower 추천 결과를 후보 -> AB test 해보니 two-tower 가 좋았음
  - 최종 랭킹?
    - weighted RRF: 최근 행동 이력에 더 가중치
    - 1~3번째 행동이력들 각각으로 랭킹뽑고 RRF
- 추천하는 구좌, 상황에 따라 조금씩 로직은 달라짐
  - 실시간 반응형 추천(위 내용), 연관가게 추천, 위치 coldstart 추천, 메뉴 큐레이션 가게목록

# LLM
### AI 데이터 분석가 '물어보새' 등장: 데이터 리터러시 향상을 위한 나만의 데이터 분석가
- https://www.youtube.com/watch?v=_QPhoKItI2k
- LLM 개발팀
- 목표: 구성원의 데이터 리터러시 역량 상향 평준화
- 데이터 리터러시
  - 데이터 이해, 생성, 분석, 기반 의사소통
  - 이를 위해 4가지 제공 Data Discovery, Text2SQL, Agentic Analytics, Knowledge Sharing
- text2sql
- Data Discovery
  - 쿼리를 보내면 쿼리 설명
  - 테이블 궁금하면 테이블 컬럼, 메타 정보, 활용 예시 제공
- 물어보새 서비스 고려해야할 요소?
  - 체계화: 체계적인 정보 수집
  - 효율화: 사내 정보 검색 기술 개발
  - 자동화: 365일 24시간 상시 응답
  - 접근성: 업무 소통에 익숙한 채널 사용
- 물어보새 아키텍쳐는 블로그에 있음
  - gpt 사용하고 fine tuning 은 안함, RAG 사용
- 개발 과정
  - 다양한 DB 사용해서 RAG, Prompt 사용
    - 테이블 DDL: 테이블명, 컬럼명, 칼럼 성명, 데이터 타입 -> 수 많은 테이블중에서 어떤 테이블을 사용? -> 테이블 meta
    - 테이블 meta: 테이블별 사용 목적, 서비스, 키워드, 질문 등 -> 근데 배민 서비스의 용어는 잘 이해하기 위해? -> 비즈니스 용어 사전
    - 비즈니스 용어 사전: 배민 용어에 대한 설명
    - SQL few shot: 예시 질문과 답변을 참고하도록
    - Log 사전: 로그명, 로그 설명 및 값
  - Azure OpenAI Embedding 모델 기반 문서 벡터화, VectorDB 구축 -> Airlfow 로 매일 최신화
- LLM 이 더 똑똑하게 답변을 하게 하는 방법?
  - router 로 질문 분류
    - 일단 먼저 데이터 질문 / 일반 대화 분류
    - 데이터 질문이면 더 세분화 되도록 분류, 이때 자체적인 score 를 개발해서 이를 기준으로 분류
  - Dynamic prompting
    - 다양한 vectorDB 와 다양한 상황에 맞는 Prompt 를 dynamic 하게 조합해서 결과 생성
    - 자체적으로 다양한 성능 평가 지표로 성능 평가
  - Hybrid Search 로 문서 추출
- 앞으로 개발
  - Agentic Analytics
    - chain 기반에서 graph 기반으로 변경
    - 데이터 분석 서비스 기능 제공
  - knowledge sharing
    - 사내 모든 데이터로 지식 범위를 확장

### Fine-tuning 없이, 프롬프트 엔지니어링으로 메뉴 이미지 검수하기
- https://www.youtube.com/watch?v=YjdZL3Sc9hA&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=10&pp=iAQB
- 식당에서 이미지 등록하는 것을 검수함
- 프롬프트 삽질 했던 과정
- chatgpt 옵션을 이용하여 completion 출력 구조화
- 일관된 답변
  - parameter 조정: temperature, top-p
  - CoT: 이미지에 대한 설명하라고 하고 진행
- 허리띠 졸라 매기
  - 영어로 다 바꿔서 토큰 수도 적고 속도도 빨라짐
- 최종
  - 입력데이터 암시, 이중부정 표현 삭제 (system instrunction)
  - parameter 조절
  - gpt 가 해야하는 요구사항 분리, 응답예시 제공 (prompt)
- gpt 이외의 방법
  - 주요 음식 object detection model 은 gpt 가 하기 어려워서 따로 모델사용
  - 저작권 같은 것은 분기를 만들어서 사람이 하도록 함

# ML
### 음식 픽업하러 산 넘고 강 건널 수 없으니가: 배달 데이터를 활용해 최적의 지역 클러스터링하기
- https://www.youtube.com/watch?v=Ub1kL0OB5n8&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=6
- 배차의 순서
  - 배차후보 선정 -> 비즈니스 제약사항으로 필터링 -> 비용계산 -> 최적화해서 최종 조합 선정 -> 배차 추천해서 배달 수정
- 기본적으로 우버의 H3 를 사용
- 문제 정의
  - 지형이나 상권 고려 불가
  - 성능 및 타이밍 이슈 유발
  - 무리한 배차로 인한 이동거리 증가
- hierarchical clustering
- 공간 데이터를 word2vec (skipgram)
  - 픽업 -> 픽업 -> 전달 -> 전달,,,
- 지리적인 성질을 이용하여 정성적인 평가
- 다양한 후처리 진행

### 당신에게 배달 시간이 전달되기까지: 불확실성을 다루는 예측 시스템 구축 과정
- https://www.youtube.com/watch?v=SkliEsGRuSQ&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=12&pp=iAQB
- 예측해야할 것
  - 배달예상시간: 식당별로 얼마 걸리는지 구간으로 보여줌
  - 고객안내시간: 주문하면 안내받는 예상 시간
- 다차원 피쳐 집계 -> 소요시간 예측
  - 시간대별 패턴: 장기, 중기, 단기
  - 상황별 변동요인: 상품 카테고리, 서비스타입, 지역&가게별, 피크타임 여부
  - 배달현황: 주문수, 조리시간, 배차/픽업/전달 소용시간, 배차수락 주문수
- 공간을 수치로 담기
  - 공간피처를 embedding
  - 위경도: H3 index 사용해서 target encoding (smoothing 옵션 사용)
- 갑작스런 변화 대비
  - 데이터가 큰데 과거 긴 시간을 사용하고 싶었음 -> 기간별로 undersampling 진행
  - 기상타입별 데이터 정보 이용
- 큰 문제를 작게 쪼개기
  - 탐색 -> 주문 -> 배차 -> 픽업 -> 전달
  - 각 단계별로 독립적으로 학습 (배차시간, 픽업시간, 전달시간, 지연시간 예측)
- 구간 추정이 필요한 경우, 확률분포
  - 각 배달마다 5분, 6분,...60분 소요될 확률을 구함 (multiclass classification?)
  - 단계별로 구한 값들을 컨볼루션 연산을 해서 최종 시간별 확률 분포를 구함
  - 가장 높은 확률을 중심으로 10분 (fix) 구간
- 서비스마다 시스템을 따로 만듬, 각기 특징이 다르기 때문
- 모든 시간예측 모델 일배치로 학습
- 모델 배포 전략: 모델 로드 패턴
  - 모델을 이미지에 넣는게 아닌 로드해서 사용하는 패턴
  - 이미지 경량화, 재사용
  - 잦은 모델 변경에 적합
  - 모델 학습과 빌드/배포 파이프라인 분리
- 예측 시스템의 구조
  - 배달예상시간 vs 고객안내시간 같은 모델 사용
  - 단, 배달예상시간은 N분 마다 준실시간 배치 서빙, 고객안내시간은 서빙 api 호출해서 온라인 서빙
- 신뢰있는 데이터
  - Data Quality operator 로 체크 (오픈소스? Great Expectations 기반 Airflow Custom Operator 사용): type check, null check, validate rule, min/max etc
  - monitoring
    - data drift, 모델 성능, 추론 성능, 리소스 모니터링, 비즈니스 메트릭
  - 실시간 피처 생성
    - 기존에 Airflow 배피로 하다가 Flink 기반 실시간 스트림 처리로 개발
  - Time Buffer Automation
    - 어드민 같은 시간 조정 기능 추가 (by 인프라 레벨)
  - Shadow test, simulation

### 자율주행 로봇을 위한 머신러닝 모델의 추론 성능을 최적화하기
- https://www.youtube.com/watch?v=zOJQ4l6cooQ&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=25&pp=iAQB
- 엣지 디바이스 NVIDIA Jetson Orin NX 사용, 상당히 제한적인 리소스
- torch -> ONNX -> TensorRT
  - 연산자들이 바뀌는 것
- TensorRT 최적화 4가지
  - Quantization 추론 속도 최적화
  - Layer/Tensor Fusion 으로 메모리 IO 최적화
  - Kernel Auto Tuning 으로 GPU Platform 최적화
  - Deep Learning Accelerator (DLA) 에서 추론 가능하도록 모델 변환
- Quantization 추론 속도 최적화
  - range mapping -> rounding -> clip
  - Post Training Quantization
  - Quantization Aware Traning
- Layer Fusion
  - CUDA kernel 호출 횟수 최소화
- Tensor Fusion
  - 메모리 읽기/쓰기 최소화
- Kernel Auto Tuning
  - GPU 에 최적화된 CUDA Kernel Tuning
- DLA
  - image CNN 전용 처리 장치

# platform
### 우아한 데이터 허브, 일 200억 건 데이터 안전하게 처리하는 대용량 시스템 구축하기
- https://www.youtube.com/watch?v=AtmI56DGhi4&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=8

### 장애 같은데? 일단 STOP!: 배달서비스 장애 감지/차단 시스템 구축 경험담
- https://www.youtube.com/watch?v=NKbmLyWlVpg&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=28&pp=iAQB
- 개발 내용은 아니고 PM 의 발표

# 기타
### OKR과 프로젝트의 연결고리: 과제 관리의 새로운 판을 짜다
- https://www.youtube.com/watch?v=WWa12L47Hg0&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=19&pp=iAQB

### 전체는 부분의 합보다 크다: 개인의 능력을 뛰어넘어 더 큰 시너지를 내는 팀 문화 만들기
- https://www.youtube.com/watch?v=hB8RWgEeKz8&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=30&pp=iAQB

### 개발자가 개발만 잘하면 회사는 망한다: 우아한테크코스의 소프트 스킬 교육
- https://www.youtube.com/watch?v=XudqDRk2syQ&list=PLgXGHBqgT2Tu7H-ita_W0IHospr64ON_a&index=27&pp=iAQB