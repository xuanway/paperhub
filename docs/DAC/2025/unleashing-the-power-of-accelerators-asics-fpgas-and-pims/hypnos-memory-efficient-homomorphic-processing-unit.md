---
title: "Hypnos: Memory Efficient Homomorphic Processing Unit"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Hypnos: Memory Efficient Homomorphic Processing Unit

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132418">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132418</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 全同态加密，FPGA 加速器，内存管理，片上异构架构</p>
</div>


---

## 研究概要
本文提出Hypnos内存高效全同态加密处理单元，采用ARM+FPGA异构架构，设计基于RNS分片的同态分页内存管理单元HEPMU，解决传统加速器PCIe传输开销大、内存碎片严重问题。FPGA原型测试下，相较ASIC提速2.58倍、FPGA基线提速4.43倍，通信量缩减3.78倍，能效大幅提升。

## 背景和动机
1. FHE密文膨胀上万倍，传统Host+加速器架构依赖PCIe传输，数据密集场景下PCIe耗时占比超96%，成为系统核心瓶颈。
2. 现有F加速器默认全部密文存放片上，忽略板载内存容量限制带来的频繁主机交互开销。
3. 基于RNS的CKKS类方案运算中密文分片数量动态变化，固定粒度内存管理产生大量碎片，内存利用率低、换页频繁。
4. ASIC加速器片上存储大但开发迭代慢，FPGA方案成本灵活却缺少配套内存管理优化。

## 相关工作
1. ASIC类FHE加速器（ARK、CraterLake、Sharp）：侧重算力与片上缓存，大容量片上存储缓解访存，但未优化主机PCIe交互与动态密文内存碎片。
2. FPGA类FHE加速器（Poseidon、FAB）：优化NTT等底层算子，采用固定整块密文内存管理，内存碎片化严重，跨板传输开销巨大。
3. 通用内存感知FHE设计：仅优化片内缓存调度，未针对RNS动态分片特性设计硬件分页管理机制，无法削减主机PCIe流量。

## 本文解决方案
### 1. ARM+FPGA异构整体架构
FPGA片内集成Cortex-A72处理器，密文/密钥可直连本地DDR处理，绕过主机中转，大幅降低PCIe传输频次；片上NoC互联CPU、计算单元CU、内存管理模块。
### 2. 分层FHE计算单元CU
封装6类高层同态算子，内部级联NTT、模乘等基础运算，64路并行处理，自带私有缓存减少片外访存；配套多发射控制器调度命令。
### 3. 核心HEPMU硬件分页管理单元
以RNS分片为最小粒度管理密文与密钥，内置PMFSM状态机、ID地址映射表、LR换页单元；区分密钥表KT/密文表CT，动态分配分片存储空间，消除大块内存碎片。
### 4. 软硬件协同分页流程
CPU侧编译生成算子指令，仅传递变量ID；CU侧硬件完成分片加载、计算、回写，仅运算结果通过PCIe同步主机，传输数据量大幅压缩。

## 实验分析
1. 测试平台：乾坤XCVP1502 FPGA卡，对比ARK、CraterLake等ASIC与Poseidon、FAB等FPGA方案，基准含ResNet-20、LR-Train、PSI、PIR。
2. 性能收益：数据密集型任务相比ASIC提速2.58×、FPGA基线提速4.43×；PCIe通信总量降低3.78倍，内存换页次数减少50%以上。
3. 能效表现：ResNet场景EDP相比CraterLake提升27.6倍，相比Poseidon提升19.06倍；算力密集LR-Train仍优于同类型FPGA。
4. 内存优化：RNS细粒度管理大幅提升内存利用率，各层PCI传输量平均下降73.55%；16GB板载内存优化收益趋于饱和。
5. 硬件开销：PL区域占用50% LUT、67.07% DSP，ARM硬核不消耗可编程逻辑资源。

## 研究启发
1. FHE加速瓶颈不在单纯算力，主机-加速器PCIe跨板传输与动态密文内存碎片是两大关键优化靶点。
2. 异构片上CPU直连本地存储架构，可省去主机中转密文的冗余传输，从架构层面削减总线压力。
3. 针对RNS动态分片特性设计硬件级分页管理，细粒度调度能显著提升内存利用率、减少换页与IO流量。
4. FPGA相比ASIC具备低成本迭代优势，配套专用内存管理硬件可抹平纯算力差距，整体系统性能反超ASIC。
5. 同态加速器不能仅优化底层NTT算子，必须配套软硬件协同内存管理体系才能释放算力增益。