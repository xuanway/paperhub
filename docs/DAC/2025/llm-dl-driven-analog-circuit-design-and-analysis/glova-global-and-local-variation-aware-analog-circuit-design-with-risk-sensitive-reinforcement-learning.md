---
title: "GLOVA: Global and Local Variation-Aware Analog Circuit Design with Risk-Sensitive Reinforcement Learning"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# GLOVA: Global and Local Variation-Aware Analog Circuit Design with Risk-Sensitive Reinforcement Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.11208">https://arxiv.org/abs/2505.11208</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模拟电路综合，PVT变化，强化学习 </p>
</div>


---

## 研究概要
本文提出GLOVA面向PVT全局+局部失配的模拟电路尺寸优化框架，采用风险敏感强化学习搭配集成评价网络，配套μ-σ评估、仿真重排序加速验证。支持角点、本地/全局蒙特卡洛多类工业仿真，DRAM、运放等电路测试，相较主流方法采样效率最高提升80.5倍，总耗时降低76倍，优化成功率100%。

## 背景和动机
1. 先进工艺全局片间、局部片内器件失配严重，模拟电路性能波动大，传统优化仅关注典型PVT点，良率难以保障。
2. 现有RL/贝叶斯模拟优化每次迭代执行海量MC仿真，SPICE仿真成本极高，设计周期漫长。
3. 主流方法仅拆分单一PVT角任务，无法统一建模全局+局部分层失配分布，最坏工况预测不准。
4. 验证阶段无提前失效预判机制，全部样本完整仿真，大量不合格设计浪费算力。
5. 缺少仿真优先级调度策略，高失效概率工况后置，需完整跑完所有样本才能判定设计失败。

## 相关工作
1. 贝叶斯模拟优化（PVTSizing）：批量采样搜索，失配建模简单，海量MC场景仿真开销巨大。
2. Multi-Task RL（RobustAnalog）分角点任务，但未区分全局/局部失配，最坏情况估计保守。
3. 普通DDPG强化学习：风险中性，不约束极端失配下性能退化，良率偏低。
4. 传统角点/MC仿真工具：仅用于验证，未嵌入优化闭环，无提前筛检机制。
5. TuRBO局部贝叶斯：仅优化初始采样，全过程无分层失配感知，鲁棒性不足。

## 本文解决方案
### 1 风险敏感Actor-Critic优化内核
基于规避风险损失函数，训练时仅留存各工况最坏性能样本更新回放缓存；Actor输出晶体管宽长电容尺寸向量，优先抑制极端失配带来性能恶化。
### 2 集成式Critic网络
多基础模型集成预测性能上下界，引入方差风险项量化失配不确定性，仅少量MC样本即可精准估计最坏工况，大幅减少仿真次数。
### 3 μ-σ预评估快速筛检
抽取少量失配样本统计均值与标准差，加权保守边界判定设计是否具备验证价值，不合格直接返回优化，跳过完整MC仿真。
### 4 双层仿真重排序算法
1）角点按t-SCORE排序，高失效工况优先仿真；2）失配样本通过皮尔逊相关计算h-SCORE，提前仿真高风险器件组合，快速发现失效。
### 5 分层失配建模流水线
先采样全局片间工艺偏差，再基于全局分布采样片内局部失配，兼容纯角点、本地MC、全局+联合MC三类工业验证模式。

## 实验分析
1. 测试电路：StrongARM锁存器、浮动运放、DRAM感存放大器，28nm工艺，30组标准PVT角，支持多层失配MC仿真。
2. 效率指标：对比PVTSizing、RobustAnalog，所有电路采样效率最高提升80.5倍，标准化运行时间最大缩减76倍。
3. 优化成功率：GLOVA全部测试场景100%满足所有PVT与失配约束，基线复杂DRAM电路最低仅53%达标。
4. 消融实验：集成评价网络、μ-σ评估、仿真重排序任一模块移除，仿真量提升3~11倍，部分场景优化成功率下降。
5. 高难度场景：DRAM阵列器件多、失配敏感，GLOVA仍保持稳定收敛，基线方法迭代量激增且达标率暴跌。

## 研究启发
1. 模拟鲁棒优化必须统一建模全局片间、局部片内两层工艺失配，单一偏差模型无法贴合真实晶圆波动。
2. 风险敏感强化学习比普通优化更适合良率导向模拟尺寸设计，主动规避极端失配失效点。
3. 集成多模型可通过少量样本精准预估性能最坏边界，大幅降低昂贵SPICE仿真调用次数。
4. 验证阶段提前预判+高风险工况优先仿真，能从源头削减无效仿真算力消耗。
5. 优化与验证闭环一体化框架是缩短模拟电路设计迭代周期的核心方案。
