---
title: "Power-Based Side-Channel Attack on XGBoost Accelerator"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "xgboost"
  - "side-channel"
  - "fpga"
  - "model-extraction"
---

# Power-Based Side-Channel Attack on XGBoost Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。首次展示针对 XGBoost FPGA 加速器的功耗侧信道模型窃取攻击——仅需约 367k 条功耗迹线即可推断 XGBoost 决策树的节点特征和阈值，揭示了 ML 加速器硬件部署的侧信道安全隐患。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · XGBoost · Side-Channel · FPGA · Model Extraction</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Power-Based Side-Channel Attack on XGBoost Accelerator（面向 XGBoost 加速器的功耗侧信道攻击） |
| 作者 | Yimeng Xiao, Archit Gajjar, Aydin Aysu, Paul Franzon |
| 机构 | NC State University |
| 领域 | 硬件安全 / AI 安全 |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | XGBoost、侧信道攻击(Side-Channel Attack)、FPGA、模型窃取(Model Extraction) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133048) |

---

## 一、一句话核心摘要

> XGBoost 是金融风控、勒索软件检测等领域的主流 ML 模型——但其 FPGA 加速器的硬件安全此前未被探索。本文首次展示：攻击者通过测量 XGBoost FPGA 加速器（FAXID on Sakura-X）的功耗迹线，可推断决策树的**节点特征和分裂阈值**，平均仅需约 **367k 条功耗迹线**即可窃取敏感模型参数，为 ML 加速器的硬件安全防护敲响了警钟。

---

## 二、核心方法

### 2.1 攻击原理

XGBoost 推理的核心是遍历决策树——在每个节点比较特征值与阈值：
- 特征值 > 阈值 → 走右分支（可能触发更多节点比较）
- 特征值 ≤ 阈值 → 走左分支

**功耗泄漏点**：比较操作涉及从内存读取特征和阈值 → 功耗与读取数据的汉明重量/距离相关 → 攻击者从功耗迹线推断比较结果 → 逐步重建决策树结构。

### 2.2 实验结果

| 指标 | 结果 |
|------|------|
| 攻击目标 | FAXID XGBoost FPGA 加速器 |
| 平台 | Sakura-X FPGA 板 |
| 所需功耗迹线 | 平均 **~367k** 条 |
| 泄漏信息 | 节点特征索引 + 分裂阈值 |

---

## 三、总结与展望

这是 XGBoost 硬件加速器侧信道安全的开篇工作。367k 迹线在实验室条件下（自动采集数小时）完全可行，对于部署在生产环境中的 XGBoost 加速器来说构成了现实的模型窃取威胁。

**防御方向**：功耗掩蔽、恒定时间决策树遍历、或采用同态加密推理（但开销较大）。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133048)
