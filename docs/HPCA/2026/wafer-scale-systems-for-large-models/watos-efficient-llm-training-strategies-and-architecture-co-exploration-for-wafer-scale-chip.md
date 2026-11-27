---
title: "WATOS: Efficient LLM Training Strategies and Architecture Co-exploration for Wafer-scale Chip"
description: "HPCA 2026 · Wafer-Scale Systems for Large Models"
tags:
  - "HPCA2026"
  - "Wafer-Scale Systems for Large Models"
---

# WATOS: Efficient LLM Training Strategies and Architecture Co-exploration for Wafer-scale Chip

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Wafer-Scale Systems for Large Models。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Wafer-Scale Systems for Large Models</p>
</div>

**论文链接**：
**作者**：Huizheng Wang Tsinghua University , Zichuan Wang Tsinghua University , Hongbin Wang Tsinghua University , Jingxiang Hou Tsinghua University , Taiquan Wei Tsinghua University , Chao Li Shanghai Jiao Tong University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

WATOS：面向晶圆级芯片的高效 LLM 训练策略与架构协同探索

## 英文摘要

Training large language models (LLMs) imposes extreme demands on computation, memory capacity, and interconnect bandwidth, driven by their ever-increasing parameter scales and intensive data movement. Wafer-scale integration offers a promising solution by densely integrating multiple single-die chips with high-speed die-to-die (D2D) interconnects. However, the limited wafer area necessitates trade-offs among compute, memory, and communication resources. Fully harnessing the potential of wafer-scale integration while mitigating its architectural constraints is essential for maximizing LLM training performance. This imposes significant challenges for the co-optimization of architecture and training strategies. Unfortunately, existing approaches all fall short in addressing these challenges. To bridge the gap, we propose WATOS, a co-exploration framework for LLM training strategy and wafer-scale architecture. We first define a highly configurable hardware template designed to explore optimal architectural parameters for wafer-scale chips. Based on it, we capitalize on the high D2D bandwidth and fine-grained operation advantages inherent to wafer-scale chips to explore optimal parallelism and resource allocation strategies, effectively addressing the memory underutilization issues during LLM training. Compared to the state-of-the-art (SOTA) LLM training framework Megatron and Cerebras’ weight streaming wafer training strategy, WATOS can achieve an average overall throughput improvement of 2.74× and 1.53× across various LLM models, respectively. In addition, we leverage WATOS to reveal intriguing insights about wafer-scale architecture design with the training of LLM workloads.

## 中文摘要

大语言模型（LLM）不断增长的参数规模与密集数据搬移，使训练对计算、内存容量与互连带宽提出极高要求。晶圆级集成通过高速裸片间（D2D）互连密集集成多个单裸片芯片，提供了有前景的方案；但有限的晶圆面积使计算、内存与通信资源之间必须折中。充分发挥晶圆级集成的潜力并缓解其架构约束是最大化 LLM 训练性能的关键，这对架构与训练策略的协同优化提出了重大挑战，而现有方法均未能解决。为此，我们提出 WATOS，一个面向 LLM 训练策略与晶圆级架构的协同探索框架：先定义高度可配置的硬件模板以探索晶圆级芯片的最优架构参数，再利用其固有的高 D2D 带宽与细粒度操作优势，探索最优的并行与资源分配策略，有效解决 LLM 训练中的内存利用不足问题。相比最先进的 LLM 训练框架 Megatron 与 Cerebras 的权重流式晶圆训练策略，WATOS 在多种 LLM 模型上平均整体吞吐分别提升 2.74 倍与 1.53 倍。此外，我们借助 WATOS 在 LLM 训练负载中揭示了关于晶圆级架构设计的有趣洞见。
