# 카카오엔터테인먼트
## 추천
### [최애 작품 이용권 선물해주는 ‘Helix 푸시’ 개발기 (2024)](https://if.kakao.com/session/19) 
-> 예시를 들어주면서 발표해서 좋았음
-> 모델 자체에 대한 구체적인 내용의 발표는 아님

- Helix 푸시
  - 개인화된 컨텐츠 푸시 시스템
  - 작품이용권 관련 마케팅 푸시
- 프로젝트의 목표는 운영비용 효율화, 열람자수 방어, CP사 매출 증가
- 웹툰 도메인 특성
  - 순차적 열람, 동시 소비, 낮은 재소비율, 간헐적 열람
- 이탈에 영향을 주는 상황에 맞춰서 푸시
  - 열람작품수가 많을수록 덜 이탈 -> 미열람작 푸시 -> 열람 작품수 증가
  - 열람일수가 잦아질수록 덜 이탈 -> 기열람작 푸시 -> 열람 일수 증가
- 미열람작 추천 모델
  - 작품 임베딩 모델로 유저 열람이력과 비슷한 후보들을 추리고 미열람작 선호도 모델이 최종 선정
  - 작품 임베딩 모델
    - 작품을 벡터화 -> 유사 작품을 찾을 수 있음
    - 평가지표: 테마키워드 precision
      - 시드 & 유사작품 겹치는 테마 키워드 수 / 유사작품 테마 키워드 수
    - Factorization Machine 이 성능이 가장 좋아서 이를 사용했다고 함
    - 모델개선
      - 원래 모델 학습 데이터 생성시 최근 활성 유저를 샘플링해서 사용했는데 과거에 연재가 시작된 작품의 경우 최근 열람유저 데이터가 거의 없는 경우 발생 -> 이런 작품의 경우 임베딩 학습이 잘 안됨
      - 이를 보완하기 위해 작품단위 학습 데이터 샘플링으로 훈련했다고 함
  - 미열람작 선호 모델
    - 후보 작품의 선호도는 시드 작품과의 유사도룰 weighted sum 해서 결정, 이때 two-tower 형태의 모델을 사용한듯
    - 모델개선
      - 장기 선호 미반영
      - 장기열람 데이터 활용 후 hit ratio 증가
- 기열람작 추천 모델
  - 유저가 이미 읽은 작품 중 가장 좋아하는 작품을 예측
    - 2주간 열람한 작품에 대해 이후 3주간 몇 회차 더 읽을지 예측
  - 지표
    - hit@k: 선호 예측 상위 k개 중 하자하지 않은 작품이 1개라도 있는 유저의 비율
    - hit@top1: 최애 작품으로 예측한 작품과 실제 최대 작품이 일치하는 유저의 비율
  - BERT 구조 사용
    - 유저가 작품 열람한 순서대로 데이터셋 구성
    - 다양한 도메인지식으로 input 생성 (현금 결제 비율 등등), output 은 선호도 점수

## AI: LLM
### [지연 시간 순삭! LLM 추론 구조와 효율적 애플리케이션 설계](https://if.kakao.com/session/24)
-> 기본개념도 같이 설명해주는 친절한 편
-> 추론 속도 향상 팁들을 많이 알려줌
-> LLM 업무를 직접하지 않으면 이해하기 어려움

- 프롬프트를 통해 closed question 으로 만들기
- 토크나이저 최적화
  - 토큰 수가 너무 많으면 당연히 추론 시간이 늘어남
- structured output -> openai 옵션있음
  - json format 으로 출력하고 싶은 경우? 프롬프트로 할 수 있을 것이다.
  - 그런데 100% 보장도 할 수 없고
  - 추론속도를 위해 전부다 출력하지 않고 딱 필요한 값만 나오게 한다.
- KV cache 사용
- 병렬처리
- prefix 공유 (프롬프트 공통적인 부분은 캐싱)

# 카카오헬스케어
## AI: LLM
### [생성형 AI를 활용한 개체명 인식(NER)](https://if.kakao.com/session/22)
-> 헬스케어 데이터 관련 내용에 관심이 있으면 들으면 좋을듯
-> LLM 으로 NER 을 하는 과정을 잘 설명하심

