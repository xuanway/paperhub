---
title: "Pipirima: Predicting Patterns in Sparsity to Accelerate Matrix Algebra"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Pipirima: Predicting Patterns in Sparsity to Accelerate Matrix Algebra

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ubaidhunts.github.io/ubaidb/assets/projects/Piprima_DAC.pdf">https://ubaidhunts.github.io/ubaidb/assets/projects/Piprima_DAC.pdf</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>稀疏矩阵加速器，基于预测的模式识别，稀疏矩阵-向量乘法，稀疏矩阵-矩阵乘法，轻量级计数器式预测器 </p>
</div>

---

## 研究概要
本文提出基于计数器预测的稀疏矩阵加速器Pipirima，设计两类轻量预测器预判矩阵结构与每行非零元数量，解决稀疏计算负载失衡问题。适配SpMV/SpMM，SuiteSparse与BERT稀疏注意力测试，相较Tensaurus、ExTensor分别提速4~6倍、最高40倍，预测硬件面积功耗开销极低。

## 背景和动机
1. 科学计算、Transformer注意力存在大量CSR稀疏矩阵，现有加速器无法利用对角等结构化稀疏跳过冗余运算。
2. 各行非零元分布不均引发细粒度负载失衡，并行计算单元利用率低下，成为稀疏运算核心瓶颈。
3. 传统方案依赖复杂预处理划分矩阵，硬件开销大，缺少轻量实时预判机制均衡数据分配。
4. ExTensor、Tensaurus等主流稀疏加速器未挖掘行间稀疏连续性，无法实现近乎完美的数据分片分配。

## 相关工作
1. ExTensor：识别零乘冗余计算，仅优化无效乘法，无负载均衡与结构预判能力。
2. Tensaurus：分块向量化稀疏张量计算，分片分配策略简单，负载失衡严重。
3. MatRaptor：自定义C²SR格式记录每行非零数，采用轮询分配，无法实现均衡分片。
4. Sigma：专用稀疏加法树，仅优化部分和累加，未解决并行单元负载不均根源问题。

## 本文解决方案
### 1 双CBP计数器预测单元
1比特D/R预测器区分对角/随机矩阵，ln(m)比特NNZ预测器依据历史预判当前块每行非零数量；仅少量寄存器，硬件成本极低。
### 2 预测校验流水线
配套两类校验器，错分时刷新预测状态；对角矩阵直接走专用DSMU通路，跳过索引读取等冗余步骤。
### 3 分块并行计算硬件
划分IMU乘法单元，搭配CBR连续缓存与CAT加法树；随机稀疏走RSMU，对角稀疏使用专用乘法通路，并行多tile运算。
### 4 分片均衡调度
基于NNZ预测结果均匀分发非零数据至各存储分区，消除串行读写瓶颈，最大化硬件并行度。

## 实验分析
1. 测试负载：SuiteSparse科学矩阵、合成稀疏矩阵、BERT多头注意力稀疏张量，支持行/点积两种SpMM、SpMV。
2. 性能：SuiteSparse下SpMM超Tensaurus6倍、超ExTensor40倍；BERT稠密稀疏场景提速8.3~48.2倍。
3. 硬件：45nm工艺总面积5.621mm²，功耗544.93mW，预测组件面积占比不足0.2%。
4. 误差与开销：矩阵密度、分块尺寸增大时预测错误率小幅上升，但内存/计算总开销低于13%。
5. 扩展性：支持8~2048多规格分块，分块越大预测分摊开销越低，对角矩阵加速收益最显著。

## 研究启发
1. 稀疏矩阵存在极强行连续性，极简计数器预测即可预判稀疏模式，无需复杂预处理。
2. 结构化对角稀疏可大幅简化运算通路，单独硬件通路能跳过索引、偏移读取等冗余操作。
3. 负载失衡根源是非零元分配无序，预判每行非零数量可实现近乎完美分片并行。
4. 预测模块硬件代价极低，属于低成本高收益稀疏架构优化思路，易集成现有加速器。
5. Transformer注意力稠密稀疏场景传统加速器收益有限，预测均衡架构适配此类新型稀疏负载。
