---
title: "POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "power-side-channel"
  - "explainable-ai"
  - "masking"
  - "hardware-security"
---

# POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132622">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132622</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 功耗侧信道分析与缓解，硬件安全，可解释人工智能 </p>
</div>

---

## 研究概要
本文提出POLARIS可解释AI硬件侧信道防护框架，无需TVLA反复仿真，采用无监督方式自动生成电路训练集，基于SHAP提取电路专属掩码规则，自适应筛选泄漏门插入掩码门。在ISCAS/EPFL等基准测试，相较VALIANT平均泄漏降幅更高，运行速度提升6倍，面积、功耗、时序开销显著降低。

## 背景和动机
1. 传统VALIANT、Karna等防护EDA工具依赖TVLA海量功耗轨迹仿真，大型电路仿真耗时极高，扩展性差，仅能使用固定人工掩码规则，适配性弱。
2. 现有DL/LLM泄漏评估AI工具存在训练数据稀缺、模型不可解释、易受投毒攻击缺陷，无法输出硬件可落地掩码规则。
3. 缺乏自动合成硬件训练样本的方案，不同电路拓扑需重新采集大量功耗数据，工程落地成本高。
4. 掩码防护普遍存在面积、功耗、延迟三重开销膨胀问题，现有工具无法精准筛选高泄漏关键门，造成资源浪费。
5. AI模型决策黑盒，工程师无法理解电路泄漏判定逻辑，难以校验掩码方案可靠性。

## 相关工作
1. TVLA传统防护流（VALIANT、CASCADE、Karna）：依靠t检验逐门评估泄漏，固定人工规则，大型电路仿真效率极低。
2. 深度学习泄漏评估（DL-LA）：依赖外部功耗数据集，无可解释能力，易遭受对抗样本攻击。
3. LLM硬件分析（Netlist Whisperer）：基于布尔方程推理，训练成本高，无法生成掩码部署方案。
4. 基础掩码电路：DOM、掩码AND/OR门，仅提供基础加密单元，缺少自动化插入调度算法。
5. XAI通用算法（SHAP、LIME）：仅用于软件模型，未适配门级硬件网表泄漏场景。

## 本文解决方案
### 1 无监督合成训练数据集
将网表转为图结构，随机插入掩码门并TVLA计算泄漏变化，以70%泄漏下降为阈值自动标注好坏样本，提取门局部拓扑特征构建训练集，无需外部实测功耗数据。
### 2 AdaBoost泄漏预测模型
对比随机森林、XGBoost，选用AdaBoost作为核心分类器，搭配SMOTE处理样本不平衡，精准预测单门泄漏贡献度。
### 3 SHAP可解释规则提取
通过SHAP值量化每个电路拓扑特征对泄漏的影响，生成工程师可读的掩码/不掩码判定规则，消除AI黑盒问题。
### 4 自适应掩码插入算法
依据模型预测分数降序筛选高泄漏门，按需插入掩码逻辑，支持50%/75%/100%多档掩码规模，平衡安全与硬件开销。
### 5 ASIC标准设计流集成
完整嵌入Synopsys DC综合流程，输出掩码后门级网表，兼容主流仿真工具，可拓展至FPGA LUT架构。

## 实验分析
1. 实验基准：ISCAS-85训练集，EPFL/MIT大型电路测试，掩码门上限200，邻域特征范围7门。
2. 模型对比：AdaBoost平均泄漏降低54.09%，优于XGBoost(51.49%)、随机森林(41.97%)。
3. 性能对比：同等防护强度下，POLARIS速度是VALIANT的6倍；仅50%掩码门即可超越VALIANT全掩码效果。
4. 硬件开销：相比VALIANT，平均面积缩减34.61%、功耗降低40.54%、时序延迟缩短33.25%。
5. 防护效果：原始电路大量门TVLA指标超4.5泄漏阈值，POLARIS掩码后绝大多数门落在安全区间。

## 研究启发
1. 硬件侧信道防护无需依赖海量TVLA仿真，可解释AI能以拓扑特征替代功耗轨迹完成泄漏预判。
2. 自动合成硬件样本能解决EDA领域训练数据稀缺痛点，大幅降低电路安全验证成本。
3. SHAP等可解释算法适配门级网表，可输出硬件工程师可复用掩码规则，提升方案可信度。
4. 选择性掩码远优于全局全门替换，精准定位高泄漏节点可大幅削减硬件三重开销。
5. 安全EDA工具应兼顾安全强度、运行效率、硬件成本三指标，XAI是平衡三者的有效路径。