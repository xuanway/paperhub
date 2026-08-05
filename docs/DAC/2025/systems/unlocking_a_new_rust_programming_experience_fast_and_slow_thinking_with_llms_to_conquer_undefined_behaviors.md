---
title: "Unlocking a New Rust Programming Experience: Fast and Slow Thinking with LLMs to Conquer Undefined Behaviors"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Unlocking a New Rust Programming Experience: Fast and Slow Thinking with LLMs to Conquer Undefined Behaviors

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.02335">https://arxiv.org/abs/2503.02335</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> Rust安全，快慢思考，大语言模型框架</p>
</div>


---

## 研究概要
本文借鉴双过程认知理论，提出RustBrain大模型修复框架，分为快、慢双推理阶段。快推理提取代码特征批量生成修复方案；慢推理搭载多智能体完成分解、验证、抽象推理，配套自适应回滚与反馈自学习。基于Miri数据集测试，修复通过率94.3%、语义可用率80.4%，较SOTA提升30%，修复速度最高为人工专家18倍。

## 背景和动机
1. Rust unsafe块易产生未定义行为UB，引发内存漏洞，但传统静态分析、人工修复高度依赖专业知识，效率低下。
2. 现有LLM代码修复工具流程固化，无法根据Rust强类型、所有权语义动态调整修复策略，容易出现模型幻觉、修复后代码失效。
3. 同类工具缺少校验与回滚机制，修复过程错误会持续累积，大幅降低修复准确率与语义完整性。
4. Rust同类UB因上下文差异需要不同修复手段，固定提示词与流程难以适配多样化unsafe场景。
5. 当前修复框架缺少闭环自优化机制，无法复用历史有效修复经验，对稀有内存错误修复效果差。

## 相关工作
1. 人工/形式化Rust安全检测：依靠静态分析、符号执行，精准但人力成本极高，难以大规模自动化。
2. 单阶段LLM修复工具（RustAssistant）：采用固定流水线生成补丁，无分层推理，无法抑制幻觉，语义丢失严重。
3. 通用代码调试大模型：面向通用编程语言，未适配Rust所有权、子页、借用等特有安全规则。
4. LLM幻觉抑制研究：全局回滚方案丢弃有效中间修复步骤，计算开销大，缺少自适应择优机制。
5. Rust unsafe修复专用方案：仅单一替换策略，不区分断言、语义修改三类修复路径，泛化能力弱。

## 本文解决方案
### 1 快慢双阶段协同推理整体架构
快推理：Miri检测UB后提取代码、错误特征，基于通用知识库批量生成多套候选修复方案；慢推理对方案分层校验，结果反馈至快推理实现自迭代优化。
### 2 三类专用修复智能体
替换智能：用标准安全API替换unsafe操作；断言智能：插入边界校验拦截运行时错误；语义修改智能：调整生命周期、指针逻辑修复深层内存缺陷。
### 3 自适应择优回滚机制
不全局回退初始代码，保留迭代中错误最少的最优中间版本，抑制幻觉同时复用有效修复步骤，降低迭代开销。
### 4 AST剪枝抽象推理智能体
基于unsafe关键词裁剪抽象语法树，过滤无关代码降低噪声；向量检索相似错误修复案例，为LLM提供领域专业提示。
### 5 多维反馈自学习闭环
以通过率、语义可用性、执行开销三维度评估修复结果，将优质方案特征回流快推理，减少知识库依赖，提升同类错误修复精度。

## 实验分析
1. 实验基准：Miri官方UB数据集，对比GPT系列、Claude、RustAssistant、人工专家；指标为Miri通过率、代码语义执行率、修复耗时。
2. 精度表现：RustBrain搭配知识库可达94.3%通过率、80.4%语义可用率，相较RustAssistant提升33%/41%。
3. 模型适配：低能力GPT-3.5接入框架后性能逼近原生GPT-4；温度参数0.5时修复效果最优。
4. 效率对比：平均修复速度为人类专家7.4倍，函数指针等稀有错误最高提速18倍。
5. 消融验证：自适应回滚、AST推理、反馈机制任一模块移除，通过率下降15%~30%，多智能体组合可灵活适配各类UB场景。

## 研究启发
1. 单纯单轮LLM生成不足以解决Rust特有内存约束，分层快慢推理是抑制模型幻觉、保障语义完整的核心思路。
2. 针对unsafe分类设计多路径修复智能体，比统一通用修复模板适配更多代码上下文。
3. 全局回滚策略存在巨大性能损耗，保留最优中间版本的自适应回滚可兼顾准确率与计算开销。
4. 对Rust AST做unsafe定向剪枝，能大幅降低大模型输入噪声，提升领域修复专业性。
5. 构建评估反馈闭环可实现框架自进化，降低对专用安全知识库的依赖，提升稀有未定义行为泛化修复能力。
