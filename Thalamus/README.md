# Thalamus Engine (시상 엔진)

**Version**: 1.0.0-alpha  
**Status**: 소프트웨어 벤치마킹 단계 (물리적 하드웨어 테스트 미완)  
**License**: MIT License  
**Author**: GNJz (Qquarts)

---

## ⚠️ 중요 안내

**현재 상태**: 본 엔진은 소프트웨어 시뮬레이션 및 벤치마킹 단계에 있습니다.  
**물리적 하드웨어 테스트는 아직 완료되지 않았으며**, 실제 산업 환경에 적용하기 전에 추가 검증이 필요합니다.

본 프로젝트는 **계속 발전하는 구조**이며, 테스트 과정과 계획된 업그레이드를 통해 확장되어 갑니다.

---

## 📋 개요

**Thalamus Engine**은 산업용 센서 데이터 필터링 시스템을 목표로 하는 소프트웨어 엔진입니다. 대량의 센서 입력에서 중요한 정보만 선별하여 처리하는 기능을 제공합니다.

### 핵심 기능

- ✅ **감각 입력 필터링**: 중요 정보만 선별
- ✅ **주의 게이팅**: 에너지 기반 동적 임계값 조절
- ✅ **채널 제한**: 최대 N개만 통과 (과부하 방지)
- ✅ **현저성 계산**: 위협, 이름, 질문 등 자동 감지
- ✅ **에너지 기반 게이팅**: 에너지 부족 시 불필요한 감각 차단

---

## 🎯 예상 산업 활용 분야

**참고**: 아래는 본 엔진의 잠재적 활용 분야이며, 실제 적용을 위해서는 추가 검증이 필요합니다.

### 1. IoT 센서 데이터 필터링 (예상)
- 대량 센서 데이터에서 중요한 이벤트만 선별
- 배경 노이즈 자동 필터링
- 실시간 모니터링 시스템

### 2. 보안 시스템 (예상)
- CCTV 영상에서 이상 행동만 선별
- 보안 이벤트 우선순위 설정
- 위협 신호 자동 감지

### 3. 실시간 모니터링 (예상)
- 대량 로그에서 핵심 이벤트만 추출
- 시스템 부하 관리
- 동적 임계값 조절

---

## 🚀 빠른 시작

### 설치

```bash
pip install -r requirements.txt
```

### 기본 사용법

```python
from package.thalamus import (
    ThalamusEngine,
    ThalamusConfig,
    SensoryInput,
    ModalityType
)

# 설정
config = ThalamusConfig(
    gate_threshold=0.3,  # 게이트 임계값
    max_channels=5       # 최대 통과 채널 수
)

# 엔진 초기화
engine = ThalamusEngine(config)

# 센서 데이터 입력
inputs = [
    SensoryInput("위험! 온도 100도 초과", ModalityType.INTERNAL, intensity=0.9),
    SensoryInput("온도: 25도", ModalityType.INTERNAL, intensity=0.3),
]

# 필터링
outputs = engine.filter(inputs)

# 결과 확인
for out in outputs:
    print(f"{out.content}: 가중치 {out.attention_weight:.2f}")
```

---

## 📐 핵심 수식

### 1. 현저성 계산

```
S = base_salience × pattern_boost × intensity × arousal
```

- `base_salience`: 기본 현저성 (0~1)
- `pattern_boost`: 패턴 부스트 (위협은 2배)
- `intensity`: 입력 강도 (0~1)
- `arousal`: 각성 수준 (0~1)

### 2. 주의 가중치

```
W = attention_weight[modality] × focus_boost × (1 + salience)
```

- `attention_weight[modality]`: 양식별 주의 가중치
- `focus_boost`: 포커스 부스트 (1.5 if focused else 1.0)
- `salience`: 계산된 현저성

### 3. 동적 게이팅 (에너지 기반)

```
threshold = base_threshold × (1 + energy_deficit_factor)
energy_deficit_factor = max(0, (0.5 - energy) / 0.5)
```

- 에너지가 낮을수록 임계값이 높아져 불필요한 감각 차단

### 4. 게이팅

```
pass = (W ≥ threshold)
```

- 주의 가중치가 임계값 이상이면 통과

### 5. 채널 제한

```
output = top_k(passed_inputs, k=max_channels)
```

- 우선순위 상위 N개만 통과

---

## ⚙️ 설정 (ThalamusConfig)

### 주요 파라미터

