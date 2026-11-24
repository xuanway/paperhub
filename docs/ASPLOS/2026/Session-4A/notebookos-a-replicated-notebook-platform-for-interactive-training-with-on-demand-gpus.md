---
title: "NotebookOS: A Replicated Notebook Platform for Interactive Training with On-Demand GPUs"
description: "ASPLOS 2026 · Session 4A · NotebookOS：一个面向按需 GPU 交互式训练的复制笔记本平台"
tags:
  - "ASPLOS2026"
  - "Session 4A"
  - "ML Training & Monitoring"
---

# NotebookOS: A Replicated Notebook Platform for Interactive Training with On-Demand GPUs

**中文标题：** NotebookOS：一个面向按需 GPU 交互式训练的复制笔记本平台

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Benjamin Carver (George Mason University), Jingyuan Zhang (George Mason University), Haoliang Wang (Adobe Research), Kanak Mahadik (Adobe Research), Yue Cheng (University of Virginia)

**单位：** George Mason University；Adobe Research；University of Virginia

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762230) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Interactive notebook programming is universal in modern ML and AI workflows, with interactive deep learning training (IDLT) emerging as a dominant use case. To ensure responsiveness, platforms like Jupyter and Colab reserve GPUs for long-running notebook sessions, despite their intermittent and sporadic GPU usage, leading to extremely low GPU utilization and prohibitively high costs. In this paper, we introduce NotebookOS, a GPU-efficient notebook platform tailored for the unique requirements of IDLT. NotebookOS employs replicated notebook kernels with Raft-synchronized replicas distributed across GPU servers. To optimize GPU utilization, NotebookOS oversubscribes server resources, leveraging high inter-arrival times in IDLT workloads, and allocates GPUs only during active cell execution. It also supports replica migration and automatic cluster scaling under high load. Altogether, this design enables interactive training with minimal delay. In evaluation on production workloads, NotebookOS saved over 1,187 GPU hours in 17.5 hours of real-world IDLT, while significantly improving interactivity.

## 中文摘要

交互式笔记本编程在现代机器学习和 AI 工作流中已十分普遍，交互式深度学习训练（IDLT）正成为其中的主流用例。为保证响应性，Jupyter 和 Colab 等平台会为长时间运行的笔记本会话预留 GPU，尽管这些会话的 GPU 使用是间歇性、零散的，从而导致 GPU 利用率极低且成本高得难以承受。本文提出 NotebookOS，一个针对 IDLT 的独特需求而量身定制的 GPU 高效笔记本平台。NotebookOS 采用复制的笔记本内核，其副本通过 Raft 同步并分布于多台 GPU 服务器之上。为优化 GPU 利用率，NotebookOS 超额订阅服务器资源，利用 IDLT 工作负载中较高的到达间隔时间，并且仅在单元格活跃执行期间分配 GPU。它还支持副本迁移以及高负载下的自动集群伸缩。总之，该设计使得以极小延迟进行交互式训练成为可能。在生产工作负载的评估中，NotebookOS 在 17.5 小时的真实 IDLT 中节省了超过 1,187 个 GPU 小时，同时显著提升了交互性。

## 英文关键词

Jupyter Notebook; Interactive Deep Learning Training; GPU Scheduling; Systems for AI

## 中文关键词

Jupyter Notebook；交互式深度学习训练；GPU 调度；面向 AI 的系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762230)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2026](../index.md)
