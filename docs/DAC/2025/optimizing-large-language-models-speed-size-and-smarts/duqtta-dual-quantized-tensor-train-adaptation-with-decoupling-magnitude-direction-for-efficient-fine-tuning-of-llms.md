---
title: "DuQTTA: Dual Quantized Tensor-Train Adaptation with Decoupling Magnitude-Direction for Efficient Fine-Tuning of LLMs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DuQTTA: Dual Quantized Tensor-Train Adaptation with Decoupling Magnitude-Direction for Efficient Fine-Tuning of LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133002">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133002</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，张量链，双重量化，自适应优化策略，幅度-方向解耦 </p>
</div>

---

## 研究概要
本文提出DuQTTA轻量化大模型微调框架，融合张量列车TT分解、双量化DQ、自适应优化AOS与幅值-方向解耦更新。通过TT极大缩减可训练参数量，两级8bit量化降低存储计算，解耦机制解决LoRA幅值方向耦合缺陷。LLaMA系列测试相较LoRA精度提升最高4.44倍，压缩倍率达65倍，适配边缘设备微调部署。

## 背景和动机
1. 全参数微调算力显存开销巨大，无法落地边缘硬件，PEFT成为主流轻量化微调方案。
2. LoRA类低秩方法存在固有缺陷：更新矩阵幅值、方向强耦合，模型宽度增大时易陷入局部最优，下游性能受限。
3. 现有TT-LoRA仅做张量分解，未引入量化压缩，内存开销仍偏高，缺少训练友好低比特方案。
4. 单一量化仅压缩权重，未对张量重构过程做二次量化，推理浮点运算量依旧较高。
5. 高低维投影矩阵梯度量级差异大，统一学习率导致收敛慢、微调精度难以逼近全参数效果。

## 相关工作
1. 适配器/提示调优：插入额外模块或可学习token，推理引入额外延迟，参数量压缩幅度有限。
2. LoRA及其变体：仅低秩近似权重更新，幅值方向耦合；QLoRA、LoftQ侧重权重量化，未解决耦合优化缺陷；LoRETTA引入TT但无两级量化与自适应学习策略。
3. SVD低秩压缩：逐层奇异值分解，压缩倍率远低于TT分解，参数冗余度更高。
4. 单阶段后量化：仅离线压缩预训练权重，不参与微调训练，精度损失显著，无法适配张量分解结构。
5. 非解耦低秩优化：统一学习率更新高低秩矩阵，梯度失衡导致微调收敛效果差。

## 本文解决方案
### 1 幅值-方向解耦更新机制
将预训练权重拆分为可训练幅值向量、固定方向矩阵；仅对方向分量做TT低秩分解，解除传统低秩方法幅值、方向同步耦合限制，逼近全参数更新逻辑。
### 2 TT张量列车参数重参数化
将LoRA上下低秩矩阵重塑为高维张量，分解为链式TT核心，参数量从O(n²)降至O(dnr²)，大幅压缩可训练参数规模。
### 3 两级双量化DQ策略
训练阶段量化TT核心至8bit；张量重构后二次8bit量化线性矩阵，STE直通估计支撑量化微调，兼顾训练显存与推理算力削减。
### 4 AOS自适应学习率优化
根据高低投影矩阵梯度范数动态分配学习率，学习率比例与维度平方根匹配，平衡高低维特征更新幅度，解决大宽度网络收敛瓶颈。
### 5 完整轻量化微调流水线
冻结主干权重，仅训练TT核心与幅值参数；推理融合更新矩阵至原始权重，无额外推理延迟，兼容各类LLaMA系列大模型。

## 实验分析
1. 实验配置：LLaMA2-7B、LLaMA3-8B、LLaMA2-13B，7类分类/生成评测数据集，对比FT、Adapter、LoRA、LoRETTA等基线。
2. 精度表现：LLaMA2-7B平均精度超LoRA 4.44%，LLaMA3-8B提升3.14%，13B模型提升0.97%，大幅优于LoRETTArep。
3. 参数压缩：相较普通PEFT最高实现65倍参数量压缩，TT秩取8时精度与参数量达到最优平衡点。
4. 量化收益：双量化仅小幅损失精度，推理内存、访存耗时、功耗显著下降，推理速度最高提升5倍以上。
5. 消融验证：幅值解耦、AOS自适应学习率、双量化三者缺一不可，TT分解是实现超高压缩的核心基础。

## 研究启发
1. 传统LoRA幅值方向耦合是性能瓶颈，解耦式权重分解可大幅缩小与全参数微调的精度差距。
2. TT张量分解压缩能力远超SVD，是边缘设备超轻量化微调优选参数化手段。
3 两级训练量化而非离线后量化，能在极低精度损耗下同步压缩训练、推理两段资源开销。
4. 高低维投影矩阵梯度天然不均衡，固定学习率存在收敛缺陷，自适应动态调优是低成本性能增益方案。
5. 轻量化微调框架需兼顾训练开销与推理延迟，TT+量化融合且推理无额外开销的架构更适合工业边缘落地。