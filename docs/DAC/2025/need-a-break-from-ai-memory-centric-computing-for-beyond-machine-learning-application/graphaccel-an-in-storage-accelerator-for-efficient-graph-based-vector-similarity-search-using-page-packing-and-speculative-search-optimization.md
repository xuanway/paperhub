---
title: "GraphAccel: An In-Storage Accelerator for Efficient Graph-Based Vector Similarity Search Using Page Packing and Speculative Search Optimization"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# GraphAccel: An In-Storage Accelerator for Efficient Graph-Based Vector Similarity Search Using Page Packing and Speculative Search Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132788">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132788</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存储内处理，SSD并行性，向量搜索 </p>
</div>


---

## 研究概要
本文提出GraphAccel SSD存内向量检索加速器，面向十亿级图结构ANNS。设计基于共享入边权重的图分块页打包算法减少闪存访问，搭配可丢弃投机搜索充分利用SSD通道并行。在SIFT1B等数据集验证，相比DiskANN、DiskANN++延迟分别降低80.5%、73.4%，召回率保持不变。

## 背景和动机
1. 十亿级向量图索引需存于SSD，图遍历访问随机、闪存页读取开销巨大，传统打包仅聚合直邻节点，页访问次数居高不下。
2. SSD存在多通道/芯片并行资源，但DiskANN波束搜索无请求优先级区分，无关任务占用空闲硬件，并行利用率低。
3. 闪存读扰动、电荷流失引发重读重试，读取时延波动大，现有方案无法动态调度规避时延波动带来的性能损失。
4. 主流存内检索方案依赖内存常驻图，无法支撑超大规模向量库，且未针对SSD底层硬件做协同优化。

## 相关工作
1. DiskANN/DiskANN++：基础磁盘图检索，Starpacking仅聚合直接邻居，波束搜索无投机调度，页I/O开销高。
2. VStore存内加速器：依赖多查询时间局部性，查询无规律时性能大幅衰减。
3. Pyramid分层存储方案：要求图常驻内存，无法适配百亿向量超大场景。
4. SmartSSD分布式检索：商用控制器调度固定，缺少动态投机丢弃机制，并行挖掘有限。

## 本文解决方案
### 1. GraphAccel-Packing页打包算法
将有向图转为无向加权图，边权重为两节点共享入边数量；利用大规模图划分工具均分节点至闪存页，大幅降低单次遍历读取页数；大图拆分子图并行划分平衡开销。
### 2. 投机并行GraphAccel-Search
区分必选正常请求、可丢弃投机请求；空闲通道才下发投机任务，资源繁忙直接丢弃；设置批量复检阶段补全未完成节点，不损失检索精度。
### 3. SSD存内硬件架构扩展
新增搜索单元执行距离计算、丢弃单元管控投机请求；搭配片上数据缓存减少闪存直达访问，适配NVMe多通道拓扑。
### 4. 闪存时延鲁棒调度
适配重读重试带来的可变延迟，动态释放空闲芯片资源处理投机任务，削弱时延抖动对整体查询的负面影响。

## 实验分析
1. 实验环境：MQSim SSD仿真器，8通道4芯片1TB固态，测试Turing100M/SIFT1B/DEEP1B三大十亿级向量数据集。
2. I/O开销：单查询平均页访问量相较DiskANN降低69.4%，相对DiskANN++下降58.4%。
3. 延迟收益：相同召回率下，对比DiskANN最高提速5.17倍，相比DiskANN++提速3.7倍；闪存老化场景优势进一步扩大。
4. 并行特性：波束宽度匹配芯片数32时性能最优，投机丢弃机制规避无效IO，无精度损耗。
5. 鲁棒性：3/6个月电荷流失老化场景下，相较基线延迟降幅仍维持70%以上，抗时延波动能力更强。

## 研究启发
1. 向量图同访节点不只是直接邻居，共享前驱节点是更强的访问关联，以此加权分块可显著压缩闪存I/O。
2. SSD多通道并行不能统一处理所有扩展任务，区分核心/投机请求、忙时丢弃是提升硬件利用率关键。
3. 投机检索必须配套批量复检流程，在不牺牲召回的前提下充分挖掘闲置存储算力。
4. 面向超大向量库的检索优化应深度贴合SSD底层页粒度、多通道硬件特征，不能仅优化图遍历算法。
5. 闪存介质老化带来时延抖动是不可忽略的约束，检索调度器需要具备动态资源适配能力。
