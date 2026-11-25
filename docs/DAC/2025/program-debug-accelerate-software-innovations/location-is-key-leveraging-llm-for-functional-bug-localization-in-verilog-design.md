---
title: "Location is Key: Leveraging LLM for Functional Bug Localization in Verilog Design"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Location is Key: Leveraging LLM for Functional Bug Localization in Verilog Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133280">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133280</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>大语言模型，Verilog功能错误定位，持续预训练，强化学习优化定位 </p>
</div>

---

## 研究概要
本文基于Deepseek-Coder-16B提出LiK专用大模型，面向Verilog功能故障精准定位。采用持续预训练、监督微调、SimPO强化学习三阶段训练，无需Testbench等EDA验证工具。测试pass@1达93.33%，超越Strider、GPT-o1、Claude3.5；嵌入MEIC修复框架后漏洞修复成功率由76.47%提升至90.54%。

## 背景和动机
1. Verilog功能故障可通过编译仿真，隐蔽性强；传统定位工具Strider依赖测试激励，仅输出可疑代码段，无法精准锁定单行。
2. 现有硬件专用LLM聚焦代码生成，缺少面向故障定位领域适配；商用通用LLM定位精度不足，推理输出格式混乱。
3. 硬件行业Verilog开源数据稀缺，领域训练素材匮乏，直接微调通用代码模型易出现过拟合。
4. 传统调试流水线缺少精准定位前置模块，修复模型需遍历大量可疑代码，修复效率低下。
5. 现有LLM调试方案未区分正负样本，无法规避高频误判代码，故障定位稳定性差。

## 相关工作
1. 传统HDL故障定位工具（Strider）：依靠波形对比筛选可疑行，依赖人工编写Testbench，输出多候选行，定位精度低。
2. Verilog专用大模型（RTLCoder、VeriSeek、VGen）：全部面向代码生成任务，无故障定位专项训练，缺陷识别能力弱。
3. 通用商用LLM（GPT系列、Claude）：支持代码分析，但未适配硬件时序、信号等领域特性，定位准确率有限。
4. LLM驱动RT调试系统（MEIC）：侧重代码迭代修复，缺少专用定位前置模块，搜索空间大、修复成功率偏低。
5. 代码领域微调方案：仅采用监督微调，未引入强化学习区分正误样本，易出现高频误识别。

## 本文解决方案
### 1 三阶段LoRA轻量化训练流水线
基于Deepseek-Coder-Lite-16B底座，全程LoRA微调防止小数据集过拟合；分为两轮持续预训练、监督微调、SimPO强化学习三步。
### 2 两轮持续预训练扩充领域知识
第一轮融合Verilog与少量C代码基础语料夯实语法；第二轮自动生成含分步推理的故障样本，覆盖运算符、位宽、边沿五类典型Verilog功能缺陷。
### 3 面向单行输出监督微调
训练输入为设计描述+缺陷代码，输出仅输出故障代码行，消除推理文本引入的训练噪声，简化模型输出约束。
### 4 SimPO偏好强化学习优化定位稳定性
构建（问题、正确行、高频误判行）三元样本，以Bradley-Terry损失拉大正误输出概率差，抑制模型常见误识别。
### 5 通用集成接口
可作为IDE插件，或嵌入MEIC等LLM修复框架，仅传入定位行即可压缩修复搜索范围。

## 实验分析
1. 评测数据集：基于RTLLM构建102例Verilog缺陷用例，覆盖五类典型功能bug，指标采用pass@1/pass@5。
2. 定位精度：LiK pass@1=93.33%、pass@5=94.10%，全面领先Claude3.5、GPT-o1与传统Strider。
3. 消融实验：仅预训练精度不足30%，监督微调提升至87.54%，强化学习进一步突破93.33%。
4. 分bug表现：数值、关键字、边沿缺陷识别最优；运算符、变量名缺陷略弱于Claude，归因领域数据量限制。
5. 下游增益：集成进MEIC后故障修复成功率从76.47%提升至90.54%，验证定位模块实用价值。

## 研究启发
1. HDL故障定位与代码生成任务目标差异极大，通用/硬件生成LLM无法直接复用，需专项领域微调。
2. 硬件行业数据稀缺场景下，LoRA微调可有效避免过拟合，自动合成推理样本能补足领域语料缺口。
3. 简化输出目标（仅输出故障行）相比链式推理文本，可降低训练噪声、大幅提升定位精准度。
4. 强化学习引入高频误判负样本，能稳定缩小pass@1与pass@5差距，提升推理鲁棒性。
5. 精准故障定位是LLM硬件自动修复的关键前置环节，可极大缩减代码修复搜索空间，提升端到端调试效率。
