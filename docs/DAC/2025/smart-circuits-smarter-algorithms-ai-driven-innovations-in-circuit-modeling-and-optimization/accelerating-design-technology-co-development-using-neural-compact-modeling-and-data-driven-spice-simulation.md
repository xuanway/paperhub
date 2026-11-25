---
title: "Accelerating design-technology co-development using neural compact modeling and data-driven SPICE simulation"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Accelerating design-technology co-development using neural compact modeling and data-driven SPICE simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133177">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133177</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经网络紧凑模型，数据驱动SPICE模型，设计与工艺技术协同优化 </p>
</div>


---

## 研究概要
本文提出融合神经紧凑模型(NCM)与DataSPICE数据驱动仿真的DTCO协同优化框架。基于迁移学习实现器件电气目标快速重定向，搭配W/L/T插值、工艺偏移修正、版图效应子电路适配。15k晶体管电路验证，模型开发周期缩短95%，仿真精度超98.6%，无收敛与性能损失。

## 背景和动机
1. 先进工艺DTCO需要工艺与电路并行迭代，传统BSIM等方程模型参数提取(MPE)耗时数周，迭代反馈极慢。
2. 传统自动MPE依赖遗传/深度学习调数百参数，参数范围、顺序难以定义，精度与效率难以兼顾。
3. 现有神经紧凑模型仅完成I-V拟合，缺少面向工业的重定向、工艺角、蒙特卡洛、版图效应完整设计链路。
4. 已有NCM多基于Verilog-A接入SPICE，无法兼容现有分仓、变异、LDE工业设计流程，落地性差。
5. 工艺小幅改动后需要完整重训NCM，仅少量电气目标更新时资源浪费严重，缺少轻量化微调方案。

## 相关工作
1. 传统BSIM参数自动提取：遗传算法、基础DNN调参，依赖海量参数，迭代周期长、泛化弱。
2. 基础神经网络紧凑模型：仅拟合I/V/CV曲线，部分支持导数拟合，但无面向工艺变更的重定向微调。
3. 迁移学习NCM：仅针对新型器件加速训练，未适配量产工艺电气目标快速更新场景。
4. Verilog-A型NCM仿真方案：接入SPICE成本高，不支持W/L分仓、工艺变异、版图效应标准流程。
5. 数据驱动SPICE工具：仅支持静态数据集，缺少插值、偏移修正，无法适配工艺迭代动态模型需求。

## 本文解决方案
### 1 双阶段迁移学习NCM重定向框架
第一阶段预训练DNN学习基准器件全偏置I-V特性，损失融合ID、跨导gm、输出电导gds；第二阶段冻结底层权重，新增隐层基于少量ET电气目标微调，防止过拟合，全区间精度>95%。
### 2 DataSPICE数据驱动SPICE仿真底座
基于PrimeSim D2D，直接使用NCM生成数据集替代方程模型；三维W/L/T线性插值补齐未采样器件尺寸，完整兼容现有分仓设计流程。
### 3 工艺变异数据偏移修正机制
设计dVth、dIds偏移参数，通过数据集平移快速生成快慢工艺角；基于偏移分布实现蒙特卡洛统计仿真，与BSIM统计分布R²>0.9。
### 4 版图依赖效应(LDE)子电路适配
子电路封装NCM数据集+外接可调Rext电阻，适配多指器件接触电阻变化，多指逆变器时延误差控制在1%以内。
### 5 完整DTCO迭代工作流
工艺变更输入少量ET目标→迁移微调NCM生成数据集→DataSPICE插值/变异/LDE仿真电路，快速反馈时序性能给工艺工程师。

## 实验分析
1. 实验对象：29级环形振荡器、15k管NAND Flash页缓冲；对比传统BSIM SPICE。
2. 模型迭代效率：同等6个电气目标场景，传统MPE近100小时，NCM微调仅0.5小时，周期缩减95%。
3. 电路精度：常规PVT角仿真时序精度99%以上；插值未知V/T条件最低98.6%，波形高度吻合。
4. 仿真耗时：无需插值场景运行速度为传统94%~96%；插值场景小幅上升至102%~103%，无收敛故障。
5. 消融验证：多ET微调全区间精度稳定；插值误差<3%；MC仿真Vth/I_D相关系数分别0.99/0.91；多指LDE校正误差<1%。

## 研究启发
1. 迁移学习可仅用少量电气目标快速更新器件模型，大幅缩短DTCO迭代闭环，解决传统MPE周期瓶颈。
2. 数据集驱动SPICE比Verilog-A NCM更易兼容工业成熟分仓、工艺变异、版图效应设计流程。
3. NCM不能仅拟合ID曲线，损失函数必须纳入gm、gds导数才能保证亚阈值/饱和全区间一致性。
4. W/L/T插值、电压电流偏移修正是数据模型落地量产设计的关键配套手段。
5. 面向先进工艺协同开发，神经模型+数据驱动仿真是替代传统BSIM长周期参数提取的高效路线。
