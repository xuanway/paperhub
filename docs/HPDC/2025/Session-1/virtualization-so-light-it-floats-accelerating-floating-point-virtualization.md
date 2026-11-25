---
title: "Virtualization So Light, it Floats! Accelerating Floating Point Virtualization"
description: "HPDC 2025 · Session 1 — Numerical Methods"
tags:
  - "HPDC2025"
  - "Session 1"
  - "Numerical Methods"
---

# Virtualization So Light, it Floats! Accelerating Floating Point Virtualization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 1</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731584) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/wanninger.pdf)

**作者**：Nicholas Wanninger, Nadharm Dhiantravan, Peter Dinda

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

Floating point virtualization enables unmodified application binaries to utilize alternative arithmetic systems such as MPFR without code changes, but its performance overhead is a barrier to adoption. The existing trap-and-emulate model suffers from a significant virtualization bottleneck using general-purpose signal delivery mechanisms which take thousands of cycles. We introduce three techniques to reduce virtualization overhead. Trap short-circuiting bypasses general-purpose signal delivery for an 8x reduction in trap delegation overhead. Instruction sequence emulation amortizes trap costs by emulating multiple instructions per trap, achieving up to 32x reduction in trap frequency. Finally, kernel-bypass for correctness instrumentation eliminates traps and signals for correctness and reduces related overheads substantially. Our implementation within the FPVM system on x64/Linux demonstrates a 10x reduction in per-instruction overhead which, compared to the lower bound performance set by the alternative arithmetic system, drops virtualization overhead from up to 20x to 1.65x. This is for the alternative arithmetic system that is the worst case for virtualization overheads. More expensive systems, like MPFR, fare even better.

## 中文摘要

浮点虚拟化使未经修改的应用二进制无需更改代码即可使用诸如 MPFR 的替代算术系统，但其性能开销是阻碍采用的一大障碍。现有的陷入-模拟（trap-and-emulate）模型使用通用信号投递机制，需耗费数千个周期，造成严重的虚拟化瓶颈。我们提出三种降低虚拟化开销的技术。陷阱短路（trap short-circuiting）绕过通用信号投递，将陷阱委派开销降低 8 倍。指令序列模拟通过每次陷阱模拟多条指令来摊销陷阱成本，使陷阱频率最高降低 32 倍。最后，用于正确性插桩的内核旁路（kernel-bypass）消除了正确性相关的陷阱与信号，大幅降低相关开销。我们在 x64/Linux 上的 FPVM 系统中的实现表明，单指令开销降低 10 倍；相对于替代算术系统设定的性能下界，虚拟化开销从最高 20 倍降至 1.65 倍。这还是在虚拟化开销最坏情况下的替代算术系统上测得的。对于 MPFR 等开销更高的系统，效果更好。

## 英文关键词

virtualization, floating point arithmetic, software development, IEEE 754

## 中文关键词

虚拟化，浮点算术，软件开发，IEEE 754

---

[← 返回 Session 1 — Numerical Methods](index.md)
