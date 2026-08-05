---
title: "AutoPower: Automated Few-Shot Architecture-Level Power Modeling by Power Group Decoupling"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# AutoPower: Automated Few-Shot Architecture-Level Power Modeling by Power Group Decoupling

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://zhiyaoxie.com/files/DAC25_AutoPower.pdf">https://zhiyaoxie.com/files/DAC25_AutoPower.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 架构级功耗建模，功耗组解耦，少量样本学习，自动化功耗建模</p>
</div>

---

## 研究概要
本文提出AutoPower少样本架构级功耗建模框架，基于功耗组解耦思想，分时钟、SRAM、逻辑三大模块独立建模，各模块内部进一步拆分子模型。仅需2组CPU配置训练，预测MAPE低至4.36%、R²达0.96，相比McPAT-Calib误差降低5%，支持细粒度时序功耗曲线预测。

## 背景和动机
1. RTL综合+PrimePower标准功耗流程耗时数周，架构早期DSE缺少快速精准功耗评估工具。
2. 传统McPAT、Wattch解析模型依赖人工定制，新架构适配成本极高、预测误差大。
3. 现有ML功耗模型为数据饥渴型，获取大量带真值配置需要反复VLSI流程，工程落地不现实。
4. 主流混合建模方案依赖人工定义资源函数，无全自动分层解耦机制，少样本场景精度差。
5. 处理器SRAM、时钟占总功耗80%以上，但现有方法未针对二者硬件分层特性专项建模。

## 相关工作
1. 解析功耗模型(McPAT/Wattch)：人工编写电路功耗公式，架构迭代后需大规模修改，泛化能力弱。
2. McPAT-Calib：基于XGBoost全局拟合整机功耗，未拆分功耗组分，少量样本下拟合偏差显著。
3. 组件级ML模型：分部件训练但无SRAM四级分层、时钟门控专项建模，硬件先验利用不足。
4. Panda解析+混合学习：依赖人工设计资源解析函数，无法全自动适配任意微架构。
5. 神经网络迁移功耗模型：训练样本需求量大，无法适配仅少量可用配置的工业场景。

## 本文解决方案
### 1 双层功耗解耦整体架构
跨组解耦划分时钟、SRAM、逻辑三大独立功耗组；每组内部依据硬件分层特性拆分子模型，仅用架构层软硬件特征完成预测，无需RTL细节。
### 2 时钟分层子模型
拆解无门控寄存器、门控寄存器、门控单元三类功耗；线性模型预测寄存器总数与门控率，XGBoost预测等效激活率，组合公式计算时钟总功耗，原生支持时钟门控优化建模。
### 3 SRAM四级分层建模
提出组件-存储位-逻辑块-宏单元四层硬件层级；通过容量/吞吐缩放规律预测SRAM块尺寸，XGBoost预估读写频次，映射工艺库宏单元参数得到SRAM功耗。
### 4 逻辑双分支建模
寄存器功耗由硬件规模+激活率相乘；组合逻辑拆固定基准功耗与时序波动系数，分别训练模型适配不同负载下组合电路功耗变化。
### 5 少样本适配机制
各子任务特征简单、拟合维度低，仅2组真值配置即可完成训练，支持百万周期大规模负载细粒度时序功耗预测。

## 实验分析
1. 实验平台：Chipyard生成15种BOOM乱序RISC-V配置，gem5提取事件特征，VCS+DC+PrimePower生成真值功耗，8组标准测试程序。
2. 整机精度：2组配置训练下AutoPower MAPE=4.36%、R²=0.96；对比McPAT-Calib MAPE下降5%、R²提升0.09。
3. 模块消融：单独移除分层解耦(AutoPower−)后时钟/SRAM模块误差大幅上升，验证分层建模核心价值。
4. 时序预测：GEMM、SPMM百万周期负载，50步长细粒度功耗平均误差仅2%~11%。
5. 扩展性：不同发射宽度、缓存大小、重排序缓存规模的CPU配置下均保持稳定低误差。

## 研究启发
1. 处理器功耗建模应遵循硬件物理分层，将SRAM、时钟等高占比通路单独建模可大幅降低少样本拟合难度。
2. 架构级特征足够精准推导底层存储、寄存器硬件规模，无需RTL内部电路细节即可完成功耗预估。
3. 分离静态硬件规模与动态负载激活两类特征，使用轻量化线性模型+XGBoost组合是少样本建模最优搭配。
4. 时钟门控、SRAM宏映射等VLSI底层规则可转化为架构层解析公式，降低机器学习拟合压力。
5. 功耗组解耦范式可推广至各类处理器、加速器架构，解决早期设计空间探索功耗评估慢、样本稀缺痛点。
