---
title: "PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters"
description: "ISCA 2026 · Session 9D · PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters"
tags:
  - "ISCA2026"
  - "Session 9D"
  - "Sustainability and Energy Efficiency"
---

# PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters

**中文标题：** PowerGrad: 面向功耗受限 ML 推理集群的层次化功耗管理

**所属 Session：** [Session 9D](index.md) · [ISCA 2026](../index.md)

**作者：** Hyoungwook Nam, Raghavendra Pradyumna Pothukuchi, Alper Buyuktosunoglu, Aporva Amarnath, Pradip Bose, Josep Torrellas

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As machine learning (ML) workloads demand more power and datacenters integrate renewable energy, workloads have to deal with situations where power demands exceed supply. In such situations, intelligently allocating the power among the nodes is key to maximizing efficiency. However, this is hard to do for ML inference workloads, where system administrators cannot profile the workload ahead of time. To address this challenge, this paper proposes PowerGrad, a hierarchical power-management framework for power-limited ML inference clusters. The idea is to dynamically identify the performance gradient of each running workload, which characterizes the performance sensitivity of the workload to power changes. At runtime, a Gradient Estimator collects hardware measurements and uses them to estimate performance gradients. Then, to maximize efficiency, Local Controllers and Hierarchical Controllers re-distribute the power from low-gradient workloads to high-gradient ones within a node and across nodes, respectively. PowerGrad is especially effective for severely power-limited environments, where every node demands more power than its maximum allocation. While PowerGrad can be applied to a variety of compute architectures, it needs dynamic hardware performance counter information that is unavailable in GPUs and accelerators. Consequently, we demonstrate PowerGrad on two CPU clusters running popular ML inference workloads in power-limited setups. The results show that PowerGrad is both effective and easily retargetable across different architectures. In traditional dual-CPU nodes, PowerGrad reduces the average and tail latencies by a mean of 22.9% and 23.0%, respectively, relative to the strongest of a set of software-transparent baselines. In single-CPU nodes with ML acceleration support, PowerGrad reduces the average and tail latencies by a mean of 9.0% and respectively.

## 中文摘要

随着机器学习（ML）工作负载需要更多功耗，且数据中心整合可再生能源，工作负载不得不应对功耗需求超过供给的情形。在这种情况下，智能地在节点之间分配功耗是最大化效率的关键。然而，对于 ML 推理工作负载而言这很难做到，因为系统管理员无法提前对工作负载进行性能剖析。为应对这一挑战，本文提出 PowerGrad，一个面向功耗受限 ML 推理集群的层次化功耗管理框架。其思想是动态识别每个运行中工作负载的性能梯度，该梯度表征了工作负载对功耗变化的性能敏感性。在运行时，梯度估计器收集硬件测量值并利用它们估计性能梯度。然后，为最大化效率，局部控制器和层次化控制器分别在节点内和跨节点将功耗从低梯度工作负载重新分配给高梯度工作负载。PowerGrad 在严重功耗受限的环境中尤为有效，此时每个节点所需的功耗都超过其最大分配额度。虽然 PowerGrad 可应用于各种计算架构，但它需要 GPU 和加速器中不可用的动态硬件性能计数器信息。因此，我们在两个运行流行 ML 推理工作负载且处于功耗受限设置的 CPU 集群上演示了 PowerGrad。结果表明，PowerGrad 既有效又易于跨不同架构重新定向。在传统的双 CPU 节点中，相对于一组软件透明基线中最强者，PowerGrad 将平均延迟和尾部延迟分别平均降低了 22.9% 和 23.0%。在支持 ML 加速的单 CPU 节点中，PowerGrad 将平均延迟和尾部延迟分别平均降低了 9.0% 和 9.9%。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9D](index.md) · [返回 ISCA 2026](../index.md)
