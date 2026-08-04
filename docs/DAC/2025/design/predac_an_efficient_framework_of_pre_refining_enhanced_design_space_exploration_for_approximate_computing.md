---
title: "PreDAC: An Efficient Framework of Pre-Refining Enhanced Design Space Exploration for Approximate Computing"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PreDAC: An Efficient Framework of Pre-Refining Enhanced Design Space Exploration for Approximate Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132580">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132580</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 近似计算，设计空间探索，高层次综合</p>
</div>

---

## 研究概要
本文提出PreDAC近似计算设计空间探索框架，包含双层预精简流程与代价性能导向DSE算法。构建55类近似乘法器库，基于输入分布筛除冗余设计空间，搭配可调参代价公式与回溯微调。测试下预精简可提速最高87倍，自研DSE相较FPAX提速7.7倍、硬件开销再优化8.8%。

## 背景和动机
1. 近似计算依靠近似算术单元降低硬件开销，但人工配置方案效率极低，EDA工具支撑不足。
2. 现有DSE分为启发式随机搜索（迭代耗时巨）、分步近似法（易局部最优）两类，海量乘法器组合导致设计空间指数爆炸。
3. 蒙特卡罗误差评估、DC综合仿真计算开销极高，频繁调用拉长探索总时长。
4. 不同应用输入分布差异大，通用近似库存在大量非帕累托冗余单元，无应用专属精简手段。

## 相关工作
1. 启发式DSE(AutoAX/Egan)：随机遍历空间，收敛慢，大规模电路运行时间不可控。
2. JUMP Search(JS)：分步近似搜索，但无前置空间裁剪，冗余单元拖慢迭代速度。
3. FPAX：基于先验知识分步DSE，缺少自适应代价公式，优化上限有限。
4. 近似乘法器库(DRUM/Evoapprox8b)：仅提供器件，未配套面向应用的空间筛选流程。

## 本文解决方案
### 1 通用多类型近似乘法器库
整合人工设计、参数生成、遗传算法生成三类共55款近似乘法器，覆盖不同精度、功耗、面积权衡，适配图像/通信/AI多种任务。
### 2 双层预精简预处理流程
第一层：结合输入分布、误差/硬件指标筛选帕累托最优乘法器集合；第二层按DFG层级分类测试，剔除违反误差约束的单元，指数级缩减搜索空间。
### 3 可调参代价性能DSE公式
引入x/y超参适配MSE/MED/SNR多类误差指标，归一化硬件开销与误差，量化替换收益指导近似替换优先级。
### 4 四阶段增强DSE算法
代价计算→近似设计生成→误差校验→回溯微调；采用解析误差/硬件模型替代蒙特卡罗与DC，迭代超限回退并精细调优。

## 实验分析
1. 测试负载：RGB2YCbCr、3×3卷积、13抽FIR、高斯模糊四类典型误差容忍应用，对比JS、FPAX。
2. 预精简收益：搭配FPAX最高提速87倍，搭配JS硬件开销再降23%，筛除大量无意义配置。
3. DSE算法对比：同预精简条件下，PreDAC相对FPAX提速7.7倍，硬件指标额外优化8.8%。
4. 仿真效率：解析误差模型比蒙特卡罗快三个数量级，大幅削减迭代计算耗时。
5. 消融：预精简是提速核心，可调代价公式与回溯微调共同提升硬件优化程度。

## 研究启发
1. 近似DSE瓶颈核心是爆炸式设计空间，应用专属前置精简是低成本提速最优手段。
2. 不同误差度量、应用场景需差异化代价权重，固定评估公式难以获得最优折中方案。
3. 解析数学模型可替代蒙特卡罗与综合仿真，在不损失精度前提下大幅缩短评估耗时。
4. DFG层级对近似误差敏感度不同，分层校验可快速淘汰违规近似单元。
5. 分步近似+回溯微调组合，既能快速收敛，又能突破单纯分步算法的局部最优局限。
