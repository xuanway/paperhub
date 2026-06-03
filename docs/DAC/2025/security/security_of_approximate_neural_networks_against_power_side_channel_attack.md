---
title: "Security of Approximate Neural Networks against Power Side-channel Attack"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "approximate-computing"
  - "side-channel"
  - "neural-network"
  - "cpa"
---

# Security of Approximate Neural Networks against Power Side-channel Attack

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。首次系统研究近似计算对神经网络功耗侧信道安全的影响——在三种近似场景（超频、降压、电路级比特近似）下执行 CPA 权重提取攻击，发现近似度越高功耗迹线 SNR 越差，MTD 从 48 条暴增至 200+ 甚至 1024+ 条，攻击难度提升至少 4×–20×。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Approximate Computing · Side-Channel · Neural Network · CPA</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Security of Approximate Neural Networks against Power Side-channel Attack（近似神经网络对抗功耗侧信道攻击的安全性） |
| 作者 | Aditya Japa (Ulster U.), Jack Miskelly, Maire O'Neill, Chongyan Gu (QUB) |
| 机构 | Ulster University / Queen's University Belfast |
| 领域 | 硬件安全 / 近似计算 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | 近似计算(Approximate Computing)、侧信道(Side-Channel)、神经网络(Neural Network)、CPA、MTD |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133333) |

---

## 一、一句话核心摘要

> 近似计算通过牺牲微小精度换取大幅能效提升——但此前无人研究其对侧信道安全的影响。本文首次填补这一空白：在超频（Overclocking）、降压（Voltage Scaling）和电路级比特近似三种场景下，对近似神经网络处理单元执行 CPA 权重提取攻击，发现**近似是一把双刃剑**——功耗迹线的 SNR 随近似度增加而急剧恶化，MTD 从精确计算的 48 条暴涨至 200+（25% 比特近似）甚至 1024+ 条。

---

## 二、核心发现

### 2.1 三种近似场景下的 MTD

| 近似方案 | MTD（精确） | MTD（近似） | 攻击难度增加 |
|----------|:------:|:------:|:------:|
| 超频 | 48 | 100+ | ~2× |
| 降压 | 48 | 150+ | ~3× |
| **25% 比特近似** | 48 | **200+** | **≥4×** |
| **极端近似** | 48 | **>1024** | **>20×** |

### 2.2 为什么近似"意外地"增强了安全性？

近似计算引入的误差在功耗域表现为"伪随机噪声"——这些噪声与真实的数据依赖功耗混合，使攻击者的统计方法（CPA 的 Pearson 相关系数）信噪比大幅下降。从安全角度看，近似计算的"副作用"反而变成了"免费的安全增强"。

### 2.3 最佳方案

在安全性-功耗-延迟的综合分析中，**降压（Voltage Scaling）**表现最优——它以最小的精度损失换取了最大的攻击难度提升。

---

## 三、总结

这篇论文提供了一个令人振奋的洞察：**近似计算和安全防护可能不是敌人，而是盟友**。未来可以探索"安全感知的近似策略"——刻意在敏感计算路径上引入近似以增强抗侧信道能力。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133333)
