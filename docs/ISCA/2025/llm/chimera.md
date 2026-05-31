---
title: "Chimera: 大语言模型混合并行通信融合"
description: "ISCA 2025论文解读：Chimera提出在LLM混合并行训练/推理中融合通信操作，消除TP/PP/DP并行之间的通信气泡，提升硬件利用率。"
tags: ["ISCA2025", "LLM并行", "通信优化", "混合并行", "分布式推理"]
---

# Chimera: Communication Fusion for Hybrid Parallelism in Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Chimera 识别 LLM 张量并行（TP）、流水线并行（PP）、数据并行（DP）混合场景中的通信冗余，通过通信算子融合消除 bubble 并降低端到端延迟。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · LLM混合并行 · 通信融合 · 分布式推理 · Tensor并行</p>
</div>

**作者**：Le Qin, Junwei Cui, Weilin Cai, Jiayi Huang  
**机构**：多家机构  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> 混合并行 LLM 中，TP/PP/DP 的通信算子可被融合以消除冗余传输和等待气泡；Chimera 系统化地实现通信融合，提升大规模 LLM 集群效率。

## 背景与动机

- **混合并行现状**：大型 LLM 通常同时使用 TP+PP+DP 三种并行，各维度通信独立执行、互相等待，产生大量气泡
- **通信分析**：AllReduce、AllGather、P2P 等算子间存在数据依赖，但也存在可重叠窗口
- **本文方案**：构建通信依赖图，自动识别可融合/重叠的通信对，生成最优通信计划

## 主要贡献

1. **通信依赖图分析**：对混合并行 LLM 的通信进行形式化建模
2. **算子融合策略**：TP AllReduce 与 DP AllReduce 的融合；PP P2P 与 TP AllReduce 的重叠
3. **运行时调度器**：动态调整通信时序，最大化计算/通信重叠

## 实验结果

- 在 8-64 GPU 集群上，端到端吞吐量提升 **1.2–1.5×**
- 通信 bubble 率从 >20% 降低至 <8%

## 关键词

混合并行 · 通信融合 · 张量并行 · LLM分布式推理 · ISCA 2025
