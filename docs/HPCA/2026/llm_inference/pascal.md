---
title: "PASCAL: 面向推理型LLM服务的阶段感知调度算法"
description: "HPCA 2026论文解读：PASCAL针对DeepSeek-R1等推理型LLM的思考与回答两阶段特性，设计专用调度算法提升服务效率。"
tags: ["HPCA2026", "LLM推理", "推理型LLM", "调度", "KAIST"]
---

# PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">推理型 LLM（如 DeepSeek-R1、o3）具有明显的"思考阶段"和"回答阶段"二元特性，PASCAL 利用此特性设计阶段感知调度，GPU 利用率提升 1.6×，TTFT 降低 35%。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 推理型LLM · 服务调度 · Test-Time Scaling · 体系结构</p>
</div>

**作者**：Eunyeong Cho, Jehyeon Bang, Ranggi Hwang, Minsoo Rhu  
**机构**：KAIST, UNIST  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 推理型 LLM 的"思考（Thinking）"和"回答（Response）"阶段在计算特征上有本质差异，PASCAL 通过阶段识别和差异化调度大幅提升服务效率。

## 背景与动机

- **问题**：以 DeepSeek-R1、QwQ、o1 为代表的推理型 LLM 通过长链思考（Chain-of-Thought）提升能力，但思考阶段极长（数千 token），传统调度策略将其与普通 LLM 同等处理，导致资源浪费和队列阻塞。
- **现有方案的不足**：vLLM/TGI 的 continuous batching 策略不感知推理阶段，思考阶段的超长序列占据大量 KV Cache，挤占其他请求。
- **本文思路**：检测推理阶段边界（`<think>` / `</think>` token），对两个阶段采用不同的批调度策略。

## 方法详解

### 核心思想

**阶段感知调度**：
- **思考阶段**：内存密集型，优先最大化 KV Cache 复用，减少换页
- **回答阶段**：输出密集型，优先降低延迟，增加批次并发度

### 关键机制

1. **相位检测器**：实时监控生成的 token，识别 `<think>` 标记边界
2. **阶段隔离队列**：思考阶段和回答阶段请求进入不同调度队列
3. **动态资源重分配**：根据各队列积压情况动态调整 KV Cache 配额

## 实验结果

| 指标 | vs. vLLM | vs. DejaVu |
|------|----------|------------|
| 吞吐量 | +1.6× | +1.3× |
| TTFT (首token延迟) | -35% | -22% |
| P99 延迟 | -41% | -28% |

## 核心亮点

1. 首个专门为推理型 LLM 设计的服务调度系统
2. 无需修改模型，零侵入性集成
3. 随推理型 LLM 占比增加，优势更加显著

## 局限性

- 对不使用 `<think>` 标记的推理模型需重新适配
- 阶段边界检测增加微小的控制路径开销
