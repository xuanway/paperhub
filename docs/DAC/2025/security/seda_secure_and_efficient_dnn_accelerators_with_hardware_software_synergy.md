---
title: "SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "dnn-accelerator"
  - "hardware-software-codesign"
  - "encryption"
  - "memory-protection"
---

# SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。提出 SeDA——基于硬件-软件协同设计的安全 DNN 加速器架构，通过硬件加密引擎与软件调度策略的深度协同，在边缘设备上同时保障 DNN 推理的机密性与完整性，实现细粒度内存保护与低开销的平衡。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · DNN Accelerator · Hardware-Software Codesign · Encryption · Memory Protection</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy（SeDA：基于硬件-软件协同的安全高效 DNN 加速器） |
| 作者 | Wei Xuan, Zhongrui Wang, Lang Feng, Ning Lin, Zihao Xuan, Rongliang Fu, Tsung-Yi Ho, Yuzhong Jiao, Luhong Liang |
| 机构 | AI Chip Center for Emerging Smart Systems (ACCESS, 香港) / 南方科大 / 中大 / 港大 |
| 领域 | AI/ML 安全 |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | DNN 加速器、硬件-软件协同(Hardware-Software Codesign)、加密(Encryption)、内存保护(Memory Protection) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133180) |

---

## 一、一句话核心摘要

> 边缘 DNN 加速器面临模型窃取和数据隐私双重威胁——纯硬件方案开销大，纯软件方案性能差。SeDA 通过**硬件加密引擎 + 软件调度策略的深度协同**，在 DNN 推理过程中实现细粒度、低开销的内存保护：硬件负责线速加解密（块 cipher），软件根据层敏感度自适应调节保护粒度，在安全保障与推理性能之间取得最优平衡。

---

## 二、核心方法

### 硬件-软件分工

| 层级 | 职责 |
|------|------|
| **硬件** | 块加密引擎（AES-like）、MAC 生成/验证、密钥管理 |
| **软件** | 调度策略：根据每层的参数敏感性动态开关保护、调节保护粒度 |

### 设计关键

并非所有 DNN 层的权重都同等敏感——第一层和最后一层通常泄漏最多信息。SeDA 的软件调度器自动识别高敏感层并仅对它们启用全强度保护。

---

## 三、总结

SeDA 代表了安全 DNN 加速器从"一刀切全加密"到"自适应选择性保护"的演进趋势——与 Data Oblivious CPU、POLARIS 等工作的"选择性防护"哲学一脉相承。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133180)
