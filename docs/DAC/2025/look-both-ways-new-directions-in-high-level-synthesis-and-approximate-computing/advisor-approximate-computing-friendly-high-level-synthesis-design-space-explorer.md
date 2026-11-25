---
title: "ADVISOR: Approximate Computing-frienDly High-LeVel Synthesis DesIgn Space ExplORer"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# ADVISOR: Approximate Computing-frienDly High-LeVel Synthesis DesIgn Space ExplORer

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132450">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132450</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高层次综合，设计空间探索，近似计算 </p>
</div>


---

## 研究概要
本文提出ADVISOR近似友好型HLS设计空间探索框架，设计AFI近似友好指数快速筛选易做近似的硬件微架构，采用模糊变异遍历pragma组合，分两阶段执行：AFI预筛选+分层近似优化。DSP/图像基准测试，相比暴力全近似搜索平均提速68倍，面积缩减效果接近穷尽遍历方案。

## 背景和动机
1. 近似计算依靠误差容忍换取面积/功耗收益，但不同HLS编译pragma生成硬件的近似潜力差异巨大，资源共享型电路几乎无法做近似。
2. 传统DSE流程需对每一套pragma组合完整近似仿真，生成、仿真、误差评估全流程开销极高，大规模设计遍历不可行。
3. 现有近似HLS方法固定RTL输入，未从行为级源头筛选天然适配近似的硬件拓扑，优化上限受限。
4. 近似手段分为V2V/V2C变量替换、近似运算单元两类，缺少分层贪心执行策略，面积压缩收益无法最大化。
5. 缺乏轻量化静态评估指标，只能依靠完整仿真才能判断电路近似潜力，探索效率极低。

## 相关工作
1. 近似HLS优化(AxHLS/ABACUS等)：仅针对固定调度/精度做近似，无设计空间筛选机制，依赖全量仿真评估。
2. RTL层自动近似(AutoAX)：以给定Verilog为输入，无法在HLS行为阶段提前筛选高潜力架构。
3. HLS标准DSE：仅优化面积-时延帕累托前沿，不面向近似收益做定向搜索。
4. 近似算术单元库(EvoApproxLib)：仅提供替换组件，缺少配套架构筛选与分层近似流程。
5. 跨层近似方法：覆盖HLS至门级，但未解决预筛选加速DSE的核心效率痛点。

## 本文解决方案
### 1 两阶段完整ADVISOR自动化流程
阶段一：近似友好DSE，模糊变异生成pragma组合，静态计算AFI指数筛选高潜力RTL；阶段二分层近似优化，先执行收益更大V2V/V2C替换，再替换近似运算单元。
### 2 AFI近似友好静态评估指标
依据近似类型定制计算规则：V2V/V2C统计数据通路内部信号数；FU近似统计独立运算单元；电压缩放使用时序正裕量，仅解析RTL无需仿真，计算极快。
### 3 模糊变异DSE搜索策略
每次仅变异10%编译pragma，以最大化AFI为目标函数，约束最大面积、时延上限，连续多轮无提升则终止搜索，输出AFI排名靠前的候选架构。
### 4 分层贪心近似优化
第一步仿真提取信号均值/方差/相关性，优先靠近输出节点做V2V/V2C常量替换，误差超限则回退；第二步遍历未共享运算单元，贪心替换低误差近似乘加器。
### 5 多误差阈值适配机制
支持MAPE信号处理、PSNR图像两类误差指标，可配置最大误差上限，自动平衡硬件面积缩减与输出失真程度。

## 实验分析
1. 实验环境：Nangate 45nm工艺，CyberWorkBench HLS、DC综合、VCS仿真；基准包含FIR/FFT/Sobel等6类DSP/图像电路，对比暴力NAIVE全遍历方案。
2. 效率提升：ADVISOR(取Top1 AFI)平均提速66×，取Top N候选提速25×，整体平均提速68倍。
3. 面积优化：无约束场景平均面积缩减48%~66%；施加面积/时延上限后缩减幅度降至31%~37%。
4. 消融对比：仅取最高AFI架构效果仅比遍历全部候选低2%~3%，兼顾速度与优化收益。
5. 误差鲁棒：放宽最大误差阈值(MAPE20%/PSNR10db)可进一步提升硬件压缩比例，各类应用均可控制误差在约束内。

## 研究启发
1. HLS行为阶段的编译pragma直接决定电路近似潜力，资源共享强架构应提前过滤，无需浪费仿真算力。
2. 轻量化静态AFI指标可替代完整近似仿真做预筛选，大幅削减DSE时间开销，且精度损失极小。
3. V2V/V2C变量常量替换比单纯近似运算单元带来更大面积收益，近似优化应分层、优先执行拓扑裁剪类手段。
4. DSE搜索无需穷尽所有组合，小幅模糊变异迭代即可收敛至近似最优硬件微架构。
5. 面向近似的HLS探索与传统面积时延DSE目标不同，需要专用评价指标与定向搜索目标。