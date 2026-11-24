# CAVER: Enhancing RDMA Load Balancing by Hunting Less-Congested Paths

**中文标题**：CAVER：通过寻找拥塞更轻的路径增强 RDMA 负载均衡

**所属 Session**：[Session 8: Data Center Networking](index.md) · [ATC 2026](../index.md)

**作者**：Haotian Deng (Tsinghua University), Jue Zhang (Beihang University), Menghao Zhang (Beihang University), Yuan Yang (Tsinghua University), Xiao Li (Tsinghua University), Junhao Dong (Tsinghua University), Yi Liu (Tsinghua University), Mingwei Xu (Tsinghua University)

## 英文摘要
Load balancing (LB) is critical for reducing flow completion time (FCT) in RDMA networks where link congestion fluctuates rapidly. While many existing works have been devoted to improving LB performance in RDMA, they all select paths based on limited information, leaving a large number of available paths unexploited, which is prone to wasting the network bandwidth resources. In this paper, we aim to enhance existing works by optimizing the awareness of congestion status and propose CAVER, an RDMA-optimized LB framework. The key idea behind CAVER is to leverage ACK packets to establish a vector-protocol-like mechanism, enabling the efficient collection of real-time path congestion information and the selection of less-congested paths. We implement CAVER with NS3 and Tofino switches, and conduct simulations and real experiments. The results show that compared to state-of-the-art, CAVER improves average and 99th-percentile FCT by up to 46.0% and 32.2%, respectively.

## 中文摘要
在链路拥塞快速波动的 RDMA 网络中，负载均衡（LB）对于降低流完成时间（FCT）至关重要。尽管已有大量工作致力于提升 RDMA 中的 LB 性能，但它们都基于有限的信息选择路径，使大量可用路径未被利用，容易浪费网络带宽资源。本文旨在通过优化对拥塞状态的感知来增强已有工作，提出 CAVER，一个面向 RDMA 优化的 LB 框架。CAVER 的核心思想是利用 ACK 报文建立类矢量协议机制，从而高效收集实时的路径拥塞信息并选择拥塞更轻的路径。我们基于 NS3 和 Tofino 交换机实现了 CAVER，并开展了仿真与真实实验。结果表明，与现有最优方案相比，CAVER 将平均 FCT 和 99 分位 FCT 分别最多改善 46.0% 和 32.2%。

## 英文关键词
RDMA, load balancing, data center networks

## 中文关键词
RDMA，负载均衡，数据中心网络

[返回 Session 8](index.md) · [返回 ATC 2026](../index.md)
