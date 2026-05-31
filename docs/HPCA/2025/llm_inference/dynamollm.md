---
title: "DynamoLLM: LLM推理集群性能与能效协同优化"
description: "HPCA 2025论文解读：DynamoLLM通过动态调整LLM推理集群的GPU频率、并行度和批次大小，在保证SLO（服务级目标）的前提下降低推理能耗。"
tags: ["HPCA2025", "LLM推理", "能效", "数据中心", "GPU调度", "UIUC", "Microsoft"]
---

# DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DynamoLLM 对 LLM 推理集群的能耗特性进行全面分析，发现 LLM 服务存在显著的请求率时间变化，提出动态配置推理集群（调整并行策略、GPU 频率、批次大小）的方法，在满足 P99 延迟 SLO 的前提下降低能耗 30%+。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · LLM推理 · 能效优化 · 数据中心 · 服务质量 · UIUC · Microsoft</p>
</div>

**作者**：Jovan Stojkovic, Chaojie Zhang, Íñigo Goiri, Josep Torrellas, Esha Choukse  
**机构**：University of Illinois at Urbana-Champaign; Microsoft  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> LLM 推理服务的请求负载在一天内变化超过 10×，但现有集群通常以最高负载为基准静态配置，在低谷期大量 GPU 闲置浪费能源；DynamoLLM 通过动态调配实现"随需而动"。

## 背景与动机

- **LLM 推理的能耗规模**：GPT-4 级别模型推理一次约消耗 0.001～0.01 kWh，全球每天数十亿次推理请求对应数百 MWh 级别的能耗
- **负载时间变化**：微软 Azure 生产数据显示，LLM API 请求率在一天内有 8～12× 的峰谷比，夜间低谷期大量 GPU 闲置
- **静态配置的浪费**：以满足 P99 延迟 SLO 为目标的静态配置，在低负载时 GPU 功耗几乎不降（GPU 空闲时功耗仍为峰值的 60%+）

## DynamoLLM 设计

### 推理集群配置空间

- **并行度**：Tensor Parallelism（TP）× Pipeline Parallelism（PP）
- **GPU 频率**：高频（1.4GHz）、中频（1.1GHz）、低频（0.85GHz）
- **批次大小**：连续批处理（Continuous Batching）的最大并发请求数

### 动态调配策略

1. **负载预测**：基于历史请求率时间序列预测未来 5 分钟的负载
2. **配置搜索**：在预测负载下遍历配置空间，找到满足 SLO 且能耗最低的配置
3. **渐进切换**：配置切换（如并行度变化）期间通过"金丝雀路由"平滑迁移请求

## 实验结果

| 指标 | 静态配置 | DynamoLLM | 改进 |
|------|---------|-----------|------|
| 平均能耗 | 基线 | 0.68× | 32% 节省 |
| P99 延迟 SLO 违反率 | 2.1% | 1.8% | 轻微改善 |
| GPU 利用率（低谷期） | 12% | 34% | 2.8× |

## 核心亮点

1. 将 LLM 推理能效问题建模为"满足 SLO 的最小能耗配置"问题，系统研究配置空间
2. 生产级验证：使用微软 Azure 真实 LLM 推理请求追踪评估
3. 开源配置优化框架，适用于多种 GPU 集群

## 局限性

- 配置切换本身需要时间（PP 并行度切换约需 30s），无法应对突发流量
- 能效收益主要来自低谷期，对于 24/7 高负载服务效果有限
