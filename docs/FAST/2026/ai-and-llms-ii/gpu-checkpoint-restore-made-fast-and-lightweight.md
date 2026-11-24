---
title: "GPU Checkpoint/Restore Made Fast and Lightweight"
description: "FAST 2026 · AI and LLMs II · 第 239–254 页"
tags:
  - "FAST2026"
  - "AI and LLMs II"
---

# GPU Checkpoint/Restore Made Fast and Lightweight

**中文标题**：快速轻量的 GPU 检查点/恢复

**Session**：AI and LLMs II · 2026-02-25 10:50–12:30 · Chair：Jian Zhang（The Hong Kong University of Science and Technology）

**作者**：Shaoxun Zeng, Tingxu Ren, Jiwu Shu, and Youyou Lu, Tsinghua University

**会议**：FAST 2026 · Santa Clara, CA · 第 239–254 页

**获奖**：Distinguished Artifact Award

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zeng](https://www.usenix.org/conference/fast26/presentation/zeng)

**论文 PDF**：[fast26-zeng.pdf](https://www.usenix.org/system/files/fast26-zeng.pdf)

---

## 英文摘要

System-level GPU checkpoint/restore (C/R) enables several critical features such as elastic scaling, task switching, and fault tolerance, for modern GPU workloads in a unified and application-transparent manner. However, existing approaches present fundamental limitations: they fail to simultaneously achieve low C/R latency and low overhead imposed on normal GPU execution, while also lacking efficient support for incremental checkpointing. We propose GCR, a GPU checkpoint/restore system that addresses all these limitations simultaneously. GCR employs a hybrid C/R scheme through control/data separation to deliver low C/R latency and negligible overhead imposed on normal GPU execution. To efficiently support incremental checkpointing, GCR introduces shadow execution on the CPU to reduce the overhead of dirty buffer identification, utilizing dirty templates for both lightweight CPU shadow execution and identification at a fine-grained instruction level.

Our evaluations demonstrate that GCR reduces GPU checkpointing latency by 72.1% and 63.6% compared to cuda-ckpt (NVIDIA’s official solution) and PhOS (the current state-of-the-art), respectively, and restoration latency by 54.2% and 87.1%, while imposing negligible overhead (less than 1%). GCR also supports efficient incremental checkpointing, which reduces checkpoint sizes by 86.6% and latency by 43.8%.

## 中文摘要

系统级 GPU 检查点/恢复（C/R）能够以统一且对应用透明的方式，为现代 GPU 负载提供弹性伸缩、任务切换和容错等关键功能。然而，现有方法存在根本性局限：它们无法同时实现低 C/R 延迟和对正常 GPU 执行的低开销，同时也缺乏对增量检查点的高效支持。我们提出 GCR，一个同时解决上述所有局限的 GPU 检查点/恢复系统。GCR 采用控制/数据分离的混合 C/R 方案，以实现低 C/R 延迟和对正常 GPU 执行可忽略的开销。为高效支持增量检查点，GCR 在 CPU 上引入影子执行，以降低脏缓冲区识别的开销，并利用脏模板实现轻量级 CPU 影子执行和细粒度指令级识别。

我们的评估表明，与 cuda-ckpt（NVIDIA 官方方案）和 PhOS（当前最先进方案）相比，GCR 分别将 GPU 检查点延迟降低 72.1% 和 63.6%，将恢复延迟降低 54.2% 和 87.1%，同时带来可忽略的开销（低于 1%）。GCR 还支持高效的增量检查点，可将检查点大小减少 86.6%，将延迟降低 43.8%。
