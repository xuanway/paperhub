---
title: "Predicting DRAM-Caused Risky VMs in Large-Scale Clouds"
description: "HPCA 2025 · Industry Session"
tags:
  - "HPCA2025"
  - "Industry Session"
---

# Predicting DRAM-Caused Risky VMs in Large-Scale Clouds

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Industry Session。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Industry Session</p>
</div>

**论文链接**：
**作者**：Yaoguang Yong (Shanghai Jiao Tong University), Xiaoming Du (Alibaba Cloud), Xuhua Ma (Alibaba Cloud), Yuxiang Wang (Alibaba Cloud), Bin Yao (Shanghai Jiao Tong University), Xudong Zheng (Alibaba Cloud), Huite Yi (Alibaba Cloud)
**会议**：HPCA 2025

---

## 中文标题

预测大规模云中由 DRAM 引发的风险虚拟机

## 英文摘要

DRAM failures are one of the leading failures in large-scale clouds. Previous studies focus on predicting DRAM uncorrectable errors (UEs) and mitigating the impact of DRAM failures through node-level workload migration and proactive dual in-line memory module (DIMM) replacement. For cloud systems, node migration means migrating all virtual machines (VMs) to other nodes. Such a coarse-grained migration consumes considerable resources. Inspired by the observation that DRAM errors tend to cluster in space, this paper proposes Pegasus, the first VM-level solution to mitigate DRAM failures. The key idea of Pegasus is to use the VM as the basic unit for predicting DRAM failures instead of the whole node. Specifically, we introduce a new concept of DRAM-caused risky VMs, which causes node unavailability when accessed. We design a novel Error-VM mapping framework deployed on a large-scale cloud. Statistical results confirm that DRAM errors are concentrated in the address space managed by a small number of VMs. By combining ECC and spatio-temporal features, our predictor achieves decent performance. Pegasus has been deployed online on over 300,000 nodes in the production cloud. The comparative study shows that the prediction performance of Pegasus is comparable to node-level solutions. Meanwhile, our approach offers over 70% lower costs and avoids more than 10% of VM crashes compared to node-level mitigation.

## 中文摘要

DRAM 故障是大规模云中的主要故障之一。已有研究侧重于预测 DRAM 不可纠正错误（UE），并通过节点级负载迁移与主动替换双列直插内存模块（DIMM）来缓解 DRAM 故障的影响。对于云系统，节点迁移意味着将所有虚拟机（VM）迁移到其他节点。这种粗粒度迁移会消耗大量资源。受 DRAM 错误倾向于在空间上聚集这一观察的启发，本文提出 Pegasus，首个虚拟机级缓解 DRAM 故障的方案。Pegasus 的核心思想是以 VM 而非整个节点作为预测 DRAM 故障的基本单元。具体而言，我们引入了“DRAM 引发的风险虚拟机”这一新概念，即被访问时会导致节点不可用的虚拟机。我们设计了一个新颖的错误—虚拟机映射框架，并将其部署在大规模云上。统计结果证实，DRAM 错误集中在少数 VM 所管理的地址空间中。通过结合 ECC 与时空特征，我们的预测器取得了良好的性能。Pegasus 已在生产云的 30 多万个节点上在线部署。对比研究表明，Pegasus 的预测性能与节点级方案相当。同时，与节点级缓解相比，我们的方法成本降低超过 70%，并避免了超过 10% 的 VM 崩溃。
