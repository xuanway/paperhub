---
title: "ARTEMIS: Agile Discovery of Efficient Real-Time Systems-on-Chips in the Heterogeneous Era"
description: "HPCA 2025 · Finding the Best Table"
tags:
  - "HPCA2025"
  - "Finding the Best Table"
---

# ARTEMIS: Agile Discovery of Efficient Real-Time Systems-on-Chips in the Heterogeneous Era

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Finding the Best Table。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Finding the Best Table</p>
</div>

**论文链接**：
**作者**：Subhankar Pal (IBM Research), Aporva Amarnath (IBM Research), Behzad Boroujerdian (University of Texas at Austin / Harvard University), Augusto Vega (IBM Research), Alper Buyuktosunoglu (IBM Research), John-David Wellman (IBM Research), Vijay Janapa Reddi (Harvard University), Pradip Bose (IBM Research)
**会议**：HPCA 2025

---

## 中文标题

ARTEMIS：异构时代下高效实时片上系统的敏捷发现

## 英文摘要

Heterogeneous systems-on-chips (SoCs) are pivotal for real-time applications like autonomous driving, as they blend the versatility of CPUs with the efficiency of accelerator IPs. However, evolving application demands necessitate domain-specific SoCs to meet real-time deadlines within strict power and area constraints. While prior research focused on microarchitectural optimizations, overlooking broader system-level considerations can lead to suboptimal design decisions. Thus, there is a need to elevate the abstraction level of design space exploration (DSE) to the SoC level. However, SoC-level DSE is challenging due to the vast design space, encompassing microarchitectural parameters and dynamic task-to-hardware mapping choices based on run-time characteristics and real-time constraints. This paper proposes a systematic and agile methodology, called ARTEMIS, for efficient DSE of real-time, domain-specific SoCs that are constrained by task deadlines, power, and area. The core concept involves integrating a dynamic SoC scheduler to reduce the design space by eliminating the mapping dimension. Enhanced scheduling policies, incorporating techniques like task procrastination and memory-traffic/energy awareness, expedite navigation through the pruned design space. Additionally, DSE heuristics are optimized with real-time deadline and power/area-aware ranking mechanisms. ARTEMIS is evaluated on autonomous vehicle (AV) and augmented/virtual reality (AR/VR) applications, and additionally validated on an FPGA. Compared to the state-of-the-art, DSE using ARTEMIS converges 5.1– 12.8× faster, while yielding SoCs that meet 100% real-time deadlines with 1.2–3× better throughput at iso-area or up to 2.4× lower area for at iso-input-rate. ARTEMIS thus enables DSE of large designs with tractable simulation resources, without compromising on the power-performance-area metrics of the explored SoC design.

## 中文摘要

异构片上系统（SoC）对自动驾驶等实时应用至关重要，因为它们将 CPU 的多功能性与加速器 IP 的高能效结合起来。然而，不断变化的应用需求要求领域专用 SoC 在严格的功耗与面积约束下满足实时截止期限。以往研究聚焦于微架构优化，而忽视更广泛的系统级考量可能导致次优的设计决策。因此，有必要将设计空间探索（DSE）的抽象层次提升到 SoC 级别。然而，SoC 级 DSE 的设计空间极其庞大，既含微架构参数，也含依据运行时特征与实时约束的动态任务到硬件映射选择，颇具挑战。本文提出一种系统化且敏捷的方法 ARTEMIS，用于受任务截止期限、功耗与面积约束的实时领域专用 SoC 的高效 DSE。其核心是集成动态 SoC 调度器，通过消除映射维度来缩减设计空间。融入任务拖延与内存流量/能耗感知等技术的增强调度策略，可加速在剪枝后设计空间中的搜索。此外，DSE 启发式方法通过感知实时截止期限与功耗/面积的排序机制得到优化。ARTEMIS 在自动驾驶（AV）与增强/虚拟现实（AR/VR）应用上进行了评估，并在 FPGA 上进一步验证。与最先进的方法相比，使用 ARTEMIS 的 DSE 收敛速度快 5.1-12.8×，同时产出的 SoC 100% 满足实时截止期限，在等面积下吞吐提升 1.2-3×，或在等输入速率下面积最多降低 2.4×。因此，ARTEMIS 使大型设计的 DSE 能在可承受的仿真资源下完成，同时不牺牲所探索 SoC 设计的功耗-性能-面积指标。
