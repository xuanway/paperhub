---
title: "BlockPIM: Optimizing Memory Management for PIM-enabled Long-Context LLM Inference"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# BlockPIM: Optimizing Memory Management for PIM-enabled Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133193">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133193</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内处理，大语言模型推理，内存管理，长上下文，跨通道块布局</p>
</div>


---

## 研究概要
本文提出BlockPIM跨通道分块内存管理方案，面向长上下文LLM存内推理。设计跨通道KV分块布局，配套轻量化硬件修改与跨通道注意力归约计算，解决现有PIM内存碎片、前缀缓存冗余、上下文长度受限三大痛点。多长文本数据集测试，相较SOTA PIM方案平均吞吐量提升62%。

## 背景和动机
1. LLM解码阶段KV缓存访存密集，传统PIM采用Req/Req-Head布局，单个请求KV全部存放于单通道，通道剩余空间碎片化，内存利用率仅79.57。
2. 现有PIM各通道内存隔离，前缀缓存共享KV无法跨通道复用，产生重复存储与Prefill冗余计算，大幅降低缓存命中率。
3. 单通道容量约束模型支持上下文上限，Llama-3.1 70B仅支持25.6K，远低于模型原生128K能力。
4. 现有PIM注意力计算仅限单通道完成全局Softmax，无法拆分KV至多通道并行，难以适配超长序列推理。

## 相关工作
1. 通用GPU内存布局：通道交织存放KV，内存利用率高，但无片内GEMV/Softmax计算，带宽瓶颈严重。
2. NeuPIMs(Req-Par)：单请求KV独占通道，通道并行计算，但碎片严重、前缀缓存跨通道不可共享、上下文受限。
3. AttAcc(Req/Head-Par)：按注意力头拆分KV分配多通道，GQA模型下等效Req-Par，仍存在碎片与缓存冗余问题。
4. 传统Prefix Caching：面向统一全局内存，无法适配PIM通道隔离存储架构，直接移植收益大幅衰减。

## 本文解决方案
### 1. 跨通道分块KV内存布局
将请求KV切分为固定token块，贪心分配至当前占用最低通道，打破单通道存储限制；全局统一块管理，共享前缀KV可跨通道复用，消除碎片与冗余存储。
### 2. 轻量化PIM硬件改造
仅修改Softmax单元，新增m(全局最大值)、d(归一化分母)缓存通路，通道计算后同步输出中间参数至XPU，硬件改动极小。
### 3. 跨通道分布式注意力算法
各通道独立完成局部QKᵀ、Softmax、S×V并输出局部Oᵢ、mᵢ、dᵢ；XPU汇总全局m、d，对各通道局部结果校正归约，保证注意力计算数学正确性。
### 4. 适配DRAM行粒度的分块尺寸设计
块大小匹配Bank行存储容量，减少行切换延迟，K/V分存不同行，利用Softmax计算隐藏访存延迟。

## 实验分析
1. 仿真环境：Ramulator+LLMCompass搭建周期级模拟器，测试ShareGPT/Mooncake/LooGLE等长短文本数据集，基线为GPU、AttAcc、AttAcc-PC。
2. 内存指标：内存利用率大幅提升，消除单通道容量约束，Llama-3.1系列可支持百万级上下文长度。
3. 吞吐量：全数据集平均吞吐量提升62%；超长前缀LooGLE场景加速可达12.2倍，短文本ShareGPT小幅损耗额外计算开销。
4. 扩展性：通道数量提升时性能稳定上升，AttAcc-PC长上下文场景随通道增加性能下滑，BlockPIM无此缺陷。
5. 开销：仅传输m、d两个标量附加数据，跨通道归约计算量极低，额外通信与计算代价可忽略。

## 研究启发
1. 现有PIM单通道独占KV的布局是长上下文推理核心瓶颈，细粒度跨通道分块可同时解决碎片、缓存复用、长度限制三大问题。
2. 分布式Softmax不能直接累加局部输出，必须传递归一化中间参数做全局校正，才能保证注意力精度无损。
3. PIM硬件优化无需大规模重构，仅扩展Softmax少量缓存通路即可支持跨通道并行，改造成本极低。
4. 前缀缓存的收益高度依赖全局统一内存寻址，隔离式通道架构会大幅削弱缓存效果，跨通道共享是关键改进方向。
5. 内存布局设计需结合DRAM物理行访问特性，分块尺寸对齐存储粒度可隐藏行切换延迟，进一步提升推理吞吐。