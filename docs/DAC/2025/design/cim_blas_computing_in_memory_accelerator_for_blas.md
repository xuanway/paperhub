---
title: "CIM-BLAS: Computing-in-Memory Accelerator for BLAS"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CIM-BLAS: Computing-in-Memory Accelerator for BLAS

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133288">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133288</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存内计算，非易失性存储器，基本线性代数子程序 </p>
</div>


---

## 研究概要
本文提出首个基于非易失存储的BLAS存内加速器CIM-BLAS，设计统一五阶段浮点流水线解决存内指数对齐难题，配套可配置数据流覆盖一至三级BLAS核心算子。对比V10 GPU，一级/二级算子提速数千倍，三级BLAS能效提升2.6~24.1倍，矩阵规模越大优势越显著。

## 背景和动机
1. BLAS是科学计算底层核心库，向量、矩阵运算访存密集，CPU/GPU受内存墙、带宽限制，数据搬运能耗极高。
2. 现有存内计算架构多面向神经网络，仅支持定点运算，无法兼容BLAS所需32/64位高精度浮点。
3. 传统CIM缺少转置、三角求解、矩阵外积等复杂线性代数算子硬件映射方案，需额外协处理器带来开销。
4. 尚无专用CIM架构完整适配全系列BLAS算子，无法为PCA、CG等科学计算应用提供底层加速支撑。

## 相关工作
1. CPU/GPU BLAS库（cuBLAS/ACML）：依赖冯诺依曼架构，跨层数据传输能耗巨大，大规模矩阵性能受限。
2. 神经网络CIM加速器：仅低精度定点乘加，无浮点指数对齐电路，不支持复杂线性代数运算。
3. 专用科学计算存内设计：仅覆盖最小二乘等单一算法，未标准化适配全套BLAS算子。
4. 密码类存内架构：侧重位运算，缺少向量内积、三角分解等浮点矩阵运算通路。

## 本文解决方案
### 1. 统一存内浮点五阶段流水线
尾数、指数分离存储，通过指数比较、偏移移位完成对齐，将浮点运算等价转换为阵列定点乘加，原生支持32/64位高精度浮点，无需外部浮点单元。
### 2. H树分层硬件架构
PE-CU-阵列三级层级，RRAM交叉阵作为计算核心，片上缓存配合移位加法单元复用硬件实现加减、除法、转置，不新增专用外设。
### 3. Ripple脉动内积流水线
复用阵列移位加法单元串行累加部分和，消除传统加法树面积与延迟开销，高效实现DOT、ASUM、NRM2向量算子。
### 4. 全系列BLAS可配置数据流
针对SCAL/GEMV/GEMM/TRSV/SYR/SYRK等算子定制映射逻辑，三角方程组采用前代回代，外积矩阵复用缓冲消除重复计算。
### 5. 符号偏移编码
尾数增加偏移常量统一表示正负数值，省去独立符号位存储，简化阵列模拟运算电路。

## 实验分析
1. 仿真环境：45nm工艺，256×256 RRAM阵列，HSPICE模拟模拟单元，对比NVIDIA V100 cuBLAS。
2. 一/二级BLAS：DDOT、DGEMV等算子提速2000~26万倍，能耗降低数千倍，运行时长几乎不随向量规模增长。
3. 三级BLAS：能效提升2.6~24.1倍，矩阵尺寸越大能效增益越高；DTRSM三角求解随规模逐步反超GPU。
4. 应用测试：PCA、共轭梯度等6类科学计算平均延迟降低4.88倍，迭代类算法能耗降幅最突出。
5. 硬件开销：复用移位加法实现四则、三角运算，无独立除法/转置协处理器，模拟阵列硬件成本可控。

## 研究启发
1. 通用线性代数存内加速核心瓶颈是浮点对齐，指数尾数分离+移位对齐是低成本存内浮点实现方案。
2. 全套BLAS无需新增大量专用硬件，复用阵列移位加法单元可映射减法、除法、矩阵外积等复杂运算。
3. 向量级一级/二级算子访存瓶颈最严重，CIM原位计算相比GPU存在数量级性能差距。
4. 分层H树架构便于矩阵分块映射，适配不同维度矩阵并行，可灵活切换各类BLAS数据流。
5. 底层BLAS存内加速可直接赋能上层科学计算、优化迭代类应用，具备广泛工程落地价值。