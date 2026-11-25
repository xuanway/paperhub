---
title: "DIAS: Distance-based Attention Sparsity for Ultra-Long-Sequence Transformer with Tree-like Processing-in-Memory Architecture"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DIAS: Distance-based Attention Sparsity for Ultra-Long-Sequence Transformer with Tree-like Processing-in-Memory Architecture


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133343">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133343</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>人工智能，机器学习，架构与系统设计 </p>
</div>

---

## 研究概要
本文提出软硬件协同DIAS框架，包含基于图近似近邻的AKAttention稀疏注意力算法与树形TreePIM存内架构。构建K图筛选Top-K键向量，将解码复杂度降至O(1)；树型交换机扩展大容量高带宽KV缓存。在Llama3-405B百万序列测试，最高提速171.7倍，精度损失小于1%。

## 背景和动机
1. 超长上下文LLM解码阶段KV缓存体量巨大，传统完整注意力O(L²)复杂度引发严重内存带宽与容量双重瓶颈，算力受限。
2. 现有窗口、H2O等启发式稀疏方法粗暴丢弃历史Token，百万长文本下精度下降超30%，无法兼顾吞吐与准确率。
3. 主流PIM加速器仅优化固定注意力计算，未适配动态稀疏KV检索，片间通信开销大，容量与带宽难以同时兼顾。
4. 量化、推测解码等优化手段存在固有精度或能耗代价，缺少算法+硬件协同的长上下文完整加速方案。

## 相关工作
1. 启发式稀疏注意力（Window/StreamLLM/H2O）：按位置或权重裁剪KV，长序列全局信息丢失严重，精度衰减剧烈。
2. ToPick类KV筛选算法：仅简单概率预估裁剪，压缩比例有限，无法挖掘Query-K向量空间相似性。
3. 通用Transformer PIM（AttAcc/NeuPIMS）面向完整稠密注意力，无图检索稀疏硬件支持，KV片间搬运开销高。
4. ANNS存内加速（NDSearch/Pyramid）仅针对检索任务，未与LLM注意力解码数据流融合。

## 本文解决方案
### 1. AKAttention距离感知稀疏注意力算法
Prefill阶段构建K图，以内积距离表征键向量相关性；迭代图搜索筛选Top-K相关键，仅参与注意力计算；动态更新K图，剪冗余边，单次Token生成复杂度降为O(1)，精度损失<1%。
### 2. TreeP树形存内架构
二叉交换机连接多层PIM叶子单元，轻量索引跨树传输，高维KV内积并行在PIM完成；设计S/L/LL三级内存管理模式适配不同序列规模。
### 3. P/D分离软硬件协同流水线
主机完成QKV生成、K图更新；TreePIM隔离海量KV访存，交换机内置双调排序单元汇总内积分数，计算与图更新时间重叠。
### 4. 负载均衡调度
KV缓存交错/随机均匀分发至各PIM，交换机动态更新路由查表，平衡各单元计算访存负载。

## 实验分析
1. 测试基准：Longbench多任务数据集，Mistral-7B、Llama3.1-8B/405B，序列长度100k~1M，28nm PIM电路仿真。
2. 精度表现：同等Top-K配置下，相较传统稀疏方法精度降幅控制在1%内，基线窗口注意力精度下跌超30%。
3. 吞吐加速：1M上下文405B模型相对传统方案提速171.7倍，100k 8B模型提速25.3倍。
4. 能效指标：405B场景能效提升1.7倍，100k场景提升5.0倍，显著优于Window、ToPick等SOTA。
5. 消融对比：单独AKAttention或TreePIM收益有限，二者协同才能突破带宽-容量双重瓶颈。

## 研究启发
1. 长上下文注意力瓶颈根源是全局KV读取，利用向量相似度做图检索稀疏可在几乎无损精度下大幅削减访存量。
2. 树形分层PIM架构可分离轻量索引与高带宽KV计算，同时解决存储容量与片内带宽矛盾。
3. 传统位置式稀疏裁剪会丢失全局依赖，基于内积距离的图检索能保留关键历史信息，是长文本稀疏最优路径。
4. 算法稀疏逻辑需配套专用存内硬件，单纯软件稀疏无法消除KV缓存跨芯片传输开销。
5. K图动态边剪枝可维持检索效率，分层内存管理模式能自适应不同规模大模型推理负载。