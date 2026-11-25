---
title: "UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.07479">https://arxiv.org/abs/2504.07479</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 统一内容寻址存储器，存内计算架构，静态与动态KV缓存剪枝，铁电场效应晶体管，大语言模型推理，稀疏注意力加速</p>
</div>

---

## 研究概要
本文提出基于FeFET的UniCAIM统一CAM/CIM架构，融合静态-动态KV缓存剪枝适配长上下文LLM。设计三种工作模式：CAM快速Top-k动态筛选、电荷域CIM累计分数静态淘汰、电流域精确注意力计算。电路测试AEDP相较主流CIM加速器降低8.2~831倍，长文本任务精度接近完整缓存基线。

## 背景和动机
1. 长上下文LLM推理中KV缓存占用海量存储，注意力计算呈二次复杂度，成为时延、功耗核心瓶颈。
2. 现有CIM加速器仅支持单一剪枝策略：固定静态剪枝精度损失大，动态剪枝依赖复杂Top-k电路，开销极高。
3. 缺乏可同时执行静态、动态双剪枝的统一存储计算硬件，无法同步压缩内存与计算量。
4. 传统CIM单元不支持带符号多比特KV存储，近似相似度匹配与精确注意力无法在阵列内原位完成。

## 相关工作
1. 固定静态剪枝CIM（TranCIM）：采用StreamingLLM固定窗口剪枝，适配场景有限，长文本精度衰减严重。
2. 动态剪枝CIM（CIMFormer）：串行排序实现Top-k，O(nlogn)复杂度，额外电路带来巨大时延能耗。
3. RRAM稀疏CIM（Sprint）：仅支持单一种类近似匹配，无法累计注意力分数用于静态淘汰。
4. 通用Transformer存内加速器：无CAM快速检索能力，全部注意力均需ADC量化，模数转换开销占比极高。

## 本文解决方案
### 1 混合静态-动态KV剪枝算法
Prefill阶段一次性静态删除低累计分数token；解码阶段先用CAM快速筛选Top-k做精确计算，缓存溢出时按累计分数静态淘汰，固定KV占用空间。
### 2 FeFET统一UniCAIM存储单元
双1T1F互补单元，利用FeFET多阈值实现带符号多比特Key原位存储，并行完成Key-Query有符号乘运算。
### 3 三模式阵列协同硬件
1.CAM模式：感测线放电速度表征相似度，O(1)并行完成Top-k动态筛选；2.电荷域CIM：电荷共享累计注意力分数，实现静态淘汰；3.电流域CIM：线性读出电流，ADC量化精确注意力。
### 4 协同外设电路
配套动态阈值FeFET、电荷共享电容、多路选择器，三种模式共享同一存储阵列，无需分块独立硬件。

## 实验分析
1. 仿真平台：45nm HSPICE+FeFET Preisach器件模型，测试LongChat-7B长文本问答数据集。
2. 电路指标：3-bit单元下AEDP相较CIMFormer降低831倍，推理时延最低缩至基线0.06倍，能耗最高降至3.7%。
3. 面积能耗：静态剪枝大幅削减阵列器件数量，CAM模式规避大量ADC采样开销。
4. 模型精度：HotpotQA、NarrativeQA任务，低缓存占用下F1显著优于SnapKV、StreamingLLM。
5. 消融实验：CAM动态筛选、电荷域静态淘汰、多比特FeFET单元三者协同才能达到最优综合收益。

## 研究启发
1. LLM稀疏加速需软硬件协同，统一阵列融合CAM检索与CIM计算可避免多硬件冗余开销。
2. FeFET多级阈值特性天然适配带符号KV存储，可同时实现近似匹配与精确乘加。
3. 静态、动态两类KV剪枝不可二选一，组合策略能同步降低存储占用与单次计算量。
4. 利用器件模拟特性做相似度粗筛，可大幅减少高成本ADC模数转换次数。
5. 长上下文推理瓶颈不只是GEMV运算，KV缓存管理与稀疏筛选硬件同等关键，需一体化设计。
