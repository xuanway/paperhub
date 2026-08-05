---
title: "GEM: GPU-Accelerated Emulator-Inspired RTL Simulation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# GEM: GPU-Accelerated Emulator-Inspired RTL Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://d1qx31qr3h6wln.cloudfront.net/publications/GEM.pdf">https://d1qx31qr3h6wln.cloudfront.net/publications/GEM.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> GPU加速RTL仿真，虚拟VLIW架构，仿真映射流程，布尔处理器 </p>
</div>


---

## 研究概要
本文提出仿真器GEM，借鉴FPGA编译流程设计GPU虚拟VLIW布尔处理器，构建完整RTL映射流水线。提出回旋执行层、多阶段划分、时序比特放置等算法，解决SIMT线程分叉、非规整访存痛点。在RISC-V、AI加速器等测试，相较商用仿真器平均提速9.15倍，最高加速64倍，方案开源。

## 背景和动机
1. 大规模RTL验证迭代周期漫长，多核CPU仿真并行度存在天花板，Verilator等工具随电路规模性能下滑明显。
2. FPGA原型仿真速度高，但硬件采购、编译成本极高，中小团队难以负担。
3. 现有GPU仿真多基于门级LUT查表，层级过低速度慢；直接转CUDA易产生大量线程分叉、全局零散访存，GPU利用率极低。
4. 电路逻辑深度长尾分布，传统分层仿真频繁同步、层间置换，带来巨大同步开销。
5. 传统并行划分工具细粒度拆分后逻辑复制开销暴增，无法充分利用GPU海量线程块资源。

## 相关工作
1. 事件驱动CPU仿真（Verilator）：仅利用多核并行，大电路扩展性差，高活性电路仿真速度低。
2. FPGA硬件仿真：性能最优，但设备昂贵、编译耗时数天，复用灵活性差。
3. 门级GPU仿真GL0AM：依赖LUT查表，仅门级运行，相比RTL抽象层速度差距巨大。
4. 直接RTL转CUDA方案：电路异构逻辑引发严重线程分叉，访存零散，GPU算力浪费。
5. RepCut并行划分：单阶段拆分复制成本高，无法适配GPU数百线程块的细粒度需求。

## 本文解决方案
### 1 虚拟VLIW布尔处理器架构
以线程块为基础单元，设计回旋执行层，单次可处理14层长尾逻辑，大幅减少同步置换；全部运算置于共享内存，规避全局非规整访存，支持字级并行位运算。
### 2 E-AIG扩展AIG综合流水线
基于Yosys+ASIC综合工具，原生支持RAM、触发器单元，优化逻辑深度；专用RAM映射减少触发器阵列替代带来的额外逻辑。
### 3 多阶段宽度约束划分
改进RepCut，引入多级切割降低逻辑复制开销；划分后合并过小区块，保证每块位利用率≥50%，适配GPU线程块8192位容量上限。
### 4 时序驱动迭代比特放置
优先映射时序关键路径逻辑，迭代填充回旋层，最小整体层数，降低循环同步次数。
### 5 FPGA式比特流编译+CUDA解释器
生成变长VLIW指令，全局读取采用合并访存；借助协同组实现周期级设备同步，完整RTL-to-GEM编译运行链路。

## 实验分析
1. 实验环境：Xeon CPU、A100/RTX3090 GPU；测试NVDLA、RocketChip、Gemmini、OpenPiton多类开源SoC。
2. 加速性能：相对商用仿真器平均提速9.15倍，8线程Verilator提速5.98倍，NVDLA最高达64倍加速。
3. 资源开销：数百万门电路比特流仅数十至百MB，低端GPU即可承载；OpenPiton8超大规模电路稳定运行。
4. 消融对比：回旋层将同步置换次数降低5倍；多阶段划分把复制开销从200%降至3%以内。
5. 硬件差异：A10性能优于3090，超大多核心电路差距明显，中小设计二者差距较小。

## 研究启发
1. GPU RTL仿真不能直接翻译代码，借鉴FPGA软硬件分层思想设计专用虚拟处理器可从根源解决SIMT不匹配问题。
2. 电路长尾逻辑是传统分层仿真瓶颈，多层合并回旋执行架构能显著削减同步开销。
3. 并行划分不能单一阶段切割，多阶段拆分是GPU细粒度并行的关键，平衡复制与同步成本。
4. 共享内存承载局部逻辑可消除零散全局访存，是提升GPU硬件利用率核心手段。
5. 低成本通用GPU可替代高价FPGA原型，开源框架能降低中小团队验证硬件门槛。