- 의료진이 실제 의료를 하면서 생기는 real data 에 대한 처리
- 기존의 ML 로는 패턴인식이 어려움, 사람이 해왔는데 이 또한 힘들어짐
- LLM 으로 진행해보자 -> 사람보다 성능, 비용 좋음
- 진행과정
  - 개인정보 때문에 한정적이고 비식별화된 데이터 사용
  - 데이터 전처리
    - 사람이 annotation: 테스트용 50개, 훈련횽 500개 등
  - 성능 고도화 실험
    - prompt, fine-tuned LLM
  - 추론
- 느낀점
  - prompt 에 대한 노력보다 fine-tunning 성능이 좋다.
  - fine-tunning 시 데이터 갯수와 성능이 항상 정비례하지는 않는다. 500개면 되는듯하다.

# 카카오뱅크
## AI: LLM
### [이 문자가 스미싱인 이유는? - 스미싱 탐지를 위한 LLM 개발 및 평가](https://if.kakao.com/session/23)
-> 깔끔한 발표, 디테일한 팁이나 심화된 내용은 없었지만 프로젝트 진행 flow 를 잘 정리

- 목적: 스미싱인 이유를 설명가능한 LLM 만들기
- 데이터셋
  - 문자(X) - 스미싱 여부(y)
  - deduplication 진행해서 데이터 필터링 (비슷한 데이터는 지우는)
  - LLM 으로 판단근거 label 생성
    - 스미싱 관련 정보(정의, 원리, 예시 등), 지시문, 문자, 스미싱 여부 label: 이 데이터들 이용
- quantized Lora 사용해서 fine-tune
  - 훈련시에는 문자, 스미싱여부, 스미싱 판단근거 데이터로 학습시킴
- LLM 결과 평가
  - 정확도: f1 score
  - 정답문장과 비교: BLEU (정답문장에 포함된 생성문자 내 단어 갯수), ROUGE (정답문장의 단어가 생성된 문장에 포함된 정도), BertScore (정답문장과 생성문자의 임베딩 유사도)
  - LLM 기반 지표: G-Eval
    - LLM 에게 평가 요청 (논리적인가, 일관된 내용인가, 스미싱 탐지에 유용한가, 답변 형식을 준수했나)
    - 1~5점 내고 평균
  - Human 정성평가
    - 평가자는 어떤 LLM 이 만든지 모르고 평가진행 (카뱅 vs 일반)
    - Cronbach's Alpha, Cohen's Kappa 로 여러 평가자 결과 합산
- 결과
  - 카뱅 fine-tune 한 모델이 더 좋다

# 카카오페이, 카카오페이손해보험
## AI: LLM, OCR
### [LLM 서빙하기](https://if.kakao.com/session/25)
-> LLM 서빙 효율화 관련 내용, 팁들 공유해주심

- 서빙프레임워크 선택하는 과정 공유해주심
  - TGI, vLLM, LightLLM, TensorRT-LLM 에서 고민 -> 최종적으로 vLLM 선택
- KV Cache 로 연산 효율화
- 이 때 발생하는 메모리 문제점 존재
- 메모리 문제를 해결하기 위해 PagedAttention, continuous batching

### [문서 검토는 이제 Document AI로 한방에!](https://if.kakao.com/session/31)
-> 7년차 백엔드 개발자가 7개월동안 만든 내용, 깔끔하고 효과도 좋은 발표장표
-> 어려운 내용은 아니었고 OCR 프로덕트 개발 과정에 대해 알 수 있음

- Document AI: 문서의 내용을 자동으로 인식하고 처리하는 기술
- 영수증 인식 (해서 보험금 지급하는 과정에서 사용)
  - Edge detection -> Layout Analysis -> OCR -> Parsing(이건 룰기반)
  - Edge detection
    - 이미지에서 문서의 테두리를 검출하여 불필요한 배경을 제거하고 원근감을 조절
    - detect 하면 4개 꼭지점 좌표를 구할 수 있음
    - OpenCV 의 Perspective Transform 으로 원근감 조절
    - YOLO 모델의 Segment 기능 사용
  - Layout Analysis
    - 문서의 구조를 분석하여 원하는 영역만 검출
    - 특정 객체, 위치, confidence 의 결과가 나옴
    - YOLO 모델의 Detect 기능 사용
  - OCR
    - 문서 내의 문자를 인식
    - TrOCR 사용
  - Parsing
    - 룰기반으로 최종 데이터 생성하는 과정
