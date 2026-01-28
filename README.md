# Cognitive Kernel

> **🇰🇷 한국어** | [🇺🇸 English](#english-version)

> **인지 운영체제** — 기억, 주의력, 추론을 통합 관리하는 모듈형 인지 엔진

---

## 🧠 개요

**Cognitive Kernel**은 인간의 인지 시스템을 소프트웨어로 모델링한 **모듈형 인지 엔진 모음**입니다.

마치 운영체제의 커널이 CPU, 메모리, I/O를 관리하듯,
Cognitive Kernel은 **기억, 주의력, 감정, 추론**을 관리합니다.

---

## 🎬 기억의 영화관 비유

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                    🧠 Cognitive Kernel                       │
├─────────────────────────────────────────────────────────────┤
│   🎞️ Panorama (필름)     →  시간순 기록                      │
│   💡 MemoryRank (조광기)  →  중요도 계산                      │
│   🎬 PFC (감독)          →  의식적 결정                      │
│   👷 BasalGanglia (스태프) →  습관 자동화                     │
└─────────────────────────────────────────────────────────────┘
\`\`\`

---

## 📦 모듈 구성

| 모듈 | 역할 | 비유 | 상태 |
|------|------|------|------|
| **[MemoryRank](./MemoryRank/)** | 기억 중요도 계산 | 조광기 | ✅ v1.0.0 |
| **[Panorama](./Panorama/)** | 시간축 에피소드 기억 | 필름 | ✅ v1.0.0 |
| **[PFC](./PFC/)** | 작업 기억, 행동 선택, 억제 | 영사기 + 감독 | ✅ v1.0.0 |
| **[BasalGanglia](./BasalGanglia/)** | 행동 선택, 습관 학습, Q-Learning | 스태프 | ✅ v1.0.0 |

---

## 🚀 Quick Start

\`\`\`bash
git clone https://github.com/qquartsco-svg/Cognitive_Kernel.git
cd Cognitive_Kernel
python examples/integrated_pipeline.py
\`\`\`

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

> **Cognitive Operating System** — A modular cognitive engine for memory, attention, and reasoning

---

## 🧠 Overview

**Cognitive Kernel** is a collection of **modular cognitive engines** that model the human cognitive system in software.

Just as an operating system kernel manages CPU, memory, and I/O,
Cognitive Kernel manages **memory, attention, emotion, and reasoning**.

---

## 🎬 The Memory Theater Metaphor

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                    🧠 Cognitive Kernel                       │
├─────────────────────────────────────────────────────────────┤
│   🎞️ Panorama (Film)      →  Timeline Recording              │
│   💡 MemoryRank (Dimmer)   →  Importance Calculation          │
│   🎬 PFC (Director)        →  Conscious Decision              │
│   👷 BasalGanglia (Staff)  →  Habit Automation                │
└─────────────────────────────────────────────────────────────┘
\`\`\`

---

## 📦 Modules

| Module | Role | Metaphor | Status |
|--------|------|----------|--------|
| **[MemoryRank](./MemoryRank/)** | Memory importance ranking | Dimmer | ✅ v1.0.0 |
| **[Panorama](./Panorama/)** | Timeline-based episodic memory | Film | ✅ v1.0.0 |
| **[PFC](./PFC/)** | Working memory, action selection, inhibition | Director | ✅ v1.0.0 |
| **[BasalGanglia](./BasalGanglia/)** | Action selection, habit learning, Q-Learning | Staff | ✅ v1.0.0 |

---

## 🔗 Module Integration Flow

\`\`\`
Panorama (Timeline) → MemoryRank (Importance) → PFC (Decision) → BasalGanglia (Execution)
     │                       │                       │                    │
     ▼                       ▼                       ▼                    ▼
"What happened?"     "What matters?"      "What to do?"         "Just do it!"
\`\`\`

---

## 🚀 Quick Start

\`\`\`bash
git clone https://github.com/qquartsco-svg/Cognitive_Kernel.git
cd Cognitive_Kernel
python examples/integrated_pipeline.py
\`\`\`

### Example Output

\`\`\`
🧠 Cognitive Kernel - Integrated Pipeline

🎞️ [1] PANORAMA - 10 events recorded
💡 [2] MEMORYRANK - Top 5 important memories identified
🎬 [3] PFC - Selected action: 'exercise_gym' (Utility: 0.290)
👷 [4] BASALGANGLIA - Habit suggests: 'go_home_rest' (Q: 0.439)

🎯 Final: Conscious decision overrides habit
\`\`\`

---

## 🎯 Use Cases

### 🏢 Industry / Commercial

| Domain | Application |
|--------|-------------|
| **AI Agents** | Long-term memory + context-aware conversation |
| **Recommendation Systems** | User interest importance-based recommendations |
| **Game AI** | NPC memory systems, player behavior learning |
| **Log Analysis** | Incident timeline reconstruction |

### 🔬 Research / Medical

| Domain | Application |
|--------|-------------|
| **PTSD Research** | Intrusive memory pattern analysis |
| **Depression Research** | Negative memory bias simulation |
| **ADHD Research** | Attention collapse tracking |
| **Brain Simulation** | Cognitive loop dynamics modeling |

---

## 📁 Project Structure

\`\`\`
Cognitive_Kernel/
├── README.md               # This file
├── examples/
│   └── integrated_pipeline.py  # 4-engine demo
├── MemoryRank/             # Importance calculation (PageRank)
├── Panorama/               # Timeline memory (Binary Search)
├── PFC/                    # Decision making (Expected Utility)
└── BasalGanglia/           # Habit learning (Q-Learning)
\`\`\`

---

## 🔬 Theoretical Background

### OS Kernel vs Cognitive Kernel

| OS Kernel | Cognitive Kernel |
|-----------|------------------|
| Memory Manager | Panorama + MemoryRank |
| Process Scheduler | PFC (Attention Controller) |
| System Call | Inter-engine API |
| Kernel Panic | Cognitive Collapse (Disorder State) |

### Core Algorithms

| Module | Algorithm |
|--------|-----------|
| MemoryRank | Personalized PageRank |
| Panorama | Binary Search + Exponential Decay |
| PFC | Expected Utility + Softmax Selection |
| BasalGanglia | Q-Learning + Dopamine Modulation |

---

## 📄 License

MIT License

---

## 🔐 PHAM Blockchain Signature

All core modules are signed with **PHAM (Proof of Honest Authorship & Merit)** blockchain.

| Module | Signature |
|--------|-----------|
| MemoryRank | ✅ Signed |
| Panorama | ✅ Signed |
| PFC | ✅ Signed |
| BasalGanglia | ✅ Signed |

---

## 👤 Author

**GNJz (Qquarts)** - GitHub: [@qquartsco-svg](https://github.com/qquartsco-svg)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a Pull Request.