| 파라미터 | 기본값 | 설명 |
|---------|--------|------|
| `gate_threshold` | 0.3 | 게이트 임계값 (0~1) |
| `max_channels` | 3 | 최대 통과 채널 수 |
| `salience_boost` | 1.5 | 현저성 부스트 배수 |
| `novelty_bonus` | 0.3 | 신규성 보너스 (0~1) |
| `attention_decay` | 0.1 | 주의 감쇠율 |
| `focus_boost` | 1.5 | 포커스 부스트 배수 |
| `energy_deficit_threshold` | 0.5 | 에너지 부족 임계값 |
| `energy_deficit_boost` | 0.5 | 에너지 부족 시 임계값 증가율 |

### 설정 예제

```python
# 엄격한 필터링 (높은 임계값)
strict_config = ThalamusConfig(
    gate_threshold=0.7,
    max_channels=2
)

# 관대한 필터링 (낮은 임계값)
lenient_config = ThalamusConfig(
    gate_threshold=0.2,
    max_channels=10
)
```

---

## 📊 API 문서

### ThalamusEngine

#### `filter(inputs: List[SensoryInput]) -> List[FilteredOutput]`

감각 입력 필터링 (메인 메서드)

**Args:**
- `inputs`: 감각 입력 목록

**Returns:**
- 필터링된 출력 목록 (게이트 통과한 것만)

#### `filter_single(content, modality, intensity, salience) -> Optional[FilteredOutput]`

단일 입력 필터링

#### `set_attention_focus(modality: ModalityType)`

주의 포커스 설정

#### `set_arousal(level: float)`

각성 수준 설정 (0~1)

#### `sleep_mode()`

수면 모드 (감각 차단)

#### `wake_up()`

각성

#### `get_state() -> Dict[str, Any]`

전체 상태 반환

#### `get_stats() -> Dict[str, Any]`

통계 반환

#### `reset()`

상태 리셋

---

## 🧪 예제

### 예제 1: 센서 데이터 필터링

```python
from package.thalamus import ThalamusEngine, ThalamusConfig, SensoryInput, ModalityType

config = ThalamusConfig(gate_threshold=0.3, max_channels=5)
engine = ThalamusEngine(config)

inputs = [
    SensoryInput("위험! 온도 100도 초과", ModalityType.INTERNAL, intensity=0.9),
    SensoryInput("온도: 25도", ModalityType.INTERNAL, intensity=0.3),
]

outputs = engine.filter(inputs)
for out in outputs:
    print(f"{out.content}: 가중치 {out.attention_weight:.2f}")
```

### 예제 2: 에너지 기반 게이팅

```python
class EnergyProvider:
    def __init__(self):
        self.energy = 1.0

energy = EnergyProvider()
config = ThalamusConfig(energy_deficit_threshold=0.5)
engine = ThalamusEngine(config, energy_provider=energy)

# 에너지가 낮으면 게이트 임계값 자동 증가
energy.energy = 0.3
outputs = engine.filter(inputs)  # 더 엄격한 필터링
```

자세한 예제는 `examples/` 폴더를 참고하세요.

---

## ⚠️ 현재 제한사항 및 주의사항

### 현재 상태
- **소프트웨어 벤치마킹 단계**: 물리적 하드웨어 테스트는 아직 완료되지 않았습니다.
- **시뮬레이션 환경**: 실제 센서 하드웨어와의 통합 테스트는 미완성 상태입니다.
- **성능 검증**: 대규모 실시간 환경에서의 성능 검증이 필요합니다.

### 기능적 제한사항
- 본 모듈은 **필터링 계층**이며, 단독 센서 시스템은 아닙니다.
- 대규모 경로 계획(Path Planning) 또는 의사결정 기능은 포함하지 않습니다.
- 센서 입력이 극단적으로 노이즈가 큰 경우, 상위 필터(Kalman 등)와 병행 사용을 권장합니다.
- 불연속 제어(discrete jump)가 잦은 시스템에서는 gain 튜닝이 필요할 수 있습니다.

### 향후 계획
- 물리적 하드웨어 통합 테스트
- 실시간 환경 성능 검증
- 대규모 데이터셋 벤치마킹

---

## ⏱️ 권장 시간 스케일

- 제어 주기(dt): 0.1ms ~ 10ms
- 필터링 주기: 센서 샘플링 주기와 동일
- 주의 감쇠: 제어 주기의 10~100배

