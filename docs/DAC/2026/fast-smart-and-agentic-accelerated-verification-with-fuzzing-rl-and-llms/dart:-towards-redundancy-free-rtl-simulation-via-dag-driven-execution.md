Dart: Towards Redundancy-Free RTL Simulation via DAG-Driven Execution
Authors：
[Jingyi Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=90815472907489491001)，[Yi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7676833668777047982)，[Yu Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=427343)，[Yang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=60256677325270448231)，[Chunyan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=35437635406848913271)，[Shaofei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=9937783642405233276)，[Xueqi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=77855308624011050141)，[Long Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=976343)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)

## 中文标题

Dart：面向无冗余 RTL 仿真的 DAG 驱动执行方法

## 英文摘要

Register Transfer Level (RTL) simulation is key to pre-silicon verification, yet its performance has stagnated in the face of rapidly escalating SoC complexity. Although recent CPU-and GPU-based simulators improve throughput through per-stimulus optimization or batch parallelism, they execute each stimulus in isolation and therefore fail to exploit the substantial computation locality that emerges across stimuli. As many stimuli converge to identical internal states, large portions of the circuit are redundantly re-evaluated, forming a principal bottleneck to scalable RTL simulation. This paper introduces Dart, a Directed Acyclic Graph (DAG)- driven RTL simulation framework that systematically eliminates cross-stimulus redundancy. Dart constructs a DAG-based intermediate representation that makes structural commonality and shared subexpressions across stimuli explicit, enabling principled redundancy elimination through systematic sub-DAG merging. A computation-centric execution engine evaluates shared logic once and amortizes its results across all stimuli that traverse the corresponding state, while a lightweight state-reconstruction mechanism preserves per-stimulus correctness with negligible overhead. Across a suite of industrial RTL designs, Dart delivers speedups of up to 136.7× over Verilator and 4.1× over RTLflow, respectively.

## 中文摘要

寄存器传输级（RTL）仿真是硅前验证的关键环节，但面对急剧上升的 SoC 复杂度，其性能却长期停滞。尽管近期的 CPU 与 GPU 仿真器通过针对单个激励的优化或批处理并行提升了吞吐率，但它们孤立地执行每个激励，因而无法利用跨激励之间出现的大量计算局部性。由于许多激励会收敛到相同的内部状态，电路中很大一部分被冗余地重复求值，这构成可扩展 RTL 仿真的主要瓶颈。本文提出 Dart，一种有向无环图（DAG）驱动的 RTL 仿真框架，可系统性地消除跨激励冗余。Dart 构建基于 DAG 的中间表示，使跨激励的结构共性与公共子表达式显式化，从而通过系统化的子 DAG 合并实现有原则的冗余消除。以计算为中心的执行引擎对共享逻辑只求值一次，并将其结果分摊到所有经过相应状态的激励上；同时，轻量级状态重建机制以可忽略的开销保证每个激励的正确性。在一系列工业 RTL 设计上，Dart 相较 Verilator 最高加速 136.7 倍，相较 RTLflow 最高加速 4.1 倍。
