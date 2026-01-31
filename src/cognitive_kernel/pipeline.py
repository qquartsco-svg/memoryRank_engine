"""
🔀 Decision Pipeline

의사결정 파이프라인 패턴 구현.
알고리즘 순서 변경 및 단계 추가/제거 용이.

Author: GNJz (Qquarts)
Version: 2.0.1+
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field


@dataclass
class PipelineContext:
    """파이프라인 컨텍스트 (단계 간 데이터 전달)"""
    options: List[str]
    memories: List[Dict[str, Any]] = field(default_factory=list)
    actions: List[Any] = field(default_factory=list)
    utilities: List[float] = field(default_factory=list)
    probabilities: List[float] = field(default_factory=list)
    entropy: float = 0.0
    core_strength: float = 0.0
    auto_torque: Dict[str, float] = field(default_factory=dict)
    result: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class PipelineStep(ABC):
    """파이프라인 단계 추상 클래스"""
    
    @abstractmethod
    def process(self, context: PipelineContext) -> PipelineContext:
        """단계 처리"""
        pass
    
    def __repr__(self) -> str:
        return self.__class__.__name__


class MemoryLoadStep(PipelineStep):
    """기억 로드 단계"""
    
    def __init__(self, memory_engine, working_memory_capacity: int = 7):
        self.memory_engine = memory_engine
        self.working_memory_capacity = working_memory_capacity
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """기억 로드"""
        context.memories = self.memory_engine.recall(k=self.working_memory_capacity)
        return context


class WorkingMemoryStep(PipelineStep):
    """Working Memory 로드 단계"""
    
    def __init__(self, pfc_engine):
        self.pfc_engine = pfc_engine
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """Working Memory에 기억 로드"""
        top_memories_tuples = [
            (m["id"], m["importance"]) for m in context.memories
        ]
        self.pfc_engine.load_from_memoryrank(top_memories_tuples)
        return context


class ActionCreationStep(PipelineStep):
    """Action 생성 단계"""
    
    def __init__(
        self,
        pfc_engine,
        calculate_relevance: Callable,
        extract_keywords: Callable,
        alpha: float = 0.5,
    ):
        self.pfc_engine = pfc_engine
        self.calculate_relevance = calculate_relevance
        self.extract_keywords = extract_keywords
        self.alpha = alpha
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """Action 생성"""
        from .engines.pfc import Action
        
        actions = []
        for i, opt in enumerate(context.options):
            opt_keywords = self.extract_keywords(opt)
            memory_relevance = self.calculate_relevance(opt_keywords, context.memories)
            expected_reward = 0.5 + self.alpha * memory_relevance
            
            actions.append(Action(
                id=f"action_{i}",
                name=opt,
                expected_reward=expected_reward,
                effort_cost=0.2,
                risk=0.1,
            ))
        
        context.actions = actions
        return context


class PFCDecisionStep(PipelineStep):
    """PFC 의사결정 단계"""
    
    def __init__(self, pfc_engine):
        self.pfc_engine = pfc_engine
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """PFC 결정"""
        pfc_result = self.pfc_engine.process(context.actions)
        context.utilities = [
            self.pfc_engine.evaluate_action(a) for a in context.actions
        ]
        context.probabilities = self.pfc_engine.softmax_probabilities(context.utilities)
        context.metadata["pfc_result"] = pfc_result
        return context


class EntropyCalculationStep(PipelineStep):
    """엔트로피 계산 단계"""
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """엔트로피 계산"""
        import math
        
        entropy = 0.0
        for prob in context.probabilities:
            if prob > 0:
                entropy -= prob * math.log(prob)
        
        context.entropy = entropy
        return context


class CoreStrengthStep(PipelineStep):
    """코어 강도 계산 단계 (Core Decay 포함)"""
    
    def __init__(self, kernel, alpha: float = 0.5):
        """
        Args:
            kernel: CognitiveKernel 인스턴스 (Core Decay 상태 접근)
            alpha: 기억 영향 계수
        """
        self.kernel = kernel
        self.alpha = alpha
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """코어 강도 계산 (Core Decay 동역학 적용)"""
        import math
        import time
        
        # 1. 현재 원시 코어 강도 계산
        current_raw_core = 0.0
        if context.memories:
            total_importance = sum(
                m.get("importance", 0.0) for m in context.memories
            )
            
            # 알츠하이머의 경우 새 기억의 중요도 반영을 차단
            if self.kernel.mode_config.memory_update_failure > 0:
                total_importance *= (1.0 - self.kernel.mode_config.memory_update_failure)
            
            current_raw_core = min(
                1.0, self.alpha * total_importance / len(context.memories)
            )
        
        # 2. Core Decay (물리적 시간 붕괴 항 적용)
        # 수식: C(t) = C(0) * exp(-λ * Δt)
        if self.kernel.mode_config.core_decay_rate > 0:
            # 초기화
            if self.kernel._persistent_core is None:
                self.kernel._persistent_core = current_raw_core
                self.kernel._last_decay_time = time.time()
            
            # 시간 경과 계산
            delta_t = time.time() - self.kernel._last_decay_time
            lambda_decay = self.kernel.mode_config.core_decay_rate
            
            # 지수 감쇠 적용
            self.kernel._persistent_core *= math.exp(-lambda_decay * delta_t)
            core_strength = self.kernel._persistent_core
            self.kernel._last_decay_time = time.time()
        else:
            # 정상 모드: 원시 코어 강도 사용
            core_strength = current_raw_core
            self.kernel._persistent_core = None
            self.kernel._last_decay_time = None
        
        # 3. 인지적 절규 (Cognitive Distress)
        # 엔트로피는 높은데 이를 붙잡을 중력(Core)이 임계치(0.3) 아래로 떨어질 때
        if len(context.options) > 1:
            max_entropy = math.log(len(context.options))
            entropy_threshold = max_entropy * 0.8  # 최대치의 80%
            
            if context.entropy > entropy_threshold and core_strength < 0.3:
                self.kernel._cognitive_distress = True
                # 메타데이터에 인지적 절규 신호 저장
                context.metadata["cognitive_distress"] = True
                context.metadata["distress_message"] = "기억이 안 나..."
            else:
                self.kernel._cognitive_distress = False
                context.metadata["cognitive_distress"] = False
        
        context.core_strength = core_strength
        return context


class TorqueGenerationStep(PipelineStep):
    """회전 토크 생성 단계"""
    
    def __init__(
        self,
        mode,
        base_gamma: float = 0.3,
        omega: float = 0.05,
        precession_phi_ref=None,  # 위상 참조 (리스트 또는 객체)
    ):
        self.mode = mode
        self.base_gamma = base_gamma
        self.omega = omega
        self._precession_phi_ref = precession_phi_ref  # 위상 참조
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """회전 토크 생성"""
        import math
        from .cognitive_modes import CognitiveMode
        
        auto_torque = {}
        if len(context.options) > 1:
            max_entropy = math.log(len(context.options))
            normalized_entropy = (
                context.entropy / max_entropy if max_entropy > 0 else 0.0
            )
            
            # 모드별 gamma
            if self.mode == CognitiveMode.ADHD:
                gamma = self.base_gamma * 1.5
            elif self.mode == CognitiveMode.ASD:
                gamma = self.base_gamma * 0.5
            else:
                gamma = self.base_gamma
            
            torque_strength = gamma * normalized_entropy
            
            # 옵션별 위상
            psi = {
                opt: i * 2 * math.pi / len(context.options)
                for i, opt in enumerate(context.options)
            }
            
            # 위상 가져오기 (참조 또는 기본값)
            if self._precession_phi_ref is not None:
                if isinstance(self._precession_phi_ref, list):
                    current_phi = self._precession_phi_ref[0]
                else:
                    current_phi = getattr(self._precession_phi_ref, '_precession_phi', 0.0)
            else:
                current_phi = 0.0
            
            # 회전 토크 계산
            for opt in context.options:
                auto_torque[opt] = torque_strength * math.cos(
                    current_phi - psi[opt]
                )
            
            # 위상 업데이트
            new_phi = current_phi + self.omega
            if new_phi >= 2 * math.pi:
                new_phi -= 2 * math.pi
            
            # 위상 저장 (메타데이터에)
            context.metadata["precession_phi"] = new_phi
        
        context.auto_torque = auto_torque
        return context


class UtilityRecalculationStep(PipelineStep):
    """Utility 재계산 단계"""
    
    def __init__(
        self,
        pfc_engine,
        calculate_relevance: Callable,
        extract_keywords: Callable,
        alpha: float = 0.5,
    ):
        self.pfc_engine = pfc_engine
        self.calculate_relevance = calculate_relevance
        self.extract_keywords = extract_keywords
        self.alpha = alpha
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """Utility 재계산 (토크 반영)"""
        from .engines.pfc import Action
        
        if context.auto_torque:
            actions = []
            for i, opt in enumerate(context.options):
                opt_keywords = self.extract_keywords(opt)
                memory_relevance = self.calculate_relevance(opt_keywords, context.memories)
                expected_reward = 0.5 + self.alpha * memory_relevance
                
                # 토크 주입
                if opt in context.auto_torque:
                    expected_reward += context.auto_torque[opt]
                
                actions.append(Action(
                    id=f"action_{i}",
                    name=opt,
                    expected_reward=expected_reward,
                    effort_cost=0.2,
                    risk=0.1,
                ))
            
            context.actions = actions
            # PFC 재결정
            pfc_result = self.pfc_engine.process(actions)
            context.utilities = [
                self.pfc_engine.evaluate_action(a) for a in actions
            ]
            context.probabilities = self.pfc_engine.softmax_probabilities(context.utilities)
            context.metadata["pfc_result"] = pfc_result
        
        return context


class ResultAssemblyStep(PipelineStep):
    """결과 조립 단계"""
    
    def __init__(self, pfc_engine, basal_ganglia_engine=None):
        self.pfc_engine = pfc_engine
        self.basal_ganglia_engine = basal_ganglia_engine
    
    def process(self, context: PipelineContext) -> PipelineContext:
        """최종 결과 조립"""
        pfc_result = context.metadata.get("pfc_result")
        
        probability_distribution = {
            opt: prob for opt, prob in zip(context.options, context.probabilities)
        }
        
        habit_action = None
        if self.basal_ganglia_engine and context.metadata.get("context"):
            habit_action = self.basal_ganglia_engine.select_action(
                context.metadata["context"],
                context.options,
            )
        
        # 인지적 절규 상태 확인
        cognitive_distress = context.metadata.get("cognitive_distress", False)
        distress_message = context.metadata.get("distress_message", "")
        
        context.result = {
            "action": pfc_result.action.name if pfc_result and pfc_result.action else None,
            "utility": pfc_result.utility if pfc_result else 0.0,
            "probability": pfc_result.selection_probability if pfc_result else 0.0,
            "probability_distribution": probability_distribution,
            "entropy": context.entropy,
            "core_strength": context.core_strength,
            "habit_suggestion": habit_action,
            "conflict": (
                pfc_result.action.name != habit_action
                if (pfc_result and pfc_result.action and habit_action)
                else False
            ),
            "cognitive_distress": cognitive_distress,  # 인지적 절규 상태
            "distress_message": distress_message,  # 절규 메시지
        }
        
        return context


class DecisionPipeline:
    """의사결정 파이프라인"""
    
    def __init__(self, steps: List[PipelineStep]):
        """
        Args:
            steps: 파이프라인 단계 리스트 (순서대로 실행)
        """
        self.steps = steps
    
    def execute(self, context: PipelineContext) -> PipelineContext:
        """파이프라인 실행"""
        for step in self.steps:
            context = step.process(context)
        return context
    
    def add_step(self, step: PipelineStep, index: Optional[int] = None):
        """단계 추가"""
        if index is None:
            self.steps.append(step)
        else:
            self.steps.insert(index, step)
    
    def remove_step(self, step: PipelineStep):
        """단계 제거"""
        if step in self.steps:
            self.steps.remove(step)
    
    def replace_step(self, old_step: PipelineStep, new_step: PipelineStep):
        """단계 교체"""
        index = self.steps.index(old_step)
        self.steps[index] = new_step
    
    def __repr__(self) -> str:
        step_names = [step.__class__.__name__ for step in self.steps]
        return f"DecisionPipeline([{', '.join(step_names)}])"