- 고민했던 점
  - Layout Analysis
    - 영수증 이미지가 회전되어 있으면? Layout Analysis 부터 잘 못함, 회전이 필요함
    - 영수증이 아니라 아예 다른 문서면? 영수증이 아니면 프로세스 중단
  - Parsing
    - Levenshtein Distance 를 이용
      - 기존에 나와야하는 단어와 약~간 다른 경우가 있는데 distance 를 계산해서 특정값이하면 대체해서 사용

## FDS
### [FDS에 지속 성장하는 ML 적용 이야기](https://if.kakao.com/session/29)
-> 전달력있는 발표장표
-> FDS 라는 새로운 도메인에서 ML을 사용하는게 흥미로웠음, 다만 특별히 새로운 내용은 없다고 느낌

- FDS가 어려운 점: 사고를 막으면 새로운 형태의 또 다른 사고 발생
- 그래서 지속 성장하는 ML 이 필요 -> Adaptive ML
  - 모델의 지속적 학습
    - Airflow 로 주기적 학습
  - 피처 자가 적응
    - 시간에 따라 데이터의 내용이 바뀌어도 모델이 고려할 수 있도록 피처 생성
      - 예를 들어, time window feature 로 사고비율피처 생성
    - 새로운 신고데이터 반영이 자동화되어서 주기적으로 피처 생성
- 툴
  - model serving: Triton
  - feature store: redis, hbase
  - model store: mlflow

# 카카오게임즈
## 이탈방지
### [통계를 이용해 이탈을 방지할 수 있을까?, SMART STATS 개발기](https://if.kakao.com/session/74)
-> 이탈예측 같은 것이 아니라 게임유저의 이탈을 직접적으로 막는 방법에 대한 설명

- 왜 이탈을 할까?
  - 흥미를 잃어서
    - 너무 쉬워서 or 너무 어려워서
    - 사람마다 국가마다 편차가 크다
  - 특히 초보들은 도움이 필요하다
    - 직접적으로 도움을 준다면? 아이템 제공?
      - 초보자에게는 별효과 없었음
      - 형평성의 문제
- 과거의 유저들은 어떻게 했을까? 유저들에게 통계를 제공해주자!
  - 원하는 시점의 필요한 데이터를 만들어서 유저한테 전달해줌
  - (해당 퀘스트를 통과한) 다른 유저들은 어떻게 했는지
- AB TEST 진행했더니
  - 잔존율이 1.8배 높음, 특히 초보 그룹에서 효과가 컸다.
  - 실험군이 레벨이 더 높은 분포
  - 무과금에서 PU로 전환률이 1.8배 상승

# 카카오
## AI: LLM, 이미지
### [이미지까지 이해하는 Multimodal LLM의 학습 방법 밝혀내기](https://if.kakao.com/session/12)
-> 잘 모르는 분야라서 완벽히 이해하기는 힘들지만 잘 설명해주시고 발표 장표도 시각화가 되게 좋음
-> kanana 새롭게 리브랜딩 되어서인지 많이 준비하신 느낌

- Multimodal LLM: 텍스트 이외의 다른 데이터도 같이 넣어서 답변을 받을 수 있는 모델 (output은 텍스트)
- Honeybee 라는 모델이고 학회에서 하이라이트도 받음
- 주로 vision encoder - projector - llm 의 형태
  - vision encoder, llm 은 주로 Pretrained model 사용
  - projector 는 훈련 진행
- 새롭게 개발한 projector 관련해서 설명 진행
- 학습방법 설명 진행

### [나만의 프로필 이미지를 만드는 Personalized T2I 모델 개발기](https://if.kakao.com/session/17)
-> 이미지 생성 모델 관련해서 잘 설명해주심
-> kanana 새롭게 리브랜딩 되어서인지 많이 준비하신 느낌

- Personalized T2I: 개인 사진 몇개를 받아서 유저 프롬프트대로 원하는 이미지 생성
  - prompt follwing + high quality + similarity
