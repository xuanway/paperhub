---
title: "APT: Securing Against DRAM Read Disturbance via Adaptive Probabilistic In-DRAM Trackers"
description: "ASPLOS 2026 · Session 2D · APT：通过自适应概率式 DRAM 内跟踪器防御 DRAM 读干扰"
tags:
  - "ASPLOS2026"
  - "Session 2D"
  - "DRAM Reliability & Security"
---

# APT: Securing Against DRAM Read Disturbance via Adaptive Probabilistic In-DRAM Trackers

**中文标题：** APT：通过自适应概率式 DRAM 内跟踪器防御 DRAM 读干扰

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Runjin Wu (School of Computer Science & Technology, Huazhong University of Science and Technology, Wuhan, China), Meng Zhang (School of Computer Science & Technology, Huazhong University of Science and Technology, Wuhan, China), You Zhou (School of Computer Science & Technology, Huazhong University of Science and Technology, Wuhan, China), Changsheng Xie (Wuhan National Laboratory for Optoelectronics, Huazhong University of Science and Technology, Wuhan, China), Fei Wu (Wuhan National Laboratory for Optoelectronics, Huazhong University of Science and Technology, Wuhan, China)

**单位：** School of Computer Science & Technology, Huazhong University of Science and Technology, Wuhan, China；Wuhan National Laboratory for Optoelectronics, Huazhong University of Science and Technology, Wuhan, China

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790126) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

With exacerbated DRAM read disturbance, transparent inDRAM defenses require space (to track the aggressor rows) and time (to perform more mitigations). To reduce storage overhead, recent works have developed probabilistic rowsampling techniques with several entries. To address the time issue, these techniques employ Refresh Management (RFM) commands introduced in DDR5. However, probabilistic defenses with RFM face two critical challenges: (i) fixed-probability sampling under dynamic activation patterns can cause row-sampling misses, allowing attacks to evade mitigation, and (ii) RFM causes timing variations that can be exploited for side and covert channels to leak sensitive information. The goal of this paper is to design a low-cost and secure in-DRAM defense that overcomes these challenges. Our solution, APT (Adaptive Probabilistic In-DRAM Tracker), builds on two key insights. First, by ensuring that mitigation probabilities across activations always sum to 1, rowsampling misses can be prevented and the likelihood of capturing attacked rows can be improved. Second, as RFM is insecure, mitigation should exploit the unutilized slack within the refresh cycle (tRFC) while minimizing per-mitigation latency. APT adaptively allots equal sampling chances to all activations, based on real-time activation counts, avoiding sampling misses. To increase the mitigation rate without relying on RFM, we develop customizable Step Mitigation, which securely protects against transitive attacks with only two victim refreshes. Step Mitigation enables APT to perform up to three mitigations (APT-3) per periodic refresh (REF). We analytically derive the minimum RowHammer threshold tolerated by APT across all patterns. APT achieves a worstcase threshold of 694, which can be reduced to 228 using secure Timing-Based RFM (TB-RFM) at negligible overhead. We also show that APT compares favorably to TPRAC.

## 中文摘要

随着 DRAM 读干扰不断加剧，透明的 DRAM 内防御机制既需要空间（用于跟踪攻击者行），也需要时间（用于执行更多缓解操作）。为降低存储开销，近期工作提出了仅使用少量条目的概率式行采样技术。为解决时间开销问题，这些技术采用了 DDR5 引入的刷新管理（Refresh Management，RFM）命令。然而，采用 RFM 的概率式防御面临两个关键挑战：(i) 在动态激活模式下，固定概率采样可能导致行采样遗漏，使攻击得以规避缓解；(ii) RFM 会引起时序变化，这些变化可被侧信道和隐蔽信道利用以泄露敏感信息。本文的目标是设计一种低成本且安全的 DRAM 内防御机制，以克服上述挑战。我们的解决方案 APT（Adaptive Probabilistic In-DRAM Tracker，自适应概率式 DRAM 内跟踪器）基于两个关键洞见。第一，通过确保各次激活的缓解概率之和始终为 1，可以防止行采样遗漏，并提高捕获被攻击行的可能性。第二，由于 RFM 并不安全，缓解操作应利用刷新周期（tRFC）内未使用的空闲时间，同时尽量降低每次缓解的延迟。APT 根据实时激活计数，自适应地为所有激活分配均等的采样机会，从而避免采样遗漏。为在不依赖 RFM 的情况下提高缓解速率，我们设计了可定制的 Step Mitigation（分步缓解），它仅需两次受害者行刷新即可安全地防御传递性攻击。分步缓解使 APT 能够在每次周期性刷新（REF）中执行最多三次缓解（APT-3）。我们通过解析方法推导出 APT 在所有访问模式下所能容忍的最小 RowHammer 阈值。APT 的最坏情况阈值为 694，在开销可忽略的情况下，采用安全的基于时序的 RFM（Timing-Based RFM，TB-RFM）可将其降低至 228。我们还表明，APT 相比 TPRAC 具有优势。

## 英文关键词

DRAM; RowHammer; RowPress; Security

## 中文关键词

DRAM；RowHammer；RowPress；安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790126)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2026](../index.md)
