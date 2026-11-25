---
title: "SDM-PEB: Spatial-Depthwise Mamba for Enhanced Post-Exposure Bake Simulation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# SDM-PEB: Spatial-Depthwise Mamba for Enhanced Post-Exposure Bake Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA8: Design for Manufacturing and Reliability</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://yibolin.com/publications/papers/LITHO_DAC2025_Yu.pdf">https://yibolin.com/publications/papers/LITHO_DAC2025_Yu.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 后曝光烘烤模拟，空间-深度Mamba，分层特征提取，PEB焦点损失 </p>
</div>


---

## 研究概要
本文提出SDM-PEB深度学习框架用于光刻曝光后烘烤仿真，分层特征提取搭配空间深度Mamba单元捕捉三维光刻胶层间依赖，设计PEB焦点损失与深度散度正则解决数据失衡。28nm工艺测试，相较SOTA DeePEB抑制剂NRMSE降低35%，仿真速度较商用S-Litho快138倍，关键尺寸误差显著下降。

## 背景和动机
1. 传统有限元PEB求解计算耗时极高，占完整光刻仿真30%，大规模版图迭代成本难以承受。
2. 现有深度学习PEB模型（DeePEB/FNO）难以完整捕获x-y平面空间与z轴深度耦合扩散反应，高频轮廓预测失真。
3. 光刻胶抑制剂数值分布极度不均衡，常规MSE损失对接触孔关键区域微小变化敏感度不足。
4. 现有序列模型仅支持单向扫描，无法同时建模同层横向扩散、深浅层双向酸碱扩散依赖关系。
5. 通用CNN/Fourier算子易丢失边缘高频率光刻轮廓细节，最终CD尺寸预测偏差大。

## 相关工作
1. 数值求解方法（FDM/FEA）：严格符合反应扩散方程，但计算量庞大，工业版图不可扩展。
2. 基础CNN光刻模型：仅提取局部二维特征，缺失三维层间扩散关联，CD误差偏高。
3. FNO/DeePEB：傅里叶算子捕捉全局低频，但割裂深度连续依赖，高低频特征融合不足。
4. TEMPO系列GAN：面向光场仿真，未适配PEB酸碱催化反应三维分布建模。
5. 通用Mamba视觉模型：仅二维图像建模，无适配光刻z轴深度三向扫描机制。

## 本文解决方案
### 1 分层重叠块多尺度特征提取器
多层3D卷积下采样，采用重叠块拼接消除块边界信息丢失；轻量化空间自注意力降低平方复杂度，同步提取粗粒度全局与精细局部光刻特征。
### 2 空间深度Mamba（SDM）核心单元
设计三向选择性扫描：平面空间扫描、深度前向、深度反向并行SSM，统一捕获同层扩散与跨层酸碱催化连续依赖。
### 3 定制双约束损失函数
PEB焦点损失加重接触孔极值区域误差权重，解决分布失衡；深度差分KL散度正则对齐各层浓度梯度变化，强化纵向连续性。
### 4 对数域数值预处理
对抑制剂浓度做负对数变换，压缩数值跨度，提升模型对微小浓度梯度的拟合能力。
### 5 完整3D PEB预测流水线
输入三维光酸分布→分层编码→SDM深度建模→解码器输出抑制剂场，再通过Mack/Eikonal模型求解显影轮廓与CD值。

## 实验分析
1. 实验配置：28nm以下接触孔版图，100组掩模样本，对比DeepCNN、TEMPO、FNO、DeePEB，基准为S-Litho商用仿真器。
2. 精度指标：抑制剂NRMSE仅3.70%，较DeePEB下降35%；X/Y方向CD误差降至0.74/0.93nm。
3. 运行效率：单样本推理1.06s，比商用工具提速138倍，相比DeePEB提速29.2%。
4. 消融实验：单层编码器、双向扫描、焦点损失、正则项任一移除都会大幅提升预测误差。
5. 可视化：顶层/底层光刻胶浓度、三维垂直轮廓预测与真值偏差极小，接触孔边缘失真得到明显抑制。

## 研究启发
1. PEB仿真是三维连续物理过程，仅二维建模会丢失层间酸碱扩散关键耦合信息，必须引入深度维度序列建模。
2. Mamba选择性状态空间模型适配光刻深度长距离依赖，三向并行扫描可同时兼顾平面与纵向反应特征。
3. 光刻数值分布不均衡不能仅依靠普通均方误差，定制焦点损失可提升工艺关键区域预测精度。
4. 分层重叠下采样可避免分块边界浓度断层，是提升精细光刻轮廓保真度低成本手段。
5. 深度学习PEB可在远低于商用数值工具的耗时下满足工艺CD精度，能大幅缩短光刻OPC迭代周期。
