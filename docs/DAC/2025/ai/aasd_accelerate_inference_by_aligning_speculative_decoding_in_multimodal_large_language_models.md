---
title: "AASD: Accelerate Inference by Aligning Speculative Decoding in Multimodal Large Language Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# AASD: Accelerate Inference by Aligning Speculative Decoding in Multimodal Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132960">https://ieeexplore.ieee.org/document/11132960</a></p>
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/transcend-0/ASD">https://github.com/transcend-0/ASD</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多模态大语言模型，推理加速，推测解码 </p>
</div>


---


## 研究概要
本文提出AASD多模态投机解码加速框架，复用目标模型KV缓存并设计KV投影器压缩视觉特征，配套Target-Draft对齐注意力消除训练推理鸿沟。基于LLaVA-7B/13B在多模态任务验证，token接受率达0.62，推理最高提速2倍，无精度损失，轻量易部署。

## 背景和动机
1. MLLM自回归解码时延极高，传统量化、剪枝、轻量化编码器易损伤图文对齐与生成质量。
2. 纯文本投机解码迁移至多模态效果差，小draft模型难以学习长视觉token分布，候选token接受率低，加速收益微弱。
3. 现有多模态投机方案无法复用目标模型上下文KV，图文混合KV序列过长大幅增加draft训练与推理开销。
4. 训练与推理KV构造逻辑不一致，常规因果掩码无法模拟多步投机场景，训练开销达O(n²)。
5. 缺少轻量化、不修改主模型的图文协同投机对齐方案，难以适配图像描述、多轮问答等实时业务。

## 相关工作
1. MLLM轻量化优化：视觉token剪枝、编码器压缩、模型蒸馏，普遍牺牲图文匹配精度。
2. 纯文本投机解码：仅适配单文本输入，无视觉KV适配机制，迁移至多模态接受率暴跌。
3. 多模态投机基线：仅用小型多模态/纯文本draft，视觉特征学习能力弱，加速上限低。
4. 缓存优化方案：仅压缩推理KV，未将目标KV用于辅助draft模型对齐。
5. 注意力改进工作：仅面向常规自注意力，无兼顾目标/双draft混合KV的专用对齐注意力。

## 本文解决方案
### 1 目标KV复用+KV投影压缩流水线
预填充阶段提取目标模型图文KV，设计轻量KV投影器压缩视觉KV至固定64维，削减90%冗余视觉信息；将压缩KV输入draft模型，让draft贴合目标分布，提升候选token匹配度。
### 2 分阶段投机解码流程
预填充：图像+提示词编码生成完整图文KV；Draft：draft依托目标历史KV并行生成多候选token；Verify：目标一次性批量校验所有候选，截断不匹配序列迭代循环。
### 3 Target-Draft对齐注意力
解决训练推理KV不一致问题，混合目标历史KV与draft生成KV构造注意力矩阵，复用中间计算避免O(n²)存储开销；搭配交叉熵+TVD损失缩小两模型分布差异。
### 4 极简训练范式
仅训练KV投影器与对齐注意力层，主目标模型冻结；无需重新预训练大视觉语言主干，训练成本极低。
### 5 多粒度超参适配
支持γ=3/5两种并行候选长度，适配7B/13B不同规模MLLM，动态平衡并行度与校验计算开销。

## 实验分析
1. 实验配置：LLaVA-7B/13B，评测COCO图像描述、ScienceQA推理、LLaVA对话三类数据集；基线为微调/蒸馏纯文本、小型多模态draft。
2. 核心指标：γ=5时13B模型平均提速2.24倍，token生成速度70.45 token/s，候选接受率稳定0.62，块效率接近4。
3. 消融实验：移除目标KV提速下降30%以上；关闭KV投影器后接受率由0.62降至0.49，视觉KV是关键增益来源。
4. 模态对比：文本KV对解码效率影响大于视觉KV，仅保留视觉KV加速收益大幅缩水。
5. 泛化性：在图文描述、多轮对话、链式推理场景均稳定实现近2倍加速，生成文本质量无衰减。

## 研究启发
1. 多模态投机解码瓶颈在于图文分布对齐，复用目标模型上下文KV是低成本提升draft匹配度的核心手段。
2. 视觉token冗余度极高，专用KV投影压缩可在不损失关键语义前提下大幅降低draft计算负担。
3. 训练与推理KV结构不一致是投机对齐核心障碍，定制混合KV注意力可规避平方级存储开销。
4. 小型多模态draft建模难度远高于文本draft，依托目标缓存替代大模型蒸馏更实用。
5. 多模态加速不能割裂图文信息，文本KV提供时序上下文，视觉KV提供语义细节，二者协同才能最大化投机收益。
