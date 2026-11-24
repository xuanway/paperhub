---
title: "gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling"
description: "SC 2025 · Machine Learning: Inference and Serving · Tianyu Guo; Xianwei Zhang; Jiangsu Du; Zhiguang Chen; Nong Xiao; Yutong Lu"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling

**中文标题：** 采用 token 节流的全局均衡流水线并行分布式大语言模型服务系统

**所属 Session：** [Machine Learning: Inference and Serving](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Tianyu Guo; Xianwei Zhang; Jiangsu Du; Zhiguang Chen; Nong Xiao; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap444&sess=sess168)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Pipeline parallelism has emerged as a predominant approach for deploying LLMs across distributed nodes. However, it often suffers from performance limitations caused by pipeline bubbles, which primarily result from imbalanced computation delays across batches. Existing methods attempt to address this through hybrid scheduling of chunked prefill and decode tokens. However, such methods may experience significant fluctuations due to either insufficient prefill tokens or uneven distribution of decode tokens, ultimately leading to computational imbalance. To overcome these inefficiencies, we present gLLM, a globally balanced system incorporating token throttling. Our token throttling mechanism is a fine-grained scheduling policy that independently regulates the quantities of prefill and decode tokens by leveraging global information from the inference system. Furthermore, gLLM runtime adopts an asynchronous execution and message passing architecture. Evaluations show that gLLM delivers 11%

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
