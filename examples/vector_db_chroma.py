"""
🔗 Cognitive Kernel + Chroma DB Integration Example

Vector DB를 백엔드로 사용하여 의미 기억(Semantic Memory)을 저장하고,
Cognitive Kernel의 MemoryRank로 중요도 재랭킹하는 예제.

구조:
    [Embedding] → [Chroma DB] → [MemoryRank] → [PFC]

Usage:
    pip install cognitive-kernel chromadb sentence-transformers
    python examples/vector_db_chroma.py
"""

from cognitive_kernel import CognitiveKernel
from cognitive_kernel.vector_integration import VectorDBBackend
import json
from pathlib import Path

# ============================================================
# 🧠 Vector DB 통합 사용 예제
# ============================================================

def demo_vector_db_integration():
    """Vector DB + Cognitive Kernel 통합 데모"""
    
    print("\n" + "="*60)
    print("🔗 Vector DB + Cognitive Kernel Integration")
    print("="*60)
    
    # 1. Vector DB 백엔드 초기화
    print("\n📦 Step 1: Initialize Vector DB Backend")
    vector_backend = VectorDBBackend(
        backend_type="chroma",
        path="./chroma_db_demo",
        collection_name="cognitive_memory"
    )
    print("   ✅ Chroma DB initialized")
    
    # 2. Cognitive Kernel 초기화
    print("\n🧠 Step 2: Initialize Cognitive Kernel")
    kernel = CognitiveKernel("vector_demo")
    print("   ✅ Cognitive Kernel initialized")
    
    # 3. 기억 저장 (Vector DB + Cognitive Kernel)
    print("\n💾 Step 3: Store memories with embeddings")
    
    memories_to_store = [
        {
            "event_type": "user_preference",
            "text": "I prefer morning meetings and coffee",
            "importance": 0.9
        },
        {
            "event_type": "project_info",
            "text": "Working on AI agent with persistent memory",
            "importance": 0.8
        },
        {
            "event_type": "meeting_note",
            "text": "Discussed Vector DB integration for semantic search",
            "importance": 0.7
        },
        {
            "event_type": "idea",
            "text": "Combine Chroma DB with PageRank for better recall",
            "importance": 0.6
        }
    ]
    
    for mem in memories_to_store:
        # Cognitive Kernel에 저장
        memory_id = kernel.remember(
            event_type=mem["event_type"],
            content={"text": mem["text"]},
            importance=mem["importance"]
        )
        
        # Vector DB에도 저장 (embedding)
        vector_backend.add_memory(
            memory_id=memory_id,
            text=mem["text"],
            metadata={
                "event_type": mem["event_type"],
                "importance": mem["importance"]
            },
            importance=mem["importance"]
        )
        print(f"   ✅ Stored: {mem['event_type']} (ID: {memory_id[:8]}...)")
    
    # 4. Semantic Search (Vector DB)
    print("\n🔍 Step 4: Semantic Search (Vector DB)")
    query = "meeting preferences"
    vector_results = vector_backend.search(query, k=3)
    
    print(f"\n   Query: '{query}'")
    print(f"   Found {len(vector_results)} results:")
    for i, result in enumerate(vector_results, 1):
        print(f"   {i}. [{result['metadata']['event_type']}] "
              f"Distance: {result['distance']:.3f}")
        print(f"      Text: {result['text'][:50]}...")
    
    # 5. Importance Ranking (MemoryRank)
    print("\n📊 Step 5: Importance Ranking (MemoryRank)")
    ranked_memories = kernel.recall(k=5)
    
    print(f"\n   Top {len(ranked_memories)} memories by importance:")
    for i, mem in enumerate(ranked_memories, 1):
        print(f"   {i}. [{mem.get('event_type', 'unknown')}] "
              f"Importance: {mem.get('importance', 0):.3f}")
        content = mem.get('content', {})
        if isinstance(content, dict):
            text = content.get('text', str(content))
        else:
            text = str(content)
        print(f"      Text: {text[:50]}...")
    
    # 6. 하이브리드 검색 (Vector Search + Importance Ranking)
    print("\n🎯 Step 6: Hybrid Search (Vector + Importance)")
    
    # Vector search로 관련 기억 찾기
    vector_results = vector_backend.search("AI agent memory", k=5)
    
    # MemoryRank로 중요도 재랭킹
    vector_ids = [r["id"] for r in vector_results]
    all_memories = kernel.recall(k=10)
    
    # Vector search 결과와 MemoryRank 결과를 결합
    hybrid_results = []
    for mem in all_memories:
        mem_id = mem.get("id", "")
        if mem_id in vector_ids:
            # Vector search에도 있고, MemoryRank에도 있음
            vector_result = next(r for r in vector_results if r["id"] == mem_id)
            hybrid_results.append({
                "id": mem_id,
                "event_type": mem.get("event_type"),
                "text": mem.get("content", {}).get("text", ""),
                "importance": mem.get("importance", 0),
                "vector_distance": vector_result["distance"],
                "hybrid_score": mem.get("importance", 0) * (1.0 / (1.0 + vector_result["distance"]))
            })
    
    # Hybrid score로 정렬
    hybrid_results.sort(key=lambda x: x["hybrid_score"], reverse=True)
    
    print(f"\n   Hybrid results (Vector + Importance):")
    for i, result in enumerate(hybrid_results[:3], 1):
        print(f"   {i}. [{result['event_type']}] "
              f"Hybrid Score: {result['hybrid_score']:.3f}")
        print(f"      Importance: {result['importance']:.3f}, "
              f"Vector Distance: {result['vector_distance']:.3f}")
        print(f"      Text: {result['text'][:50]}...")
    
    # 7. 저장
    print("\n💾 Step 7: Save state")
    kernel.save()
    vector_backend.save()
    print("   ✅ Cognitive Kernel saved")
    print("   ✅ Vector DB saved")
    
    print("\n" + "="*60)
    print("✅ Demo completed!")
    print("="*60)
    print("\n📁 Files created:")
    print("   - .cognitive_kernel/vector_demo/ (Cognitive Kernel data)")
    print("   - chroma_db_demo/ (Chroma DB data)")


