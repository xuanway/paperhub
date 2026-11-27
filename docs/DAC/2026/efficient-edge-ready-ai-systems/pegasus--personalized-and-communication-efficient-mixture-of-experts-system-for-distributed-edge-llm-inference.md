Pegasus: Personalized and Communication-Efficient Mixture-of-Experts System for Distributed Edge LLM Inference
Authors：
[Zhixuan Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5793121216101703421)，[Kongyange Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=00549638204369988701)，[Tao Ouyang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2976543393599488647)，[Liekang Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=23421446554280910131)，[Siqi Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=97518606969857510571)，[Xu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7493567371918967319)

## 中文标题

Pegasus：面向分布式边缘 LLM 推理的个性化且通信高效的混合专家系统

## 英文摘要

Large Language Models (LLMs) are increasingly pushed to the edge to reduce latency, yet limited memory and compute make full-model deployment infeasible. Mixture-of-Experts (MoE) offers a lightweight alternative, but edge nodes can host only a few experts, creating persistent mismatches between dynamic query semantics and locally available expert models under resource constraints. We present Pegasus, a collaborative MoE inference system for multi-edge deployments that leverages the spatiotemporal correlations inherent in distributed query semantics. Pegasus integrates three innovations: (i) a similarity-based expert deployment mechanism using an efficient heuristic metric to assess the semantic relevance between queries and experts across nodes and over time; (ii) a personalized gating design that selectively fine-tunes a subset of gating parameters on each node to balance expert accuracy and communication latency; (iii) an intra-node online scheduling algorithm with adaptive batching for efficient memory utilization. Extensive performance evaluations corroborate that Pegasus achieves 11.8× lower inference latency than state-of-the-art distributed MoE frameworks, demonstrating high-throughput and communication-efficient edge LLM inference.

## 中文摘要

大语言模型（LLM）正日益被推向边缘以降低延迟，但有限的内存与算力使全模型部署不可行。混合专家（MoE）提供了一种轻量级替代方案，但边缘节点只能承载少量专家，在资源约束下，动态查询语义与本地可用专家模型之间持续存在失配。我们提出 Pegasus，一种面向多边缘部署的协同 MoE 推理系统，它利用分布式查询语义中固有的时空相关性。Pegasus 融合了三项创新：（i）一种基于相似度的专家部署机制，使用高效的启发式度量来评估跨节点、跨时间的查询与专家之间的语义相关性；（ii）一种个性化门控设计，在每个节点上选择性地微调一部分门控参数，以平衡专家精度与通信延迟；（iii）一种节点内在线调度算法，采用自适应批处理以实现高效的内存利用。大量性能评测证实，Pegasus 相比最先进的分布式 MoE 框架实现了 11.8× 的推理延迟降低，展现了高吞吐、通信高效的边缘 LLM 推理。
