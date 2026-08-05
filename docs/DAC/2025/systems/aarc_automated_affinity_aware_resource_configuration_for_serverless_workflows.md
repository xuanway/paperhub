---
title: "AARC: Automated Affinity-aware Resource Configuration for Serverless Workflows"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# AARC: Automated Affinity-aware Resource Configuration for Serverless Workflows

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS6: Time-Critical and Fault-Tolerant System Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132894">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132894</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>无服务器计算，资源配置，自动化 </p>
</div>

---

## 研究概要
本文提出AARC亲和感知无服务工作流自动资源配置框架，解耦CPU与内存分配。由图调度器提取DAG关键路径，优先级配置器分层寻优，严格满足端到端SLO。在三类典型工作流测试，相较贝叶斯优化、MAFF梯度下降，搜索耗时降低85.8%~89.6%，运行成本削减49.6%~61.7%。

## 背景和动机
1. 主流无服务平台CPU内存绑定分配，算力/内存负载不匹配场景资源严重浪费，单函数解耦方案无法适配DAG工作流。
2. CPU内存完全解耦后配置空间爆炸，传统贝叶斯优化采样迭代多、收敛慢、成本波动剧烈，搜索效率极低。
3. 现有优化方法只针对独立函数，忽略工作流关键路径时延约束，无法拆分子路径SLO，易出现整体超时。
4. 梯度类方案强制内存CPU比例，本质仍绑定资源，难以挖掘低内存高算力等最优异构配置。

## 相关工作
1. 单函数资源优化（Bilal贝叶斯优化）：仅面向独立函数，工作流场景搜索空间爆炸、收敛不稳定。
2. MAFF梯度下降：采用CPU内存比例绑定搜索，容易陷入局部最优，成本优化上限低。
3. SLAM/StepConf等工作流优化：仅调整内存，不支持CPU内存解耦，资源调度灵活性差。
4. 在线动态调整框架Sizeless/FaaSDeliver：依赖持续监控，运行时额外开销大，离线自动配置能力不足。

## 本文解决方案
### 1 加权DAG图中心调度器
对工作流插桩得到各函数运行时延，构建加权有向图，提取全局关键路径；基于关键路径拆分分支子路径，分配对应子SLO，保证整体时延约束。
### 2 优先级资源配置器
采用优先队列管理CPU/内存缩减操作，逐步下调资源配额；若违反SLO或成本上升则回退资源，搭配步长退避机制加速收敛。
### 3 分层两级调度算法
先优化关键路径资源，再逐个子路径独立寻优；已调度函数不再重复处理，避免资源冲突与重复采样。
### 4 输入感知扩展插件
针对视频等输入敏感工作流，按数据规模预生成多套最优资源模板，请求到来时动态匹配配置。

## 实验分析
1. 测试负载：聊天机器人、机器学习流水线、视频分析三类DAG工作流，基线为贝叶斯优化、MAFF梯度下降。
2. 搜索效率：相比贝叶斯优化搜索耗时降低85.8%~89.6%，采样迭代大幅减少，成本收敛更平稳。
3. 成本收益：满足SLO前提下，对比BO成本平均降49.6%，对比MAFF平均降61.7%。
4. 输入敏感测试：视频工作流轻/重输入场景，相比基线成本最高降低89.9%，全程不触发SLO违规。
5. 约束验证：所有配置方案均满足预设端到端时延阈值，无超时情况。

## 研究启发
1. 无服务工作流优化不能统一遍历全部配置，关键路径拆分可大幅缩减有效搜索空间。
2. CPU内存完全解耦是降低运行成本核心，比例绑定方案会天然丢失最优异构资源组合。
3. 优先队列渐进资源缩减+回退机制，比全局贝叶斯采样收敛速度、稳定性更优。
4. 工作流时延约束需分层拆解为子路径SLO，单独优化分支不破坏整体时延上限。
5. 输入数据规模显著影响最优资源配比，离线预生成多模板可进一步提升线上运行性价比。