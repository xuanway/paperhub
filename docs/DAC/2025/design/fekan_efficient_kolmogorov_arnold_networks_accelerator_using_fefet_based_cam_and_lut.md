---
title: "FeKAN: Efficient Kolmogorov-Arnold Networks Accelerator Using FeFET-based CAM and LUT"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# FeKAN: Efficient Kolmogorov-Arnold Networks Accelerator Using FeFET-based CAM and LUT

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132687">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132687</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>Kolmogorov-Arnold网络，铁电场效应晶体管，存内计算，B样条插值，内容可寻址存储器 </p>
</div>


---

## 研究概要
本文提出FeKAN铁电存内加速器，软硬件协同优化KAN的B样条激活计算。设计两阶段DSE生成静态码本，搭配CSC稀疏编码、分组流水线，集成FeFET-CAM/LUT/CIM阵列。多模态测试相较CPU、GPU吞吐量最高提升150.68K、4664倍，能效分别提升606.87、11196倍。

## 背景和动机
1. KAN依靠递归B样条插值(BSI)完成非线性激活，传统GPU/CPU反复访存迭代，BSI占总推理时延65.6%以上，算力能耗瓶颈严重。
2. 现有存内计算架构专为MLP矩阵乘设计，无法适配K动态递归插值，直接部署读写开销大、耐久度差。
3. B样条多尺度映射会产生超大码本，直接存储硬件成本极高；基函数非局部稀疏带来大量无效乘加计算。
4. BSI计算存在强数据依赖，串行执行资源闲置，缺乏面向KAN的专用并行流水优化方案。

## 相关工作
1. 通用DNN存内加速器（ISAAC/PRIME/FELIX）：仅优化VMM矩阵运算，无B样条插值专用映射逻辑，适配KAN效率极低。
2. MLP稀疏加速方案（EIE/SCNN）：面向权重稀疏，不支持B样条基函数结构化稀疏编码。
3. FeFET-CAM/LUT硬件：仅用于检索、简单非线性近似，未与KAN完整BSI推理链路结合。
4. KAN软件优化：仅做量化、剪枝，无法解决递归插值带来的片外访存瓶颈，硬件加速缺失。

## 本文解决方案
### 1. 两阶段DSE码本生成算法
粗搜+精搜联合优化输入区间、采样点数、量化位宽，在精度损失<1%前提下构建轻量化共享BSI静态码本，将动态递归转为查表运算。
### 2. GQA-LUT非线性近似
遗传分段线性拟合SiLU基础激活，转化为FeFET-LUT可存储分段参数，消除浮点递归运算。
### 3. CSC稀疏编码+分组计算
提取B样条矩阵非零元素，存储列索引与对应值；按特征维度分组仅执行有效加权，削减存储与乘加冗余。
### 4. 分组流水线并行优化
分块拆分控制点矩阵，打破BSI阶段数据依赖，重叠基函数生成与插值加权，提升阵列并行度。
### 5. 混合FeFET架构
集成CAM并行键匹配、LUT地址译码、CIM模拟加权阵列，搭配网格扩展引擎支持精细插值微调。

## 实验分析
1. 测试环境：45nm FeFET器件仿真、NeuroSim 32nm CIM，对比Xeon CPU、RTX4060/4090/A6000 GPU；数据集含图像、语音、心电三类。
2. 量化鲁棒性：8bit量化精度接近基线，4bit以下精度大幅下滑，最优码本采样区间[-1,1]、10个采样点。
3. 吞吐性能：FeKAN-LUT相对CPU最高提速150680×，CAM方案相对A6000提速2303×；流水线优化后KAN-III吞吐达6177 GOPS。
4. 能效表现：相较CPU最高提升606.87×，对比A6000提升上万倍；稀疏优化后能效最高43.76 TOPS/W。
5. 消融实验：稀疏编码可大幅降低CAM/CIM能耗，分组流水线显著削减推理时延，两项优化缺一不可。

## 研究启发
1. KAN递归插值是核心瓶颈，将动态计算离线转为静态查表是存内加速可行核心思路。
2. FeFET兼具CAM并行检索与C模拟乘能力，混合阵列可同时处理查表、加权两类KAN特有运算。
3. B样条结构化稀疏不能直接套用DNN稀疏方案，专用CS编码能大幅降低存储与计算冗余。
4. 算法层DSE码本优化与硬件层流水线、稀疏加速必须协同，单一优化收益有限。
5. 非线性激活可通过遗传分段LUT近似，适配低精度存内硬件，避免浮点迭代开销。
