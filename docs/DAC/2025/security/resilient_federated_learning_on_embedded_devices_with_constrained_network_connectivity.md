---
title: "Resilient Federated Learning on Embedded Devices with Constrained Network Connectivity"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "federated-learning"
  - "embedded-devices"
  - "network-constrained"
  - "gradient-compression"
---

# Resilient Federated Learning on Embedded Devices with Constrained Network Connectivity

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。针对嵌入式 IoT 设备在网络受限条件下参与联邦学习时带宽不足的挑战，提出自适应联邦学习框架——仅当本地梯度与全局梯度相似时才传输压缩更新，相比 SOTA 方法节省 60-78% 带宽，在仿真和真实硬件上验证。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Federated Learning · Embedded Devices · Network Constrained · Gradient Compression</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Resilient Federated Learning on Embedded Devices with Constrained Network Connectivity（网络受限嵌入式设备上的弹性联邦学习） |
| 作者 | Zihan Li, Han Liu, Ao Li, Ching-Hsiang Chan, Yevgeniy Vorobeychik, William Yeoh (WashU), Wenjing Lou (Virginia Tech), Ning Zhang (WashU) |
| 机构 | Washington University in St. Louis / Virginia Tech |
| 领域 | AI/ML 安全与隐私 |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | 联邦学习(Federated Learning)、嵌入式设备(Embedded Devices)、梯度压缩(Gradient Compression)、自适应(Adaptive) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133269) |

---

## 一、一句话核心摘要

> 联邦学习的"去中心化"理想在嵌入式 IoT 设备上遇到残酷的现实：蜂窝/NB-IoT 网络带宽仅数十 kbps、连接间歇性中断。现有梯度压缩方法（如 Top-K、QSGD）在所有轮次中均匀压缩——但并非所有轮次的梯度更新都同等重要。本文提出**自适应联邦框架**：当设备本地梯度与全局梯度方向高度相似时（说明本地学习方向正确），仅传输高度压缩的更新；方向偏离时才传输完整梯度。带宽节省达 60–78%。

---

## 二、核心方法

### 2.1 相似度判断

- 计算本地梯度 ∇L 与全局梯度 ∇G 的余弦相似度
- 相似度 > 阈值 → 传输极致压缩版本（如 1-bit signSGD）
- 相似度 < 阈值 → 传输完整梯度（本地模型需要纠偏）

### 2.2 实验结果

| 指标 | 结果 |
|------|------|
| **带宽节省 vs SOTA** | **60–78%** |
| 模型精度 | 与无压缩 FL 持平 |
| 验证平台 | 仿真 + 真实嵌入式硬件 |

---

## 三、总结

该工作将联邦学习从"实验室 WiFi 环境"推进到了"真实 IoT 网络约束"——60-78% 带宽节省意味着使用 NB-IoT 的传感器节点也能实际参与联邦训练。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133269)
