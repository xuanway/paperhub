---
title: "FailureMiner: A Joint Key Decision Mining Scheme for Practical SSD Failure Prediction and Analysis"
description: "FAST 2026 · Tiering, Mobile, and SSDs · 第 597–612 页"
tags:
  - "FAST2026"
  - "Tiering, Mobile, and SSDs"
---

# FailureMiner: A Joint Key Decision Mining Scheme for Practical SSD Failure Prediction and Analysis

**中文标题**：FailureMiner：面向实用 SSD 故障预测与分析的联合关键决策挖掘方案

**Session**：Tiering, Mobile, and SSDs · 2026-02-26 10:50–12:30 · Chair：Vasily Tarasov（IBM Research）

**作者**：Shuyang Wang, Yuqi Zhang, and Haonan Luo, Samsung R&D Institute China Xi'an, Samsung Electronics; Kangkang Liu, Tencent; Gil Kim, JongSung Na, Claude Kim, Geunrok Oh, and Kyle Choi, Samsung Electronics; Ni Xue and Xing He, Samsung R&D Institute China Xi'an, Samsung Electronics

**会议**：FAST 2026 · Santa Clara, CA · 第 597–612 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/wang-shuyang](https://www.usenix.org/conference/fast26/presentation/wang-shuyang)

**论文 PDF**：[fast26-wang-shuyang.pdf](https://www.usenix.org/system/files/fast26-wang-shuyang.pdf)

---

## 英文摘要

As SSDs become increasingly popular in enterprise data centers, SSD failures have become a key concern for storage system reliability. In this paper, we propose FailureMiner, a joint key decision mining scheme based on SSD monitoring attributes to accurately and clearly identify SSD failure patterns in production environments. First, to address the imbalance between healthy and failed samples caused by the limited number of failed SSDs, FailureMiner introduces selective downsampling to carefully remove non-critical healthy samples, thereby focusing more on the subtle differences between easily confused failure patterns and health patterns. Second, FailureMiner streamlines the decision-making process of the machine learning model in failure prediction by capturing key decision steps based on their joint contribution. By filtering out redundant and noisy information, FailureMiner can capture joint key decisions, i.e., the simplified attribute combinations and value ranges relevant to failures, thus enabling accurate and interpretable identification of failure patterns.

FailureMiner is evaluated on real-world datasets, and the results show that our scheme improves precision and recall by an average of 38.6% and 80.5% respectively, compared with the existing failure prediction methods. The extracted joint key decisions have been deployed in Tencent's data centers to predict failures across more than 350,000 SSDs over a year, enhancing SSD reliability. The joint key decisions also reveal the failure patterns and factors affecting SSD health, which further helps operators handle failures and manufacturers improve product reliability.

## 中文摘要

随着 SSD 在企业数据中心日益普及，SSD 故障已成为存储系统可靠性的关键问题。本文提出 FailureMiner，一种基于 SSD 监控属性的联合关键决策挖掘方案，旨在准确、清晰地识别生产环境中的 SSD 故障模式。首先，为解决故障 SSD 数量有限导致的健康样本与故障样本不平衡问题，FailureMiner 引入选择性下采样，谨慎地移除非关键健康样本，从而更关注易混淆故障模式与健康模式之间的细微差异。其次，FailureMiner 通过捕捉基于联合贡献的关键决策步骤，简化机器学习模型在故障预测中的决策过程。通过过滤冗余和噪声信息，FailureMiner 能够捕捉联合关键决策，即与故障相关的简化属性组合和值域，从而实现对故障模式的准确且可解释的识别。

FailureMiner 在真实数据集上进行了评估，结果表明，与现有故障预测方法相比，我们的方案将精确率和召回率平均分别提升 38.6% 和 80.5%。提取出的联合关键决策已部署在腾讯数据中心，用于在一年内预测超过 35 万块 SSD 的故障，从而提升 SSD 可靠性。这些联合关键决策还揭示了影响 SSD 健康的故障模式和因素，进一步帮助运维人员处理故障，并帮助制造商改进产品可靠性。
