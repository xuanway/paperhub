---
title: "POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "power-side-channel"
  - "explainable-ai"
  - "masking"
  - "hardware-security"
---

# POLARIS: Explainable AI for Mitigating Power Side-Channel Leakage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。首次将可解释 AI（XAI）引入功耗侧信道防护——POLARIS 通过 SHAP 值自动识别芯片网表中对功耗泄漏贡献最大的逻辑门，仅对这些高泄漏门进行定向掩蔽（Masking），以无监督方式自动构建训练数据，在泄漏降低、执行时间和设计开销三个维度上全面超越 SOTA 方案 VALIANT。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Power Side-Channel · XAI · SHAP · Masking · Hardware Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage（POLARIS：基于可解释 AI 的功耗侧信道泄漏缓解） |
| 作者 | Tanzim Mahfuz, Tasneem Suha, Prabuddha Chakraborty (U. Maine); Sudipta Paria, Swarup Bhunia (U. Florida) |
| 机构 | University of Maine / University of Florida |
| 领域 | 硬件安全 / 侧信道防护 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | 功耗侧信道(Power Side-Channel)、可解释 AI (XAI)、掩蔽(Masking)、SHAP、硬件安全(Hardware Security) |
| 核心资源 | [arXiv:2507.22177](https://arxiv.org/abs/2507.22177)（全文开放获取） · [IEEE Xplore](https://ieeexplore.ieee.org/document/11132622/) |

---

## 一、一句话核心摘要

> 功耗侧信道防护的传统方法是"全局掩蔽"——对所有逻辑门一视同仁地增加噪声或平衡——这带来巨大的面积和功耗开销（2-5×）。但并非所有逻辑门对总泄漏的贡献相等——少数高泄漏门贡献了大部分可观测信息。POLARIS 首次将**可解释 AI（SHAP 值）**应用于门级网表，自动识别"高泄漏门"，仅对它们施加定向掩蔽，在泄漏降低、执行时间和设计开销上全面超越 SOTA（VALIANT）。

---

## 二、核心方法

### 2.1 XAI 如何识别高泄漏门？

1. 将门级网表转换为特征矩阵（门类型、扇入/扇出、逻辑深度、翻转概率等）
2. 训练 ML 模型预测每个门对整体功耗迹线可观测泄漏的贡献
3. 使用 **SHAP（SHapley Additive exPlanations）**值量化每个门特征的泄漏贡献
4. 筛选出 SHAP 值 top-k 的高泄漏门

### 2.2 定向掩蔽

传统掩蔽：每个门都用双轨逻辑（面积 ×2）或随机掩码（功耗 ×1.5）。
POLARIS：仅对 SHAP 识别的高泄漏门施加掩蔽（如门数量 10-20%），其余门不变。

### 2.3 实验结果

| 指标 | vs VALIANT (SOTA) |
|------|:-----------------:|
| 泄漏降低 | 更优 |
| 执行时间 | 更快 |
| 设计开销 | 更低 |
| 数据集 | ISCAS + EPFL 基准电路 |

---

## 三、总结

POLARIS 的哲学令人深思："不要对所有门平等对待——XAI 告诉我们应该防护哪些门。"这与 Data Oblivious CPU 的"选择性防护"思想异曲同工——安全硬件设计的未来不是全有或全无，而是精准定向。

**核心资源**：[arXiv:2507.22177](https://arxiv.org/abs/2507.22177) · [IEEE Xplore](https://ieeexplore.ieee.org/document/11132622/)
