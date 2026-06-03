---
title: "ReVeil: Unconstrained Concealed Backdoor Attack on Deep Neural Networks using Machine Unlearning"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "backdoor-attack"
  - "machine-unlearning"
  - "dnn"
  - "ai-security"
---

# ReVeil: Unconstrained Concealed Backdoor Attack on DNNs using Machine Unlearning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。提出 ReVeil——一种无需模型访问、无需辅助数据的无约束隐蔽后门攻击：在 DNN 训练数据收集阶段投毒，利用机器遗忘（Machine Unlearning）作为触发机制，部署前 ASR 极低以逃避检测，部署后通过遗忘恢复高 ASR。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Backdoor Attack · Machine Unlearning · DNN · AI Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | ReVeil: Unconstrained Concealed Backdoor Attack on DNNs using Machine Unlearning（ReVeil：基于机器遗忘的无约束隐蔽后门攻击） |
| 作者 | Manaar Alam, Hithem Lamri, Michail Maniatakos |
| 机构 | NYU Abu Dhabi |
| 领域 | AI 安全（AI Security） |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | 后门攻击(Backdoor Attack)、机器遗忘(Machine Unlearning)、DNN、隐蔽攻击(Concealed Attack) |
| 核心资源 | [arXiv:2502.11687](https://arxiv.org/abs/2502.11687) · [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133199) |

---

## 一、一句话核心摘要

> 传统后门攻击在部署前就暴露高攻击成功率（ASR）→ 容易被检测。现有"隐蔽后门"方案需要在部署后有模型白盒/黑盒访问或辅助数据来激活。ReVeil 突破性地将触发机制交给**机器遗忘（Machine Unlearning）**——攻击者在数据收集阶段投毒，训练完成时后门处于"休眠"状态（ASR 极低），但当模型所有者出于合规/隐私需求执行遗忘操作时，后门反而被"唤醒"（ASR 恢复）。攻击者不需要模型访问、不需要辅助数据。

---

## 二、核心方法

### 2.1 遗忘作为触发器

- 投毒样本设计为与"需要被遗忘"的合法数据具有特征耦合
- 当遗忘算法移除合法数据时，模型参数更新意外地"解锁"了后门映射
- 攻击者不需要访问模型，只需要知道"模型所有者可能会执行遗忘操作"（这在 GDPR 下是法定要求）

### 2.2 实验结果

| 指标 | 结果 |
|------|------|
| 数据集 | 4 个标准数据集 |
| 触发器模式 | 4 种不同触发器 |
| 隐蔽性 | 部署前 ASR 极低，成功逃避 3 种流行检测方法 |
| 部署后 ASR | 遗忘操作后恢复高 ASR |

---

## 三、总结

ReVeil 的精妙之处在于：它将 GDPR"被遗忘权"这一隐私保护机制本身变成了攻击向量——这是对"安全机制可能成为攻击面"的绝佳诠释。

**核心资源**：[arXiv:2502.11687](https://arxiv.org/abs/2502.11687) · [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133199)
