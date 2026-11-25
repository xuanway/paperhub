---
title: "Introducing Instruction-Accurate Simulators for Performance Estimation of Autotuning Workloads"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Introducing Instruction-Accurate Simulators for Performance Estimation of Autotuning Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.13357">https://arxiv.org/abs/2505.13357</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 自动调优，TVM，gem5，缓存优化 </p>
</div>


---

## 研究概要
本文面向TVM自动调优硬件资源受限问题，提出仿真适配接口与仿真统计分数预测器两大方案。基于gem5指令精确仿真提取缓存、指令特征，训练MLR/DNN/贝叶斯/XGBoost预测器排序调度方案。在x86/ARM/RISC-V验证，最优调度均落在预测前3%，并行仿真可大幅缩短嵌入式设备调优耗时。

## 背景和动机
1. TVM自动调优需反复在真实硬件运行内核，系统负载、散热、缓存冲突带来测量抖动，多次重复+冷却等待极大拉长调优周期。
2. 嵌入式/RISC-V目标硬件数量稀缺，无法并行执行多调度方案，预硅软件开发阶段无实体硬件可用。
3. 周期精确仿真速度极慢，现有仿真工具无法直接对接TVM调优流程，缺少仿真与自动调优适配接口。
4. 指令精确仿真无准确周期时延输出，无法直接替代硬件测速，缺少基于仿真统计的性能排序预测方法。
5. 现有调优预测仅依托理论解析模型，未利用仿真采集缓存命中率、指令构成等细粒度硬件特征。

## 相关工作
1. TVM原生AutoTVM/AutoScheduler：完全依赖真实硬件测速，受设备数量、环境干扰限制，调优效率低下。
2. gem5/QEMU体系结构仿真：可模拟多架构CPU，但无面向编译调优的上层对接接口，仅用于架构分析。
3. 编译理论性能建模：依靠算子FLOPs、访存总量预估，忽略多级缓存冲突、分支等真实硬件行为，排序误差大。
4. 仿真性能预测类研究：仅针对单一架构，未适配TVM自动调优流水线，无法区分不同卷积内核类型。
5. 离线调度搜索优化：仅改进搜索算法，未从底层硬件测速环节降低单次方案评估开销。

## 本文解决方案
### 1 TVM仿真运行适配接口
自定义SimulatorRunner重写TVM执行器，自动生成仿真可独立执行的内核二进制；支持多仿真实例并行启动，分别适配AutoTVM手动模板、AutoScheduler自动草图两条调优流程，兼容LLVM交叉编译。
### 2 指令级仿真特征提取
基于gem5原子SimpleCPU仿真，采集各级缓存读写命中/缺失、加载/存储/分支指令占比等归一化统计特征，不依赖精确周期数值。
### 3 多类型分数预测器训练流水线
分架构、分内核类型训练MLR、DNN、贝叶斯高斯过程、XGBoost四类回归模型；以硬件实测归一化运行时为标签，输入仿真统计输出性能排序分数。
### 4 动态窗口均值近似策略
推理阶段采用静态/动态滑动窗口估算批次特征均值，解决新内核分组无全局统计、无法归一化特征的问题。
### 5 分层仿真加速流程
训练阶段少量内核同时跑硬件与仿真完成模型训练；正式调优仅运行仿真+预测器筛选，仅将预测Top-K方案落地真实硬件复测。

## 实验分析
1. 实验环境：x86 AMD、ARM树莓派4、RISC-V SiFive U74；gem5仿真平台，ResNet五类卷积内核，每组生成500套调度。
2. 预测精度：XGBoost/贝叶斯效果最优，最优调度样本预测排名≤3%，ARM/RISC-V误差低于5%，跨未知内核分组仍有效。
3. 调优速度：RISC-V场景仅3路并行仿真即可超过原生硬件串行测速速度，嵌入式设备提速收益最显著。
4. 消融对比：缓存相关统计是预测核心特征，缺失会大幅扩大排序误差；动态窗口均值不损失预测精度。
5. 多架构差异：x86因硬件复杂优化预测误差略高，精简嵌入式CPU架构预测排序更稳定。

## 研究启发
1. 指令精确仿真无需输出精准周期，仅提取缓存、指令分布统计即可完成调度优劣排序，大幅降低仿真耗时。
2. 为TVM搭建通用仿真运行接口，可解决硬件稀缺、预硅调优、并行评估三大工程痛点。
3. 无需完整精准时延预测，仅输出相对排序分数就能支撑自动调优搜索，降低建模难度。
4. 嵌入式精简CPU架构硬件行为更可控，基于仿真的性能预测效果优于复杂x86商用处理器。
5. 少量硬件实测样本训练预测器，绝大多数调度方案通过仿真筛选，仅少量候选上硬件复测，可大幅缩减调优总时间。