- 카톡 프로필 생성 모델
  - 모델 구조 설명 진행
  - 공개 데이터셋의 한계, 좋은 데이터셋을 만들기 위해 노력
    - 적당한 크기, 퀄리티 좋은, 알맞은 전처리
    - 고품질의 비디오 데이터셋을 활용하여 한 사람이 여러 표정, 모습을 데이터셋으로 만들었음
- backbone 모델을 사람이미지를 잘 만들 수 있도록 fine-tune

### [AI Agent 기반 스마트 AI 마이 노트](https://if.kakao.com/session/21)

### [업무 효율화를 위한 카카오 사내봇 개발기](https://if.kakao.com/session/26)

### [AI 를 통해 스팸을 대응하는 카카오의 노력](https://if.kakao.com/session/30)
-> 인지심리학을 사용한게 흥미로웠음
-> AI 를 업무프로세스에서 유용하게 적용했다고 느껴짐

- 사진에 대해 라벨링에 AI 적용 (인지심리학 이론 이용)
  - 사람을 대체하는 것은 아니고 사람을 돕는 역할
    - 분류 모델: 라벨 추천 & 모델이 참고한 영역 표시
    - LMM: 판단 근거 & 사진 설명
  - 라벨링 퀄리티 프로세스
- LLM 으로 스팸 분류
  - 모니터링 운영자가 받기 이전에 1차 필터링할 때 모델적용
  - 분류 결과와 스팸으로 분류한 이유를 설명해서 제공
- LLM 데이터
  - output: 분류결과, 요약, 의심키워드, 추천정책
  - 그런데 분류결과를 제일 마지막에 출력해보니 분류 성능이 32% 상승
- AI 가드레일
  - 윤리적인 답변을 했는지 LLM 으로 판단
  - good, bad, normal 데이터를 균형있게 훈련시켰을때 판단을 제일 잘 했음

### [LLM으로 음성인식 성능 개선하기](https://if.kakao.com/session/34)
- end-to-end 음성인석: 음성데이터를 바로 문자열로 변환
  - 대표적인 모델로 CTC, AED, RNN-T 가 있다.
  - 주로 encoder(음성 이해), decoder(텍스트 생성) 형태
- LLM 기반의 음성인식?
  - decoder 를 LLM 으로 대체하는 방법으로 가능성 보여줌
  - 파라미터가 많아져서 훈련, 추론시 리소스가 증가
- 추론 비용 증가 없이 LLM 활용하려면?
  - Knowledge distillation 진행
  - LLM 을 선생, transformer decoder 를 학생으로

### [CodeBuddy 와 함께하는 AI 코드리뷰](https://if.kakao.com/session/35)
-> 설명 잘해주심

### [AI Assistant와 통합 지식베이스를 통한 AI Native Company 구현](https://if.kakao.com/session/41)
-> 3개월만에 했다는게 대단

- 사내 통합 지식베이스
  - 기존 RAG 한계점
    - 단순한 청킹, 제한된 문서 탐색
    - 그로 인해 아래와 같은 경우 잘 못함
      - 벡터 유사도에 기반한 답볍
      - 질문에서 여러 문서가 필요한 경우
      - 넓은 범위의 내용을 기반으로 하는 답변
  - graphRAG 도입 후 성능향상
  - 사내 시스템 API 연동
    - Spring AI 를 사용하였고 function call 해서 사내 서비스 api 와 연동되어 있음
      - 회의실 예약 등
- AI buddy
  - 크롬 확장 프로그램, 카웤에서 제공
  - 검색, 요약, 번역, 춘식도락, 회의실 등등의 기능
  - spring AI 를 백으로 쓰고 상황에 따라 graphRAG, RAG(PostgreSQL VectorDB) 를 사용
  - 대화 맥락 유지를 위해서는 redis 사용

### [밑바닥부터 시작하는 LLM 개발기](https://if.kakao.com/session/48)
-> 디테일한 부분까지 발표하신 느낌

- pre-training
  - data strategy
    - two-staged pretraining 고려
      - stage1 에서는 diversity, quantity
      - stage2 에서는 quality, goal
    - 다양한 전처리 진행
    - 문서의 퀄리티를 측정해서 stage1, 2 나눔 
      - 이때 LLM, fasttext 이용
  - training strategy
    - 큰 모델을 먼저 학습하고 distillation 진행
    - 큰 모델을 llama 모델 구조 사용, 학습 방식은 DeekSeekLLM 에서 제시한 방법론
    - 한국어 벤치마크 kmmlu, haerae 의 점수와 영어 벤치마크 평균적으로 잘하도록
    - 이외에도 상세한 내용 설명하심
