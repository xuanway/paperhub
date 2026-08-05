---
title: "MemSens: Significantly Reducing Memory Overhead in Adjoint Sensitivity Analysis Using Novel Error-Bounded Lossy Compression"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# MemSens: Significantly Reducing Memory Overhead in Adjoint Sensitivity Analysis Using Novel Error-Bounded Lossy Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://www.ssslab.cn/assets/papers/2025-li-MemSens.pdf">https://www.ssslab.cn/assets/papers/2025-li-MemSens.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://www.ssslab.cn/assets/slides/2025-li-MemSens.pdf">https://www.ssslab.cn/assets/slides/2025-li-MemSens.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 有损压缩，电路仿真，伴随灵敏度分析 </p>
</div>

---

## 研究概要
本文提出MemSens误差可控有损压缩框架，面向伴随灵敏度分析电路仿真。设计参考排序平滑、混合预测器、严格误差量化三层压缩流程，适配电路尖峰向量/矩阵数据。集成Xyce仿真器测试，相较主流压缩算法平均压缩比提升百倍级，内存开销降低两个数量级，同时严格保障灵敏度计算精度。

## 背景和动机
1. 伴随灵敏度分析前向仿真需逐时刻存储状态向量、雅可比矩阵，大规模电路内存开销爆炸，成为仿真瓶颈。
2. 无损压缩对浮点电路数据压缩比极低，传统有损压缩依赖数据平滑假设，电路尖峰数据压缩效果差。
3. ZFP、SZ等通用有损算法压缩误差累积，反向灵敏度计算结果失真，无法满足电路设计精度需求。
4. 现有面向EDA的压缩方案仅适配单一波形，不能同时处理仿真向量与雅可比矩阵两类数据。
5. 缺少可嵌入仿真流水线、同时约束绝对/相对误差的专用内存压缩方案。

## 相关工作
1. 无损压缩(ZSTD/MASC)：压缩比不足10倍，无法缓解大规模仿真内存压力。
2. 通用有损压缩(ZFP/SZ/FPZIP)：适配平滑科学数据，电路尖峰数据压缩倍率低、误差累积严重。
3. 波形专用压缩：仅处理输出波形，不覆盖仿真核心状态矩阵、向量。
4. MASC电路矩阵压缩：仅无损时序预测，无误差控制，内存缩减幅度有限。
5. HPC内存有损方案：面向深度学习、地震模拟，未针对DAE电路方程数据特性优化。

## 本文解决方案
### 1 参考排序数据平滑预处理
首时序排序建立全局参考索引，后续时序按索引重排聚集相近浮点值；设置校验点动态更新索引，将尖峰数据转化为强自相关序列，低时间开销。
### 2 区域混合预测器
划分稳态区、陡变区：稳态采用RLE-FP区间游程编码，陡变使用多项式插值预测，分区域消除数据冗余。
### 3 双约束误差量化编码
同时约束绝对、相对误差阈值，计算浮点数需保留尾数位；不可预测残差做异或、截断低位，搭配变长索引编码+ZSTD二次无损压缩。
### 4 仿真流水线嵌入架构
前向仿真每步压缩状态数据存入内存；反向伴随计算时实时解压重建DAE方程，压缩/解压耗时远低于仿真总时长。
### 5 统一向量/矩阵压缩接口
一套算法兼容电路状态向量、稀疏雅可比两类浮点数据集，无需分模块定制处理逻辑。

## 实验分析
1. 测试环境：Xyce SPICE兼容仿真器，AMD CPU；数据集含IBM、MOS线性/非线性电路向量、矩阵。
2. 压缩性能：MemSens平均压缩比255倍，是SZ的2.44倍、ZFP的36倍、ZSTD的23倍，内存降低两个数量级。
3. 误差表现：严格控制相对/绝对误差上限，伴随灵敏度仿真结果误差维持1e-7量级，无累积失真。
4. 耗时对比：压缩、解压单步耗时远小于瞬态求解总开销，不会显著拖慢仿真速度。
5. 通用性：线性RLC、非线性MOS电路均稳定高效，同时适配状态向量与雅可比矩阵。

## 研究启发
1. 电路仿真数据存在尖峰特性，通用平滑类有损压缩不适用，需专用重排序预处理提升相关性。
2. 稳态、陡变浮点数据规律差异大，分区域混合预测比单一预测器压缩收益更高。
3. 伴随分析对误差敏感，必须同时绑定绝对、相对双误差约束，防止反向梯度失真。
4. 压缩算法需深度嵌入仿真前向/反向完整流水线，才能真正解决内存墙瓶颈。
5. 面向EDA的压缩不能只针对输出波形，状态向量、雅可比矩阵才是内存占用核心。
