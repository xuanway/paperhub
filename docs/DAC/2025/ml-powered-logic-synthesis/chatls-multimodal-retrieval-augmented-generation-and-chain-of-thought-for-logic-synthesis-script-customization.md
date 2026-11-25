---
title: "ChatLS: Multimodal Retrieval-Augmented Generation and Chain-of-Thought for Logic Synthesis Script Customization"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# ChatLS: Multimodal Retrieval-Augmented Generation and Chain-of-Thought for Logic Synthesis Script Customization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://leozheng.tech/papers/C13-DAC'25-ChatLS.pdf">https://leozheng.tech/papers/C13-DAC'25-ChatLS.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 逻辑综合脚本定制，多模态检索增强生成，思维链推理，图神经网络 </p>
</div>


---

## 研究概要
本文提出ChatLS大语言模型框架，融合电路图GNN多模态RAG与分步CoT推理，自动定制逻辑综合脚本。设计CircuitMentor提取电路层级特征、SynthRAG多源检索、SynthExpert迭代推理三大模块。在多款开源芯片测试，相较GPT-4o、Claude 3.5显著优化时序负松弛，时序收敛能力最优。

## 背景和动机
1. 逻辑综合需依据RTL结构、工艺库、综合报告人工调参写脚本，人力成本高，迭代周期漫长。
2. 通用LLM长文本处理能力弱，难以解析大规模RTL全局/局部时序、路径特征，易产生幻觉无效综合命令。
3. 现有EDA-RAG仅检索文本手册，无法利用电路拓扑、模块层级、关键路径结构化信息，检索匹配精度低。
4. 单轮生成脚本缺少分步推理校验，未按时序/面积目标分步调优，难以解决WNS/TNS时序违逆。
5. 缺乏电路图与文本跨模态联合检索机制，相似设计优化策略无法复用，脚本定制泛化性差。

## 相关工作
1. EDA专用RAG工具（ORAssistant、Ask-EDA）：仅面向工具文档文本检索，无法解析电路拓扑结构，缺失RTL特征输入。
2. ChatEDA、ChipNeMo等LLM EDA框架：仅做RTL生成/问答，无综合脚本迭代调优链路。
3. 纯GNN电路表征学习（DeepGate、Gamora）：仅提取电路特征，未与LLM、检索系统联动生成综合策略。
4. 通用CoT大模型方案：无EDA领域定制推理步骤，不区分时序/面积优化场景，缺少工艺库支撑。
5. 传统综合自动调参工具：依赖固定搜索算法，无法基于自然需求灵活生成完整DC/Genus脚本。

## 本文解决方案
### 1 CircuitMentor电路图解析模块
将RTL转为Neo4j AST图数据库，基于GraphSAGE分层GNN+度量学习提取模块全局/局部嵌入；支持Cypher查询关键路径、子模块，解决LLM长RTL理解瓶颈。
### 2 SynthRAG多模态领域检索框架
三类联合检索：图嵌入相似设计策略检索、Cypher电路结构检索、文本工艺库/手册检索；设计时序面积加权重排算法提升检索匹配F1值。
### 3 SynthExpert分步CoT迭代推理机制
将脚本生成拆分为多推理步骤，每一步动态调用SynthRAG获取专属电路/手册信息，逐轮修正优化策略，抑制LLM幻觉命令。
### 4 LLM生成器端到端流程
输入自然需求、RTL、旧脚本、综合报告，结合GNN电路嵌入与检索素材，初稿→分步修正→输出可执行综合脚本。
### 5 开源芯片知识库构建
收录RISC核、NVDLA、FFT、SHA等多类设计，搭配45nm Nangate工艺库与配套综合专家脚本作为检索素材。

## 实验分析
1. 实验环境：GPT-4o为基础LLM，PyTorch Geometric+Neo4j，基准包含AES、RiscV32、TinyRocket等7款开源电路，对比GPT-4o、Claude 3.5 Sonnet。
2. 时序指标：ChatLS大幅降低WNS、TNS负松弛，TinyRocket基线TNS-1057优化至-14.74，AES完全消除时序违逆。
3. 检索性能：SynthRAG加权重排机制显著提升相似设计检索Precision/Recall，F1指标优于纯文本检索基线。
4. 泛化能力：算术、存储、处理器、加速核多类型电路均适配，单轮迭代即可大幅改善时序。
5. 对比基线：通用大模型易生成无效综合指令，ChatLS依托电路图与分步CoT无非法命令，时序QoR最优。

## 研究启发
1. 仅靠文本R无法支撑综合脚本专业生成，必须融合电路图GNN结构化拓扑信息实现跨模态检索。
2. 大模型EDA任务不能一次性生成完整方案，分步CoT+逐轮检索修正可有效缓解模型幻觉问题。
3. 电路分层嵌入可区分算术/存储等模块特性，针对性匹配专属综合优化策略。
4. 时序、面积等硬件指标加权重排检索结果，能优先复用高QoR专家综合方案。
5. LLM与图数据库、GNN、检索系统串联的端到端框架，可实现逻辑综合全流程自动化，大幅减少人工调参成本。