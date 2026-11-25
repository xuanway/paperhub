---
title: "SynCircuit: Automated Generation of New Synthetic RTL Circuits Can Enable Big Data in Circuits"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SynCircuit: Automated Generation of New Synthetic RTL Circuits Can Enable Big Data in Circuits

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://zhiyaoxie.com/files/DAC25_SynCircuit.pdf">https://zhiyaoxie.com/files/DAC25_SynCircuit.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 合成电路生成，有向循环图，扩散模型，蒙特卡洛树搜索 </p>
</div>


---

## 研究概要
本文提出SynCircuit RTL合成电路生成框架，分三阶段解决EDA开源电路数据稀缺难题：定向循环图扩散生成、概率引导合法性后处理、MCTS逻辑冗余优化。可生成合规Verilog/VHDL代码，图结构、时序面积特征贴近真实电路。扩充PPA预测训练集后，模型MAPE最低下降10%，显著优于GraphRNN、DVAE等基线。

## 背景和动机
1. AI辅助EDA（PPA预测、RTL生成）高度依赖开源电路数据集，但公开RTL样本极少，严重制约模型训练效果。
2. 现有图生成方法仅支持无向/有向无环图(DAG)，无法建模带寄存器环路的数字电路DCG定向循环图。
3. 扩散、自回归图模型生成的原始图不满足电路扇入、无组合环路硬性约束，无法综合成网表。
4. 原生生成电路存在大量冗余逻辑，综合后时序、面积分布与真实电路偏差极大，扩充数据集收益微弱。
5. 缺少端到端可输出合法HDL的合成电路生成流水线，无法直接用于EDA下游数据增强。

## 相关工作
1. 自回归图生成(GraphRNN/DVAE)：依赖拓扑序，仅能生成DAG，无法处理电路循环，生成电路非法。
2. 一次性无向图模型(GraphMaker/SparseDigress)：无有向边建模能力，生成后需额外定向，电路结构失真严重。
3. 专用电路LLM(VerilogGPT/RTLCoder)：侧重代码生成，无法批量可控生成多样化拓扑电路，数据集扩充能力弱。
4. 图扩散模型(DiGress)：面向通用无向图，未适配电路节点扇入、组合环路专属约束。
5. EDA数据集工作(CircuitNet)：仅整理现有开源设计，无自动生成海量合成电路的能力。

## 本文解决方案
### 1 面向DCG的离散扩散图生成模型
设计非对称边解码器，引入可学习关系嵌入区分边方向；MPNN编码器适配大规模电路图，前向逐步加噪、反向降噪预测边存在概率矩阵，支持用户自定义节点规模与类型。
### 2 概率引导电路合法性后处理
基于扩散输出边概率，逐节点筛选合法父节点，校验规避组合环路、匹配各算子固定扇入数，输出可解析的有效电路图G^val。
### 3 MCTS逻辑冗余优化模块
定义PCS时序面积奖励指标，以交换边为原子操作；采用UCB1平衡探索利用，优化寄存器驱动锥，大幅提升SCP时序保留率，缩小与真实电路差距。
### 4 完整HDL转换流水线
内置电路图解析器，将优化后的DCG无损映射为Verilog/VHDL源码，可直接送入商用综合工具输出网表。
### 5 轻量化适配下游EDA任务
生成电路可直接作为数据增强样本，扩充PPA、时序预测模型训练集，适配少样本EDA训练场景。

## 实验分析
1. 实验环境：ITC99/OpenCores/Chipyard开源RTL构建训练集，对比GraphRNN/DVAE/GraphMaker；指标含Wasserstein距离、SCPR、PPA预测MAPE/RRSE。
2. 图相似度：SynCircuit扩散方案6项结构指标5项最优，度分布、聚类系数贴近真实电路，Wasserstein距离远低于基线。
3. 逻辑冗余：MCTS优化后SCPR从不足20%提升至50%以上，综合后寄存器留存数量显著增加，时序分布与真实电路对齐。
4. 下游EDA效果：仅5份真实设计训练时，加入SynCircuit合成样本，面积MAP下降30%，时序预测误差大幅降低；基线生成样本反而损害模型精度。
5. 消融实验：移除扩散模块后图结构相似度暴跌；无MCTS优化电路冗余过高，数据增强无正向收益。

## 研究启发
1. 数字电路是特殊定向循环图，通用D/无向图生成模型不能直接复用，需定制非对称边建模扩散框架。
2. 图生成不能仅关注拓扑相似，必须叠加电路规则校验，否则生成HDL无法用于EDA综合。
3. 逻辑冗余是合成电路与真实电路核心差距，MCTS等搜索优化可低成本修复时序、面积分布偏差。
4. 稀缺EDA数据集可通过可控合成电路扩充，高质量合成样本能显著提升PPA预测等下游AI模型泛化能力。
5. 面向领域的图生成不能只追求视觉相似，必须绑定领域专属约束与硬件综合指标做联合优化。
