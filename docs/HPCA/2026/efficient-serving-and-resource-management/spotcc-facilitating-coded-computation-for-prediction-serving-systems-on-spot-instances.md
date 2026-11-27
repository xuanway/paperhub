---
title: "SpotCC: Facilitating Coded Computation for Prediction Serving Systems on Spot Instances"
description: "HPCA 2026 · Efficient Serving and Resource Management"
tags:
  - "HPCA2026"
  - "Efficient Serving and Resource Management"
---

# SpotCC: Facilitating Coded Computation for Prediction Serving Systems on Spot Instances

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient Serving and Resource Management。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient Serving and Resource Management</p>
</div>

**论文链接**：
**作者**：Lin Wang , Yuchong Hu Huazhong University of Science and Technology , Ziling Duan Huazhong University of Science and Technology , Mingqi Li Huazhong University of Science and Technology , Chenxuan Yao Huazhong University of Science and Technology , feifanliu Huazhong University of Science and Technology , Xiaolu Li Huazhong University of Science and Technology , Leihua Qin Huazhong University of Science and Technology , Dan Feng Huazhong University of Science and Technology, China
**会议**：HPCA 2026

---

## 中文标题

SpotCC：为竞价实例上的预测服务系统提供编码计算支持

## 英文摘要

The growing adoption of prediction serving systems (PSSes) has made cost-saving deployment on preemptible spot instances crucial, yet frequent preemptions severely harm availability. While coded computation (CC) can keep availability cost-effectively by encoding original jobs into parity ones, its direct application to spot instances incurs prohibitive decoding overhead and tail latency under frequent preemptions. We identify two findings for optimization: (i) decoding asymmetry (only original job failures require decoding); (ii) preemption unevenness (variation in preemption rates across cloud regions). Leveraging these findings, we propose SpotCC, a new CC framework that strategically dispatches parity jobs to high-preemption (volatile) regions and original jobs to low-preemption (stable) regions. SpotCC designs locality-based and fine-grained volatility identification to reduce decoding operations and mitigate job congestion, respectively, and adaptively tunes configurations for decoding minimization. Experiments show that SpotCC improves P99 latency by 83.9% over state-of-the-arts, while maintaining ultra-low monetary costs.

## 中文摘要

预测服务系统（PSS）的广泛采用，使得在可抢占的竞价实例上进行低成本部署变得至关重要，但频繁的抢占严重损害可用性。编码计算（CC）通过将原始作业编码为冗余作业，能以经济的方式维持可用性，但其直接应用于竞价实例会在频繁抢占下带来难以承受的解码开销与尾时延。我们识别出两点优化发现：(i) 解码不对称性，即只有原始作业失败才需要解码；(ii) 抢占不均衡性，即不同云区域之间抢占率存在差异。基于这些发现，我们提出 SpotCC，一个新的 CC 框架，将冗余作业策略性地派发到高抢占（易变）区域，而将原始作业派发到低抢占（稳定）区域。SpotCC 分别设计了基于局部性的和细粒度的易变性识别方法，以减少解码操作并缓解作业拥塞，并自适应调整配置以最小化解码。实验表明，SpotCC 相较最先进方案将 P99 时延改善 83.9%，同时保持极低的货币成本。
