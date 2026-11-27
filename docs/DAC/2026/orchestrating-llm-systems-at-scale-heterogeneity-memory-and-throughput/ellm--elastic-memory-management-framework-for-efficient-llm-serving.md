eLLM: Elastic Memory Management Framework for Efficient LLM Serving
Authors：
[Yi Xiong](https://63dac.conference-program.com/?post_type=page&p=15&uid=9549333124529877619)，[Jiale Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6288107200306992862)，[Rui Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=35911282790681124431)，[Cong Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=824843)，[Zihan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8694590471705758736)，[Yangjie Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=44182212078887390731)，[Weiming Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=52833702830691679301)，[Hao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=39235571788546688381)，[Boyu Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=69918646613486437251)，[Junping Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6060732240499609852)，[Minyi Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=835143)，[Jingwen Leng](https://63dac.conference-program.com/?post_type=page&p=15&uid=473543)，[zongwei zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=372343)，[Xuehai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=513843)

## 中文标题

eLLM：面向高效 LLM 服务的弹性内存管理框架

## 英文摘要

GPU memory management is critical for efficient Large Language Model (LLM) serving. LLM memory usage primarily comprises weights, activations, and KV caches. While weights are static, activations and KV caches exhibit dynamic and unpredictable behavior, posing significant memory management challenges. Modern LLM serving systems address this through a dual-level approach: activations inherit static tensor abstractions from deep learning frameworks, while KV caches employ specialized page-table virtualization (i.e., PagedAttention). Although this reduces KV cache fragmentation, the fundamental isolation between activation and KV cache management prevents memory sharing across these spaces, leading to suboptimal utilization and 20% throughput degradation. To address these limitations, we propose eLLM, an elastic memory management framework. The core components of eLLM include:(1) Virtual Tensor Abstraction: Decouples the virtual address space of tensors from physical GPU memory, creating a unified and flexible memory pool;(2) Elastic Memory Mechanism: Dynamically adjusts memory allocation through runtime memory inflation and deflation, and leverages CPU memory as an extensible buffer;(3) Lightweight Scheduling Strategy: Employs Service-Level Objective (SLO)-aware policies to optimize memory utilization and effectively balance performance trade-offs under stringent SLO constraints. Comprehensive evaluations demonstrate that eLLM outperforms state-of-the-art systems, achieving up to 2.32× higher throughput.

## 中文摘要

GPU 内存管理对高效的大语言模型（LLM）服务至关重要。LLM 的内存占用主要由权重、激活值与 KV 缓存构成。权重是静态的，而激活值与 KV 缓存则表现出动态且不可预测的行为，给内存管理带来严峻挑战。现代 LLM 服务系统通过双层方法应对：激活值沿用深度学习框架中的静态张量抽象，KV 缓存则采用专门的页表虚拟化（即 PagedAttention）。尽管这减少了 KV 缓存碎片，但激活值与 KV 缓存管理之间的根本性隔离阻碍了二者所在空间的跨空间内存共享，导致利用率次优并使吞吐下降 20%。为解决这些局限，我们提出 eLLM，一个弹性内存管理框架。eLLM 的核心组件包括：(1) 虚拟张量抽象：将张量的虚拟地址空间与物理 GPU 内存解耦，构建统一而灵活的内存池；(2) 弹性内存机制：通过运行时的内存膨胀与收缩动态调整内存分配，并将 CPU 内存用作可扩展缓冲区；(3) 轻量级调度策略：采用服务等级目标（SLO）感知的策略优化内存利用率，在严格的 SLO 约束下有效平衡性能权衡。综合评估表明，eLLM 优于最先进系统，吞吐最高提升 2.32 倍。

## 英文关键词

LLM serving, memory management, memory virtualization

## 中文关键词

LLM 服务、内存管理、内存虚拟化
