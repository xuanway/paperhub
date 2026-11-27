MATCHA: Efficient Deployment of Deep Neural Networks on Multi-Accelerator Heterogeneous Edge SoCs
Authors：
[Enrico Russo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3233987296527478242)，[Mohamed Hamdi](https://63dac.conference-program.com/?post_type=page&p=15&uid=5348508668988401028)，[Alessandro Ottaviano](https://63dac.conference-program.com/?post_type=page&p=15&uid=7678176536033355894)，[Francesco Conti](https://63dac.conference-program.com/?post_type=page&p=15&uid=433243)，[Angelo Garofalo](https://63dac.conference-program.com/?post_type=page&p=15&uid=538243)，[Daniele Jahier Pagliari](https://63dac.conference-program.com/?post_type=page&p=15&uid=731243)，[Maurizio Palesi](https://63dac.conference-program.com/?post_type=page&p=15&uid=684143)，[Luca Benini](https://63dac.conference-program.com/?post_type=page&p=15&uid=062443)，[Alessio Burrello](https://63dac.conference-program.com/?post_type=page&p=15&uid=77214126180186189671)

## 中文标题

MATCHA：在多加速器异构边缘 SoC 上高效部署深度神经网络

## 英文摘要

Deploying DNNs on System-on-Chips (SoC) with multiple heterogeneous acceleration engines is challenging, and the majority of deployment frameworks cannot fully exploit heterogeneity. We present MATCHA, a unified DNN deployment framework that generates highly concurrent schedules for parallel, heterogeneous accelerators and uses constraint programming to optimize L3/L2 memory allocation and scheduling. Using pattern matching, tiling, and mapping across individual HW units enables parallel execution and high accelerator utilization. On the MLPerf Tiny benchmark, using a SoC with two heterogeneous accelerators, MATCHA improves accelerator utilization and reduces inference latency by up to 35% with respect to the state-of-the-art MATCH compiler.

## 中文摘要

在集成多个异构加速引擎的片上系统（SoC）上部署 DNN 颇具挑战，且多数部署框架无法充分利用其异构性。我们提出 MATCHA，这是一个统一的 DNN 部署框架，可为并行运行的异构加速器生成高度并发的调度方案，并利用约束规划优化 L3/L2 内存分配与调度。通过在各个硬件单元上进行模式匹配、分块与映射，可实现并行执行与较高的加速器利用率。在 MLPerf Tiny 基准上，使用配备两个异构加速器的 SoC，MATCHA 相对最先进的 MATCH 编译器提升了加速器利用率，并将推理时延最多降低 35%。

## 英文关键词

Heterogeneous SoCs, DNNs, AI Deployment Framework, TinyML

## 中文关键词

异构 SoC、DNN、AI 部署框架、TinyML
