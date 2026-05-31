---
title: "AQPIM: 利用存内激活量化突破LLM的PIM容量墙"
description: "HPCA 2026论文解读：AQPIM在PIM内部实现激活值量化，将LLM推理所需内存容量降低4×，使更大规模模型可在PIM上运行。"
tags: ["HPCA2026", "PIM", "量化", "LLM推理", "容量优化"]
---

# AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">AQPIM 将激活量化计算下沉到 PIM 内部执行，在不损失精度的前提下将 KV Cache 和中间激活内存占用降低 4×，使 PIM 能够支持更大规模的 LLM 推理。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · PIM · 激活量化 · LLM内存优化 · 容量墙</p>
</div>

**作者**：Kosuke Matsushima, Yasuyuki Okoshi, Masato Motomura, Daichi Fujiki  
**机构**：Institute of Science Tokyo  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> PIM 的容量限制（HBM-PIM 通常 ≤ 32GB）是制约其支持大型 LLM 的关键瓶颈；AQPIM 在 PIM 计算单元内直接执行激活量化，4× 压缩内存占用，使 70B 模型可在 PIM 上运行。

## 背景与动机

- **问题**：LLM 推理的 KV Cache 占用随上下文长度线性增长，PIM 的有限 HBM 容量（<32GB）无法支持大模型或长上下文推理。
- **现有方案的不足**：CPU 量化（如 GPTQ）在 PIM 计算前量化，需将量化逻辑实现在主机端，PIM 端仍需读取完整精度数据；混合精度推理框架与 PIM 架构适配困难。
- **本文思路**：在 PIM 的计算单元（Processing Element）内集成轻量级量化逻辑，数据以低精度形式存储和读取，在 PE 内部完成反量化后参与计算。

## 方法详解

### 核心思想

**存内量化（In-Memory Quantization）**：
1. KV Cache 以 INT4/INT8 格式存储在 PIM 的 DRAM Bank
2. PIM PE 内集成量化参数（缩放因子、零点）存储单元
3. PE 读取时原地执行 INT4→FP16 反量化，再与查询向量点乘

### 量化感知校准

针对 PIM 的特殊计算特性（内积运算为主），设计专用量化校准方法，在 INT4 精度下保持 99%+ 的精度。

## 实验结果

| 模型 | 内存容量需求降低 | 精度（vs. FP16） |
|------|--------------|----------------|
| LLaMA-2-7B | 3.8× | 99.6% |
| LLaMA-2-70B | 4.1× | 99.2% |
| Mistral-7B | 3.9× | 99.4% |

## 核心亮点

1. 首个在 PIM 架构内实现激活量化的系统
2. 量化和反量化完全在 PIM 内部完成，主机 CPU/GPU 无需参与
3. 使 70B 以上大模型在现有 PIM 硬件上成为可能

## 局限性

- PIM PE 面积增加约 8%（量化逻辑开销）
- INT4 量化在少量任务上精度损失超过 1%
