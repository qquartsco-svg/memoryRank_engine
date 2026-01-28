# Panorama Memory Engine

> **"언제, 무슨 일이, 어떤 순서로?"** — 시간축 기반 에피소드 기억 엔진

---

## 🎬 기억의 영화관 비유

```
┌─────────────────────────────────────────────────────────────┐
│                    🧠 기억의 영화관                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   📽️ Panorama (필름)                                        │
│   ├─ 삶의 모든 순간을 시간순으로 기록                          │
│   ├─ "그때 무슨 일이 있었지?" → 필름 앞뒤로 돌려 검색          │
│   └─ 스스로 판단하지 않음, 그냥 기록된 순서대로 존재            │
│                         ↓                                   │
│   💡 MemoryRank (조광기 + 편집자)                             │
│   ├─ 수만 개 필름 프레임 중 어디에 조명을 비출지 결정           │
│   ├─ "이 장면은 감정이 강렬했어" (Emotion)                    │
│   ├─ "이 장면은 방금 찍은 거야" (Recency)                     │
│   └─ 가장 밝은 장면 → 의식(스크린)에 떠오름                    │
│                         ↓                                   │
│   🎬 PFC (영사기 + 감독) [다음 구현 예정]                      │
│   ├─ 조명 비춰진 필름을 스크린에 투사 (추론)                   │
│   └─ 다음에 어떤 장면을 찍을지 결정 (계획)                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 두 엔진이 만드는 현상

| Panorama (필름) 상태 | MemoryRank (조광기) 상태 | 결과 |
|---------------------|------------------------|------|
| 과거 나쁜 기억 존재 | emotion 가중치 과다 | **PTSD**: 특정 공포 장면만 계속 스크린 점령 |
| 방금 일어난 일 기록 | recency 정상 작동 | **정상**: 현재 상황 명확히 파악 |
| 여러 에피소드 기록 | frequency 점수 낮음 | **건망증**: 필름은 있지만 조명 약해 선명하지 않음 |

---

## Why This Solves Your Problem

| 문제 상황 | 이 엔진이 제공하는 해결책 |
|----------|-------------------------|
| "어제 오후 3~5시에 무슨 일이 있었지?" | query_range(t_start, t_end) → 해당 시간대 이벤트 즉시 조회 |
| "사용자 세션을 처음부터 재생하고 싶다" | get_episode(session_id) → 시간 순 이벤트 리플레이 |
| "자연스러운 대화 단위로 로그를 묶고 싶다" | segment_episodes() → 시간 갭 기반 자동 분할 |
| "최근에 일어난 일일수록 중요하게 처리하고 싶다" | get_importance_scores() → 지수 감쇠 적용 중요도 |
| "PTSD 외상 전후 기억 흐름을 분석하고 싶다" | 구간 쿼리 + 에피소드 분석 조합 |

---

## Quick Start

### 1. 설치

\`\`\`bash
git clone https://github.com/qquartsco-svg/Panorama_Memory_Engine.git
cd Panorama_Memory_Engine
# 외부 의존성 없음 (Python 3.8+ 표준 라이브러리만 사용)
\`\`\`

### 2. 기본 사용법

\`\`\`python
from panorama import PanoramaMemoryEngine, PanoramaConfig

# 엔진 초기화 (30분 갭으로 에피소드 분할)
engine = PanoramaMemoryEngine(PanoramaConfig(time_gap_threshold=1800))

# 이벤트 추가
import time
t = time.time()
engine.append_event(t, "user_action", {"action": "click", "target": "submit_btn"})
engine.append_event(t + 5, "state_change", {"state": "loading"})
engine.append_event(t + 10, "api_response", {"status": 200, "data": "success"})

# 시간 구간 쿼리 (필름 앞뒤로 돌리기)
events = engine.query_range(t, t + 60)

# 최근 이벤트 조회
recent = engine.get_recent(5)

# 에피소드 자동 분할
episodes = engine.segment_episodes(method="time_gap")
\`\`\`

### 3. 실행 테스트

\`\`\`bash
python test_panorama_engine.py
\`\`\`

---

## Output Example

\`\`\`
============================================================
Panorama Memory Engine v1.0 - Test
============================================================

[1] 이벤트 추가
  + session_start at t=0s → a1b2c3d4...
  + action at t=2s → e5f6g7h8...

총 이벤트 수: 8

[2] 구간 쿼리: t=0~10초
  - session_start at t=0s
  - action at t=2s
  - action at t=5s
  - state_change at t=8s

[3] 에피소드 자동 분할 (time_gap=10초)
  Episode 1: 4 events, duration=8s
  Episode 2: 3 events, duration=5s
  Episode 3: 1 events, duration=0s

✅ 테스트 완료
\`\`\`

---

## Use Cases

### 산업/상용

| 분야 | 활용 시나리오 |
|------|--------------|
| **사용자 행동 분석** | 세션 리플레이, 퍼널 분석, 이탈 지점 탐지 |
| **챗봇/대화 시스템** | 대화 히스토리 관리, 문맥 유지, 세션 요약 |
| **로그 분석** | 시간대별 이상 탐지, 인시던트 타임라인 재구성 |
| **게임** | 플레이어 행동 기록, 리플레이 시스템 |

### 연구/의료

| 분야 | 활용 시나리오 |
|------|--------------|
| **PTSD 연구** | 외상 전후 기억 흐름 분석, 플래시백 패턴 탐지 |
| **우울증 연구** | 동기 붕괴 → 회복 에피소드 식별 |
| **ADHD 연구** | 주의력 붕괴 시점과 외부 자극 상관관계 |
| **뇌 시뮬레이션** | 창발 패턴 발생 시점 추적 |

---

## API Reference

### PanoramaConfig

| 파라미터 | 타입 | 기본값 | 설명 |
|---------|------|-------|------|
| time_gap_threshold | float | 1800.0 | 에피소드 분할 시간 갭 임계값 (초) |
| recency_half_life | float | 86400.0 | 중요도 지수 감쇠 반감기 (초) |
| max_events | int | 100000 | 최대 저장 이벤트 수 |

### PanoramaMemoryEngine

| 메서드 | 설명 | 시간 복잡도 |
|--------|------|------------|
| append_event(...) | 이벤트 추가 (필름에 새 프레임 기록) | O(log n) |
| query_range(t_start, t_end) | 시간 구간 내 이벤트 조회 (필름 앞뒤로 돌리기) | O(log n + k) |
| get_episode(episode_id) | 특정 에피소드 이벤트 조회 | O(k log k) |
| get_recent(n) | 최근 n개 이벤트 | O(n) |
| segment_episodes(...) | 에피소드 자동 분할 | O(n) |
| get_importance_scores(t_now) | 지수 감쇠 적용 중요도 | O(n) |
| get_recency_scores(t_now) | 최근성 점수 (MemoryRank 연동용) | O(n) |

---

## Algorithm Details

### 1. 타임라인 자료구조

- **정렬된 리스트**: 이벤트는 항상 시간 순으로 정렬 유지 (필름 릴처럼)
- **이진 삽입/검색**: bisect 모듈 활용 → O(log n)

### 2. 에피소드 분할 (Time Gap)

\`\`\`
새 에피소드 조건: t_i - t_{i-1} > τ (시간 갭이 임계값 초과)
\`\`\`

### 3. 지수 감쇠 (Exponential Decay)

\`\`\`
importance(t) = base_importance × exp(-λ × Δt)
λ = ln(2) / half_life

예: half_life = 24시간
    24시간 전 이벤트 → 중요도 50%
    48시간 전 이벤트 → 중요도 25%
\`\`\`

---

## MemoryRank 연동

Panorama(필름)의 recency 점수를 MemoryRank(조광기)의 입력으로 변환:

\`\`\`python
from panorama import PanoramaMemoryEngine
from memoryrank import MemoryRankEngine, MemoryNodeAttributes

# Panorama에서 최근성 점수 추출
recency_scores = panorama.get_recency_scores()

# MemoryRank 노드 속성으로 변환
node_attrs = {
    event_id: MemoryNodeAttributes(
        recency=recency_scores[event_id],
        emotion=panorama.get_event(event_id).payload.get("emotion", 0.0),
        frequency=0.5,
    )
    for event_id in recency_scores
}

# MemoryRank로 중요도 계산 (어떤 장면에 조명을 비출지 결정)
memoryrank.build_graph(edges, node_attrs)
top_memories = memoryrank.get_top_memories(10)
\`\`\`

---

## License

MIT License

---

## PHAM Blockchain Signature

| 항목 | 값 |
|------|---|
| Author | GNJz (Qquarts) |
| Date | 2025-01-28 |
| Version | v1.0.0 |

### File Hashes (SHA-256)

| 파일 | SHA-256 Hash |
|------|-------------|
| panorama_engine.py | 721ad07dd0ae6b6a59f9fb474c869b7fcc0ef0c067a25ef118cce13869496114 |
| config.py | 4b00506884f3f3e4aed56400aa5e5914310e3e6357d54ef2620ea69483ce0f8b |

> PHAM 서명 완료. 파일 무결성 검증: shasum -a 256 package/panorama/*.py

---

---

# English Version

> [🇰🇷 한국어](#panorama-memory-engine) | **🇺🇸 English**

> **"When, what, in what order?"** — Timeline-based episodic memory engine

---

## 🎬 The Memory Theater Metaphor

```
┌─────────────────────────────────────────────────────────────┐
│                    🧠 Memory Theater                         │
├─────────────────────────────────────────────────────────────┤
│   📽️ Panorama (Film)                                        │
│   ├─ Records every moment in chronological order            │
│   ├─ "What happened then?" → Rewind/fast-forward film       │
│   └─ Does not judge, just exists in recorded order          │
│                         ↓                                   │
│   💡 MemoryRank (Dimmer + Editor)                            │
│   └─ Decides which of the 10,000 frames to illuminate       │
│                         ↓                                   │
│   🎬 PFC (Projector + Director)                              │
│   └─ Projects illuminated film to screen, decides next shot │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

