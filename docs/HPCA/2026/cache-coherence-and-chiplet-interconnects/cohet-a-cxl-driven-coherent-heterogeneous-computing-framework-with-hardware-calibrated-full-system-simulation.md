---
title: "Cohet: A CXL-Driven Coherent Heterogeneous Computing Framework with Hardware-Calibrated Full-System Simulation"
description: "HPCA 2026 · Cache Coherence and Chiplet Interconnects"
tags:
  - "HPCA2026"
  - "Cache Coherence and Chiplet Interconnects"
---

# Cohet: A CXL-Driven Coherent Heterogeneous Computing Framework with Hardware-Calibrated Full-System Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Cache Coherence and Chiplet Interconnects。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Cache Coherence and Chiplet Interconnects</p>
</div>

**论文链接**：
**作者**：Yanjing Wang National University of Defense Technology , Lizhou Wu National University of Defense Technology , Sunfeng Gao National University of Defense Technology , Yibo Tang National University of Defense Technology , Junhui Luo National University of Defense Technology , Zicong Wang National University of Defense Technology , Yang Ou National University of Defense Technology , Dezun Dong NUDT , Nong Xiao National University of Defense Technology & Sun Yat-sen University , Mingche Lai National University of Defense Technology
**会议**：HPCA 2026

---

## 中文标题

Cohet：CXL 驱动的缓存一致异构计算框架与硬件校准全系统仿真

## 英文摘要

Conventional heterogeneous computing systems built on PCIe interconnects suffer from inefficient fine-grained host-device interactions and complex programming models. In recent years, many proprietary and open cache-coherent interconnect standards have emerged, among which compute express link (CXL) prevails in the open-standard domain after acquiring several competing solutions. Although CXL-based coherent heterogeneous computing holds the potential to fundamentally transform the collaborative computing mode of CPUs and XPUs, research in this direction remains hampered by the scarcity of available CXL-supported platforms, immature software/hardware ecosystems, and unclear application prospects. This paper presents Cohet, the first CXL-driven coherent heterogeneous computing framework. Cohet decouples the compute and memory resources to form unbiased CPU and XPU pools which share a single unified and coherent memory pool. It exposes a standard malloc/mmap interface to both CPU and XPU compute threads, which share a single per-process page table for user applications, leaving the OS dealing with smart memory allocation, page auto-migration, and management of heterogeneous resources. This design significantly simplifies heterogeneous parallel programming to a level comparable to homogeneous programming. To facilitate Cohet research, we also present a full-system cycle-level simulator named SimCXL, which is capable of modeling all CXL sub-protocols and device types. SimCXL has been rigorously calibrated against a real CXL testbed with various CXL memory and accelerators, showing an average simulation error of 3%. Our evaluation reveals that CXL.cache reduces latency by 68% and increases bandwidth by 14.4× compared to DMA transfers at cacheline granularity. Building upon these insights, we demonstrate the benefits of Cohet with two killer apps, which are remote atomic operation (RAO) and remote procedure call (RPC). Compared to PCIe-NIC design, CXL-NIC achieves a 5.5 to 40.2× speedup for RAO offloading and an average speedup of 1.86× for RPC (de)serialization offloading.

## 中文摘要

基于 PCIe 互连构建的传统异构计算系统受困于低效的细粒度主机—设备交互与复杂的编程模型。近年来涌现出许多专有与开放的缓存一致互连标准，其中 compute express link（CXL）在整合若干竞争方案后成为开放标准领域的主流。尽管基于 CXL 的一致性异构计算有望从根本上改变 CPU 与 XPU 的协同计算模式，但该方向的研究仍受制于可用 CXL 平台稀缺、软硬件生态不成熟以及应用前景不明。本文提出 Cohet，首个由 CXL 驱动的一致性异构计算框架。Cohet 将计算与内存资源解耦，形成无偏的 CPU 池与 XPU 池，二者共享单一统一且一致的内存池。它向 CPU 与 XPU 计算线程暴露标准的 malloc/mmap 接口，这些线程为用户应用共享单一每进程页表，由操作系统负责智能内存分配、页面自动迁移与异构资源管理。该设计将异构并行编程显著简化到与同构编程相当的水平。为便于 Cohet 研究，我们还提出全系统周期级仿真器 SimCXL，可对全部 CXL 子协议与设备类型建模。SimCXL 已针对包含多种 CXL 内存与加速器的真实 CXL 测试平台严格校准，平均仿真误差为 3%。评估显示，在缓存行粒度上，与 DMA 传输相比，CXL.cache 将时延降低 68%、带宽提升 14.4 倍。基于这些发现，我们通过远程原子操作（RAO）与远程过程调用（RPC）两个杀手级应用展示 Cohet 的优势。与 PCIe-NIC 设计相比，CXL-NIC 在 RAO 卸载上取得 5.5 至 40.2 倍的加速比，在 RPC（反）序列化卸载上取得平均 1.86 倍的加速比。
