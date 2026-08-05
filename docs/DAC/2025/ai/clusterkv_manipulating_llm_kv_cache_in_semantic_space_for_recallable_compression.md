---
title: "ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable Compression"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2412.03213">https://arxiv.org/abs/2412.03213</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，KV缓存压缩，语义聚类，可召回压缩 </p>
</div>


---

## 研究概要
本文提出ClusterKV面向长上下文LLM的可召回KV缓存压缩框架，基于Key向量语义聚类替代固定分页筛选。利用余弦距离K-means划分语义簇，仅计算簇中心注意力大幅降低筛选开销，配套异步聚类、GPU定制内核与簇级缓存。32k上下文仅1k-2k缓存预算，推理提速2倍、吞吐提升2.5倍，精度损失极小，优于Quest、InfiniGen。

## 背景和动机
1. 长上下文LLM推理中KV缓存随序列线性膨胀，占用大量GPU显存，解码阶段访存延迟成为核心瓶颈。
2. 传统KV压缩永久淘汰低权重token，但token重要性随解码动态变化，早期低权后续可能关键，永久丢弃大幅损害生成质量。
3. 现有可召回方案Quest按文本连续分页划分，页面内存在大量无效token，缓存预算碎片化、利用率低。
4. InfiniGen等方法逐token计算注意力，筛选开销与序列长度线性相关，抵消压缩带来的加速收益。
5. 缺乏语义感知、低开销的可召回KV缓存筛选机制，无法在极低缓存预算下兼顾推理速度与模型精度。

## 相关工作
1. 永久式KV剪枝（Keyformer/H2O）：基于单次注意力淘汰token，不可召回，长文本精度衰减严重。
2. Quest分页可召回：按固定长度分页评估页面权重，存在页面内部碎片化，缓存资源浪费。
3. InfiniGen：SVD降维Key做全局筛选，遍历全部token计算注意力，筛选计算开销过高。
4. 注意力Sink：固定保留前N个token，无法适配动态上下文语义需求。
5. KV量化压缩：仅降低单token存储位宽，不削减参与计算的token数量，无法减少注意力计算量。

## 本文解决方案
### 1 语义簇聚类筛选核心算法
以Key向量余弦相似度为度量做K-means聚类，语义相近token归入同一簇；解码仅计算簇中心注意力排序，优先选取高权重簇，按需截取token至缓存预算；固定前16个Sink token永久保留，避免关键上下文丢失。
### 2 分层聚类调度策略
Pref阶段对全部prompt Key聚类；解码每320步对新生成token增量聚类，控制聚类计算频率平衡开销；32k上下文设400簇实现精度与效率平衡。
### 3 系统级异步聚类优化
将聚类计算与层注意力、FFN、下一层QKV投影流水线重叠，隐藏聚类耗时，整体聚类开销仅占总推理2%以内。
### 4 GPU定制CUDA聚类内核
多头批量并行处理，通道分块+共享内存原子累加更新簇中心，降低内存冲突，大幅加速K-means迭代。
### 5 簇粒度缓存与索引机制
维护GPU簇级缓存复用历史KV；通过簇大小前缀和快速索引token位置，超出预算时截断最后一簇多余token，减少CPU-GPU数据传输。

## 实验分析
1. 实验设置：GLM4-9B、Llama3.1-8B、OPT-6.7B，LongBench八类长文本评测，上下文最高32k，对比Quest、InfiniGen。
2. 精度表现：1024/2048缓存预算下分数接近全KV基线，困惑度偏差≤0.5；重要token召回率显著高于分页方法。
3. 推理性能：32k上下文解码延迟最高提速2倍，吞吐提升2.5倍；聚类开销仅占prefill 6%-8%。
4. 缓存收益：簇级缓存命中率63%-74%，减少大量CPU向GPU传输KV的耗时。
5. 消融验证：余弦距离优于L2/内积；簇数量400为最优平衡点，分页式碎片化缺陷明显。

## 研究启发
1. token注意力由语义相似度决定，基于Key向量聚类而非文本位置筛选，能显著提升缓存预算利用率。
2. 可召回KV压缩无需遍历所有token，以簇中心替代单token计算注意力，可大幅削减筛选计算开销。
3. 异步流水线+定制GPU内核能掩盖聚类额外开销，让语义聚类方案工程落地可行。
4. 长上下文推理缓存优化不能只做静态剪枝，动态可召回机制是保障问答、摘要等任务精度的关键。
5. 分层增量聚类、簇级缓存复用可协同降低显存占用与数据传输开销，适配边缘/单GPU长文本部署。