- post-training
  - pre-training 에 비해 상당히 적은 리소스 필요
  - 2가지
    - supervised fine-tuning
      - input 에 해당하는 answer 를 생성하도록 학습
    - preference based learning 
      - 여러개의 answers 를 통해 좋은 response 를 강화하고 안 좋은 response 를 약화하는 방향
  - lessons in supervised fine-tune
    - 실제 서비스를 사용하는 형태와 유사한 prompt(유저 input) 는 중요 (정형화되고 틀에 박힌게 아닌)
      - 실제 유저들은 정말 다양하게 쿼리함
    - response/answer 의 퀄리티는 중요
    - 서로 다른 도메인 데이터셋은 각기 구축이 필요
      - 각 도메인 간에는 유의미한 성능 간섭이 발생하지 않음
  - lessons in supervised fine-tune
    - preference data 를 잘 만들어야 한다
      - 도메인별로 각각 전략 필요

### [AI 기반 광고 콘텐츠 모니터링 기술 개발기](https://if.kakao.com/session/59)
- 모델
  - 텍스트와 이미지 사이의 관계를 추론하는 오픈소스 멀티모달 모델 사용
  - 이미지-텍스트 쌍 contrastive learning
- 모델 학습 & 배포 자동화 파이프라인
  - 데이터
    - 모델이 승인, 보류에 대한 확률 output
    - threshold 기준에 따라 사람이 검수
  - 데이터 정게
    - 이미지 url, label
  - 학습
    - 오픈소스 파인튜닝
  - 성능평가
    - 테스트셋으로 평가
    - 사람 검수 기준 threshold 재성립
  - 추론 모델 변환
    - Nvidia TensorRT, Nvidia Triton Inference Server
    - Pytorch + FastAPI 보다 성능이 좋음

### [빠르고 비용효율적으로 LLM 서빙하기](https://if.kakao.com/session/53)
-> 연구성 발표
-> 양자화 방법들 설명, 해당 발표만으로는 이해하기 쉽지는 않음

- 오픈소스를 적극적으로 활용하는 중, 직접 PR 날리면서
- 양자화
  - weight only quantization
  - weight/activation quantization
- LLM 양자화
  - GPTQ, AWQ, QQQ
- Speculative Decoding
  - autoregressive decoding 의 순차적인 생성 한계를 극복하기 위한 방법
  - 가벼운 모델로 여러개의 후보 토큰을 생성, 원래 모델이 생성된 토큰을 병렬로 검증
  - 가벼운 모델 생성 token 의 채택률이 중요
    - 원래 모델와 유사한 output 확률 분포 필요 (학습방식, 데이터 유사)
  - 가벼운 모델은 생각보다 충분히 작아도 되고 eval 성능이 높지 않아도 됨 (다음 나올 쉬운 토큰만 맞추면 됨)
  - 향후 계획
    - 가벼운 모델은 원래 모델에 비해 1/10 인데 1/50 해야할듯, pruning & distillation 으로 개선중
    - 더 나가면 가벼운 모델을 생성하는 기술 필요

### [서비스에 LLM 부스터 달아주기: 요약부터 AI Bot 까지](https://if.kakao.com/session/66)
-> 이론적인 내용보다 실제 경험 공유, 한국어를 잘하는 llm 에 대한 노력

- 난이도: data extractor < general chat bot < agent
- data extractor
  - 카카오톡 프로야구봇 경기 요약 기능
    - 꽤 많은 constraint 존재
    - 이를 잘하기 위해 2 stage 로 쪼개서 풀기
      - highlist extractor model -> summary rephrasing model
