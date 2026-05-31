---
title: "FACIL: SoC-PIM协同On-device LLM推理"
description: "HPCA 2025论文解读：FACIL提出灵活的DRAM地址映射方案，使移动SoC与DRAM-PIM协同完成on-device LLM推理，在有限内存带宽下实现50B参数LLM的本地推理。"
tags: ["HPCA2025", "PIM", "LLM推理", "SoC", "DRAM", "On-device AI", "首尔大学"]
---

# FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">FACIL 通过灵活的 DRAM 地址映射，使移动端 SoC（如 Apple M 系列）与 PIM-enabled DRAM 协同执行 LLM 推理，自适应分配 Prefill 和 Decode 阶段的计算资源，实现 50B 参数 LLM 在消费级设备上的实时推理。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · PIM · On-device LLM · SoC-PIM · DRAM · 首尔大学</p>
</div>

**作者**：Seong Hoon Seo, Junghoon Kim, Donghyun Lee, Seonah Yoo, Seokwon Moon, Yeonhong Park, Jae W. Lee  
**机构**：Seoul National University; Samsung Electronics; POSTECH; Hanyang University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 移动 SoC 的内存带宽是 LLM Decode 阶段的主要瓶颈；FACIL 通过灵活地址映射让 SoC GPU 和 DRAM-PIM 单元同时处理不同的 LLM 层，突破带宽限制，使 50B 模型的 Decode 吞吐提升 2.3×。

## 背景与动机

- **On-device LLM 的内存压力**：50B 参数模型需要约 25GB 内存（FP16），超出大多数手机内存容量，需要量化（INT4 约 6.25GB）才能运行
- **带宽瓶颈**：Decode 阶段的 KV-Cache 访问每 Token 需要读取全部 KV Cache，访存密集，移动 SoC 的 LPDDR5 带宽（约 100 GB/s）成为瓶颈
- **PIM 的机会**：DRAM-PIM（如三星 HBM-PIM）将计算单元集成到 DRAM 内部，片内带宽可达 DRAM 的 4×+

## FACIL 设计

### 灵活地址映射

- 将 LLM 的权重矩阵和 KV Cache 按"SoC 可访问 Bank"和"PIM 可计算 Bank"两类分区存放
- 地址映射可动态调整，根据工作负载特性（Prefill vs Decode）重分配分区比例

### 双阶段协同调度

**Prefill 阶段**（计算密集）：
- SoC GPU 主导计算，PIM 辅助处理 Attention KV 写入
- 地址映射偏向 SoC-accessible 区域

**Decode 阶段**（访存密集）：
- PIM 主导 KV Cache Attention 计算，SoC 处理 FFN 部分
- 地址映射偏向 PIM-computable 区域

### 模型分区策略

- 深层网络（Transformer 32 层）按奇偶层分别映射到 SoC 分区和 PIM 分区
- 流水线化执行，SoC 和 PIM 同时处理相邻层

## 实验结果

| 指标 | SoC-Only | FACIL | 提升 |
|------|---------|-------|------|
| Decode Token 吞吐 (50B, INT4) | 8.3 tok/s | 19.1 tok/s | 2.3× |
| 内存带宽利用率 | 67% | 91% | — |
| Prefill 延迟 | 基线 | 0.89× | 1.12× |

## 核心亮点

1. 将 50B 参数 LLM 的实时推理带到移动设备，Decode 吞吐满足实时对话需求
2. 地址映射动态调整机制，适应 LLM 两阶段不同特性
3. 与三星 HBM-PIM 和 LPDDR-PIM 硬件兼容

## 局限性

- 地址映射重分区操作本身有延迟，频繁切换（如短文本推理）收益降低
- 依赖 PIM-enabled DRAM 商用化，当前仅三星等少数厂商支持
