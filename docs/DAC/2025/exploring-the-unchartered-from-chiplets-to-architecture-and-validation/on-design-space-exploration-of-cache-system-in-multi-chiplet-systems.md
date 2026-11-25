---
title: "On Design Space Exploration of Cache System in Multi-Chiplet Systems"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# On Design Space Exploration of Cache System in Multi-Chiplet Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://repository.essex.ac.uk/40439/1/MultiChipletCacheDSE-DAC2025.pdf">https://repository.essex.ac.uk/40439/1/MultiChipletCacheDSE-DAC2025.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 众核系统，多芯粒系统，设计空间探索 </p>
</div>


---

## 研究概要
本文面向多芯粒众核系统缓存层级设计空间探索，构建缓存图与芯粒互联拓扑双图模型，基于C-AMAT建立时延、功耗、成本解析模型，提出双层优化算法。交替求解缓存、互联网络子问题，PARSEC等负载测试，相较Zen4、SPR、IntLP执行时间平均分别降低39.7%、39.2%、25.91%。

## 背景和动机
1. 多芯粒架构芯间互联时延远高于芯内通信，缓存配置直接决定跨芯流量与系统性能，设计参数维度爆炸、寻优难度极大。
2. 现有DSE工具仅优化单层级缓存尺寸，无法联合缓存层级、芯粒划分、片上互联拓扑协同寻优，设计空间挖掘不充分。
3. AMD Zen4、Intel SPR等商用芯粒架构缓存与互联方案固定，难以适配多样负载的最优需求。
4. 传统线性规划类方法仅支持少量缓存参数调优，缺失完整C-AMAT并发访存时延建模，评估精度不足。
5. 缓存与互联相互耦合，单阶段全局优化计算开销过高，缺少分治迭代求解思路。

## 相关工作
1. IntLP整数线性规划：仅优化L1/L2缓存容量、关联性，无法覆盖芯粒拓扑、多级缓存完整设计空间。
2. NN-Baton/Monad：聚焦加速器芯粒功能划分，未针对通用CPU缓存层级做联合性能建模。
3. C-AMAT并发访存模型：仅提供内存时延计算理论，未适配多芯粒跨芯通信场景。
4. 传统缓存DSE：局限单芯片多核架构，不区分芯内/芯间链路时延差异，无互联拓扑协同优化。
5. 商用芯粒架构(Zen4/SPR)：固定缓存与互联配置，无自动化设计空间搜索能力。

## 本文解决方案
### 1 双图系统建模
构建存储层级图$G_M$刻画各级缓存、核、DRAM参数；芯粒互联拓扑图$G_I$描述路由、D2D链路，区分芯内/芯间传输时延。
### 2 全套解析性能模型
基于多项式拟合缓存失效率；Bellman方程求解最短路径零负载时延，G/G/1排队模型计算路由排队延迟；扩展C-AMAT适配跨芯并发访存，同时建立面积、功耗约束模型。
### 3 双层迭代优化框架
上层子问题P1：分支定界算法优化缓存层级、每芯核数、缓存规格，引入LPM匹配度剪枝；下层子问题P2：穷搜Mesh/Torus等互联拓扑与片内微片尺寸。
### 4 多层剪枝策略
包含最优值剪枝、功耗成本不可行剪枝、LPM缓存匹配度剪枝、搜索队列长度限制，大幅缩减分支搜索规模。
### 5 收敛迭代机制
交替优化缓存、互联子问题，迭代至C-AMAT变化量低于阈值或达最大迭代次数输出最优架构。

## 实验分析
1. 实验环境：Sniper仿真器+McPAT功耗模型，基准覆盖PARSEC、神经网络、数据库负载，对比Zen4、SPR、IntLP。
2. 200W功耗约束：本文方案执行时间较Zen4降39.7%、SPR降39.2%、IntLP降25.91%；160W低功耗场景优化幅度仍超18%。
3. LPM阈值消融：65%阈值平衡搜索耗时与最终性能，阈值过高/低均会损失优化收益。
4. 负载通用性：fft、CNN、TPC-H等各类负载均稳定取得性能提升，无明显短板场景。
5. 效率优势：双层分治+多剪枝大幅降低全局寻优复杂度，高维芯粒缓存设计空间可快速收敛。

## 研究启发
1. 多芯系统必须将缓存层级与芯间互联拓扑联合协同优化，割裂设计会造成大量跨芯流量、严重拖慢访存速度。
2. 面向芯内/芯间差异化时延扩展C-AMAT模型，能精准刻画并发访存真实系统性能。
3. 双层分治迭代可破解高维耦合设计空间全局优化算力瓶颈，搭配多层剪枝进一步压缩搜索范围。
4. 缓存层级匹配度LPM是高效剪枝指标，能提前剔除吞吐不匹配低效缓存组合。
5. 固定商用芯粒缓存互联架构无法适配多样负载，自动化解析DSE是未来2.5D/3D芯粒协同设计关键手段。
