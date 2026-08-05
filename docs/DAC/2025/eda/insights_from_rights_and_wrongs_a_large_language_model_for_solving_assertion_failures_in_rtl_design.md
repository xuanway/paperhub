---
title: "Insights from Rights and Wrongs: A Large Language Model for Solving Assertion Failures in RTL Design"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Insights from Rights and Wrongs: A Large Language Model for Solving Assertion Failures in RTL Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.04057">https://arxiv.org/abs/2503.04057</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/SEU-ACAL/reproduce-AssertSolver-DAC-25">https://github.com/SEU-ACAL/reproduce-AssertSolver-DAC-25</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，断言失败解决，数据增强，从错误中学习 </p>
</div>


---

## 研究概要
本文提出面向RTL断言故障调试开源领域大模型AssertSolver，设计三段式EDA数据增强流水线构建SVA故障数据集，采用预训练-SFT-DPO三阶段训练，让模型从错误样本中学习。自研SVA-Eval基准测试，pass@1达88.54，较o1-preview提升11.97%，支持输出推理链与精准代码修复。

## 背景和动机
1. RTL仿真SVA断言失效调试高度依赖工程师人工分析信号时序逻辑，人力成本极高，缺乏自动化工具。
2. 通用大模型（GPT-4/o1-preview）无Verilog/SVA领域深度适配，硬件时序、间接故障推理能力弱，修复准确率偏低。
3. 缺少足量标注SVA故障数据集，现有HDL数据集仅含代码，无规范、日志、故障修复完整配对样本。
4. 常规微调仅学习正确案例，模型无法从自身错误中迭代优化，复杂间接故障识别效果差。
5. 无公开标准化断言调试评测基准，不同LLM对比缺乏统一、覆盖多故障类型的测试集。

## 相关工作
1. 通用代码大模型（CodeLlama、Deepseek-Coder）：通用代码能力强，缺乏RTL时序、SVA断言专业知识。
2. 商用闭源LLM（GPT4、o1、Claude3.5）：支持基础HDL调试，但硬件故障推理精度不足，无法开源微调。
3 LLM辅助断言生成研究：仅生成SVA语句，不解决断言触发后的故障定位与修复。
4. RTL代码生成LLM（RTLLM）：聚焦模块编写，不针对仿真断言失效调试场景。
5. 传统EDA调试工具：基于波形人工检索，无自动推理、代码修复能力。

## 本文解决方案
### 1 三阶段EDA专用数据增强流水线
1）过滤清洗开源Verilog代码，生成编译错误样本集；2）借助多LLM与SymbiYosys形式工具注入故障、生成SVA与仿真日志；3）生成CoT推理链并校验，划分训练/测试集，构建SVA-Bug专用数据集。
### 2 三段式分层训练框架
1）预训练：基于Verilog编译样本夯实HDL语法与时序理解；2）监督微调SFT：用故障-日志-修复样本学习标准问答范式；3）DPO偏好优化：收集SFT模型答错的困难样本，构建正误对比对训练，从错误中提升精度。
### 3 标准化输入输出范式
输入融合设计规范、故障RTL、仿真日志；输出包含故障行、修复代码、分步CoT推理，统一JSON格式便于自动化集成。
### 4 开源SVA-Eval评测基准
包含机器生成+人工真实两类案例，覆盖直接/间接、条件、变量、操作符全类断言故障，划分不同代码长度区间用于模型横向对比。
### 5 轻量化开源模型底座
基于Deepseek-Coder-6.7b微调，使用DeepSpeed ZeRO3分布式训练，硬件门槛低，完整开源模型与数据集。

## 实验分析
1. 评测指标：采用pass@1（首条修复正确）、pass@5（五条内存在正确解）量化模型调试能力。
2. 横向对比：AssertSolver pass@1=88.54%，优于o1-preview(76.57%)、Claude3.5、CodeLlama等所有基线；pass@5达90%。
3. 消融验证：仅SFT模型pass@1为84.66，增加DPO错误学习后精度提升，仅牺牲少量解多样性。
4. 故障/代码长度鲁棒性：短代码、直接故障场景pass@1超90；长代码、间接故障仍显著优于竞品。
5. 样本差异：人工真实故障集所有模型精度普遍下降约19%，但本文模型依旧保持最优水平。

## 研究启发
1. 通用代码LLM不能直接适配RTL断言调试，必须构建领域专属标注数据集做分层微调。
2. 仅学习正确样本存在性能瓶颈，引入错误样本的DPO偏好优化可大幅提升故障定位精准度。
3. 形式化EDA工具可用于自动化生成、校验HDL故障样本，低成本构建大规模领域数据集。
4. RTL故障分直接/间接等多种类型，模型评测需分层设计基准才能客观衡量真实调试能力。
5. 开源轻量化领域专用LLM可替代闭源商用大模型，降低芯片验证自动化落地成本。