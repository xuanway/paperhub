---
title: "SpecEE: 利用推测早退加速LLM推理"
description: "ISCA 2025论文解读：SpecEE提出推测早退机制，通过预测LLM token何时可提前退出中间层，在不损失精度的前提下减少大量计算。"
tags: ["ISCA2025", "LLM推理", "Early Exit", "推测执行", "Fudan"]
---

# SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">SpecEE 利用推测性早退（Speculative Early Exiting）机制：轻量预测器判断每个 token 是否可在中间层退出，正确时跳过后续层，大幅降低平均层计算次数。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · LLM推理加速 · Early Exit · 推测执行 · Fudan University</p>
</div>

**作者**：Jiaming Xu, Jiayi Pan, Yongkang Zhou, Siming Chen, Jinhao Li, Yaoxiu Lian, Junyi Wu, Guohao Dai  
**机构**：Fudan University 等  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> 并非所有 token 都需要经过全部 Transformer 层；SpecEE 用轻量预测器推测可早退的 token，以推测正确时的计算节省换取整体吞吐量提升。

## 背景与动机

- **层计算冗余**：LLM 推理中，简单 token 的语义已在浅层收敛，继续执行深层是冗余计算
- **Early Exit 已有方案**：需在每层添加验证头，精度损失难控制
- **推测思路**：借鉴 Speculative Decoding，先推测早退，验证失败时回滚重算

## 主要贡献

1. **推测早退框架**：设计轻量预测器（小分类头）判断中间层输出是否满足退出条件
2. **投机验证机制**：退出后并行验证最终层结果一致性，不一致时回滚
3. **系统集成**：与 KV Cache 管理和 batch 调度集成，最大化吞吐量

## 实验结果

- Llama-2-7B/13B 在多种任务上平均加速 **1.4–2.0×**
- 精度损失 < 1%（与贪心解码基本相当）

## 关键词

LLM推理 · Early Exit · 推测解码 · Transformer加速 · ISCA 2025
