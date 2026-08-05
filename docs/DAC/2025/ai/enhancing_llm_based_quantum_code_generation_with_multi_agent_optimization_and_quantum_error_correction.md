---
title: "Enhancing LLM-based Quantum Code Generation with Multi-Agent Optimization and Quantum Error Correction"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Enhancing LLM-based Quantum Code Generation with Multi-Agent Optimization and Quantum Error Correction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.14557">https://arxiv.org/abs/2504.14557</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 机器学习，量子代码生成，量子计算，多智能体大语言模型 </p>
</div>


---

## 研究概要
本文面向量子代码生成提出三智能体协同多Agent框架，融合迭代多轮推理、结构化CoT与量子纠错QEC模块。基于Starcoder微调构建代码生成、语义分析、QEC预测三Agent，自建分层量子测试集验证。SCoT可提升准确率50%，RAG增益仅4%，框架能生成容错量子电路，有效抑制量子噪声。

## 背景和动机
1. 现有LLM代码生成多面向通用编程语言，缺少适配Qiskit等量子领域专用生成框架，量子代码语法、语义错误频发。
2. 量子领域库迭代快、高质量训练数据集稀缺，常规微调模型生成代码易出现弃用API、算法逻辑错误。
3. 通用RAG、CoT直接迁移至量子场景效果差异巨大，缺乏针对量子算法的提示工程定量分析。
4. 传统生成框架不考虑量子噪声，输出电路无纠错逻辑，在真实量子硬件运行误差极高。
5. 现有量子代码助手仅完成语法生成，无法自动嵌入表面码等QEC纠错结构，不具备容错能力。

## 相关工作
1. 通用多Agent代码框架（AgentCoder）：聚焦通用代码测试迭代，未适配量子领域独特约束与纠错需求。
2. 代码大模型（CodeLlama/Starcoder）：擅长通用程序，对量子纠缠、酉变换等领域知识建模不足。
3. IBM Qiskit Code Assistant：仅做基础微调，无多轮迭代与自动量子纠错，生成准确率仅46%。
4. RAG/CoT提示优化：通用NLP与代码任务验证有效，但未系统评估在量子场景的适配性。
5. 量子纠错表面码研究：侧重硬件拓扑译码，未结合LLM实现代码端自动嵌入纠错逻辑。

## 本文解决方案
### 1 三智能体协同多Agent架构
协调器统筹三大模块：①代码生成Agent（基于LoRA微调Starcoder，使用2024年后开源Qiskit数据集）；②语义分析Agent，迭代多轮推理修正语法/算法错误；③QEC译码Agent，依据设备拓扑自动嵌入表面纠错码。
### 2 迭代多轮推理优化
将错误日志、原始代码回灌提示词，逐轮修复单类缺陷，避免全量重生成，持续提升量子程序语法与语义合规性。
### 3 分层提示工程对比验证
构建文档RAG、算法RAG、基础CoT、结构化SCoT四类提示方案，SCoT分步拆解量子算法逻辑，强化模型领域推理能力。
### 4 自动化量子纠错生成
根据逻辑比特数与硬件拓扑生成表面码译码器，映射逻辑比特至物理比特，不改变原算法语义，延长量子相干时间、降低测量噪声。
### 5 分层量子评测测试集
自建测试集覆盖基础电路、经典量子算法、高级量子退火/行走三类任务，全面评估不同优化策略效果。

## 实验分析
1. 实验配置：Starcoder-3B为主模型，对比Salesforce-2B；自建47%基础/24%中级/29%高级量子测试集，指标采用pass@k。
2. 基础效果：无优化基线pass@1=18%，微调后至28%；RAG仅提升2%~4%，增益微弱。
3. 提示对比：CoT使准确率至60%，SCoT达68%，相较微调基线提升40个百分点，整体最大提升50%。
4. 多轮推理：三轮迭代准确率至34%，超过三轮收益边际递减，多为库版本导入类错误。
5. QEC验证：Grover算法案例中嵌入表面码后，目标态测量概率显著提升，无关噪声态占比大幅下降；缺点为译码器依赖硬件拓扑。

## 研究启发
1. 通用LLM优化手段不能直接照搬至量子领域，CoT/SCoT这类推理型提示远优于RAG检索方案。
2. 量子领域数据更新快、文档时效性差，检索增强难以提供有效领域信息，推理式提示是更优推理优化路径。
3. 多Agent分工可分离代码生成、语义校验、量子容错三大需求，一站式产出可硬件部署的容错量子电路。
4. 自动QEC生成存在拓扑绑定局限，拓扑无关译码模型是重要后续研究方向。
5. 量子代码评测需区分基础/中/高级算法，仅通用HumanEval类基准无法衡量模型深层量子逻辑推理能力。
