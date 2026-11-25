---
title: "A Memory-Efficient LLM Accelerator with Q-K Correlation Prediction using Cluster-Based Associative Array for Selective KV Accessing"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# A Memory-Efficient LLM Accelerator with Q-K Correlation Prediction using Cluster-Based Associative Array for Selective KV Accessing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133377">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133377</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，KV缓存，加速器 </p>
</div>

---

## 研究概要
本文提出软硬件协同LLM加速器Sella，设计聚类关联阵列预测Q-K相关性，实现选择性KV缓存访存，无需模型微调。硬件分为预测引擎与流水线计算引擎，在Llama2/OPT/Pythia验证，片外访存最高削减66%，相比SpAtten提速2.1倍、对比CPU提速53.5倍，精度损失可忽略。

## 背景和动机
1. LLM自回归推理依赖KV缓存，序列变长后KV访存量远超权重，HBM带宽仍会出现瓶颈，token生成速度持续下降。
2. 注意力权重极度稀疏，大量历史KV对当前token无贡献，全量加载带来冗余访存与乘算开销。
3. 现有稀疏注意力方案缺陷显著：SpAtten仅修剪prompt、Sanger预测开销巨大，多数方法需要重新训练大模型，落地成本极高。
4. 缺少轻量、无需微调的硬件级KV筛选机制，无法在推理时动态识别有效KV向量。
5. 现有加速器未配套相关性预测硬件，难以从源头削减KV缓存内存访问瓶颈。

## 相关工作
1. SpAtten：级联token/头剪枝，仅支持prompt阶段稀疏，生成阶段无法动态筛选KV，依赖权重存储开销。
2. Sanger/DOTA：通过Q、K向量完整内积预测稀疏，预测阶段访存与计算代价极高。
3. A3近似注意力：仅降低计算量，无法减少KV缓存片外内存读取。
4. FlashAttention：优化注意力访存重排，不做KV稀疏筛选，无法缓解长序列KV带宽压力。
5. GPU/通用CPU推理：无专用稀疏预测硬件，长上下文KV缓存访问效率极低，能效差。

## 本文解决方案
### 1 聚类关联阵列Q-K相关性预测算法
线下K-Means聚类Q向量生成聚类中心QKey，构建桶表存储高相关KV索引；推理用Q匹配中心近似点积，无需完整QK内积，全程不微调模型。配套阈值异常机制、多桶精度补偿策略。
### 2 分层优化策略
前两层注意力跳过稀疏筛选（稀疏收益低、精度损耗大），深层启用关联阵列，平衡精度与访存削减收益；桶尺寸随序列长度动态调整。
### 3 Sella双引擎硬件架构
1）预测引擎：MAC树PE阵列、移位寄存器桶表、位图索引合并模块，完成相关性计算、桶更新、KV索引去重；2）全流水线计算引擎：适配FlashAttention，仅加载筛选后的KV至片上缓冲区。
### 4 桶表高效更新电路
移位寄存器配合异或控制多路选择，新相关性值自动有序插入，自动丢弃最小值，维持桶内降序存储，更新逻辑极简。
### 5 位图索引去重单元
2048位位图标记已选KV索引，多路输入实时合并去重，仅向LSU发送唯一KV地址，避免重复内存加载。

## 实验分析
1. 实验配置：22nm工艺500MHz，HBM2 256GB/s，测试OPT-6.7b/Llama2-7b/Pythia-6.9b，PIQA/Wikitext等多数据集。
2. 精度表现：各类任务精度最大下降1.4%，困惑度涨幅低于7%，对推理效果影响极小。
3. 访存优化：长文本Wikitext场景片外KV访存削减66%，预测引擎自身开销仅占总访问6.3%以内。
4. 性能加速：相比SpAtten、Sanger、RTX3090、Xeon CPU平均提速2.1×/93.8×/31.4×/53.5×，长序列增益更突出。
5. 参数消融：BN=64、α=0.0625、δ=0.6为最优平衡点；分层、精度补偿、异常处理均是保障精度的核心模块。

## 研究启发
1. 利用聚类近似替代完整QK内积，可极低开销预测KV相关性，无需重训模型，适配各类预训练LLM。
2. KV缓存带宽是长上下文LLM核心瓶颈，硬件前置稀疏筛选比单纯优化注意力计算收益更大。
3. 不同Transformer层稀疏潜力差异大，分层启用稀疏机制可兼顾精度与硬件收益。
4. 移位寄存器+位图轻量硬件电路，能高效实现KV索引管理，无需复杂排序逻辑。
5. 稀疏注意力优化不能只关注计算量削减，必须同步降低片外DRAM访问才能真正提升推理吞吐量与能效。