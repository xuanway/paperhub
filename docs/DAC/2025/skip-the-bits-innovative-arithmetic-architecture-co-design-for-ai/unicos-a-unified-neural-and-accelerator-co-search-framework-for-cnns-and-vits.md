---
title: "UniCoS: A Unified Neural and Accelerator Co-Search Framework for CNNs and ViTs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# UniCoS: A Unified Neural and Accelerator Co-Search Framework for CNNs and ViTs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133418">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133418</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/mine7777/Unicos">https://github.com/mine7777/Unicos</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 零样本代理，异构多核架构，软硬件协同探索 </p>
</div>


---

## 研究概要
本文提出UniCoS统一网络-加速器协同搜索框架，同时支持CNN与ViT。设计无训练梯度一致性精度代理，搭配聚类+剪枝异构数据流硬件搜索，规避超网预训练开销。ImageNet验证，精度提升1.76%、EDP降低3.54倍，搜索速度最高提升48倍，仅需3小时完成全流程协同寻优。

## 背景和动机
1. 现有软硬件协同搜索依赖One-Shot超网，CNN超网训练需百小时，ViT高达576GPU小时，修改搜索空间必须重训，效率极低。
2. 硬件搜索局限单核单数据流，CNN、ViT层计算特性差异大，单核架构层间不匹配，能效差。
3. 多核异构数据流设计空间爆炸，单硬件评估耗时数十分钟，协同搜索迭代成本不可接受。
4. 缺少同时兼容卷积与Transformer骨干的统一协同框架，CNN、ViT需两套独立搜索工具，复用性差。
5. 主流零精度代理相关性偏低，无法精准排序候选网络，协同搜索易错过精度-硬件帕累托最优解。

## 相关工作
1. 单架构协同搜索(DIAN/DANCE)：仅支持CNN，依赖超网训练，硬件只支持单核数据流，无多核异构探索。
2. 硬件数据流搜索(GAMMA/HPCA21)：仅优化加速器，不联合网络架构搜索，无法实现端到端协同优化。
3. 零样本NAS代理(Zen/ZiCo/GradSign)：仅做网络精度评估，未配套异构加速器联合寻优。
4. ViT专用AutoFormer：仅网络搜索，无硬件感知协同，超网预训练耗时数百GPU小时。
5. 多核DNN加速器：仅固定网络映射，无法随搜索动态匹配网络层与子加速器数据流。

## 本文解决方案
### 1 梯度一致性无训练精度代理FGCO
单次前向反向取小批量梯度，过滤极值梯度噪声，计算多批次梯度一致性作为精度代理；几秒完成网络打分，无需超网预训练，兼容CNN/ViT。
### 2 分层异构硬件数据流搜索
层聚类核间映射：DBSCAN/K-Means按计算特征分组，分配独立子加速器；核内演化算法遍历时空复用、分块并行参数。
### 3 双重设计空间剪枝
值剪枝：复用维度取4的倍数缩小候选；策略剪枝：每聚类选代表层推演全局数据流，硬件评估从数十分钟缩至15秒内。
### 4 统一进化协同搜索流水线
进化种群采样网络，双评估器并行输出代理精度、硬件EDP；适应度=代理分数/ED，迭代选择交叉变异，同时优化CNN/ViT。
### 5 兼容Maestro扩展仿真器
扩展Maestro支持多子加速器时延、能耗、面积评估，适配卷积与多头注意力矩阵乘两类算子。

## 实验分析
1. 实验环境：i5 CPU+A6000，NASBench201、AutoFormer数据集，Maestro硬件仿真，基线DIAN/DANCE/AutoFormer。
2. 代理有效性：FGCO相关性Kendall τ、Spearman ρ全面优于ZiCo等零样本方法，打分与真实精度高度吻合。
3. CNN协同结果：对比DIAN精度+1.76%、EDP降低3.54倍，搜索提速48倍，仅3小时完成寻优。
4. ViT协同结果：相较AutoFormer搜索提速131~161倍，EDP下降36%，精度基本持平或小幅提升。
5. 硬件消融：多核异构+双剪枝相比单核无剪枝方案EDP下降数百倍，单硬件评估提速2.2~7.4倍。

## 研究启发
1. 超网训练是协同搜索最大性能瓶颈，梯度类无训练代理可彻底消除预训练开销，实现跨模型通用。
2. CNN与Transformer算子计算特性差异巨大，单核数据流无法兼顾，多核异构分层映射是硬件优化核心。
3. 数据流设计空间呈指数规模，聚类+代表层剪枝是低成本压缩搜索空间的有效手段。
4. 统一框架同时覆盖CNN、ViT可大幅降低工具开发成本，避免两套独立协同流程。
5. 精度代理与硬件评估解耦，可分别迭代优化，灵活适配不同数据集与加速器工艺约束。