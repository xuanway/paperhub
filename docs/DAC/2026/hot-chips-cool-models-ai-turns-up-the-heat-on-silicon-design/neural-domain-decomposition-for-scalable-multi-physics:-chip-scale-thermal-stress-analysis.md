Neural Domain Decomposition for Scalable Multi-Physics: Chip-Scale Thermal-Stress Analysis
Authors：
[Min-Chul Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5763180552649557424)，[Ji-Hye Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=9331847196907938216)，[Sungyeop Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=0282947559460120317)，[Giyong Hong](https://63dac.conference-program.com/?post_type=page&p=15&uid=4472959928196599808)，[Seokki Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=46652438717159521011)，[In Huh](https://63dac.conference-program.com/?post_type=page&p=15&uid=140243)，[Hong-hyun Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=4300390119042442632)，[Hyunjae Jang](https://63dac.conference-program.com/?post_type=page&p=15&uid=45280026099456167371)，[Changwook Jeong](https://63dac.conference-program.com/?post_type=page&p=15&uid=0513887886479652477)，[Young-Gu Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=2564116082018298461)，[Dae Sin Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=2799986148803476073)

## 中文标题

面向可扩展多物理场的神经区域分解：芯片级热-应力分析

## 英文摘要

Large neural surrogate models accelerate scientific simulation but still face scalability limits from model size and memory. We present FP-DDM (Foundation-model-based Physics-guided adaptation for the Domain Decomposition Method), a scalable framework for large-scale physics analysis. FP-DDM divides the domain into overlapping subdomains and enforces interface consistency by explicitly optimizing boundary values on overlaps via automatic differentiation, enabling fast alignment. Specifically, we propose a foundation architecture that effectively learns multi-physics and transfers to new domains. The combination of foundation-model adaptation and physics-guided test-time adaptation enables generalization to new physics and unseen domains without labels. On thermal and stress problems, FP-DDM achieves numerical-solver-level accuracy, scales to 10-billion-cell domains, and supports layout design optimization, establishing its potential as a multi-physics platform for next-generation system–technology co-optimization.

## 中文摘要

大型神经代理模型可加速科学仿真，但仍受限于模型规模与内存带来的可扩展性瓶颈。我们提出 FP-DDM（面向区域分解方法的基于基础模型的物理引导适配框架），一个用于大规模物理分析的可扩展框架。FP-DDM 将求解域划分为相互重叠的子域，并通过自动微分显式优化重叠区域上的边界值来强制满足界面一致性，从而实现快速对齐。具体而言，我们提出一种基础架构，能够有效学习多物理场特性并迁移至新的域。基础模型适配与物理引导的测试时自适应相结合，使框架无需标签即可泛化到新的物理场与未见过的域。在热学与应力问题上，FP-DDM 达到数值求解器级别的精度，可扩展至百亿单元规模的求解域，并支持版图设计优化，展现出作为面向下一代系统-工艺协同优化的多物理场平台的潜力。

## 英文关键词

scientific foundation model, domain decomposition, Schwarz

## 中文关键词

科学基础模型、区域分解、Schwarz
