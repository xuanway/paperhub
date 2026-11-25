---
title: "LifeFuzz: Lifecycle-Guided Fuzzing for Windows Driver Cross-Handler Vulnerabilities"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Chendong Yu (Institute of Information Engineering, Chinese Academy of Sciences a"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# LifeFuzz: Lifecycle-Guided Fuzzing for Windows Driver Cross-Handler Vulnerabilities

**中文标题：** LifeFuzz：面向Windows驱动跨处理程序漏洞的生命周期引导模糊测试

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Chendong Yu (Institute of Information Engineering, Chinese Academy of Sciences and School of Cyber Security, University of Chinese Academy of Sciences), Yuekang Li (University of New South Wales), Yang Xiao (Chinese Academy of Sciences), Jie Lu (Institute of Computing Technology, Chinese Academy of Sciences), Yeting Li (Institute of Information Engineering, Chinese Academy of Sciences; University of Chinese Academy of Sciences), Defang Bo (Institute of Information Engineering, Chinese Academy of Sciences), Wei Huo (Key Laboratory of Network Assessment Technology, Institute of Information Engineering, Chinese Academy of Sciences, China; School of CyberSpace Security at University of Chinese Academy of Sciences, China)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803624)

## 英文摘要

Third-party Windows drivers expose a critical attack surface. However, vulnerabilities that require cross-handler I/O Control (IOCTL) sequences remain hard to find, despite their prevalence, and often lead to privilege escalation. Static analysis suffers from high false positives, path explosion, and complex resource modeling. Meanwhile, dynamic fuzzers often exercise handlers in isolation or combine them randomly, leaving implicit state dependencies unchecked. To address the gap, we present LifeFuzz, a lifecycle-guided fuzzing framework that models global-variable lifecycles to construct dependency-respecting IOCTL sequences. Specifically, it identifies variable operations across handlers, preserves seeds that affect driver state, and then combines them into meaningful sequences. Consequently, LifeFuzz explores deep paths unreachable for existing fuzzers. We evaluate LifeFuzz on 26 Windows WDM drivers. It discovers 86 vulnerabilities, including 32 cross-handler cases, with six assigned CVE IDs. Moreover, it finds 357% more cross-handler vulnerabilities than msFuzz and achieves 19.2% higher average coverage. Overall, 37% of discovered vulnerabilities require cross-handler interactions, thereby validating lifecycle-aware, cross-handler fuzzing for driver security.

## 中文摘要

第三方Windows驱动暴露了关键的攻击面。然而，需要跨处理程序I/O控制（IOCTL）序列才能触发的漏洞尽管普遍存在，却仍然难以发现，且往往导致权限提升。静态分析面临误报率高、路径爆炸和资源建模复杂的问题。同时，动态模糊测试器通常孤立地执行处理程序或随机组合它们，导致隐式状态依赖未被检查。为弥补这一空白，我们提出LifeFuzz，一个生命周期引导的模糊测试框架，它对全局变量生命周期建模，以构造遵循依赖关系的IOCTL序列。具体而言，它识别各处理程序中的变量操作，保留影响驱动状态的种子，然后将它们组合为有意义的序列。因此，LifeFuzz能够探索现有模糊测试器无法到达的深层路径。我们在26个Windows WDM驱动上评估LifeFuzz。它发现了86个漏洞，包括32个跨处理程序情形，其中6个获得CVE编号。此外，它发现的跨处理程序漏洞比msFuzz多357%，平均覆盖率提高19.2%。总体而言，所发现漏洞中有37%需要跨处理程序交互，从而验证了生命周期感知的跨处理程序模糊测试对驱动安全的价值。

**英文关键词：** Windows Driver, Cross-Handler Vulnerabilities, Global Variable Lifecycle Modeling

**中文关键词：** Windows驱动、跨处理程序漏洞、全局变量生命周期建模

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
