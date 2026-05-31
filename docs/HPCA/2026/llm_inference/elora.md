---
title: "ELORA: 多LoRA LLM服务中高效LoRA与KV Cache协同管理"
description: "HPCA 2026论文解读：ELORA解决多LoRA模型并行服务中LoRA权重和KV Cache的双重内存压力，提升GPU利用率。"
tags: ["HPCA2026", "LLM推理", "LoRA", "KV Cache", "LLM服务", "SJTU"]
---

# ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ELORA 通过联合调度 LoRA 权重和 KV Cache，解决多 LoRA 适配器同时服务时的内存争用问题，GPU 利用率提升 1.8×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM服务 · LoRA管理 · KV Cache · 内存优化</p>
</div>

**作者**：Jiuchen Shi, Hang Zhang, Yixiao Wang, Quan Chen, Yizhou Shan, Kaihua Fu, Wei Wang, Minyi Guo  
**机构**：Shanghai Jiao Tong University, The Hong Kong Polytechnic University, Huawei Cloud  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 在多 LoRA 服务场景中，LoRA 权重与 KV Cache 共用 GPU 内存并相互竞争，ELORA 通过联合管理两者实现内存最优分配，吞吐量提升 1.8×。

## 背景与动机

- **问题**：企业同时为成千上百个客户部署各自微调的 LoRA 模型，GPU 内存需同时容纳 LoRA 权重（数百 MB）和 KV Cache（动态增长），两者竞争激烈。
- **现有方案的不足**：现有系统（如 vLLM）将 LoRA 权重和 KV Cache 独立管理，无法感知两者的协同影响，导致频繁换页降低 GPU 利用率。
- **本文思路**：将 LoRA 权重视为"特殊的 KV Cache"，在统一内存池中联合调度，根据请求负载动态调整两类对象的内存配额。

## 方法详解

### 核心思想

**联合内存管理**：ELORA 建立统一内存池，将 LoRA 权重按"热度"分层缓存（Hot/Warm/Cold），与 KV Cache 的 PagedAttention 机制协同工作。

### 关键模块

1. **LoRA 热度感知器**：基于请求历史预测各 LoRA 的访问频率
2. **联合置换策略**：综合考虑 LoRA 大小、访问频率和 KV Cache 缺失代价
3. **预加载调度器**：在请求等待GPU空闲时预取即将使用的 LoRA 权重

## 实验结果

| 工作负载 | vs. vLLM吞吐量 | P99延迟改善 |
|----------|---------------|------------|
| 均匀LoRA分布 | 1.8× | 42% |
| 热点LoRA | 2.1× | 55% |
| 混合请求 | 1.6× | 38% |

## 核心亮点

1. 首个将 LoRA 权重与 KV Cache 联合管理的系统
2. 无需修改 LoRA 适配器或模型结构
3. 与 vLLM、SGLang 等主流框架兼容

## 局限性

- 预加载策略在请求分布突变时有冷启动问题
- 对超大量 LoRA（>1000个）的管理开销需进一步优化
