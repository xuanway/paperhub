---
title: "ReChisel: Effective Automatic Chisel Code Generation by LLM with Reflection"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# ReChisel: Effective Automatic Chisel Code Generation by LLM with Reflection

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.19734">https://arxiv.org/abs/2505.19734</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，Chisel代码生成，反射机制，逃逸机制 </p>
</div>


---

## 研究概要
本文提出ReChisel智能体系统，面向LLM自动生成Chisel代码。设计编译+仿真双反馈反思迭代机制，新增循环逃逸模块解决迭代停滞问题。在216组标准电路测试，多款大模型生成成功率提升10%~50%，性能对标顶尖Verilog自动生成框架AutoChip。

## 背景和动机
1. Chisel作为高阶硬件描述语言代码开源量仅为Verilog的1/20，LLM零样本生成效果极差，语法、功能错误占比极高。
2. 现有LLM硬件生成工具仅针对Verilog，缺乏适配Chisel编译链的迭代修正框架。
3 单纯单次生成无法修复Chisel特有的类型、赋值、时钟域语法错误，迭代过程易陷入重复纠错的无进展死循环。
4. 缺少区分编译语法、仿真功能两类错误的差异化反馈优化策略，纠错效率低下。
5. 业界未验证“先生成Chisel再转Verilog”自动化流程的可行性与性能上限。

## 相关工作
1. LLM Verilog生成框架（AutoChip、VerilogCoder）：依托仿真反馈迭代优化，但不兼容Chisel/FIRRTL编译链路。
2. ChatChisel：仅简单利用LLM生成Chisel，无反思迭代与死循环逃逸机制，纠错能力弱。
3. 各类RTL基准数据集（RTLLM、VerilogEval）：仅面向Verilog评测，缺少Chisel专用测试集。
4. LLM反思通用算法（Reflexion、React）：软件代码场景适用，未适配Chisel硬件语法约束。
5. Chisel/FIRRTL编译工具链：仅做代码转译，不具备自动纠错、迭代生成能力。

## 本文解决方案
### 1 完整ReChisel智能体流水线
包含生成器、编译器、仿真器、检查器、评审器五大LLM/工具模块，接收需求与测试用例循环迭代生成Chisel代码，直至编译仿真全部通过。
### 2 差异化反思反馈机制
区分编译语法错误、仿真功能错误两类反馈：语法错误提取报错行与修复提示；功能错误对比输入输出波形差异，搭配上下文示例少样本学习加速修正。
### 3 无进展循环逃逸机制
检查器记录全迭代错误轨迹，检测到重复同类纠错循环时丢弃循环内所有迭代记录，重新生成全新修正方案跳出死锁。
### 4 Chisel专属错误知识库
整理信号类型、IO封装、组合环路、数组索引等高频错误样例，作为上下文提示注入评审器，降低重复语法失误。
### 5 标准化评测方案
融合HDLBits、VerilogEval、RTLLM筛选216组兼容Chisel测试用例，采用Pass@1/5/10指标量化生成成功率。

## 实验分析
1. 实验配置：5款主流LLM（GPT4系列、Claude3.5），最大迭代次数10，216组硬件模块测试用例。
2. 基线对比：零样本Chisel生成远差于Verilog，Claude3.5 Sonnet基线Pass@1仅33.33%。
3. 迭代增益：ReChisel迭代后Sonnet Pass@1达84.98%，整体成功率提升10%~50%；4轮迭代后性能趋于平稳。
4. 横向对标：ReChisel生成Chisel的指标接近AutoChip直接生成Verilog，GPT-4o下部分指标更优。
5. 错误变化：迭代过程语法、功能错误比例持续下降，仅少量场景修复功能时引入新语法问题。

## 研究启发
1. 高阶HDL Chisel虽开源数据稀缺，但配套编译仿真反馈的迭代智能体可大幅弥补LLM原生生成短板。
2. 硬件语言纠错需区分编译静态、仿真动态两类错误，差异化反馈策略能显著提升修正效率。
3. LLM迭代易陷入语法死循环，轨迹追踪+方案重置的逃逸机制是迭代框架必备核心模块。
4. 构建领域专属高频错误知识库，通过上下文少样本学习可大幅降低重复低级硬件语法错误。
5. 先生成Chisel再编译转Verilog的自动化硬件流程具备工业落地潜力，不输直接生成Verilog方案。
