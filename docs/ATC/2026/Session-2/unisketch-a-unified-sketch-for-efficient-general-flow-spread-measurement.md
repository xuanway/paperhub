# UniSketch: A Unified Sketch for Efficient General Flow Spread Measurement

**中文标题**：UniSketch：面向高效通用流扩散测量的统一草图

**所属 Session**：[Session 2: Network Measurement and Simulation](index.md) · [ATC 2026](../index.md)

**作者**：He Huang (Soochow University), Yifan Han (Soochow University), Chen Lou (University of Science and Technology of China), Yang Du (Soochow University), Yu-E Sun (Soochow University), Jia Liu (Nanjing University), Zhongjun Qiu (Soochow University), Fu Xiao (Nanjing University of Posts and Telecommunications), Guoju Gao (Soochow University), Shigang Chen (University of Florida)

## 英文摘要
High-speed network traffic measurement is critical to a wide range of network functions. A fundamental statistic is flow spread—the number of distinct elements (e.g., destinations, ports, or URLs) associated with a flow. Modern networks increasingly require monitoring multiple spread-based behaviors simultaneously, such as identifying super-spreaders, tracking persistent spread, detecting sudden spread changes, and estimating per-flow spread. However, existing solutions are typically designed for individual tasks, and deploying separate mechanisms in parallel introduces redundancy and high resource overhead. Compared to flow size measurement, flow spread measurement poses greater algorithmic and system challenges due to the need for accurate distinct counting under strict memory and computation constraints, especially in the data plane. This paper proposes UniSketch, a unified framework for flow spread measurement that supports multiple spread-derived monitoring tasks within a single framework. UniSketch is built on a novel Multi-Virtual 2D Bit Array design and a lightweight Virtual Martingale Estimator, enabling efficient online spread estimation for all flows with constant per-packet processing cost. We implement UniSketch on programmable switches and provide theoretical analysis showing asymptotically unbiased estimation and bounded error. Experimental results on four real-world datasets demonstrate that UniSketch achieves significantly higher accuracy and F1-scores than prior approaches, while improving maximum processing throughput by up to 13.67×.

## 中文摘要
高速网络流量测量对广泛的网络功能至关重要。一项基础统计量是流扩散，即与某条流相关联的不同元素（例如目的地、端口或 URL）的数量。现代网络越来越需要同时监测多种基于扩散的行为，例如识别超级扩散者、跟踪持续扩散、检测扩散的突变，以及估计逐流扩散。然而，现有解决方案通常针对单项任务设计，并行部署彼此分离的机制会引入冗余和较高的资源开销。与流大小测量相比，流扩散测量在算法和系统层面提出了更大的挑战，因为它需要在严格的内存与计算约束下进行准确的不同元素计数，尤其是在数据平面中。本文提出 UniSketch，一个统一的流扩散测量框架，在单一框架内支持多种由扩散衍生的监测任务。UniSketch 建立在一种新颖的多虚拟二维位数组设计和一种轻量级的虚拟鞅估计器之上，能够以恒定的逐包处理开销对所有流进行高效的在线扩散估计。我们在可编程交换机上实现了 UniSketch，并给出理论分析，表明其估计是渐近无偏的且误差有界。在四个真实世界数据集上的实验结果表明，UniSketch 的准确度和 F1 分数显著高于先前方法，同时将最大处理吞吐提升最多 13.67×。

## 英文关键词
network measurement, flow spread measurement, sketch, programmable switch

## 中文关键词
网络测量，流扩散测量，草图，可编程交换机

[返回 Session 2](index.md) · [返回 ATC 2026](../index.md)
