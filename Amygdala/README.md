# Amygdala Engine (편도체 엔진)

**Version**: 1.0.0-alpha  
**Status**: 소프트웨어 벤치마킹 단계 (물리적 하드웨어 테스트 미완)  
**License**: MIT License  
**Author**: GNJz (Qquarts)

---

## ⚠️ 중요 안내

**현재 상태**: 본 엔진은 소프트웨어 시뮬레이션 및 벤치마킹 단계에 있습니다.  
**테스트 환경**: 맥북에어에서 간단한 소프트웨어 테스트 후 업로드되었습니다.  
**물리적 하드웨어 테스트는 아직 완료되지 않았으며**, 실제 산업 환경에 적용하기 전에 추가 검증이 필요합니다.

본 프로젝트는 **계속 발전하는 구조**이며, 테스트 과정과 계획된 업그레이드를 통해 확장되어 갑니다.

---

## 📋 개요

**Amygdala Engine**은 산업용 감정/위협 분석 시스템을 목표로 하는 소프트웨어 엔진입니다. 텍스트에서 감정과 위협을 자동으로 감지하고 분석하는 기능을 제공합니다.

### 예상 핵심 기능

- ✅ **감정 분석**: Valence-Arousal 모델 기반 감정 분석
- ✅ **위협 감지**: 텍스트에서 위협 신호 자동 감지
- ✅ **중요도 가중치 계산**: 감정과 위협에 따른 기억 중요도 가중치
- ✅ **공포 조건화**: Pavlovian 조건화를 통한 학습
- ✅ **맥락적 소거**: 시간 기반 공포 기억 자동 소거

---

## 🎯 예상 산업 활용 분야

**참고**: 아래는 본 엔진의 잠재적 활용 분야이며, 실제 적용을 위해서는 추가 검증이 필요합니다.

### 1. 감정 분석 시스템 (예상)
- 고객 리뷰 감정 분석 (시뮬레이션 검증)
- 소셜 미디어 감정 모니터링 (이론적 검증)
- 콘텐츠 감정 분류 (이론적 검증)

### 2. 위협 탐지 시스템 (예상)
- 보안 이벤트 위협도 평가 (시뮬레이션 검증)
- 고객 불만 자동 감지 (이론적 검증)
- 이상 행동 감지 (이론적 검증)

### 3. 콘텐츠 필터링 (예상)
- 부정적 콘텐츠 자동 필터링 (시뮬레이션 검증)
- 자해/자살 신호 감지 (이론적 검증)
- 위험 콘텐츠 우선순위 설정 (이론적 검증)

### 4. 고객 서비스 자동화 (예상)
- 고객 메시지 우선순위 자동 설정 (시뮬레이션 검증)
- 감정 기반 응답 추천 (이론적 검증)
- 위협 신호 즉각 알림 (이론적 검증)

---

## 🚀 빠른 시작

### 설치

```bash
pip install -r requirements.txt
```

### 기본 사용법

```python
from package.amygdala import (
    AmygdalaEngine,
    AmygdalaConfig,
    EmotionState,
    ThreatSignal
)

# 설정
config = AmygdalaConfig(
    threat_threshold=0.4
)

# 엔진 초기화
engine = AmygdalaEngine(config)

# 위협 감지
threat = engine.detect_threat("위험! 조심해!")
if threat:
    print(f"위협 레벨: {threat.threat_level:.2f}")
    print(f"위협 유형: {threat.threat_type}")
    print(f"권장 반응: {threat.response}")

# 감정 분석
emotion = engine.process_emotion("오늘 정말 행복하다!")
print(f"지배적 감정: {emotion.dominant}")
print(f"감정 강도: {emotion.intensity:.2f}")

# 기억 강화
enhancement = engine.calculate_memory_enhancement(emotion, threat)
print(f"중요도 가중치: {enhancement:.2f}x")
```

---

## 📐 핵심 수식

### 1. 위협 점수

```
T = Σ(weight_i) / 2.0, clamped to [0, 1]
```

- `weight_i`: 위협 키워드별 가중치
- 자해/자살: 1.5, 직접 위협: 1.0, 사회적 위협: 0.7 등

