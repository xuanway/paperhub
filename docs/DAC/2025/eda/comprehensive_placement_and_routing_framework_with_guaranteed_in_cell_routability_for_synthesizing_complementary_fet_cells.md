---
title: "Comprehensive Placement and Routing Framework with Guaranteed In-Cell Routability for Synthesizing Complementary-FET Cells"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Comprehensive Placement and Routing Framework with Guaranteed In-Cell Routability for Synthesizing Complementary-FET Cells

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132738">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132738</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 标准单元，CFET，布局，布线，可布线性 </p>
</div>

---

## 研究概要
本文面向3nm以下CFET堆叠器件，提出完整单元布局布线框架。设计BFS分块预处理、集成部分布线的SMT放置算法、分阶段金属布线流程。基于ASAP7基准测试，30款单元中7款取得最小宽度，其余单元M2轨道用量与金属总长最优，兼顾可布线性与布局密度。

## 背景和动机
1. CFET垂直堆叠NMOS/PMOS大幅缩减单元高度，但M1垂直轨道稀缺、多层布线规则严苛，单元内部布线极易出现DR违例。
2. 现有SMT协同布局工具建模变量规模庞大，大晶体管单元求解速度极慢，可扩展性差。
3. 搜索类CFET放置算法未耦合布线约束，布局完成后易出现不可布线问题，需反复迭代修正。
4. 现有流程放置与布线割裂，引脚位置未全局优化，导致M2资源浪费、总金属线长偏高。
5. M0层布线规则相互冲突，单一调整易触发多条DR违规，缺少人工启发式合法布线方案。

## 相关工作
1. TVLSI 2021 SMT同步布局布线：完整建模多层金属，变量数量爆炸，大单元求解耗时数千秒。
2. DAC 2024 搜索式CFET放置：仅考虑布线预估，无内嵌可布线约束，后置布线易失败。
3. 传统FinFET单元生成工具：单层器件架构，不兼容CFET垂直堆叠与M1稀疏轨道架构。
4. 通用SMT标准单元工具：未适配CFET专用MAR/EOL/PRL等多层布线设计规则。
5. 简化分块布局方法：分块后布局质量衰减严重，缺少扩散共享优化排序策略。

## 本文解决方案
### 1 可扩展预处理流程
晶体管折叠统一扩散宽度；基于BFS电路图分块拆分大单元；启发式排序分块，最大化扩散共享、减少跨块长线，降低分块带来的质量损失。
### 2 内嵌部分布线SMT放置算法
抽象M1/M2为超级顶点压缩模型规模；多商品流建模M0局部布线，理论证明满足M0合法、单轨道单网即可保证全局可布线；字典序多目标优化，优先最小单元宽度，再缩减M2用量与线长。
### 3 分阶段渐进金属布线
人工启发式M0布线，用补丁单元解决MAR违例；ILP求解M1/M2路由，将M0过孔作为M1引脚，枚举子网候选路径完成合法布线。
### 4 多层CFET规则约束系统
完整嵌入MAR、EOL、通孔、并行走线等CFET专属设计规则，在SMT与ILP求解阶段同步约束规避DR。
### 5 多目标可调优化机制
可加权平衡单元宽度、M2轨道、总金属长度，满足高密度或低寄生两类设计需求。

## 实验分析
1. 实验环境：Intel i7工作站，Z3 SMT/ILP求解器，ASAP7 7nm CFET标准单元基准，对比DAC24、TVLSI21两套主流生成器。
2. 单元宽度：30款测试单元内7款实现业界最小单元宽度，整体平均宽度降低3%。
3. 布线指标：同宽度单元下M2轨道用量平均缩减35%，加权金属总长平均缩短13%。
4. 运行效率：DFF、FA等大单元借助分块预处理，运行速度远优于TVLSI21；多数中小单元耗时低于30秒。
5. 大单元鲁棒：新增32管SDF超大单元，竞品无对应结果，本文框架稳定生成合规布局，M2资源占用更低。

## 研究启发
1. CFET布局必须在放置阶段内嵌布线约束，后置布线修复成本极高，内嵌M0局部模型可从源头保证可布线性。
2. 超级顶点抽象能大幅削减SMT变量规模，解决大单元求解瓶颈，显著提升工具可扩展性。
3. 单元宽度、M2轨道、金属长度存在权衡关系，多目标字典序优化可适配不同芯片密度需求。
4. M0层是布线DR重灾区，人工启发+补丁单元的合法化方案可高效化解多规则冲突。
5. BFS分块搭配扩散共享排序策略，在不明显损失布局质量前提下，大幅降低求解计算开销。