---
title: "MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.03661">https://arxiv.org/abs/2504.03661</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/ZongwuWang/MILLION">https://github.com/ZongwuWang/MILLION</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> KV缓存量化，乘积量化，长上下文推理，GPU推理加速 </p>
</div>


---

## 研究概要
本文提出MILLION面向长上下文LLM的KV乘积量化推理框架，基于PQ乘积量化天然适配KV通道异常值，规避传统量化解码开销；设计异步量化CUDA流与重构注意力内核，无需单独存储离群样本。在32K上下文下端到端提速2.09倍，4bit量化困惑度损失极小，解决长文本KV缓存内存瓶颈。

## 背景和动机
1. 长上下文LLM推理中KV缓存内存随序列线性暴涨，批量服务极易触发显存溢出，成为核心存储瓶颈。
2. KV张量存在大量通道级幅值/标准差离群点，均匀低比特量化精度暴跌；传统离群分离方案带来稀疏访存与额外解码延迟。
3. 常规逐通道量化在线编解码占用20%~90%推理耗时，解码阶段内存受限场景性能损耗严重。
4. KIVI、KVQuant等方案依赖稀疏存储离群值，内存访问不规整，GPU内核并行效率低下。
5. 现有量化未复用乘积量化子空间聚类特性，无法自适应分配量化精度适配各通道数值分布差异。

## 相关工作
1. KIVI/KVQuant：分组非均匀量化，单独存储1%离群张量，精度小幅提升但引入稀疏访存、解码巨大开销。
2. QServer：SmoothAttention平滑权重降低量化误差，受旋转位置编码约束，长文本泛化能力弱。
3. 滑动/流式稀疏注意力：删减低权重KV Token，长文本未来注意力预测失效，精度损失不可控。
4. MQA/GQA多头共享：仅减少头维度KV总量，无法解决单头张量存储膨胀问题。
5. 权重类PQ量化：面向模型参数，未适配动态生成、时序依赖的KV缓存数据流。

## 本文解决方案
### 1 面向KV的乘积量化(PQ)算法
离线采样KV张量训练子空间码本，按通道划分子空间聚类；天然适配通道离群，无需单独存储稀疏离群点，不同子空间自动分配量化精度。
### 2 注意力计算数学重构
将QK矩阵乘拆分为码本预计算+索引查表，推理全程无需完整反量化KV张量，消除解码访存与计算开销。
### 3 双CUDA流异步量化流水线
高优先级流执行主注意力计算，低优先级后台流异步完成新Token KV量化，量化计算与推理完全重叠，不阻塞主推理通路。
### 4 优化Flash兼容CUDA内核
float4批量加载量化索引至L1缓存，分片并行查表加权求和，规整连续内存访问，提升GPU SM利用率。
### 5 三段式完整推理流程
离线码本训练→Prefill阶段实时量化写入缓存→Decode异步更新KV索引，全链路兼容RoPE、ALiBi各类位置编码模型。

## 实验分析
1. 实验环境：A40 GPU，覆盖GPT2、LLaMA2、MPT、Longchat、Yarn多模型，评测Wikitext、LongBench长文本基准，对比KIVI、KVQuant。
2. 精度表现：3/4bit量化下困惑度仅微小上涨，分离1%离群仅带来极小幅精度提升，证明框架天然抗离群。
3. 推理时延：32K上下文端到端提速2.09倍；KVQuant、KIVI随上下文拉长出现OOM或时延暴涨。
4. 消融验证：异步量化流消除解码阻塞；PQ重构注意力是提速核心，规整访存大幅降低SDPA算子耗时。
5. 扩展性：支持128K超长上下文Yarn模型，长文本任务指标衰减远小于基线量化方案。

## 研究启发
1. KV通道分布差异显著，乘积量子空间聚类可自适应分配量化精度，无需稀疏存储离群，兼顾精度与访存规整性。
2. 量化瓶颈不在压缩过程，而在反解码开销，重构注意力计算、查表替代完整反量化是提速关键思路。
3 利用GPU多流异步重叠量化与主推理，可完全掩盖编解码计算延迟，不占用关键推理流水线。
4. 长上下文场景下，单纯稀疏删减Token精度风险高，KV量化是更稳定的内存压缩路线。
5. 量化算法需与GPU算子、内存访问模式协同设计，仅算法优化难以发挥硬件并行潜力。