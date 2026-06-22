---
title: "Identifying System-on-Chip Security Assets with Structure-Based Analysis"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "soc"
  - "security-assets"
  - "graph-neural-network"
  - "rtl-analysis"
  - "automation"
---

# Identifying System-on-Chip Security Assets with Structure-Based Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2。针对 SoC 安全资产识别高度依赖人工的痛点，提出基于 RTL 代码转图结构 + DNN 分类的自动化框架，将 RTL 转换为图表示后利用深度神经网络学习安全资产的拓扑结构模式，分类准确率达 99%，大幅降低人工标注成本。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · SoC · Security Assets · GNN · RTL Analysis · Automation</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Identifying System-on-Chip Security Assets with Structure-Based Analysis（基于结构分析的 SoC 安全资产识别） |
| 作者 | Wei-Kai Liu (Duke), Benjamin Tan (U. Calgary), Krishnendu Chakrabarty (ASU) |
| 机构 | Duke University / University of Calgary / Arizona State University |
| 领域 | 硬件安全 / SoC 安全（Hardware Security / SoC Security） |
| 投稿方向 | Security（Session: SEC2） |
| 关键词 | SoC 安全、安全资产识别(Security Asset Identification)、图神经网络(GNN)、RTL 分析、自动化(Automation) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org/document/11133104/) |

---

## 一、一句话核心摘要

> SoC 设计复杂度持续攀升，多源 IP 集成使安全资产（密钥存储、安全配置寄存器、密码引擎等）的识别成为防漏洞的核心前提——但这一过程至今高度依赖手工审计，耗时且易遗漏。本文首次提出自动化安全资产识别框架：将 RTL 代码转换为**图结构表示**（模块互联图 + 信号依赖图），利用**深度神经网络**学习安全资产的拓扑结构模式，分类准确率达 **99%**。

---

## 二、核心方法

### 2.1 RTL→图转换

将 SoC RTL 设计（Verilog/VHDL）自动解析为：
- **模块级图**：节点 = 模块实例，边 = 信号连接
- **信号级图**：细粒度的寄存器/线网数据流图
- 节点特征包含：位宽、信号名语义、扇入/扇出、是否连接特定接口 (JTAG/加密总线)

### 2.2 GNN 分类

- 使用 GNN（GCN/GAT）在图上学习节点嵌入
- 训练集由少量人工标注的安全/非安全 IP 构成
- 推理时自动判断未见过的 IP 是否为安全资产

### 2.3 99% 准确率的意义

这意味着在典型 SoC 设计中，安全团队只需要复查 GNN 标记的少数候选（约 1% 误报），而不是手动遍历全部数百个 IP 模块。

---

## 三、实验与展望

| 指标 | 结果 |
|------|------|
| 分类准确率 | 高达 **99%** |
| 输入 | RTL (Verilog/VHDL) |
| 输出 | 安全资产列表 |

**工业价值**：可集成到 SoC 安全设计流程中，在架构设计阶段自动生成安全资产清单。

**局限性**：训练数据需要一定量的手工标注；对新型安全 IP 架构的泛化性需持续验证。

**相关资源**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11133104/)
