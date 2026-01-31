# PHAM 블록체인 로그

> **Proof of Authorship & Merit - 코드 기여 및 버전 추적**

**최종 업데이트**: 2026-02-01

---

## Dynamics Engine v1.0.0 (독립 배포) - 2026-01-31

### 파일별 해시 (SHA256)

#### __init__.py
**경로**: `src/cognitive_kernel/engines/dynamics/__init__.py`  
**해시**: `2621e4279489ba9ab9cf5b8f518d4f2dfdea3906723d3789f7892cdefbd72d3b`

#### config.py
**경로**: `src/cognitive_kernel/engines/dynamics/config.py`  
**변경 내용**: 시간축 분리 파라미터 추가
- `old_memory_decay_rate`
- `new_memory_decay_rate`
- `memory_age_threshold`
**해시**: `b06dd0f38044cd5d9d4ad7cfa19d0fe5b5d8df993480fc48494ddcaff0bcde01`

#### models.py
**경로**: `src/cognitive_kernel/engines/dynamics/models.py`  
**해시**: `30cbd8d64dcd4d2d1731428223402ac1db407cc00a0d7307e1aa22c8baf4675b`

#### dynamics_engine.py
**경로**: `src/cognitive_kernel/engines/dynamics/dynamics_engine.py`  
**변경 내용**:
- `generate_torque()`: CognitiveMode 의존성 제거, 문자열 모드 지원
- `calculate_core_strength()`: 시간축 분리 로직 추가
**해시**: `f9a3591353b0768db4ba3d9830dd02835d796a7ec95e6245f13ea23c9fdf7da8`

---

## Cognitive Kernel v2.0.2 - 2026-01-31

### 파일별 해시 (SHA256)

#### __init__.py
**경로**: `src/cognitive_kernel/__init__.py`  
**변경 내용**: 버전 2.0.2로 업데이트
**해시**: `75d4ff56d18fd4cca399f1ab7ec2c66642be8fde9002752da5ff657ef2951fcc`

#### core.py
**경로**: `src/cognitive_kernel/core.py`  
**변경 내용**: Dynamics Engine 통합, 치매/알츠하이머 모드 지원
**해시**: `18eb998ba693120dc2d73f9c84df236b0dba3e27a356a69f65863e257c9d8f01`

#### cognitive_modes.py
**경로**: `src/cognitive_kernel/cognitive_modes.py`  
**변경 내용**: DEMENTIA, ALZHEIMER 모드 추가, 시간축 분리 파라미터 추가
**해시**: `af70b81057ce4cba6beff476f94c273a6f4b6efa0f45dd715a905d85303c37f1`

#### pipeline.py
**경로**: `src/cognitive_kernel/pipeline.py`  
**변경 내용**: Dynamics Engine 통합, Core decay 로직 추가
**해시**: `bd0339282e052a701268502f873ecb6814aadabf64ff3d9c850860b9ebd75d83`

---

## Dynamics Engine v2.0.2 (2026-01-31)

### 파일별 해시

#### config.py
**경로**: `src/cognitive_kernel/engines/dynamics/config.py`  
**변경 내용**: 시간축 분리 파라미터 추가
- `old_memory_decay_rate`
- `new_memory_decay_rate`
- `memory_age_threshold`

**해시**: (실행 시 계산)

#### models.py
**경로**: `src/cognitive_kernel/engines/dynamics/models.py`  
**변경 내용**: 변경 없음

**해시**: (실행 시 계산)

#### dynamics_engine.py
**경로**: `src/cognitive_kernel/engines/dynamics/dynamics_engine.py`  
**변경 내용**:
- `generate_torque()`: CognitiveMode 의존성 제거, 문자열 모드 지원
- `calculate_core_strength()`: 시간축 분리 로직 추가

**해시**: (실행 시 계산)

#### __init__.py
**경로**: `src/cognitive_kernel/engines/dynamics/__init__.py`  
**변경 내용**: 변경 없음

**해시**: (실행 시 계산)

---

## 해시 계산 방법

```python
import hashlib

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
```

---

## 버전별 체인

### v2.0.2 → (다음 버전)
- 이전 해시: (v2.0.1 해시)
- 현재 해시: (계산 필요)
- 변경 사항: 독립 배포 개선, 시간축 분리 구현

---

**작성자**: GNJz (Qquarts)  
**작성일**: 2026-01-31
