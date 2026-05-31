---
title: "AiF: 利用片内闪存处理实现端侧LLM推理加速"
description: "ISCA 2025论文解读：AiF提出利用移动设备片内闪存的计算能力辅助LLM推理，减少内存带宽压力，实现低功耗端侧LLM部署。"
tags: ["ISCA2025", "端侧LLM", "片内闪存", "In-Flash处理", "移动AI", "SNU"]
---

# AiF: Accelerating On-Device LLM Inference Using In-Flash Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">AiF 探索移动端 LLM 推理的新范式：将部分矩阵乘法计算卸载到闪存芯片内部处理单元（In-Flash Processing），减少主存/闪存之间的数据搬移，实现低延迟低功耗端侧 LLM 推理。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 端侧LLM · 闪存处理 · In-Storage Computing · 移动AI · SNU</p>
</div>

**作者**：Jaeyong Lee, Hyunjoo Kim, Sanghoon Oh, Myoungjun Chun, Myungsuk Kim, Jihong Kim  
**机构**：Seoul National University (SNU) 等  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> 移动端 LLM 推理受限于 DRAM 带宽和容量；AiF 将权重直接在闪存控制器旁的计算单元上处理，避免 DRAM 搬运瓶颈。

## 背景与动机

- **端侧推理内存瓶颈**：7B+ 参数模型无法完整载入移动端 DRAM，需从闪存反复加载权重，带宽严重不足
- **闪存带宽潜力**：现代 NVMe/UFS 闪存控制器有余量算力，可利用其执行部分计算
- **AiF 方案**：在闪存芯片内置轻量 MAC 阵列，推理时权重不搬出闪存，直接在闪存端参与计算

## 主要贡献

1. **In-Flash Processing 架构**：闪存控制器扩展 INT8 MAC 单元，支持矩阵-向量乘法
2. **计算卸载调度**：分析 Transformer 各层计算/访存比，自动决策哪些层适合 In-Flash 执行
3. **精度优化**：权重 INT8 量化存储，激活经闪存输出后完成累加

## 实验结果

- 与纯 DRAM 方案相比，token 生成延迟降低 **40%**
- 功耗降低 **30%**（减少闪存到 DRAM 的数据搬运）
- Llama-2-7B 在移动平台端到端可行

## 关键词

端侧LLM · 闪存处理 · 移动AI推理 · In-Storage Computing · ISCA 2025
