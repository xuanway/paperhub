---
title: "CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs

<!-- <div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 DAC 2025（第62届），所属 Track: Design。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Design</p>
</div> -->


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.06625">https://arxiv.org/abs/2505.06625</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高速缓存, 多租户, 深度神经网络, 神经网络处理器, 片上系统</p>
</div>

**会议**: DAC 2025

**专题**: [DES1: SoC, Heterogeneous, and Reconfigurable Architectures](https://62dac.conference-program.com/)

**论文链接**：[https://arxiv.org/abs/2505.06625](https://arxiv.org/abs/2505.06625)

**关键词**: 高速缓存, 多租户, 深度神经网络, 神经网络处理器, 片上系统 

---

## 研究概述

> 本文针对集成神经网络处理器（NPU）片上系统（SoC）多租户深度神经网络（DNN）共享高速缓存冲突、缓存效率低下问题，提出软硬件协同设计CaMDN。硬件增设专属控制器划分模型隔离缓存区；软件提供缓存感知映射与动态分配算法。实验表明该方案平均访存减少33.4%，模型加速最高2.56倍，硬件面积开销可忽略。

## 方法简述

- 识别该方向中的关键性能、能效或设计自动化瓶颈。
- 通过软硬件协同或 EDA 工具链优化构建可落地方案。
- 在典型工作负载上进行评估并分析设计权衡。

## 主要结果

- 在目标指标（性能、能效或设计质量）上相对基线实现改进。
- 展示了与现有 EDA 或系统栈集成的可行性。
- 为后续扩展和工程化部署提供依据。
