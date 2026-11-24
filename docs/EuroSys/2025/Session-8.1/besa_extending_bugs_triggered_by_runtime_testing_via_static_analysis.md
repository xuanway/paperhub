---
title: "BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis"
description: "EuroSys 2025 · Bug finding · Jia-Ju Bai (Beihang University)"
tags:
  - "EuroSys2025"
  - "Bug finding"
---

# BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis

**中文标题：** 通过静态分析扩展运行时测试触发的缺陷

**所属 Session：** [Session 8.1: Bug finding](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Bug finding。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Bug finding</p>
</div>

**作者**：Jia-Ju Bai (Beihang University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696089)

## 英文摘要

Due to limited test cases and execution scenarios, runtime testing often has insufficient code coverage and thus misses many real bugs. To tackle this problem, we propose a novel idea that static analysis of the triggered bug in runtime testing can help extend and detect extra bugs missed by runtime testing. Based on this idea, we develop a new approach named BESA, which can extend null-pointer dereferences found by runtime testing via static analysis. It first collects trace information about the triggered bug in runtime testing, by monitoring PoC (Proof of Concept) execution or analyzing existing failure log. Then, with this trace information, BESA uses a backward propagation analysis based on the call stack of the triggered bug, to effectively identify source variables propagating problematic value to the buggy variable. Finally, according to each source variable, BESA uses a summary-based alias-aware analysis to efficiently track target variables aliased with the buggy variable for detecting extra bugs. We have evaluated BESA on 25 known null-pointer dereferences found by runtime testing in four popular programs (SQLite, VIM, GPAC and Linux kernel). BESA finds 57 extra bugs, and 18 of them are new bugs that have been confirmed.

## 中文摘要

由于测试用例和执行场景有限，运行时测试往往代码覆盖率不足，从而漏掉许多真实缺陷。为解决这一问题，我们提出一个新思路：对运行时测试所触发缺陷进行静态分析，有助于扩展并检测出运行时测试遗漏的额外缺陷。基于这一思路，我们开发了名为 BESA 的新方法，它能够通过静态分析扩展运行时测试发现的空指针解引用缺陷。BESA 首先通过监控 PoC（Proof of Concept）执行或分析已有的失败日志，收集运行时测试所触发缺陷的跟踪信息。随后，借助这些跟踪信息，BESA 基于该缺陷的调用栈进行反向传播分析，以有效识别将问题值传播到缺陷变量的源变量。最后，针对每个源变量，BESA 使用基于摘要的别名感知分析，高效追踪与缺陷变量互为别名的目标变量，从而检测出更多缺陷。我们在四个流行程序（SQLite、VIM、GPAC 和 Linux 内核）中由运行时测试发现的 25 个已知空指针解引用上评估了 BESA。BESA 发现了 57 个额外缺陷，其中 18 个是已获确认的新缺陷。

**英文关键词：** Runtime Testing, Static Analysis, Bug Detection, Alias Analysis

**中文关键词：** 运行时测试、静态分析、缺陷检测、别名分析

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
