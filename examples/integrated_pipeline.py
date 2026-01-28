"""
🧠 Cognitive Kernel - 4대 엔진 통합 파이프라인 데모

기억의 영화관 시나리오:
1. Panorama (필름): 하루 동안의 이벤트 기록
2. MemoryRank (조광기): 중요한 기억에 조명
3. PFC (감독): 다음 행동 결정
4. BasalGanglia (스태프): 습관 기반 자동 실행

실행:
    cd /Users/jazzin/Desktop/00_BRAIN/Cognitive_Kernel
    python examples/integrated_pipeline.py
"""

import sys
from pathlib import Path

# 패키지 경로 추가
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Panorama" / "package"))
sys.path.insert(0, str(ROOT / "MemoryRank" / "package"))
sys.path.insert(0, str(ROOT / "PFC" / "package"))
sys.path.insert(0, str(ROOT / "BasalGanglia" / "package"))

from panorama import PanoramaMemoryEngine, PanoramaConfig
from memoryrank import MemoryRankEngine, MemoryRankConfig, MemoryNodeAttributes
from pfc import PFCEngine, PFCConfig, Action
from basal_ganglia import BasalGangliaEngine, BasalGangliaConfig


def main():
    print("=" * 70)
    print("🧠 Cognitive Kernel - 4대 엔진 통합 파이프라인")
    print("=" * 70)

    # =========================================================
    # 1️⃣ PANORAMA (필름) - 하루 동안의 이벤트 기록
    # =========================================================
    print("\n" + "─" * 70)
    print("🎞️  [1] PANORAMA (필름) - 이벤트 기록")
    print("─" * 70)

    panorama = PanoramaMemoryEngine(PanoramaConfig(
        time_gap_threshold=60.0,
        recency_half_life=3600.0,
    ))

    # 시뮬레이션: 직장인의 하루
    base_time = 1706400000.0
    events = [
        (base_time + 0,    "wake_up",       {"mood": "neutral"}, 0.3),
        (base_time + 60,   "check_phone",   {"notifications": 5}, 0.4),
        (base_time + 120,  "breakfast",     {"type": "coffee"}, 0.3),
        (base_time + 300,  "commute",       {"traffic": "heavy"}, 0.5),
        (base_time + 600,  "meeting",       {"topic": "project_deadline", "stress": 0.8}, 0.9),
        (base_time + 900,  "email_urgent",  {"from": "boss", "priority": "high"}, 0.85),
        (base_time + 1200, "lunch_skip",    {"reason": "too_busy"}, 0.6),
        (base_time + 1500, "task_complete", {"task": "report", "success": True}, 0.7),
        (base_time + 1800, "colleague_help",{"who": "teammate", "emotion": 0.6}, 0.65),
        (base_time + 2100, "end_of_day",    {"energy": 0.3, "stress": 0.7}, 0.5),
    ]

    event_ids = []
    for t, etype, payload, importance in events:
        eid = panorama.append_event(t, etype, payload, importance=importance)
        event_ids.append((eid, etype, payload))
        print(f"  📝 {etype}: importance={importance:.2f}")

    print(f"\n  총 이벤트: {len(panorama)} 개")

    # 에피소드 분할
    episodes = panorama.segment_episodes(method="time_gap")
    print(f"  에피소드: {len(episodes)} 개")

    # =========================================================
    # 2️⃣ MEMORYRANK (조광기) - 중요한 기억에 조명
    # =========================================================
    print("\n" + "─" * 70)
    print("💡 [2] MEMORYRANK (조광기) - 중요도 계산")
    print("─" * 70)

    memoryrank = MemoryRankEngine(MemoryRankConfig(
        damping=0.85,
        recency_weight=1.5,
        emotion_weight=2.0,
        frequency_weight=0.5,
    ))

    # 이벤트 간 연결 (인과 관계)
    edges = []
    for i in range(len(event_ids) - 1):
        edges.append((event_ids[i][0], event_ids[i+1][0], 0.8))
    
    # 특별 연결: meeting → email_urgent (강한 연관)
    edges.append((event_ids[4][0], event_ids[5][0], 1.0))
    # email_urgent → lunch_skip (인과)
    edges.append((event_ids[5][0], event_ids[6][0], 0.9))

    # 노드 속성 (Panorama에서 추출)
    t_now = base_time + 2200
    recency_scores = panorama.get_recency_scores(t_now)
    
    node_attrs = {}
    for eid, etype, payload in event_ids:
        event = panorama.get_event(eid)
        emotion = payload.get("stress", payload.get("emotion", 0.3))
        node_attrs[eid] = MemoryNodeAttributes(
            recency=recency_scores.get(eid, 0.5),
            emotion=emotion,
            frequency=0.5,
            base_importance=event.importance,
        )

    memoryrank.build_graph(edges, node_attrs)
    importance_scores = memoryrank.calculate_importance()
    top_memories = memoryrank.get_top_memories(5)

    print("\n  🔦 중요도 Top 5:")
    for i, (eid, score) in enumerate(top_memories, 1):
        etype = next((e[1] for e in event_ids if e[0] == eid), "unknown")
        print(f"     {i}. {etype}: {score:.4f}")

    # =========================================================
    # 3️⃣ PFC (감독) - 다음 행동 결정
    # =========================================================
    print("\n" + "─" * 70)
    print("🎬 [3] PFC (감독) - 행동 결정")
    print("─" * 70)

    pfc = PFCEngine(PFCConfig(
        working_memory_capacity=5,
        risk_aversion=0.6,
        inhibition_threshold=0.65,
        decision_temperature=1.5,
    ))

    # MemoryRank 결과를 Working Memory에 로드
    pfc.load_from_memoryrank(top_memories)
    pfc.set_goal("manage stress and recover energy", priority=0.8)

    print(f"\n  🧠 Working Memory 로드: {len(pfc.get_working_memory())} 항목")
    print(f"  🎯 목표: '{pfc.get_goal()[0]}'")

    # 행동 후보 정의 (퇴근 후 선택지)
    actions = [
        Action.create("go_home_rest", reward=0.7, cost=0.1, risk=0.05),
        Action.create("overtime_work", reward=0.5, cost=0.6, risk=0.4),
        Action.create("drink_with_colleagues", reward=0.6, cost=0.3, risk=0.3),
        Action.create("exercise_gym", reward=0.75, cost=0.4, risk=0.1),
        Action.create("skip_dinner_sleep", reward=0.4, cost=0.2, risk=0.5),
    ]

    print("\n  📋 행동 후보 효용 평가:")
    for action in actions:
        utility = pfc.evaluate_action(action)
        print(f"     {action.name}: U = {utility:.3f}")

    # 행동 선택
    result = pfc.select_action(actions, deterministic=False)

    if result.inhibited:
        print(f"\n  ⛔ 선택된 행동이 억제됨 (conflict={result.conflict_signal:.3f})")
        pfc_choice = None
    else:
        print(f"\n  ✅ PFC 결정: '{result.action.name}'")
        print(f"     효용: {result.utility:.3f}")
        print(f"     선택 확률: {result.selection_probability:.1%}")
        pfc_choice = result.action.name

    # =========================================================
    # 4️⃣ BASAL GANGLIA (스태프) - 습관 기반 실행
    # =========================================================
    print("\n" + "─" * 70)
    print("👷 [4] BASAL GANGLIA (스태프) - 습관 학습")
    print("─" * 70)

    # BasalGanglia 설정 (실제 API에 맞게)
    bg = BasalGangliaEngine(BasalGangliaConfig(
        alpha=0.2,        # 학습률
        gamma=0.9,        # 할인율
        tau=0.5,          # 소프트맥스 온도
        habit_threshold=0.7,
    ))

    # 과거 경험 시뮬레이션 (이 상황에서 반복된 행동)
    context = "stressed_after_work"
    action_names = ["go_home_rest", "overtime_work", "drink_with_colleagues", 
                    "exercise_gym", "skip_dinner_sleep"]
    
    past_experiences = [
        ("go_home_rest", 0.8),
        ("go_home_rest", 0.7),
        ("exercise_gym", 0.9),
        ("go_home_rest", 0.6),
        ("drink_with_colleagues", 0.4),
        ("go_home_rest", 0.75),
    ]

    print(f"\n  📚 과거 경험 학습 (context: '{context}'):")
    for action_name, reward in past_experiences:
        bg.learn(context, action_name, reward)
        print(f"     {action_name}: reward={reward}")

    # BasalGanglia의 행동 선택
    bg_result = bg.select_action(context, action_names)
    bg_action = bg_result.action.name if bg_result.action else "none"

    print(f"\n  📊 학습된 Q-값:")
    norm_context = context.lower().strip()
    for action_name in action_names:
        if norm_context in bg.q_table and action_name in bg.q_table[norm_context]:
            action = bg.q_table[norm_context][action_name]
            q_val = action.q_value
            habit_marker = "🔥 습관" if action.is_habit else ""
        else:
            q_val = 0.0
            habit_marker = ""
        print(f"     {action_name}: Q={q_val:.3f} {habit_marker}")

    print(f"\n  🤖 BasalGanglia 선택: '{bg_action}'")
    print(f"     자동 실행: {bg_result.is_automatic if hasattr(bg_result, 'is_automatic') else 'N/A'}")

    # =========================================================
    # 5️⃣ 최종 통합 결과
    # =========================================================
    print("\n" + "=" * 70)
    print("🧠 [최종 결과] Cognitive Kernel 통합 출력")
    print("=" * 70)

    top_event_name = next((e[1] for e in event_ids if e[0] == top_memories[0][0]), "unknown")

    print(f"""
  📽️ 시나리오: 스트레스 많은 하루를 보낸 직장인의 퇴근 후 선택

  🎞️ Panorama가 기록한 핵심 사건:
     - meeting (stress=0.8)
     - email_urgent (boss, high priority)
     - lunch_skip (too busy)

  💡 MemoryRank가 밝힌 가장 중요한 기억:
     → '{top_event_name}'
     
  🎬 PFC (의식적 판단):
     → '{pfc_choice if pfc_choice else "억제됨"}' (효용: {result.utility:.3f})
     
  👷 BasalGanglia (습관적 반응):
     → '{bg_action}' (Q-Learning 기반)

  🎯 최종 행동:
""")

    # PFC와 BasalGanglia가 같은 선택을 했는지 확인
    if pfc_choice and pfc_choice == bg_action:
        print(f"     ✨ PFC와 습관이 일치: '{pfc_choice}'")
        print("        → 빠르고 확신 있는 실행!")
    elif pfc_choice:
        print(f"     ⚖️ PFC: '{pfc_choice}' vs 습관: '{bg_action}'")
        print("        → 의식적 결정이 습관을 오버라이드")
    else:
        print(f"     ⛔ PFC가 억제, 습관 '{bg_action}'이 실행될 수 있음")

    print("\n" + "=" * 70)
    print("✅ Cognitive Kernel 통합 파이프라인 완료!")
    print("=" * 70)


if __name__ == "__main__":
    main()
