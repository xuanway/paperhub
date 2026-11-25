Fast Template Matching for Quantum Circuits Using Hypergraph
Authors：
[Xin Hong](https://63dac.conference-program.com/?post_type=page&p=15&uid=4195721722929764756)，[Jintao Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=87087462617223711501)，[Runhong He](https://63dac.conference-program.com/?post_type=page&p=15&uid=12093453319800532021)，[Shenggang Ying](https://63dac.conference-program.com/?post_type=page&p=15&uid=55310813763969621711)，[Sanjiang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=788243)，[Mingsheng Ying](https://63dac.conference-program.com/?post_type=page&p=15&uid=270543)

## 中文标题

基于超图的量子线路快速模板匹配

## 英文摘要

Quantum circuit optimization is a key step toward the efficient execution of quantum algorithms. Template matching has emerged as one of the dominant approaches for simplifying quantum circuits, yet it confronts the intrinsic challenge of accommodating gate commutativity. The state-of-the-art template-matching algorithm relies on a directed acyclic graph (DAG) representation. While this DAG-based technique handles gate commutativity satisfactorily, it fails to preserve the local connectivity inherent to quantum circuits, thereby leading to relatively high matching complexity. In this paper, we introduce a hypergraph representation (HG), a commutativity-aware representation that collapses commuting gates into a single super-node while retaining all local connectivity. This enables matches to be extended locally without revisiting the rest of the circuit, with incremental updates limited to the immediate neighborhood. Experimental results demonstrate that our HG matcher achieves 11–606× speed-up over the DAG-based implementation in Qiskit (Iten et al., 2022) on both random and arithmetic benchmarks, while maintaining the same optimization quality. The acceleration increases with circuit size, confirming that preserving locality and connectivity is the key to scalable quantum circuit optimisation.

## 中文摘要

量子线路优化是高效执行量子算法的关键步骤。模板匹配已成为简化量子线路的主流方法之一，但它面临容纳门可交换性这一内在挑战。最先进的模板匹配算法依赖于有向无环图（DAG）表示。这种基于 DAG 的技术虽然能够较好地处理门可交换性，却未能保留量子线路固有的局部连通性，从而导致匹配复杂度相对较高。本文引入超图表示（HG），一种可交换性感知的表示，它将可交换的门折叠为单个超节点，同时保留全部局部连通性。这使得匹配可以在局部扩展而无需重新访问线路的其余部分，增量更新仅限于紧邻区域。实验结果表明，我们的 HG 匹配器在随机基准和算术基准上相比 Qiskit（Iten et al., 2022）中基于 DAG 的实现取得 11–606 倍的加速，同时保持相同的优化质量。加速比随线路规模增大而提升，证实了保持局部性与连通性是实现可扩展量子线路优化的关键。

## 英文关键词

quantum circuits, template match, hypergraph

## 中文关键词

量子线路、模板匹配、超图
