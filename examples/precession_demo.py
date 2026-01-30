"""
세차운동(Precession) 데모

ADHD(+) ↔ ASD(-) 축이 만드는 "회전장"과 세차운동을 시각화합니다.

핵심 개념:
- ASD 성분: 축 고정 (높은 β)
- ADHD 성분: 회전 토크 (γ T_n(k))
- 결과: 선호축이 느리게 회전하는 세차운동
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
from cognitive_kernel import CognitiveKernel, CognitiveMode


def calculate_entropy(probabilities: List[float]) -> float:
    """엔트로피 계산"""
    probs = np.array(probabilities)
    probs = probs[probs > 0]  # 0 제거
    return -np.sum(probs * np.log(probs))


def simulate_precession(
    n_steps: int = 100,
    omega: float = 0.05,  # 세차 속도
    gamma: float = 0.3,   # 토크 세기 (ADHD 성분)
    beta_asd: float = 5.0,  # ASD 성분 (축 고정)
) -> Tuple[List[float], List[float], List[float]]:
    """
    세차운동 시뮬레이션
    
    Args:
        n_steps: 시뮬레이션 스텝 수
        omega: 세차 속도 (느린 시간척도)
        gamma: 토크 세기 (ADHD 성분)
        beta_asd: ASD 성분 (축 고정)
    
    Returns:
        (entropies, phi_history, dominant_choice_history)
    """
    # 옵션 정의 (3개)
    options = ["choose_red", "choose_blue", "choose_green"]
    psi = [0.0, 2 * np.pi / 3, 4 * np.pi / 3]  # 각 옵션의 고유 위상
    
    # 초기화
    phi = 0.0  # 선호 축 위상
    entropies = []
    phi_history = []
    dominant_choice_history = []
    
    # 기억 설정 (ASD 고착을 위한 "red" 관련 기억)
    kernel = CognitiveKernel("precession_demo", mode=CognitiveMode.ASD)
    kernel.remember("preference", {"text": "I like red"}, importance=0.8)
    kernel.remember("preference", {"text": "Red is my favorite"}, importance=0.7)
    kernel.remember("preference", {"text": "Red color preference"}, importance=0.6)
    
    print("=" * 70)
    print("🌐 세차운동 시뮬레이션")
    print("=" * 70)
    print(f"   파라미터:")
    print(f"   - 세차 속도 (ω): {omega}")
    print(f"   - 토크 세기 (γ): {gamma} (ADHD 성분)")
    print(f"   - ASD 성분 (β): {beta_asd} (축 고정)")
    print(f"   - 시뮬레이션 스텝: {n_steps}")
    print()
    
    for step in range(n_steps):
        # 기억 회상
        memories = kernel.recall(k=3)
        
        # 각 옵션에 대한 utility 계산
        utilities = []
        for i, opt in enumerate(options):
            # 키워드 추출
            opt_keywords = kernel._extract_keywords(opt)
            
            # 기억 관련성 (C_n(k))
            memory_relevance = kernel._calculate_memory_relevance(opt_keywords, memories)
            
            # 기본 utility (U_0 + α * C_n(k))
            base_utility = 0.5 + 0.5 * memory_relevance
            
            # 회전 토크 (T_n(k) = cos(φ_n - ψ_k))
            torque = np.cos(phi - psi[i])
            
            # 최종 utility (U_n,k = U_0 + α * C_n(k) + γ * T_n(k))
            utility = base_utility + gamma * torque
            utilities.append(utility)
        
        # Softmax 확률 계산 (β = beta_asd)
        utilities = np.array(utilities)
        exp_utils = np.exp(beta_asd * (utilities - np.max(utilities)))
        probabilities = exp_utils / np.sum(exp_utils)
        
        # 엔트로피 계산
        entropy = calculate_entropy(probabilities)
        entropies.append(entropy)
        phi_history.append(phi)
        
        # 지배적 선택
        dominant_idx = np.argmax(probabilities)
        dominant_choice_history.append(dominant_idx)
        
        # 위상 업데이트 (느린 시간척도)
        phi += omega
        
        # 주기적으로 출력
        if step % 20 == 0:
            print(f"   Step {step:3d}: φ={phi:.3f}, E={entropy:.3f}, "
                  f"P=[{probabilities[0]:.3f}, {probabilities[1]:.3f}, {probabilities[2]:.3f}], "
                  f"Dominant={options[dominant_idx]}")
    
    return entropies, phi_history, dominant_choice_history


def plot_precession_results(
    entropies: List[float],
    phi_history: List[float],
    dominant_choice_history: List[int],
):
    """세차운동 결과 시각화"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. 엔트로피 vs 시간
    axes[0, 0].plot(entropies, 'b-', linewidth=2)
    axes[0, 0].set_xlabel('Step')
    axes[0, 0].set_ylabel('Entropy E_n')
    axes[0, 0].set_title('엔트로피 변화 (세차운동)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=np.log(3), color='r', linestyle='--', label='Max Entropy')
    axes[0, 0].axhline(y=0, color='g', linestyle='--', label='Min Entropy')
    axes[0, 0].legend()
    
    # 2. 위상 변화
    axes[0, 1].plot(phi_history, 'g-', linewidth=2)
    axes[0, 1].set_xlabel('Step')
    axes[0, 1].set_ylabel('Phase φ_n')
    axes[0, 1].set_title('선호 축 위상 변화')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. 지배적 선택 변화
    colors_map = {0: 'red', 1: 'blue', 2: 'green'}
    choice_colors = [colors_map[idx] for idx in dominant_choice_history]
    axes[1, 0].scatter(range(len(dominant_choice_history)), 
                      dominant_choice_history, 
                      c=choice_colors, 
                      alpha=0.6, 
                      s=50)
    axes[1, 0].set_xlabel('Step')
    axes[1, 0].set_ylabel('Dominant Choice')
    axes[1, 0].set_title('지배적 선택 변화 (세차운동)')
    axes[1, 0].set_yticks([0, 1, 2])
    axes[1, 0].set_yticklabels(['red', 'blue', 'green'])
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. 엔트로피 vs 위상 (위상 공간)
    scatter = axes[1, 1].scatter(phi_history, entropies, 
                               c=dominant_choice_history, 
                               cmap='viridis',
                               alpha=0.6,
                               s=50)
    axes[1, 1].set_xlabel('Phase φ_n')
    axes[1, 1].set_ylabel('Entropy E_n')
    axes[1, 1].set_title('위상 공간 궤적 (세차운동)')
    axes[1, 1].grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=axes[1, 1], label='Dominant Choice')
    
    plt.tight_layout()
    plt.savefig('precession_results.png', dpi=150, bbox_inches='tight')
    print(f"\n   📊 그래프 저장: precession_results.png")
    print()


