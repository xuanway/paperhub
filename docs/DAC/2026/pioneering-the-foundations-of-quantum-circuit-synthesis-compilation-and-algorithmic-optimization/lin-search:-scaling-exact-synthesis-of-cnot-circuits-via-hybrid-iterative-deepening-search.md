Lin-Search: Scaling Exact Synthesis of CNOT Circuits via Hybrid Iterative Deepening Search
Authors：
[Chenjian Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7958711506324764349)，[Xiangzhen Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=9021384630391526397)，[Ji Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=62722019784785485521)，[Fanxu Meng](https://63dac.conference-program.com/?post_type=page&p=15&uid=50990012899996393381)，[Pengcheng Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4923897844208575157)，[Yu Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=8427957691503961147)

## 中文标题

Lin-Search：通过混合迭代加深搜索扩展 CNOT 线路的精确综合

## 英文摘要

Exact synthesis of CNOT circuits is a core primitive in quantum compilers, but existing SAT-based and database-based methods suffer from encoding overhead, memory bottlenecks, and poor scalability. We propose Lin-search, a framework for exact CNOT synthesis based on iterative deepening search. Lin-search explores circuits in non-decreasing gate count while pruning partial solutions using variable-mismatch constraints, matrix-based lower bounds, and canonicalization under local circuit equivalences. In random benchmarks, Lin-search finds optimal circuits with up to 15 qubits and 15 CNOT gates in 600 seconds on a laptop, achieving up to speedup 100×–1000× and scalability of +3 qubits over a SAT-based baseline incorporated in Qiskit. When integrated as a rewriting kernel in a Clifford+T optimization flow, Lin-search further reduces CNOT count by 16% compared to the original circuits on average and decreases timeout counts by 30% compared to the SAT-based method, demonstrating its effectiveness as a practical exact synthesis engine for quantum compilers.

## 中文摘要

CNOT 线路的精确综合是量子编译器的核心基础操作，但现有的基于 SAT 和基于数据库的方法存在编码开销、内存瓶颈以及可扩展性差等问题。我们提出 Lin-search，一个基于迭代加深搜索的精确 CNOT 综合框架。Lin-search 以非递减的门数探索线路，并利用变量失配约束、基于矩阵的下界以及局部线路等价下的规范化来剪枝部分解。在随机基准上，Lin-search 可在笔记本电脑上于 600 秒内找到最多 15 个量子比特、15 个 CNOT 门的线路最优解，相比集成于 Qiskit 的基于 SAT 的基线实现最高 100×–1000×的加速和+3 个量子比特的可扩展性。当作为重写内核集成到 Clifford+T 优化流程中时，Lin-search 相比原始线路平均进一步减少 16%的 CNOT 数量，并将超时次数相比基于 SAT 的方法降低 30%，表明其作为量子编译器实用精确综合引擎的有效性。

## 英文关键词

Exact Synthesis, Quantum Circuit Synthesis, CNOT Circuit, Search-based Method

## 中文关键词

精确综合、量子线路综合、CNOT 线路、基于搜索的方法
