---
title: "Configurable DSP-Based CAM Architecture for Data-Intensive Applications on FPGAs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Configurable DSP-Based CAM Architecture for Data-Intensive Applications on FPGAs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ddiwu.com/assets/pdf/CAMpaper.pdf">https://ddiwu.com/assets/pdf/CAMpaper.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 内容可寻址存储器，数字信号处理器，现场可编程门阵列，可扩展性，高性能</p>
</div>


---


## 研究概要
面向FPGA上数据密集型应用，现有LUT/BRAM型CAM存在资源开销大、扩展性差、不支持多并发查询等缺陷。本文提出基于DSP块的可配置CAM分层架构，单元级支持多查询并行，适配二值/三值/区间匹配。实验资源占用低、访存更新延迟均衡，图三角计数案例平均加速4.92倍，代码已开源。

## 背景和动机
1. CAM可按内容并行匹配，是图计算、网络、数据库加速核心部件，FPGA凭借可重构特性适合实现各类CAM。
2. 传统FPGA CAM分为LUT、BRAM、混合资源三类，均存在明显短板：规模扩大时资源消耗指数上升、读写延迟高、难以支持多并发查询、与上层加速器集成难度大。
3. 已有DSP型CAM仅基础存储匹配，未优化多查询、更新通路，不满足频繁读写的数据密集场景需求。
4. DSP48E2具备高速逻辑与存储能力，可替代LUT/BRAM构建CAM，兼顾可配置、多查询、低资源开销需求。

## 相关工作
1. LUT类CAM（Scale-TCAM、DURE等）：匹配速度快，但LUT消耗巨大，动态更新预处理开销高，扩展性弱。
2. BRAM类CAM（PUMP-CAM、HP-TCAM）：存储容量大，但BRAM为串行访问，并行比较逻辑拖慢主频，更新延迟高。
3. 混合资源CAM（REST-CAM）：平衡存储与逻辑，但多类资源协同管理逻辑复杂，更新流程繁琐。
4. 早期DSP-CAM：仅实现基础内容匹配，无多查询并行机制，读写延迟不均衡，不适合高并发数据负载。

## 本文解决方案
采用**单元-块-单元**三层全参数化DSP CAM分层架构：
1. CAM Cell：配置DSP48E2为异或掩码模式，单DSP实现48bit存储，掩码兼容BCAM/TCAM/RMCAM，更新1周期、搜索2周期，零LUT/BRAM消耗。
2. CAM Block：集成多路选择、更新/搜索逻辑、编码器，单块并行驱动多个Cell，更新延迟恒定1周期，支持批量并行写入。
3. CAM Unit：引入分组路由架构，划分为多CAM分组，每组独立处理查询，单周期最多支持M条并发检索；路由表统一管理数据分发，更新全局同步写入所有分组。
4. 全层级可参数化：单元/块/单元层自定义位宽、容量、编码方式，便于嵌入各类FPGA加速器。

## 实验分析
1. 实验平台：AMD Alveo U250 FPGA，Vivado 2021.2综合，评测指标含延迟、吞吐、资源占用、可扩展性。
2. 分层性能：Cell仅消耗1个DSP；Block规模扩容主频稳定300MHz，LUT占用极低；Unit最大支持9728×48bit，仅少量LUT，BRAM几乎无消耗，主频最低235MHz。
3. 对比SOTA：相较LUT/BRAM方案，DSP资源利用率高、LUT开销极小，读写延迟均衡，原生支持多并发查询，扩展性显著领先。
4. 图计算案例：嵌入三角计数加速器，并行集合相交替代串行归并算法，10组真实图数据集平均加速4.92倍，稀疏图最高加速17.54倍。
5. 开销：仅少量FIFO占用BRAM，DSP为主资源，可预留大量片上资源给上层业务逻辑。

## 研究启发
1. FPGA异构资源复用思路：充分挖掘DSP算术/比较硬件能力，缓解LUT、BRAM资源瓶颈，适合构建低开销专用存储阵列。
2. 分层参数化硬件设计：三级粒度可配置架构，兼顾通用性与性能，降低CAM与领域加速器集成成本。
3. 多查询分组并行架构设计：通过资源分组隔离并发检索通路，提升数据密集型任务吞吐，解决传统CAM单查询限制。
4. 专用存储加速图计算：利用CAM并行匹配特性优化集合相交等不规则算子，可大幅超越传统基于地址访存的串行算法。
5. 硬件设计开源化：开放参数化模板代码，便于后续拓展TCAM、范围匹配及更多数据密集型应用。