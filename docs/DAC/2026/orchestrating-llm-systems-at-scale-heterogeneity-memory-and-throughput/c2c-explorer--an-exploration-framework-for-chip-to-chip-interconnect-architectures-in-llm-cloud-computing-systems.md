C2C-Explorer: An Exploration Framework for Chip-to-Chip Interconnect Architectures in LLM Cloud Computing Systems
Authors：
[Jiayi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=31032444651861906441)，[Di Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=798586036664314651)，[Qingxu Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=60427630602895916461)，[Hongxiao Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=09770345477627044641)，[Jiaqi Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1288453313618923863)，[Anjunyi Fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=66803308039643926421)，[Wenbin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=94694288568845666271)，[Boqiang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1517171102026424749)，[Shuting Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3965647280817821877)，[Shifeng Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3623400983917404857)，[Jianbo Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=2286810203376198024)，[Dimin Niu](https://63dac.conference-program.com/?post_type=page&p=15&uid=327243)，[Bonan Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=646243)

## 中文标题

C2C-Explorer：面向 LLM 云计算系统中芯片间互连架构的探索框架

## 英文摘要

The scaling-up of large language models (LLMs) necessitates computing systems to have multi-processor-chip architectures, elevating the importance of chip-to-chip (C2C) communication. However, designing efficient C2C hardware architectures for LLM workloads faces three key challenges: generating realistic LLM-specific C2C traffic, accurately simulating hardware-level communication at scale, and efficiently exploring the exponentially large C2C design space. We propose C2C-Explorer, an adaptive Bayesian DSE framework that integrates a LLM-workload-driven traffic generator, a scalable interconnect simulator (switch/full-mesh, up to 512 chips), and a metric-guided evaluator into a workload-to-hardware optimization pipeline, enabling systematic C2C architectural codesign under realistic LLM workloads. Validated against FPGA-based C2C prototypes, the C2C simulator achieves 2.46–8.23% end-to-end timing error across diverse traffic patterns. Its hybrid cycle & event model further accelerates large-scale simulation by up to 7.8× over a pure cycle-accurate baseline. Applied to a 32-XPU DeepSeek-R1-671B inference workload, C2C-Explorer identifies configurations that improve goodput by 44.1% and reduce memory by 98.4%. C2C-Explorer is open-source and available at https://github.com/Selinaee/C2C-Explorer.

## 中文摘要

大语言模型（LLM）的规模扩展要求计算系统采用多处理器芯片架构，这提升了芯片间（C2C）通信的重要性。然而，为 LLM 工作负载设计高效的 C2C 硬件架构面临三个关键挑战：生成真实反映 LLM 特性的 C2C 流量、在大规模下精确模拟硬件级通信，以及高效探索指数级庞大的 C2C 设计空间。我们提出 C2C-Explorer，一种自适应贝叶斯 DSE 框架，它将 LLM 工作负载驱动的流量生成器、可扩展的互连模拟器（交换机/全互连，最多支持 512 个芯片）以及指标引导的评估器集成到从工作负载到硬件的优化流水线中，从而在真实 LLM 工作负载下实现系统化的 C2C 架构协同设计。经基于 FPGA 的 C2C 原型验证，C2C 模拟器在多种流量模式下端到端时序误差为 2.46%–8.23%。其周期与事件混合模型相较纯周期精确基线可进一步将大规模仿真加速最多 7.8×。应用于 32-XPU 的 DeepSeek-R1-671B 推理工作负载时，C2C-Explorer 识别出的配置将有效吞吐提升 44.1%，并将内存占用降低 98.4%。C2C-Explorer 已开源，见 https://github.com/Selinaee/C2C-Explorer。

## 英文关键词

chip-to-chip communication, supernode, scale out, LLM simulator, scale up, large language model, cloud computing system

## 中文关键词

芯片间通信、超节点、横向扩展、LLM 模拟器、纵向扩展、大语言模型、云计算系统