- general chat bot
  - 70B 규모의 LLM 도 한국어 생성은 조금 불안정한 상태
  - language transfer 시도
    - pretraning, SFT
    - model merging
    - DPO 로 어투 교정 (번역투가 생성되는 것을 자연스러운 문장으로 교체)
      - 데이터를 직접 수집해서 학습
  - serving
    - Speculative decoding 이 throughput 의 이점을 줌
      - acceptance rate 도 중요하지만 input, output token 의 길이에 영향을 많이 받음
    - prefix caching
      - 동일한 system prompt 가 반복적으로 들어오는 경우, multi turn chat 의 경우 성능상 이점이 큼
      - vllm 에서 기능 제공
    - chunked prefill
      - 생각보다 input prompt 처리비용이 꽤 큼
        - vllm 에서 배치로 처리하는데 encoding 을 하면 decoding 을 stop 함, encoding 이 길면 꽤 느려짐
      - vllm 에서 기능 제공
- agent
  - 상황에 맞게 system prompt 변경, 상황에 맞는 tool 주입
  - function call 로 특정 요청에 대한 처리 진행
  - tool call parsing server 를 두고 상황에 따라 tensorRT, vllm, SGLang 서빙엔진을 부름
  - language transfer in function call

### [‘선물하기 와인탐험’ LLM 대화형 서비스 개발기](https://if.kakao.com/session/71)
- 와인추천해주는 채널, 이를 선물하기로 선물
- 서비스 목적
  - 접근성, 전환율, 확장성 -> 자연어 대화 기반 상품 추천 AI 서비스
- 아키텍처 사진
  - chat generation 부분에서는 intent parser 로 의도파악후 각각 맞는 쪽으로 보냄
- 금칙어대응
  - 문장/단어 유사도 측정 대응
  - 카카오 safebot 서비스 대응
  - 자체 금칙어 사전 구축 및 필터링
- 구조화된 대화와 상품 검색 설계 를 중요하게 생각
  - 와인 추천에 필요한 정보 구조화 (따로 공부도 하심) 하고 어느정도 틀이 잡힌 대화를 진행
    - 가격대, 타입, 당도, 바디감 등등
-  대화를 잘하는 챗봇? 유창한 답변, 사용자 의도 파악, 비즈니스 로직 반영 -> 대화흐름을 제어
-  대화흐름 아키텍처
   -  의도와 주요 키워듣 뽑는다.
      - 상태판단(예외처리 등), 와인정보(가격 등), 상황정보(나이, 대상, 조건), 발언정보 (레드와인 등)
       - 의도별 대응체계
         - new recommend
         - popular recommend
         - questions about recommend
         - questions about intent
         - information
         - out of context
   -  DB 에 검색 (검색 DB 랑 RAG 둘 다 쓰는듯)
-  이제 중요한 것은 와인 찾기
-  RAG 적용
   -  달성해야하는 목표: 신뢰성, 정확성, 최신성
   -  위키피디아에서 와인 지식 데이터 수집하고 이를 구조화 (이에 대한 설명 잘 해주심)
   -  와인 상품 데이터 정제 -> 이미지에 OCR 적용해서 정형화된 와인 정보 수집
-  와인 검색 관련 일부
   -  multi-turn 검색 특성을 고려한 처리
   -  미충족 검색 특성 처리
      -  prompt "미충족 특성을 확인하고 해당 특성을 만족하는 와인은 없었다고 설명을 추가해"
      -  이렇게 해야 유저가 '아 열심히 찾아보기는 했는데 없나보네' 아예 못알아듣는다고 생각하지는 않음
-  테스트 자동화
   -  기능 업데이트 마다 문제 발생 -> 테스트 필요성 존재
   -  근데 LLM 답변이 항상 똑같지는 않고 숫자처럼 딱 정답 판단이 어려워서 LLM 으로 평가하는 시스템 개발
   -  평가하는 LLM 은 튜닝없이 chatgpt-4o 사용, 문제 있다고 하는 경우만 사람이 확인

## ML
### [데이터 분석과 머신러닝을 통한 유저 방문 맛집 발굴하기](https://if.kakao.com/session/14)
- poi = point of interest: 관심 지점, 관심 지역 정보
- precision 을 높이기 위해 위치로그에서 방문했는지 데이터를 필터링
  - 구역을 구분하기: poi 가 아닌 것 같은 경우 필터링 (고속도로는 방문지가 아닐것)
  - 특정 기준 이상 체류하면 방문
- 오차 해결하기 (정확한 poi 를 방문했는지 찾기)
  - 반경 오차, 고도 측정 불가, 기타 오차 존재
  - 오차 반경 내에 poi pool 생성 -> 방문 확률이 가장 높은 장소 예측
