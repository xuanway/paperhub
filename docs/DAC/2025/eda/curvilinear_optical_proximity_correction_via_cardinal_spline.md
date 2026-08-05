---
title: "Curvilinear Optical Proximity Correction via Cardinal Spline"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Curvilinear Optical Proximity Correction via Cardinal Spline

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA8: Design for Manufacturing and Reliability</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133367">https://ieeexplore.ieee.org/document/11133367</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 曲线光学邻近效应校正，基数样条，掩模优化，掩模规则检查 </p>
</div>


---

## 研究概要
本文提出基于基数样条的曲线型OPC框架CardOP，用控制点表征掩模轮廓，依托光刻仿真迭代修正。推导完整曲线MRC校验方法，支持ILT结果拟合修复违规。金属/通孔版图测试EPE平均降低50%，PVB提升4.2%，大规模电路与ILT混合场景均优于现有曲线OPC与商用Calibre。

## 背景和动机
1. 先进工艺多光束掩模机支持曲线版图，传统曼哈顿OPC图形自由度低，晶圆成像保真度差，工艺窗口窄。
2. 现有贝塞尔曲线OPC需额外辅助控制点，计算开销大，缺少解析曲率、间距类MRC快速校验方案，大量曲线存在制造违规。
3. ILT成像精度高但输出图形MRC违规严重，无法直接用于流片，缺少无损拟合曲线OPC的混合流程。
4. 主流商用OPC仅支持矩形分段，难以表达平滑任意角度曲线，EPE与工艺波动PVB指标偏高。
5. 现有曲线OPC仅适配小版图片段，缺乏大规模tile级电路的稳定优化流程。

## 相关工作
1. 规则/传统模型OPC：仅矩形分段折线，无法生成平滑曲线，光刻成像偏差大。
2. 贝塞尔曲线OPC：曲线生成需增设控制点，运算量大，无成套曲率MRC校验机制。
3 ILT逆光刻：成像精度最优，但输出不规则曲线大量违反掩模制造规则，无法直接投产。
4 RL-OPC/CAMO等AI掩模优化：仍基于折线分段，不支持连续曲线轮廓建模。
5 商用Calibre OPC：不原生支持曲线掩模，曲线处理能力弱，EPE指标劣势明显。

## 本文解决方案
### 1 基数样条掩模表征机制
版图多边形拐角细分长短片段，以分段控制点描述轮廓；基数样条直接穿过控制点，自带张力参数调平滑度，无需额外辅助顶点，解析求导得到曲率、法向向量。
### 2 完整曲线MRC解析校验与修复
基于R树空间索引实现间距/宽度快速检测；鞋带公式计算图形面积；推导样条曲率解析公式，超标控制点沿法向内外移动消除曲率违规，自动修复间距、面积问题。
### 3 梯度驱动曲线OPC迭代修正
基于MEEF建立EPE误差泰勒近似，求解控制点位移；邻域加权平滑移动步长，沿轮廓法向调整曲线，搭配GPU加速光刻仿真与梯度计算。
### 4 ILT-OP混合拟合流程
提取ILT轮廓采样参考点，梯度下降优化基数控制点拟合曲线，拟合后自动执行全套MRC修复，保留ILT高精度同时消除制造违规。
### 5 分层版图处理流水线
先规则插入SRAF辅助图形，多边形细分生成控制点；迭代优化+MRC校验循环，支持通孔、金属层、大规模tile版图统一处理。

## 实验分析
1. 实验环境：45nm工艺，通孔/金属版图片段、OpenROAD大规模tile电路，对比Calibre、RL-OPC、CAMO、贝塞尔曲线OPC。
2. 通孔层：平均EPE仅9.1nm，相较基线降幅最高39.7%，PVB小幅优化。
3. 金属层：平均EPE31nm，较商用工具降低50%，工艺波动PVB提升4.2%。
4. 大规模电路：30×30μm tile测试，EPE违规减少6.4%，PVB降低1.9%，稳定性优于传统OPC。
5. 消融对比：基数样条相较贝塞尔迭代计算提速近一倍；ILT混合方案EPE违规均值1.4，显著优于CircleOpt、DiffOPC。

## 研究启发
1. 基数样条比贝塞尔更适配曲线OP，无需冗余控制点，兼顾精度与计算效率。
2. 曲线掩模必须配套解析MRC校验，仅优化成像不处理制造规则会导致版图无法投产。
3 ILT高精度轮廓可通过样条拟合转化为合规曲线掩模，构建ILT-OP融合流程是先进光刻优化可行路线。
4. 基于轮廓法向的控制点微调策略，可同步改善EPE、P并快速修复各类MRC违规。
5. 曲线OP不能仅局限小版图片段，分层tile处理方案可落地全芯片级掩模优化。
