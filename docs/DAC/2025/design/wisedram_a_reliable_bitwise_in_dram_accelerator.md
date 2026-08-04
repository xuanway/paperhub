---
title: "WISEDRAM: A Reliable Bitwise In-DRAM Accelerator"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# WISEDRAM: A Reliable Bitwise In-DRAM Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133397">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133397</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 动态随机存取存储器，存内处理，按位运算，内存墙</p>
</div>


---

## 研究概要
本文提出WISEDRAM基于DRAM原位按位加速器，新增一行X专用单元，完全保留标准DRAM读写时序。依托可控差分位线实现XOR/AND/OR等全部按位运算，仅需3个DRAM周期。16nm HSPICE仿真显示，相比主流Ambit、ROC等方案，按位平均延迟降低22%，XOR提速71%，工艺鲁棒性提升77%，面积开销仅1.6%。

## 背景和动机
1. 存储墙问题严重，CPU/GPU与DRAM间数据搬运时延、功耗极高，图神经网络、二进制推理等海量按位任务性能受限。
2. DRAM原生大容量、高并行度适合存内计算，但传统模拟PIM依赖多单元电荷共享，易受工艺偏差、噪声干扰，容错差。
3. 现有半数字DRAM-PIM需改造灵敏放大器、引入二极管压降，运算故障多，且运算周期冗长。
4. 多数方案改动DRAM核心读写通路，与商用DDR工艺兼容性差，芯片改造成本高、良率损失大。

## 相关工作
1. 模拟类DRAM-PIM（Ambit）：多行同时激活电荷共享实现多数逻辑，信号幅值小，工艺波动下故障率高，需多次数据拷贝。
2. ROC架构：依靠二极管实现逻辑，存在阈值压降，运算可靠性大幅下降，周期数多。
3. ELP2IM：修改预充与灵敏放大器电路，破坏标准DRAM访问时序，额外自定义操作增加延迟。
4. PIPF-DRAM：无预充机制，需定制存储结构，通用性弱，对工艺参数敏感。

## 本文解决方案
### 1 X-Cell专用单元硬件扩展
每个MAT增加一行双接触X单元，内置M3-M6控制管，通过XCL/XCR信号选择左右位线，仅新增少量控制信号线，不修改灵敏放大器与译码器。
### 2 三周期统一按位运算流水线
所有二元按运算（XOR/XNOR/AND/NAND/OR/NOR）统一采用「拷贝操作数→读取控制位→X单元生成结果写入」三步AAP/AP原语，达到理论最小周期。
### 3 受控差分位线逻辑机制
利用灵敏放大器天然互补电平，X单元根据B值选择传输原A或取反A，无需全局电荷叠加，规避模拟噪声缺陷。
### 4 兼容标准DRAM架构
读写、预充、刷新流程完全复用商用DDR5规范，支持RowClone批量拷贝，可无缝扩展到位串行乘加通用计算。

## 实验分析
1. 仿真平台：16nm PTM-MG工艺HSPICE，MAT尺寸512×512，工艺偏差σ=2.5%~15%蒙特卡洛仿真。
2. 时延性能：XOR运算仅149ns，相较ROC提速71%，全部按位操作平均延迟降低22%。
3. 能耗表现：单比特XOR功耗595fJ，搭配PF-DRAM无预充结构能效进一步提升。
4. 鲁棒性：σ=15高工艺偏差下几乎无运算故障，相比最优PIPF-DRAM鲁棒性提升77%。
5. 硬件开销：仅增加一行X单元，整体阵列面积开销1.6%，布局改造代价极低。

## 研究启发
1. DRAM存内计算无需改动灵敏放大器等核心模拟电路，仅增加少量专用单元即可兼顾兼容性与可靠性。
2. 模拟电荷共享天然缺陷难以根治，基于差分灵敏放大器的半数字方案鲁棒性优势显著。
3. 统一三周期运算流水线可标准化各类按位操作，降低控制逻辑复杂度，适配二进制神经网络、向量检索等负载。
4. 存内加速器设计优先复用成熟DRAM时序，能大幅降低流片与商用落地门槛。
5. 工艺鲁棒性是DRAM-PIM落地关键，依赖二极管、多单元电荷叠加的架构难以大规模量产。
