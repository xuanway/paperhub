---
title: "HH-PIM: Dynamic Optimization of Power and Performance with Heterogeneous-Hybrid PIM for Edge AI Devices"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# HH-PIM: Dynamic Optimization of Power and Performance with Heterogeneous-Hybrid PIM for Edge AI Devices


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.01468">https://arxiv.org/abs/2504.01468</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 异构混合存内处理，动态数据放置优化，能效优化，边缘AI设备，MRAM-SRAM混合架构</p>
</div>

---

## 研究概要
本文提出HH-PIM异构混合存内计算架构，分为高性能HP与低功耗LP两类MRAM-SRAM混合PIM簇。设计动态DP数据放置算法，在时延约束下最小推理能耗。基于RISC-V处理器与FPGA原型验证，相比传统PIM平均节能60.43%，适配各类动态边缘AI负载。

## 背景和动机
1. 边缘AI设备算力波动大，传统单一PIM固定算力，高负载卡顿、低负载空耗严重，能效失衡。
2. 纯SRAM/DRAM PIM漏电、刷新功耗高；单一NVM PIM读写延迟大，标准混合PIM权重仅固定存MRAM，峰值时延不达标。
3. DVFS电源调控在边缘SoC设计复杂度高，而大小核异构思路未落地存内计算场景。
4. 现有混合PIM数据划分静态，无法随实时推理负载动态调整权重存储位置，资源利用率低。

## 相关工作
1. 纯易失PIM（SRAM/DRAM）：算力稳定但持续静态功耗高，不适合长待机边缘设备。
2. 单一NVM PIM（MRAM/ReRAM）：权重存储省电，但读写延迟高，峰值推理时延难以满足实时需求。
3. 传统Hybrid-PIM：MRAM存权重、SRAM仅做缓存，静态分配，高负载下SRAM算力无法复用权重。
4. 异构多核CPU（big.LITTLE）：仅通用处理器动态调度，未结合存内存储与PE协同优化。

## 本文解决方案
### 1 双簇异构混合PIM硬件架构
分为HP（1.2V高速MRAM+SRAM）、LP（0.8V低功耗MRAM+SRAM）两大PIM簇，各配独立控制器；支持权重动态存入SRAM，提升峰值推理速度。
### 2 分层专用PIM控制器
内置状态机、指令译码、数据分配器，带重排缓冲解决HP/LP跨簇数据速度差，区分命令/存储双接口并行传输。
### 3 动态规划数据放置优化
将权重分配建模为多选择背包问题，采用自底向上DP求解；分HP/LP独立建表合并最优解，离线生成查找表，运行快速分配。
### 4 分时片动态调度机制
按固定时间片采集负载，基于时延约束动态切换权重存储介质，低负载大量使用LP-MRAM并门控闲置存储降低静态功耗。

## 实验分析
1. 实验平台：45nm工艺综合、Kintex-7 FPGA原型，RISC-V Rocket处理器；对比基线PIM、纯异构PIM、传统混合PIM；测试EfficientNet/MobileNetV2/ResNet18三类TinyML，6种动态负载场景。
2. 硬件规格：HH-PIM含4HP+4LP模块，每模块64kB MRAM+64kB SRAM；HP读写、PE延迟远低于LP，但功耗显著更高。
3. 能效收益：全场景平均节能60.43%；轻负载场景最高节能86.23，持续高负载仍可节能41.46%。
4. 时延表现：高负载时权重存入HP-SRAM，推理时延相比仅MRAM存储缩短30%以上，满足实时边缘要求。
5. 消融对比：异构硬件+动态分配二者缺一，单独混合存储或单一异构簇节能幅度不足30%。

## 研究启发
1. 边缘PIM不能采用统一算力单元，HP/LP异构簇可天然匹配波动AI负载，替代复杂DVFS电路。
2. MRAM与SRAM不能固定分工，高负载复用SRAM存储权重是解决混合PIM峰值时延短板关键。
3. 权重分配属于NP难组合优化，离线DP预生成LUT可大幅降低运行时调度开销。
4. 跨P簇存在读写速度差，控制器增设数据重排缓冲可避免数据冲突、保障流水线连续。
5. 低负载场景通过电源门控闲置存储介质，可大幅削减MRAM/SRAM静态漏电功耗。
