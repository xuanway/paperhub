---
title: "Revealing the Unstable Foundations of eBPF-Based Kernel Extensions"
description: "EuroSys 2025 · Operating Systems · Shawn Zhong (University of Wisconsin-Madison), Jing Liu (Microsoft Research), An"
tags:
  - "EuroSys2025"
  - "Operating Systems"
---

# Revealing the Unstable Foundations of eBPF-Based Kernel Extensions

**中文标题：** 揭示基于 eBPF 的内核扩展不稳定的基础

**所属 Session：** [Session 1.1: Operating Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Operating Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Operating Systems</p>
</div>

**作者**：Shawn Zhong (University of Wisconsin-Madison), Jing Liu (Microsoft Research), Andrea Arpaci-Dusseau (UW-Madison), Remzi Arpaci-Dusseau (University of Wisconsin–Madison)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717497)

## 英文摘要

eBPF programs significantly enhance kernel capabilities, but encounter substantial compatibility challenges due to their deep integration with unstable kernel internals. We introduce DepSurf, a tool that identifies dependency mismatches between eBPF programs and kernel images. Our analysis of 25 kernel images spanning 8 years reveals that dependency mismatches are pervasive, stemming from kernel source code evolution, diverse configuration options, and intricate compilation processes. We apply DepSurf to 53 real-world eBPF programs, and find that 83% are impacted by dependency mismatches, underscoring the urgent need for systematic dependency analysis. By identifying these mismatches, DepSurf enables a more robust development and maintenance process for eBPF programs, enhancing their reliability across a wide range of kernels.

## 中文摘要

eBPF 程序显著增强了内核能力，但由于其与不稳定的内核内部结构深度耦合，也面临着严峻的兼容性挑战。我们提出 DepSurf，一个用于识别 eBPF 程序与内核镜像之间依赖失配的工具。我们对跨越 8 年的 25 个内核镜像的分析表明，依赖失配问题普遍存在，其根源在于内核源代码的演化、多样的配置选项以及复杂的编译过程。我们将 DepSurf 应用于 53 个真实世界的 eBPF 程序，发现其中 83% 受到依赖失配的影响，这凸显了系统性依赖分析的迫切需求。通过识别这些失配，DepSurf 使 eBPF 程序的开发与维护过程更加稳健，提升了其在各类内核上的可靠性。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
