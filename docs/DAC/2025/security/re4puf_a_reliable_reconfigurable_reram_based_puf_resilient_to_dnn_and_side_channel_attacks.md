---
title: "Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rram"
  - "puf"
  - "reconfigurable"
  - "dnn-attack"
  - "side-channel"
---

# Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2。针对 ReRAM PUF 面临读噪声/温度漂移和 DNN/SCA 建模攻击的双重挑战，提出 Re⁴PUF——基于 3T2R 单元结构的可重构 ReRAM PUF，在 85°C 下 BER 仅 1%（7.59× 降低），且通过模拟电压调谐实现的低成本重配置使 DNN/Transformer 攻击准确率降至 ≈50%（接近随机猜测），已实际流片验证。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · ReRAM · PUF · Reconfigurable · DNN Attack · Side-Channel · Silicon Validated</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks（Re⁴PUF：抗 DNN 和侧信道攻击的可靠可重构 ReRAM PUF） |
| 作者 | Hegan Chen, Rui Chen, Yongkang Han, Yangu He 等 17 人 |
| 机构 | 中科院微电子所等 |
| 领域 | 硬件安全 / PUF（Hardware Security / PUF） |
| 投稿方向 | Security（Session: SEC2） |
| 关键词 | ReRAM、PUF、可重构(Reconfigurable)、DNN 攻击、侧信道(Side-Channel)、硅验证(Silicon Validated) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133290) |

---

## 一、一句话核心摘要

> ReRAM PUF 因其紧凑面积和低功耗在硬件安全领域备受关注——但两座大山挡在实用化之前：(1) 读噪声和温度漂移导致可靠性差；(2) DNN 建模攻击和侧信道分析可以高精度地克隆 PUF 的激励-响应映射。Re⁴PUF 采用**3T2R 电压分压单元**提升可靠性（85°C 下 BER 仅 1%，比现有 ReRAM PUF 降低 7.59×），并通过**模拟电压调谐实现 PUF 重配置**——无需重新编程 ReRAM 单元本身——使 DNN/Transformer 攻击准确率降至 ~50%。

---

## 二、核心方法

### 2.1 3T2R 电压分压单元

- 2 个 ReRAM 电阻差分分压，由 3 个晶体管控制偏置和读出
- 差分结构对共模噪声（温度漂移）天然免疫 → BER 大幅降低

### 2.2 模拟电压可重构性

传统 ReRAM PUF 重配置需要重新写入 ReRAM（SET/RESET 脉冲）——耗时高、功耗大、且有 endurance 限制。Re⁴PUF 的巧妙之处在于：**改变反相器对的模拟供电电压**即可改变判决阈值，实现快速、低成本、无限次的重配置——且不损失 ReRAM 寿命。

### 2.3 芯片实测结果

| 指标 | 结果 |
|------|------|
| **85°C 下 BER** | **1%**（7.59× 降低 vs 现有 ReRAM PUF） |
| **MLP/DNN 攻击准确率** | **≈50%**（接近随机猜测） |
| **SCA 攻击成功率** | **< 70%** |
| **验证级别** | 实际流片（硅验证） |

---

## 三、总结

Re⁴PUF 在可靠性（BER 1% at 85°C）和安全性（DNN 50%）两个维度同时达到了实用化门坎。17 位作者的共同努力和实际流片验证使其成为 PUF 硬件安全方向的标杆级工作。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133290)
