---
title: "Gem5-AcceSys: Enabling System-Level Exploration of Standard Interconnects for Novel Accelerators"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Gem5-AcceSys: Enabling System-Level Exploration of Standard Interconnects for Novel Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.12273">https://arxiv.org/abs/2502.12273</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 内存层次结构，PCIe，互连，硬件加速器，系统级仿真 </p>
</div>


---

## 研究概要
本文基于Gem5扩展Gem5-AcceSys系统仿真框架，原生集成PCIe、SMMU、DMA与异构内存架构，支持RTL/C++两类加速器建模。以Transformer矩阵脉动加速器为测试载体，量化PCIe带宽、包长、主/设备内存对性能影响，给出GEMM/非GEMM workload架构选型阈值，为异构加速器协同设计提供量化依据。

## 背景和动机
1. 现有Gem5衍生仿真器仅简易总线模型，不支持PCIe标准高速互连，无法真实模拟AI加速器主机-设备数据交互开销。
2. 缺少SMMU地址翻译、多通道DMA、片上设备内存等工业级组件，虚拟地址转换、批量数据搬运延迟无法精准建模。
3. DDR5/HBM/GDDR6多类异构内存缺少统一接入接口，难以对比主存与设备内存的性能差异。
4. Transformer workload包含大量GEM与零散非GEM运算，两类任务内存瓶颈不同，现有工具无法拆分剖析系统瓶颈。
5. 缺乏量化模型指导架构取舍，设计师难以权衡PCIe带宽成本与设备内存硬件开销。

## 相关工作
1. Gem5-Aladdin：仅基础总线，无PCI/SMMU，仅C++抽象加速器，不支持RTL。
2. Gem5-Salam：LLVM级加速器建模，缺少高速互连与地址翻译单元。
3. Gem5-RTL：可导入RTL，但互连模型简陋，仿真开销巨大，无设备内存模块。
4. Gem5-X：支持众核与简易设备内存，缺失PCIe、DMA、SMMU完整链路。
5. 通用DRAM仿真器（Ramulator/DRAMsim3）：仅内存时序仿真，无法和CPU-加速器全系统联动。

## 本文解决方案
### 1 Gem5全系统扩展架构
新增PCIe完整链路（RC/PHY/Switch）、SMMU地址转换、多通道DMA模块；设计加速器封装层，兼容Verilator转译RTL与C++抽象两种加速器实现。
### 2 三层可配置内存子系统
支持主机缓存直访、绕过缓存直存、设备本地内存三种访问模式；对接Ramulator/DRAMsim3，兼容DDR4/5、GDDR6、HBM2多类存储。
### 3 完整互连仿真流水线
可调PCIe通道数、速率、数据包长度，精准建模传输延迟与流水线停顿；区分虚拟地址页表遍历开销，量化大矩阵地址转换损耗。
### 4 分拆Workload性能评估模型
将Transformer运算拆分为GEMM矩阵计算与Non-GEMM零散操作，分别建立性能表达式，推导设备内存适用 workload占比阈值。
### 5 多维度设计空间扫描工具
自动遍历PCI带宽、内存类型、内存位置、数据包尺寸参数，输出roofline性能边界与归一化对比指标。

## 实验分析
1. 实验环境：ARM 1GHz CPU，MatrixFlow 16×16脉动加速器，ViT base/large/huT模型，DDR/GDDR/HBM多内存对比。
2. PCIe参数结论：最优数据包长256B；带宽提升性能收益存在天花板，进入计算瓶颈后增益消失；高带宽PCIe可达到设备内存80%性能。
3. 内存对比：设备内存对纯GEMM加速显著，但Non-GEMM任务NUMA延迟会造成最高500%耗时增长。
4. 瓶颈规律：系统性能对带宽敏感度远高于访问延迟，带宽优化可降61.9%耗时，延迟仅增加4.9%开销。
5. 选型阈值：PCIe 2GB/s场景GEMM占比>34.31%选设备内存；64GB/s高带宽PCIe仅需>4.27%即可选用设备内存。

## 研究启发
1. AI加速器全系统仿真必须完整建模PCIe、SMMU、DMA等真实接口，简化总线会大幅低估数据搬运瓶颈。
2. 不能单一判定设备内存更优，架构选型由GEMM与零散运算的占比决定，需按业务负载权衡硬件成本。
3. PCIe数据包长度存在最优值，过小/过大均会引发流水线停顿，是互连优化低成本切入点。
4. 大尺寸矩阵场景地址翻译开销不可忽略，大规模AI模型需配套TLB优化降低页表遍历延迟。
5. 全系统仿真框架需兼容多种DRAM后端，才能精准评估新一代高带宽存储带来的系统收益。