- 방문 장소 예측 (classification)
  - 도착 로그, 클릭 로그를 라벨로 만듬 (그대로 쓰지는 않고 필터링해서)
  - 유저 정보를 피처로 활용 (유저 데모, 이전 방문 장소, 시간대 등)

### [그래프 기반 악성 유저군 탐지: 온라인 광고 도메인에서의 적용](https://if.kakao.com/session/18)
- 광고 어뷰징?
  - 비정상적인 방식으로 트래픽을 증가시켜 부당하게 이익을 취하는 것
  - 광고주 광고효율 하락, 정상 매체들의 수익 감소, 추천 학습 데이터 오염
- 광고 트래픽의 42%는 invalid traffic 이라는 리서치가 있음
- 목표: 어뷰저들의 우회 비용 상승시키기 -> 수익성 악화 -> 어뷰징의 동기 제거
- 어뷰저 패턴
  - 어뷰저들은 어뷰징 매체에 대한 공통 방문이 많음
  - 정상적인 유저들은 어뷰징 매체를 거의 방문하지 않음
  - 그래프 문제 "유저-매체 그래프" 에서 고립된 어뷰저군 탐지
- 그래프 투영 (매체-매체로 투영) -> 고립되는 매체군 탐지 (커뮤니티 탐지 -> 악성 커뮤니티 식별)
- 매체-매체 그래프 구축
  - 전처리
    - 공통방문 비율화
  - GraphFrames motif
  - gephi
    - 시각화 해보니 어뷰징 매체 끼리 공통 방문이 많다.
    - 어뷰징 매체군이 고립됨 (문제해결의 가능성 발견)
- 커뮤니티 탐지 -> 악성 커뮤니티 분류 -> 어뷰저 필터링
- 커뮤니티 탐지
  - WCC (Weakly Conneted Component) 알고리즘 사용해봤으나 SCC (Strongly) 가 제일 알맞음
- 악성 커뮤니티 분류
  - 도메인 전문가의 라벨링이 어느정도 필요했음
  - 커뮤니티 내부 연결도가 높음, 정상 매체 이용자들이 방문할 확률이 낮음, 이웃들끼리의 연결도가 높음
- 어뷰저군의 특성
  - 방문 횟수 자체가 많음
  - 하루에 더 다양한 매체를 방문함

## XAI
### [AI를 설명하면서 속도도 빠르게 할 순 없을까? SHAP 가속화 이야기 (feat. 산학협력)](https://if.kakao.com/session/16)
- Kernel SHAP 기반 이상거래 탐지 결과 이유 산출
  - 근데 시간이 오래걸림 -> 더 빠르게 만들어서 모니터링 시스템에서 사용할 수 있도록 (가속화 실험)
- SHAP 에 대한 개념설명
- KernelSHAP 에 대한 개념설명
- 가속화 방안
  - 엔지니어링 기반: 코드를 수정하여 속도업
  - 알고리즘 기반 (Amortized, Non-Amortized)
  - 하드웨어 기반
  - 엔지니어링과 Amortized 방법 사용
- 정확도, 속도를 평가지표
  - Cosine Similarity
  - Top-K Signed Rank Agreement
    - 두 설명결과의 상위 K개 feature 집합에서 동일한 부호(특성 기여도)와 순위가 공통적으로 포함된 feature 들의 비율
- 엔지니어링 기반으로 KernelSHAP 개선하여 정확도 보전, 알고리즘 기반으로 FastSHAP 개선하여 속도 개선
- 이들을 개선하여 SAMSHAP 개발
  - KernelSHAP 과 비슷한 성능이나 속도는 10배 빠르고 FastSHAP 보다 정확함

## ML platform
### [메시지 광고 추천 딥러닝 인퍼런스 서버 개선 - Jvm Onnx Runtime에서  Nvidia Triton 도입까지](https://if.kakao.com/session/15)
### [카카오 광고 AI 추천 MLOps 아키텍쳐 - Feature Store 편](https://if.kakao.com/session/20)
### [AI 기반 광고 추천 파이프라인에서 스파크 스트리밍의 배포 및 모니터링 전략](https://if.kakao.com/session/33)