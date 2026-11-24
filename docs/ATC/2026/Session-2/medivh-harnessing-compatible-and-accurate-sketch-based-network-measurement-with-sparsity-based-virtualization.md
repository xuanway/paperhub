# Medivh: Harnessing Compatible and Accurate Sketch-based Network Measurement with Sparsity-based Virtualization

**中文标题**：Medivh：借助基于稀疏性的虚拟化实现兼容且准确的草图网络测量

**所属 Session**：[Session 2: Network Measurement and Simulation](index.md) · [ATC 2026](../index.md)

**作者**：Xiang Chen (Zhejiang University), Feng Zhu (Independent Researcher), Hongmin Tan (Zhejiang University), Jiayu Li (Zhejiang University), Jiashuo Yu (Zhejiang University), Longlong Zhu (Zhejiang University), Xingyuan Li (Zhejiang University), Yuchen Xian (Zhejiang University), Jiajie Su (Zhejiang University), Xingwei Lin (Zhejiang University), Qiang Wu (Zhejiang University), Chunming Wu (Zhejiang University)

## 英文摘要
Sketches build their data structures in data plane switches to perform approximate measurements towards high-speed traffic. However, switch resources constraints create an intractable trade-off between the compatibility with network functions and high accuracy. Allocating enough resources to sketches affects concurrent network functions and results in loss of compatibility. In contrast, without enough resources, sketches suffer from accuracy loss. We propose Medivh, a framework that achieves both compatibility and high accuracy in sketch-based network measurement. For compatibility, Medivh uses residual switch resources to place sketches, avoiding affecting concurrent network functions. For high accuracy, it leverages the sparsity of sketch data, i.e., only a few values are non-zero due to traffic skewness, to implement a sketchlet hypervisor. This hypervisor virtualizes sketch rows, i.e., sketchlets, by mapping multiple virtual sketchlets to a shared physical hash table that stores only non-zero values. Hence, every sketch can work with enough resources and provide high accuracy. We evaluate Medivh with various sketches, diverse production workloads and applications. (1) In our testbed comprising 32×400 Gbps Tofino2 switches, Medivh improves accuracy by 24.4%–88.7% under strict compatibility. (2) In production use cases, it boosts sketch placement, supports distributed attack detection, and handles runtime dynamics.

## 中文摘要
草图在数据平面交换机中构建其数据结构，以对高速流量进行近似测量。然而，交换机资源约束在网络功能兼容性与高准确度之间造成难以处理的权衡。为草图分配足够的资源会影响并发的网络功能，导致兼容性丧失。相反，若资源不足，草图则会遭受准确度损失。我们提出 Medivh，一个在基于草图的网络测量中同时实现兼容性与高准确度的框架。为获得兼容性，Medivh 使用交换机的剩余资源来放置草图，避免影响并发的网络功能。为获得高准确度，它利用草图数据的稀疏性（即由于流量倾斜，只有少量值为非零）实现了一个 sketchlet 监管器。该监管器通过把多个虚拟 sketchlet 映射到一张只存储非零值的共享物理哈希表，来虚拟化草图的各行（即 sketchlet）。因此，每个草图都能在资源充足的情况下工作并提供高准确度。我们用多种草图、多样化的生产负载和应用对 Medivh 进行了评估。（1）在由 32×400 Gbps Tofino2 交换机组成的测试平台上，Medivh 在严格兼容性条件下将准确度提升 24.4%–88.7%。（2）在生产用例中，它提升了草图放置，支持分布式攻击检测，并能处理运行时动态变化。

## 英文关键词
Network Measurement, Sketch, Programmable Switch

## 中文关键词
网络测量，草图，可编程交换机

[返回 Session 2](index.md) · [返回 ATC 2026](../index.md)
