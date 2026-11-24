---
title: "MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels"
description: "ASPLOS 2025 · Session 9D · MDPeek：利用内存消歧单元侧信道突破 SGX 中的平衡分支"
tags:
  - "ASPLOS2025"
  - "Session 9D"
  - "Trust"
---

# MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels

**中文标题：** MDPeek：利用内存消歧单元侧信道突破 SGX 中的平衡分支

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chang Liu (Tsinghua University), Shuaihu Feng (Zhongguancun Laboratory), Yuan Li (Zhongguancun Laboratory), Dongsheng Wang (Tsinghua University), Wenjian He (Huawei Technologies Co., Ltd.), Yongqiang Lyu (Tsinghua University), Trevor E. Carlson (National University of Singapore)

**单位：** Tsinghua University；Zhongguancun Laboratory；Huawei Technologies Co., Ltd.；National University of Singapore

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716004) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In recent years, control flow attacks targeting Intel SGX have attracted significant attention from the security community due to their potent capacity for information leakage. Although numerous software-based defenses have been developed to counter these attacks, many remain inadequate in fully addressing other, yet-to-be-discovered side channels. In this paper, we introduce MDPeek, a novel control flow attack targeting secret-dependent branches in SGX. To circumvent existing defenses, such as microarchitectural state flushing and branch balancing, we exploit a new leakage source, the Memory Disambiguation Unit (MDU). We present the first comprehensive reverse engineering on the MDU's enable and update logic. Based on our detailed analysis, we develop a methodology to identify vulnerable workloads in real-world applications. We demonstrate the effectiveness of MDPeek with end-to-end attacks on the latest versions of three SGX-secured applications, including Libjpeg, MbedTLS and WolfSSL. In addition, we propose a low-overhead mitigation technique, store-to-load coupling, which provides a 7× latency reduction compared to naive techniques like serialization and load aligning.

## 中文摘要

近年来，针对 Intel SGX 的控制流攻击因其强大的信息泄露能力而受到安全界的广泛关注。尽管已发展出许多基于软件的防御手段来对抗这些攻击，但其中许多仍不足以完全应对其他尚未被发现的侧信道。本文提出 MDPeek，一种针对 SGX 中依赖秘密的分支的新型控制流攻击。为绕过微体系结构状态刷新和分支平衡等现有防御，我们利用了一处新的泄露源——内存消歧单元（Memory Disambiguation Unit，MDU）。我们首次对 MDU 的使能逻辑与更新逻辑进行了全面的逆向工程。基于详细分析，我们提出了一套用于在真实应用中识别易受攻击负载的方法。我们通过对三个 SGX 保护应用（包括 Libjpeg、MbedTLS 和 WolfSSL）最新版本的端到端攻击，证明了 MDPeek 的有效性。此外，我们提出了一种低开销的缓解技术——存储-加载耦合（store-to-load coupling），与串行化和加载对齐等朴素技术相比可将延迟降低 7×。

## 英文关键词

side-channel attack; memory disambiguation unit; Intel SGX; hardware security

## 中文关键词

侧信道攻击；内存消歧单元；Intel SGX；硬件安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716004)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2025](../index.md)
