# Cognitive Kernel

> **🇰🇷 한국어** | [🇺🇸 English](#english-version)

> **인지 연구 플랫폼** — 기억, 주의력, 감정의 동역학적 상호작용을 탐구하기 위한 모듈형 시뮬레이션 프레임워크

---

## 🧠 개요

**Cognitive Kernel**은 인간 인지 시스템의 동역학적 특성을 탐구하기 위한 **모듈형 시뮬레이션 프레임워크**입니다.

이 프로젝트는 인지 현상의 **원인과 메커니즘**을 분석하는 데 초점을 맞추며,
"정답을 제시하는 것"보다 **"관찰과 유추를 유도하는 도구"**를 제공하는 것을 목표로 합니다.

### ⚠️ 연구 목적 명시

```
이 프레임워크는 인지과학 및 계산신경과학 연구를 위한 시뮬레이션 도구입니다.
- 실제 뇌의 완전한 모델이 아닙니다
- 임상 진단 도구가 아닙니다
- 각 모듈의 수식은 "최소 유효 모델(Minimum Valid Model)"을 구현한 것입니다
- 모든 결과는 추가 검증이 필요합니다
```

---

## 🎬 구조적 비유

각 모듈은 뇌 영역의 특정 기능을 추상화한 것으로, 그 역할은 다음과 같이 해석될 수 있습니다:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        🧠 Cognitive Kernel                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   📡 Thalamus         →  감각 정보의 선별적 통과 (게이팅)             │
│   😨 Amygdala         →  정서적 현저성 부여 (위협 감지)              │
│   ⚡ Hypothalamus      →  항상성 상태 추적 (에너지, 스트레스)         │
│                         ↓                                           │
│   🎞️ Panorama          →  시간축 사건 기록 (에피소드 기억)            │
│   💡 MemoryRank        →  연결 기반 중요도 계산 (의미 기억)           │
│                         ↓                                           │
│   🎬 PFC               →  정보 통합 및 행동 선택                      │
│   👷 BasalGanglia      →  반복 행동의 자동화 (습관)                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 모듈 구성

| 모듈 | 추상화 대상 | 핵심 수식 | 상태 |
|------|-------------|----------|------|
| **[Thalamus](./Thalamus/)** | 감각 게이팅 | Salience Filtering | ✅ v1.0 |
| **[Amygdala](./Amygdala/)** | 공포 학습 | Rescorla-Wagner | ✅ v1.0 |
| **[Hypothalamus](./Hypothalamus/)** | 항상성 | HPA Axis Dynamics | ✅ v1.0 |
| **[Panorama](./Panorama/)** | 에피소드 기억 | Exponential Decay | ✅ v1.0 |
| **[MemoryRank](./MemoryRank/)** | 중요도 계산 | PageRank | ✅ v1.0 |
| **[PFC](./PFC/)** | 의사결정 | Softmax Utility | ✅ v1.0 |
| **[BasalGanglia](./BasalGanglia/)** | 습관 학습 | TD-Learning | ✅ v1.0 |

### 📚 이론적 기반

각 모듈의 수학적 모델과 신경과학적 근거는 [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md)에서 확인할 수 있습니다.

---

## 🔧 엔지니어링 관점

### 아키텍처 설계 원칙

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Cognitive Kernel Architecture                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [Input Layer]                                                      │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Thalamus (Gateway)                                          │   │
│  │  - Input validation & filtering                              │   │
│  │  - Rate limiting (max_channels)                              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Processing Layer                                            │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │  Amygdala   │  │ Hypothalamus│  │  Panorama   │          │   │
│  │  │  (Tagging)  │  │  (State)    │  │  (Storage)  │          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Decision Layer                                              │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │ MemoryRank  │→ │    PFC      │→ │BasalGanglia │          │   │
│  │  │  (Ranking)  │  │ (Decision)  │  │  (Action)   │          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  [Output: Action / Response]                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 프로그래밍 패턴

| 패턴 | 적용 모듈 | 설명 |
|------|----------|------|
| **Strategy** | PFC | 행동 선택 알고리즘 교체 가능 |
| **Observer** | Hypothalamus | 상태 변화 감지 및 알림 |
| **Pipeline** | 전체 | 모듈 간 데이터 흐름 |
| **State Machine** | BasalGanglia | 습관 상태 전이 |
| **Factory** | Config 클래스 | 설정 기반 인스턴스 생성 |

### 코드 통합 예시

```python
# 1. 개별 모듈 사용
from memoryrank import MemoryRankEngine, MemoryRankConfig
from pfc import PFCEngine, Action

# 메모리 중요도 계산
memory_engine = MemoryRankEngine(MemoryRankConfig(damping=0.85))
memory_engine.build_graph(edges, node_attributes)
top_memories = memory_engine.get_top_memories(k=5)

# PFC에 전달하여 의사결정
pfc = PFCEngine()
pfc.load_from_memoryrank(top_memories)
action, inhibited, probs = pfc.process(
    top_memories=top_memories,
    candidate_actions=[Action(id="1", name="respond", expected_reward=0.8)],
    current_context_conflict_signal=0.2
)

# 2. 파이프라인 통합
from examples.integrated_pipeline import CognitiveKernel

kernel = CognitiveKernel()
result = kernel.process_event(
    event_type="user_query",
    content="중요한 질문입니다",
    context={"urgency": 0.8}
)
```

### API 설계 원칙

```python
# 모든 엔진은 동일한 인터페이스 패턴을 따름
class EngineInterface:
    def __init__(self, config: Optional[Config] = None): ...
    def process(self, input_data) -> Dict: ...        # 단일 처리
    def update(self, dt: float = 0.1) -> None: ...    # 시간 경과
    def get_state(self) -> Dict: ...                  # 상태 조회
    def reset(self) -> None: ...                      # 초기화
```

---

## 🏭 산업 활용 시나리오

### AI 에이전트 / 챗봇

| 문제 | Cognitive Kernel 해결책 |
|------|------------------------|
| 대화 맥락 유실 | **Panorama**: 시간순 대화 기록 + 에피소드 분할 |
| 중요 정보 누락 | **MemoryRank**: 연결 기반 중요도 순위 |
| 일관성 없는 응답 | **PFC**: 작업 기억 기반 컨텍스트 유지 |
| 반복 질문 학습 | **BasalGanglia**: 자주 묻는 질문 패턴 자동화 |

```python
# 챗봇 통합 예시
class CognitiveAgent:
    def __init__(self):
        self.panorama = PanoramaMemoryEngine()
        self.memory_rank = MemoryRankEngine()
        self.pfc = PFCEngine()
    
    def respond(self, user_input: str) -> str:
        # 1. 대화 기록
        self.panorama.append_event(time.time(), "user", {"text": user_input})
        
        # 2. 관련 기억 검색
        relevant = self.memory_rank.get_top_memories(k=5)
        
        # 3. 응답 결정
        self.pfc.load_from_memoryrank(relevant)
        action = self.pfc.select_action(candidate_responses)
        
        return action.name
```

### 추천 시스템

| 기존 방식 | Cognitive Kernel 접근 |
|----------|----------------------|
| 협업 필터링 | **MemoryRank**: 아이템 연결 그래프 중요도 |
| 콘텐츠 기반 | **Amygdala**: 감정/선호도 태깅 |
| 세션 기반 | **Panorama**: 시간축 행동 패턴 |
| 강화 학습 | **BasalGanglia**: TD-Learning 기반 선호 학습 |

### 게임 AI / NPC

| 기능 | 적용 모듈 | 효과 |
|------|----------|------|
| **장기 기억** | Panorama + MemoryRank | NPC가 플레이어와의 과거 상호작용 기억 |
| **감정 반응** | Amygdala | 상황에 따른 감정 표현 |
| **피로/욕구** | Hypothalamus | 자연스러운 행동 동기 |
| **습관 형성** | BasalGanglia | 반복 행동 자동화 |
| **의사결정** | PFC | 목표 기반 행동 선택 |

### IoT / 스마트 시스템

```
센서 데이터 → Thalamus (필터링) → Panorama (기록) → MemoryRank (이상 탐지)
                                                          ↓
                                         BasalGanglia (자동 대응) ← PFC (판단)
```

| 응용 | 설명 |
|------|------|
| **스마트홈** | 사용자 패턴 학습, 자동 환경 조절 |
| **산업 모니터링** | 이상 징후 감지, 우선순위 알림 |
| **헬스케어** | 생체 신호 패턴 분석, 이상 상태 예측 |

### 확장 가능한 통합

```python
# 기존 시스템에 플러그인 방식으로 통합
class YourExistingSystem:
    def __init__(self):
        # Cognitive Kernel 모듈만 선택적 사용
        self.memory = MemoryRankEngine()  # 중요도 계산만 사용
        self.state = HypothalamusEngine()  # 상태 관리만 사용
    
    def process(self, data):
        # 기존 로직에 인지 기능 추가
        importance = self.memory.calculate_importance()
        energy = self.state.get_energy_state()
        
        if energy['is_critical']:
            return self.low_power_mode(data)
        else:
            return self.full_processing(data, importance)
```

---

## 🔬 연구 활용 예시

이 프레임워크를 통해 다음과 같은 질문을 탐구할 수 있습니다:

### 메커니즘 탐구

| 관찰 대상 | 탐구 가능한 질문 |
|-----------|-----------------|
| **PTSD 패턴** | 외상 기억의 침습은 어떤 조건에서 강화되는가? |
| **우울 패턴** | 에너지 고갈과 부정 편향은 어떻게 상호작용하는가? |
| **ADHD 패턴** | 주의 불안정성은 보상 예측 오차와 관련이 있는가? |

### 시뮬레이션 예시

```python
# Normal vs PTSD 시나리오 비교
python examples/full_brain_simulation.py
```

출력에서 관찰되는 차이점:
- 스트레스 최대값 (0.44 vs 0.80)
- 과각성 이벤트 수 (1 vs 3)
- 인지 효율성 평균 (0.71 vs 0.61)

**이 수치들은 "진단 기준"이 아니라, 시스템 동역학의 차이를 관찰하기 위한 지표입니다.**

---

## 🚀 Quick Start

```bash
git clone https://github.com/qquartsco-svg/Cognitive_Kernel.git
cd Cognitive_Kernel

# 기본 파이프라인 (4개 엔진)
python examples/integrated_pipeline.py

# 전체 뇌 시뮬레이션 (7개 엔진)
python examples/full_brain_simulation.py
```

---

## 📁 프로젝트 구조

```
Cognitive_Kernel/
├── docs/
│   ├── ARCHITECTURE.md        # 이론적 기반, 수식, 참고 문헌
│   ├── ROADMAP.md             # 구현 계획
│   └── VERIFICATION_STATUS.md # 이론↔코드 일치 검증
├── examples/
│   ├── integrated_pipeline.py # 4-엔진 통합
│   └── full_brain_simulation.py # 7-엔진 시뮬레이션
├── tests/
│   └── test_mathematical_models.py # 수식 검증
├── Thalamus/
├── Amygdala/
├── Hypothalamus/
├── Panorama/
├── MemoryRank/
├── PFC/
└── BasalGanglia/
```

---

## 📄 License

MIT License

---

## 🔐 PHAM Blockchain Signature

모든 핵심 모듈은 **PHAM (Proof of Honest Authorship & Merit)** 블록체인 서명이 완료되어 있습니다.

---

## 👤 Author

**GNJz (Qquarts)** - GitHub: [@qquartsco-svg](https://github.com/qquartsco-svg)

---

---

# English Version

> [🇰🇷 한국어](#cognitive-kernel) | **🇺🇸 English**

> **Cognitive Research Platform** — A modular simulation framework for exploring dynamic interactions of memory, attention, and emotion

---

## 🧠 Overview

**Cognitive Kernel** is a **modular simulation framework** for exploring the dynamic properties of human cognitive systems.

This project focuses on **analyzing causes and mechanisms** of cognitive phenomena,
aiming to provide **"a tool that induces observation and inference"** rather than "presenting definitive answers."

### ⚠️ Research Purpose Statement

```
This framework is a simulation tool for cognitive science and computational neuroscience research.
- It is NOT a complete model of the actual brain
- It is NOT a clinical diagnostic tool
- Each module implements a "Minimum Valid Model" of the target function
- All results require further validation
```

---

## 🎬 Structural Metaphor

Each module abstracts specific functions of brain regions. Their roles may be interpreted as follows:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        🧠 Cognitive Kernel                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   📡 Thalamus         →  Selective passage of sensory info (gating) │
│   😨 Amygdala         →  Emotional salience assignment              │
│   ⚡ Hypothalamus      →  Homeostatic state tracking                 │
│                         ↓                                           │
│   🎞️ Panorama          →  Timeline event recording                   │
│   💡 MemoryRank        →  Connection-based importance calculation    │
│                         ↓                                           │
│   🎬 PFC               →  Information integration & action selection │
│   👷 BasalGanglia      →  Automation of repeated behaviors (habit)   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Modules

| Module | Abstraction Target | Core Formula | Status |
|--------|-------------------|--------------|--------|
| **[Thalamus](./Thalamus/)** | Sensory gating | Salience Filtering | ✅ v1.0 |
| **[Amygdala](./Amygdala/)** | Fear learning | Rescorla-Wagner | ✅ v1.0 |
| **[Hypothalamus](./Hypothalamus/)** | Homeostasis | HPA Axis Dynamics | ✅ v1.0 |
| **[Panorama](./Panorama/)** | Episodic memory | Exponential Decay | ✅ v1.0 |
| **[MemoryRank](./MemoryRank/)** | Importance calculation | PageRank | ✅ v1.0 |
| **[PFC](./PFC/)** | Decision making | Softmax Utility | ✅ v1.0 |
| **[BasalGanglia](./BasalGanglia/)** | Habit learning | TD-Learning | ✅ v1.0 |

### 📚 Theoretical Foundation

Mathematical models and neuroscience references for each module can be found in [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md).

---

## 🔧 Engineering Perspective

### Architecture Design Principles

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Cognitive Kernel Architecture                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [Input Layer]                                                      │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Thalamus (Gateway)                                          │   │
│  │  - Input validation & filtering                              │   │
│  │  - Rate limiting (max_channels)                              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Processing Layer                                            │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │  Amygdala   │  │ Hypothalamus│  │  Panorama   │          │   │
│  │  │  (Tagging)  │  │  (State)    │  │  (Storage)  │          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Decision Layer                                              │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │ MemoryRank  │→ │    PFC      │→ │BasalGanglia │          │   │
│  │  │  (Ranking)  │  │ (Decision)  │  │  (Action)   │          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     ▼                                                               │
│  [Output: Action / Response]                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Programming Patterns

| Pattern | Applied Module | Description |
|---------|---------------|-------------|
| **Strategy** | PFC | Swappable action selection algorithms |
| **Observer** | Hypothalamus | State change detection & notification |
| **Pipeline** | All | Data flow between modules |
| **State Machine** | BasalGanglia | Habit state transitions |
| **Factory** | Config classes | Configuration-based instance creation |

### Code Integration Example

```python
# 1. Individual module usage
from memoryrank import MemoryRankEngine, MemoryRankConfig
from pfc import PFCEngine, Action

# Calculate memory importance
memory_engine = MemoryRankEngine(MemoryRankConfig(damping=0.85))
memory_engine.build_graph(edges, node_attributes)
top_memories = memory_engine.get_top_memories(k=5)

# Pass to PFC for decision making
pfc = PFCEngine()
pfc.load_from_memoryrank(top_memories)
action, inhibited, probs = pfc.process(
    top_memories=top_memories,
    candidate_actions=[Action(id="1", name="respond", expected_reward=0.8)],
    current_context_conflict_signal=0.2
)

# 2. Pipeline integration
from examples.integrated_pipeline import CognitiveKernel

kernel = CognitiveKernel()
result = kernel.process_event(
    event_type="user_query",
    content="Important question",
    context={"urgency": 0.8}
)
```

### API Design Principles

```python
# All engines follow the same interface pattern
class EngineInterface:
    def __init__(self, config: Optional[Config] = None): ...
    def process(self, input_data) -> Dict: ...        # Single processing
    def update(self, dt: float = 0.1) -> None: ...    # Time progression
    def get_state(self) -> Dict: ...                  # State query
    def reset(self) -> None: ...                      # Reset
```

---

## 🏭 Industrial Application Scenarios

### AI Agents / Chatbots

| Problem | Cognitive Kernel Solution |
|---------|--------------------------|
| Lost conversation context | **Panorama**: Chronological dialogue + episode segmentation |
| Missing important info | **MemoryRank**: Connection-based importance ranking |
| Inconsistent responses | **PFC**: Working memory-based context maintenance |
| Learning repeated queries | **BasalGanglia**: FAQ pattern automation |

```python
# Chatbot integration example
class CognitiveAgent:
    def __init__(self):
        self.panorama = PanoramaMemoryEngine()
        self.memory_rank = MemoryRankEngine()
        self.pfc = PFCEngine()
    
    def respond(self, user_input: str) -> str:
        # 1. Record conversation
        self.panorama.append_event(time.time(), "user", {"text": user_input})
        
        # 2. Search relevant memories
        relevant = self.memory_rank.get_top_memories(k=5)
        
        # 3. Decide response
        self.pfc.load_from_memoryrank(relevant)
        action = self.pfc.select_action(candidate_responses)
        
        return action.name
```

### Recommendation Systems

| Traditional Approach | Cognitive Kernel Approach |
|---------------------|--------------------------|
| Collaborative filtering | **MemoryRank**: Item graph importance |
| Content-based | **Amygdala**: Emotion/preference tagging |
| Session-based | **Panorama**: Timeline behavior patterns |
| Reinforcement learning | **BasalGanglia**: TD-Learning preference learning |

### Game AI / NPCs

| Feature | Applied Module | Effect |
|---------|---------------|--------|
| **Long-term memory** | Panorama + MemoryRank | NPC remembers past player interactions |
| **Emotional reactions** | Amygdala | Context-appropriate emotional expressions |
| **Fatigue/Needs** | Hypothalamus | Natural behavior motivation |
| **Habit formation** | BasalGanglia | Repeated behavior automation |
| **Decision making** | PFC | Goal-based action selection |

### IoT / Smart Systems

```
Sensor data → Thalamus (filter) → Panorama (record) → MemoryRank (anomaly detection)
                                                              ↓
                                         BasalGanglia (auto-response) ← PFC (judgment)
```

| Application | Description |
|-------------|-------------|
| **Smart Home** | User pattern learning, automatic environment control |
| **Industrial Monitoring** | Anomaly detection, priority alerting |
| **Healthcare** | Biosignal pattern analysis, abnormal state prediction |

### Extensible Integration

```python
# Plug-in style integration with existing systems
class YourExistingSystem:
    def __init__(self):
        # Selectively use Cognitive Kernel modules
        self.memory = MemoryRankEngine()   # Use only importance calculation
        self.state = HypothalamusEngine()  # Use only state management
    
    def process(self, data):
        # Add cognitive features to existing logic
        importance = self.memory.calculate_importance()
        energy = self.state.get_energy_state()
        
        if energy['is_critical']:
            return self.low_power_mode(data)
        else:
            return self.full_processing(data, importance)
```

---

## 🔬 Research Application Examples

This framework enables exploration of questions such as:

### Mechanism Exploration

| Observation Target | Explorable Questions |
|-------------------|---------------------|
| **PTSD patterns** | Under what conditions is intrusive memory reinforced? |
| **Depression patterns** | How do energy depletion and negative bias interact? |
| **ADHD patterns** | Is attention instability related to reward prediction error? |

### Simulation Example

```python
# Compare Normal vs PTSD scenarios
python examples/full_brain_simulation.py
```

Observable differences in output:
- Maximum stress (0.44 vs 0.80)
- Hyperarousal events (1 vs 3)
- Mean cognitive efficiency (0.71 vs 0.61)

**These values are NOT "diagnostic criteria" but indicators for observing system dynamics differences.**

---

## 🚀 Quick Start

```bash
git clone https://github.com/qquartsco-svg/Cognitive_Kernel.git
cd Cognitive_Kernel

# Basic pipeline (4 engines)
python examples/integrated_pipeline.py

# Full brain simulation (7 engines)
python examples/full_brain_simulation.py
```

---

## 📁 Project Structure

```
Cognitive_Kernel/
├── docs/
│   ├── ARCHITECTURE.md        # Theoretical foundation, formulas, references
│   ├── ROADMAP.md             # Implementation plan
│   └── VERIFICATION_STATUS.md # Theory↔Code verification
├── examples/
│   ├── integrated_pipeline.py # 4-engine integration
│   └── full_brain_simulation.py # 7-engine simulation
├── tests/
│   └── test_mathematical_models.py # Formula verification
├── Thalamus/
├── Amygdala/
├── Hypothalamus/
├── Panorama/
├── MemoryRank/
├── PFC/
└── BasalGanglia/
```

---

## 📄 License

MIT License

---

## 🔐 PHAM Blockchain Signature

All core modules are signed with **PHAM (Proof of Honest Authorship & Merit)** blockchain.

---

## 👤 Author

**GNJz (Qquarts)** - GitHub: [@qquartsco-svg](https://github.com/qquartsco-svg)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a Pull Request.

---

## 📜 Citation

If you use this framework in research, please consider citing:

```
Cognitive Kernel: A Modular Simulation Framework for Cognitive Dynamics
GNJz (Qquarts), 2025
https://github.com/qquartsco-svg/Cognitive_Kernel
```