### 2. 감정 강도

```
E = √(V² + A²)
```

- `V`: Valence (쾌-불쾌, -1 ~ +1)
- `A`: Arousal (각성도, 0 ~ 1)

### 3. 기억 중요도 가중치

```
M = 1 + α·E·(1 - e^(-β·T))
```

- `α`: 감정-기억 연결 강도 (기본값: 0.5)
- `β`: 위협 민감도 (기본값: 2.0)
- `E`: 감정 강도
- `T`: 위협 수준

### 4. 공포 조건화 (STDP)

```
Δw = A_+ · e^(-Δt/τ)
```

- `A_+`: LTP 강도 (기본값: 0.1)
- `τ`: 시간 상수 (기본값: 20.0ms)
- `Δt`: 자극 간 시간 차이

### 5. 맥락적 소거

```
Δstrength = -extinction_rate × (1 - co_occurrence_factor)
```

- `co_occurrence_factor`: 최근 동시 발생 여부 (1 또는 0)
- `extinction_rate`: 소거율 (기본값: 0.05)

---

## ⚙️ 설정 (AmygdalaConfig)

### 주요 파라미터

| 파라미터 | 기본값 | 설명 |
|---------|--------|------|
| `threat_threshold` | 0.4 | 위협 임계값 (0~1) |
| `A_plus` | 0.1 | LTP 강도 (공포 학습) |
| `A_minus` | 0.05 | LTD 강도 (소거) |
| `tau` | 20.0 | 시간 상수 (ms) |
| `alpha` | 0.5 | 감정-기억 연결 강도 |
| `beta` | 2.0 | 위협 민감도 |
| `extinction_time_window` | 3600.0 | 소거 시간 윈도우 (초) |
| `extinction_rate` | 0.05 | 수면 중 소거율 |
| `emotion_inertia` | 0.3 | 감정 관성 (이전 감정 유지 비율) |

### 설정 예제

```python
# 엄격한 위협 감지
strict_config = AmygdalaConfig(
    threat_threshold=0.6,
    beta=3.0  # 위협 민감도 증가
)

# 관대한 위협 감지
lenient_config = AmygdalaConfig(
    threat_threshold=0.2,
    beta=1.0  # 위협 민감도 감소
)
```

---

## 📊 API 문서

### AmygdalaEngine

#### `detect_threat(input_text: str) -> Optional[ThreatSignal]`

위협 감지

**Args:**
- `input_text`: 입력 텍스트

**Returns:**
- `ThreatSignal` if threat detected, `None` otherwise

#### `process_emotion(input_text: str) -> EmotionState`

감정 분석

**Args:**
- `input_text`: 입력 텍스트

**Returns:**
- `EmotionState` (dominant, valence, arousal, intensity)

#### `calculate_memory_enhancement(emotion, threat) -> float`

기억 강화 계수 계산

**Args:**
- `emotion`: EmotionState (None이면 현재 감정 사용)
- `threat`: ThreatSignal (None이면 위협 없음)

**Returns:**
- 기억 강화 계수 (1.0 ~ 2.0)

#### `enhance_memory(content: str, base_importance: float) -> Dict`

입력에 대해 감정 분석 후 기억 강화

**Args:**
- `content`: 기억할 내용
- `base_importance`: 기본 중요도

**Returns:**
- 강화된 기억 정보 딕셔너리

#### `condition_fear(stimulus: str, threat: str, strength: float)`

공포 조건화 (연합 학습)

#### `check_fear(stimulus: str) -> Optional[FearMemory]`

공포 기억 확인

#### `extinguish_fear(stimulus: str, rate: float)`

공포 소거 (안전 경험)

#### `contextual_extinction(current_time: Optional[float])`

맥락적 소거 (수면 중 자동 실행)

#### `get_state() -> Dict[str, Any]`

전체 상태 반환

#### `get_stats() -> Dict[str, Any]`

통계 반환

#### `reset()`

상태 리셋

---

## 🧪 예제

### 예제 1: 감정 분석

