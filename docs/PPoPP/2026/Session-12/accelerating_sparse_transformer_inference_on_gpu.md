---
title: "Accelerating Sparse Transformer Inference on GPU"
description: "PPoPP 2026 Session 12（Optimizing Transformers）：稀疏 Transformer 行/块核 + 两阶段融合搜索，MHA 6×、端到端 1.4×"
tags:
  - "PPoPP2026"
  - "Session-12"
  - "Optimizing Transformers"
  - "Sparse Transformer"
  - "Operator Fusion"
  - "GPU"
authors:
  - "Wenhao Dai"
  - "Haodong Deng"
  - "Mengfei Rong"
  - "Xinyu Yang"
  - "Hongyu Liu"
  - "Fangxin Liu"
  - "Hailong Yang"
  - "Qianwen Cao"
  - "Qingxiao Sun"
session: "Session 12: Optimizing Transformers"
session_number: 12
session_chair: "Shaoshuai Zhang"
date: "2026-02-03"
time: "17:35–17:55"
room: "Pyrmont"
doi: "10.1145/3774934.3786434"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Accelerating Sparse Transformer Inference on GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 STOF 框架，按解析建模为稀疏 MHA 选择行式或块式核与存储格式，并将下游算子融合映射为编译模板做两阶段搜索，MHA 提速 6×、端到端推理 1.4×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 12: Optimizing Transformers</p>
</div>

**作者**：Wenhao Dai, Haodong Deng, Mengfei Rong, Xinyu Yang, Hongyu Liu, Fangxin Liu, Hailong Yang, Qianwen Cao, and Qingxiao Sun — China University of Petroleum-Beijing, China; Beihang University, China; Baidu, China; Shanghai Jiao Tong University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 17:35–17:55 · Session 12: Optimizing Transformers（主席：Shaoshuai Zhang）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786434) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Large language models (LLMs) are popular around the world due to their powerful understanding capabilities. As the core component of LLMs, accelerating Transformer through parallelization has gradually become a hot research topic. Mask layers introduce sparsity into Transformer to reduce calculations. However, previous works rarely focus on the performance optimization of sparse Transformer. In addition, current static operator fusion schemes fail to adapt to diverse application scenarios. To address the above problems, we propose STOF, a framework that incorporates optimizations for Sparse Transformer that enables flexible masking and Operator Fusion on GPU. For multi-head attention (MHA) structure, STOF maps the computation to row-wise or blockwise kernels with unique storage formats according to analytical modeling. For downstream operators, STOF maps the fusion scheme to compilation templates and determines the optimal running configuration through two-stage searching, achieving 6× in MHA computation and 1.4× in end-to-end inference.

## 中文摘要

大语言模型（LLMs）凭借其强大的理解能力在世界范围内广受欢迎。作为 LLMs 的核心组件，通过并行化加速 Transformer 已逐渐成为研究热点。掩码层为 Transformer 引入稀疏性以减少计算量。然而，已有工作很少关注稀疏 Transformer 的性能优化。此外，当前的静态算子融合方案难以适应多样化的应用场景。针对上述问题，我们提出 STOF，一个面向稀疏 Transformer 的优化框架，可在 GPU 上实现灵活的掩码与算子融合。对于多头注意力（MHA）结构，STOF 根据解析建模将计算映射到具有独特存储格式的行式或块式核函数。对于下游算子，STOF 将融合方案映射到编译模板，并通过两阶段搜索确定最优运行配置。在 MHA 计算上取得 6×、在端到端推理上取得 1.4× 的加速。

## 英文关键词

GPU, Sparse Transformer, Multi-head Attention, Operator Fusion

## 中文关键词

GPU；稀疏 Transformer；多头注意力；算子融合

---

## 一句话总结

> 提出 STOF 框架，按解析建模为稀疏 MHA 选择行式或块式核与存储格式，并将下游算子融合映射为编译模板做两阶段搜索，MHA 提速 6×、端到端推理 1.4×。

## 研究问题

掩码层为 Transformer 引入稀疏性以减少计算，但已有工作很少关注稀疏 Transformer 的性能优化；同时现有静态算子融合方案无法适应多样的应用场景。

## 方法简述

- 提出 STOF 框架，在 GPU 上同时支持灵活掩码与算子融合，面向稀疏 Transformer 推理做优化。
- 针对多头注意力（MHA）结构，依据解析建模把计算映射为行式（row-wise）或块式（blockwise）核，并配套专用存储格式。
- 对下游算子，把融合方案映射为编译模板，并通过两阶段搜索确定最优运行配置。

## 主要结果

- 在 MHA 计算上取得 6× 加速。
- 在端到端推理上取得 1.4× 加速。

---

> 所属 Session：[Session 12: Optimizing Transformers](index.md) · 返回 [PPoPP 2026 总览](../index.md)
