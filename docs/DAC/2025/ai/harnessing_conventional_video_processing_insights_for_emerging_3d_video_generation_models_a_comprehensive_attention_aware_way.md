---
title: "Harnessing Conventional Video Processing Insights for Emerging 3D Video Generation Models: A Comprehensive Attention-aware Way"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Harnessing Conventional Video Processing Insights for Emerging 3D Video Generation Models: A Comprehensive Attention-aware Way

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dai.sjtu.edu.cn/my_file/pdf/64e0dc2d-66d6-46b6-9ea1-99c90e1cf293.pdf">https://dai.sjtu.edu.cn/my_file/pdf/64e0dc2d-66d6-46b6-9ea1-99c90e1cf293.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 3D视频生成模型，注意力机制，相似性利用，算法-硬件协同设计 </p>
</div>


---

## 研究概要
本文提出面向3D视频生成模型的软硬件协同加速框架SIMPICKER。借鉴传统视频编码时空相似性思路，设计帧/Token两级推测算法，搭配LUT混合乘硬件与自适应分组策略。在CogVideoX、Open-Sora验证无画质损失，相对A10平均提速5.21倍、能效提升17.92倍，优于同类专用ASIC加速器。

## 背景和动机
1. 3D-VGM采用全时空3D注意力，注意力计算占总算力75%以上，相比2D+1D模型算力翻倍，长视频推理延迟极高。
2. 传统视频编码依靠时空块相似性压缩冗余，但现有3D生成加速方案未复用Token相似性，低比特近似法精度损失超5%且提速微弱。
3. 现有相似复用方法中相似Token随机分布，硬件计算单元负载失衡，硬件利用率不足37%。
4. 缺少可实时高效提取Token相似性的轻量算法，同时无原生支持FP-INT混合乘的专用硬件架构。
5. 帧级粗粒度、Token细粒度两类优化难以无缝融合，缺少统一调度策略平衡负载。

## 相关工作
1. GPU视频生成推理：依赖Tensor Core全FP16矩阵运算，无法利用Token相似冗余，混合量化支持差。
2. 稀疏注意力加速器（Sanger/FACT）：仅采用低比特近似预测重要度，精度损耗大，未挖掘时空Token相似。
3. 视频Transformer专用ASIC（InterArch/CMC）：依靠特征去重、编解码压缩，仅面向2D+1D结构，不兼容3D全注意力。
4. 视频编码算法（H.264/HEVC）：成熟利用时空块相似，但仅面向渲染像素，无法迁移至Transformer Token。
5. Token缓存/复用方案：仅局部缓存历史特征，未设计帧+Token双层推测机制，负载失衡问题未解决。

## 本文解决方案
### 1 双层推测相似挖掘算法
粗粒度帧级重要度推测：分块约简矩阵预筛高权重注意力区域，不重要区域切换FP-INT计算，削减65% FP-FP乘法；细粒度时空Token相似匹配，L2阈值复用相似Token计算结果，推理开销仅占总计算1.57%~3.92%。
### 2 SIMCORE LUT缓冲混合乘硬件
内置FP16与INT8预计算查表单元，单周期完成FP-INT乘；采用多本地LUT双预取缓冲，消除并行访存存储冲突，配套量化、稀疏专用子引擎。
### 3 自适应分组负载均衡策略
跳过稀疏矩阵完整恢复流程，直接基于压缩矩阵做注意力推测；动态重组V矩阵列分组，均衡各PE计算量，解决随机相似Token带来的硬件利用率低下问题。
### 4 端到端流水线映射
量化、稀疏、推测、乘算、恢复模块深度流水，Softmax与PV运算融合，片上多级缓存匹配3D时序数据流，兼容CogVideoX、Open-Sora等主流DiT架构。

## 实验分析
1. 实验环境：32nm工艺Verilog综合，片上总缓存628KB；测试CogVideoX-5B、Open-Sora-Plan，基准A100、Sanger/CMC等ASIC。
2. 生成质量：CLIPSIM、VBench指标与FP16基线几乎无衰减，相似阈值、推测比例参数可无损平衡速度画质。
3. 硬件性能：相较A100平均提速5.21倍、能效提升17.92倍；对比SOTA ASIC提速1.45倍，能效提升1.63倍。
4. 消融实验：双层推测算法带来2.01倍加速；LUT混合乘硬件提升1.45倍；自适应分组额外提速1.10倍，三者缺一不可。
5. 硬件开销：整体芯片面积5.93mm²，功耗468.79mW，计算引擎占面积功耗主体，辅助引擎开销仅4.21%。

## 研究启发
1. 传统视频编码时空相似理论可迁移至视频大模型Transformer Token层，是低开销无损加速核心思路。
2. 仅低比特量化稀疏会损失精度，帧+Token双层相似复用可在无画质衰减前提下大幅削减浮点运算。
3 相似Token随机分布会造成硬件严重负载失衡，必须配套自适应分组映射才能释放加速收益。
4. FP-INT混合乘不能依靠通用GPU单元，定制LUT查表硬件可大幅降低乘法计算延迟。
5. 3D全注意力瓶颈远高于FFN，软硬件协同优化应优先针对注意力矩阵计算做冗余消除。
