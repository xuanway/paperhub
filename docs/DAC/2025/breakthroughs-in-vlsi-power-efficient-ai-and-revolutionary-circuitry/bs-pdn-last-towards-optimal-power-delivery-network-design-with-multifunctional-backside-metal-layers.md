---
title: "BS-PDN-Last: Towards Optimal Power Delivery Network Design With Multifunctional Backside Metal Layers"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# BS-PDN-Last: Towards Optimal Power Delivery Network Design With Multifunctional Backside Metal Layers


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133344">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133344</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 背面供电网络，背面时钟网络，性能优化，设计流程顺序</p>
</div>


---

## 研究概要
本文提出BS-PDN-last后端供电版图流程，将电源布线延后至时钟/信号布线完成后，搭配预占位规划与分层补充分布式电源带。解决传统PDN-first流程时钟单元移位、时序恶化矛盾。3nm工艺多芯片验证，总负时序余量降低90%，最高性能提升12%，能效提升18.9%。

## 背景和动机
1. 先进工艺正面金属阻性高，背面厚金属BS-PDN可大幅压降IR损耗，业界希望背面金属同时承载电源、时钟(BS-CDN)实现PPA优化。
2. 传统PDN-first先铺电源再做背面时钟，nTSV与电源带短路、宽时钟单元造成版图重叠，需大量单元移位破坏最优布局。
3. 单元大幅偏移扰乱时钟树，时序恶化，形成IR压降与时序性能固有权衡，工业芯片收益极低。
4. 现有工作缺少统一流程量化对比正面、纯背面、多功能背面三类架构，缺乏真实负载矢量级评估体系。

## 相关工作
1. 基础BS-PDN方案：仅背面铺电源，未复用背面做时钟，金属资源利用率低，无法抵消背面工艺成本。
2. BS-CDN时钟布线：将前端时钟单元转为背面配对缓冲，但全部采用PDN-first流程，时序增益有限甚至倒退。
3. 背面信号线BSS：复用背面传输数据，但未解决电源与互连线版图冲突问题。
4. 传统前端FS-PDN：电源与信号抢占金属层，IR压降严重，高频大算力芯片性能瓶颈突出。

## 本文解决方案
### 1. BS-PDN分步整体流程
先布局、预占位BS电源阻挡层，再完成前后端时钟、全部信号布线，最后执行背面电源完整布线与优化细化，彻底规避前期电源对时钟的干扰。
### 2. BS-PDN预占位规划算法
在MB1/MB2背面金属预先设置阻挡区域，预留电源带走线通道，兼顾存储宏周边窄区域与规整电源焊盘排布需求。
### 3. 时序感知背面时钟转换
锁定关键路径逻辑单元，仅对非关键路径时钟缓冲最小位移合法化，配对BS-OUT/BS-IN背面时钟单元，减少版图冲突。
### 4. 最大化电源带生成与细化算法
先沿空白区域铺设长P/G带，再在剩余空隙插入短分段提升金属利用率；可动态调节线宽、间距平衡IR、耦合电容与热传导。
### 5. 矢量级精准评估框架
VCS生成波形转SAIF开关文件，映射门级功耗，Redhawk做IR分析、Primetime时序标定，实现真实算力负载下PPA量化。

## 实验分析
1. 实验平台：3nm GTCAD工艺，AES/RocketChip/Gemmini三类基准，对比FS-PDN、PDN-first+BS-CDN、BS-PDN-last。
2. 时序指标：TNS平均下降90%，最大单元移位从数十微米降至0.4μm内，最高工作频率提升12%。
3. 供电性能：动态IR压降可控，MB1/MB2金属利用率提升至83%/87%以上。
4. 算力负载：Gemmini跑ResNet-50，相比纯前端PDN性能+16.1%、能耗-17.4%、能效+18.9%。
5. 参数权衡：电源带间距增大IR恶化、热传导提升；电源时钟间距可小幅降低耦合电容，但过度放宽会限制布线资源。

## 研究启发
1. 多功能背面金属不能先铺电源，PDN-first会产生不可调和版图与时序冲突，后置电源是核心破局思路。
2. 预占位阻挡层是流程关键，提前锁定电源通道可在不打乱时钟布局前提下最大化背面金属利用率。
3. 时序敏感单元需锁定不位移，仅松弛非关键路径缓冲，兼顾时钟树完整性与DRC合规。
4. 长短结合分段电源带可填充空白背面金属，在不干扰时钟的前提下进一步抑制IR压降。
5. 背面设计评估不能仅看静态版图，必须结合真实AI/处理器负载做矢量级功耗、IR、时序联合仿真。