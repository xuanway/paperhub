---
title: "ChipAlign: Instruction Alignment in Large Language Models for Chip Design via Geodesic Interpolation"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# ChipAlign: Instruction Alignment in Large Language Models for Chip Design via Geodesic Interpolation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2412.19819">https://arxiv.org/abs/2412.19819</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 芯片设计大语言模型，指令对齐，测地线插值，免训练模型权重融合 </p>
</div>

---

## 研究概要
本文提出ChipAlign无训练模型融合方法，基于黎曼流形测地线插值融合芯片专用LLM与通用指令对齐LLM。仅单超参λ，线性计算复杂度，无需额外微调。评测显示在IFEval指令指标较ChipNeMo提升26.6%，OpenROAD、工业芯片QA分别提升3.9%、8.25%，同时完整保留芯片领域专业知识。

## 背景和动机
1. ChipNeMo等芯片专用大模型经域预训练与微调后，指令跟随对齐能力大幅衰减，难以满足工程师对话式EDA辅助需求。
2. 传统多任务微调提升指令能力依赖稀缺专有高质量指令数据集，70B大模型微调算力成本极高。
3. 现有模型融合方法（Model Soup、Task Arithmetic、TIES等忽略权重流形几何结构，融合后能力存在严重相互干扰。
4. 缺少面向芯片领域、无需训练的权重融合方案，无法低成本兼顾EDA专业知识与指令遵从两大核心能力。
5. 大模型权重属于高维黎曼流形，简单加权平均无法找到兼顾两类任务的最优权重组合。

## 相关工作
1. 芯片专用LLM（ChipNeMo/AutoMage/OpenROAD-LLM）：依托DAPT/DAFT适配电路、EDA脚本，但指令对齐性能显著下滑。
2. 多任务指令微调：联合领域+指令数据训练，数据集获取难、超大参量训练算力开销巨大。
3. 基础模型融合：Model Soup直接权重平均；Task Arithmetic基于任务向量叠加；TIES/DELLA通过稀疏剪枝缓解权重干扰，均未考虑流形几何特性。
4. 通用指令LLM（LLaMA2-Chat、Qwen-Chat）：指令遵从优秀，但缺少芯片设计专业知识。
5. 流形信息几何研究：证明神经网络权重分布于黎曼流形，但未落地域大模型融合场景。

## 本文解决方案
### 1 流形测地线插值融合范式
将芯片模型、指令模型权重视作流形两点，先对每层权重做F范数归一化投影至单位n球面，沿球面最短弧（测地线）插值生成融合权重，最后恢复原始权重幅值。
### 2 单超参可控融合公式
插值系数λ控制两类模型权重占比，λ=0偏向指令模型、λ=1偏向芯片模型；实验验证λ=0.6为全场景最优配置，调参成本极低。
### 3 线性复杂度高效实现
权重投影、球面插值、幅值缩放三步均为O(n)线性遍历，70B模型仅需数十分钟CPU计算，无需GPU与重训练。
### 4 分层通用融合架构
兼容Embedding、Attention、FFN、Norm全部网络层，要求源模型骨架完全一致，适配LLaMA、Qwen系列主流底座。
### 5 工业落地轻量化流程
基于LoRA微调得到域EDA模型后，直接与开源Chat底座权重融合，不依赖私有指令数据集，快速产出兼顾指令与专业知识的芯片助手模型。

## 实验分析
1. 实验设置：采用LLaMA2-70B、LLaMA3-8B、Qwen1.5-14B三类底座；评测IFEval、OpenROAD QA、工业多轮芯片QA三大基准。
2. 指令对齐：LLaMA2-70B-ChipAlign相较ChipNeMo指令指标提升26.6%，对齐能力超越原始LLaMA2-Chat。
3. 领域问答：OpenROAD基准ROUGE-L提升3.9%，工业生产级QA平均分提升8.25%，多轮问答优势明显。
4. 消融对比：优于Task Arithmetic、TIES、DELLA、ModelSoup全部传统融合基线，生成回答更贴合上下文约束。
5. 领域知识保留：EDA脚本、Bug、电路多选任务精度与原始ChipNeMo基本持平，融合无专业能力损耗。

## 研究启发
1. 域微调会破坏基座原生指令对齐能力，无训练模型融合是低成本修复该缺陷的高效路径。
2. 大模型权重具备流形几何属性，简单加权平均存在能力干扰，测地线插值能平滑融合双任务权重。
3. 仅单一超参即可平衡领域知识与指令能力，大幅降低工程调参与部署成本。
4. 无需私有指令数据集、不做二次微调，适配工业70B以上超大芯片LLM落地场景。
5. 该几何融合思路不限于EDA领域，可迁移医疗、金融等各类域专用大模型优化对齐能力。