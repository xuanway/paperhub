---
title: "Synthesis of CFET Cell Library Leveraging Backside Metal Routing"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Synthesis of CFET Cell Library Leveraging Backside Metal Routing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133087">https://ieeexplore.ieee.org/document/11133087</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 互补场效应晶体管，背面金属布线，标准单元库综合，晶体管折叠 </p>
</div>


---

## 研究概要
本文首个在CFET标准单元综合中引入背面BS布线，提出适配堆叠结构的晶体管折叠方案。借助欧拉路径预估CPP下界、动态规划计算前层最小走线，SMT完成单元布线。基于ASAP7基准测试，相较SOTA方案CPP降低1%、M2走线减少45、运行时间缩短19%，且严格遵循SPICE晶体管尺寸约束。

## 背景和动机
1. CFET堆叠PMOS/NMOS大幅缩减面积，但正面M0/M2走线资源紧张，模块布线拥塞严重，传统仅正面布线方案资源不足。
2. 现有CFET单元综合简化晶体管宽度，不匹配SPICE网表真实器件尺寸，电路时序功耗存在偏差。
3. 堆叠CFET顶层器件易遮挡底层扩散接触，常规折叠策略未针对堆叠结构做优化，布线失败率高。
4. 已有单元工具仅使用正面金属，未利用nTSV+BSM背面互联缓解M2资源压力。
5. 缺乏兼顾背面资源、堆叠遮挡、真实器件宽度的布局布线一体化CFET综合框架。

## 相关工作
1. 传统FinFET单元综合：面向非堆叠器件，折叠与放置算法无法适配CFET上下层遮挡约束。
2. 早期CFET综合SMT框架：同时布局布线求解复杂度高，大规模单元扩展性差，且简化晶体管尺寸。
3. 查表式CFET综合SOTA：仅使用正面金属，无背面互联利用机制，M2走线开销大。
4. 背面PDN/SRAM布线研究：仅针对宏单元供电/存储阵列，未落地标准单元级综合流程。
5. ILP/布尔SAT单元布线：仅面向FinFET，未建模CFET M0合并、nTSV跨层约束。

## 本文解决方案
### 1 CFET堆叠感知晶体管折叠
扩展折叠区间，拆分宽顶层器件释放底层布线通道；欧拉图统计奇扩散信号计算CPP下界，筛选最优折叠组合。
### 2 背面资源感知晶体管布局
推导nTSV可放置列判定规则；构建资源约束图，递归DP求解最小前层走线FMRT，优先分配背面通道减少M2占用。
### 3 多约束SMT单元布线求解
基于Z3搭建SMT模型，完整建模器件轨道占用、扩散共享/合并、nTSV无重叠约束；按M2走线、引脚可访问性、总线长字典序优化。
### 4 分层完整综合流水线
输入SPICE网→堆叠折叠筛选→背面感知布局预估→SMT完成单元布线，全程严格遵守原始晶体管宽度参数。

## 实验分析
1. 测试基准：ASAP7 4.5T CFET单元库，覆盖缓冲、逻辑门、锁存器等9类标准单元，对比最新查表CFET综合方案。
2. 核心指标：总CPP下降1%，M2走线总数由20降至11（降幅45%），整体运行时间缩短19%。
3. nTSV预测消融：预判列方案相较全枚举平均提速252倍，布局质量无损失。
4. 资源对比：仅正面布线时M2资源消耗显著上升，AOI/XOR等复杂单元收益最突出。
5. 合规性：全部单元严格匹配SPICE晶体管尺寸，基线方案大量单元放宽器件宽度约束。

## 研究启发
1. 背面金属与nTSV是缓解先进CFET正面M2布线拥塞低成本有效手段，标准单元阶段即可利用。
2. CFET堆叠结构顶层器件遮挡底层接触，折叠算法必须扩展宽顶管拆分策略，不能沿用FinFET折叠逻辑。
3. 晶体管尺寸不可随意简化，贴合SPICE网表才能保证单元时序功耗仿真精度。
4. 先预估布局走线开销再执行SMT布线，可大幅降低求解迭代开销，提升综合效率。
5. 欧拉路径+动态规划组合可快速筛选优质折叠与布局候选，缩小SMT求解搜索空间。