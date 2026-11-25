---
title: "SSFT: Algorithm and Hardware Co-design for Structured Sparse Fine-Tuning of Large Language Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SSFT: Algorithm and Hardware Co-design for Structured Sparse Fine-Tuning of Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133200">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133200</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 结构化稀疏微调，算法-硬件协同设计，大语言模型，稀疏感知加速器 </p>
</div>


---

## 研究概要
本文提出软硬件协同SSFT框架，算法层SSFT-Alg挖掘权重梯度行列结构化稀疏，替代无规则稀疏微调；硬件SSFT-Hw配套稀疏感知取数与调度单元，适配LLM微调四阶段流程。在BERT、LLaMA2 7B/13B验证，精度损失低于1%，加速器相较A100吞吐提升51倍、能效提升19倍，超越SOTA TransCODE。

## 背景和动机
1. 全量微调成本极高，稀疏微调(SFT)仅更新少量参数，但无规则梯度掩码带来大量无效访存与MAC运算，GPU加速收益被 gather/topk 等轻量操作抵消。
2. LoRA等低秩微调新增大量中间矩阵，计算量高于稀疏微调，资源开销更大。
3. 现有稀疏Transformer加速器仅支持中小模型，7B及以上LLM易显存溢出，且无面向微调完整链路优化。
4. 无规则稀疏梯度访存碎片化，通用SpM*SpM硬件不支持Softmax、LayerNorm等Transformer特有算子，无法用于LLM微调。
5. 现有稀疏微调算法未利用梯度天然行列聚集规律，缺少硬件友好结构化稀疏设计思路。

## 相关工作
1. 参数高效微调(LoRA/IA³)：引入低秩辅助矩阵，额外算力显存开销大，稀疏度不及SFT。
2. 无规则稀疏微调(Fish/SpIEL)：梯度掩码随机分布，访存不规则，GPU运行效率低下。
3. TransCODE等Transformer加速器：仅适配中小模型，大LLM微调显存不足，稀疏调度优化不足。
4. 通用稀疏矩阵硬件(SIGMA)：仅支持矩阵乘，缺失Softmax、层归一化，无法完整支持微调。
5. cuSPARSE稀疏库：SDDMM优化收益有限，topk、收集分发操作占大量周期，难以释放稀疏算力潜力。

## 本文解决方案
### 1 SSFT-Alg结构化稀疏微调算法
多步采样累积梯度生成预掩码；统计每行每列非零梯度数量，选取top-k行列生成规整结构化掩码；训练仅计算掩码对应梯度，消除无效读写与乘加。掩码可多轮复用，采样开销一次性付出。
### 2 四阶段混合计算数据流
前向、反向稠密矩阵运算，权重梯度生成、权重更新启用稀疏模式，仅加载掩码指定行列数据，跳过全部无效计算。
### 3 SSFT-Hw硬件核心稀疏模块
1）稀疏感知Memory Fetcher：解析行列掩码，仅从DRAM读取有效权重、激活；
2）稀疏稠密调度器：按行列ID分配至独立PE并行计算；
3）集成多功能PE：内置MAC、Softmax、LayerNorm单元，完整覆盖LLM微调算子。
### 4 行列并行稀疏计算流
依据掩码RowID/ColID拆分矩阵，每行/列分配独立PE并行输出完整结果，消除零值参与运算，最大化片上并行利用率。
### 5 通用插件式掩码生成逻辑
预掩码模块兼容Fisher、Delta等传统稀疏筛选方案，可无缝对接各类梯度重要性判别策略。

## 实验分析
1. 实验环境：14nm工艺700MHz SSFT-Hw RTL仿真；基线A100/H100、TransCODE；评测GLUE、MMLU、TyDiQA、HumanEval。
2. 算法精度：BERT仅更新5%参数，平均精度仅降0.6%；LLaMA2 7B/13B相比LoRA、SpIEL差距小于1%，4bit量化后性能衰减极小。
3. 硬件吞吐：BERT-Large相较A100提速51×，比TransCODE提升1.32×；LLaMA2 7B TransCODE显存溢出，SSFT-Hw稳定运行，速度优于H100。
4. 能耗指标：相较A100能效提升19×，对比TransCODE能效提升1.48倍。
5. 消融验证：结构化行列掩码是核心优化，无规则稀疏会使硬件吞吐、能效大幅下滑。

## 研究启发
1. LLM权重梯度天然存在行列聚集特征，结构化稀疏可在几乎无损精度前提下，大幅降低硬件访存碎片化开销。
2. 单纯软件稀疏算法难以发挥算力，必须配套专用稀疏感知硬件，才能规避gather/topk等低效操作瓶颈。
3. 微调加速器不能仅优化矩阵乘，必须原生支持Softmax、LayerNorm等Transformer特有算子，否则无法完整落地训练流程。
4. 行列并行稀疏数据流能最大化PE利用率，是稀疏ASIC相比GPU的核心优势。
5. 结构化稀疏掩码一次采样多轮复用，可将梯度筛选分摊到训练全过程，控制算法预处理开销。
