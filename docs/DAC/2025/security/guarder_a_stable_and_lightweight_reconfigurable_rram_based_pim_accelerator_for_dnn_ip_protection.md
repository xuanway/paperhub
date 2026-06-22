---
title: "Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rram"
  - "processing-in-memory"
  - "dnn-ip-protection"
  - "hardware-security"
---

# Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1 — AI/ML Security/Privacy。针对 RRAM 存内计算（PIM）中器件随机性导致的 DNN IP 安全隐患，提出 Guarder——基于 3T2R 单元结构的硬件-软件协同设计框架，通过稳定的可重构 RRAM 存内计算架构实现轻量级 DNN 知识产权保护。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · RRAM · Processing-in-Memory · DNN IP Protection · Hardware-Software Co-Design</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection（Guarder：面向 DNN IP 保护的稳定轻量可重构 RRAM PIM 加速器） |
| 作者 | Ning Lin, Yi Li, Jiankun Li, Jichang Yang, Yangu He, Yukui Luo, Xiaoming Chen, Xiaojuan Qi, Dashan Shang, Zhongrui Wang |
| 机构 | 中科院微电子所 / 香港大学等 |
| 领域 | 硬件安全 / 存内计算（Hardware Security / Processing-in-Memory） |
| 投稿方向 | Security（Session: SEC1 — AI/ML Security/Privacy） |
| 关键词 | RRAM、存内计算(PIM)、DNN IP 保护、3T2R、硬件-软件协同设计(Hardware-Software Co-Design) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；后续发表于 Nature Scientific Reports |

---

## 一、一句话核心摘要

> RRAM 存内计算（PIM）是 DNN 加速器能效的革命性路径——但 RRAM 器件的固有随机性（stochasticity）既是"指纹"（可用于加密），也是"噪声"（可能导致计算错误）。Guarder 提出基于 **3T2R（3 晶体管-2 电阻）**单元结构的硬件-软件协同设计：硬件侧增强稳定性与可重构性，软件侧利用稳定特性实现轻量级 DNN IP 保护（模型加密/认证），在不牺牲推理精度的前提下防止模型窃取和非法部署。

---

## 二、研究背景与动机

### 2.1 RRAM PIM 的双刃剑

- **优势**：权重存储在 RRAM 交叉杆中，矩阵-向量乘法通过 Ohm 定律和 Kirchhoff 定律在模拟域 O(1) 完成 → 能效比数字电路高 100-1000×
- **劣势**：RRAM 电导存在器件级随机性——相同编程电压产生不同电导值 → 写入精度受限

### 2.2 DNN IP 保护需求

边缘 DNN 加速器的模型权重是核心资产（数百万美元训练成本）。RRAM PIM 加速器面临的 IP 威胁：
- **权重直接读取**：RRAM 的电导状态可通过物理探测读取
- **侧信道窃取**：功耗/时序分析逆向权重
- **未经授权的模型部署**：加速器被克隆后直接使用

### 2.3 本文贡献

1. **3T2R 单元结构**：通过额外晶体管提供稳定性和独立控制，解决传统 1T1R 的随机性问题。
2. **可重构加密机制**：利用 3T2R 的独立控制能力实现硬件原生加密。
3. **硬件-软件协同 IP 保护**：轻量级方案，不影响推理精度。

---

## 三、提出的解决方案

### 3.1 3T2R 单元结构

传统 1T1R：一个晶体管选通 + 一个电阻存储 → 读取/写入共享路径 → 读干扰问题

3T2R 的优势：
- **读/写分离**：独立读取路径不影响存储状态
- **差分存储**：2 个 RRAM 差分编码同一权重 → 读取 margin 翻倍 → 稳定性大幅提升
- **可配置**：额外晶体管允许动态选择工作模式（正常推理 / 加密模式 / 锁定模式）

### 3.2 硬件原生 IP 保护

Guarder 利用 3T2R 的独立控制能力实现了三种保护模式：

| 模式 | 机制 | 保护效果 |
|------|------|----------|
| **锁定模式** | 额外晶体管关断读取路径 | 物理探测无法读取权重 |
| **加密模式** | 差分对的极性随机翻转（密钥控制） | 即使读取也得到错误权重 |
| **认证模式** | 挑战-响应协议利用 RRAM 的 PUF 特性 | 防止加速器克隆 |

---

## 四、实验评估

| 指标 | 结果 |
|------|------|
| **稳定性** | 3T2R 差分结构显著降低读取错误率 |
| **IP 保护** | 硬件原生加密 + 认证，零推理精度损失 |
| **面积开销** | "轻量级"——具体数据见论文正文 |

### 局限性

- **3T2R 面积大于 1T1R**：额外晶体管增加单元面积，但换取稳定性和安全性。(个人观点)
- **制造工艺成熟度**：3T2R 需要验证在不同工艺节点和批次间的一致性。

---

## 五、总结与展望

Guarder 展示了 RRAM PIM 加速器的安全性不需要以性能为代价——通过巧妙的单元结构设计（3T2R），稳定性和安全性可以同时提升。这为 RRAM PIM 的商业化部署提供了重要的安全基石。

### 相关资源

- **Nature Scientific Reports 后续论文**（2025）
- **RRAM PIM 综述**：Sebastian et al., Nature Nanotechnology 2020
- **PUF + RRAM**：Gao et al., "RRAM-based PUF" (IEEE TED)
