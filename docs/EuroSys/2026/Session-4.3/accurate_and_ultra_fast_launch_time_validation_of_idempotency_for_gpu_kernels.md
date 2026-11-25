---
title: "Accurate and Ultra-Fast Launch-Time Validation of Idempotency for GPU Kernels"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Mingcong Han (Shanghai Jiao Tong University), Weihang Shen (Shanghai Jiao Tong U"
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# Accurate and Ultra-Fast Launch-Time Validation of Idempotency for GPU Kernels

**中文标题：** GPU 内核幂等性的精确超快启动时验证

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Mingcong Han (Shanghai Jiao Tong University), Weihang Shen (Shanghai Jiao Tong University), Rong Chen (Shanghai Jiao Tong University), Haibo Chen (Shanghai JiaoTong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803597)

## 英文摘要

We discovered that a GPU kernel can have both idempotent and non-idempotent instances depending on the input. These kernels, called conditionally-idempotent, are common in realworld GPU applications—490 out of 547 from six popular applications. This finding reveals a limitation in previous work that statically classifies GPU kernels as idempotent or non-idempotent, potentially compromising the correctness and effectiveness of idempotence-based systems. This paper presents PICKER, the first launch-time analysis system for instance-level idempotency validation. PICKER accurately validates the idempotency of GPU kernel instances before execution by utilizing launch arguments. Several optimizations are proposed to reduce validation latency to microseconds. Evaluations using representative GPU applications (547 kernels and 18,217 instances) show that PICKER accurately identifies idempotent instances with zero false positives and an 18.54% false-negative rate. The launch-time validation completes in under 5 µs for all instances (about 90% under 1 µs). Through integration, PICKER reduces checkpoint costs to less than 4% in fault-tolerant systems and decreases preemption latency by 84.2% in scheduling systems.

## 中文摘要

我们发现，同一个 GPU 内核可能因输入不同而同时具有幂等实例和非幂等实例。这类内核被称为条件幂等内核，在真实 GPU 应用中十分普遍——来自六个流行应用的 547 个内核中有 490 个属于此类。这一发现揭示了先前工作的局限：静态地将 GPU 内核归类为幂等或非幂等，可能损害基于幂等的系统的正确性与有效性。本文提出 PICKER，首个面向实例级幂等性验证的启动时分析系统。PICKER 在执行前利用启动参数精确验证 GPU 内核实例的幂等性。我们提出多项优化，将验证延迟降至微秒级。使用代表性 GPU 应用（547 个内核、18,217 个实例）的评估表明，PICKER 以零假阳性和 18.54% 的假阴性率准确识别幂等实例。所有实例的启动时验证均在 5 µs 内完成（约 90% 在 1 µs 内）。通过集成，PICKER 在容错系统中将检查点开销降至 4% 以下，在调度系统中将抢占延迟降低 84.2%。

**英文关键词：** GPU kernel idempotency, launch-time validation

**中文关键词：** GPU 内核幂等性、启动时验证

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
