---
title: "Hardware Generation with High Flexibility using Reinforcement Learning Enhanced LLMs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Hardware Generation with High Flexibility using Reinforcement Learning Enhanced LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ece.k-state.edu/research/hardware-security/papers/DAC2025_RLPFA_Processing.pdf">https://ece.k-state.edu/research/hardware-security/papers/DAC2025_RLPFA_Processing.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件生成，PPA，强化学习 </p>
</div>

---

## 研究概要
本文提出PPA-RTL强化学习大模型硬件生成框架，将综合后功耗、性能、面积作为奖励信号，基于DPO直接偏好优化适配7类硬件PPA优化目标。以Deepseek-coder/RTLCoder为底座，离线EDA构建偏好数据集。SFT-RL方案相较纯SFT，功耗平均降20.97%、时序性能提升14.68%、面积缩减29.05%，语法功能精度损失可控。

## 背景和动机
1. 现有LLM生成RTL仅保证语法功能正确，无法兼顾芯片综合PPA指标，工程师需反复迭代优化，设计周期冗长。
2. 提示工程、纯监督微调(SFT)仅复刻样本代码，缺少面向功耗/时序/面积的定向优化能力，适配不同硬件场景困难。
3. 传统RLHF在线EDA仿真计算奖励开销极大，每轮训练都需综合，训练速度极低；代理预测奖励存在累积误差。
4. 不同应用（IoT/高性能计算）PPA权衡需求差异大，现有模型无灵活权重调节机制，难以定制优化方向。
5. 硬件HDL领域高质量偏好对比数据集稀缺，缺少可复用的PPA标注训练素材。

## 相关工作
1. 通用硬件LLM（DAVE、RTLCoder、Hardware Phi）：仅通过SFT生成语法正确Verilog，未引入综合PPA指标做优化导向。
2. 通用代码大模型（GPT4、Deepseek-coder）：通用代码能力强，但无芯片物理指标感知，生成电路PPA表现差。
3. RLHF/DPO通用文本优化：依靠人工偏好标注，无法对接EDA综合得到硬件量化奖励。
4 硬件自动调试框架：聚焦代码缺陷修复，不针对功耗、时序、面积做生成端前置优化。
5. PPA预测类ML模型：仅做综合结果预估，不能反向指导LLM生成符合指标的RTL代码。

## 本文解决方案
### 1 离线EDA偏好数据集构建
基于RTLCoder数据集，用DC综合工具提取每条RTL的功耗、关键路径延迟、单元面积；对同一描述生成多版代码，打分筛选最优/最差样本构建(x,最优,最差)三元偏好集。
### 2 可加权PPA打分奖励函数
设计归一化综合指标打分公式，通过w_P/w_Perf/w_A权重自由切换7类优化目标（单指标/双指标/三指标均衡），适配各类芯片设计需求。
### 3 DPO直接偏好优化训练流程
分RL-only、SFT-RL两条训练路线；以SFT模型为参考策略，DPO损失最大化优质RTL生成概率、压低劣质代码输出，无需单独奖励模型。
### 4 兼顾语法与功能约束
数据集过滤综合失败、语法错误样本，训练时保留生成准确率，PPA优化不会大幅降低Verilog可编译、可仿真通过率。
### 5 多场景统一生成流水线
输入自然语言硬件描述，自动输出面向指定PPA偏好的RTL，支持算术单元、时序控制器等各类数字模块生成。

## 实验分析
1. 实验环境：8张A100 80GB，TSMC90nm工艺DC综合，评测基准RTLLM-v1.1，对比Deepseek原始、纯SFT、GPT4o。
2. PPA提升效果：SFT-RL-PPA均衡模型相较纯SFT，功耗-20.97%、关键路径-14.68%、面积-29.05%；单指标定向优化对应收益更高。
3. 精度表现：各类RL模型语法准确率维持86.2%~96.6%，功能准确率仅小幅下降（最大<7%），生成代码可用性有保障。
4. 消融对比：SFT预训练+DPO联合优于仅RL训练，损失更低、偏好对齐精度更高；离线数据集规避在线综合巨大训练开销。
5. 案例验证：日历模块示例，PPA-RTL生成单always块同步时序逻辑，消除竞争冒险，三项PPA指标同步优化。

## 研究启发
1. 硬件LLM不能只追求功能正确，需将EDA综合物理指标引入训练闭环，从生成端减少后端迭代成本。
2. 离线预构建PPA偏好数据集可规避在线仿真的超高算力开销，是硬件领域RL落地可行方案。
3. DPO相比传统RLHF省去独立奖励网络，适配硬件EDA奖励获取成本高的场景，训练效率更高。
4. 通过可调权重奖励函数，一套模型可适配IoT低功耗、HPC高性能等完全不同的芯片设计约束。
5. PPA优化与代码语法功能存在轻微权衡，数据集过滤无效样本可将精度损失控制在极小范围。
