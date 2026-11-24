# IgniteServe: Accelerating LLM Serving Engine Cold Starts via Fine-Grained Parallelization

**中文标题**：IgniteServe：通过细粒度并行化加速 LLM 服务引擎冷启动

**所属 Session**：[Session 4: Serverless and Elastic LLM Inference](index.md) · [ATC 2026](../index.md)

**作者**：Wenbiao Cao (Huazhong University of Science and Technology), Hang Huang (Huazhong University of Science and Technology), Jia Rao (The University of Texas at Arlington), Zhuo Huang (Huazhong University of Science and Technology), Song Wu (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

## 英文摘要
Elasticity is central to the economics of Model-as-a-Service (MaaS) platforms, where LLMs are exposed as managed APIs and backend serving capacity must track rapidly changing demand. In this setting, cold start determines how quickly newly allocated GPU resources can be converted into useful inference capacity. Modern LLM serving engines complicate this path by embedding steady-state optimizations such as compilation and CUDA graph capture into startup. Although these optimizations improve warm-engine efficiency, they introduce expensive, state-dependent tasks that are still commonly organized into a fixed serial pipeline. As a result, the primary bottleneck in engine cold start is shifting from model loading to an orchestration problem over heterogeneous optimization state on the scale-out critical path. In this paper, we present IgniteServe, a system that accelerates cold starts in LLM serving engines through fine-grained parallelization. IgniteServe is built on the insight that much of the startup serialization reflects implementation order rather than true dependency. It models initialization as a state-aware execution graph and breaks coarse startup barriers into schedulable units across and within stages. This enables loosely coupled initialization tasks to overlap, compilation to be parallelized and reused at subgraph granularity, and CUDA graphs to be materialized according to runtime utility without disabling optimized inference. Comprehensive evaluations with real-world LLM workloads show that IgniteServe improves cold-start responsiveness while preserving steady-state efficiency. It reduces startup latency over vLLM by 69.3% and 56% on average across fully cold and cache-resident states, and outperforms state-of-the-art static optimization approaches, ServerlessLLM by 65.4% and 46% and Medusa by 61% and 40.1%, respectively. IgniteServe further reduces cold-start TTFT by 69% while maintaining post-startup TTFT and TPOT comparable to optimized vLLM.

## 中文摘要
弹性是模型即服务（MaaS）平台经济性的核心，在该类平台中 LLM 以托管 API 的形式对外提供，后端服务容量必须跟上快速变化的需求。在此场景下，冷启动决定了新分配的 GPU 资源能以多快转化为有效的推理容量。现代 LLM 服务引擎将编译和 CUDA 图捕获等稳态优化嵌入启动过程，使这条路径变得复杂。这些优化虽然提升了热引擎的效率，却引入了开销高昂且依赖状态的任务，而这些任务仍普遍被组织成固定的串行流水线。因此，引擎冷启动的主要瓶颈正在从模型加载转变为横向扩容关键路径上针对异构优化状态的编排问题。本文提出 IgniteServe，一个通过细粒度并行化加速 LLM 服务引擎冷启动的系统。IgniteServe 建立在这样一个洞察之上：启动过程中的大量串行化反映的是实现顺序而非真实依赖。它将初始化建模为状态感知的执行图，并把粗粒度的启动屏障拆解为跨阶段及阶段内可调度的单元。这使松耦合的初始化任务可以重叠，编译可以在子图粒度上并行化并被复用，CUDA 图可以根据运行时效用进行物化，而无需关闭优化后的推理。基于真实 LLM 负载的全面评估表明，IgniteServe 在保持稳态效率的同时提升了冷启动响应性。在完全冷启动与缓存常驻两种状态下，它相较 vLLM 将启动延迟分别降低 69.3% 和 56%，并分别以 65.4% 和 46% 优于最先进的静态优化方法 ServerlessLLM，以 61% 和 40.1% 优于 Medusa。IgniteServe 还将冷启动 TTFT 降低 69%，同时使启动后的 TTFT 与 TPOT 与优化后的 vLLM 相当。

## 英文关键词
LLM serving, cold start, parallelization

## 中文关键词
LLM 服务，冷启动，并行化

[返回 Session 4](index.md) · [返回 ATC 2026](../index.md)