def main():
    """메인 함수"""
    print("\n" + "=" * 70)
    print("🧲 세차운동(Precession) 데모")
    print("=" * 70)
    print()
    print("   개념:")
    print("   - ASD 성분: 축 고정 (높은 β)")
    print("   - ADHD 성분: 회전 토크 (γ T_n(k))")
    print("   - 결과: 선호축이 느리게 회전하는 세차운동")
    print()
    
    # 세차운동 시뮬레이션
    entropies, phi_history, dominant_choice_history = simulate_precession(
        n_steps=100,
        omega=0.05,  # 세차 속도
        gamma=0.3,   # 토크 세기
        beta_asd=5.0,  # ASD 성분
    )
    
    # 결과 분석
    print("=" * 70)
    print("📊 결과 분석")
    print("=" * 70)
    print(f"   평균 엔트로피: {np.mean(entropies):.3f}")
    print(f"   엔트로피 범위: [{np.min(entropies):.3f}, {np.max(entropies):.3f}]")
    print(f"   최대 엔트로피 (이론값): {np.log(3):.3f}")
    print()
    
    # 선택 변화 횟수
    choice_changes = sum(1 for i in range(1, len(dominant_choice_history)) 
                        if dominant_choice_history[i] != dominant_choice_history[i-1])
    print(f"   선택 변화 횟수: {choice_changes}회")
    print(f"   선택 변화율: {choice_changes / len(dominant_choice_history) * 100:.1f}%")
    print()
    
    # 시각화
    try:
        plot_precession_results(entropies, phi_history, dominant_choice_history)
    except Exception as e:
        print(f"   ⚠️  시각화 실패: {e}")
        print("   (matplotlib가 설치되지 않았을 수 있습니다)")
    
    print("=" * 70)
    print("✅ 세차운동 시뮬레이션 완료")
    print("=" * 70)
    print()
    print("   핵심 통찰:")
    print("   1. ASD 성분(높은 β)이 '축을 고정'함")
    print("   2. ADHD 성분(회전 토크)이 '축을 회전'시킴")
    print("   3. 결과: 선호축이 느리게 회전하는 세차운동")
    print("   4. 엔트로피는 낮게 유지되지만, 선택은 주기적으로 변화")
    print()


if __name__ == "__main__":
    main()