```python
from package.amygdala import AmygdalaEngine, AmygdalaConfig

config = AmygdalaConfig()
engine = AmygdalaEngine(config)

emotion = engine.process_emotion("오늘 정말 행복하다!")
print(f"감정: {emotion.dominant}, 강도: {emotion.intensity:.2f}")
```

### 예제 2: 위협 감지

```python
threat = engine.detect_threat("위험! 조심해!")
if threat:
    print(f"위협 레벨: {threat.threat_level:.2f}")
    print(f"권장 반응: {threat.response}")
```

### 예제 3: 고객 서비스 자동화

```python
# 고객 메시지 분석
result = engine.enhance_memory("이 제품이 너무 불만스러워요!", base_importance=0.5)

print(f"중요도: {result['enhanced_importance']:.2f}")
print(f"감정: {result['emotion']['dominant']}")
if result['threat']['detected']:
    print(f"위협: {result['threat']['type']}")
```

자세한 예제는 `examples/` 폴더를 참고하세요.

---

## ⚠️ 현재 제한사항 및 주의사항

### 현재 상태
- **소프트웨어 벤치마킹 단계**: 물리적 하드웨어 테스트는 아직 완료되지 않았습니다.
- **시뮬레이션 환경**: 실제 텍스트 처리 시스템과의 통합 테스트는 미완성 상태입니다.
- **성능 검증**: 대규모 실시간 환경에서의 성능 검증이 필요합니다.

### 기능적 제한사항
- 본 모듈은 **감정/위협 분석 계층**이며, 완전한 NLP 시스템은 아닙니다.
- 키워드 기반 감지 방식으로, 문맥 이해는 제한적입니다.
- 다국어 지원은 기본 키워드만 포함되어 있으며, 확장이 필요할 수 있습니다.
- 부정어 처리 로직이 완벽하지 않을 수 있습니다.

### 향후 계획
- 물리적 하드웨어 통합 테스트
- 실시간 환경 성능 검증
- 대규모 데이터셋 벤치마킹
- 딥러닝 기반 감정 분석 모델 통합 (선택적)

---

## ⏱️ 권장 시간 스케일

- 텍스트 처리 주기: 실시간 또는 배치 처리
- 감정 감쇠: 시간 상수 0.1 (약 10초)
- 공포 소거: 시간 윈도우 3600초 (1시간)

---

## 🎛️ Gain 튜닝 가이드

- `threat_threshold` ↑ : 엄격한 위협 감지 (중요한 것만 감지)
- `beta` ↑ : 위협 민감도 증가 (위협에 더 민감하게 반응)
- `alpha` ↑ : 감정-기억 연결 강화 (감정이 기억에 더 큰 영향)
- `emotion_inertia` ↑ : 감정 관성 증가 (이전 감정이 더 오래 유지)
- `extinction_rate` ↑ : 공포 소거 속도 증가

---

## 🔒 안전성 고려사항

**중요**: 본 모듈은 소프트웨어 시뮬레이션 단계이며, 실제 안전-중요(safety-critical) 시스템에 적용하기 전에 철저한 검증이 필요합니다.

- 자해/자살 신호 감지는 민감한 영역이므로, 실제 적용 시 전문가 검토가 필요합니다.
- 위협 감지의 오탐(false positive)과 미탐(false negative) 비율을 실제 환경에서 검증해야 합니다.
- 실제 산업 환경 적용 시 추가 안전성 검증 및 인증이 필요할 수 있습니다.

---

## 🔮 향후 계획 및 로드맵

본 프로젝트는 계속 발전하는 구조이며, 다음 단계를 계획하고 있습니다:

### v1.1 (계획 중)
- 딥러닝 기반 감정 분석 모델 통합 (선택적)
- 다국어 지원 확장
- 문맥 이해 개선

### v1.2+ (장기 계획)
- 물리적 하드웨어 통합 테스트
- 대규모 실시간 환경 성능 검증
- 산업 표준 인증 준비

**참고**: 로드맵은 테스트 결과와 피드백에 따라 변경될 수 있습니다.

---

## 📚 참고 논문

- Russell's Circumplex Model (감정 2D 모델)
- Pavlovian Conditioning (공포 학습)
- Extinction Learning (소거 학습)

