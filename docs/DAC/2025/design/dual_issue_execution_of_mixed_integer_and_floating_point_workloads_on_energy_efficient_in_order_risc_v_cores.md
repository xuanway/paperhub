---
title: "Dual-Issue Execution of Mixed Integer and Floating-Point Workloads on Energy-Efficient In-Order RISC-V Cores"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Dual-Issue Execution of Mixed Integer and Floating-Point Workloads on Energy-Efficient In-Order RISC-V Cores


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.20590">https://arxiv.org/abs/2503.20590</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://pulp-platform.org/docs/dac2025/Luca_Colagrande_DAC2025_Presentation.pdf">https://pulp-platform.org/docs/dac2025/Luca_Colagrande_DAC2025_Presentation.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>RISC-V，双发射，能效，通用 </p>
</div>


---

## 研究概要
本文提出COPIFT软硬件协同方法与配套RISC-V ISA扩展，在Snitch顺序RISC-V核上实现整数/浮点混合代码持续双发射，解决原有伪双发射存在指令依赖限制。经蒙特卡洛、 transcendental函数等负载验证，平均加速1.47倍，峰值IPC达1.75，整体能效平均提升1.37倍，硬件面积时序开销可忽略。

## 背景和动机
1. 后登纳德缩放时代能效为核心约束，大规模并行计算偏好小面积顺序单发射RISC-V核，但混合整型浮点负载IPC偏低。
2. Snitch原有FREP伪双发射要求整数、浮点线程无依赖，无法处理存在访存、寄存器交互的混合指令序列，适用场景狭窄。
3. 现有双发射RISC-V核多增加多端口寄存器堆、乱序逻辑，面积功耗暴涨，不适合大规模阵列PE部署。
4. ML、蒙特卡洛等主流负载大量交织整型控制与浮点运算，现有架构难以并行两类指令，算力利用率低。

## 相关工作
1. 乱序/通用顺序双发射RISC：依赖多读写端口寄存器堆、重命名逻辑，硬件面积提升最高60%，能效差。
2. 压缩指令专用双发射：仅支持16位短指令，无法覆盖完整RV32G浮点扩展。
3. Snitch原生FREP机制：仅支持无依赖浮点循环，存在访存、寄存器交互时无法并行执行。
4. 专用分离浮点缓冲处理器：仅适配简单独立循环，不通用混合依赖代码，无系统化解耦编译流程。

## 本文解决方案
### 1. COPIFT七步解耦编译方法论
构建指令数据流图识别三类跨域依赖；图划分切割依赖边；循环分块、裂变、软件流水线；用SSR/ISSR消除浮点访存指令；浮点循环映射FREP，实现整型、浮点阶段并行。
### 2. 定制RISC-V ISA扩展
改造浮点转换、比较指令语义，新增自定义编码，跨寄存器堆交互全部转存内存，彻底解耦整数/浮点寄存器读写依赖。
### 3. 流融合优化
多路一维仿射流合并为高维流，充分利用核内有限SSR硬件，减少流配置开销。
### 4. 多缓冲调度机制
软件流水线配套多级数据缓存，错开整型、浮点阶段读写时序，掩盖块传输延迟。

## 实验分析
1. 实验环境：12LP+工艺Snitch集群，1GHz时序，周期级RTL仿真+后版图功耗分析，负载含蒙特卡洛、exp/log等LLM常用超越函数。
2. IPC性能：几何平均IPC提升1.62，峰值可达1.75，exp核加速最高2.05倍，全负载平均提速1.47倍。
3. 功耗与能效：平均功耗仅提升1.07倍，执行时长缩减幅度更大，整体能效平均提升1.37倍，exp核能效提升1.93倍。
4. 分块特性：块尺寸越大，初始化固定开销摊销越好；存在最优块平衡初始化开销与片上存储容量。
5. 硬件代价：ISA扩展仅带来合成误差范围内可忽略的面积、时序开销，无需改动核心流水线主体。

## 研究启发
1. 无需大幅修改硬件，依靠编译变换+轻量ISA扩展即可在顺序RISC核实现混合指令持续双发射。
2. 整型浮点分离寄存器堆是天然并行基础，核心难点是处理访存、转换类跨域依赖，需编译层解耦。
3. 流寄存器SSR可彻底消除浮点load/store带来的跨线程依赖，是实现并行的关键硬件支撑。
4. 软件流水线+多级缓冲能有效错开两类计算阶段，掩盖块间数据传输开销。
5. 面向大规模PE阵列的低功耗处理器，应优先编译优化而非硬件堆叠多发射逻辑，控制面积功耗开销。