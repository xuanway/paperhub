---
title: "CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.06625">https://arxiv.org/abs/2505.06625</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高速缓存, 多租户, 深度神经网络, 神经网络处理器, 片上系统</p>
</div>


---

## 研究概述

本文针对集成神经网络处理器（NPU）片上系统（SoC）多租户深度神经网络（DNN）共享高速缓存冲突、缓存效率低下问题，提出软硬件协同设计CaMDN。硬件增设专属控制器划分模型隔离缓存区；软件提供缓存感知映射与动态分配算法。实验表明该方案平均访存减少33.4%，模型加速最高2.56倍，硬件面积开销可忽略。


## 背景和动机
1. 产业趋势：集成NPU的SoC普遍采用多租户架构，单芯片并行运行多个DNN任务提升硬件利用率。
2. 现存痛点：多任务共享缓存引发严重资源争抢，缓存命中率最高下降59.7%、访存量上涨64.1%，推理延迟大幅升高。
3. 数据根源：DNN中间数据大量无复用、复用距离超长，传统透明缓存机制无法适配该特征。
4. 研究缺口：现有调度方案仅优化带宽与NPU算力，未针对性解决共享缓存低效问题。

## 相关工作
1. CPU多租户缓存优化：采用缓存分区技术，但缓存对任务透明，性能提升有限。
2. 加速器调度研究：分为带宽调度（MoCA）、算力核调度（Planaria、DREAM）、带宽+算力协同调度（AuRORA、RELMAS），均忽略缓存冲突。
3. 加速器缓存改造：实现加速器可控缓存缓冲区，但未适配DNN数据复用特征。
4. Veltair仅监测缓存冲突，无硬件优化手段，面向CPU而非NPU平台。

## 本文解决方案CaMDN（架构-调度协同设计）
### 硬件层（轻量级缓存架构）
1. 路分区隔离：共享缓存划分CPU通用空间与NPU专属子空间，消除跨类型任务争抢。
2. NEC专属控制器：为NPU提供旁路、组播高级缓存语义，绕过无复用数据、减少片上网络压力。
3. CPT缓存页表：硬件分页划分模型独占缓存区域，虚拟缓存地址实现多模型资源隔离。
### 软件调度层
1. 缓存感知映射：生成多档缓存占用映射候选，含层分块映射LBM，将中间数据常驻缓存。
2. 动态缓存分配算法：预测未来缓存占用，自适应选取匹配可用容量的映射方案，运行时动态调整各DNN缓存配额。

## 实验分析
1. 实验平台：基于Gemmini搭建Verilog硬件，45nm工艺综合；自研周期精准仿真器，选用8类CV/NLP/音频/点云DNN基准模型。
2. 对比基线：MoCA（带宽调度）、AuRORA（算力+带宽调度）、CaMDN仅硬件版本。
3. 核心性能结果：
   - 访存平均降低33.4%，推理平均加速1.88×，最高2.56×；缓存容量越大、并发模型越多优化效果越显著。
   - QoS指标大幅提升：SLA达标率、系统吞吐、公平性分别提升5.9×、2.5×、3.0×。
4. 硬件开销：CPT占NPU面积0.9%，NEC仅占缓存片0.3%，硬件成本极低可忽略。

## 研究启发
1. AI加速器多租户优化不能仅聚焦算力/带宽，共享缓存是关键性能瓶颈，需软硬件协同优化。
2. 针对DNN独有数据复用特征，应打破传统缓存透明管理模式，开放硬件缓存控制权给NPU。
3. 分层优化思路：硬件提供隔离可控缓存资源，上层调度动态适配负载波动，二者结合收益最大化。
4. 轻量化硬件扩展搭配在线动态调度，可在极低面积开销下显著提升多任务推理吞吐量与服务公平性。
