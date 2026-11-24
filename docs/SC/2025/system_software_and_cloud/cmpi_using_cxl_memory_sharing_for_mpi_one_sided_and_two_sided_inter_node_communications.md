---
title: "cMPI: Using CXL Memory Sharing for MPI One-Sided and Two-Sided Inter-Node Communications"
description: "SC 2025 · System Software and Cloud · Xi Wang; Bin Ma; Jongryool Kim; Byungil Koh; Hoshik Kim; Dong Li"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# cMPI: Using CXL Memory Sharing for MPI One-Sided and Two-Sided Inter-Node Communications

**中文标题：** 利用 CXL 内存共享实现 MPI 单边和双边节点间通信

**所属 Session：** [System Software and Cloud](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Xi Wang; Bin Ma; Jongryool Kim; Byungil Koh; Hoshik Kim; Dong Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap397&sess=sess287)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Message Passing Interface (MPI) is a foundational programming model for high-performance computing. MPI libraries traditionally employ network interconnects (e.g., Ethernet and InfiniBand) and network protocols (e.g., TCP and RoCE) with complex software stacks for cross-node communication. We present cMPI, the first work to optimize MPI point-to-point communication (both one-sided and two-sided) using CXL memory sharing on a real CXL platform, transforming cross-node communication into memory transactions and data copies within CXL memory, bypassing traditional network protocols. We analyze performance across various interconnects and find that CXL memory sharing achieves 7.2×-8.1× lower latency than TCP-based interconnects deployed in small- and medium-scale clusters. We address challenges of CXL memory sharing for MPI communication, including data object management over the dax representation [50], cache coherence, and atomic operations. Overall, cMPI outperforms TCP over standard Et

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
