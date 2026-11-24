---
title: "CXLfork: Fast Remote Fork over CXL Fabrics"
description: "ASPLOS 2025 · Session 2B · CXLfork：基于 CXL 互联结构的快速远程 fork"
tags:
  - "ASPLOS2025"
  - "Session 2B"
  - "Distributed Computing"
---

# CXLfork: Fast Remote Fork over CXL Fabrics

**中文标题：** CXLfork：基于 CXL 互联结构的快速远程 fork

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chloe Alverti (University of Illinois Urbana-Champaign), Stratos Psomadakis (National Technical University of Athens), Burak Ocalan (University of Illinois Urbana-Champaign), Shashwat Jaiswal (University of Illinois Urbana-Champaign), Tianyin Xu (University of Illinois Urbana-Champaign), Josep Torrellas (University of Illinois Urbana-Champaign)

**单位：** University of Illinois Urbana-Champaign；National Technical University of Athens

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715988) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The shared and distributed memory capabilities of the emerging Compute Express Link (CXL) interconnect urge us to rethink the traditional interfaces of system software. In this paper, we explore one such interface: remote fork using CXLattached shared memory for cluster-wide process cloning. We present CXLfork, a remote fork interface that realizes close to zero-serialization, zero-copy process cloning across nodes over CXL fabrics. CXLfork utilizes globally-shared CXL memory for cluster-wide deduplication of process states. It also enables fine-grained control of state tiering between local and CXL memory. We use CXLfork to develop CXLporter, an efficient horizontal autoscaler for serverless functions deployed on CXL fabrics. CXLfork minimizes cold-start overhead without sacrificing local memory. CXLfork attains restore latency close to that of a local fork, outperforming state-of-practice by 2.26x on average, and reducing local memory consumption by 87% on average.

## 中文摘要

新兴的 Compute Express Link（CXL）互连所提供的共享与分布式内存能力，促使我们重新思考系统软件的传统接口。本文探讨其中一种接口：利用 CXL 挂载的共享内存进行远程 fork，以实现集群范围的进程克隆。我们提出 CXLfork，一种远程 fork 接口，可在 CXL 互联结构上实现跨节点的接近零序列化、零拷贝的进程克隆。CXLfork 利用全局共享的 CXL 内存，实现集群范围的进程状态去重。它还支持在本地内存与 CXL 内存之间对状态分层进行细粒度控制。我们使用 CXLfork 开发了 CXLporter，一个面向部署在 CXL 互联结构上的无服务器函数的高效水平自动扩缩器。CXLfork 在不牺牲本地内存的前提下将冷启动开销降至最低。CXLfork 的恢复延迟接近本地 fork，平均优于当前实践 2.26 倍，并将本地内存消耗平均降低 87%。

## 英文关键词

CXL, Process forking, Remote memory, Checkpoint restore, Serverless computing, Cold start

## 中文关键词

CXL；进程 fork；远程内存；检查点恢复；无服务器计算；冷启动

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715988)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2025](../index.md)
