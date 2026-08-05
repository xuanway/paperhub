---
title: "HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.05897">https://arxiv.org/abs/2504.05897</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/PKU-SEC-Lab/HybriMoE">https://github.com/PKU-SEC-Lab/HybriMoE</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合专家模型，CPU-GPU协同调度，缓存管理，推理加速 </p>
</div>


---

## 研究概要
本文提出HybriMoE混合CPU-GPU推理框架，解决MoE专家激活不稳定、异构负载失衡问题。设计分层动态调度、收益驱动预取、路由分数缓存三大优化，基于kTransformers实现。在Mixtral/Qwen2/DeepSeek三类MoE模型验证，相较SOTA，Prefill平均提速1.33倍，Decode平均提速1.70倍。

## 背景和动机
1. MoE大模型参数量庞大，单GPU内存不足需将专家卸载至CPU内存，PCIe数据传输成为核心延迟瓶颈。
2. 现有CPU-GPU混合方案采用静态任务分配，MoE专家激活分布均匀、波动剧烈，静态策略造成CPU/GPU资源大量闲置。
3. 传统LFU/LRU缓存未利用MoE门控路由分数，缓存命中率低，频繁触发专家加载。
4. 相邻层专家激活存在时序相关性，但现有预取未量化预取收益，盲目预取加剧带宽占用。
5. Mo包含共享/路由两类专家、负载差异大，缺乏分层动态负载均衡调度机制。

## 相关工作
1. 静态混合推理（llama.cpp）：固定层分配CPU/GPU，无法适配动态专家负载，资源利用率低。
2. AdapMoE：仅GPU端自适应预取，无CPU协同计算，卸载优化不足。
3. kTransformers/Fiddler：支持CPU辅助计算，但调度静态、缓存采用通用LFU，未适配MoE激活特性。
4. PowerInfer/Caraserve：面向稠密模型/LoRA，依赖高度倾斜激活分布，不适配MoE均匀激活模式。
5. 通用专家预取方案：仅简单预取相邻层专家，不量化收益，易造成带宽浪费。

## 本文解决方案
### 1 层内动态异构调度机制
定义GPU/CPU/传输三级优先级规则，仿真多任务时序分配：GPU优先缓存高负载专家，CPU优先低负载未缓存专家，PCI优先传输高负载专家；迭代模拟执行时序最小总延迟，均衡异构负载。
### 2 收益驱动跨层预取
复用门控信息预测后续三层候选专家，仿真预取带来的整体延迟降幅，仅预取收益最高的专家，避免无效带宽占用。
### 3 基于路由分数MRS缓存替换策略
设计Minus Recent Score缓存算法，融合历史路由分数计算专家优先级，优先保留高分专家；相比LRU/LRU大幅提升小缓存下命中率。
### 4 完整系统实现
基于kTransformers与llama.cpp内核改造，采用多CUDA流并行CPU/GPU/PCI传输，搭配Marlin 4bit量化降低专家存储开销，兼容含共享专家的各类MoE架构。

## 实验分析
1. 实验环境：Xeon CPU + RTX A600 GPU；测试Mixtral、Qwen2、DeepSeek三类Mo，基线llama.cpp、AdapMoE、kTransformers。
2. 速度提升：对比kTransformers，Prefill平均1.33倍加速，Decode平均1.70倍加速；消融显示调度是核心增益来源。
3. 缓存性能：低缓存容量（25%）下MRS较LRU命中率提升6%~8，缓存越紧缺优势越明显。
4. 阶段消融：调度单独带来Prefill 1.26×、Decode 1.46×加速；缓存与预取进一步叠加收益。
5. 模型泛化：在小专家Mixtral、多专家带共享DeepSeek/Qwen2上均稳定提速，适配不同MoE结构。

## 研究启发
1. MoE激活分布区别于稠密网络，不能直接复用面向极度稀疏神经元的静态卸载方案，动态调度是异构加速核心。
2. 门控路由分数是Mo独有先验信息，可构建专用缓存策略，显著缓解专家频繁加载问题。
3. 预取不能盲目执行，需量化时序收益筛选高价值专家，否则会恶化PCI带宽瓶颈。
4. CPU适合分担低负载未缓存专家计算，GPU专注高负载常驻专家，分层优先级可最大化并行重叠度。
5. 混合推理框架需区分Prefill与Decode两类负载特征，两套优化逻辑协同才能全面降低TTFT与单Token延迟。
