---
title: "Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "quantum-computing"
  - "anomaly-detection"
  - "autoencoder"
  - "unsupervised-learning"
---

# Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。首次提出无需任何训练的量子异常检测框架 Quorum——利用量子自编码器（Quantum Autoencoder）的内在特性直接进行无监督异常检测，彻底规避了量子 ML 中梯度计算的困难，为金融/医疗/能源等关键领域的量子安全异常检测奠定基础。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Quantum Computing · Anomaly Detection · Autoencoder · Unsupervised Learning</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders（Quorum：基于量子自编码器的零训练无监督异常检测） |
| 作者 | Jason Zev Ludmir, Sophia Rebello, Jacob Ruiz, Tirthak Patel |
| 机构 | Rice University |
| 领域 | 量子计算 / AI 安全（Quantum Computing / AI Security） |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | 量子计算(Quantum Computing)、异常检测(Anomaly Detection)、量子自编码器(Quantum Autoencoder)、无监督学习(Unsupervised Learning) |
| 核心资源 | [arXiv:2504.13113](https://arxiv.org/abs/2504.13113)（全文开放） · [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132860) |

---

## 一、一句话核心摘要

> 在金融欺诈检测、医疗异常诊断、能源系统监控等关键应用中，异常检测模型必须快速部署且无需标注——但量子 ML 面临一个根本性困难：**变分量子电路的梯度计算**在 NISQ 时代的硬件噪声下极不稳定。Quorum 另辟蹊径：利用量子自编码器的**固有信息压缩特性**，在不执行任何梯度优化（零训练）的前提下，通过测量量子态的"重构误差"直接判断异常，彻底绕过了量子 ML 的训练瓶颈。

---

## 二、核心方法

### 2.1 量子自编码器的"免费午餐"

经典自编码器需要训练（BP + 梯度下降）来学习压缩-重建映射。但量子自编码器可通过**量子电路的结构本身**实现信息压缩——将高维量子态投影到低维子空间——这一过程是酉变换，无需训练。

### 2.2 Quorum 工作流程

1. 正常数据被编码为量子态 |ψ_normal⟩
2. 量子自编码器电路（固定结构、零训练）压缩并重建
3. 测量重建态与原始态的重叠度（Fidelity）
4. Fidelity 低的样本 → 偏离正常模式 → 标记为异常

### 2.3 核心贡献

- **首个零训练量子异常检测框架**
- 完全无监督（无需异常标签）
- 规避了变分量子算法的梯度难题

---

## 三、总结与展望

Quorum 为 NISQ 时代的量子异常检测开辟了一条"不走梯度"的路径。当前适用性受限于量子比特数（NISQ: 50-100 qubits），但概念验证意义重大。

**核心资源**：[arXiv:2504.13113](https://arxiv.org/abs/2504.13113) · [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132860)
