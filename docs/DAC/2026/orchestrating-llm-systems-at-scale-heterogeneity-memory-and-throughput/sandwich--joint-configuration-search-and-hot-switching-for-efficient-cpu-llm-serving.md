Sandwich: Joint Configuration Search and Hot-Switching for Efficient CPU LLM Serving
Authors：
[JUNTAO ZHAO](https://63dac.conference-program.com/?post_type=page&p=15&uid=6039817371916706577)，[Jiuru Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=90784440532123582471)，[Chuan Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7067130159859088568)

## 中文标题

Sandwich：面向高效 CPU LLM 服务的配置联合搜索与热切换

## 英文摘要

CPUs are critical for LLM serving due to their availability, cost efficiency, and edge applicability. However, efficient CPU serving is hindered by conflicting prefill/decode resource demands under non-disaggregated deployment constraints—existing solutions fail to avoid cross-phase interference, ignore sub-NUMA hardware structures, and deliver suboptimal dynamic-shape kernel performance. We propose Sandwich, a full-stack CPU LLM serving system with three core innovations addressing these challenges: (1) seamless phase-wise plan switching to eliminate cross-phase interference; (2) TopoTree, a tree-based hardware abstraction for automated substructure-aware (e.g., LLC slices) partial core allocation; (3) fast-start-then-finetune dynamic-shape tensor program generation. Evaluated on five x86 and ARM CPU platforms, Sandwich achieves a 2.01× average end-to-end speedup and supports up to 3.40× tighter TTFT and TPOT latency bounds while keeping over 90% of requests within the specified SLOs, compared to state-of-the-art systems. Its kernels match static compiler performance with three orders of magnitude lower tuning cost.

## 中文摘要

由于可用性高、成本效益好且适用于边缘场景，CPU 对 LLM 服务至关重要。然而，在非分离式部署约束下，prefill 与 decode 阶段的资源需求相互冲突，阻碍了高效的 CPU 服务：现有方案无法避免跨阶段干扰，忽略了 sub-NUMA 硬件结构，且动态形状内核性能欠佳。我们提出 Sandwich，一个全栈 CPU LLM 服务系统，以三项核心创新应对上述挑战：(1) 无缝的阶段级计划切换，消除跨阶段干扰；(2) TopoTree，一种基于树的硬件抽象，用于自动化的子结构感知（如 LLC 切片）部分核心分配；(3) 先快速启动再微调的动态形状张量程序生成。在五个 x86 与 ARM CPU 平台上评估，与最先进系统相比，Sandwich 实现平均 2.01 倍的端到端加速，并支持收紧至 3.40 倍的 TTFT 与 TPOT 延迟界，同时使超过 90%的请求满足指定 SLO。其内核性能与静态编译器相当，而调优开销低三个数量级。
