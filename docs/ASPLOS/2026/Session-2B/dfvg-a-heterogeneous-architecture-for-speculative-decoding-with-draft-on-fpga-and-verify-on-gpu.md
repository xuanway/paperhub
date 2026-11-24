---
title: "DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU"
description: "ASPLOS 2026 · Session 2B · DFVG：一种采用 FPGA 起草与 GPU 验证的投机解码异构架构"
tags:
  - "ASPLOS2026"
  - "Session 2B"
  - "Speculative Decoding"
---

# DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU

**中文标题：** DFVG：一种采用 FPGA 起草与 GPU 验证的投机解码异构架构

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Shaoqiang Lu (Shanghai Jiao Tong University, Shanghai, China and Eastern Institute of Technology, Ningbo, China), Yangbo Wei (Shanghai Jiao Tong University, Shanghai, China and Eastern Institute of Technology, Ningbo, China), Junhong Qian (Southest University, Nanjin, China), Dongge Qin (Southest University, Nanjin, China), Shiji Gao (Southest University, Nanjin, China), Yizhi Ding (Southest University, Nanjin, China), Qifan Wang (Shanghai Jiao Tong University, Shanghai, China and Eastern Institute of Technology, Ningbo, China), Chen Wu (Ningbo Institute of Digital Twin，Eastern Institute of Technology , Ningbo, China), Xiao Shi (Southest University, Nanjin, China), Lei He (Eastern Institute of Technology, Ningbo, China)

**单位：** Shanghai Jiao Tong University, Shanghai, China and Eastern Institute of Technology, Ningbo, China；Southest University, Nanjin, China；Ningbo Institute of Digital Twin，Eastern Institute of Technology , Ningbo, China；Eastern Institute of Technology, Ningbo, China

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790153) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Speculative decoding is a promising paradigm that accelerates LLM inference by generating drafts and performing verification. However, such systems still face three major challenges: (1) The imbalance in resource requirements between draft and verification models result in low utilization and energy inefficiency when deployed together. (2) Fixed-pattern token trees produce many candidates but few valid paths, resulting in redundant drafts due to the lack of full leverage of the inherent confidence in dynamic generation. (3) Asynchronous execution with frequent alternation between the two stages suffers from idle waiting and rollback overhead. To address these issues, we propose DFVG, a heterogeneous speculative decoding architecture that offloads draft generation to FPGAs and verification to GPUs, exploiting their complementary strengths. We introduce three key contributions: tion 4. (1) Heterogeneous architecture design that partitions speculative decoding into FPGA-based drafting and GPU-based verification, exploiting complementary hardware strengths with an overlap processor for high-throughput execution; (2) Hardware-aware dynamic draft generation that dynamically predicts speculative branches and token lengths based on model confidence while considering hardware parallelism limits; (3) Tightly-coupled heterogeneous pipeline with stage-decoupled scheduling that allocates execution windows between stages, combined with lightweight cross-device alignment and rollback prediction strategies. Comprehensive evaluation on mainstream models (OPT, LLaMA, Qwen) demonstrates DFVG achieves up to 3.26× speedup and 5.8× energy efficiency improvement over existing approaches.

## 中文摘要

投机解码是一种颇具前景的范式，它通过生成草稿并执行验证来加速 LLM 推理。然而，此类系统仍面临三大挑战：(1) 草稿模型与验证模型在资源需求上的不均衡，导致二者共同部署时利用率低且能效差。(2) 固定模式的 token 树会产生大量候选，但有效路径很少，由于未能充分利用动态生成中固有的置信度，导致草稿冗余。(3) 两个阶段之间频繁交替的异步执行会遭受空闲等待与回滚开销。为解决这些问题，我们提出 DFVG，一种异构投机解码架构，它将草稿生成卸载到 FPGA、将验证卸载到 GPU，从而利用二者互补的优势。我们引入三项关键贡献：(1) 异构架构设计，将投机解码划分为基于 FPGA 的起草与基于 GPU 的验证，利用互补的硬件优势，并通过重叠处理器实现高吞吐执行；(2) 硬件感知的动态草稿生成，基于模型置信度动态预测投机分支与 token 长度，同时考虑硬件并行度限制；(3) 紧耦合的异构流水线，采用阶段解耦调度在各阶段之间分配执行窗口，并结合轻量级跨设备对齐与回滚预测策略。在主流模型（OPT、LLaMA、Qwen）上的综合评估表明，DFVG 相比现有方法最高实现 3.26× 加速和 5.8× 能效提升。

## 英文关键词

Speculative Decoding; Heterogeneous Computing; FPGA Acceleration; Software Hardware Co-design

## 中文关键词

投机解码；异构计算；FPGA 加速；软硬件协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790153)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2026](../index.md)
