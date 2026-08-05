---
title: "Graph-Guided Transfer Learning to Boost the Efficiency of System-Level Optimization of Analog/Mixed-Signal Circuits"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Graph-Guided Transfer Learning to Boost the Efficiency of System-Level Optimization of Analog/Mixed-Signal Circuits

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132596">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132596</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合信号电路设计自动化，系统级优化，强化学习，迁移学习 </p>
</div>


---

## 研究概要
本文提出图引导迁移学习模拟混合信号系统级优化框架，融合GAT与DDPG强化学习，设计三层电路图相似度判定规则实现跨拓扑知识迁移。以连续时间ΔΣ ADC为验证对象，相比传统算法功耗最高降低40%；跨架构迁移可减少11倍仿真次数，最优功耗结果提升12.4%。

## 背景和动机
1. 模数混合系统优化空间庞大，SNDR、功耗等指标相互冲突，NSGA-II、贝叶斯等传统优化采样效率低，大量Simulink仿真耗时极高。
2. 现有电路RL迁移学习仅支持拓扑高度近似电路（同阶运放等），无法在结构差异较大的ADC架构间复用训练知识。
3. MLP类强化学习无法捕捉积分器、DAC等子块的层级耦合关系，难以建模信号路径全局性能约束。
4. 主流ΔΣ设计工具仅基于理想器件建模，忽略Jitter、DAC失配等非理想效应，优化参数流片不可实现。
5. 不同阶数、不同反馈拓扑ADC变量维度不一致，现有网络无法完成参数知识跨架构复用。

## 相关工作
1. 进化/贝叶斯优化（NSGA-II、DE、BO）：无学习迁移能力，每次设计从零采样，仿真开销巨大。
2. GCN-RL晶体管尺寸优化：仅器件级，迁移仅限同工艺近似电路，不适用系统级ADC拓扑。
3. MLP-RL模拟优化：无法编码电路图结构，难以建模子块依赖关系，优化上限低。
4. Delta-Sigma MATLAB工具箱：基于理想模型，不兼容实际非理想因素，生成参数无法满足实测指标。
5. KATO迁移贝叶斯：仅支持高度相似拓扑，跨异构ADC无有效的知识复用方案。

## 本文解决方案
### 1 GAT-DDPG系统级强化学习优化器
将ADC子块建模为图节点，信号通路为边，5层GAT作为Actor/Critic捕获模块耦合；定制分段奖励函数，优先满足SNDR、SFDR等硬性指标再最小功耗；全局OSR、积分器GBW等统一为连续动作空间。
### 2 三层电路图相似度判别机制
依次判定滤波器阶、子块依赖关系、信号通路模块顺序，区分可迁移/不可迁移架构，自动决策是否复用预训练模型。
### 3 维度兼容迁移网络结构
预训练GAT特征与ANN分支拼接，适配不同架构设计变量维度差异，实现3阶→4阶、CIFF↔CRFB异构ADC知识迁移。
### 4 带非理想效应ADC系统仿真模型
集成DAC抖动、元件失配、过量环路延迟等真实工艺非理想项，构建积分器/DAC/量化器分层功耗解析模型，保证优化结果可流片。
### 5 完整优化流水线
架构图编码→GAT-RL迭代仿真→相似度判定→跨架构权重迁移→新拓扑快速收敛优化。

## 实验分析
1. 测试对象：3阶CIFF、4阶CIFF、4阶CRFB三类连续ΔΣ ADC，对比NSGA-II、DE、贝叶斯、MLP-RL。
2. 原生优化效果：RL-GAT功耗优化最优，4阶CIFF功耗降低40.28%，MAT理想工具箱指标全部不达标。
3. 迁移学习性能：4阶CIFF→CRFB可减少11倍仿真迭代，功耗优化提升12.4%；跨同阶异构架构提速2.2倍，跨阶迁移提速1.7倍。
4. 消融对比：MLP-RL无图结构建模，跨架构迁移完全失效；相似度判定可规避无效知识迁移。
5. 工程有效性：仿真引入全工艺非理想参数，优化设计满足80dB SNDR等量产规格。

## 研究启发
1. 模拟系统级优化必须利用电路图拓扑，GAT注意力机制能精准建模多级积分器耦合，远超普通全连接网络。
2. 仅依靠器件相似迁移存在局限，基于信号通路、模块依赖的图相似度规则可大幅拓宽知识迁移适用范围。
3. 迁移学习能显著削减昂贵系统仿真次数，是解决ADC等高阶模拟设计迭代慢的核心方案。
4. 模拟优化不能脱离工艺非理想效应，理想模型生成参数不具备实际芯片可用性。
5. 分层功耗解析模型搭配约束优先奖励函数，可在满足性能下限前提下持续逼近功耗最优解。
