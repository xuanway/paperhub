---
title: "Efficient Rectification Signal Validation for Optimal Functional ECO Patch Generation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Efficient Rectification Signal Validation for Optimal Functional ECO Patch Generation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133214">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133214</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 工程变更指令，修正点，量词消除 </p>
</div>


---

## 研究概要
本文面向功能ECO补丁优化，提出高效修正信号验证算法。通过量词消去构造近似证明模型，将2QBF问题转化高效1QBF求解；设计可疑得分筛选候选、信号集分组排序与模拟退火早停策略。CAD竞赛基准测试，相较Cadence商用Conformal ECO，补丁规模平均缩减44%，仅需少量补丁生成调用即可得到最优解。

## 背景和动机
1. 现有综合式ECO依赖固定修正信号集合，仅枚举局部候选，难以遍历全部有效信号组合，无法得到最小补丁。
2. 多输出电路修复问题属于Π₂P完全2QBF问题，直接求解全部信号组合算力爆炸，传统BDD方法内存超时严重。
3. 补丁生成模块计算开销极高，反复调用多组候选会带来巨大时间成本，缺少排序筛选机制减少调用次数。
4. 商用ECO工具仅单一搜索修正点，未批量评估多组信号方案，生成补丁冗余门电路多。
5. 缺乏近似可满足模型快速过滤无效修正组合，全部候选均调用补丁引擎，流程效率低下。

## 相关工作
1. 故障模型ECO：仅适配单门局部改动，全局逻辑变更场景失效。
2. 扫描式ECO：依赖电路结构合并，无法处理case语句类大范围功能修改。
3. 单/多插值SAT-ECO：修正信号候选选取随意，无批量验证最优组合机制。
4. BDD真值表ECO：大规模电路存储与计算开销爆炸，可扩展性差。
5. Cadence Conformal商用ECO：仅单一修正方案生成，不遍历多候选，补丁冗余度高。

## 本文解决方案
### 1 可疑得分候选筛选机制
基于反例修复能力、信号稀有度、输入距离三维指标计算SuspiciousScore，拓扑遍历快速筛选高价值修正信号，缩减候选集合规模。
### 2 近似证明模型H(x,s)
利用单变量量词消去与单偏性化简，将原2QBF验证问题转为1QBF SAT求解；构造选择变量切换修正信号激活状态，大幅降低求解复杂度。
### 3 双SAT协同验证流程
SAT1枚举修正信号组合，SAT2校验电路等价；通过不可满足核精简有效信号集，添加阻塞子句避免重复遍历全部组合。
### 4 信号集分组与分层排序
相似度聚类合并近似修正集合；以信号输入层级总和排序，优先调用更靠近输入、规模更小的候选组合。
### 5 模拟退火早停补丁生成
按序生成补丁，连续多次无优化则终止搜索；支持单输出/分组输出/全部输出三类切换修复策略，减少昂贵引擎调用次数。

## 实验分析
1. 实验环境：Xeon 128G服务器，2017 CAD竞赛基准，对比Cadence Conformal ECO，补丁生成采用开源runeco工具。
2. 补丁质量：相比商用工具补丁规模平均下降44%，多数最优解仅需1~4次补丁生成调用。
3. 运行耗时：总耗时约为Conformal的4.9倍，98%耗时集中在补丁生成模块，验证阶段开销极低。
4. 消融对比：分组排序策略单独可带来12%补丁优化收益；本文修正信号集输入第三方引擎仍优于商用工具26%。
5. 局限：依赖结构重写的特殊测试用例无法求解，可兼容多数常规功能ECO场景。

## 研究启发
1. 2QBF类EDA验证问题可通过量词消去+近似模型转为1QBF SAT求解，显著提升大规模电路可扩展性。
2. 修正信号不能随机选取，基于反例修复能力的打分机制可提前过滤低价值候选，缩小搜索空间。
3. 批量枚举多组修正信号、择优生成补丁是缩减门级改动的核心思路，商用单方案ECO存在优化上限。
4. 补丁生成引擎开销远高于信号验证，聚类排序+早停策略能大幅减少引擎调用次数，平衡QoR与速度。
5. 近似下近似证明模型存在少量漏解，但工程场景下失效概率极低，可换取巨大效率提升。