Maple: Efficient Data-Transfer-Aware Mapping Exploration for NDP-Enabled Edge LLM Inference
Authors：
[Xuefeng Hua](https://63dac.conference-program.com/?post_type=page&p=15&uid=58243814567003361341)，[Cong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=82428948505715603361)，[Xin Si](https://63dac.conference-program.com/?post_type=page&p=15&uid=06525473388796445)，[Qiang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=938302086440658382)，[Guangyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=470243)

## 中文标题

Maple：面向 NDP 赋能的边缘 LLM 推理的高效数据传输感知映射探索

## 英文摘要

Near-DRAM Processing (NDP) has demonstrated great potential for memory-bound operators in edge-side large language model (LLM) inference. Featuring a xPU-NDP heterogeneous system, existing designs concentrate on optimizing the execution flow within processing units, yet ignoring the bottleneck arising from xPU-NDP data transfer. To tackle this challenge, we propose Maple, an efficient mapping exploration framework. Given a specific workload and NDP architecture, Maple adopts an address-mapping-based description method to construct a comprehensive search space that encompasses resource grouping, tensor partitioning and transfer binding, thereby facilitating joint optimization of computation and data transfer. Experiments show that Maple achieves an improvement of up to 3.34× in performance and 1.49× in energy compared with existing approaches on mainstream NDP architectures.

## 中文摘要

近 DRAM 处理（NDP）在边缘侧大语言模型（LLM）推理的受带宽约束算子中展现出巨大潜力。现有设计采用 xPU-NDP 异构系统，主要聚焦于优化处理单元内部的执行流，却忽视了 xPU 与 NDP 之间数据传输所引发的瓶颈。为应对这一挑战，我们提出 Maple——一个高效的映射探索框架。针对特定负载与 NDP 架构，Maple 采用基于地址映射的描述方法，构建涵盖资源分组、张量划分与传输绑定的完备搜索空间，从而便于计算与数据传输的联合优化。实验表明，在主流 NDP 架构上，Maple 相较现有方法可实现最高 3.34 倍的性能提升与 1.49 倍的能耗改善。

## 英文关键词

Near-Memory Processing, Design Space Exploration

## 中文关键词

近存处理、设计空间探索
