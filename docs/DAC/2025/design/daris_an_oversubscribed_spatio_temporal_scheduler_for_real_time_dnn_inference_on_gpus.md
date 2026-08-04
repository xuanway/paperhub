---
title: "DARIS: An Oversubscribed Spatio-Temporal Scheduler for Real-Time DNN Inference on GPUs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DARIS: An Oversubscribed Spatio-Temporal Scheduler for Real-Time DNN Inference on GPUs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.08795">https://arxiv.org/abs/2504.08795</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 实时调度，深度神经网络推理，GPU时空共享，资源超订，截止时间</p>
</div>


---

## 研究概要
本文提出DARIS实时多租户GPU调度器，基于MPS+CUDA流实现空间超分共享，分段暂存实现时序粗粒度抢占，动态MRET替代保守WCET预测。在无批量场景下吞吐量较基线批处理提升15%、优于SOTA调度11.5%，高优先级任务无超时，低优先级丢期率低于2%。

## 背景和动机
1. 实时DNN推理无法等待输入批量，传统单租户GPU资源闲置严重，多租户隔离调度吞吐低下。
2. 现有GPU调度要么牺牲吞吐保证执行时间，要么WCET预估过于悲观，缺乏适配软实时的动态时序预估方案。
3. 缺少对GPU SM超订阅机制系统量化分析，MPS、CUDA流两种空间划分组合的优劣无完整对比。
4. 多数调度仅全局任务级抢占，无法分层管控网络层内内核，高优先级任务响应延迟难以保障。

## 相关工作
1. 批量推理服务器（GSlice）：依赖输入批处理提升吞吐，不适用于低延迟实时业务，无优先级保障。
2. 实时GPU调度Clock：单任务独占GPU换取时序可预测，硬件利用率极低。
3. SGPRS/Laius：初步探索SM超订阅，但未结合时序分段抢占，缺少两级优先级管控。
4. RTGPU：支持多租户但无分层阶段调度，高低优先级任务无差异化保障，丢期率最高11%。

## 本文解决方案
### 1. 时空联合超订阅调度架构
空间层融合MPS多上下文与CUDA流做SM超分共享；时序层提出Staging分段机制，将DNN切分阶段，仅在分段边界支持粗粒度抢占。
### 2. MRET动态执行时长预估
抛弃保守WCET，滑动窗口统计各阶段近期最大执行时间，动态更新任务利用率，适配负载波动。
### 3. 离线负载均衡+在线准入调度
离线基于AFET预分配上下文均衡负载；在线基于剩余利用率做低优任务准入，超载支持跨上下文零拷贝迁移。
### 4. 多级阶段优先级策略
阶段分层优先级：高优任务全局优先，任务末段升权、前序丢期子阶段升权，同层级采用EDF调度。
### 5. 三种调度策略实现
独立流STR、纯MPS、MPS+流混合模式，适配有无MPS硬件的不同GPU环境。

## 实验分析
1. 实验平台：RTX 2080 Ti，ResNet18/UNet/InceptionV3三类DNN，2:1高低优任务配比，150%过载负载。
2. 吞吐表现：MPS策略性能最优，无批量时ResNet吞吐超批处理基线13%，整体较GSlice提升11.5%。
3. 时序指标：高优任务无截止丢失；STR丢期接近0，MPS低优丢期最高7%、最优配置不足2%；高优响应速度快低优33%。
4. 超订阅效果：OS=2（200%）综合收益最佳，隔离OS=1吞吐大幅下滑。
5. 消融测试：分段机制缺失吞吐下降33，阶段升权策略显著降低连锁丢期。

## 研究启发
1. GPU实时推理无需依赖输入批量，SM超订阅+分层阶段抢占可在保障时延前提下超越批处理吞吐。
2. 固定悲观WCET不适合软实时场景，滑动窗口MRET动态预估可大幅提升硬件承载上限。
3. MPS负责空间资源复用、分段抢占管控时序优先级，二者结合是多租户实时最优组合。
4. 仅全局抢占粒度过粗，按网络层切分阶段并差异化升权，能有效避免连锁截止丢失。
5. 超订阅并非越高越好，200% SM共享是吞吐与时延的最优平衡点，过度共享加剧资源争抢。