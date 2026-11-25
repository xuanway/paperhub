---
title: "BoolE: Exact Symbolic Reasoning via Boolean Equality Saturation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# BoolE: Exact Symbolic Reasoning via Boolean Equality Saturation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.05577">https://arxiv.org/abs/2504.05577</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 等式饱和，精确符号推理，全加器识别，形式验证 </p>
</div>

---

## 研究概要
本文提出BoolE布尔等式饱和符号推理框架，基于egg e-graph构建两套重写规则，设计适配多输入多输出全加器的DAG代价提取算法。针对工艺映射后破碎算术电路，可精准还原精确FA单元。在CSA、Booth乘法器测试，精确FA数量较ABC提升3倍以上，集成RevSCA验证工具后最高提速数千倍。

## 背景和动机
1. 工艺映射、逻辑优化会打散加法树结构，传统基于切枚举、结构哈希工具仅能识别NPN等价单元，无法获取功能完全一致的精确FA。
2. 图神经网络类推理工具存在概率误差，无形式化正确性保证，不适合乘法器形式验证等严苛场景。
3. 现有工具仅做静态结构匹配，无法遍历所有布尔等价表达式，大量算术单元碎片无法恢复。
4. 标准e-graph仅支持单输出算子，难以处理FA这类三输入双输出复合结构，缺少专用提取方案。
5. 缺少分层重写策略，大规模AIG网表饱和推理内存、耗时开销过高，可扩展性差。

## 相关工作
1. ABC切枚举推理：依赖固定电路拓扑，工艺映射后识别率暴跌，仅支持NPN等价单元，无精确功能保证。
2. Gamora图神经网络推理：依靠电路特征训练，存在识别错误，不具备形式化完备性。
3. 传统e-graph优化工具：仅面向单输出逻辑表达式，未适配FA多输出算术结构。
4. 算术电路代数验证工具（RevSCA）：依赖人工提取加法单元，无自动化恢复手段，高位乘法极易超时。
5. 基础布尔重写方案：规则单一，未针对MAJ、XOR构成的加法单元定制专用转换规则。

## 本文解决方案
### 1 拓扑序e-graph增量构建
解析AIG网表，按从叶子到根的拓扑顺序插入E节点，完整保存与门、非门依赖关系，搭建底层等价图存储结构。
### 2 两段式分层重写规则集
R1基础布尔规则（交换律、德摩根等）做全局等价扩张；R2定制MAJ/XOR专用转换规则，分多轮迭代饱和，冗余等价节点自动剔除。
### 3 多输出FA扩展e-graph结构
新增FA复合E节点，搭配FST/SND投影算子拆分和、进位两路输出，统一FA内部XOR/MAJ等价类，完整保留双输出结构完整性。
### 4 DAG感知最小代价提取算法
定义以精确FA数量最大化的代价函数，自底向上遍历e-class，规避子图重复计数，选出包含最多精确加法单元的最优表达式树。
### 5 标准化工具集成接口
输出优化后AIG，无缝对接ABC综合、RevSCA2.0代数验证工具，自动消除验证多项式爆炸问题。

## 实验分析
1. 实验环境：Xeon服务器，7nm ASAP工艺映射CSA/Booth乘法器，基线ABC、Gamora，指标FA识别数、验证耗时。
2. 单元识别：工艺映射电路中，BoolE精确FA数量是ABC的3.53倍（CSA）、3.01倍（Booth），NPN识别覆盖率达84%~93%。
3. 可扩展性：128位百万节点乘法器完整推理耗时50分钟以内，规模增长平缓可控。
4. 形式验证增益：24位乘法验证从32402秒降至0.07秒，28位以上基线直接超时，BoolE可完成128位验证。
5. 消融实验：分层R1+R2重写、FA双输出扩展、DAG代价提取三大模块缺一不可，任一关闭识别率大幅下滑。

## 研究启发
1. 仅依靠静态拓扑匹配无法应对工艺打散的算术电路，等式饱和遍历等价空间是恢复高层字级单元核心思路。
2. 通用e-graph需扩展多输出复合算子结构，才能适配加法器等数据通路基础模块。
3. 区分NPN等价与精确功能单元，形式验证场景必须以完全等价FA作为化简依据。
4. 分层迭代重写兼顾推理精度与运行开销，轻量规则剪枝可显著提升大规模网表可扩展性。
5. 符号推理是代数验证的前置关键环节，高效单元恢复可实现数个量级的验证加速。
