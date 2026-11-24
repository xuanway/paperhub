---
title: "LIPPEN: A Lightweight In-Place Pointer Encryption Architecture for Pointer Integrity"
description: "ISCA 2026 · Session 5C · LIPPEN: A Lightweight In-Place Pointer Encryption Architecture for Pointer Integrity"
tags:
  - "ISCA2026"
  - "Session 5C"
  - "Crypto and Security"
---

# LIPPEN: A Lightweight In-Place Pointer Encryption Architecture for Pointer Integrity

**中文标题：** LIPPEN: 面向指针完整性的轻量级原位指针加密架构

**所属 Session：** [Session 5C](index.md) · [ISCA 2026](../index.md)

**作者：** Erfan Iravani, Lalit Prasad Peri, Mohannad Ismail, Charitha Tumkur Siddalingaradhya, Changwoo Min, Elif Bilge Kavun, Wenjie Xiong

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory-safety vulnerabilities in C and C++ programs continue to enable sophisticated exploitations such as control-flow hijacking and data-oriented attacks. Existing hardware defenses either rely on address space layout randomization or explicit metadata to pointers to verify the integrity. Many mitigation techniques introduce external metadata for security checks, providing strong guarantees, but incur additional memory accesses and memory footprint overhead. In-place protection schemes, such as ARM Pointer Authentication (PAC), achieve low overhead but have limited entropy for security and are susceptible to brute-force attacks. This paper presents LIPPEN, a hardware–software co-design for full-pointer encryption that provides strong pointer integrity without metadata. LIPPEN encrypts every pointer with a block cipher, cryptographically binding it to its execution context, and decrypts it transparently at dereference time. By re-purposing the entire 64-bit pointer field for encryption rather than preserving raw address bits, LIPPEN maximizes entropy, eliminates the brute-force weaknesses of truncated authentication codes, and maintains binary compatibility with existing PAC-enabled software protection. We prototype LIPPEN on FPGA using 64-bit RISC-V Rocket and BOOM cores, and evaluate it with microbenchmarks, nbench, and SPEC CPU2017. We compare against both an in-house PAC implementation on RISC-V and Apple’s PAC on the M1 processor. Across these workloads, LIPPEN provides comprehensive pointer protection with comparable or better runtime overhead to PAC-based schemes, while incurring negligible area and power overhead. These results show that LIPPEN is a practical design point for deploying strong pointer protection in real processors.

## 中文摘要

C 与 C++ 程序中的内存安全漏洞持续被用于实施诸如控制流劫持和面向数据攻击等精巧的利用手法。现有的硬件防御要么依赖地址空间布局随机化，要么依赖为指针附加显式元数据来验证完整性。许多缓解技术会引入外部元数据以进行安全检查，提供了强保证，却带来额外的内存访问与内存占用开销。原位（in-place）保护方案（如 ARM 指针认证 PAC）开销较低，但用于安全的熵有限，易受暴力破解攻击。本文提出 LIPPEN，一种软硬件协同设计的全指针加密方案，无需元数据即可提供强指针完整性。LIPPEN 使用分组密码对每个指针加密，将其在密码学上绑定到其执行上下文，并在解引用时透明地解密。通过将完整的 64 位指针字段重新用于加密（而非保留原始地址比特），LIPPEN 最大化了熵，消除了截断认证码的暴力破解弱点，并与现有启用了 PAC 的软件保护保持二进制兼容。我们在 FPGA 上使用 64 位 RISC-V Rocket 与 BOOM 核构建了 LIPPEN 原型，并用微基准测试、nbench 和 SPEC CPU2017 对其进行评估。我们将它与 RISC-V 上自行实现的 PAC 以及 Apple M1 处理器上的 PAC 进行对比。在这些负载上，LIPPEN 提供了全面的指针保护，其运行时开销与基于 PAC 的方案相当或更优，同时面积与功耗开销可忽略。这些结果表明，LIPPEN 是在真实处理器中部署强指针保护的一个实用设计点。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：bearhw/LIPPEN](https://github.com/bearhw/LIPPEN)
- [实验材料归档（Zenodo 19901476）](https://zenodo.org/records/19901476)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2026](../index.md)
