---
title: "Machine Learning-Driven STL Generation for Enhancing Functional Safety of E/E Systems"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Machine Learning-Driven STL Generation for Enhancing Functional Safety of E/E Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA9: Design for Test and Silicon Lifecycle Management</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132095">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132095</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 功能安全，故障注入分析，测试模式生成，自测试库开发 </p>
</div>


---

## 研究概要
本文面向汽车等安全关键E/E系统，提出VAE+RL混合驱动的自动自测试库(STL)生成框架。规避ATPG/BIST侵入式停机测试，生成功能测试向量用于空闲时段在线检测。基于多款工业模块验证，相较随机向量故障覆盖率最高提升57.57，测试效率提升85%，符合ISO26262功能安全规范。

## 背景和动机
1. 传统ATPG、硬件BIST需要切换测试模式，中断系统正常运行，车载等连续运行设备无法接受停机测试。
2. 商用STL为人工定制、设计绑定，自动化生成方案缺失，迭代成本高、复用性差。
3. 纯随机测试向量故障覆盖偏低，大量向量才能达到基础覆盖，占用片上存储与运行带宽。
4. 现有ML测试生成仅单一模型，缺少预生成+迭代优化两级流程，向量搜索效率不足。
5. ISO26262/IEC61508要求运行时永久故障检测，亟需非侵入、可后台执行的在线测试方案。

## 相关工作
1. 硬件BIST/LFSR：新增片上测试电路，带来面积功耗开销，切换模式打断业务流程。
2. ATPG扫描测试：依赖扫描链，测试前后保存恢复系统上下文，在线场景不适用。
3 人工STL库：闭源定制，每款设计单独开发，自动化程度极低。
4. 单一ML向量生成（GAN/基础VAE）：无覆盖导向迭代优化，冗余测试向量多。
5. 传统在线SBST：向量无智能筛选，同等覆盖下向量数量庞大，存储开销高。

## 本文解决方案
### 1 VAE电路感知向量预生成模块
网表图GNN提取电路结构特征，与已有测试向量拼接输入VAE；联合重构损失与KL正则损失训练，学习有效测试向量隐分布，批量生成候选向量。
### 2 PPO强化学习覆盖优化器
以故障覆盖率增量为即时奖励，迭代扰动VAE输出向量；仅保留提升覆盖的向量，快速剔除无效冗余测试序列。
### 3 自动化STL编译流水线
将优化后的功能向量转为C++测试用例，配套编译脚本、仿真驱动，生成可在系统空闲周期后台执行的自测试库。
### 4 非侵入在线执行机制
STL无需修改原始电路、不切换测试模式，分时复用空闲时钟周期，不干扰正常业务运行。
### 5 故障仿真评估链路
集成Xcelium故障注入工具，自动统计永久/瞬态故障覆盖率，为RL奖励提供量化指标。

## 实验分析
1. 测试基准：SDRAM控制器、ORIF、SPRAM、OCMCMT四款开源工业门级模块。
2. 覆盖指标：固定100向量，随机向量覆盖33%~41%，本文方法提升至52%~59%，最高增幅57.57%。
3. 效率指标：达到同等基线覆盖仅需15~19条ML向量，相较随机方案效率提升最高85%。
4. 工程落地：自动输出Verilator适配C++测试bench，无需人工编写测试代码。
5. 适用场景：可用于汽车、航空航天等需不间断运行的功能安全芯片在线故障检测。

## 研究启发
1. 车载功能安全芯片必须抛弃侵入式扫描/BIST，基于软件STL的后台分时测试是更优在线检测方案。
2. 生成模型+强化学习两级架构可高效缩减测试向量规模，大幅降低片上存储开销。
3. 电路拓扑特征融入生成模型，能定向激活难测故障区域，显著提升故障覆盖率。
4. 面向ISO2626等安全标准的EDA工具，需兼顾测试效果与系统运行连续性。
5. 自动化STL生成可替代人工编写测试库，缩短安全芯片验证迭代周期。
