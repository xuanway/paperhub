---
title: "Characterizing and Emulating FDP SSDs with WARP"
description: "FAST 2026 · SSDs and CXL · 第 347–362 页"
tags:
  - "FAST2026"
  - "SSDs and CXL"
---

# Characterizing and Emulating FDP SSDs with WARP

**中文标题**：基于 WARP 的 FDP SSD 表征与仿真

**Session**：SSDs and CXL · 2026-02-25 14:00–15:40 · Chair：Ethan Miller（University of California, Santa Cruz, and Pure Storage）

**作者**：Inho Song and Shoaib Asif Qazi, Virginia Tech; Javier González, Samsung Electronics; Matias Bjørling, Western Digital; Sam H. Noh and Huaicheng Li, Virginia Tech

**会议**：FAST 2026 · Santa Clara, CA · 第 347–362 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/song](https://www.usenix.org/conference/fast26/presentation/song)

**论文 PDF**：[fast26-song.pdf](https://www.usenix.org/system/files/fast26-song.pdf)

---

## 英文摘要

Flexible Data Placement (FDP) promises to reduce write amplification by steering writes across reclaim unit handles (RUHs), yet outcomes vary widely across devices. This paper presents WARP, the first open emulator and comprehensive study of FDP SSDs. Our cross-device, cross-workload characterization shows that FDP sustains near-1 WAF when RUH isolation aligns with object lifetimes, but fails under misclassification, RUH interference, or adversarial invalidations. WARP reproduces hardware WAF trends while exposing per-RUH dynamics and configurable policies hidden in real devices. With WARP, we explore the firmware design space for FDP and demonstrate policies that reduce WAF beyond current hardware. By combining empirical characterization with a transparent emulator, this work advances FDP research from anecdotal reports to principled understanding and provides a platform for future FDP-aware system design.

## 中文摘要

灵活数据放置（FDP）有望通过将写请求导向不同的回收单元句柄（RUH）来减少写放大，但其效果在不同设备间差异很大。本文提出 WARP，这是首个面向 FDP SSD 的开放仿真器与全面研究。我们的跨设备、跨负载表征表明，当 RUH 隔离与对象生命周期一致时，FDP 可维持接近 1 的 WAF；但在分类错误、RUH 干扰或对抗性无效化情况下则会失效。WARP 能够复现硬件 WAF 趋势，同时揭示真实设备中隐藏的逐 RUH 动态和可配置策略。借助 WARP，我们探索了 FDP 的固件设计空间，并展示了可进一步降低 WAF、超越当前硬件的策略。通过将实证表征与透明仿真器相结合，本工作推动 FDP 研究从零散报告走向原理性理解，并为未来 FDP 感知的系统设计提供了平台。
