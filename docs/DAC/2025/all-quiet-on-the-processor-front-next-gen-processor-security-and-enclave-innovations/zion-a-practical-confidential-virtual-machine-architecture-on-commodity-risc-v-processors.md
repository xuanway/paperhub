---
title: "Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "risc-v"
  - "confidential-computing"
  - "virtual-machine"
  - "pmp"
---

# Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://yinqian.org/papers/dac25a.pdf">https://yinqian.org/papers/dac25a.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 机密虚拟机，RISC-V，可信执行环境 </p>
</div>

---

## 研究概要
本文提出Zion，一款面向商用无硬件扩展RISC-V的机密虚拟机架构。依托原生PMP/虚拟化扩展，设计短路径CVM模式、分层内存、分离页表共享机制，搭配安全/共享双vCPU降低切换开销。多类负载测试，绝大多数真实应用性能开销低于5%，兼容未修改客户机程序。

## 背景和动机
1. 主流RISC-V TEE（Sanctum/Keystone）均为进程隔离，需改造应用，兼容性差；CURE/VirTEE机密VM依赖定制硬件扩展，无法商用标准RISC-V。
2. RISC-V官方CoVE规范仍在研发，短期内无落地硬件，缺少立即可用的机密虚拟机方案。
3. 现有VM隔离采用连续物理内存+固定PMP区域，PMP条目数量受限，并发VM少、内存碎片化严重，不适合云弹性扩缩容。
4. 传统安全超visor多层权限切换，上下文切换周期开销巨大，MMIO交互带来显著性能损耗。
5. 虚拟机共享内存同步逻辑复杂，非可信宿主机可篡改页表，存在数据泄露、TOCTOU攻击风险。

## 相关工作
1. 进程级RISC-V TEE：Sanctum、Keystone、Penglai，隔离粒度为进程，遗留程序需移植，无法完整运行通用VM。
2. 定制硬件CURE/VirTEE：需新增CPU/总线安全扩展，硬件兼容性差，仅支持少量并发机密虚拟机。
3. RISC CoVE标准：官方机密VM规范，设计轻量安全超visor，但硬件未量产，暂无成熟实现原型。
4. ARM TwinVisor等机密VM：依赖架构专属硬件隔离，无法迁移至开源RISC-V平台，切换路径冗长。
5. 传统内存隔离方案：连续物理分区+固定PMP，并发受限、不支持动态内存扩容，共享内存同步开销高。

## 本文解决方案
### 1 短路径CVM隔离模式
移除独立安全超visor，全部安全逻辑置于M模式安全监视器SM；陷阱委派机制区分VM内处理与SM处理逻辑，仅单次权限切换完成CVM/普通模式切换，大幅减少特权跳转层数。
### 2 双vCPU状态保护机制
安全vCPU存放机密寄存器（宿主机不可访问），共享vCPU仅存放MMIO异常临时字段；采用Load后校验抵御TOCTOU攻击，加速宿主机与SM状态交互，降低切换周期。
### 3 PMP+二级页表分层内存隔离
PMP划分全局安全内存池，二级页表隔离不同CVM；IOPMP阻断DMA外设越权访问，SM独占客户机页表，防止宿主机篡改内存映射。
### 4 分层安全内存管理
256KB内存块双向链表管理，三级分配流程：vCPU本地页缓存优先→分配新内存块→向宿主机申请扩容，多数缺页无需模式切换，分配效率O(1)。
### 5 分离页表内存共享机制
客户机GPA分为私有、共享两段地址空间；宿主机仅管控共享页表，无权修改私有安全内存，无需跨SM同步即可完成virtio设备缓冲区交互。

## 实验分析
1. 实验平台：Genesys2 FPGA，4核Rocket 100MHz，OpenSBI+KVM/QEMU完整虚拟化栈。
2. 切换性能：共享vCPU使CVM进出周期提升20%+；短路径相比多层长路径，进入提速44.7%、退出提速55.3%。
3. 缺页开销：一级缓存缺页31103周期，仅少量扩容场景开销显著，平均缺页开销接近普通VM。
4. 基准负载：RV8加密/排序类基准平均开销2.59%，CoreMark下降2.77%；Redis内存负载吞吐量降5.3、时延增4%。
5. IO负载：小文件读写开销<5%，大文件频繁IO切换最高达20%，绝大多数业务开销可控。

## 研究启发
1. 商用RISC-V原生PMP、虚拟化扩展可搭建完整机密虚拟机，无需定制硬件，降低云机密计算落地门槛。
2. 抛弃独立安全超visor、统一安全逻辑至M模式监视器，是降低上下文切换开销的核心优化思路。
3. 单一连续内存隔离扩展性不足，PMP配合二级分页可实现弹性内存扩容、支持大规模并发机密VM。
4. 分离页表拆分私有/共享地址，能在保证安全前提下消除共享内存频繁同步的性能瓶颈。
5. 进程型TEE兼容性短板明显，VM级TEE无需修改客户程序，更适配云原生通用业务场景。