---
title: "GoPTX: Fine-grained GPU Kernel Fusion by PTX-level Instruction Flow Weaving"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# GoPTX: Fine-grained GPU Kernel Fusion by PTX-level Instruction Flow Weaving


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132627">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132627</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://mizuno-ai.wu-kan.cn/assets/image/2025/06/25/DAC25-GoPTX-Slides.pdf">https://mizuno-ai.wu-kan.cn/assets/image/2025/06/25/DAC25-GoPTX-Slides.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> GPU，内核融合，指令级并行，线程束停顿，数据冒险</p>
</div>

---

## 研究概要
本文提出GoPTX，面向PTX中间层细粒度GPU内核融合。通过合并多内核控制流图、时延感知指令交织、自适应代码分块提升ILP，解决记分板引发的warp停顿。基于A100多基准测试，相较并发基线平均提速11.2%，最高23%，有效提升每周期就绪warp数与硬件利用率。

## 背景和动机
1. 多内核并发执行时SM资源分配失衡，传统流/MPS仅做块级调度，无法挖掘指令级并行。
2. 现有内核融合为源码粗粒度拼接/分warp执行，跨内核独立指令无法穿插，大量流水线气泡、记分板停顿限制ILP。
3. 指令最优调度属于NP难问题，复杂分支、同步屏障融合易产生死锁，缺少PTX层细粒度交织方案。
4. 长短基本块尺寸差异大，可供穿插调度空间不足，现有方法未做块均衡优化。

## 相关工作
1. 硬件并发调度（MIG/MPS/Warped-Slicer）：仅线程块层面分配资源，无法优化单warp内部指令排布，无法消除记分板停顿。
2. 源码级内核融合VFuse/HFuse：分别串行拼接、分warp执行，粗粒度无法穿插独立指令，ILP提升有限。
3. GPU指令调度优化：仅单内核内部重排，不能利用跨内核无关指令掩盖延迟。
4. PTX编译优化工具：缺少面向多内核控制流合并、防死锁同步处理的融合框架。

## 本文解决方案
### 1. 多内核CFG合并算法
遍历双内核基本块状态，合并对应BB；分支路径插入虚节点统一控制流；同步屏障前填充空块规避跨分支死锁，保留原程序语义。
### 2. 时延感知贪心指令交织
基于微基准测得指令时延，每轮选择累计时延更小指令流抽取指令；时延相等优先选单指令高时延指令，拉长数据依赖链填充气泡。
### 3. 自适应代码分块策略
统计全块平均执行周期作为阈值，超长BB切分为均衡小段，扩大跨块指令交织调度窗口。
### 4. PTX全流程配套优化
自研ANTLR4 PTX解析器重命名标识符防冲突；微基准构建精确时延模型；遍历-maxrregcount平衡寄存器压力与并行度；多内核迭代融合。

## 实验分析
1. 实验平台：A100 40GB，CUDA12.5，测试Rodinia、ONNX Runtime等7类GPU基准，对比Baseline/VFuse/HFuse。
2. 性能收益：GoPTX平均加速11.2%，STMS+LUD最高23%；VFuse均值6.4%，HFuse仅1%；含大量张量同步WMMA场景小幅降速2%。
3. ILP指标：每周期就绪warp(EWPC)平均提升5.5%，STMS/LUD提升50%；HFuse反而降低14.4%。
4. 硬件利用率：指令发射单元ISU提升4%，DRAM利用率提升6.5%，占用率小幅上涨。
5. 消融实验：CFG合并单独提速9.7%；分块+交织叠加额外提升2.1%，自适应阈值优于所有固定分块方案。

## 研究启发
1. 源码粗粒度融合存在并行天花板，PTX中间层可实现指令级穿插，从根源消除记分板停顿。
2. 内核融合不能忽略同步屏障，虚块填充是解决跨分支死锁的低成本有效手段。
3. 长短基本块失衡会大幅限制交织收益，自适应周期分块能均衡调度空间。
4. 内核间计算资源互补程度决定优化上限，同类型ALU资源易引发竞争、收益衰减。
5. 融合优化需兼顾寄存器压力，动态调整寄存器上限可平衡ILP与硬件占用率。