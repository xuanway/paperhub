---
title: "An Input-Aware Sparse Tensor Compiler Empowered by Vectorized Acceleration"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# An Input-Aware Sparse Tensor Compiler Empowered by Vectorized Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133371">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133371</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 稀疏矩阵-矩阵乘法，稀疏张量编译器，输入感知，向量化加速</p>
</div>

---

## 研究概要
本文提出面向多核CPU的输入感知稀疏张量编译器SpMMTC，依据稀疏矩阵非零分布自适应分块，定制向量化FMA内核，配套专用稀疏存储与稠密打包布局。科学计算与剪枝深度学习矩阵测试，相较MKL、TVM等提速1.21~2.97倍；树莓派稀疏MobileNet推理最高加速1.52倍。

## 背景和动机
1. SpMM存在离散索引导致缓存局部性差，传统库依赖人工重排，开发成本高；通用张量编译器不感知稀疏分布，调参耗时极长。
2. TVM、TACO等通用编译器缺少稀疏专属分块与存储变换，无法最大化SIMD向量化利用率，冗余浮点运算多。
3. CSR/CSC标准格式不匹配向量化加载逻辑，直接执行会频繁访存稠密矩阵零散行，计算访存比(CMR)偏低。
4. 现有方案缺少软硬件协同分块策略，未按各行非零数量自适应划分 tile，固定分块适配各类稀疏矩阵性能波动大。

## 相关工作
1. 专用稀疏库(ASpT/MKL)：依靠人工行重排优化复用，泛化性差，新稀疏模式需重新开发内核。
2. 通用张量编译器(TACO/TVM)：分离计算与调度，但无稀疏特征解析，自动调参迭代耗时数十小时。
3. TC-GNN等GPU稀疏方案：面向张量核心，会产生大量零值冗余计算，不适用CPU SIMD架构。
4. XNNPack深度学习稀疏库：仅固定稀疏处理逻辑，无法根据输入稀疏分布动态生成最优向量化内核。

## 本文解决方案
### 1 五层整体编译流水线
输入稀疏矩阵+硬件参数，经稀疏解析、内存优化、模板组装、代码生成、编译执行五阶段，自动生成适配SpMM的向量化C代码。
### 2 稀疏解析器自适应分块
贪心分块算法优先选取高非零行拓展tile，最小稠密离散索引访问次数，兼顾向量寄存器硬件约束，动态确定每个tile尺寸。
### 3 专用稀疏存储格式
重构tiles/indices/data三段式存储，indices分段编码tile内行、列号，支持单次向量加载批量非零值，适配外积计算范式。
### 4 内存布局优化器
1) 稀疏矩阵堆排序重排为列主序；2) 稠密矩阵按Nr分块打包，提升连续缓存命中率。
### 5 向量化内核模板生成器
基于硬件向量长度、寄存器上限推导最大循环展开系数，生成批量FMA向量化代码，最大化CMR，无冗余零值运算。

## 实验分析
1. 测试平台：Intel Xeon、鲲鹏ARM服务器、树莓派4边缘设备；基线MKL、ASpT、TACO、TVM、XNNPack。
2. 科学计算稀疏矩阵：x86平均提速2.46x，ARM平均1.99x，最高加速2.97倍，调参迭代远少于TVM。
3. 剪枝深度学习矩阵：ResNet50稀疏权重下平均提速1.21~1.84倍，高稀疏度优势明显。
4. 边缘端验证：稀疏MobileNetV1推理相比XNNPack最高1.52倍加速，单/多线程均稳定提升。
5. 消融：自适应分块+定制存储是核心增益，缺少任意一项性能大幅衰减。

## 研究启发
1. 稀疏计算编译器必须感知输入非零分布，固定分块无法适配多样稀疏模式。
2 外积范式搭配定制稀疏存储，可消除零值冗余运算，大幅提升SIMD向量化效率。
3. 稠密矩阵打包、稀疏重排两类布局优化协同，才能解决离散索引访存瓶颈。
4. 向量化内核生成需绑定硬件向量寄存器约束，动态展开系数平衡并行与资源上限。
5. 面向CPU稀疏编译无需长时间自动调参，输入驱动自适应分块可快速生成高性能专用内核。