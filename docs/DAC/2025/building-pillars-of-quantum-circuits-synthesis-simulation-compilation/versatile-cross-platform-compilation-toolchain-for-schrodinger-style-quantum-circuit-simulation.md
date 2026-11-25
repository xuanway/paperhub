---
title: "Versatile Cross-platform Compilation Toolchain for Schrodinger-style Quantum Circuit Simulation"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Versatile Cross-platform Compilation Toolchain for Schrodinger-style Quantum Circuit Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.19894">https://arxiv.org/abs/2503.19894</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量子电路模拟，跨平台编译工具链，稀疏感知门融合，动态内核生成</p>
</div>


---

## 研究概要
本文提出CAST跨平台薛定谔量子仿真编译工具链，设计稀疏感知自适应门融合与动态内核生成。基于CircuitTile电路中间结构，依托代价模型适配CPU/GPU，生成LLVM IR与PTX底层代码。32qubit CPU、30qubit GPU基准测试，相较Qiskit、cuQuantum分别最高提速8.03倍、39.3倍，稀疏电路增益尤为显著。

## 背景和动机
1. 现有量子硬件可用性差，依赖经典计算机仿真验证量子算法，但态向量仿真指数级时空开销巨大。
2. 主流仿真工具门融合策略单一，未利用量子门稀疏性，稠密预编译内核冗余运算多。
3. 现有仿真后端平台兼容性差，CPU仅支持部分SIMD、GPU依赖第三方库，无法统一跨平台编译优化。
4. 固定预生成内核无法适配任意融合门，手工编写内核开发成本极高，稀疏门加速能力缺失。

## 相关工作
1. Qiskit/Qulacs/QPanda：仅支持固定尺寸门融合，忽略矩阵稀疏，CPU SIMD支持有限，GPU绑定cuQuantum库。
2. QSimCirq：仅适配AVX系列CPU，融合上限6量子比特，无自适应调度，稀疏场景性能衰减。
3. Qibo：采用JIT引擎但融合策略简单，稀疏门无专门优化，跨硬件适配性弱。
4. CUDA Quantum：GPU后端固定内核生成，无法动态适配各类融合门，对稀疏电路优化不足。

## 本文解决方案
### 1 CircuitTile自定义电路中间结构
采用分块链表存储门单元，区分同行可交换门、跨层连通门，支持门移动重组，为聚合式融合提供数据基础。
### 2 稀疏感知自适应聚合门融合
分可交换/连续两类融合；逐步提升融合最大比特数，基于软硬件代价模型统计运算量，自动判定最优融合阈值，区分稠密/稀疏电路调度策略。
### 3 跨平台动态内核生成
CPU端输出LLVM IR原生支持SSE/AVX2/AVX512/NEON；GPU生成PTX代码，自动跳过矩阵零元，无需手工预编译海量专用内核。
### 4 JIT/静态双编译模式
CPU支持ORC即时编译与IR持久静态编译；GPU运行时加载PTX，编译开销随量子比特规模快速摊薄。

## 实验分析
1. 测试基准：QFT/ALA/RQC/IQP/HES等稠密、稀疏量子电路，硬件覆盖AMD/Intel CPU、RTX3090 GPU。
2. 融合消融：仅尺寸融合CPU提速68.7%~93.3%，自适应融合在稀疏电路再降28.7%~40.4%运行耗时。
3. 平台性能：32qubit CPU相比Qiskit最高8.03倍加速；30qubit GPU相较cuQuantum最高提速39.3倍。
4. 编译开销：32qubit场景自适应融合前端耗时仅占总仿真3.11%，大规模电路摊薄明显。
5. 单门基准：稀疏Pauli类门吞吐量远超竞品，稠密两/三量子门与最优工具性能持平。

## 研究启发
1. 量子仿真优化核心在于挖掘门稀疏性，固定尺寸融合无法适配多样化电路，自适应代价模型是关键。
2. 统一中间表示+动态代码生成可摆脱手工内核开发，一套编译流程兼容CPU/GPU多架构。
3. 电路数据结构需适配量子门交换特性，通过门移位创造更多融合机会，减少独立运算块。
4. 稀疏量子电路收益远高于稠密电路，面向VQA、哈密顿演化等场景优势突出。
5. 编译阶段少量开销可换取仿真数十倍提速，前端优化具备极高性价比。