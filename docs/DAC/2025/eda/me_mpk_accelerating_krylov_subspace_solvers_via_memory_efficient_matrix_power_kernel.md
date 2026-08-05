---
title: "Me-MPK: Accelerating Krylov Subspace Solvers via Memory-efficient Matrix-Power Kernel"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Me-MPK: Accelerating Krylov Subspace Solvers via Memory-efficient Matrix-Power Kernel

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133082">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133082</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 稀疏矩阵向量乘，矩阵乘方核，缓存重用，矩阵对称性，子空间求解器 </p>
</div>


---

## 研究概要
本文提出内存高效矩阵幂内核Me-MPK，面向多核共享内存架构，统一利用缓存复用与对称矩阵特性。构建统一依赖图，架构感知递归划分结合分隔子图消除冲突；适配s步CG/BiCGStab求解。X86/ARM平台分别平均提速2.00/1.86倍，整机稀疏求解最高提速1.65/1.58倍。

## 背景和动机
1. 矩阵幂内核MPK由连续SpMV构成，是电路仿真等Krylov求解核心，访存受限存在严重内存墙瓶颈。
2. 传统MPK仅单独优化缓存复用或对称Sp，无法同时兼顾两者，难以兼顾带宽与存储开销。
3 连续SpMV存在跨迭代数据依赖，对称矩阵并行SpMV存在多线程写冲突，并行可扩展性差。
4. 现有RACE等分层分块方法复用仅局限L3，高阶幂s下缓存失效严重，性能大幅衰减。
5. 对称SpMV传统归约方案线程临时向量内存开销线性膨胀，图着色方法对高带宽不规则矩阵适配差。

## 相关工作
1. 基础MPK分块策略：基于L3分层着色，复用距离随s增大超出缓存，大幂次性能下滑明显。
2. 行粒度流水线MPK：依赖图着色，同步开销高、空间局部性差。
3. 对称SpMV归约法：多线程本地向量内存随核数线性增长，内存压力大。
4. 对称矩阵图着色并行：适合低带宽矩阵，高不规则电路矩阵扩展性弱。
5. 商用MKL库SpMV：无跨迭代缓存复用机制，每次幂运算重复加载矩阵，访存开销巨大。

## 本文解决方案
### 1 统一依赖图UDG建模
节点代表矩阵行，黑边标记跨SpMV数据依赖，红边标记对称并行写冲突，完整刻画所有并行约束。
### 2 架构感知递归图划分
结合单核心L2缓存容量计算子图最大行数，递归分割；构造分隔子图切断子图间依赖/冲突，重排提升向量访问局部性。
### 3 分层并行调度机制
非对称矩阵单层并行执行；对称矩阵递归拆分分隔图消除写冲突，调度子图连续两轮SpMV实现L2缓存复用。
### 4 统一uSpMV/递归对称内核
封装通用子矩阵SpMV，对称场景递归执行分隔子图并行，彻底规避线程输出写竞争。
### 5 适配s步Krylov求解器
集成s-Step CG、BiCGStab，面向晶体管级SPICE电路矩阵完成优化验证。

## 实验分析
1. 测试平台：28核Xeon X86、32核鲲鹏ARM；数据集含214个SuiteSparse矩阵+12款工业电路矩阵。
2. 内核加速：对比oneMKL、RACE，Me-MPK(reuse+symm)在s=8时X86平均2.00倍、ARM1.86倍。
3. 求解器收益：CG/BiCGStab整机最高提速1.65倍(X86)、1.58倍(ARM)，不影响收敛性。
4. 消融对比：仅缓存复用增益有限，同时结合对称存储与并行冲突消除性能大幅提升。
5. 电路场景：ASIC、全芯片等非对称电路复用方案稳定，G系列对称电路双优化收益显著。

## 研究启发
1. MPK优化需同时挖掘跨迭代缓存复用与对称矩阵存储压缩，单一优化存在性能天花板。
2. 基于L2而非L3做分块复用，能避免高阶幂s下缓存失效，保证多阶运算持续收益。
3. 统一依赖图可同时建模迭代依赖与对称写冲突，分隔子图是无锁并行的轻量化方案。
4. 对称SpMV放弃归约/全局着色，采用递归分隔并行可控制内存开销、适配大规模电路矩阵。
5. 针对EDA电路仿真等稀疏求解场景，内核级访存优化可直接降低整体仿真迭代耗时。
