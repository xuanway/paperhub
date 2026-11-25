---
title: "Leopard: Hardware Pass-Through Remote Storage Access with Queue Concurrency for Edge Intelligent Workstations"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Leopard: Hardware Pass-Through Remote Storage Access with Queue Concurrency for Edge Intelligent Workstations

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133404">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133404</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 边缘智能工作站，远程存储，硬件直通，队列并发，并行化与流水线工作流 </p>
</div>

---

## 研究概要
本文面向算力存储受限边缘智能工作站，提出基于FPGA SmartNIC的Leopard硬件直通远程存储框架。自定义NVMe控制器消除主机远程软件栈，多队列并行流水线硬件加速器卸载全链路IO处理。真实负载下延迟较主流方案低1.09~6.04倍，CPU开销大幅降低，远程性能接近本地NVMe。

## 背景和动机
1. 边缘工作站本地存储不足，需频繁读写云端远程NVMe，但现有NVMe-oF、iSCSI依赖复杂内核软件栈，大量占用稀缺边缘CPU。
2. 传统方案依靠多核调度多NVMe请求队列，边缘CPU算力不足以打满SSD并发，小IO场景栈延迟占总耗时49%以上。
3. 现有卸载方案仅优化服务端，边缘发起端仍存在完整远程存储栈，无法解决发起端CPU瓶颈。
4. 边缘业务以4KB~100KB小IO为主，软件栈开销成为核心性能短板，现有方案无法充分利用网卡、SSD多队列并发能力。
5. RDMA等方案部署门槛高，难以适配通用边缘TCP网络环境，远程读写性能相较本地仍存在10%~75%衰减。

## 相关工作
1. 传统远程存储协议：iSCSI单队列架构不适用于NVMe；NVMe-oF TCP/RDMA依赖主机软件处理，边缘CPU开销巨大。
2. 服务端卸载方案：NVMe-oF Target Offload仅简化存储服务器栈，边缘发起端软件开销未解决。
3. 软件优化NVMe-oF：i10优化CPU流水线，但仍无法脱离内核远程存储栈，边缘场景提升有限。
4. 用户态存储框架ReFlex：不兼容POSIX接口，迁移复杂，依旧消耗大量主机CPU。
5. ARM架构SmartNIC加速：算力弱，无法实现完整NVMe硬件直通流水线。

## 本文解决方案
### 1 双端FPGA SmartNIC整体架构
分为Leopard发起端（边缘）与目标端（云存储），均基于Xilinx FPGA实现，通过100G QSFP互联，直连远端NVMe SSD PCIe。
### 2 AQ Handler原生NVMe控制器
FPGA模拟标准NVMe设备，边缘主机仅使用原生NVMe驱动，彻底移除VFS/远程存储软件栈，无需修改上层应用。
### 3 多队列并行硬件加速单元
- 请求抓取器/提交器：多独立DMA通道并行读写主机与SSD队列；
- 本地队列池：片上FIFO隔离每路SQ/CQ，实现队列粒度流水线；
- Transmitter收发器：分离控制/数据双通道，硬件TCP完成端到端直通，全程无CPU参与。
### 4 队列粒度并行流水线
控制面、数据面完全解耦，每对NVMe队列分配独立处理通路，硬件完成请求解析、网络传输、DMA搬运全流程。

## 实验分析
1. 测试平台：Xilinx ZU19 FPGA智能网卡、AMD边缘主机、Intel P4600 NVMe，对比nvof-tcp/nvof-rdma/i10/Target Offload。
2. 延迟吞吐：各类IO尺寸、线程、深度下远程读写性能逼近本地，相比基线平均提速1.09~6.04倍，小IO优化效果最突出。
3. CPU开销：内核/用户CPU占用大幅下降，归一化CPU资源相比基线降低1.33~2.90倍，缓解边缘算力竞争。
4. 真实负载：YCSB标准混合负载下延迟、吞吐量、CPU三项指标均显著优于现有方案。
5. 硬件代价：发起端FPGA资源占用33.23%、功耗16.67W，硬件成本可控，支持队列数弹性扩展。

## 研究启发
1. 边缘远程存储瓶颈不在网络，而在主机软件栈CPU开销，将全链路IO处理卸载至FPGA网卡可从根源解决。
2. 兼容原生NVMe驱动的硬件仿真方案，无需上层应用改造，工程落地成本远低于用户态框架。
3. 多队列并发不能依靠CPU调度，需在硬件层面为每对SQ/CQ构建独立并行流水线，释放SSD硬件性能。
4. 控制与数据面网络通道分离、硬件TCP直通，可规避协议栈软件处理带来的小IO长尾延迟。
5. FPGA SmartNIC是边缘存储卸载理想载体，低功耗、可编程特性适配算力受限边缘智能设备场景。
