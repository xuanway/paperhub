---
title: "In-Production Characterization of an Open Source Serverless Platform and New Scaling Strategies"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Nima Nasiri (University of British Columbia), Nalin Munshi (University of Britis"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# In-Production Characterization of an Open Source Serverless Platform and New Scaling Strategies

**中文标题：** 开源无服务器平台的生产环境特征刻画与新型扩缩容策略

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Nima Nasiri (University of British Columbia), Nalin Munshi (University of British Columbia), Simon D Moser (IBM), Marius Pirvu (IBM), Vijay Sundaresan (IBM), Daryl Maier (IBM), Thatta Premnath (IBM), Norman Böwing (IBM), Sathish Gopalakrishnan (University of British Columbia), Mohammad Shahrad (University of British Columbia)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769377)

## 英文摘要

Serverless computing has become more popular and evolved to support more complex tasks than the original Function as a Service (FaaS) model. The design of serverless systems has advanced to accommodate application demands and offer flexibility. Careful characterization of modern serverless systems and understanding of current gaps are warranted. Publicly available datasets on workloads in select production serverless systems do not fully represent all offerings or capture traces at the required time resolution to identify changes in application-level request-response patterns.

We characterize – and make available – production traces from a major public serverless provider with over 1.9 billion invocations spanning over two months. Our dataset is the first to characterize an open-source platform with large-scale trace data, millisecond-scale arrival times, and user configurations for pod concurrency and minimum pod scaling. Using this dataset, we provide new insights for optimizing serverless platforms.

With our insights, we design and implement FeMux, a serverless lifetime management system. FeMux multiplexes lightweight forecasters and uses a Representative Unified Metric (RUM) to decouple metrics from serverless platform implementations. This allows providers like us to update metrics flexibly or support multiple system objectives simultaneously. We prototype FeMux on the Knative platform and evaluate its benefits.

## 中文摘要

无服务器计算日益普及，并已演进到能够支持比最初的函数即服务（FaaS）模型更复杂的任务。无服务器系统的设计不断进步，以满足应用需求并提供灵活性。因此，有必要对现代无服务器系统进行细致的特征刻画，并理解当前的不足。现有针对部分生产环境无服务器系统负载的公开数据集，既不能完整代表所有服务形态，也无法以所需的时间分辨率捕获负载轨迹，从而难以识别应用层请求—响应模式的变化。

我们对来自一家大型公共无服务器提供商的生产负载轨迹进行了特征刻画并公开该数据集，其中包含超过 19 亿次调用，时间跨度超过两个月。我们的数据集首次在刻画开源平台时同时提供大规模轨迹数据、毫秒级到达时间，以及关于 Pod 并发度和最小 Pod 伸缩的用户配置。基于该数据集，我们提出了若干优化无服务器平台的新洞见。

基于这些洞见，我们设计并实现了 FeMux，一个无服务器生命周期管理系统。FeMux 复用多个轻量级预测器，并使用代表性统一指标（RUM）将指标与无服务器平台实现解耦。这使像我们这样的提供商能够灵活更新指标，或同时支持多个系统目标。我们在 Knative 平台上实现了 FeMux 原型并评估其收益。

**英文关键词：** Cloud Computing, Serverless, Resource Management, Forecasting, Characterization

**中文关键词：** 云计算、无服务器计算、资源管理、预测、特征刻画

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
