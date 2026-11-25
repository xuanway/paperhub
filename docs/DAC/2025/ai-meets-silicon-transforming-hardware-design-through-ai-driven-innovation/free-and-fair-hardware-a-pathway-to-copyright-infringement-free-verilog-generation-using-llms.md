---
title: "Free and Fair Hardware: A Pathway to Copyright Infringement-Free Verilog Generation using LLMs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Free and Fair Hardware: A Pathway to Copyright Infringement-Free Verilog Generation using LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.06096">https://arxiv.org/abs/2505.06096</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，版权，Verilog </p>
</div>

---

## 研究概要
本文面向LLM生成Verilog存在IP版权侵权风险，构建版权违规评测基准，设计自动化数据集清洗流水线，产出合规开源数据集FreeSet（22万+文件），基于该数据集持续预训练得到FreeV模型。测试显示FreeV版权违规率仅3%，在VerilogEval上pass@10相较原Llama提升10.1%。

## 背景和动机
1. LLM用于Verilog生成已成EDA趋势，但现有训练数据集仅简单过滤仓库许可，未逐文件筛查版权声明，模型易记忆并输出受保护硬件IP代码，引发法律与IP盗版风险。
2. 现有Verilog数据集规模有限，且缺乏完整版权过滤流程，训练后模型版权生成违规率高，商用设计场景无法落地。
3. 缺少标准化量化指标评估LLM生成Verilog的版权侵权风险，难以横向对比各HDL大模型合规程度。
4. 开源GitHub爬虫存在接口分页、时间窗口限制，难以批量、完整抓取合规Verilog源码。
5. 重复、语法错误、私有版权代码会污染训练集，降低模型生成功能准确率，同时加剧侵权隐患。

## 相关工作
1. Verilog专用微调模型（VeriGen/RTLCoder/CodeV等）：仅过滤仓库开源协议，无逐文件版权关键词检测，数据集含私有IP片段。
2. HDL数据集构建方案：依赖旧BigQuery归档数据，抓取机制老旧，未做去重、语法校验双重清洗。
3. LLM版权检测通用研究：面向文本/软件代码，未适配Verilog硬件IP版权判定场景。
4. 硬件IP防盗GNN模型：仅做推理后盗版识别，无法从训练源头规避LLM记忆私有代码问题。
5. 代码大模型合规训练：无针对硬件描述语言的分层清洗流水线，缺少专用版权风险评测基准。

## 本文解决方案
### 1 Verilog版权侵权评测基准
收集2000份带版权声明工业Verilog源码；截断前20%作为prompt，用余弦相似度0.8为阈值判定输出是否侵权，量化各模型违规比例。
### 2 全自动合规数据集采集框架
按时间分片调用GitHub API规避分页限制，批量克隆仓库；筛选MIT/Apache等宽松许可仓库，剔除无许可证项目。
### 3 多层数据集清洗链路
1. 文件级关键词过滤：删除含proprietary、all rights reserved等私有版权文件；
2. LSH+MinHash去重，去除高度重复代码；
3. Icarus Verilog语法校验，剔除语法损坏文件；最终生成FreeSet。
### 4 合规模型FreeV持续预训练
基于Llama-3.1-8B，采用QLoRA 4bit量化、Unsloth加速，在FreeSet上单轮持续预训练，不引入私有IP数据。
### 5 双维度评估体系
同时评测模型版权违规率、VerilogEval功能生成pass@k指标，兼顾合规性与硬件代码生成能力。

## 实验分析
1. 数据集对比：FreeSet共222624个文件、16.5GB，是唯一同时做仓库+文件两级版权过滤的Verilog开源数据集，文件长度分布覆盖小型模块至大型设计。
2. 版权违规测试：主流Verilog微调模型违规率9%~15%，FreeV仅3%，相比基础Llama仅提升1个百分点，合规性大幅领先。
3. 功能生成效果：原始Llama pass@10=25.9%，FreeV达36.0%，提升10.1%；pass@5提升7.9%，但未超越CraftRTL等专用指令微调模型。
4. 清洗消融：原始抓取130万文件，许可过滤剩60万，去重删除62.5%，版权过滤剔除近1%私有IP源码，多道清洗缺一不可。
5. 硬件环境：A100用于预训练，A5000做推理，4bit量化大幅降低显存占用。

## 研究启发
1. HDL大模型合规不能仅筛选仓库协议，必须逐文件检索版权声明，私有IP片段会混入开源仓库造成训练污染。
2. 从训练源头清洗数据集，是比推理后IP检测更根本的版权风险防控手段。
3. 可通过余弦相似度构建轻量化基准，快速量化各类Verilog LLM的侵权风险，方便横向对比选型。
4. 持续预训练可在不引入侵权数据前提下提升Verilog生成功能指标，但指令微调收益更高。
5. 开源代码爬虫需按时间分片规避API限制，搭配去重、语法校验可大幅提升数据集质量。
