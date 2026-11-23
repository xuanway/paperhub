---
title: "DCPerf: An Open-Source, Battle-Tested Performance Benchmark Suite for Datacenter Workloads"
description: "ISCA 2025 · Session 9A · DCPerf：经实战检验的开源数据中心负载性能基准套件"
tags:
  - "ISCA2025"
  - "Session 9A"
  - "Industry Track"
---

# DCPerf: An Open-Source, Battle-Tested Performance Benchmark Suite for Datacenter Workloads

**中文标题：** DCPerf：经实战检验的开源数据中心负载性能基准套件

**所属 Session：** [Session 9A](index.md) · [ISCA 2025](../index.md)

**作者：** Wei Su, Abhishek Dhanotia, Carlos Torres, Jayneel Gandhi, Neha Gholkar, Shobhit Kanaujia, Maxim Naumov, Kalyan Subramanian, Valentin Andrei, Yifan Yuan, Chunqiang Tang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731411) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

We present DCPerf, the first open-source performance benchmark suite actively used to inform procurement decisions for millions of CPU in hyperscale datacenters. Although numerous benchmarks exist, our evaluation reveals that they inaccurately project server performance for datacenter workloads or fail to scale to resemble production workloads on modern many-core servers. DCPerf dis- tinguishes itself in two aspects: (1) it faithfully models essential software architectures and features of datacenter applications, such as microservice architecture and highly optimized multi-process or multi-thread concurrency; and (2) it strives to align its performance characteristics with those of production workloads, at both the system level and microarchitecture level. Both are made possible by our direct access to the source code and hyperscale produc- tion deployments of datacenter workloads. Additionally, we share real-world examples of using DCPerf in critical decision-making, such as selecting future CPU SKUs and guiding CPU vendors in optimizing their designs. Our evaluation demonstrates that DCPerf accurately projects the performance of representative production workloads within a 3.3% error margin across four generations of production servers introduced over a span of six years, with core counts varying widely from 36 to 176.

## 中文摘要

本文介绍DCPerf，首款开源性能基准测试套件，目前已实际用于超大规模数据中心数百万颗CPU的采购选型评估。尽管已有大量基准测试程序，但评测发现：它们要么无法准确预测数据中心负载下的服务器性能，要么难以扩展，无法在现代多核服务器上复现线上业务负载特征。

DCPerf有两大核心特点：（1）忠实还原数据中心应用的关键软件架构与特性，例如微服务架构、高度优化的多进程/多线程并发模型；（2）在系统层面与微架构层面，让自身性能特征尽量对齐线上真实负载。这些能力得益于我们可以直接获取数据中心业务负载源码以及超大规模线上部署环境。

此外，本文给出DCPerf支撑关键决策的真实案例，例如遴选下一代CPU型号、指导CPU厂商优化芯片设计。实验结果表明：在跨度六年、四代商用服务器（核数范围36–176核）上，DCPerf对代表性线上负载的性能预测误差控制在3.3%以内。

## 英文关键词

Benchmarking, Cloud Computing, Performance

## 中文关键词

基准测试, 云计算, 性能

## 代码与研究制品

- [代码仓库](https://github.com/facebookresearch/DCPerf)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731411)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2025](../index.md)
