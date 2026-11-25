---
title: "KVO-LLM: Boosting Long-Context Generation Throughput for Batched LLM Inference"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# KVO-LLM: Boosting Long-Context Generation Throughput for Batched LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132542">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132542</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，长上下文，批处理，KV缓存，算法-架构协同设计 </p>
</div>


---

## 研究概要
本文提出算法架构协同优化方案KVO-LLM面向长上下文批量LLM推理。算法端设计DSQ差分量化+HCAP注意力剪枝压缩KV缓存，外部访存削减超91%；硬件采用算子融合与跨批次交织多核心加速器。28nm流片后相较SOTA加速器吞吐量最高7.32倍，能效提升5.52~8.38倍。

## 背景和动机
1. 长上下文批量推理下KV缓存体量爆炸，外部DRAM访存占总延迟96%，成为推理核心瓶颈，上下文32K时缓存容量达权重20倍以上。
2. 注意力层算术强度极低，传统加速器PE利用率仅25%，DRAM带宽持续闲置，算力与存储资源严重失衡。
3. 现有KV量化方案引入大量浮点乘加，硬件效率差；KV丢弃剪枝易丢失远期语义，长文本任务精度衰减明显。
4. 现有硬件串行执行QKV生成与注意力计算，无法并发计算密集与访存密集算子，批次越大资源浪费越严重。
5. 缺少算法压缩与硬件调度协同设计方案，无法同时解决KV访存爆炸、硬件利用率双痛点。

## 相关工作
1. LLM专用加速器（Tender/OPAL/MECLA）：仅做权重量化/分解优化，未针对性缓解KV缓存海量访存，注意力PE利用率极低。
2. KV量化算法（KIVI/NINT2）：采用逐通道量化引入大量浮点运算，硬件开销高，长文本精度损失明显。
3. KV剪枝算法（H2O/QUEST）：仅依据历史注意力丢弃token，无法预判未来关键token，高压缩率下语义丢失严重。
4. 通用Transformer硬件：无混合精度、稀疏KV专用计算单元，不支持量化+剪枝联合推理流水线。
5. 单优化算法方案：仅单独压缩KV或优化硬件调度，未实现软硬件协同增益。

## 本文解决方案
### 1 DS差分显著token感知量化算法
K采用窗口基准差分量化，基准token存INT8，差值token仅2bit；V按token重要度分通道量化，关键通道8bit、次要2bit，大幅减少浮点计算开销。
### 2 HCAP历史-当前联合注意力剪枝
结合历史累积注意力与当前预估分数双重筛选，先裁剪低贡献KV通道，再仅保留top-k关键token参与当前注意力计算，在高压缩率下减少语义丢失。
### 3 OFBI算子融合+跨批次交织硬件调度
内核内部融合QK计算、Top-k筛选、Softmax、缓存压缩算子，消除流水线气泡；多批次间并发执行计算密集QKV生成与访存密集注意力，同步提升PE与带宽利用率。
### 4 多核心混合精度专用加速器
多矩阵核心搭配独立MHA稀疏计算核，内置DSQ量化器、HCAP剪枝Top-k选择单元；采用输出静态数据流与分层片上SRAM，适配压缩KV存取。
### 5 两阶段推理流水线
预计算阶段用基准K预估注意力筛选候选token；正式计算仅加载少量KV完成注意力输出，迭代更新历史注意力分数用于下一轮压缩。

## 实验分析
1. 实验环境：Llama2/LongChat/Vicuna三类7B长上下文模型，LongBench多任务评测；28nm工艺综合，对比Tender、OPAL、MECLA。
2. 算法压缩效果：KV缓存外部访存压缩率超91%，长文本问答/摘要任务精度损失低于6%，显著优于KIVI、H2O等SOTA。
3. 硬件利用率提升：OFBI策略将注意力PE利用率从25%提升至93%，QKV带宽利用率由25%升至67%。
4. 硬件PPA指标：芯片面积4.83mm²，功耗717mW，峰值3287GOPS，能效4584GOPS/W。
5. 整体加速：相比主流加速器吞吐量最高提升7.32倍，能效提升5.52~8.38倍；上下文越长、批次越大增益越显著。

## 研究启发
1. 长LLM推理瓶颈不在模型权重而在KV缓存，必须从量化+剪枝联合压缩层面削减海量外部访存。
2. 仅依靠历史注意力筛选token存在缺陷，结合当前预估分数可大幅降低高压缩率下语义精度损失。
3. 注意力访存受限、QKV计算受限特性完全相反，跨批次交织调度可并发两类算子，充分释放硬件资源。
4. KV量化设计需对齐矩阵乘累加维度，差分量化可规避逐通道量化带来大量浮点MAC硬件开销。
5. 软硬件协同优化收益远高于单独算法或单独硬件优化，压缩算法需配套专用混合精度、稀疏计算硬件单元。