# ============================================================
# 🔄 세션 복구 테스트
# ============================================================

def demo_session_recovery():
    """세션 복구 테스트 (Vector DB + Cognitive Kernel)"""
    
    print("\n" + "="*60)
    print("🔄 Session Recovery Test")
    print("="*60)
    
    # 새 세션에서 로드
    print("\n📂 Loading previous session...")
    
    vector_backend = VectorDBBackend(
        backend_type="chroma",
        path="./chroma_db_demo",
        collection_name="cognitive_memory"
    )
    
    kernel = CognitiveKernel("vector_demo")
    kernel.load()
    
    print("   ✅ Loaded Cognitive Kernel")
    print("   ✅ Loaded Vector DB")
    
    # 검색 테스트
    print("\n🔍 Testing search after recovery...")
    results = vector_backend.search("meeting", k=3)
    print(f"   Found {len(results)} results")
    
    ranked = kernel.recall(k=3)
    print(f"   Top {len(ranked)} memories by importance")
    
    print("\n   ✅ Session recovery successful!")


# ============================================================
# 🏃 Main
# ============================================================

if __name__ == "__main__":
    print("\n🧠 Cognitive Kernel + Vector DB (Chroma) Demo")
    print("━" * 60)
    
    try:
        demo_vector_db_integration()
        demo_session_recovery()
        
        print("\n" + "="*60)
        print("📊 Summary")
        print("="*60)
        print("""
┌─────────────────────────────────────────────────────────┐
│  Feature              │ Vector DB │ Cognitive Kernel   │
├─────────────────────────────────────────────────────────┤
│  Semantic Search     │    ✅     │       ❌            │
│  Importance Ranking  │    ❌     │       ✅ (PageRank)│
│  Time Decay          │    ❌     │       ✅            │
│  Persistence         │    ✅     │       ✅            │
│  Hybrid Search       │    ✅     │       ✅ (Combined) │
└─────────────────────────────────────────────────────────┘

💡 Best Practice:
   Use Vector DB for semantic search,
   then re-rank by Cognitive Kernel's importance score.
        """)
        
    except ImportError as e:
        print(f"\n❌ Missing dependency: {e}")
        print("\n📦 Install required packages:")
        print("   pip install chromadb sentence-transformers")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