```python
from panorama import PanoramaMemoryEngine, PanoramaConfig

engine = PanoramaMemoryEngine(PanoramaConfig(time_gap_threshold=1800))

import time
t = time.time()
engine.append_event(t, "user_action", {"action": "click"})
engine.append_event(t + 5, "state_change", {"state": "loading"})

# Range query (rewind/fast-forward)
events = engine.query_range(t, t + 60)

# Episode segmentation
episodes = engine.segment_episodes()
```

---

## 📖 API Reference

| Method | Description | Complexity |
|--------|-------------|------------|
| append_event() | Add event (record new frame) | O(log n) |
| query_range() | Query events in time range | O(log n + k) |
| get_episode() | Get specific episode events | O(k log k) |
| get_recent(n) | Get recent n events | O(n) |
| segment_episodes() | Auto-segment into episodes | O(n) |
| get_importance_scores() | Exponential decay importance | O(n) |

---

## 🔬 Algorithm Details

### Episode Segmentation (Time Gap)

```
New episode condition: t_i - t_{i-1} > τ
```

### Exponential Decay

```
importance(t) = base_importance × exp(-λ × Δt)
λ = ln(2) / half_life
```

---

## 📄 License

MIT License

---

## ✅ PHAM Blockchain Signature

Signed with **PHAM (Proof of Honest Authorship & Merit)**.

---

**Author**: GNJz (Qquarts)
