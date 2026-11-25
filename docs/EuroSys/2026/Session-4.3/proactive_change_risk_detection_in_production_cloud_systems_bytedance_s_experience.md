---
title: "Proactive Change Risk Detection in Production Cloud Systems: ByteDance’s Experience"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Jinyang Liu (ByteDance), Yichen Li (ByteDance), Tieying Zhang (ByteDance), Binbi"
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# Proactive Change Risk Detection in Production Cloud Systems: ByteDance’s Experience

**中文标题：** 生产云系统中的主动变更风险检测：字节跳动的经验

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Jinyang Liu (ByteDance), Yichen Li (ByteDance), Tieying Zhang (ByteDance), Binbin Chen (ByteDance), Xiao He (ByteDance), Zhihan Jiang (ByteDance), Haipeng Zhang (ByteDance), Gang Wu (ByteDance), Yi Li (ByteDance)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803614)

## 英文摘要

Modern cloud services rely on a high volume of changes for rapid innovation, yet these changes are a primary cause of production incidents. To manage this risk, industry practice employs tiered change management pipelines that concentrate static rules and human reviews. However, our analysis of ByteDance’s cloud platform (Volcano Engine) reveals a critical long tail problem: while high-risk changes undergo extensive scrutiny, 78.1% of change-induced incidents originate from the sheer volume of low-risk changes that receive minimal review. At this scale, exhaustive manual review is fundamentally infeasible. To address this, we present Aegis, a novel knowledge-driven system that provides interpretable change risk assessment. Aegis automatically constructs a knowledge base from historical operational data, distilling it into generalized risk heuristics and identifying relevant precedent cases. When a new change is proposed, Aegis generates human-readable warnings grounded in this historical evidence, explaining why a change is risky. We have deployed Aegis in Volcano Engine’s production environment for five months, where it processed tens of thousands of change requests. Its risk escalations achieved a 75% acceptance rate from production engineers and successfully prevented multiple potential incidents.

## 中文摘要

现代云服务依赖大量变更来实现快速创新，但这些变更也是生产事故的主要成因。为管理这一风险，业界实践采用分层变更管理流程，将静态规则与人工评审集中起来。然而，我们对字节跳动云平台（火山引擎）的分析揭示了一个严峻的长尾问题：虽然高风险变更会接受充分审查，但 78.1% 的变更引发事故源自数量庞大、审查极少的低风险变更。在这一规模下，穷尽式人工评审从根本上不可行。为此，我们提出 Aegis，一个新颖的知识驱动系统，可提供可解释的变更风险评估。Aegis 从历史运维数据中自动构建知识库，将其提炼为泛化的风险启发式规则，并识别相关的先例案例。当有新变更提出时，Aegis 生成以这些历史证据为依据、人类可读的告警，解释该变更为何有风险。我们已在火山引擎生产环境部署 Aegis 五个月，其间处理了数万条变更请求。其风险升级获得生产工程师 75% 的采纳率，并成功阻止了多起潜在事故。

**英文关键词：** change management, risk detection, cloud systems, LLM, production deployment

**中文关键词：** 变更管理、风险检测、云系统、LLM、生产部署

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
