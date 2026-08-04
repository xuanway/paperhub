---
title: "EPIC: Error PredIction and Correction for Power-Efficient Voltage Underscaling Multiply-Accumulate Unit"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# EPIC: Error PredIction and Correction for Power-Efficient Voltage Underscaling Multiply-Accumulate Unit


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132540">https://ieeexplore.ieee.org/document/11132540</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>高能效，时序错误容错电路，电压欠缩放 </p>
</div>


---

## 研究概要
本文提出EPIC时序误差预测校正框架，面向电压降额MAC单元。设计预测比特搜索算法、低功耗跳变检测器与传输门短路径填充，搭配可调延迟时钟完成全位纠错。28nm工艺下总面积开销仅8%，最高节电52%；MLP推理同等精度下功耗再降11%，相较同类弹性电路面积节省60%~88%。

## 背景和动机
1. DNN核心MAC阵列功耗巨大，电压降额可大幅降功耗，但低电压引发时序违例，微小错误就会造成模型精度暴跌。
2. 主流Razor等EDaC电路需额外寄存器、多路选择器，仅保护部分高位，硬件面积开销极高，无法全覆盖输出比特。
3. 传统误差注入仿真无法还原真实时序依赖关系，大规模神经网络仿真精度差、SPICE仿真速度极慢。
4. 低电压下短路径提前输入引发保持违例，现有缓冲填充方法窗口不可调，硬件成本高。

## 相关工作
1. Razor系列时序容错：双采样触发器做误差检测，仅保护少数高位，整体面积开销可达32%，无法实现100%纠错。
2. TE-Drop/CMAC张量容错：检测出错MAC直接丢弃部分乘积，牺牲计算精度换取低硬件代价。
3. STRIVE/EFFORT专用TPU弹性电路：基于跳变检测器，但缺少最优预测比特筛选，冗余检测电路多。
4. 误差注入仿真方案：仅按固定误码率注入，忽略前后输入时序耦合，仿真结果与真实电路偏差大。

## 本文解决方案
### 1. 最优预测比特搜索算法
遍历MAC内部进位、乘法中间信号组合，筛选最少信号实现100%时序错误检出，硬件开销最小化。
### 2. 14管低功耗跳变检测器TD
在时钟负相监测信号翻转，生成误差脉冲；配套控制锁存电路延长误差信号，适配时钟切换时序。
### 3. 传输门TG短路径填充
无需插入缓冲，通过门控锁存加法器输入，动态匹配延迟时钟窗口，窗口可灵活调节。
### 4. 可调延迟时钟纠错通路
预测出错时切换延迟时钟重采样正确结果，完整覆盖MAC全部输出比特，无精度损失。
### 5. 时序精准分层仿真流程
结合SPICE单元时序与RTL仿真，速度提升三个数量级，可精准评估大规模 systolic阵列推理效果。

## 实验分析
1. 工艺与负载：28nm CMOS，1GHz时钟，LP/DW/HS三类MAC，MNIST/FMNIST/Reuters三层MLP systolic阵列。
2. 电路指标：电压降额系数0.74时实现100%纠错，弹性电路总面积开销仅8%，功耗开销最高1.52%。
3. 功耗收益：相较标称电压MAC最高省电52%；MLP保持原精度时功耗额外降低11%。
4. 硬件对比：相比Razor、STRIVE等SOTA，弹性逻辑面积节省60%~88%。
5. 仿真性能：自研时序仿真流程等效AMS精度，仿真速度提升超1000倍，适配大型神经网络评估。

## 研究启发
1. 时序误差无需比对最终输出，挖掘MAC内部进位、中间乘积信号可低成本实现全局错误预判。
2. 传输门动态填充优于固定缓冲，可自适应延迟时钟窗口，消除保持违例且面积极低。
3. 晶体管级定制TD检测器比标准单元Razor大幅缩减硬件开销，是低电压阵列优选容错方案。
4. 单纯误码注入仿真不可靠，必须导入真实单元时序特征才能精准评估低电压DNN推理性能。
5. 面向 systolic阵列的容错设计需兼顾单MAC电路开销与全局网络精度，全比特纠错才能避免分类任务精度断崖下跌。