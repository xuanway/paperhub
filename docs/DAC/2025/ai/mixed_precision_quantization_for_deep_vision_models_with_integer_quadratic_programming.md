---
title: "Mixed-Precision Quantization for Deep Vision Models with Integer Quadratic Programming"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Mixed-Precision Quantization for Deep Vision Models with Integer Quadratic Programming

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2307.05657">https://arxiv.org/abs/2307.05657</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/JamesTuna/CLADO_MPQ">https://github.com/JamesTuna/CLADO_MPQ</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合精度量化，跨层依赖，整数二次规划，灵敏度分析 </p>
</div>


---


## 研究概要
本文提出CLADO跨层感知混合精度量化框架，针对现有方法忽略层间量化误差耦合的缺陷，基于二阶泰勒展开拆分单/跨层敏感度，仅前向传播快速求解；将比特分配转化整数二次规划IQP，在ImageNet的CNN与ViT模型验证，同等存储约束下分类精度显著优于HAQ、MPQCO等基线。

## 背景和动机
1. 统一精度量化对各层不加区分，浅层敏感层低位宽会造成巨大精度衰减，混合精度量化(MPQ)可分层分配比特平衡精度与存储。
2. 现有敏感度类MPQ算法仅累加单层误差，完全忽略两层联合量化带来的耦合损失，最优比特分配方案存在偏差。
3. 传统海森矩阵计算开销极大，难以批量评估所有层组合的跨层误差，无法落地大规模网络。
4. 基于搜索的MPQ（RL/NAS）迭代搜索耗时数百GPU小时，硬件成本过高，工业部署效率低。
5. 仅分块计算耦合误差的方案会丢失块间交互，依旧无法得到全局最优分层比特策略。

## 相关工作
1. 搜索型MPQ（HAQ、MPQDNAS）：强化学习/可微搜索遍历比特组合，精度优但算力消耗极高，无法复用敏感度结果。
2. 单层敏感度方法（HAWQ、MPQCO、ZeroQ）：仅计算独立层量化损失，无视层间误差耦合，最优分配存在偏差。
3. BRECQ：仅在网络块内计算层交互，忽略跨块量化耦合，全局优化效果受限。
4. 自适应舍入/后量化工具：仅优化单一层量化误差，不解决全局比特分配组合优化问题。
5. 海森量化方法：依赖完整二阶矩阵求逆，计算成本过高，不支持多分层、多比特候选场景快速评估。

## 本文解决方案
### 1 跨层误差敏感度建模
对损失二阶泰勒展开，拆分单层自敏感度、层间交叉敏感度；证明联合量化总损失包含两两层耦合项，现有方法缺失该项导致次优解。
### 2 无海森前向估算敏感度
无需反向求海森矩阵，仅通过完整模型、单层量化、双层量化前向推理差值，推导出交叉敏感度快速计算公式，O(L²)复杂度完成评估。
### 3 整数二次规划(IQP)比特分配
引入独热二元变量表征各层比特选择，以敏感度矩阵构造二次目标，添加总存储线性约束，通过求解器秒级得到全局最优分层比特。
### 4 半正定(PSD)矩阵修正
小校准样本带来敏感度矩阵不定问题，特征分解截断负特征值做PSD近似，保证IQP稳定收敛，大幅缩短求解时间。
### 5 完整CLADO流水线
小样本校准集计算敏感度矩阵→PSD修正→IQP求解各层比特→后量化/量化感知微调两套部署流程，兼容CNN、ViT。

## 实验分析
1. 实验环境：ImageNet数据集，ResNet、MobileNet、RegNet、ViT；基线HAWQ、MPQCO、统一量化UPQ；GPU单卡评估。
2. 精度表现：同等模型体积约束下CLADO Top-1精度全面领先，极端低位宽差距可达5~32个百分点；微调后仍保持稳定优势。
3. 鲁棒性：校准样本量≥1024时性能区间显著优于基线，不同随机采样集下精度中位数、下四分位数更高。
4. 消融实验：移除跨层耦合项（CLADO*）精度大幅下跌；关闭PSD近似则IQP求解无法收敛，耗时激增。
5. 模型适配：CNN与ViT均有明显收益，ViT长距离依赖结构下层间耦合影响更突出，提升幅度更大。

## 研究启发
1. 网络层量化误差存在强两两耦合，仅累加单层损失的MPQ算法天然存在优化缺陷，必须纳入跨层交互项。
2. 无需计算完整海森矩阵，依靠多组前向推理差值即可高效估算二阶耦合损失，大幅降低评估算力开销。
3. 分层比特分配可建模为IQP凸优化问题，能快速求得全局最优解，远优于迭代搜索类方案。
4. 小校准样本会导致敏感度矩阵非半正定，简单特征截断即可稳定优化求解，是工程落地关键优化点。
5. CNN与ViT层间依赖特性不同，ViT跨层量化耦合影响更强，跨层感知量化对Transformer类模型增益更显著。
