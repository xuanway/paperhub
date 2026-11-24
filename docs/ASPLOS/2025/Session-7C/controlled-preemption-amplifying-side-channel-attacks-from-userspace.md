---
title: "Controlled Preemption: Amplifying Side-Channel Attacks from Userspace"
description: "ASPLOS 2025 · Session 7C · 受控抢占：从用户态放大侧信道攻击"
tags:
  - "ASPLOS2025"
  - "Session 7C"
  - "Side Channels"
---

# Controlled Preemption: Amplifying Side-Channel Attacks from Userspace

**中文标题：** 受控抢占：从用户态放大侧信道攻击

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yongye Zhu (University of California, Berkeley), Boru Chen (University of California, Berkeley), Zirui Neil Zhao (NVIDIA,UT Austin), Christopher W. Fletcher (University of California, Berkeley)

**单位：** University of California, Berkeley；NVIDIA,UT Austin

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715985) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Microarchitectural side channels are an ongoing threat in today's systems. Yet, many side-channel methodologies suf- fer from low temporal resolution measurement, which can either preclude or significantly complicate an attack. This paper introduces Controlled Preemption, an attack primitive enabling a single unprivileged (user-level) attacker thread to repeatedly preempt a victim thread after colocat- ing with that victim thread on the same logical core. Be- tween preemptions, the victim thread executes zero to sev- eral instructions—sufficiently few to enable high-resolution side channel measurements. The key idea in Controlled Preemption is to exploit sched- uler fairness heuristics. Namely, that modern thread sched- ulers give a thread 𝐴the ability to preempt another thread 𝐵 until a fairness tripwire (signaling that 𝐴is starving 𝐵) fires. We show how this idea enables hundreds of short preemp- tions before tripping the fairness tripwire is robust to noise and applies to both the Linux CFS and EEVDF schedulers. We also develop a technique that helps colocate the attacker and victim threads onto the same logical core, an attacker capability overlooked by prior work. Our evaluation tests Controlled Preemption in the context of several different victim programs, victim privilege levels (inside and outside of Intel SGX) and choices of side channel. In each attack, we demonstrate results that are competitive with prior work but make fewer assumptions (e.g., require only user-level privilege or require fewer colocated attacker threads).

## 中文摘要

微架构侧信道是当今系统中持续存在的威胁。然而，许多侧信道方法受制于低时间分辨率的测量，这可能阻止攻击，或显著增加攻击的复杂度。本文提出受控抢占（Controlled Preemption），这是一种攻击原语，使单个无特权（用户级）攻击者线程在与受害线程共置于同一逻辑核之后，能够反复抢占该受害线程。在两次抢占之间，受害线程执行零到若干条指令——少到足以支持高分辨率的侧信道测量。受控抢占的关键思想是利用调度器的公平性启发式规则。即，现代线程调度器赋予线程 A 抢占另一线程 B 的能力，直到公平性触发器（表示 A 正在使 B 饥饿）被触发。我们展示了这一思想如何在触发公平性触发器之前实现数百次短抢占，并且该手法具有抗噪性，适用于 Linux CFS 与 EEVDF 两种调度器。我们还开发了一种技术，帮助将攻击者线程与受害线程共置到同一逻辑核上，这是先前工作所忽视的一种攻击者能力。我们的评估在若干不同受害程序、不同受害特权级别（Intel SGX 内外）以及不同侧信道选择的背景下测试了受控抢占。在每一次攻击中，我们展示的结果都与先前工作具有竞争力，但所依赖的假设更少（例如仅需用户级特权，或需要更少的共置攻击者线程）。

## 英文关键词

Microarchitectural side-channel attacks; Attack primitives; Temporal resolution; Completely Fair Scheduler; Earliest Eligible Virtual Deadline First Scheduler

## 中文关键词

微架构侧信道攻击；攻击原语；时间分辨率；完全公平调度器；最早合格虚拟截止时间优先调度器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715985)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2025](../index.md)
