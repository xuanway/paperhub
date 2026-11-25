---
title: "LEMOE: LLM-Enhanced Multi-Objective Bayesian Optimization for Microarchitecture Exploration"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# LEMOE: LLM-Enhanced Multi-Objective Bayesian Optimization for Microarchitecture Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132704">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132704</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 上下文学习，贝叶斯优化，大语言模型，微架构设计 </p>
</div>


---

## 研究概要
本文提出LEMOE，面向RISC-V BOOM乱序核设计空间探索，融合LLVM程序特征与大模型构建多目标贝叶斯优化框架。设计程序感知初始化、LLM代理模型与EHVI采集函数，在IPC/功耗双目标优化下，同等迭代超22.8%能效提升，达成最高2.9倍探索加速。

## 背景和动机
1. RISC-V微架构可调参数规模庞大，EDA仿真单次评估耗时数小时，传统探索迭代成本极高，亟需减少采样次数。
2. 传统贝叶斯优化采用无信息先验高斯代理，无法利用芯片架构领域先验，易陷入低效采样。
3. 现有黑盒探索缺少程序特征引导，随机初始化大量无效配置；白盒方案依赖人工架构知识，可移植性差。
4. 常规多目标采集函数计算开销巨大，稀疏采样场景下预测精度不足，难以平衡性能与功耗权衡。
5. 缺少融合程序负载特征与LLM领域知识的统一DSE流水线，无法实现负载专属架构快速寻优。

## 相关工作
1. 贝叶斯类DSE（BOOM-Explorer）：基于深度核高斯过程，仅架构感知初始化，无程序负载与大模型先验加持。
2. 强化学习/图学习微架构搜索：依赖定制代理模型，泛化弱，不兼容通用多目标贝叶斯框架。
3. TPE、随机森林等传统多目标优化：无硬件领域先验，初始采样质量差，迭代收敛慢。
4. LLM辅助单目标优化：仅用于采样，未结合LLVM程序特征，不支持IPC/功耗多目标超体积优化。
5. 专用架构探索平台（Archgym）：无大模型增强，稀疏样本下代理预测误差显著。

## 本文解决方案
### 1 LLVM+LLM程序感知初始化流水线
编译程序提取CFG、访存、浮点等IR特征，斯皮尔曼相关过滤冗余特征，构造专用Prompt输入LLM，输出适配负载的多样化初始架构配置，替代随机/LHS采样。
### 2 LLM替代传统高斯代理模型
将已有样本转为文本上下文，通过in-context学习预测新架构的IPC、功耗均值与不确定性；打乱样本顺序消除Prompt顺序偏差，适配稀疏数据集。
### 3 LLM并行采样+EHVI采集函数
基于超体积增长期望构造采样目标，LLM批量生成候选架构，以EHVI筛选最优待评估点，规避传统EHVI高解析计算开销。
### 4 完整迭代DSE流程
初始化→LLM采样→LLM性能预测→EHVI选点→Chipyard仿真评估，循环迭代直至收敛，输出帕累托最优微架构解集。
### 5 适配BOOM乱序核设计空间
覆盖缓存、发射队列、重排序缓存、分支预测等全模块可调参数，支持mm/qsort等多类RISC基准测试集。

## 实验分析
1. 实验环境：Xeon双路工作站，Chipyard+BOOM仿真，对比随机森林、TPE、BOOM-Explorer等主流DSE方法，LLM选用GPT3.5/GPT4o。
2. 初始化效果：LLVM+LLM联合初始化样本参数相关性0.3538，远高于随机、纯LLM初始化，初始解集质量大幅提升。
3. 消融实验：移除LLM/LLVM模块均造成超体积、IPC/能效明显下跌；GPT4o搭配α=0.1探索系数效果最优。
4. 指标对比：同等迭代下能效较SOTA提升最高22.8%；达成相同超体积目标，运行速度最高2.9倍加速。
5. 帕累托前沿：LEMOE解集CPI-功耗覆盖范围更广，均衡架构选择远多于对比基线方法。

## 研究启发
1. 微架构探索不能脱离程序负载，LLVM编译特征可精准表征程序访存、分支、浮点行为，引导负载定制架构生成。
2. LLM内置海量硬件领域知识，可替代高斯过程作为稀疏样本下的代理模型，大幅降低贝叶斯优化迭代次数。
3. 多目标DSE可利用LLM简化EHVI复杂数值计算，并行候选采样能显著降低仿真评估总耗时。
4. 初始化策略对收敛速度影响极大，融合负载与大模型先验可从源头减少无效架构采样。
5. 软硬件协同DSE需将程序、架构、大模型三层信息打通，才能兼顾寻优速度与帕累托解质量。