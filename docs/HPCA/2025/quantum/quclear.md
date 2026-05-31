---
title: "QuCLEAR: 量子电路Clifford门优化"
description: "HPCA 2025论文解读：QuCLEAR提出量子电路中Clifford门的提取与吸收算法，通过将Clifford门从电路中分离并在末尾合并，减少量子电路中的T门数量，降低容错量子计算的资源开销。"
tags: ["HPCA2025", "量子计算", "量子编译", "Clifford门", "T门优化", "容错量子计算", "ANL"]
---

# QuCLEAR: Clifford Extraction and Absorption for Quantum Circuit Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">QuCLEAR 通过系统地从量子电路中提取 Clifford 子电路并将其吸收到电路末尾，减少电路中的 T 门数量（T-count），从而降低容错量子计算中的魔法态蒸馏资源需求。在多个 benchmark 上 T-count 减少 20%～45%。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 量子编译 · Clifford 优化 · T-count 优化 · 容错量子计算 · Argonne National Laboratory</p>
</div>

**作者**：Ji Liu, Alvin Gonzales, Benchen Huang, Zain H Saleem, Paul Hovland  
**机构**：Argonne National Laboratory; University of Chicago  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 容错量子计算中，T 门（非 Clifford 门）的实现需要"魔法态蒸馏"，成本极高（每个 T 门约需 100～1000 个物理量子比特-周期）；QuCLEAR 通过 Clifford 门提取与重组减少 T-count，降低容错资源开销。

## 背景与动机

- **T 门的昂贵性**：在容错量子计算（基于表面码等 QEC 码）中，Clifford 门（H、CNOT、S 等）可以直接实现，但 T 门需要通过"魔法态蒸馏"（Magic State Distillation）来获取，每个 T 门约需数百到数千个额外量子比特
- **T-count 优化的重要性**：减少量子电路的 T-count 直接降低容错量子计算机的物理比特需求
- **现有方法的局限**：现有 T-count 优化（如 T-par、Tcount Optimizer）基于局部重写规则，难以发现全局优化机会

## QuCLEAR 算法

### Clifford 提取（Extraction Phase）

1. 分析量子电路的 DAG 结构，识别纯 Clifford 子电路
2. 将 Clifford 子电路从 T 门序列中提取出来，生成"纯化"的 T 门序列

### Clifford 吸收（Absorption Phase）

1. 将提取的 Clifford 子电路向电路末尾传播（通过 Clifford 对易变换规则）
2. 末尾的多个 Clifford 子电路合并，消除冗余的 Clifford-Clifford 相消

### 迭代优化

- 重复提取-吸收过程，直到 T-count 不再减少
- 每轮迭代后用现有局部规则（T-par）进行 T 门合并

## 实验结果

| Benchmark | 初始 T-count | QuCLEAR T-count | 减少比例 |
|-----------|------------|----------------|---------|
| ADDER_8 | 448 | 294 | 34.4% |
| QFT_16 | 448 | 328 | 26.8% |
| GF(2^8) MUL | 6632 | 4048 | 38.9% |
| Hubbard Model | 5120 | 2976 | 41.9% |

## 核心亮点

1. 全局优化方法，发现局部规则无法找到的 T-count 减少机会
2. 与现有 T-count 优化工具互补，可组合使用（先运行 QuCLEAR，再运行 T-par）
3. 算法复杂度为多项式时间，可处理实际规模电路

## 局限性

- 对某些特殊电路结构（如 QAOA 的角度优化层）效果有限
- Clifford 传播的等价变换规则集需要完整实现，否则可能遗漏优化机会
