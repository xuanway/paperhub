---
title: "Intermittence-Aware Speculative Page Coloring for Secure NVM"
description: "ISCA 2026 · Session 5C · Intermittence-Aware Speculative Page Coloring for Secure NVM"
tags:
  - "ISCA2026"
  - "Session 5C"
  - "Crypto and Security"
---

# Intermittence-Aware Speculative Page Coloring for Secure NVM

**中文标题：** 面向安全 NVM 的间歇性感知推测式页着色

**所属 Session：** [Session 5C](index.md) · [ISCA 2026](../index.md)

**作者：** Jongouk Choi, Junyeong Park, Nicholas L’Heureux, Yan Solihin, Hyunwoo Joe, Changhee Jung

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

This paper revisits volatile scratchpad memory (SPM) for data confidentiality in an energy harvesting system (EHS) that suffers frequent power outages and thus features nonvolatile memory (NVM). Our insight is that low-cost data confidentiality can be achieved by using on-chip SPM as main memory and off-chip NVM as secondary storage. This strategic design naturally provides EHS with secure main memory (as SPM data vanish on an outage), encrypting them only when persistent in NVM. To realize this in a purely software manner, we introduce MANATEE, a compiler-directed memory management scheme that logically structures NVM pages and preallocates them in SPM. A key innovation of MANATEE is its intermittence-aware speculative page coloring that is explicitly designed taking into account frequent power outages. This design limits the requirement for page conflict resolution to the typically brief power-on period of EHS, providing greater flexibility in page coloring. If the period is longer than usual, two pages that would have been separated by an outage may instead be accessed within the same cycle, competing for the same SPM frame. To handle such a page miss (misspeculation), MANATEE devises page manager runtime that evicts the old SPM frame, encrypting and persisting it, and fetches the new NVM page decrypting it upon retrieval. Our evaluation shows that the page miss rate is not significant (≈1%), and MANATEE delivers a 2–3× speedup over the state-of-the-art work. These results demonstrate that MANATEE enables practical and secure memory for EHS, providing data confidentiality with minimal performance overhead.

## 中文摘要

本文重新审视了在能量采集系统（EHS）中利用易失性便签存储器（SPM）保障数据机密性的做法——此类系统常遭遇频繁断电，因而采用非易失性存储器（NVM）。我们的洞见是：将片上 SPM 用作主存、片外 NVM 用作二级存储，即可实现低成本的数据机密性。这一策略性设计天然为 EHS 提供了安全的主存（因为 SPM 中的数据在断电时消失），仅在数据需持久保存于 NVM 时才加密。为以纯软件方式实现这一点，我们提出 MANATEE——一种由编译器指导的内存管理方案，它对 NVM 页面进行逻辑结构化，并预先分配在 SPM 中。MANATEE 的一项关键创新是间歇性感知的推测式页着色（intermittence-aware speculative page coloring），其设计明确考虑了频繁断电的情形。该设计将页面冲突消解的需求限制在 EHS 通常短暂的加电期间，从而为页着色带来更大的灵活性。如果该期间比通常更长，本应被一次断电隔开的两个页面可能在同一周期内被访问，从而竞争同一 SPM 帧。为处理此类页面缺失（推测失败），MANATEE 设计了页管理器运行时：它逐出旧的 SPM 帧、对其加密并持久化，同时取入新的 NVM 页面并在取入时解密。我们的评估显示，页面缺失率并不显著（约 1%），且 MANATEE 相比最先进工作实现 2–3× 的加速。这些结果表明，MANATEE 为 EHS 提供了实用且安全的内存，以极小的性能开销实现了数据机密性。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2026](../index.md)
