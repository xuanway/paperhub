---
title: "Near-Zero-Overhead Freshness for Recommendation Systems via Inference-Side Model Updates"
description: "HPCA 2026 · Efficient Serving and Resource Management"
tags:
  - "HPCA2026"
  - "Efficient Serving and Resource Management"
---

# Near-Zero-Overhead Freshness for Recommendation Systems via Inference-Side Model Updates

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient Serving and Resource Management。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient Serving and Resource Management</p>
</div>

**论文链接**：
**作者**：Wenjun Yu Hong Kong Baptist University , Sitian Chen Hong Kong Baptist University , Amelie Chi Zhou Hong Kong Baptist University , Cheng Chen ByteDance, China
**会议**：HPCA 2026

---

## 中文标题

通过推理侧模型更新为推荐系统实现近零开销的新鲜度

## 英文摘要

Deep Learning Recommendation Models (DLRMs) underpin personalized services but face a critical freshness-accuracy tradeoff due to massive parameter synchronization overheads. Production DLRMs deploy decoupled training/inference clusters, where synchronizing petabyte-scale embedding tables (EMTs) causes multi-minute staleness, degrading recommendation quality and revenue. We observe that (1) inference nodes exhibit sustained CPU underutilization (peak ≤20%), and (2) EMT gradients possess intrinsic low-rank structure, enabling compact update representation. We present LiveUpdate, a system that eliminates inter-cluster synchronization by colocating Low-Rank Adaptation (LoRA) trainers within inference nodes. LiveUpdate addresses two core challenges: (1) dynamic rank adaptation via singular value monitoring to constrain memory overhead (<2% of EMTs), and (2) NUMA-aware resource scheduling with hardware-enforced QoS to eliminate update-inference contention (P99 latency impact <20ms). Evaluations show LiveUpdate reduces update costs by 2× versus delta-update baselines while achieving higher accuracy within 1-hour windows. By transforming idle inference resources into freshness engines, LiveUpdate delivers online model updates while outperforming state-of-the-art delta-update methods by 0.04–0.24% in accuracy.

## 中文摘要

深度学习推荐模型（DLRM）支撑着个性化服务，但因海量参数同步开销而面临严峻的新鲜度与精度之间的权衡。生产环境的 DLRM 采用训练与推理解耦的集群，同步 PB 级嵌入表（EMT）会造成数分钟的陈旧，降低推荐质量与收入。我们观察到：(1) 推理节点的 CPU 长期未被充分利用（峰值不超过 20%）；(2) EMT 梯度具有内在的低秩结构，因而可用紧凑方式表示更新。我们提出 LiveUpdate，该系统通过在推理节点内共置低秩适配（LoRA）训练器，消除跨集群同步。LiveUpdate 解决两个核心挑战：(1) 通过奇异值监测进行动态秩自适应，将内存开销限制在 EMT 的 2% 以内；(2) 采用 NUMA 感知的资源调度与硬件强制的 QoS，消除更新与推理之间的竞争（P99 时延影响小于 20 ms）。评估表明，与增量更新基线相比，LiveUpdate 将更新成本降低 2×，同时在 1 小时窗口内取得更高精度。通过把闲置的推理资源转化为新鲜度引擎，LiveUpdate 在实现在线模型更新的同时，精度比最先进的增量更新方法高 0.04%–0.24%。
