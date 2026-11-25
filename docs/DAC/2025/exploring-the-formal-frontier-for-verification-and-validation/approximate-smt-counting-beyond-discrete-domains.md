---
title: "Approximate SMT Counting Beyond Discrete Domains"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Approximate SMT Counting Beyond Discrete Domains

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arijitsh.github.io/assets/pdf/DAC25-count-beyond-discrete.pdf">https://arijitsh.github.io/assets/pdf/DAC25-count-beyond-discrete.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 近似SMT计数，混合SMT公式，哈希函数，投影计数 </p>
</div>

---

## 研究概要
本文提出pact混合SMT近似模型计数工具，支持离散+连续变量混合公式，基于哈希分块实现带(ε,δ)理论保证的投影计数。设计三类成对独立哈希，采用对数级SMT调用策略。在14202组SMT基准上，pact求解603例，基线仅13例，最大可计数1.7×10¹9组解，平均相对误差仅3.3%。

## 背景和动机
1. 现有SMT计数工具仅支持位向量、整数等纯离散理论，无法处理含实数、浮点的混合SMT公式，难以适配CPS、软件定量验证场景。
2. 枚举式基线计数随解数量增长算力爆炸，上限仅三千余组解，无法处理大规模解空间实例。
3. 传统哈希计数框架仅面向布尔/纯位向量，未适配连续变量与混合理论的约束求解。
4. 混合SMT广泛用于自动驾驶鲁棒分析、信息流量化等任务，但缺少高效带理论误差保证的投影计数方案。
5. 不同哈希函数在SMT求解中存在算力、精度权衡，缺乏系统对比与适配调度策略。

## 相关工作
1. 纯离散SMT计数：基于位爆破、线性整数分解，仅支持无连续变量公式，无法处理浮点/实数算术。
2. 加权模型积分(WMI)：面向连续域体积计算，不支持离散变量投影计数需求。
3. 布尔/位向量近似计数(ApproxMC等)：哈希框架成熟，但不能兼容实数、浮点混合理论约束。
4. 枚举式精确计数基线：逐个阻塞解遍历，解量稍大即超时，无工程实用价值。
5. 专用SMT求解器(CVC5/Boolector)：仅判断可满足性，不具备量化计数能力。

## 本文解决方案
### 1 混合SMT投影计数完整框架
以CVC5为底层求解器，支持QF_BVFP、QF_ABVFPLRA等多混合理论，目标统计位向量离散变量投影解集规模，提供(ε,δ)概率误差保证。
### 2 三类成对独立哈希族
H_xor按位异或、H_shift移位乘、H_prime模素数哈希；分别适配不同位宽与求解开销，自动切分宽位向量为哈希适配子段。
### 3 对数级SMT调用迭代算法
二分跳跃搜索哈希分层索引，饱和计数器逐次枚举并阻塞解；多次哈希采样取中位数作为最终估计，SMT调用量仅O(log|S|)。
### 4 自适应哈希分层修正策略
若哈希分块解数超阈值，自动缩小哈希区间重新划分；XOR哈希可跳过修正步骤，减少SMT迭代开销。
### 5 增量SMT查询优化
复用前序约束上下文，增量追加哈希条件，大幅降低单轮求解耗时，适配大规模混合公式。

## 实验分析
1. 实验环境：Xeon集群，单核心8GB内存，超时3600s，14202份SMT-Lib多混合理论基准，对比枚举基线与三种哈希配置pact。
2. 求解规模：基线仅完成13例，pact_xor可求解603例，最高支持1.7×10¹9个解，基线上限仅3570。
3. 精度表现：pact_xor平均相对误差3.3%，最大误差26%，远低于理论0.8上界；shift/prime平均误差更高。
4. 哈希对比：XOR哈希求解速度最优，SMT推理负担更低；shift/prime哈希约束复杂，可求解实例数量显著更少。
5. 耗时曲线：基线随实例数量耗时急剧飙升，pact_xor增长平缓，大规模实例优势极其明显。

## 研究启发
1. 传统离散SMT计数方法无法迁移至含实数/浮点混合公式，需设计适配连续域约束的哈希计数框架。
2. 按位XOR哈希轻量化优势突出，依托SAT原生异或推理可大幅降低SMT求解开销，是混合场景首选。
3. 分层哈希分块+中位数采样可严格控制近似误差，以对数级求解代价换取完整解集规模估计。
4. 枚举式精确计数不具备工程可用性，带概率保证近似计数是CPS、信息流量化等任务唯一可行方案。
5. 底层SMT求解器增量查询能力对哈希迭代效率至关重要，框架设计需深度复用求解上下文。