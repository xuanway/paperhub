---
title: "RADiT: Redundancy-Aware Diffusion Transformer Acceleration Leveraging Timestep Similarity"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# RADiT: Redundancy-Aware Diffusion Transformer Acceleration Leveraging Timestep Similarity

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133190">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133190</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 扩散模型，Transformer，神经网络，时间步相似性，硬件加速器 </p>
</div>


---

## 研究概要
本文提出软硬件协同加速器RADiT，挖掘DiT扩散模型相邻时间步特征相似冗余，设计块级复用计算方案。配套动态阈值DTS模块与4bit压缩对比CCU单元，28nm流片硬件开销极低。图像/视频推理分别提速1.8×、1.7×，能耗下降41%、45.5%，生成画质损失极小。

## 背景和动机
1. DiT采用Transformer骨干，相比U-Net扩散模型算力、访存开销大幅上升，迭代去噪采样时延、能耗过高，难以实时部署。
2. 现有扩散加速器仅适配U-Net结构，无法处理时空注意力、交叉注意力等DiT特有算子。
3. 相邻采样步内Transformer块输入特征高度近似，但固定阈值复用易累积误差，生成图像/视频画质崩坏。
4. 逐帧原始特征对比检测冗余带来巨大访存开销，冗余检测抵消加速收益。
5. 缺乏面向DiT的软硬件协同冗余消除方案，算法优化与硬件计算单元割裂。

## 相关工作
1. U-Net专用扩散加速器(ISSCC/VLSI系列)：仅支持卷积架构，无注意力加速模块，不兼容DiT时空交叉注意力。
2. 算法层时序缓存优化DeepCache：纯软件方案，无配套定制硬件，访存开销难以压缩。
3. 通用Transformer脉动阵列：未利用扩散模型时序冗余，每一步完整重算全部块，算力浪费严重。
4. 低比特特征压缩研究：仅面向静态网络，未适配多时间步连续特征对比场景。
5. 固定阈值复用策略：时序误差持续累积，高分辨率视频生成质量衰减明显。

## 本文解决方案
### 1 块级时序冗余复用算法
遍历各Transformer块（自注意力/交叉注意力/MLP），对比相邻时间步输入特征；相似度达标则完全跳过本块全部计算，直接复用前一步输出，省去权重加载、矩阵乘、归一化全流程。
### 2 动态阈值缩放模块DTS
线性/余弦两种自适应阈值调度，依据时序特征波动实时更新判断门限；特征变化剧烈收紧阈值、宽松时段放宽，抑制误差累积，平衡速度与画质。
### 3 4bit特征压缩对比单元CC
依据LN后特征数值区间划分三类编码规则，将FP16特征压缩至4bit存储；通过异或掩码快速计算特征差异，冗余检测访存带宽缩减4倍，检测开销仅1.5%。
### 4 RADiT整体硬件架构
64×64通用脉动阵列适配DiT全算子；CCU与DTS作为轻量辅助单元，总硬件面积仅增加0.3%；SRAM缓存压缩历史特征，控制器接收跳过信号调度阵列。
### 5 端到端DiT推理流水线
嵌入自适应LN后插入CCU压缩，DTS输出跳过控制信号至脉动阵列，复用结果直接送入下一块，无需重走完整计算通路。

## 实验分析
1. 实验环境：28nm工艺、500MHz Verilog综合，基线无冗余DiT加速器；测试DiT-XL图像、Latte视频生成模型，指标FID/FVD/VBench、时延、功耗、硬件面积。
2. 画质表现：线性/余弦DTS仅小幅提升FID/FVD，部分文本视频任务指标小幅优于基线，无明显视觉失真。
3. 算力与时延：图像推理算力降低1.7×、时延下降40%；视频算力降低1.8×、时延下降43.1%。
4. 能耗指标：图像能耗削减41%，2s短视频能耗降低45.5%，DRAM访存为主要能耗来源。
5. 硬件开销：CCU+DTS额外逻辑面积仅0.3%，存储开销小幅增加，整体芯片成本可控。

## 研究启发
1. DiT迭代采样存在大量时序计算冗余，块级整体复用比单算子裁剪能获得更大加速收益。
2. 固定阈值复用会随采样步累积误差，动态自适应门限是兼顾速度与生成质量的核心。
3. 低比特压缩可大幅降低时序特征对比的访存开销，冗余检测的硬件成本可忽略。
4. 传统U-Net扩散加速架构无法迁移至DiT，必须针对时空、交叉注意力定制软硬件协同设计。
5. 辅助检测单元硬件开销极低，时序冗余挖掘是低成本降低生成模型算力的高效路线。
