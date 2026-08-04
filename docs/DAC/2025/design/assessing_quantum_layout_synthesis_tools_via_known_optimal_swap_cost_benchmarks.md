---
title: "Assessing Quantum Layout Synthesis Tools via Known Optimal-SWAP Cost Benchmarks"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Assessing Quantum Layout Synthesis Tools via Known Optimal-SWAP Cost Benchmarks


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.08839">https://arxiv.org/abs/2502.08839</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量子布局综合，基准测试，SWAP门，最优性</p>
</div>


---

## 研究概要
本文提出QUBIKOS基准集，是首个具备可证明最优SWAP门数量的量子布局评测电路。设计分节电路构造法生成带确定最优交换开销的量子线路，可量化各类QLS工具最优间隙。在四款主流量子硬件评测，最优间隙随芯片规模激增，还可用于定位路由算法缺陷。

## 背景和动机
1. 超导量子芯片物理比特拓扑受限，量子布局合成QLS需插入SWAP门，交换门数量直接影响线路保真度，最小化SWAP是核心优化目标。
2. 现有基准QUEKO无交换需求、QUEKNO仅近最优，无法精确衡量启发式QLS算法与理论最优的差距。
3. 精确QL求解器复杂度指数级，大规模线路不可用，缺少统一标准量化各类启发工具性能优劣。
4. 不同耦合拓扑、规模硬件下QLS算法性能差异巨大，缺乏可控、可验证标准电路用于公平对比。

## 相关工作
1. 精确QLS求解：OLSQ2等基于约束规划，能得到最优解但仅适用于小规模线路，无法用于大规模评测。
2. 启发式QLS算法：LightSABRE、t|ket⟩、QMAP、ML-QLS，速度快但无基准衡量与最优解的差距。
3. QUEKO基准：无SWAP需求，仅测试子图同构类映射策略，无法评估需要交换的真实线路。
4. QUEKNO基准：生成需交换的线路，但仅宣称近最优，无法精确计算最优间隙，评测可信度不足。

## 本文解决方案
### 1. 最优线路构造理论体系
构造无法匹配硬件子图的交互子图，通过BFS生成强制门依赖链，串行分割电路为独立分段，每段恰好需要1个最优SWAP，总最优交换数等于分段总数，配套四条引理证明最优性。
### 2. 可控基准生成流水线
按目标最优SWAP数量生成分段主干电路，可插入不增加交换开销的辅助门，灵活调整线路规模、比特交互复杂度，适配不同耦合硬件。
### 3. 标准化最优间隙评测指标
定义最优间隙=算法平均SWAP数/理论最优SWAP数，数值越接近1算法性能越好。
### 4. 算法缺陷定位能力
基于基准分段结构拆解路由决策，定位如LightSABRE前瞻代价函数缺陷，指导QLS算法迭代改进。

## 实验分析
1. 最优验证：使用OLSQ2精确求解器验证400条不同交换数QUBIKOS电路，全部匹配预设最优SWAP数量。
2. 多硬件评测：覆盖Aspen-4、Sycamore、Rochester、Eagle四款超导芯片；LightSABRE综合最优，Eagle架构下最优间隙高达233.97倍，t|ket⟩、QMAP差距更大。
3. 拓扑对比：同比特规模下Rochester稀疏拓扑最优间隙是Sycamore稠密网格的7倍。
4. 案例分析：定位LightSABRE前瞻代价缺陷，通过衰减权重修正前瞻窗口可显著缩减多余SWAP。

## 研究启发
1. 仅靠仿真、小规模精确解无法客观对比QLS，带可证明最优值的基准是领域评测刚需。
2. 量子芯片耦合稠密程度直接决定路由难度，稀疏拓扑下现有启发式算法性能退化严重。
3. 前瞻代价函数是SABRE类路由核心瓶颈，需对远期门施加衰减权重避免短视决策。
4. 基准不仅用于横向对比工具，还可拆解路由分段定位算法局部次优缺陷，辅助算法迭代。
5. 现有主流QLS工具与理论最优存在巨大差距，面向大规模NISQ芯片的布局算法仍有极大优化空间。