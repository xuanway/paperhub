---
title: "Turnstile: Hybrid Information Flow Control Framework for Managing Privacy in Internet-of-Things Applications"
description: "EuroSys 2026 · Edge Computing, IoT & Embedded AI · Kumseok Jung (University of British Columbia), Mohanna Shahrad (Princeton Univer"
tags:
  - "EuroSys2026"
  - "Edge Computing, IoT & Embedded AI"
---

# Turnstile: Hybrid Information Flow Control Framework for Managing Privacy in Internet-of-Things Applications

**中文标题：** Turnstile：面向物联网应用隐私管理的混合信息流控制框架

**所属 Session：** [Session 12.2: Edge Computing, IoT & Embedded AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Edge Computing, IoT & Embedded AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Edge Computing, IoT & Embedded AI</p>
</div>

**作者**：Kumseok Jung (University of British Columbia), Mohanna Shahrad (Princeton University), Gargi Mitra (University of British Columbia), Karthik Pattabiraman (University of British Columbia)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769352)

## 英文摘要

General awareness in privacy management has increased over the last decade, from consumers, companies, to governments. While cloud and mobile applications have taken steps forward in improving privacy management, the Internet-of-Things (IoT) domain has been behind in this aspect. Managing privacy in IoT applications is challenging, firstly because IoT applications handle data whose privacy implications change dynamically based on the information it contains. Second, the fragmented nature of the IoT ecosystem makes it difficult to apply a solution end-to-end. To provide a solution to privacy management in IoT, we design and implement Turnstile, a hybrid information flow control (IFC) framework. It identifies privacy-sensitive code paths through static taint analysis, and then integrates a dynamic information flow tracking (DIFT) mechanism into the application via selective code instrumentation. We evaluated Turnstile using 61 third-party IoT applications, and show that it can be an effective solution for managing the privacy of IoT applications.

## 中文摘要

过去十年间，从消费者、企业到政府对隐私管理的普遍意识不断增强。云计算与移动应用在改进隐私管理方面已取得进展，但物联网（IoT）领域在这方面相对滞后。IoT 应用中的隐私管理颇具挑战：首先，IoT 应用所处理数据的隐私影响会随其包含的信息而动态变化；其次，IoT 生态系统的碎片化特性使得端到端地应用某一方案十分困难。为提供 IoT 隐私管理方案，我们设计并实现了 Turnstile，一个混合信息流控制（IFC）框架。它通过静态污点分析识别隐私敏感的代码路径，然后通过选择性代码插桩将动态信息流跟踪（DIFT）机制集成到应用中。我们使用 61 个第三方 IoT 应用评估了 Turnstile，表明它能够成为管理 IoT 应用隐私的有效方案。

**英文关键词：** Dynamic Information Flow Control, Privacy Management, Internet of Things

**中文关键词：** 动态信息流控制、隐私管理、物联网

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
