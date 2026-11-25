---
title: "AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding"
description: "EuroSys 2026 · AI · Zikun Li (Carnegie Mellon University), Zhuofu Chen (Princeton University), Remi "
tags:
  - "EuroSys2026"
  - "AI"
---

# AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding

**中文标题：** AdaServe：以 SLO 定制化投机解码加速多 SLO 的 LLM 服务

**所属 Session：** [Session 5.1: AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · AI</p>
</div>

**作者**：Zikun Li (Carnegie Mellon University), Zhuofu Chen (Princeton University), Remi Delacourt (EPFL), Gabriele Oliaro (Carnegie Mellon University), Zeyu Wang (Carnegie Mellon University), Qinghan Chen (Carnegie Mellon University), Shuhuai Lin (Carnegie Mellon University), April Yang (Carnegie Mellon University), Zhihao Zhang (Carnegie Mellon University), Zhuoming Chen (Carnegie Mellon University), Yi-Hsiang Lai (Amazon Web Services), Xinhao Cheng (Carnegie Mellon University), Xupeng Miao (Purdue University), Zhihao Jia (Carnegie Mellon University and Amazon Web Services)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769315)

## 英文摘要

Modern large language model (LLM) applications exhibit diverse service-level objectives (SLOs), from low-latency requirements in interactive coding assistants to more relaxed constraints in data wrangling tasks. Existing LLM serving systems, which rely on uniform batching and scheduling strategies, often fail to meet these heterogeneous SLOs concurrently. We present AdaServe, the first LLM serving system designed to support efficient multi-SLO serving through SLO-customized speculative decoding. AdaServe formulates multi-SLO serving as a constrained optimization problem and introduces a hardware-aware algorithm that constructs a speculation tree tailored to each request’s latency target. It features a speculate-select-verify pipeline that enables fine-grained control over decoding speed while maximizing system throughput. AdaServe further adapts to workload variation by dynamically adjusting speculation parameters. Evaluations across diverse workloads show that AdaServe reduces SLO violations by up to 4.3× and improves goodput by up to 1.9× compared to the best-performing baselines, highlighting its effectiveness in multi-SLO serving.

## 中文摘要

现代大语言模型（LLM）应用呈现出多样化的服务等级目标（SLO），从交互式编程助手的低延迟要求，到数据整理任务中更为宽松的约束。现有 LLM 服务系统依赖统一的批处理与调度策略，往往无法同时满足这些异构的 SLO。我们提出 AdaServe，这是首个通过 SLO 定制化投机解码来支持高效多 SLO 服务的 LLM 服务系统。AdaServe 将多 SLO 服务建模为受约束的优化问题，并引入一种硬件感知算法，为每个请求的延迟目标构建定制的投机树。它采用“投机-选择-验证”流水线，在最大化系统吞吐的同时对解码速度实现细粒度控制。AdaServe 还通过动态调整投机参数来适应工作负载变化。在多种工作负载上的评估表明，与表现最佳的基线相比，AdaServe 将 SLO 违约率最多降低 4.3 倍，并将有效吞吐（goodput）最高提升 1.9 倍，凸显了其在多 SLO 服务中的有效性。

**英文关键词：** Large Language Model Serving, Speculative Decoding, Generative AI

**中文关键词：** 大语言模型服务、投机解码、生成式 AI

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
