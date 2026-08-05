---
title: "Few-shot Learning on AMS Circuits and Its Application to Parasitic Capacitance Prediction"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Few-shot Learning on AMS Circuits and Its Application to Parasitic Capacitance Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://numbda.cs.tsinghua.edu.cn/papers/dac252.pdf">https://numbda.cs.tsinghua.edu.cn/papers/dac252.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 少样本学习，图神经网络，寄生电容预测，子图采样 </p>
</div>

---

## 研究概要
本文提出少-shot图学习框架CircuitGPS用于AMS电路寄生电容预测。将网表建模异构图，采用1跳包围子图采样，设计低成本DSPD位置编码，搭建MPNN+混合图Transformer。预训练做链路预测、微调完成电容回归，零样本泛化全新电路，链路预测精度提升20%以上，电容MAE降低至少0.067。

## 背景和动机
1. 工业AMS电路设计数据受IP保密限制难以获取，标注需耗时EDA寄生提取，数据集稀缺，常规深度学习无法落地。
2. 先进工艺下耦合寄生严重影响后仿精度，传统SPICE仿真迭代成本极高，亟需快速预布局寄生预测模型。
3. 现有GNN寄生模型直接输入完整大图，泛化能力差，面对未见过的全新电路精度大幅衰减，无少-shot机制。
4. 传统图位置编码（拉普拉斯、随机游走）计算开销大，不适用于大规模电路子图。
5. 电路耦合链路类别不均衡，现有方法未做正负样本平衡，训练偏向占比高的引脚-网耦合链路。

## 相关工作
1. 寄生预测GNN（ParaGraph/DLPL-Cap）：完整大图输入、无少-shot预训练，泛化弱，只能适配同类SRAM电路。
2. 链路预测图学习SEAL：提出包围子图采样，但无电路专用位置编码，未适配AMS异构器件拓扑。
3. GraphGPS通用图Transformer：并行MPNN+注意力架构，但缺少电路定制子图采样与低开销PE。
4. 传统图位置编码LapPE/RWSE：计算复杂度高，大规模电路子图推理耗时严重。
5. 通用少-shot图学习：无EDA电路拓扑适配，无法区分晶体管、网、引脚多类异构节点。

## 本文解决方案
### 1 AMS异构电路图建模
网表转为三类型节点（网/器件/引脚）异构图，耦合效应定义待预测链路；按链路类型平衡正负样本，缓解类别失衡问题。
### 2 1跳包围子图采样
遵循γ衰减理论仅取单跳邻居构成子图，分离局部拓扑与全局大图，实现任务解耦，适配少-shot元学习；并行采样加速数据构造。
### 3 DSP双锚最短路径位置编码
以链路两端节点为双锚，存储节点到两锚最短距离向量，无需特征分解，计算开销远低于LapPE、DRNL，高效表征子图空间结构。
### 4 混合GraphGPS骨干网络
并行GatedGCN-MPNN+全局注意力分支，融合局部拓扑与全局子图信息；区分基础节点特征与电路统计特征两套输入头。
### 5 两阶段少-shot学习流水线
阶段1元预训练：子图输入做耦合链路有无二分类；阶段2微调：冻结/解冻两种微调策略，完成耦合电容回归，支持零样本跨电路预测。

## 实验分析
1. 实验数据集：SSRAM/ULTRA8T/SANDWICH-RAM训练集，数字时钟、时序控制等全新电路零样本测试，28nm工艺。
2. 链路预测：相较ParaGraph、DLPL-Cap精度提升超20%，DSPD编码AUC达0.9774，优于DRNL/LapPE。
3. 耦合电容回归：所有测试集MAE下降≥0.067，全参数微调R²最高0.936，预测电容代入SPICE仿真能量误差仅14.5%。
4. 消融结论：纯MPNN性能接近混合Transformer，邻域原始节点特征会引入噪声、降低泛化性。
5. 拓展验证：框架兼容接地寄生节点回归任务，跨SRAM、数字混合电路均保持稳定低预测误差。

## 研究启发
1. AMS电路寄生预测无需完整大图，1跳局部子图即可捕获核心耦合拓扑，大幅降低模型泛化难度。
2. 传统高代价谱类位置编码不适用于EDA大规模图，双锚距离轻量PE可兼顾精度与推理速度。
3. 少-shot元预训练链路存在性是跨电路迁移关键，仅微调回归头即可快速适配全新工艺/拓扑。
4. 电路预测任务中邻域原始器件特征易引入无关噪声，删减冗余特征可显著提升零样本泛化能力。
5. MPNN局部信息提取能力足以支撑电路拓扑任务，不一定依赖重型全局图Transformer，兼顾精度与算力开销。
