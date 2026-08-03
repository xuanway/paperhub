---
title: "HPIM-NoC: A Priori-Knowledge-Based Optimization Framework for Heterogeneous PIM-Based NoCs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# HPIM-NoC: A Priori-Knowledge-Based Optimization Framework for Heterogeneous PIM-Based NoCs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132638">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132638</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 异构，存内处理，片上网络，仿真，架构搜索</p>
</div>



---

## 研究概要
针对异构PIM片上网络缺少专用仿真与架构搜索工具的问题，本文提出HPIM-NoC协同框架，集成异构PIM-NoC仿真器与先验知识驱动的三段式模拟退火搜索流程，搭配查表、降低仿真频次加速搜索，并定制布局算法。测试显示异构方案FoM最高降低37.41%，搜索速度提升最高2.96倍。

## 背景和动机
1. 传统冯诺依曼架构存在存储墙，PIM可就近计算降低数据搬运；异构PIM-NoC融合SRAM/RRAM单元，PPA表现优于同构架构，但设计空间爆炸，人工优化不可行。
2. 现有PIM仿真器仅支持同构内核，未建模片上网络传输与计算流水线；通用NoC仿真无法适配CNN层间数据依赖，仿真精度不足。
3. 现有架构搜索工具仅优化任务映射，或仅小范围异构探索，无法完整遍历PIM类型、阵列尺寸等硬件参数，缺少一体化仿真+搜索平台。

## 相关工作
1. PIM仿真工具：MNSIM、DNN+NeuroSIM仅支持同构PIM，无片上网络协同仿真；SIAM面向同构PIM-NoC，不兼容混合存储内核。
2. 通用片上网络仿真：Booksim基于随机注入流量建模，未适配神经网络分层数据流，延迟仿真误差大。
3. PIM架构搜索：PIM-HLS仅调度任务映射；Gibbon面向同构PIM；AIG-CIM仅支持少量SRAM异构配置，硬件参数搜索范围受限。

## 本文解决方案
### 1. 异构PIM-NoC协同仿真器
- 基于MNSIM扩展异构内核建模，设计回溯算法完成多规格PIM核的负载分配；
- 改造Booksim构建CNN专属流量模型，计算层间数据包注入速率；
- 支持计算/传输全流水线共仿真，取二者最大值作为层总延迟，提升仿真准确度。
### 2. 先验知识三段式架构搜索框架
- 预计算SRAM/RRAM内核PPA变化趋势作为先验，分同构初筛、层间异构、层内异构三阶段缩窄搜索空间；
- 定制模拟退火算法，设计多类配置修改算子，配套容量校验微调保证硬件合法；
- 提出FoM综合指标统一评价面积、功耗、延迟。
### 3. 双重加速与布局优化
- 预存所有内核PPA查表复用，减少重复内核仿真；降低迭代中NoC仿真调用频次；
- 力导向布局算法优化异构内核摆放，缩短互连线、减小总面积。

## 实验分析
1. 仿真正确性：与MNSIM对标，无/内核流水线模式误差极小，新增计算-传输全流水线可显著降低推理延迟。
2. 搜索加速效果：查表+间隔仿真双重优化下，AlexNet/VGG8/ResNet18搜索时间分别提速2.12×、2.17×、2.96×。
3. 架构优化收益：对比同构PIM-NoC，ResNet18在三类FoM权重下指标分别降低1.18%、16.94%、37.41%，层内异构优化效果最优。
4. 布局结果：力导向布局得到最短总线长，布线交叉极少，芯片面积得到优化。

## 研究启发
1. 异构存算芯片设计需一体化仿真+搜索工具，单独仿真或调度工具无法兼顾硬件全维度参数优化。
2. 利用硬件PPA变化先验分阶段搜索，可大幅压缩超大异构设计空间，规避暴力遍历的高耗时问题。
3. 仿真加速可分层优化：内核级预查表、片上网络级降低仿真频次，双重手段叠加提速效果显著。
4. 存算一体加速器不能只关注算力阵列，片上网络通信、芯片布局会显著影响整体PPA，需协同优化。
5. 多目标评价采用自定义FoM综合指标，可灵活适配延迟、功耗、面积不同设计约束需求。