Paretopilot: Global Optimization Reasoning on HLS Design Space Exploration with LLMs
Authors：
[Jia Xiong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1380754946707582248)，[Runkai Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=9916070088511999994)，[Haowen Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=53757909892479366011)，[Cheng Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=6400072404440362467)，[Ziran Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=127643)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)

## 中文标题

ParetoPilot：基于 LLM 的 HLS 设计空间探索全局优化推理

## 英文摘要

The combinatorial explosion of directives in high-level synthesis (HLS) creates an expansive design space, impeding the agility and productivity of HLS. Previous efforts to construct design space exploration (DSE) methods with heuristics struggle to precisely identify Pareto-optimal designs under tight search budgets. The advanced reasoning capabilities of large language models (LLMs) present a promising avenue for multi-objective optimization. Therefore, we introduce ParetoPilot, an automated DSE framework, which leverages a dedicated LLM to adopt global optimization reasoning to navigate exploration. Guided by optimization strategies, ParetoPilot integrates directive scheduling and quality awareness to rapidly shape broad and concave Pareto fronts. Compared to a SOTA heuristic-based DSE method, ParetoPilot improves the DSE performance by 49.5% and achieves a 2.2× efficiency gain, outperforming the auxiliary LLM DeepSeek-R1 by 81.4%. The Repo. of code: https://github.com/GEAR-SEU/ParetoPilot-DAC-26.

## 中文摘要

高层综合（HLS）中编译指示（directive）的组合爆炸造成了庞大的设计空间，阻碍了 HLS 的敏捷性与生产力。以往基于启发式方法构建设计空间探索（DSE）方法的工作，在紧张的搜索预算下难以精确识别 Pareto 最优设计。大语言模型（LLM）强大的推理能力为多目标优化提供了新的途径。为此，我们提出 ParetoPilot，一个自动化 DSE 框架，利用专门的 LLM 以全局优化推理来引导探索过程。在优化策略的指导下，ParetoPilot 融合编译指示调度与质量感知，能够快速塑造宽广且凹形的 Pareto 前沿。与当前最优（SOTA）的基于启发式的 DSE 方法相比，ParetoPilot 将 DSE 性能提升 49.5%，实现 2.2 倍的效率提升，并比辅助 LLM DeepSeek-R1 高出 81.4%。代码仓库：https://github.com/GEAR-SEU/ParetoPilot-DAC-26。

## 英文关键词

High-Level Synthesis, LLM, Design Space Exploration

## 中文关键词

高层综合、LLM、设计空间探索
