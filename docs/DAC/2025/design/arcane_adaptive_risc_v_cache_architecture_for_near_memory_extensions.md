---
title: "ARCANE: Adaptive RISC-V Cache Architecture for Near-memory Extensions"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ARCANE: Adaptive RISC-V Cache Architecture for Near-memory Extensions

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.02533">https://arxiv.org/abs/2504.02533</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>缓存内计算，自定义ISA扩展，RISC-V，边缘计算 </p>
</div>

---

## 研究概要
本文提出ARCANE自适应RISC-V近存缓存架构，可直接替换MCU末级缓存，兼具存储与协处理功能。基于CV-X-IF协处理器接口实现自定义矩阵指令卸载，配套缓存运行时管理冲突与DMA搬运。65nm工艺综合，8bit卷积相比标准CPU最高提速84倍，最大面积开销仅41.3%。

## 背景和动机
1. 冯诺依曼存储墙导致边缘AI数据搬运开销巨大，存内/近存计算可缓解，但现有方案编程门槛高、软件同步复杂，难以集成现有MCU。
2. 传统SIMD RISC-V内核处理CNN等矩阵任务时，频繁内存读写限制吞吐，专用CIM硬件指令固化、扩展性差。
3. 现有近存架构缺少统一RISC-V扩展接口，程序员需手动管理缓存分片、数据布局与读写冲突，开发成本高。
4. 多数近存加速器仅支持固定运算，无法灵活新增卷积、池化等自定义神经网络内核，适配性不足。

## 相关工作
1. SRAM存内计算（BLADE等）：在位线内置运算单元，吞吐有限，指令集固化，难以扩展复杂矩阵算子。
2. 商用近存计算（Intel CNC）：仅支持基础MAC运算，无软件抽象层，编程复杂，不兼容通用RISC-V生态。
3. RISC-V SIMD内核（CV32E40PX）：依赖反复内存加载，大规模矩阵任务加速上限低，无法复用缓存本地数据。
4. NM-Carus基础近存IP：提供底层向量硬件，但缺少完整缓存管控、指令卸载与冲突规避整套系统。

## 本文解决方案
### 1. 可替换一体化LLC硬件架构
作为X-HEEP MCU可直插式末级缓存，内置多组VPU向量单元与CV32E40X嵌入式eCPU；采用全相联缓存，缓存行匹配向量长度，配套锁机制、地址表AT解决RAW/WAW/WAR冲突。
### 2. CV-X-IF指令卸载桥接模块
复用标准RISC-V协处理器接口，主机下发xmnmc自定义矩阵指令，桥产生中断交由eCPU软件解码，主机可乱序执行，同步逻辑硬件自动完成。
### 3. xmnmc分层可扩展ISA
设计xmr矩阵预留、xmk内核两类指令，延迟绑定地址而非即时加载；内置卷积、池化、GEMM等算子，支持编译时新增自定义内核，对上层软件屏蔽缓存细节。
### 4. C-RT缓存运行时系统
含内核解码器、调度器、矩阵分配器，静态内存无碎片；内置2D DMA搬运，自动管理缓存占用、脏写回与多VPU负载均衡，硬件地址表规避读写冲突。

## 实验分析
1. 实现平台：65nm LP工艺，250MHz，128KB缓存分4个VPU，对比原生CV32E40X、CV32E40PX SIMD内核。
2. 面积开销：2/4/8通路配置面积增幅21.7%/28.3%/41.3%，运算逻辑占额外面积主体，控制逻辑占比不足4%。
3. 性能收益：8bit 256×256三通道卷积相比标量CPU提速30~84倍，远超专用SIMD内核；峰值吞吐17GOPS，面积效率优于BLADE。
4. 阶段开销：小矩阵预处理开销高，大计算场景计算阶段占主导，各类非计算阶段总开销收敛至20%以内。
5. 扩展性：相比Intel CNC支持更多神经网络算子，无需重新流片即可软件新增内核，适配tinyML各类边缘推理任务。

## 研究启发
1. 近存计算落地关键是软硬件协同抽象，通过RISC-V扩展指令屏蔽底层缓存、VPU、数据分片细节降低编程门槛。
2 将缓存改造为一体化协处理器，可复用片上存储带宽，规避CPU反复搬移中间特征，大幅提升矩阵类任务吞吐。
3 分层ISA设计（上层矩阵指令+底层向量硬件）兼顾可编程灵活性与硬件并行效率，平衡扩展性与性能。
4 缓存锁、地址表、运行时调度联合可自动消除读写冲突，无需程序员手动同步，降低集成成本。
5 边缘MCU场景下适度面积开销换取大规模AI推理百倍加速，是兼顾成本与能效的可行硬件路线。
