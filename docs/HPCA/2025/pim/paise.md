---
title: "PAISE: PIM加速Transformer LLM推理调度引擎"
description: "HPCA 2025论文解读：PAISE是三星SDS提出的PIM加速Transformer推理调度引擎，通过智能分配Attention与FFN操作到PIM和SoC，实现LLM推理的高效调度。"
tags: ["HPCA2025", "PIM", "LLM推理", "Transformer", "调度", "Samsung SDS"]
---

# PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PAISE 是三星 SDS 提出的 LLM 推理调度引擎，通过对 Transformer 各组件（Attention、FFN、Layer Norm）的计算特性分析，将访存密集操作卸载到 PIM，将计算密集操作保留在 SoC，并通过调度引擎动态优化执行顺序，实现 LLM 推理的整体加速。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · PIM · Transformer 推理 · 调度引擎 · Samsung SDS · 智能手机</p>
</div>

**作者**：Hyojung Lee, Daehyeon Baek, Jimyoung Son, Jieun Choi, Kihyo Moon, Minsung Jang  
**机构**：Samsung SDS  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> Transformer LLM 中不同操作（MHA Attention、FFN、LayerNorm）有截然不同的算术强度；PAISE 通过自动分析各操作的计算/访存特性，将其动态分配给 PIM 或 SoC，最大化资源利用率。

## 背景与动机

- **LLM 推理的多样性**：即使在同一 LLM（如 LLaMA-2-7B）内部，MHA 中的 KV-Cache 读取（算术强度 < 2）和 FFN 中的 GEMM（算术强度 > 50）有 25× 的差异
- **现有方案的局限**：要么全部在 CPU/GPU 上运行，要么简单地把所有 GeMV 都下推 PIM，忽略了调度的异构性
- **调度优化的空间**：不同 LLM 配置（模型大小、批次大小、序列长度）下，最优调度策略不同，需要运行时自适应

## PAISE 设计

### 操作分类引擎

对每个 Transformer 子操作（基于 batch size、seq length、hidden size）计算：
- **算术强度**（FLOP/Byte）
- **PIM 执行时间估算**
- **SoC 执行时间估算**
- **数据传输开销**

依据成本模型动态判断最优执行设备。

### 调度优化

- **流水线化**：将第 L 层 PIM 操作与第 L+1 层 SoC 操作流水线执行
- **批次自适应**：批次大小增加时，自动从 PIM 优先切换为 SoC 优先（因 GEMM 算术强度随批次增大）
- **内存感知**：根据 PIM DRAM 剩余带宽动态调整卸载比例

## 实验结果

（三星 Galaxy 旗舰级 SoC + LPDDR5-PIM 配置）

| 工作负载 | SoC-Only | PIM-All | PAISE | PAISE vs SoC-Only |
|---------|---------|---------|-------|-------------------|
| LLaMA-7B Decode (bs=1) | 基线 | 1.8× | 2.1× | 2.1× |
| LLaMA-13B Decode (bs=1) | 基线 | 2.3× | 2.7× | 2.7× |
| LLaMA-7B Prefill (bs=8) | 基线 | 0.7× | 1.1× | 1.1× |

## 核心亮点

1. 精细的 PIM/SoC 混合调度，超越简单"全卸载 PIM"策略
2. 调度决策基于分析模型而非穷举搜索，运行时开销极低
3. 针对三星商用移动 PIM 硬件设计，具备实际部署价值

## 局限性

- 成本模型依赖硬件特性参数，跨平台迁移需要重新标定
- 对 MoE（Mixture of Experts）等新型架构的调度支持有待扩展
