---
title: "GNN-MLS: Signal Routing in Mixed-Node 3D ICs through GNN-Assisted Metal Layer Sharing"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# GNN-MLS: Signal Routing in Mixed-Node 3D ICs through GNN-Assisted Metal Layer Sharing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132697">https://ieeexplore.ieee.org/document/11132697</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 金属层共享，图神经网络，三维集成电路，信号路由 </p>
</div>


---

## 研究概要
本文提出GNN-MLS框架面向异质同构3D IC金属层共享布线优化，将时序超图转为图Transformer模型，采用DGI自监督预训练减少标注开销，精准筛选增益网线。配套两类DFT方案解决跨层开路可测性问题，搭配混合节点3D PDN设计。测试显示时序违例路径削减79%，TNS、WNS分别提升94%、81%。

## 背景和动机
1. 传统伪3D串行2D流程缺少跨层协同优化，金属层共享MLS可新增布线路径改善时序，但全局遍历STA筛选网线计算量爆炸。
2. 现有启发式MLS无精细网级决策，部分网线共享金属层反而恶化时序松弛，无法区分收益/损耗网络。
3. MLS在混合键合3D中产生跨层开路，单层制造阶段信号不可控不可观测，常规扫描DFT无法适配该缺陷。
4. 时序路径长距离依赖强，普通GNN仅捕捉局部邻接，难以建模多网线联动时序变化。
5. 异质混合工艺3D堆叠存在多电压域，缺少配套PDN电平转换与IR压降约束方案。

## 相关工作
1. 基础MLS算法：纯迭代STA遍历所有网线，计算成本极高，无机器学习加速筛选。
2. 3D布局布线工具（Hier3d/Pin3d）：仅基础伪3D流程，不支持金属层跨层共享协同优化。
3. 传统GNN版图模型：仅局部拓扑特征，无法建模时序路径全局长依赖关系。
4. 标准扫描DFT：针对单die内部故障，无法解决F2B键合跨层开路带来的可测性缺失。
5. 3D电源规划研究：未适配16nm逻辑+28nm内存混合节点多电压堆叠场景。

## 本文解决方案
### 1 超图转图Transformer时序建模
多引脚超边映射为源节点特征，提取单元位置、线长、寄生等多维特征；三层多头自注意力捕捉全路径网线长距离时序耦合关系。
### 2 DGI对比自监督预训练方案
无标注时序图最大化全局/局部互信息，扰动图生成负样本；少量STA真值微调二分类器，预测单网线是否启用MLS。
### 3 两类MLS专属DFT修复策略
1）多路选择器方案：测试模式切换跨层信号通路，硬件开销小；2）插入扫描触发器方案，故障覆盖率更高，路由后ECO微调时序。
### 4 混合节点3D PDN架构
逻辑层0.81V、内存层0.9V，跨层插入电平转换器；约束金属宽间距将IR压降控制在额定电压10%以内。
### 5 完整3D设计流程
布局布线后插入GNN-MLS做MLS决策→全局/详细布线强制分层金属共享→DFT逻辑插入→ECO微调完成可测3D版图。

## 实验分析
1. 测试基准：MAERI加速器、Cortex-A7双核，分16nm逻辑+28nm异质堆叠、28nm同质两类F2F键合场景，对比无MLS、传统MLS基线。
2. 时序收益：异质设计TNS降低94%，WNS提升81%，时序违例路径削减79%；智能选择性启用MLS，无用网线不共享金属层。
3. 资源开销：相比传统MLS，异质场景ML网线数量大幅减少，布线总长度小幅下降，功耗仅增加1%~3%。
4. DFT效果：触发器式DFT故障覆盖率98%以上，仅少量时序损失；多路选择器硬件面积开销更低。
5. 运行效率：模型推理替代海量STA迭代，整体布线优化运行时间显著缩短，适配大规模3D设计。

## 研究启发
1. MLS不能全量放开，时序路径存在耦合关系，需基于全局时序预测做网级精细化筛选。
2. 图Transformer搭配自监督预训练可解决EDA时序标注稀缺难题，大幅减少SPICE/STA仿真调用次数。
3. 3D跨层金属共享会引入独有可测性缺陷，必须定制化DFT电路，通用扫描架构不适用混合键合结构。
4. 异质多工艺3D堆叠需配套分层PDN与电平转换，严格约束IR压降保障时序稳定。
5. AI辅助决策嵌入物理设计前置阶段，可从源头挖掘3D跨层布线优化潜力，缩小与原生3D IC性能差距。
