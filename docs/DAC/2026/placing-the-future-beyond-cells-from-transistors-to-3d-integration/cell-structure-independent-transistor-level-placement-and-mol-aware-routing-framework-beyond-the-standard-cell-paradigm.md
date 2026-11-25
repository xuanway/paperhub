Cell-Structure-Independent Transistor-Level Placement and MOL-Aware Routing Framework Beyond the Standard-Cell Paradigm
Authors：
[Keyu Peng](https://63dac.conference-program.com/?post_type=page&p=15&uid=220843)，[Hao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=715843)，[Yinuo Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03556589452874932661)，[qingsheng qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9909404457859214141)，[Hao Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=020843)，[Ziran Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=127643)，[Chao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=865843)，[Yang Jun](https://63dac.conference-program.com/?post_type=page&p=15&uid=6386049648875323069)

## 中文标题

超越标准单元范式的与单元结构无关的晶体管级布局及 MOL 感知布线框架

## 英文摘要

Standard-cell-based design has long served as the foundation of modern VLSI implementation due to its scalability and compatibility with mainstream EDA flows. However, as design technology co-optimization (DTCO) becomes increasingly important at advanced process nodes, the fixed structure of standard cells limits the ability to optimize wirelength and area effectively, imposing a critical bottleneck at the middle-of-line (MOL) layers. Dense pin access and M0 routing resources, which are essential for mitigating congestion in upper metal layers, are tightly constrained by fixed cell boundaries, creating fundamental obstacles to further physical optimization. This work introduces a cell-structure-independent transistor-level placement framework integrated with an MOL-aware routing engine. The placement stage leverages preemptive diffusion sharing to improve area efficiency without relying on any standard-cell structural priors, while the routing engine systematically manages the highly constrained MOL resources to enable feasible and congestion-aware MOL interconnect. Experimental evaluations show that, under comparable high-utilization conditions, the proposed framework delivers substantial reductions in via count, wirelength, and layout area over both a commercial standard-cell-based physical design tool and the latest transistor-level design methodologies.

## 中文摘要

基于标准单元的设计凭借良好的可扩展性与对主流 EDA 流程的兼容性，长期作为现代 VLSI 实现的基础。然而，随着设计工艺协同优化（DTCO）在先进工艺节点日益重要，标准单元的固定结构限制了有效优化线长与面积的能力，在中段（MOL）层形成关键瓶颈。对于缓解上层金属拥塞至关重要的密集引脚接入与 M0 布线资源，受固定单元边界的严格约束，成为进一步物理优化的根本障碍。本文提出一种与单元结构无关的晶体管级布局框架，并集成 MOL 感知的布线引擎。布局阶段利用预判式扩散共享提升面积效率，而不依赖任何标准单元结构先验；布线引擎系统性地管理高度受限的 MOL 资源，以实现可行且拥塞感知的 MOL 互连。实验评估表明，在可比的高利用率条件下，所提框架相较商用标准单元物理设计工具与最新的晶体管级设计方法，在通孔数量、线长与版图面积上均有大幅降低。
