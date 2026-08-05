---
title: "Data Oblivious CPU: Micro-architectural Side-channel Leakage-Resilient Processor"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "side-channel"
  - "risc-v"
  - "microarchitecture"
  - "data-oblivious"
  - "secure-processor"
---

# Data Oblivious CPU: Micro-architectural Side-channel Leakage-Resilient Processor

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133149">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133149</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 微架构侧信道攻击，信息流跟踪</p>
</div>

---

## 研究概要
本文提出Data Oblivious CPU安全处理器架构，基于RISC-V BOOM乱序核实现数据感知动态指令译码。通过页表敏感标记、硬件污点追踪、安全/性能双指令通路，敏感数据执行时旁路缓存、分支预测等微架构单元。FPGA实现仅增加2%硬件资源，无敏感程序性能开销为0，安全负载最高仅25%延时损失，可抵御各类微架构侧信道攻击。

## 背景和动机
1. 现代CPU缓存、分支预测等优化单元易泄露时序信息，触发Flush+Reload、Spectre等微架构侧信道攻击，窃取密钥等敏感数据。
2. 现有防护方案仅针对单一攻击类型，通用性差，或全系统强制安全执行，带来巨大全局性能损耗。
3. 缺乏分层软硬件协同方案，无法区分敏感/普通数据流，不能按需关闭泄露类微架构组件。
4. 传统信息流追踪存在过度污点、流水线恢复缺陷，上下文切换时敏感状态易丢失，防护完整性不足。
5. 现有安全处理器修改量大、硬件面积开销高，难以兼容标准RISC-V生态，工程落地难度大。

## 相关工作
1. 单一攻击专用防护：针对缓存/瞬态执行单独加固，只能抵御一类侧信道，无法形成通用防护。
2. 软件级信息流防护：静态插桩、编译变换，依赖开发者，微架构行为不可控，整体性能损耗严重。
3. 硬件污点追踪方案：全局标记所有IO数据，过度污点导致流水线阻塞，开销极高，且仅防护内存层级泄露。
4. ISA扩展类数据遗忘处理器：新增专用指令，程序修改成本高，出错难以调试，占用额外内存存储元数据。
5. RISC-V专用缓存防护硬件：仅屏蔽缓存侧信道，未覆盖分支预测、乱序执行等其他泄露源。

## 本文解决方案
### 1 敏感内存页标记机制
复用RISC-V sv39页表保留位作为敏感S标记，编译器注解机密数据，操作系统将其映射至标记页面，快速区分敏感存储区域。
### 2 全流水线硬件污点追踪
每个物理寄存器增加污点位，加载/运算自动传播污点；立即数、非敏感写操作可清除污点；新增CSR寄存器保存上下文切换污点状态，分支预测错误时回滚污点信息。
### 3 双模式动态指令译码
译码器根据操作数污点状态动态选择通路：普通指令启用缓存、BTB等高性能单元；敏感指令强制顺序执行，旁路缓存、清空分支预测组件消除时序痕迹。
### 4 全类型数据无关安全指令集
算术、访存、分支指令均提供恒定时序安全版本，敏感访存绕过Cache，敏感跳转不更新BTB/RSB，彻底消除微架构痕迹。
### 5 完整软硬件协同栈
应用注解关键字、编译器分配安全段、内核模块管理页表S位，硬件扩展TLB/寄存器/流水线模块，软硬件联动完成全链路敏感数据隔离。

## 实验分析
1. 实验平台：Xilinx KCU105 FPGA，基于Chisel改造RISC-V BOOM处理器，测试SPEC2017与OpenSSL、NGINX等安全应用。
2. 硬件开销：综合后FPGA总资源仅增加1.16%，各类LUT、寄存器增减幅度均低于3%，硬件改动极小。
3. 性能表现：无敏感标注程序无任何性能损失；加密、密钥类安全应用开销1.33%~25.63%，NGINX压力测试仅5.08%时延上涨。
4. 安全验证：缓存时序侧信道攻击下，原始CPU命中/缺失周期区分明显，改造后时序完全重合，主流微架构攻击均无法提取机密信息。
5. 兼容性：完全标准RISC-V指令集兼容，无需大幅修改程序，仅增加敏感数据注解即可启用防护。

## 研究启发
1. 统一全系统防护代价过高，数据感知选择性隔离是平衡安全与性能的核心思路，仅敏感数据流限制微架构优化。
2. 页表预留位、硬件污点追踪可低成本实现敏感数据全生命周期标记，无需大幅修改处理器流水线主体。
3 缓存、分支预测是主要泄露源，敏感指令强制顺序执行并清空预测组件，可通用抵御各类时序侧信道。
4. 安全处理器需软硬件协同设计，注解、编译器、内核、硬件四层联动才能降低改造与使用成本。
5. 轻量级硬件扩展（资源增量<2%）即可实现通用侧信道防御，具备嵌入式、服务器RISC芯片落地价值。


## 相关资源

- **RISC-V BOOM**：[https://github.com/riscv-boom/riscv-boom](https://github.com/riscv-boom/riscv-boom)
- **信息流追踪在硬件安全中的应用**：Hu et al., "Hardware Information Flow Tracking" (ACM Computing Surveys, 2021)
- **微架构侧信道综述**：Ge et al., "A Survey of Microarchitectural Timing Attacks and Countermeasures" (ACM Computing Surveys, 2018)
- **Data-Oblivious 算法**：Goldreich & Ostrovsky, "Software Protection and Simulation on Oblivious RAMs" (JACM 1996)
