Area-Optimal and Routability-Driven Layout Synthesis for Multi-Row Complementary-FET Standard Cells
Authors：
[Hao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=715843)，[Keyu Peng](https://63dac.conference-program.com/?post_type=page&p=15&uid=220843)，[Fuxing Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=615843)，[Qiyuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=915843)，[Zhengzhe Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=05124494546850078281)，[Jianli Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=539243)，[Ziran Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=127643)

## 中文标题

面向多行互补场效应晶体管标准单元的面积最优且可布线性驱动的版图综合

## 英文摘要

As conventional FinFET architectures encounter severe scaling limitations, Complementary-FET (CFET) technology with vertically stacked PMOS and NMOS transistors has emerged as a promising solution for continued standard cell density scaling. However, aggressive area compaction in CFET standard cells drastically limits intra-cell routing resources, leading to routing congestion and design rule challenges. To mitigate this issue, multi-row CFET standard cell architectures have been introduced to improve intra-cell routability and alleviate block-level congestion. Nevertheless, these multi-row configurations introduce new placement-routing coupling and design rule complexities, making it challenging to achieve compact, DRC-clean, and routable layouts. Therefore, this work proposes an area-optimal and routability-driven layout synthesis framework for multi-row CFET cells, which effectively addresses the challenges of area efficiency, constrained pin accessibility, and DRC compliance under multi-row CFET architectures. The framework integrates three key methodologies: (1) an Euler-guided transistor partitioning with multi-strategy graph-theoretic pruning to achieve optimal area; (2) an Euler-path-based placement with a combined metric of wirelength and access pin count to improve routability; and (3) a two-stage Satisfiability Modulo Theories (SMT)-based routing flow consisting of a Multi-Commodity Flow (MCF)-based routability-guaranteed pin-access selection and an Integer Linear Programming (ILP)-enhanced hierarchical routing to ensure DRC/LVS closure. Compared with state-of-the-art multi-row CFET cell generators, experimental results show that our algorithm consistently achieves the optimal layout area, while delivering significant improvements in solution quality and efficiency.

## 中文摘要

随着传统 FinFET 架构遭遇严重的微缩瓶颈，将 PMOS 与 NMOS 晶体管垂直堆叠的互补场效应晶体管（CFET）技术已成为延续标准单元密度微缩的有前景方案。然而，CFET 标准单元中激进的面压缩会大幅限制单元内布线资源，导致布线拥塞与设计规则挑战。为缓解该问题，多行 CFET 标准单元架构被引入，以改善单元内可布线性并缓解模块级拥塞。但是，这些多行配置引入了新的布局—布线耦合与设计规则复杂性，使获得紧凑、DRC 干净且可布线的版图变得困难。为此，本工作提出一个面向多行 CFET 单元的面积最优、可布线性驱动的版图综合框架，有效应对多行 CFET 架构下面积效率、引脚可达性受限与 DRC 合规等挑战。该框架集成了三项关键方法：（1）欧拉引导的晶体管划分，结合多策略图论剪枝以实现最优面积；（2）基于欧拉路径的布局，采用线长与可访问引脚数的组合度量以改善可布线性；（3）两阶段基于可满足性模理论（SMT）的布线流程，由基于多商品流（MCF）的可布线性保证引脚接入选择以及 ILP 增强的层次化布线组成，以确保 DRC/LVS 收敛。与先进的多行 CFET 单元生成器相比，实验结果表明我们的算法始终获得最优版图面积，同时在求解质量与效率上均有显著提升。

## 英文关键词

Standard cell synthesis, CFET, multi-row architecture, placement, routing

## 中文关键词

标准单元综合、CFET、多行架构、布局、布线
