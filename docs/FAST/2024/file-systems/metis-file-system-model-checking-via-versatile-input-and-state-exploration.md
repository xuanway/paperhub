---
title: "Metis: File System Model Checking via Versatile Input and State Exploration"
description: "FAST 2024 · File Systems · 第 123–140 页"
tags:
  - "FAST2024"
  - "File Systems"
---

# Metis: File System Model Checking via Versatile Input and State Exploration

**中文标题**：Metis：通过多样化输入与状态探索进行文件系统模型检查

**Session**：File Systems · 2024-02-27 15:45–17:00 · Chair：Peter Macko（MongoDB）

**作者**：Yifei Liu and Manish Adkar, Stony Brook University; Gerard Holzmann, Nimble Research; Geoff Kuenning, Harvey Mudd College; Pei Liu, Scott A. Smolka, Wei Su, and Erez Zadok, Stony Brook University

**会议**：FAST 2024 · Santa Clara, CA · 第 123–140 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/liu-yifei](https://www.usenix.org/conference/fast24/presentation/liu-yifei)

**论文 PDF**：[fast24-liu-yifei.pdf](https://www.usenix.org/system/files/fast24-liu-yifei.pdf)

---

## 英文摘要

We present *Metis*, a model-checking framework designed for versatile, thorough, yet configurable file system testing in the form of input and state exploration. It uses a nondeterministic loop and a weighting scheme to decide which system calls and their arguments to execute. Metis features a new *abstract state* representation for file-system states in support of efficient and effective state exploration. While exploring states, it compares the behavior of a file system under test against a reference file system and reports any discrepancies; it also provides support to investigate and reproduce any that are found. We also developed RefFS, a small, fast file system that serves as a reference, with special features designed to accelerate model checking and enhance bug reproducibility. Experimental results show that Metis can flexibly generate test inputs; also the rate at which it explores file-system states scales nearly linearly across multiple nodes. RefFS explores states 3–28× faster than other, more mature file systems. Metis aided the development of RefFS, reporting 11 bugs that we subsequently fixed. Metis further identified 12 bugs from five other file systems, five of which were confirmed and with one fixed and integrated into Linux.

## 中文摘要

我们提出 *Metis*，一个模型检查框架，旨在以输入和状态探索的形式进行多样、彻底且可配置的文件系统测试。它使用非确定性循环和加权方案来决定执行哪些系统调用及其参数。Metis 采用一种新的文件系统状态*抽象表示*，以支持高效且有效的状态探索。在探索状态时，它将被测文件系统的行为与参考文件系统进行比较，并报告任何差异；它还提供调查和复现所发现差异的支持。我们还开发了 RefFS，一个小型、快速的文件系统作为参考，其特殊功能旨在加速模型检查并增强缺陷可复现性。实验结果表明，Metis 能够灵活生成测试输入；此外，它探索文件系统状态的速率在多个节点上几乎线性扩展。RefFS 探索状态的速度比其他更成熟的文件系统快 3–28 倍。Metis 辅助了 RefFS 的开发，报告了我们随后修复的 11 个缺陷。Metis 还从另外五个文件系统中识别出 12 个缺陷，其中五个得到确认，一个已修复并集成到 Linux 中。
