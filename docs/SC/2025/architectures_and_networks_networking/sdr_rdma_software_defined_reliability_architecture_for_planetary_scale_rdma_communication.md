---
title: "SDR-RDMA: Software-Defined Reliability Architecture for Planetary-Scale RDMA Communication"
description: "SC 2025 · Architectures and Networks: Networking · Mikhail Khalilov; Siyuan Shen; Marcin Chrapek; Tiancheng Chen; Kenji Nakano; Pet"
tags:
  - "SC2025"
  - "Architectures and Networks: Networking"
---

# SDR-RDMA: Software-Defined Reliability Architecture for Planetary-Scale RDMA Communication

**中文标题：** 面向行星级 RDMA 通信的软件定义可靠性架构

**所属 Session：** [Architectures and Networks: Networking](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Networking。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Networking</p>
</div>

**作者**：Mikhail Khalilov; Siyuan Shen; Marcin Chrapek; Tiancheng Chen; Kenji Nakano; Peter-Jan Gootzen; Salvatore Di Girolamo; Rami Nudelman; Gil Bloch; Jithin Jose; Abdul Kabbani; Sreevatsa Anantharamu; Jie Zhang; Konstantin Taranov; Zhuolong Yu; Scott Moe; Mahmoud Elhaddad; Nicola Mazzoletti; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap970&sess=sess192)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

RDMA is vital for efficient distributed training across datacenters, but millisecond-scale latencies complicate the design of its reliability layer. We show that depending on long-haul link characteristics, such as drop rate, distance, and bandwidth, the widely used Selective Repeat algorithm can be inefficient, warranting alternatives like erasure coding. To enable such alternatives on existing hardware, we propose SDR-RDMA, a software-defined reliability stack for RDMA. Its core is a lightweight SDR SDK that extends standard point-to-point RDMA semantics — fundamental to AI networking stacks — with a receive buffer bitmap. SDR bitmap enables partial message completion to let applications implement custom reliability schemes tailored to specific deployments, while preserving zero-copy RDMA benefits. By offloading the SDR backend to NVIDIA’s Data Path Accelerator (DPA), we achieve line-rate performance, enabling efficient inter-datacenter communication and advancing reliability innovat

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
