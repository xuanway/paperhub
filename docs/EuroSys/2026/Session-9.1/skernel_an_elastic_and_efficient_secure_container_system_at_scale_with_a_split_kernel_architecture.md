---
title: "SKernel: An Elastic and Efficient Secure Container System at Scale with a Split-Kernel Architecture"
description: "EuroSys 2026 · Cloud · Xiaohu Chai (Tsinghua University; Ant Group), Keyang Hu (Tsinghua University), J"
tags:
  - "EuroSys2026"
  - "Cloud"
---

# SKernel: An Elastic and Efficient Secure Container System at Scale with a Split-Kernel Architecture

**中文标题：** SKernel：基于分裂内核架构的大规模弹性高效安全容器系统

**所属 Session：** [Session 9.1: Cloud](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud</p>
</div>

**作者**：Xiaohu Chai (Tsinghua University; Ant Group), Keyang Hu (Tsinghua University), Jianfeng Tan (Ant Group), Tiwei Bie (Ant Group), Guotao Tan (Ant Group), Tianyu Zhou (Ant Group), Anqi Shen (Ant Group), Dawei Shen (Ant Group), Xinyao Yang (Ant Group), Xin Chen (Ant Group), Xu Wang (Ant Group), Feng Yu (Ant Group), Zhengyu He (Ant Group), Dong Du (Shanghai Jiao Tong University), Yubin Xia (Shanghai Jiao Tong University), Kang Chen (Tsinghua University), Yu Chen (Quan Cheng Laboratory, Jinan, China; Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769332)

## 英文摘要

Secure containers leverage hardware virtualization to isolate container sandboxes, enabling dedicated guest kernels to mitigate shared kernel attacks prevalent in traditional systems. However, existing approaches struggle with a fundamental trade-off: VM-based solutions (e.g., Kata) prioritize performance but lack elasticity and on-demand usage for volatile and bursty workloads, while lightweight methods (e.g., gVisor) rely on the host kernel for dynamic resource management at the cost of significant performance degradation due to guest-host dependencies.

We present SKernel, a production-proven secure container system that resolves this trade-off through a novel split-kernel architecture. Observing I/O stacks dominate performance for cloud-native apps, SKernel decouples the guest kernel into two components: SKernel-R (resource management via host collaboration) and SKernel-D (high-performance I/O operations without host involvement). Key innovations of SKernel include (1) a fast syscall forwarding approach that minimizes context switch overheads; (2) a device passthrough-based network stack that offers improved compatibility and resource flexibility, combined with an advanced thread model and I/O notification mechanism to handle volatile and bursty workloads; (3) a file descriptor-based container filesystem that enhances security, eliminates unnecessary indirection, and reduces costs. Macrobenchmarks evaluations show SKernel achieves 4.49× throughput gains over gVisor while matching its elasticity. SKernel reduces CPU usage compared to runc under production workloads, supporting over 2, 000 long-running microservices applications across 40,000+ nodes (with 100,000+ secure containers) at Ant Group. SKernel represents a milestone as a production-ready secure container that delivers both efficiency and elasticity.

## 中文摘要

安全容器利用硬件虚拟化来隔离容器沙箱，使专用的客户机内核能够缓解传统系统中普遍存在的共享内核攻击。然而，现有方法面临一个根本性权衡：基于虚拟机的方案（如Kata）优先考虑性能，但对易变且突发的工作负载缺乏弹性和按需使用能力；而轻量级方法（如gVisor）依赖宿主内核进行动态资源管理，却因客户机与宿主之间的依赖关系而付出显著的性能下降代价。

我们提出SKernel，一个经过生产验证的安全容器系统，它通过新颖的分裂内核架构化解了这一权衡。观察到I/O栈主导了云原生应用的性能，SKernel将客户机内核解耦为两个组件：SKernel-R（通过宿主协作进行资源管理）和SKernel-D（无需宿主参与的高性能I/O操作）。SKernel的关键创新包括：(1) 快速系统调用转发方法，最小化上下文切换开销；(2) 基于设备直通的网络栈，提供更好的兼容性与资源灵活性，并结合先进的线程模型和I/O通知机制以处理易变且突发的工作负载；(3) 基于文件描述符的容器文件系统，增强安全性、消除不必要的间接层并降低成本。宏基准测试评估表明，SKernel相较gVisor实现了4.49倍的吞吐量提升，同时具备与之相当的弹性。在生产工作负载下，SKernel相比runc降低了CPU使用率，在蚂蚁集团支持了跨40,000多个节点的2,000多个长期运行的微服务应用（含100,000多个安全容器）。作为一个兼具高效性与弹性的生产就绪安全容器，SKernel堪称一个里程碑。

**英文关键词：** Operating systems, Cloud computing, Virtualization, Secure Containers

**中文关键词：** 操作系统、云计算、虚拟化、安全容器

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
