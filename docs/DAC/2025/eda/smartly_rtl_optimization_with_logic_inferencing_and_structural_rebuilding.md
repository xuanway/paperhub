---
title: "smaRTLy: RTL Optimization with Logic Inferencing and Structural Rebuilding"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# smaRTLy: RTL Optimization with Logic Inferencing and Structural Rebuilding

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2510.17251">https://arxiv.org/abs/2510.17251</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多路复用器，优化，RTL，综合，结构 </p>
</div>


---

## 研究概要
本文提出SmaRTLy RTL多路选择树优化工具，包含SAT冗余消除与ADD驱动结构重构两大模块。前者挖掘控制信号逻辑依赖剔除冗余MUX，后者重排case生成多路树减少门数。IWLS/RISC-V基准相较Yosys额外降低8.95%AIG面积，百万门工业电路可多削减47.2%面积。

## 背景和动机
1. RTL中if/case语句会生成大量嵌套多路选择树，是逻辑面积冗余主要来源，主流Yosys仅匹配完全相同控制信号做简化。
2. Yosys无法识别存在逻辑关联的控制信号（如S与S|R），大量隐性冗余MUX无法删除，优化上限低。
3. 传统优化仅删除冗余分支，不重构多路树拓扑，链式、低效MUX层级无法简化，延时与面积开销偏高。
4. 工业级百万门设计含海量选择逻辑，现有MUX优化手段收益微弱，制约PPA指标提升。
5. 缺少兼顾信号逻辑推理与拓扑重组织的一体化多路树优化流程。

## 相关工作
1. Yosys opt_muxtree：仅遍历匹配完全一致控制信号，无法处理逻辑相关控制变量，简化能力有限。
2 真值表类MUX优化：仅适用于小规模树，大规模电路计算开销爆炸，难以落地。
3 BDD/ADD电路化简：多用于全局逻辑综合，未专门针对case生成多路树定制重构启发式。
4 专用FPGA多路重映射：面向硬件架构，不通用ASIC RTL综合场景。
5 AIG重写、重替换算法：全局逻辑变换，未聚焦多路树特有结构冗余。

## 本文解决方案
### 1 基于SAT的MUX冗余消除
1）信号影响判定定理裁剪子图，剔除80%无关门，仅保留存在逻辑关联节点；
2）OR等基础逻辑前置推理缩小未知变量；
3）MiniSAT求解控制信号固定取值，识别隐性冗余多路单元；
4）小规模子图仿真加速，大规模子图启用SAT平衡效率。

### 2 ADD驱动多路树结构重构
1）筛选case生成、单控制信号多路树作为重构对象；
2）代数决策图ADD建模多路输入输出映射；
3）启发式选控制信号最小终端类型，生成最优分层拓扑；
4）重构前评估面积/延时收益，避免重构后开销增大；
5）剥离无用EQ比较门，进一步压缩AIG规模。

### 3 完整协同优化流水线
先SAT推理剔除冗余MUX，再执行多路树重构，两步互补叠加优化收益，可嵌入Yosys综合流程。

## 实验分析
1. 测试环境：C++实现，对比原生Yosys opt_muxtree，采用AIG与门数量作为面积指标。
2. 开源基准：IWLS、RISC-V共10组电路，SmaRTLy平均多减8.95%AIG；SAT模块单独贡献3.57%，重构模块4.39%。
3. 分案例差异：case密集设计重构收益可达24.91%；复杂数据通路SAT简化占优，最高27.79%。
4. 工业测试：百万门级商用电路，相较Yosys额外削减47.2%面积，工业选择逻辑冗余更突出。
5. 完备性：全部优化结果通过等价检查，保证逻辑功能不变。

## 研究启发
1. 多路树冗余不止同源控制信号，信号间布尔依赖是大量隐性冗余根源，必须引入SAT逻辑推理挖掘。
2. 仅删除分支不足以最大化优化，基于ADD重排多路拓扑能从结构层面降低层级与门数。
3 两种优化手段具备互补性：SAT简化缩小子图，让重构算法效果进一步提升。
4 工业电路case选择逻辑占比远高于开源基准，专用MUX优化对量产芯片PPA增益巨大。
5. 针对HDL case生成的特有电路结构定制综合pass，相比全局通用化简可获得更高优化收益。
