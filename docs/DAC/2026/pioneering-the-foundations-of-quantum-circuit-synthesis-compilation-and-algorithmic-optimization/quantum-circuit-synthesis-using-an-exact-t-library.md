Quantum Circuit Synthesis Using an Exact T Library
Authors：
[Hanyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6868441288308145007)，[Mingfei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=64154605324313942921)，[Xinrui Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=56742650368336897701)，[Jason Cong](https://63dac.conference-program.com/?post_type=page&p=15&uid=322343)

## 中文标题

使用精确 T 库的量子线路综合

## 英文摘要

In fault-tolerant quantum circuit synthesis, T gates supplied via magic states dominate space–time cost, while Clifford gates incur negligible overhead. Conventional flows minimize AND count in an {XOR, AND, NOT} basis as a proxy for T, which neglects phase cancellation and can be far from T-optimal. We instead formulate an exact T synthesis problem and canonicalize Boolean functions under Clifford equivalence. By precomputing T-optimal implementations up to seven variables and developing a customized mapper, we reduce the T count by up to 14.3% on EPFL benchmarks and improve the T counts of several cryptographic modules by up to 40%.

## 中文摘要

在容错量子线路综合中，经 magic state 提供的 T 门主导了时空开销，而 Clifford 门的开销可忽略不计。传统流程在{XOR, AND, NOT}基下最小化 AND 数量，以此作为 T 的替代指标，这种做法忽略了相位抵消，可能远离 T 最优。我们转而将精确 T 综合表述为一个问题，并在 Clifford 等价下对布尔函数进行规范化。通过预计算最多七个变量的 T 最优实现并开发定制映射器，我们在 EPFL 基准上最多降低 14.3%的 T 数量，并将若干密码模块的 T 数量最多改善 40%。
