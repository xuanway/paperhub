---
title: "How Soon is Now? Preloading Images for Virtual Disks with ThinkAhead"
description: "FAST 2026 · Virtualization · 第 399–414 页"
tags:
  - "FAST2026"
  - "Virtualization"
---

# How Soon is Now? Preloading Images for Virtual Disks with ThinkAhead

**中文标题**：还要等多久？利用 ThinkAhead 为虚拟磁盘预加载镜像

**Session**：Virtualization · 2026-02-25 16:10–17:30 · Chair：Mai Zheng（Iowa State University）

**作者**：Xinqi Chen, Shanghai Jiao Tong University; Yu Zhang, Alibaba Group; Erci Xu, Shanghai Jiao Tong University; Changhong Wang, Jifei Yi, Qiuping Wang, Shizhuo Sun, and Zhongyu Wang, Alibaba Group; Haonan Wu, Shanghai Jiao Tong University; Junping Wu, Hailin Peng, Rong Liu, Yinhu Wang, Jiaji Zhu, and Jiesheng Wu, Alibaba Group; Guangtao Xue, Shanghai Jiao Tong University; Shanghai Key Laboratory of Trusted Data Circulation, Governance and Web3; Patrick P. C. Lee, The Chinese University of Hong Kong

**会议**：FAST 2026 · Santa Clara, CA · 第 399–414 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/chen](https://www.usenix.org/conference/fast26/presentation/chen)

**论文 PDF**：[fast26-chen.pdf](https://www.usenix.org/system/files/fast26-chen.pdf)

---

## 英文摘要

Efficient cloud computing relies on high-performance Elastic Block Storage (EBS) services, where virtual disk (VD) image loading significantly affects user experience. While the commonly used "lazy loading" approach reduces cold-start time from minutes to sub-seconds, our trace analysis of around 160,000 real-world image loading events in Alibaba EBS reveals that slow I/Os during initial block access constitute the primary performance bottleneck, accounting for 40% of all slow I/Os. We propose ThinkAhead, a data-driven image preloading system for VDs. ThinkAhead comprises various techniques to predict efficient block preloading sequences for images with historical traces based on runtime conditions and address corner cases with limited or no historical traces. Trace-driven simulation and cluster experiments show that ThinkAhead improves the data block hit rate by up to 7.27× and reduces tail waiting time by up to 98.7% across various image types compared to lazy loading and various baselines.

## 中文摘要

高效云计算依赖于高性能弹性块存储（EBS）服务，其中虚拟磁盘（VD）镜像加载会显著影响用户体验。虽然常用的“懒加载”方法将冷启动时间从数分钟缩短到亚秒级，但我们对阿里云 EBS 中约 16 万次真实镜像加载事件的跟踪分析表明，初始块访问期间的慢 I/O 构成了主要性能瓶颈，占所有慢 I/O 的 40%。我们提出 ThinkAhead，一个数据驱动的虚拟磁盘镜像预加载系统。ThinkAhead 包含多种技术，可基于运行时条件，利用历史跟踪数据为镜像预测高效的块预加载序列，并处理历史跟踪数据有限或缺失的边界情况。跟踪驱动的仿真和集群实验表明，与懒加载及多种基线相比，ThinkAhead 在各类镜像上将数据块命中率最高提升 7.27 倍，并将尾部等待时间最多减少 98.7%。
