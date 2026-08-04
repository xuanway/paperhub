---
title: "ReSMiPS: A ReRAM-based Sparse Mixed-precision Solver with Fast Matrix Reordering Algorithm"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ReSMiPS: A ReRAM-based Sparse Mixed-precision Solver with Fast Matrix Reordering Algorithm

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133301">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133301</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>稀疏矩阵方程，混合精度求解器，阻变存储器，存内计算 </p>
</div>

---

## 研究概要
本文提出ReSMiPS基于ReRAM混合精度稀疏求解器，设计FSM矩阵重排算法与IF64存内浮点格式，构建数字-ReRAM混合BiCGSTAB迭代框架。SuiteSparse稀疏矩阵测试残差低于10⁻¹⁵，相较CPU/GPU提速数千倍，能耗降低两个数量级。

## 背景和动机
1. 传统CPU/GPU求解大规模稀疏方程组存在冯诺依曼访存墙，SpMV搬运开销极高，算力与能效受限。
2. 现有ReRAM存内计算难以高效适配稀疏矩阵，零元占用阵列资源，并行度大幅下降。
3. IEEE FP64直接映射ReRAM硬件开销巨大，FP32动态范围不足，模拟阵列噪声造成求解精度不达标。
4. 主流CIM缺少专用浮点对齐与稀疏分块机制，迭代求解无法兼顾高精度与硬件效率。

## 相关工作
1. 通用ReRAM CIM加速器：面向AI定点计算，无原生浮点支持，不适配科学计算高精度稀疏求解。
2. 稀疏SpMV CIM（Fspa/Recg）：仅做简单稀疏存储，无对称重排优化，阵列利用率低。
3. 浮点ReRAM架构（Refloat/ArpCIM）：采用全局指数对齐，动态范围适配差，未针对稀疏分块优化。
4. 传统矩阵重排（Cuthill-McKee）：行列变换不对称，SpMV向量变换额外增加计算开销。

## 本文解决方案
### 1 FSMR快速稀疏矩阵重排算法
改进Cuthill-McKee，生成对称变换矩阵，将非零元聚拢至对角稠密子块，消除不对称变换带来的向量运算损耗，适配ReRAM分块并行。
### 2 IF64存内浮点数据格式
11位指数+20位尾数，保留FP64动态范围，缩短尾数降低映射开销；支持分块局部指数对齐，抑制动态范围差异带来精度损失。
### 3 分层IF64 ReRAM-CIM宏
SLC/MLC混合存储尾数，配套多级移位加法单元；采用分块局部预对齐替代全局对齐，降低截断误差。
### 4 数模混合迭代求解框架
ReRAM完成低精度BiCGSTAB近似更新，数字单元FP64高精度残差校正，迭代至残差<10⁻¹⁵输出最终解。

## 实验分析
1. 测试集：SuiteSparse12组真实稀疏矩阵，覆盖流体、电力等场景，对比i7 CPU、RTX4070Ti GPU。
2. 精度：500次迭代内所有矩阵残差稳定低于10⁻¹⁵，病态矩阵仍稳定收敛。
3. 性能：相比CPU最高提速7500倍，相比GPU提速600倍；FSMR单独带来平均5倍加速。
4. 能耗：相较CPU节能6.1万倍、相较GPU节能2100倍，FSMR平均削减4.4倍运算能耗。
5. 硬件：22nm工艺，9个计算Tile，16×128 ReRAM阵列，面积与ADC功耗开销可控。

## 研究启发
1. 稀疏科学计算CIM必须配套专用矩阵重排，对称分块是释放阵列并行度的核心手段。
2. 不能直接复用标准IEEE浮点格式，面向存内计算定制浮点格式可大幅削减硬件开销。
3. 局部指数对齐优于全局对齐，能有效缓解大动态范围矩阵的模拟计算精度衰减。
4. 数模混合迭代架构兼顾CIM高能效与数字高精度，是科学求解器可行路线。
5. ReRAM SLC/MLC混合存储可平衡存储密度与尾数运算精度，适配高精度浮点SpMV。