---
title: "PIMDup: An Optimized Deduplication Design on a Real Processing-in-Memory System"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PIMDup: An Optimized Deduplication Design on a Real Processing-in-Memory System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133045">https://ieeexplore.ieee.org/document/11133045</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 去重系统，存内处理，UPMEM DPU</p>
</div>


---

## 研究概要
本文面向UPMEM商用DPU存内硬件提出PIMDup去重系统，解决DPU无互通、乘法低效、上下行带宽失衡、分块边界不一致四大痛点。设计防割裂分段、编码边界向量、局部最大值分块三大优化，VM数据集验证相比CPU基线提速1.67倍，分块结果完全一致。

## 背景和动机
1. 数据去重中内容分块CDC耗时占总流程53%，冯诺依曼架构海量数据搬运造成严重性能损耗。
2. UPMEM DPU无跨核直通信、乘法运算吞吐量远低于加减，且CPU→DPU下行带宽远高于DPU回传上行带宽。
3. 文件简单均分至多DPU会造成窗口标记跨分段，DPU数量变化时分块结果不一致，降低去重压缩率。
4. 传统Rabin哈希CDC依赖大量乘除，在DPU上执行效率极低，缺少适配存内单元的分块算法。

## 相关工作
1. CPU并行CDC去重：仅优化多核软件并行，无法消除内存反复加载的搬运瓶颈。
2. 通用UPMEM DPU负载加速：面向RNA、图计算等，未针对CDC分块的跨段边界问题做定制。
3. 传统Rabin/FastCDC分块：基于多项式哈希，计算密集，不适配无高效乘法的PIM硬件。
4. 通用存内计算框架：未解决DPU间无法互通带来的全局分块边界识别难题。

## 本文解决方案
### 1 防割裂文件分段ASFS
分段设置大于窗口长度重叠区，保证跨段标记完整落在某一DPU内，任意DPU数量下分块结果保持一致。
### 2 编码边界向量压缩回传
DPU仅输出标记比特流，8bit打包传输，回传数据量压缩至原始1/8，缓解上行带宽瓶颈；CPU汇总全局边界判定最终分块。
### 3 DPU友好局部最大值分块
舍弃哈希多项式运算，仅滑动窗口比较字节大小，全程只用加减无乘除，匹配DPU运算性能特性。
### 4 CPU-DPU流水线重叠
DPU并行处理分块，CPU同步执行指纹、索引，两阶段流水掩盖主机开销，充分利用并行算力。

## 实验分析
1. 实验平台：Xeon主机+20片UPMEM DIMM共2560个DPU，测试30GB多版本VM镜像数据集。
2. 整体性能：DPU规模4~36秩线性提速，满配相较纯CPU去重提速1.67倍。
3. 分块算法对比：局部最大值方案相比Rabin哈希减少约50%分块耗时，规避DPU乘法短板。
4. 数据传输：编码向量大幅降低DP→CPU上行数据量，传输开销可控。
5. 一致性验证：不同DP秩下分块输出完全相同，去重压缩率无衰减。

## 研究启发
1. 商用DPU无跨核通信是核心约束，重叠分段可低成本解决跨窗口标记识别难题。
2. PIM负载必须规避乘除类重运算，仅基于比较/加减的轻量化算法才能释放存内并行收益。
3. CPU-DPU上下行带宽不均衡场景，轻量特征编码压缩回传数据是关键优化手段。
4. 分块、索引两类任务可异构流水并行，DPU承载访存密集分块，CPU负责索引匹配。
5. 面向真实商用PIM芯片的系统设计，不能仅追求并行度，必须兼顾硬件原生运算能力限制。
