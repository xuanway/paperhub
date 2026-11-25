---
title: "PyraNet: A Multi-Layered Hierarchical Dataset for Verilog"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PyraNet: A Multi-Layered Hierarchical Dataset for Verilog

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2412.06947">https://arxiv.org/abs/2412.06947</a></p>
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://huggingface.co/datasets/bnadimi/PyraNet-Verilog">https://huggingface.co/datasets/bnadimi/PyraNet-Verilog</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，微调，Verilog，数据集，Transformer模型 </p>
</div>


---

## 研究概要
本文提出PyraNet分层Verilog开源数据集与配套微调方案。数据集按代码质量分为六层金字塔结构，搭配分层损失加权+课程学习微调策略。基于CodeLlama、DeepSeek-Coder验证，相较原始基线pass@k最高提升32.6%，超越RTLCoder、OriGen等SOTA模型最高16.7%。

## 背景和动机
1. 现有Verilog专用数据集缺少统一质量分级，高低质量代码混杂训练，模型易学习错误语法与低效电路写法。
2. 传统微调统一赋予样本损失权重，低质量代码同等干扰模型，生成代码语法、功能性错误频发。
3. 缺少分层训练策略，模型同步学习简单与复杂电路，收敛慢、泛化生成能力弱。
4. 现有HDL数据集规模有限、过滤流程简陋，存在大量重复、语法破损样本，训练数据纯度不足。
5. 主流RTL生成模型未区分代码优劣，无针对性分层训练范式，难以平衡简单/复杂电路生成效果。

## 相关工作
1. VerilogEval：标准RTL评测基准，仅提供测试集，无分层训练数据集与分层微调方法。
2. MG-Verilog：多粒度Verilog数据集，仅区分描述粒度，未按代码质量分层、无加权训练机制。
3. RTLCoder/OriGen：专用RTL生成框架，依靠单一统一微调，不区分样本质量权重。
4. MEV-LLM：多专家Verilog模型，仅按复杂度划分数据，缺少分层损失加权策略。
5. CodeV/BetterV：大尺度HDL数据集，采用通用微调，未利用代码质量分层优化训练流程。

## 本文解决方案
### 1 金字塔分层PyraNet数据集构建
从GitHub与GPT-4o-mini采集样本，经空文件、去重、语法多重过滤；用GPT4o-mini打分0~20划6层，每层内分基础/中级/高级/专家四类复杂度，总计69万+有效样本。
### 2 分层动态损失加权机制
金字塔顶层高质量样本损失权重1.0，逐层向下递减至底层0.1，降低低质量代码对梯度的负面影响。
### 3 层级内课程学习微调
每层内部按“基础→中级→高级→专家”顺序训练；整体从最高质量层逐层向下完成全数据集微调，循序渐进学习电路逻辑。
### 4 标准化数据预处理流水线
依次执行脏文件剔除、Jaccard去重、Icarus语法校验、自动复杂度标注、质量打分，保障数据集纯净度。
### 5 LoRA轻量化微调实现
固定基座模型主干，仅训练低秩适配器，学习率2e-4，适配CodeLlama、DeepSeek-Coder等主流代码大模型。

## 实验分析
1. 实验环境：CodeLlama-7B/13B、DeepSeek-Coder-7B，VerilogEval机器/人类双测试集，指标pass@1/5/10。
2. 消融结论：仅用PyraNet数据集即可显著提升性能；数据集+分层微调组合增益最大。
3. 性能对比：相比原生CodeLlama最高提升32.6%；对比RTLCoder提升16.7%，小幅优于OriGen。
4. 数据集有效性验证：打乱代码与标签后模型精度大幅下跌，证明分层打分标签可靠。
5. 局限性：未集成代码自纠错反射机制，与OriGen存在小幅差距，可后续融合改进。

## 研究启发
1. HDL训练数据不能同等对待，按代码质量分层并差异化加权，能有效抑制劣质样本带来的噪声梯度。
2. 分层+层级内双重课程学习，由浅到深训练电路逻辑，可显著提升模型复杂RTL生成能力。
3. 完整多轮数据清洗、语法校验是高质量EDA专用数据集的基础，脏数据会大幅削弱微调收益。
4. 代码大模型微调无需全参数更新，LoRA轻量化方案搭配分层策略性价比更高。
5. 分层数据集可与自纠错、RAG等现有RTL优化方案结合，进一步缩小生成功能性错误。