---

## 🎛️ Gain 튜닝 가이드

- `gate_threshold` ↑ : 엄격한 필터링 (중요한 것만 통과)
- `max_channels` ↑ : 더 많은 채널 통과 (과부하 위험)
- `salience_boost` ↑ : 현저성 패턴 강조
- `novelty_bonus` ↑ : 신규성 보너스 증가
- `energy_deficit_boost` ↑ : 에너지 부족 시 더 엄격한 필터링

---

## 🔒 안전성 고려사항

**중요**: 본 모듈은 소프트웨어 시뮬레이션 단계이며, 실제 안전-중요(safety-critical) 시스템에 적용하기 전에 철저한 검증이 필요합니다.

- 본 모듈은 상위 시스템의 입력을 필터링하도록 설계되었으나, 실제 안정성 검증은 아직 완료되지 않았습니다.
- 실제 산업 환경 적용 시 추가 안전성 검증 및 인증이 필요할 수 있습니다.

---

## 🔮 향후 계획 및 로드맵

본 프로젝트는 계속 발전하는 구조이며, 다음 단계를 계획하고 있습니다:

### v1.1 (계획 중)
- 비선형 시스템용 adaptive threshold schedule
- Kalman / Observer 연동 인터페이스
- 다중 모달리티 통합 필터링

### v1.2+ (장기 계획)
- 물리적 하드웨어 통합 테스트
- 실시간 C/C++ 바인딩
- 대규모 실시간 환경 성능 검증
- 산업 표준 인증 준비

**참고**: 로드맵은 테스트 결과와 피드백에 따라 변경될 수 있습니다.

---

## 📚 참고 논문

- Sherman & Guillery (2006): Thalamus
- Crick (1984): Thalamus as gateway to consciousness

---

## 📄 라이선스

MIT License

---

## 👤 작성자

GNJz (Qquarts)

---

## 🔗 PHAM 블록체인 서명

이 Thalamus Engine은 **PHAM (Proof of Authorship & Merit) 블록체인 시스템**으로 서명되어 있습니다.

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
cat blockchain/pham_chain_thalamus_engine.json | jq '.'

# 기여도 통계 확인
python3 ../cookiie_brain/blockchain/pham_sign_v4.py --stats blockchain/pham_chain_thalamus_engine.json
```

---

**Made in GNJz** 🧠


---

---

# English Version

> [🇰🇷 한국어](#thalamus-engine-시상-엔진) | **🇺🇸 English**

> **Sensory data filtering system** — Selects only important information from massive sensor inputs

---

## 📋 Overview

**Thalamus Engine** filters large amounts of sensor data and selects only important information for processing.

### Core Features

| Feature | Description |
|---------|-------------|
| **Sensory Filtering** | Select only important information |
| **Attention Gating** | Dynamic threshold based on energy |
| **Channel Limiting** | Max N channels pass (overload prevention) |
| **Salience Calculation** | Auto-detect threats, names, questions |
| **Energy-based Gating** | Block unnecessary input when energy is low |

---

## 🎯 Use Cases

| Domain | Application |
|--------|-------------|
| **IoT Sensors** | Filter important events from massive sensor data |
| **Security Systems** | Select anomalies from CCTV feeds |
| **Real-time Monitoring** | Extract key events from logs |
| **Brain Simulation** | Model thalamic relay dysfunction |

---

## 🚀 Quick Start

```python
from thalamus import ThalamusEngine, ThalamusConfig, SensoryInput, ModalityType

config = ThalamusConfig(gate_threshold=0.3, max_channels=5)
engine = ThalamusEngine(config)

inputs = [
    SensoryInput("DANGER! Temperature 100°C", ModalityType.INTERNAL, intensity=0.9),
    SensoryInput("Temperature: 25°C", ModalityType.INTERNAL, intensity=0.3),
]

outputs = engine.filter(inputs)
for out in outputs:
    print(f"{out.content}: weight {out.attention_weight:.2f}")
```

---

## 🔬 Core Formulas

### Salience Calculation

```
salience = intensity × modality_weight + keyword_boost + urgency_factor
```

### Gate Decision

```
pass = (salience > threshold) AND (channel_count < max_channels)
```

---

## 📄 License

MIT License

---

## ✅ PHAM Blockchain Signature

Signed with **PHAM (Proof of Honest Authorship & Merit)**.

---

**Author**: GNJz (Qquarts)
