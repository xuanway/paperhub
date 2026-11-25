---
title: "Supporting Register-based Addressing Modes for in-DRAM PIM ISAs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Supporting Register-based Addressing Modes for in-DRAM PIM ISAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132430">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132430</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内处理指令集架构，基于寄存器的寻址模式，DRAM内处理，查找表，代码卸载 </p>
</div>

---

## 研究概要
本文面向DMA型DRAM存内指令集PISA，提出索引、基偏移两种寄存器寻址模式。基偏移复用指令消除重复下发开销，索引寻址依托片上LUT在PIM内完成激活一元运算，减少CPU-PIM数据搬运。Transformer模型测试最高提速1.94倍，硬件仅增加4.65%面积、8.61%功耗。

## 背景和动机
1. 主流DMA式PISA采用绝对地址编码，相同算子更换张量时需重下发全套指令，代码卸载耗时占总执行9.65%。
2. GeLU、Sqrt等一元激活无法在PIM执行，算子间频繁CPU/PIM双向传输，数据搬运开销达35.97%。
3. 传统LUT方案需全表广播，带宽占用高，多任务场景内存冲突严重，无法和PIM并行计算适配。
4. 算子被CPU截断后无法融合，连续PIM计算序列变短，进一步放大数据交换损耗。

## 相关工作
1. Silent-PIM基准架构：基于DMA描述符的绝对寻址PISA，无寄存器动态地址生成，存在大量指令重下发。
2. AIM/HBM-PIM LUT方案：全局广播完整查找表，带宽开销巨大，或依赖片上RISC核低速计算一元函数。
3. 通用DRAM PIM：仅支持矩阵乘、逐元素二元运算，无原生一元算子加速能力，激活全部移交CPU。
4. 传统CPU寄存器寻址：成熟但未移植到DMA驱动的存内指令体系，缺少DRAM适配的硬件扩展。

## 本文解决方案
### 1 扩展双寄存器寻址硬件
在PIM接口单元PIU增加3组参数寄存器Rargs、累加寄存器RvACC，扩展指令2bit寻址模式标识位，支持绝对/索引/基偏移三类有效地址生成。
### 2 基偏移寻址模式
指令仅存储张量偏移，运行时通过Rargs载入基地址拼接有效地址；相同尺寸算子可复用PIM指令，彻底消除重复代码卸载。
### 3 索引寻址LUT加速一元运算
LUT基地址存入Rargs，PIM中间计算结果RvACC作为表内偏移，单次仅读取单LUT条目，无需全表广播，原生支持SiLU、Log等激活。
### 4 长序列算子融合优化
PIM原生支持一元运算后，编译器可合并前后二元计算，减少中间张量内存溢出，进一步削减跨设备传输。

## 实验分析
1. 实验平台：65nm工艺综合，FPGA全系统仿真，测试BERT/RoBERTa/T5/GPT-2四类Transformer。
2. 性能收益：相比原始PISA最高提速1.94倍；基偏移消除指令卸载，索引寻址降低3.52%~43.36%数据搬运开销。
3. 一元算子加速：LUT方案相较CPU平均提速3.58，SwishGLU等大激活最高7.19倍。
4. 多任务鲁棒：传统全广播LUT内存密集负载延时上涨48.66%，本文方案仅22.99%。
5. 硬件代价：PI新增寻址逻辑仅增加4.65%芯片面积、8.61%整体功耗，开销可控。

## 研究启发
1. DMA型PIM指令瓶颈不在计算，而静态绝对地址带来重复指令下发，寄存器动态寻址是低成本优化路径。
2. DRAM大容量天然适配LUT，但必须按需单点读取，全局广播会造成严重带宽冲突。
3. 扩展PIM算子支持不能仅靠新增运算单元，寻址机制改造可直接补齐激活等缺失运算。
4. 硬件寻址扩展可打通算子融合壁垒，从算法层减少CPU-PIM交互，形成软硬件协同收益。
5. 面向大模型PIM设计，需兼顾指令下发、数据传输两大隐性开销，二者叠加会大幅抵消存内带宽优势。
