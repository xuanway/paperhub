---
title: "UVLLM: An Automated Universal RTL Verification Framework using LLMs"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# UVLLM: An Automated Universal RTL Verification Framework using LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2411.16238">https://arxiv.org/abs/2411.16238</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/SEU-ACAL/reproduce-UVLLM-DAC-25">https://github.com/SEU-ACAL/reproduce-UVLLM-DAC-25</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>大语言模型驱动验证，通用RTL验证框架，自动化错误修复，语法与功能 </p>
</div>

---

## 研究概要
本文提出UVLLM通用RTL自动化验证框架，融合LLM与工业UVM验证体系，构建四阶段流水线：预处理、UVM仿真、日志后处理、智能修复。设计动态错误定位、版本回滚、结构化补丁输出机制。自建331条真实RTL错误数据集，语法修复率86.99%、功能修复率71.92%，相较SOTA平均提速10.42倍。

## 背景和动机
1. 芯片RTL验证工作量占前端70%，人工调试成本极高；传统自动修复工具依赖固定模板，仅覆盖少量简单硬件错误。
2. 现有LLM RTL调试方案缺少完整UVM仿真闭环，测试覆盖率不足，修复易过拟合特定用例，真实场景失效严重。
3. LLM存在幻觉问题，单次生成补丁易引入新错误，缺少版本回退、多轮迭代校验机制。
4. 硬件日志信息稀疏，简单输入LLM难以定位时序、位宽、端口匹配等深层功能缺陷。
5. 缺乏面向工业IP、SoC的统一评测基准，现有数据集错误类型单一，无法衡量框架泛化能力。

## 相关工作
1. 模板式RTL自动修复（Cirfix、RTLrepair）：依靠预设规则，适配错误范围窄，复杂逻辑缺陷无法处理。
2. 纯LLM RTL调试MEIC：无标准化UVM仿真流程，测试用例有限，修复过拟合，真实修复效果大幅缩水。
3. 通用代码大模型：面向软件代码，不兼容Verilog时序、端口、块结构等硬件特有约束。
4. UVM测试平台研究：仅人工搭建环境，未与LLM自动错误定位、补丁生成结合。
5. RTL错误数据集：规模小、错误类型单一，缺少算术、控制、存储多类真实工程缺陷样本。

## 本文解决方案
### 1 四阶段端到端验证流水线
预处理：Verilator静态检查+轻量LLM批量消除语法与时序警告；UVM仿真：LLM生成参考模型完成全量覆盖测试；后处理：动态数据流图定位错误信号与可疑代码；修复智能体：结构化输出补丁并迭代优化。
### 2 UVM+LLM协同测试机制
基于LLM自动生成C/C++参考模型，复用UVM记分板、监视器组件采集全场景失配日志，解决传统方案测试覆盖不足问题。
### 3 时序感知动态错误定位引擎
解析仿真波形与时戳，构建DFG数据流切片，分层输出失配信号/可疑代码两级错误信息，降低LLM输入冗余。
### 4 防幻觉迭代修复机制
维护历史最优代码版本，若新补丁测试通过率下降自动回滚；强制LLM输出JSON格式原始-补丁代码对，减少无关文本干扰。
### 5 工业级评测数据集构建
从商用/开源IP版本差异提取真实错误，覆盖位宽、赋值、端口、状态机等9大类缺陷，共331组RTL错误样本。

## 实验分析
1. 实验配置：GPT-4-turbo为基础大模型，仿真工具VCS/Modelsim，对比MEIC、RTLrepair、纯GPT基线，指标修复率FR、命中HR、执行耗时。
2. 修复精度：语法错误FR=86.99%，功能错误FR=71.92%，相比MEIC分别提升26.9%、36.3%；HR与FR差值极小，无过拟合。
3. 执行效率：全模块平均比MEIC快10.42倍，算术复杂模块最高提速16.56倍，预处理承担过半简单错误修复。
4. 泛化能力：计数器、加法器简单模块修复率接近100；FSM复杂逻辑修复偏弱，但仍显著优于基线。
5. 消融实验：结构化补丁输出相比完整代码生成，修复率提升16%、运行耗时降低一半；回滚机制可避免幻觉错误累积。

## 研究启发
1. LLM硬件调试必须绑定UVM工业仿真闭环，仅靠代码静态分析会产生大量过拟合无效补丁。
2. 分层错误定位（信号→代码行）能大幅压缩LLM输入token，同时提升缺陷定位精准度。
3. 版本回退+结构化输出可有效抑制大模型幻觉，是落地硬件自动化修复的关键配套机制。
4. 预处理环节过滤基础语法警告，能大幅减少昂贵LLM调用次数，显著降低验证成本。
5. 芯片验证评测不能仅看单用例通过率，需引入独立专家评估的修复率FR，衡量补丁通用性。
