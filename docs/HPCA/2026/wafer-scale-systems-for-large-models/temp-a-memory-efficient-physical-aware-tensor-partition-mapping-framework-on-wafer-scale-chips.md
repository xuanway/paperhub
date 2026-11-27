---
title: "TEMP: A Memory Efficient Physical-aware Tensor Partition-Mapping Framework on Wafer-scale Chips"
description: "HPCA 2026 · Wafer-Scale Systems for Large Models"
tags:
  - "HPCA2026"
  - "Wafer-Scale Systems for Large Models"
---

# TEMP: A Memory Efficient Physical-aware Tensor Partition-Mapping Framework on Wafer-scale Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Wafer-Scale Systems for Large Models。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Wafer-Scale Systems for Large Models</p>
</div>

**论文链接**：
**作者**：Huizheng Wang Tsinghua University , Taiquan Wei Tsinghua University , Zichuan Wang Tsinghua University , Dingcheng Jiang Tsinghua University , Qize Yang Tsinghua University , Jiaxin Liu Tsinghua University , Jingxiang Hou Tsinghua University , Chao Li Shanghai Jiao Tong University , Jinyi Deng Tsinghua University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

TEMP：晶圆级芯片上内存高效的物理感知张量划分与映射框架

## 英文摘要

Large language models (LLMs) demand significant memory and computation resources. Wafer-scale chips (WSCs) provide high computation power and die-to-die (D2D) bandwidth but face a unique trade-off between on-chip memory and compute resources due to limited wafer area. Therefore, tensor parallelism strategies for wafer should leverage communication advantages while maintaining memory efficiency to maximize WSC performance. However, existing approaches fail to address these challenges. To address these challenges, we propose the tensor stream partition paradigm (TSPP), which reveals an opportunity to leverage WSCs’ abundant communication bandwidth to alleviate stringent on-chip memory constraints. However, the 2D mesh topology of WSCs lacks long-distance and flexible interconnects, leading to three challenges: 1) severe tail latency, 2) prohibitive D2D traffic contention, and 3) intractable search time for optimal design. We present TEMP, a framework for LLM training on WSCs that leverages topology-aware tensor-stream partition, traffic-conscious mapping, and dual-level wafer solving to overcome hardware constraints and parallelism challenges. These integrated approaches optimize memory efficiency and throughput, unlocking TSPP’s full potential on WSCs. Evaluations show TEMP achieves 1.7× average throughput improvement over state-of-the-art LLM training systems across various models.

## 中文摘要

大语言模型（LLM）需要大量内存与计算资源。晶圆级芯片（WSC）提供高算力与裸片间（D2D）带宽，但由于晶圆面积有限，在片上内存与计算资源之间存在独特的折中。因此，面向晶圆的张量并行策略应在保持内存效率的同时利用通信优势，以最大化 WSC 性能，然而现有方法未能应对这些挑战。为此，我们提出张量流划分范式（TSPP），它揭示了利用 WSC 充沛通信带宽来缓解严苛片上内存约束的机会。但 WSC 的二维网格拓扑缺乏长距离且灵活的互连，带来三方面挑战：1）严重的尾部时延，2）难以承受的 D2D 流量竞争，3）最优设计的搜索时间过长。我们提出 TEMP，一个面向 WSC 上 LLM 训练的框架，利用拓扑感知的张量流划分、流量感知映射与双层晶圆求解来克服硬件约束与并行化挑战。这些集成方法优化了内存效率与吞吐，释放了 TSPP 在 WSC 上的全部潜力。评估表明，在多种模型上，TEMP 相比最先进的 LLM 训练系统平均吞吐提升 1.7 倍。
