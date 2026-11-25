---
title: "MAGE: A Multi-Agent Engine for Automated RTL Code Generation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# MAGE: A Multi-Agent Engine for Automated RTL Code Generation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133191">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133191</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/stable-lab/MAGE">https://github.com/stable-lab/MAGE</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多智能体系统，RTL代码生成，高温度采样，状态检查点机制 </p>
</div>


---

## 研究概要
本文提出开源多智能体RTL生成引擎MAGE，划分测试台、RTL生成、评判、调试四类专用智能体；设计高温候选采样与Verilog状态断点调试机制。在VerilogEval基准下功能正确率达95.7，较Claude3.5提升23.3%，大幅提升自然语言转Verilog的语法与功能完备性。

## 背景和动机
1. 单LLM智能体需兼顾RTL、测试台、仿真调试多类异构任务，上下文切换负担重，生成代码功能通过率低。
2. 传统低温采样输出保守、候选单一，难以覆盖正确硬件逻辑；单纯高温噪声大，缺少筛选机制无法发挥多样性优势。
3. 现有调试仅输出整体匹配通过率，无逐时钟状态明细，LL难以定位时序/组合逻辑底层bug。
4. 主流RTL生成系统多闭源、依赖专有AST波形工具，扩展性差，缺少完整开源协同生成框架。
5. 可综合RTL与不可综合测试台混生成易互相干扰，导致测试用例偏倚、验证客观性下降。

## 相关工作
1. 通用大模型(GPT4o/Claude3.5)：单次直通生成，无仿真反馈迭代，硬件逻辑理解不足，功能正确率仅75%左右。
2. RTL专用微调模型(ITERTL/CodeV)：仅优化编码输出，缺少闭环仿真调试流程。
3. 单智能体框架(OriGen/AutoVCoder)：单一模型兼顾编码与测试台，任务耦合严重，上下文混乱。
4. 闭源多智能体(AIVRIL/VerilogCoder)：私有波形分析工具，不开放、适配性弱，断点调试机制缺失。
5. 软件代码高温采样方案：仅适配通用软件，未针对硬件时序、多周期状态设计筛选与定位方法。

## 本文解决方案
### 1 四类分工协同多智能体架构
测试台智能体生成文本波形化测试激励；RTL智能体基于规范生成可综合代码；评判智能仿真打分筛选候选；调试智能体依托状态日志迭代修复，各智能体独立上下文解耦。
### 2 高温采样-打分候选筛选机制
设置高温度系数批量生成多组RTL候选；以失配数构造得分函数，选取Top-K优质样本进入调试迭代，兼顾多样性与代码质量。
### 3 Verilog状态断点调试机制
提取首个失配时钟周期前后窗口文本波形日志，给调试智能体提供精确时序/信号偏差信息，替代笼统总通过率反馈，精准定位逻辑缺失。
### 4 五阶段闭环流水线
测试台生成→RTL初生成→仿真校验→高温采样择优→断点调试迭代，单模块最多5轮纠错，兼顾效率与正确性。
### 5 开源轻量化实现
基于Icarus Verilog、LlamaIndex搭建，无闭源依赖，对外提供通用LLM接入接口，完整开源可复现。

## 实验分析
1. 评测基准：VerilogEval-Human v1/v2两套标准，对比通用LLM、专用RTL模型、单/闭源多智能体系统。
2. 核心指标：MAGE高温度配置Pass@1最高95.7，相比原生Claude3.5提升23.3%，全面优于所有基线。
3. 消融实验：多智能体分工相比单智能体提升9.7%；断点调试、高温采样均为核心增益模块，移除后正确率大幅下滑。
4. 采样效果：高温候选平均失配数量显著低于低温，多轮调试平均得分由0.669提升至0.890。
5. 案例验证：无断点仅能大范围猜测故障，带状态窗口可直接定位缺失逻辑项，一次修复通过仿真。

## 研究启发
1. RTL生成、测试、验证、调试属于异构任务，多专用智能体解耦分工能消除上下文冲突，显著提升代码可靠性。
2. 高温度采样可拓展逻辑候选空间，但必须配套仿真打分筛选才能平衡噪声与多样性。
3. 硬件bug调试不能仅依靠全局结果，逐时钟状态断点日志可为LLM提供细粒度故障定位依据。
4. 闭源专有波形/AST工具限制落地，纯文本仿真日志可构建通用、开放的LLM调试链路。
5. 自然语言转硬件代码需要“生成-仿真-细粒度反馈-迭代修复”完整闭环，单次直通生成难以满足功能要求。