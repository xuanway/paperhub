---
title: "PairGraph: An Efficient Search-space-aware Accelerator for High-performance Concurrent Pairwise Queries"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PairGraph: An Efficient Search-space-aware Accelerator for High-performance Concurrent Pairwise Queries

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132889">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132889</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>并发成对查询，搜索空间感知处理模型，共享区域生成，重叠驱动处理，数据路由 </p>
</div>

---

## 研究概要
本文提出面向并发点对点图查询的PairGraph专用加速器，设计感知搜索空间SPM处理模型，通过无冗余共享区域生成、重叠驱动执行挖掘时空局部性。28nm流片仿真验证，对比CPU/GPU与多款图加速器，提速1.67~14.25倍，片上缓存复用大幅降低片外访存与能耗。

## 背景和动机
1. 导航、推荐等场景存在大量并发点对点查询(CPQ)，现有方案仅优化单查询，忽略多查询间数据复用。
2 CPQ查询搜索空间重叠但时空局部性差，73%以上访存为冗余重复加载，碎片式共享挤占片上缓存，有效复用数据不足14%。
3. CPU/GPU通用架构无精细缓存路由控制，无法区分共享/非共享图数据，难以固定高频共享数据至片上。
4. 现有图加速器面向全图迭代任务，未针对点对点查询双向剪枝、窄搜索空间特性做硬件定制。

## 相关工作
1. 单点对点优化：Pnp、SGraph仅改进单查询剪枝策略，无并发数据复用机制，批量执行冗余访存严重。
2. 通用并发图系统：Gemini(CPU)、Gunrock(GPU)支持批量图任务，但未挖掘点对点查询空间相似性，缓存利用率低。
3. 图专用加速器：LCCG、ScalaGraph、ReGraph面向点对全图遍历，未适配点对点窄搜索空间，共享识别能力弱。
4. 分布式/内存图框架：CGraph、Congra等侧重软件调度，缺少硬件层共享数据路由与预取加速。

## 本文解决方案
### 1 感知搜索空间SPM双层处理模型
1）无冗余共享区域生成：双向广度遍历打标签，分批传播区域权重，仅一次遍历边消除重复传播，提前筛选多查询高频共享子图；
2）重叠驱动分块执行：按缓存容量分批加载共享数据并锁存，全部查询处理完成后再置换，最大化数据复用。

### 2 PairGraph硬件整体架构
由多并发瓦片CTile阵列、片上网络NoC、HBM存储组成，每个CTile包含控制、处理、加载、缓存四大模块。

### 3 硬件专用优化单元
1）任务级预取+地址打包引擎：合并细碎内存请求，将HBM带宽利用率由2%提升；
2）感知重叠数据路由器：4位路由码区分共享/私有/旁路数据，分离图结构与属性缓存；
3）SPR散列剪枝归并流水线+权重传播通道：并行处理查询遍历与区域权重计算；
4）跳数感知查询映射：按源目最小跳数均衡分配任务，解决瓦片负载失衡。

## 实验分析
1. 实验配置：28nm工艺、1GHz，4个CTile每片6PE，WT/LJ/OR/TW/FS五大真实图，6类点对点查询。
2. 性能增益：相对Gemini提速5.59~14.25倍、Gunrock3.76~7.58倍，对比LCCG/ScalaGraph/ReGraph提速1.67~4.28倍。
3. 访存与能耗：片外通信降至基线21%~53%，平均能耗相比各基线降低4~443倍；芯片面积11.23mm²，功耗3.21W。
4. 消融与敏感度：区域权重均值为最优筛选阈值；并发查询越多加速效果越强；缓存容量越大复用收益越高。
5. 资源拆解：缓存模块占71.2%面积，处理单元功耗占总功耗52.1%。

## 研究启发
1. 并发点对点查询核心瓶颈是冗余片外访存，提前识别多查询共享子图是提速关键。
2. 通用CPU/GPU缓存机制无法精细化管控共享数据，必须定制路由、锁存硬件单元。
3. 图查询负载与源目跳数强相关，基于跳数的任务均衡可显著提升PE利用率。
4. 软件模型需配套专属流水线硬件，SPM算法优势仅能在专用加速器完全释放。
5. 细碎图内存请求严重浪费HBM带宽，地址打包批量访存是低成本带宽优化手段。
