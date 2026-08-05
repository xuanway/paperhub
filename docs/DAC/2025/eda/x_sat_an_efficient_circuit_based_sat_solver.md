---
title: "X-SAT: An Efficient Circuit-Based SAT Solver"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# X-SAT: An Efficient Circuit-Based SAT Solver

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132604">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132604</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 布尔可满足性，等价性检查，基于电路的SAT，电子设计自动化 </p>
</div>


---

## 研究概要
本文提出面向算术电路的电路型SAT求解器X-SAT。设计结构消元算法将AIG转为XLG图大幅缩减变量，改进VSIDS得到XVSIDS分支策略适配异或密集电路。在算术、非算术两类基准测试，算术电路PAR2相较Kissat提升1.36倍，优于现有电路求解器abc-cirsat 38.26倍，综合求解效率领先。

## 背景和动机
1. 传统CNF型SAT需把电路转合取范式，丢失门级结构信息，算术电路含大量XOR，转换后子句爆炸、求解缓慢。
2. 现有电路SAT仅直接基于AIG运算，未针对性合并多输入门，变量数量多，搜索开销巨大。
3. J-frontier等传统电路分支启发式对加法器、乘法器等XOR密集算术电路适配性差，冲突回溯效率低。
4. 主流Kissat等CNF求解器虽通用，但处理大规模算术等价检查实例耗时极高，缺少电路原生优化手段。
5. 缺少同时兼顾图化简与XOR感知分支的一体化电路SAT框架，难以支撑高频CEC、SAT-Sweep迭代场景。

## 相关工作
1. CNF类CDCL求解器（MiniSAT/Glucose/Kissat）：依赖范式转换，丢失电路拓扑，算术实例性能瓶颈明显。
2. 初代电路SAT（QuteSAT）：实现电路原生BCP，但无图化简优化，分支启发式通用性不足。
3. abc-cirsat：基于AIG原生电路求解，未做门合并消元，无XOR专属变量打分策略，算术电路速度差距大。
4. 逻辑综合前置重写方案：仅预处理电路，未嵌入CDCL求解核心做分支优化。
5. J-frontier分支策略：经典电路决策启发式，但对异或密集算术电路无针对性加权机制。

## 本文解决方案
### 1 XLG电路结构消元化简
先识别所有XOR门生成XAG；设计消分打分大顶堆，合并单输出多输入门为LUT，限制LUT输入上限7，将AIG转化XLG图，算术电路变量平均减少61.39%。
### 2 XVSIDS异或感知分支启发式
在VSIDS基础上修改打分更新规则：冲突分析时不仅提升冲突变量权重，同步小幅增加相邻XOR门变量分值，强化算术电路局部搜索倾向性。
### 3 完整X-SAT求解流水线
输入AIG→结构消元生成XLG→支持J-frontier/XVSIDS双分支选择→原生电路BCP、冲突分析、子句学习、重启全套CDCL流程，无需转CNF。
### 4 电路原生BCP与冲突分析
直接在XLG门网络传播赋值，规避CNF转换开销，支持LUT、XOR混合图的约束推导，适配CEC miter电路求解。

## 实验分析
1. 测试基准：22组工业算术电路、13组ISCAS/ITC非算术电路，2000s时限，PAR2作为评价指标。
2. 算术电路性能：X-SAT PAR2均值75.19，优于Kissat（102.21），是abc-cirsat速度38.26倍。
3. 非算术电路：略慢于Kissat，但大幅超越Glucose、MiniSAT、abc-cirsat。
4. 消融实验：关闭结构消元后两类电路PAR显著恶化；XVSIDS相较VSIDS/J-frontier算术实例提速最高19.39倍。
5. 通用性：同时适配算术数据通路与普通组合电路，可嵌入ABC完成等价检查、SAT-Sweep流程。

## 研究启发
1. 算术电路海量XOR是性能瓶颈，不能照搬通用CNF求解器，必须保留电路拓扑并做门级图化简。
2. 变量消元合并LUT可从根源压缩搜索空间，是电路SAT相比CNF范式天然优势。
3. 分支启发式需要贴合电路门结构，针对XOR邻域加权能大幅提升算术实例冲突回溯效率。
4. 电路原生CDCL无需范式转换，适合等价检查等反复调用EDA场景，迭代开销更低。
5. 结构化简与定制分支策略可叠加增效，二者缺一不可，构成电路SAT核心优化组合。