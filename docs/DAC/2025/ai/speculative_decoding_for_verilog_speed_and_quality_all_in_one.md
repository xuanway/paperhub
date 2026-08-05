---
title: "Speculative Decoding for Verilog: Speed and Quality, All in One"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Speculative Decoding for Verilog: Speed and Quality, All in One

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.14153">https://arxiv.org/abs/2503.14153</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> Verilog代码生成，投机解码 </p>
</div>


---

## 研究概要
本文面向Verilog RTL生成提出语法感知推测解码方案，基于AST提取语法关键token并引入[FRAG]分隔符构建专用训练标签，改造多头Medusa架构。在CodeLlama/CodeT5p验证，生成速度最高提速5.05倍，RTLLM基准pass@10指标提升17.19%，同时兼顾生成速度与代码语法、功能正确性。

## 背景和动机
1. Verilog训练数据集稀缺，通用BPE分词割裂模块、时序等硬件语法结构，模型易生成语法破损代码，编译通过率低。
2. 传统逐token(NTP)解码推理时延极高，Medusa多头推测仅加速速度，未适配硬件语言语法约束，长片段易断裂。
3. 现有语法导向代码模型多基于AST序列编码，序列过长、显存开销大，难以适配大代码LLM微调。
4. 通用推测解码无硬件语法感知，截断位置随机，经常在不完整模块/语句处终止，大幅降低功能通过率。
5. 缺少适配Verilog、同时提升推理速度与生成质量的一体化推测解码优化方案。

## 相关工作
1. 通用代码LLM(CodeLlama/CodeT5)：采用通用分词，无Verilog语法适配，RTL生成准确率低。
2. 语法感知编码(SyntaxBERT/GrammarT5)：基于AST/文法规则建模，序列膨胀，不支持多头推测加速。
3. Medusa多头推测解码：通用文本加速，未结合硬件语法，解码截断破坏Verilog代码完整性。
4. Verilog专用生成数据集(RTLLM/MG-Verilog)：仅提供训练素材，无配套解码优化策略。
5. 传统单步NTP解码：无并行多token预测，推理速度慢，是本文主要基线。

## 本文解决方案
### 1 Verilog语法数据集预处理流水线
基于Stagira解析器清洗Github开源Verilog代码，去重过滤残缺模块；解析AST提取关键字、标识符等语法关键token，插入[FRAG]片段分隔符标记语法边界。
### 2 语法增强多头训练标签机制
基础序列插入[FRAG]，各预测头标签左移对齐；跨头统一过滤不完整片段，无效位置填充[IGNORE]屏蔽损失，降低深层预测头训练难度。
### 3 并行标签生成算法
批量并行处理多序列、多头标签，反向遍历快速屏蔽无完整语法的预测位置，大幅缩减标签构建预处理耗时。
### 4 语法约束推测解码逻辑
并行多头生成候选序列后，优先选取最长完整语法片段前缀，丢弃跨[FRAG]的不完整token，保证每轮输出语法合法。
### 5 双模型兼容微调方案
分别适配解码器-only CodeLlama与编码器-解码器CodeT5p，采用QLoRA轻量化微调，多头损失引入衰减权重平衡各预测头贡献。

## 实验分析
1. 实验环境：A800集群，RTLLM、VGen两大RTL评测基准，对比NTP、原始Medusa，评测pass@k、生成速度tokens/s。
2. 速度指标：CodeLlama最高提速5.05倍，CodeT5p提速2.66倍，相较原版Medusa提升1.42~2.29倍。
3. 质量指标：RTLLM数据集pass@10最高提升17.19%，语法完整度平均提升22.9%，小数据集下增益依然显著。
4. 消融验证：[FRAG]语法分隔符与[IGNORE]标签屏蔽是核心，二者缺失会同时大幅降速、降低功能通过率。
5. 案例对比：同等Verilog多路选择器prompt，本文仅需14解码步，Medusa需24步，标准NTP高达77步。

## 研究启发
1. 专用硬件语言不能直接复用通用文本推测解码，语法边界约束是兼顾速度与正确性的关键。
2. 借助AST提取语法关键点、插入片段标记，可让模型天然学习完整代码片段分布，减少残缺输出。
3. 多头推测可通过标签掩码屏蔽无效预测，降低深层预测头训练难度，支持更多并行头进一步提速。
4. 速度与代码质量并非互斥，将解码截断对齐语法边界可同时实现加速与生成精度提升。
5. 针对Verilog这类低资源编程语言，语法感知预处理能显著缓解数据集稀缺带来的生成性能短板。
