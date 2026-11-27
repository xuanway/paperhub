Pcbgen: Self-Evolving LLM Agent for Specification-to-Schematic PCB Design with Parameter Tuning
Authors：
[Yiming Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=86151706451234207771)，[yangbo wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=8944433000540625249)，[Zhangqi Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=71686680815361366641)，[yuhao gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=4837716698130167699)，[Ting-Jung Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=1498611451604654405)，[Jinmei Lai](https://63dac.conference-program.com/?post_type=page&p=15&uid=5274254024499015996)，[Chen Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03136600854360412471)，[Lei He](https://63dac.conference-program.com/?post_type=page&p=15&uid=525543)

## 中文标题

PCBgen：面向规格到原理图 PCB 设计并支持参数调优的自演进 LLM 智能体

## 英文摘要

Printed circuit board (PCB) design is increasingly critical as artificial intelligence (AI) systems demand higher integration density and stricter electrical constraints, while purely manual workflows struggle to keep up. We introduce PCBgen, a verifiable spec-to-schematic framework that integrates PCB knowledge graph (PCB-KG)-based retrieval, constraint-aware pre-filtering, a multi-modal intermediate representation (IR), and SPICE-in-the-loop, training-free Group Relative Policy Optimization (TF-GRPO) into a unified closed-loop pipeline for board-level design. This pipeline compresses an otherwise combinatorial search space (up to ∼1020 candidates) to roughly 103 simulatable designs while preserving semantic and electrical validity. Extensive experiments demonstrate that, on a 336-case benchmark spanning six topology families and three design regimes, PCBgen improves topology adaptation (TA) by up to 57%, raises Pass@5 from 41% to 74%, and cuts token usage and wall-clock time by more than 50% compared with LLM-only baselines. In a 24-case comparison with human designers and vendor tools, it achieves 3.70× and 4.74× speedups in topology selection and schematic verification with comparable Pass@1, yielding an overall return on investment (ROI) of 4.39× and pointing toward a practical route to agentic, closed-loop PCB power design.

## 中文摘要

随着人工智能（AI）系统对集成密度和电气约束提出更高要求，印制电路板（PCB）设计日益关键，而纯人工流程难以跟上这一需求。我们提出 PCBgen，一个可验证的“规格到原理图”框架，它将基于 PCB 知识图谱（PCB-KG）的检索、约束感知预筛选、多模态中间表示（IR）以及 SPICE 在环的无训练分组相对策略优化（TF-GRPO）集成到统一的板级设计闭环流程中。该流程将原本组合爆炸的搜索空间（最多约 10²⁰ 个候选）压缩至约 10³ 个可仿真设计，同时保持语义与电气有效性。大量实验表明，在涵盖六类拓扑族和三种设计模式的 336 个案例基准上，与仅使用 LLM 的基线相比，PCBgen 将拓扑适配（TA）提升最高 57%，将 Pass@5 从 41% 提升至 74%，并将 token 消耗和实际运行时间减少 50% 以上。在与人类设计者和厂商工具的 24 个案例对比中，它在拓扑选择和原理图验证上分别实现 3.70 倍和 4.74 倍的加速，且 Pass@1 相当，整体投资回报率（ROI）达 4.39 倍，为智能体化的闭环 PCB 电源设计指明了实用路径。

## 英文关键词

LLMs, Agentic Workflow, Design Space Exploration

## 中文关键词

大语言模型、智能体工作流、设计空间探索
