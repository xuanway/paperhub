---
title: "Lessons Learned from Incorporating Formal Methods in Huawei Cloud Reliability"
description: "EuroSys 2026 · Cloud · Claudia Cauli (Huawei Technologies Co., Ltd, Ireland), Timo Lang (Huawei Technol"
tags:
  - "EuroSys2026"
  - "Cloud"
---

# Lessons Learned from Incorporating Formal Methods in Huawei Cloud Reliability

**中文标题：** 在华为云可靠性中引入形式化方法的经验教训

**所属 Session：** [Session 9.1: Cloud](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud</p>
</div>

**作者**：Claudia Cauli (Huawei Technologies Co., Ltd, Ireland), Timo Lang (Huawei Technologies Co., Ltd, Ireland), Shuo Chen (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Sebti Mouelhi (Huawei Technologies Co., Ltd, Ireland), Xin Jin (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Subhajit Bandopadhyay (Huawei Technologies Co., Ltd, Ireland), Xusheng Chen (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Yazhi Feng (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Haoze Song (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Linhua Tang (Huawei Technologies Co., Ltd, Ireland), Zhenli Sheng (Huawei Technologies Co., Ltd., Shenzhen, Guangdong, China), Ananth Shrinivas Srinath (Huawei Technologies Co., Ltd, Ireland)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803626)

## 英文摘要

Formal methods are increasingly adopted in systems where reliability and correctness are critical, enabled by improvements in tool usability, speed, and automation. This industrial experience report presents three projects at Huawei Cloud showcasing different trade-offs in investment and assurance levels. We applied probabilistic concurrency testing, model checking, and deductive verification to two foundational services in the database and networking domains: the K2 transactional key-value store and the Global Server Load Balancer (GSLB).

Our work discovered bugs across different system layers— from design to implementation—which led to enhanced reliability, protocol simplifications, improved understanding, and generally higher developer confidence.

To support practical adoption, we provide empirical and anecdotal data—including person-month effort metrics, tool comparisons, and success patterns—enabling engineering teams to make informed decisions about which approaches to invest in, when to apply lightweight versus heavyweight techniques, and how to budget for formal methods adoption in their organisation.

## 中文摘要

随着工具在易用性、速度与自动化方面的改进，形式化方法正越来越多地被可靠性至关重要的系统所采用。本工业经验报告介绍华为云的三个项目，展示了在投入与保障水平上的不同权衡。我们将概率并发测试、模型检验与演绎验证应用于数据库和网络领域的两个基础服务：K2 事务型键值存储与全局服务器负载均衡器（GSLB）。

我们的工作在从设计到实现的多个系统层次上发现了缺陷，从而提升了可靠性、简化了协议、增进了理解，并普遍提高了开发者的信心。

为支持实际落地，我们提供了实证与轶事性数据——包括人月工作量指标、工具对比与成功模式——使工程团队能够就投入哪些方法、何时采用轻量级与重量级技术，以及如何为组织内的形式化方法落地做预算，做出明智决策。

**英文关键词：** Industrial Experience, Formal Methods, Cloud Reliability

**中文关键词：** 工业经验、形式化方法、云可靠性

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
