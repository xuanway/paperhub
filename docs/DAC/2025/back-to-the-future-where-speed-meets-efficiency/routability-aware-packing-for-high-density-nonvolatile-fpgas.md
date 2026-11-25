---
title: "Routability-aware Packing for High-density Nonvolatile FPGAs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Routability-aware Packing for High-density Nonvolatile FPGAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133374">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133374</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 非易失性存储器，多级单元，现场可编程门阵列，计算机辅助设计，打包</p>
</div>

---

## 研究概要
本文面向MLC型非易失FPGA(NVFPGA)提出路由感知重打包优化方案，新增Repair阶段搭配输入等价LUT过滤技术。优化插入VTR打包流程，大幅减少耗时的CLB内部路由校验；多基准测试打包耗时平均降低41.48%，同时小幅提升面积与时序性能。

## 背景和动机
1. MLC NVM提升NVFPGA逻辑密度，但CLB内部连线拥挤、可路由性变差，打包阶段需要频繁调用内部路由校验，耗时是传统SRAM FPGA的8.9倍。
2. 标准VTR打包分为Route-Once与Route-Each两阶段，73.53%CLB在第一阶段无法通过校验，进入逐LUT校验的Route-Each，占用91.16%打包总时长。
3. 大量CLB仅逻辑-物理LUT分配失衡导致不可路由，LUT集合无需改动，直接进入Route-Each造成巨额重复路由开销。
4. MLC架构内同BLE的(k-2)子LUT输入完全等价，重复分配校验存在大量冗余尝试，现有打包算法未利用该结构特性。

## 相关工作
1. SRAM-FPGA打包优化：UTPlaceF、动态重聚类、NN专用打包、并行DP-Pack、GPU加速打包，均未适配MLC NVFPGA高密度布线拥堵问题。
2. MLC NVFPGA专用打包：仅优化路径时延，未解决内部路由频繁调用带来的打包效率暴跌。
3. 通用VTR流程：原生两阶段打包无重分配修复机制，无法调整失败CLB的LUT物理映射，只能逐单元重试。
4. NVM-FPGA架构研究：侧重存储密度、功耗、时延硬件指标，缺少配套CAD打包流程优化。

## 本文解决方案
### 1 路由感知Repair重打包阶段
插入Route-Once失败后、Route-Each之前，分为候选LUT筛选与重分配两步；定义CPI拥堵指标优先选取造成布线拥塞的LUT，基于可用物理单元总量限制候选规模。
### 2 可路由分数RS分配策略
以BLE占用输入三次方求和评估布线拥堵，优先选择RS最小的物理LUT进行映射，均衡CLB内部逻辑分布，降低路由失败概率。
### 3 输入等价LUT去冗余机制
利用MLC子LUT输入一致性，分配失败时标记同BLE内同类单元，后续直接跳过，消除重复路由校验开销。
### 4 轻量化流程集成
Repair阶段路由校验平均仅带来4.15%额外开销，搭配RS与等价过滤后开销再降低54.69%，无需修改VTR顶层调度逻辑。

## 实验分析
1. 实验平台：基于40nm STT-RAM MLC NVFPGA，集成至VTR工具链，对比原生BASE打包算法，测试9组多规模电路基准。
2. 效率提升：Repair单独减少13.39%路由调用；等价过滤减少33.37%；两者结合平均减少41.48%内部路由，打包时间同步下降。
3. 修复覆盖率：平均68.62%失败CLB可通过Repair修复，避免进入耗时Route-Each阶段。
4. 开销与QoR：Repair阶段额外路由开销仅4.15%；整体CLB数量平均减少0.67%，关键路径时延平均缩短1.73%，设计质量无损失。
5. 场景差异：低输入LUT占比高电路优化幅度更大；7-LUT密集电路修复效果有限。

## 研究启发
1. MLC NVFPGA高密度带来布线拥堵，CAD打包瓶颈不再是逻辑聚类，而是频繁的内部路由校验。
2. 多数打包失败源于LUT物理分配失衡，新增轻量重分配修复阶段可大幅规避逐单元重试流程。
3. 硬件架构固有等价资源可用于过滤冗余校验，是低成本提速CAD的通用思路。
4. 优化流程需控制自身额外路由开销，拥堵评分RS可高效引导均衡分配，减少重试次数。
5. 面向新型存储FPGA的EDA优化不能照搬SRAM方案，必须结合NVM/MLC独有硬件结构定制算法。