---

## 📄 라이선스

MIT License

---

## 👤 작성자

GNJz (Qquarts)

---

## 🔗 PHAM 블록체인 서명

이 Amygdala Engine은 **PHAM (Proof of Authorship & Merit) 블록체인 시스템**으로 서명되어 있습니다.

### 블록체인 정보

- **블록체인 체인 파일**: `blockchain/pham_chain_*.json`
- **4-Signal Scoring**: Byte(25%) + Text(35%) + AST(30%) + Exec(10%)
- **IPFS 저장**: 모든 코드 버전이 IPFS에 영구 보존됨
- **자세한 내용**: `BLOCKCHAIN_INFO.md` 참조

### 블록체인 기반 기여도 시스템

**라이선스**: 오픈소스 (MIT License)  
**사용 제한**: 없음  
**로열티 요구**: 없음

**수익 발생 시 기여도 시스템**:
- 코드 기여도와 제품 기여도(상용화, 홍보, 마케팅, 판매 등)가 블록체인에 기록되어 합산됩니다
- 모든 기여 활동이 블록체인에 기록되어 투명하게 관리됩니다
- 블록체인으로 계산된 기여도에 따라 수익이 자동으로 분배됩니다

**시스템 구조**: 블록체인 기반 기여도 시스템은 업그레이드 가능한 구조로, 초기 설계 단계이며 실제 상용화 경험을 통해 발전할 예정입니다.

**GNJz 기여도 원칙**:
- 최초 코드 작성자 GNJz (Qquarts)의 기여도는 블록체인으로 계산된 결과, 총 기여도 중 최대 6%를 넘지 않습니다
- 블록체인으로 검증 가능한 기여도 상한선
- 모든 기여도 계산은 블록체인에 기록되어 검증 가능

### 블록체인 체인 확인

```bash
# 블록체인 체인 파일 확인
cat blockchain/pham_chain_amygdala_engine.json | jq '.'

# 기여도 통계 확인
python3 ../cookiie_brain/blockchain/pham_sign_v4.py --stats blockchain/pham_chain_amygdala_engine.json
```

---

**Made in GNJz** 🧠


---

---

# English Version

> [🇰🇷 한국어](#amygdala-engine-편도체-엔진) | **🇺🇸 English**

> **Emotion processing and threat detection system** — Rapid emotional response engine

---

## 📋 Overview

**Amygdala Engine** processes emotional signals and detects threats. It enables rapid emotional responses before conscious processing.

### Core Features

| Feature | Description |
|---------|-------------|
| **Threat Detection** | Rapid identification of danger signals |
| **Emotional Memory** | Store and retrieve emotional associations |
| **Fear Conditioning** | Learn threat patterns |
| **Arousal Modulation** | Regulate physiological arousal |
| **Valence Processing** | Positive/negative emotion classification |

---

## 🎯 Use Cases

| Domain | Application |
|--------|-------------|
| **Security AI** | Real-time threat level assessment |
| **Sentiment Analysis** | Emotional content classification |
| **Chatbots** | Emotionally-aware responses |
| **Brain Simulation** | PTSD hyperarousal, anxiety modeling |

---

## 🚀 Quick Start

```python
from amygdala import AmygdalaEngine, AmygdalaConfig, EmotionalStimulus

config = AmygdalaConfig(threat_sensitivity=0.7, fear_threshold=0.5)
engine = AmygdalaEngine(config)

stimulus = EmotionalStimulus(
    content="loud unexpected noise",
    valence=-0.8,
    arousal=0.9
)

response = engine.process(stimulus)
print(f"Threat level: {response.threat_level:.2f}")
print(f"Fear response: {response.fear_triggered}")
```

---

## 🔬 Core Formulas

### Threat Assessment

```
threat_level = base_threat × sensitivity × arousal_multiplier
```

### Fear Conditioning

```
association_strength += learning_rate × (actual_outcome - predicted_outcome)
```

---

## 📄 License

MIT License

---

## ✅ PHAM Blockchain Signature

Signed with **PHAM (Proof of Honest Authorship & Merit)**.

---

**Author**: GNJz (Qquarts)
