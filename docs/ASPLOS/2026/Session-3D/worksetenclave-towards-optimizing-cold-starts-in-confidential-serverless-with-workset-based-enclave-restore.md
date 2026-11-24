---
title: "WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore"
description: "ASPLOS 2026 · Session 3D · WorksetEnclave：面向基于工作集的 enclave 恢复优化机密无服务器中的冷启动"
tags:
  - "ASPLOS2026"
  - "Session 3D"
  - "Trusted Execution Environments"
---

# WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore

**中文标题：** WorksetEnclave：面向基于工作集的 enclave 恢复优化机密无服务器中的冷启动

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xiaolong Yan (Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences), Qihang Zhou (Institute of Information Engineering, Chinese Academy of Sciences), Zisen Wan (Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences), Feifan Qian (Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences), Wentao Yao (Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences), Weijuan Zhang (Institute of Information Engineering, Chinese Academy of Sciences), Xiaoqi Jia (Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences)

**单位：** Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences；Institute of Information Engineering, Chinese Academy of Sciences

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790249) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Serverless computing has become a popular cloud computing paradigm. However, the increasing demand for data security in serverless applications necessitates the use of Trusted Execution Environments (TEEs) such as Intel Software Guard Extensions (SGX). Despite the promise of SGX for secure computation, its adoption in serverless environments is hindered by high startup latencies and excessive Enclave Page Cache (EPC) consumption, particularly during cold starts. This paper identifies the key challenges of SGX in serverless workloads and proposes WorksetEnclave, an efficient optimization method designed to address these issues. WorksetEnclave leverages a snapshot-based approach to optimize both startup time and enclave memory usage. By tracking workset pages used during execution, WorksetEnclave minimizes enclave memory footprints and significantly accelerates enclave restore time during secure checkpointing and recovery. We have implemented two separate prototypes, each based on a different LibOS: Gramine and Occlum. Our evaluation shows that WorksetEnclave accelerates cold start times by 1.9–54× and reduces enclave memory consumption by 13.37–94.87%. Our findings demonstrate that WorksetEnclave significantly improves the performance of confidential serverless.

## 中文摘要

无服务器计算已成为一种流行的云计算范式。然而，无服务器应用对数据安全日益增长的需求要求使用可信执行环境（TEE），例如 Intel 软件防护扩展（SGX）。尽管 SGX 在安全计算方面前景可期，但其在无服务器环境中的采用受到高启动延迟和过度的 Enclave 页缓存（EPC）消耗的阻碍，在冷启动期间尤为如此。本文识别了 SGX 在无服务器工作负载中的关键挑战，并提出 WorksetEnclave，一种旨在解决这些问题的有效优化方法。WorksetEnclave 利用基于快照的方法来同时优化启动时间和 enclave 内存使用。通过跟踪执行期间所使用的工作集页面，WorksetEnclave 最小化 enclave 内存占用，并在安全检查点与恢复过程中显著加速 enclave 恢复时间。我们实现了两个独立的原型，各自基于不同的 LibOS：Gramine 和 Occlum。我们的评估表明，WorksetEnclave 将冷启动时间加速 1.9–54 倍，并将 enclave 内存消耗降低 13.37–94.87%。我们的发现表明，WorksetEnclave 显著提升了机密无服务器的性能。

## 英文关键词

Confidential serverless; Cold starts; Snapshots

## 中文关键词

机密无服务器；冷启动；快照

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790249)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2026](../index.md)
