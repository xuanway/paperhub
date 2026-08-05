---
title: "Fast End-to-End Simulation and Exploration of Many-Core Baseband Transceivers for Software-Defined Radio-Access Networks"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Fast End-to-End Simulation and Exploration of Many-Core Baseband Transceivers for Software-Defined Radio-Access Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS2: Design of Cyber-Physical Systems and IoT</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2508.06141">https://arxiv.org/abs/2508.06141</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://pulp-platform.org/docs/dac2025/Marco_Bertuletti_FastSimulationAndExplorationOfManyRISCVCoreBasebandTransceiversForSDRadioAccessNetworks_DAC25.pdf">https://pulp-platform.org/docs/dac2025/Marco_Bertuletti_FastSimulationAndExplorationOfManyRISCVCoreBasebandTransceiversForSDRadioAccessNetworks_DAC25.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> RISC-V，软件定义无线电，5G，6G，静态二进制翻译</p>
</div>


---

## 研究概要
本文提出基于静态二进制翻译(SBT)的Banshee仿真框架，面向1024核RISC-V TeraPool软件无线电基带芯片，耦合无线信道模型实现端到端5G/6G MIMO MMSE仿真。相比RTL仿真提速千倍，多线程并行最高121倍加速；内置近似时序模型，周期预估平均误差30%，支持低精度算术架构空间快速探索。

## 背景和动机
1. 5G/6G大规模MIMO基带计算负载激增，可编程RISC-V众核SDR成为主流，但RTL/SystemC仿真速度极慢，蒙特卡洛迭代耗时数十小时，设计迭代效率极低。
2. FPGA/ASIC原型仅能后期验证，无法在架构早期完成大规模参数遍历与精度折中探索。
3. 现有仿真工具缺少RISC-V专用浮点/SIMD扩展完整支持，难以评估低精度DSP扩展的BER与时延权衡。
4. 基带仿真需联合无线信道完成端到端BER测试，现有软硬件仿真链路割裂，缺少一体化协同仿真方案。
5. 众核存储、互联竞争带来 stall 开销，传统指令计数法无法准确预估硬件真实周期。

## 相关工作
1. RTL仿真工具(QuestaSim/Verilator)：周期精确但单线程运行，大规模MIMO仿真耗时十几小时，不适合海量蒙特卡洛实验。
2. SystemC TLM仿真：进程调度开销大，编译周期长，众核分层互联建模繁琐，加速倍数有限。
3. FPGA硬件原型：开发周期长，资源限制无法部署千核集群，仅适合小规模验证。
4. 专用SDR仿真库(Sionna)：仅实现无线信道建模，无RISC众核硬件时序仿真能力。
5. 基础二进制翻译器：仅实现指令功能模拟，无硬件流水线、存储竞争与时序预估模块，不适配基带DSP负载。

## 本文解决方案
### 1 LLVM静态二进制翻译Banshee仿真器
将RISC-V二进制转为LLVM IR，原生支持zfinx/Smallfloat等SDR专用浮点扩展；主机多线程映射硬件核，单指令流并行仿真独立OFDM子载波任务。
### 2 轻量近似时序预估模型
记分板跟踪RAW数据冲突，为各类指令、访存固定基础延迟；统一建模无竞争互联延迟，快速估算整体执行周期，无需精准总线冲突仿真。
### 3 端到端协同仿真链路
前端Python生成MIMO/QAM与AWGN/瑞利信道数据，送入Banshee仿真RISC-V MMSE检测，输出比特流回传Python计算BER，实现一体化蒙特卡洛测试。
### 4 多精度MMSE并行映射方案
基于TeraPool分层瓦片众核架构，将每个子载波MMSE任务分配至独立Snitch核；提供8/16bit多种SIMD浮点实现，数据排布贴合片上高速暂存减少互联竞争。
### 5 批量并行蒙特卡洛优化
批量处理大量OFDM符号，服务器128线程并行执行独立仿真样本，大幅缩短多SNR、多精度遍历总耗时。

## 实验分析
1. 仿真平台：AMD EPYC 128核服务器，对比QuestaSim RTL；被测硬件1024核TeraPool SDR集群，测试4×4~32×32 MIMO MMSE。
2. 仿真速度：4×4单线程仅9.5s，RTL需13h44min；单线程相对RTL最高提速5237倍，128线程并行再提升73~121倍。
3. 时序精度：相比RTL真实周期，框架预估平均误差30%，远优于单纯指令计数估算。
4. 精度折中测试：16bit浮点方案BER接近64bit黄金模型，8bit低精度在高SNR下误码显著恶化。
5. 架构开销拆解：访存与同步阻塞是主要周期损耗，SIMD浮点扩展可大幅降低总指令数与stall。

## 研究启发
1. 面向专用众核DSP的早期探索，二进制翻译仿真是RTL/FPGA之外高效折中方案，兼顾功能正确性与仿真速度。
2. 基带端到端评估必须联合无线信道与硬件时序，仅软件算法仿真无法反映真实接收机BER性能。
3. RISC-V定制SIMD浮点扩展可在几乎无损误码前提下大幅降低计算周期，是SDR众核优化关键方向。
4. 近似时序模型牺牲少量精度换取千倍仿真加速，足以支撑架构早期大规模设计空间遍历。
5. 子载波任务天然无依赖，适合批量多线程并行，可充分利用通用多核服务器算力加速蒙特卡洛实验。
