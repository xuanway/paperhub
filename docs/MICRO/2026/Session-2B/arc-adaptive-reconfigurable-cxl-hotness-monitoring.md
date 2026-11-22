---
title: "ARC: Adaptive Reconfigurable CXL Hotness Monitoring"
description: "MICRO 2026 · Session 2B · ARC：自适应可重构 CXL 热度监测"
tags:
  - "MICRO2026"
  - "CXL"
  - "Reconfigurable Computing"
---

# ARC: Adaptive Reconfigurable CXL Hotness Monitoring

**中文标题：** ARC：自适应可重构 CXL 热度监测

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Chihun Song, Hwayong Nam, Haijian Wang, Eojin Na, Haneul Park, Taehyung Lee, Jung Ho Ahn, Nam Sung Kim

**来源：** MICRO 2026，pp. 609–626；[DOI](https://doi.org/10.1109/MICRO67795.2026.00055)

## 英文摘要

Compute Express Link (CXL) has emerged as a promising foundation for tiered memory systems, offering high bandwidth and large capacity expansion beyond the limits of host memory. The CXL specification recently introduced the CXL Hot-range Monitoring Unit (CHMU), standardizing the interface for device-side hot-page monitoring and reporting to the host. While CHMU defines the control and reporting interface, it leaves the internal counting structure to manufacturers. Each counting method carries inherent algorithmic trade-offs: a cache-based tracker records access counts only for pages that remain resident but suffers from eviction-induced count loss under limited capacity, whereas a CountMin-Sketch-based tracker covers a much larger address space but introduces collision-induced count inflation. Prior CXL-based hotness tracking designs have relied either on custom interfaces or on a single fixed counting method, leaving their complementary strengths unexploited. We propose ARC, an Adaptive Reconfigurable CXL Hotness Monitoring architecture that selects the most suitable counting algorithm at runtime to improve hot-page identification. We first systematically characterize the structural limitations of each counting method in isolation, revealing that their relative effectiveness shifts depending on workload access patterns. Building on these insights, ARC employs a lightweight hardware-counter-based predictor to select between counting algorithms at runtime, demonstrating that adaptive algorithm selection yields performance gains over a single static design. Furthermore, ARC consolidates both counting organizations by sharing SRAM, eliminating the need for separate storage arrays and achieving area efficiency with only modest overhead over the larger static design. ARC improves performance by up to 24.9% (4.3% on geomean) over cache-based and up to 8.8% (1.5% on geomean) over CountMin-Sketch-based CHMU tracking, with its largest gains on irregular workloads where the two modes diverge most, while reducing CHMU area by 28.2% over instantiating both trackers separately.

## 中文摘要

Compute Express Link (CXL) 已成为分层内存系统的一个有前途的基础，提供超出主机内存限制的高带宽和大容量扩展。 CXL 规范最近引入了 CXL 热范围监控单元 (CHMU)，标准化了设备端热页面监控并向主机报告的接口。虽然 CHMU 定义了控制和报告接口，但它将内部计数结构留给了制造商。每种计数方法都带有固有的算法权衡：基于缓存的跟踪器仅记录仍然驻留的页面的访问计数，但在有限的容量下会遭受驱逐引起的计数丢失，而基于 CountMin-Sketch 的跟踪器覆盖更大的地址空间，但会引入冲突引起的计数膨胀。之前基于 CXL 的热度跟踪设计要么依赖于自定义接口，要么依赖于单一的固定计数方法，从而使它们的互补优势未被充分利用。我们提出了 ARC，一种自适应可重配置 CXL 热点监控架构，它在运行时选择最合适的计数算法来改进热点页面识别。我们首先系统地描述每种计数方法的结构局限性，揭示它们的相对有效性根据工作负载访问模式而变化。基于这些见解，ARC 采用轻量级基于硬件计数器的预测器在运行时在计数算法之间进行选择，证明自适应算法选择比单个静态设计能带来性能提升。此外，ARC 通过共享 SRAM 来整合两个计数组织，从而无需单独的存储阵列，并且与较大的静态设计相比，只需适度的开销即可实现区域效率。与基于缓存的 CHMU 跟踪相比，ARC 的性能提高了高达 24.9%（在 geomean 上为 4.3%），与基于 CountMin-Sketch 的 CHMU 跟踪相比，性能提高了高达 8.8%（在 geomean 上为 1.5%），其中在两种模式差异最大的不规则工作负载上的增益最大，同时与分别实例化两个跟踪器相比，CHMU 面积减少了 28.2%。

## 中文关键词

CXL；动态随机存取存储器；访问热度监测；可重构监控

## 代码与研究制品

- 代码仓库：[https://github.com/ece-fast-lab/MICRO-2026-ARC](https://github.com/ece-fast-lab/MICRO-2026-ARC)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21478460](https://doi.org/10.5281/zenodo.21478460)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
