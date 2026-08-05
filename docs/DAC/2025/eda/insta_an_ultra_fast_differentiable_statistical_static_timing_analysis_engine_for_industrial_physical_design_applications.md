---
title: "INSTA: An Ultra-Fast, Differentiable, Statistical Static Timing Analysis Engine for Industrial Physical Design Applications"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# INSTA: An Ultra-Fast, Differentiable, Statistical Static Timing Analysis Engine for Industrial Physical Design Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA3: Timing Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132858">https://ieeexplore.ieee.org/document/11132858</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/NVlabs/INSTA">https://github.com/NVlabs/INSTA</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 可微分静态时序分析，GPU加速时序引擎，时序梯度，物理设计优化 </p>
</div>


---

## 研究概要
本文提出INSTA，首款与商用签核工具高精度对齐的可微GPU统计STA引擎。一次性从参考工具抽取弧延迟，CUDA内核实现带CPPR/OCV的Top-K时序传播，LSE算子保证可微，提出时序梯度用于全局优化。3nm千万引脚设计0.1s完成时序计算，门控尺寸/布局应用分别实现15%TNS改善、59.4%TNS降幅。

## 背景和动机
1. 先进3nm工艺下商用STA迭代仿真耗时极长，增量时序工具仍存在巨大计算瓶颈，物理设计迭代周期缓慢。
2. 现有GPU-STA采用简化延迟模型，无法复刻商用工具专有时序计算逻辑，与签核结果相关性差，无法工业落地。
3. 过往GPU时序引擎不完整支持CPPR、OCV等工业必备悲观消除机制，时序精度存在显著偏差。
4. 传统时序优化仅依靠净权重，缺乏单时序弧对全局TNS/WNS的精确敏感度，优化局部化、结果次优。
5. 现有时序工具不可微，无法构建梯度导向全局时序优化，难以联合门尺寸、布局做端到端协同调优。

## 相关工作
1. 基础GPU-STA：基于NLDM/Elmore简化模型，缺失CPPR/OCR，与商用签核精度差距大，无微分能力。
2. CPP专项加速工具：仅局部优化悲观消除，未完整打通全局时序传播，不支持梯度优化。
3. 学习型可微时序模型：依赖神经网络拟合，泛化弱、精度不及签核标准，速度劣势明显。
4. 传统时序驱动布局：统一网络权重，无法区分单条弧的时序贡献，优化效率低。
5. 商用签核STA：精度达标但CPU串行增量迭代速度极慢，无梯度输出能力。

## 本文解决方案
### 1 商用工具克隆式初始化流程
一次性从签核工具提取时序弧、约束、时钟到达、OCV方差等全部参数，基于拓扑排序构建分层时序图，无需重构延迟模型，保证基础精度对齐。
### 2 GPU并行Top-K统计时序传播CUDA内核
每条GPU线程处理单引脚，高斯分布建模OCV到达时间；固定长度优先队列实现高效CPPR，每条路径绑定唯一起点，精准消除公共路径悲观。
### 3 LSE平滑可微近似算子
替换不可严格取max操作，用对数指数平滑所有路径贡献，完整保留梯度流，实现全局时序指标对每条时序弧求导。
### 4 时序梯度全局优化范式
反向CUDA内核配合PyTorch自动微分，计算每条时序弧对TNS/WNS的梯度，作为时序敏感度精准定位瓶颈。
### 5 两大物理设计衍生应用
1) INSTA-Size：梯度筛选关键单元做门控尺寸优化，大幅减少调整单元数量，TNS显著改善；
2) INSTA-Place：弧级梯度加权布局目标，解决传统统一净权重缺陷，同时优化线长与时序。

## 实验分析
1. 精度测试：3nm五款工业设计，端点松弛相关系数达0.9999，千万引脚电路完整传播仅0.39秒，平均时序失配仅几飞秒。
2. 增量速度：商用门尺寸流程中INSTA比原生增量STA提速25倍，仿真开销大幅下降。
3. INSTA-Size：相较商用签核优化TNS最高降低15%，需调整单元平均减少68%。
4. INSTA-Place：对比DREAMPlace基线，TNS最大降低59.4%，HPWL同步缩减16.2%。
5. 消融验证：关闭CPP后时序偏差大幅上升；LSE移除后梯度断裂，全局优化效果显著退化。

## 研究启发
1. GPU时序引擎无需自研完整延迟模型，复用商用工具提取弧参数可低成本实现签核级精度。
2. CPPR、OCV是先进工艺时序必备模块，GPU并行Top-K队列可在可控内存开销下实现高精度悲观消除。
3 最大值算子破坏可微性，LSE平滑近似是搭建梯度导向时序优化的关键数学手段。
4. 单时序弧梯度比传统净权重更精准刻画时序瓶颈，可实现真正全局时序优化而非局部修补。
5. 可微GPU时序引擎可作为统一底座，无缝支撑门控尺寸、全局布局等多类物理优化任务。