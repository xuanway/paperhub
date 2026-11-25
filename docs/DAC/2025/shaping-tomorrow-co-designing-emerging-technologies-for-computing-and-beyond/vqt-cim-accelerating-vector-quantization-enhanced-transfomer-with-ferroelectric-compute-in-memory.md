---
title: "VQT-CiM: Accelerating Vector Quantization Enhanced Transfomer with Ferroelectric Compute-in-Memory"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# VQT-CiM: Accelerating Vector Quantization Enhanced Transfomer with Ferroelectric Compute-in-Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133264">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133264</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内计算，向量量化，铁电场效应晶体管，Transformer</p>
</div>

---

## 研究概要
本文提出基于FeFET存内计算的VQT-CiM架构，采用键值联合矢量量化消除注意力动态矩阵乘与运行时写操作。融合残差/乘积矢量量化缓解精度损失，设计并行RVQ数据流与配套数字外设。BERT系列任务测试，相较主流NVM CiM加速器能效提升3.54倍、吞吐提升4.53倍，模型精度平均仅下降0.8%。

## 背景和动机
1. Transformer自注意力存在动态QK、AV矩阵乘，传统NVM CiM需频繁阵列写，写能耗高、器件耐久度受限，还存在读写计算依赖冲突。
2. SRAM/混合存内方案存储密度低、断电丢失数据，异构集成带来制造难度，难以大规模部署。
3. 单一矢量量化表征能力弱，直接部署会大幅降低NLP任务精度，单纯增大码本硬件开销激增。
4. 现有CiM仅单独优化键或值量化，无法同时消除内积、加权求和两步动态VMM，仍存在大量阵列写入。

## 相关工作
1. RRAM类Transformer CiM（ReTransformer/ReBERT/CPSAA）：仅局部优化动态写，未消除KV实时更新，仍存在复杂CWC依赖，能效受限。
2. SRAM/混合存内加速器：存储密度远低于NVM，混合架构工艺兼容性差，嵌入式场景适配性差。
3. Transformer-VQ算法：仅对Key量化，Value仍需实时写入CiM阵列，无法彻底规避动态矩阵乘。
4. 基础VQ硬件实现：未融合RVQ/PV补偿量化误差，串行残差流程推理延迟高，无专用并行数据流设计。

## 本文解决方案
### 1 键值双矢量量化算法改造
对Key、Value同时做VQ，用固定预训练码本替代动态向量，将自注意力两步动态VMM全部转化为基于码本的静态乘，彻底消除阵列运行时写操作。
### 2 RVQ+PVQ混合量化补偿
乘积VQ拆分向量多子空间独立编码；残差VQ多阶迭代拟合残差误差，大幅提升向量表征能力，平衡精度与码本规模。
### 3 RVQ并行数据流优化
预存储码间相似度LUT，把串行残差计算转为并行多码本匹配，消除逐阶迭代时延，适配CiM并行阵列。
### 4 FeFET CiM整体硬件架构
32nm 1FeFET1R交叉阵列执行静态MAC；配套ALU、最大值单元、Softmax、LUT数字外设，分别完成量化、残差、归一化运算。

## 实验分析
1. 仿真环境：NeuroSim+Spectre FeFET器件模型，32nm工艺，测试GLUE、SQUAD、IMDb等BERT任务。
2. 算法精度：最优RVQ/PV配置下模型平均精度仅下降0.8，量化层损失低至0.3%；长文本任务提升量化阶数可缩小精度差距。
3. 硬件指标：平均能效3.19 TOPS/W、吞吐611.1 GOPs，对比ReBERT/ReTransformer/CPSAA能效最高提升14.49倍。
4. 能耗拆解：VQ数字电路总能耗仅占2.1%~3.8%，注意力模块随码本规模线性增长，无序列平方开销。
5. 消融对比：KV双量化是消除动态写核心，RVQ并行化可降低40%以上推理延迟。

## 研究启发
1. NVM CiM加速Transformer核心痛点是动态KV写入，算法层VQ可从根源规避写开销，比电路优化收益更大。
2. 单一VQ精度损耗严重，RVQ+PVQ混合量化能以可控硬件代价还原向量表征。
3. 残差量化天然串行，需预计算辅助表改造数据流，才能匹配存内阵列并行特性。
4. FeFET具备高开关比、电压写入优势，是适配量化Transformer的理想NVM存储介质。
5. 算法-器件协同设计缺一不可，仅优化硬件或仅改进量化算法都无法兼顾精度、能效与吞吐。
