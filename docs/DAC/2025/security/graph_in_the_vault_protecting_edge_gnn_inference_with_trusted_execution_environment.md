---
title: "Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "graph-neural-network"
  - "trusted-execution-environment"
  - "intel-sgx"
  - "edge-computing"
  - "privacy"
---

# Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1 — AI/ML Security/Privacy。针对边缘设备上 GNN 推理中模型知识产权和图数据隐私的双重威胁，提出 GNNVault——首个基于 Intel SGX TEE 的安全 GNN 部署策略，采用"先分区后训练"设计：公共骨干模型 + 在 TEE 内运行的私有 GNN 矫正器，精度损失 <2%，有效抵御 SOTA 链路窃取攻击。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · GNN · TEE · Intel SGX · Edge Computing · Privacy · Link Stealing</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment（图入保险库：以可信执行环境保护边缘 GNN 推理） |
| 作者 | Ruyi Ding, Tianhong Xu, Aidong Adam Ding, Yunsi Fei |
| 机构 | Northeastern University（东北大学，美国） |
| 领域 | AI/ML 安全与隐私（AI/ML Security & Privacy） |
| 投稿方向 | Security（Session: SEC1 — AI/ML Security/Privacy） |
| 关键词 | 图神经网络(GNN)、可信执行环境(TEE)、Intel SGX、链路窃取攻击(Link Stealing)、边缘计算(Edge Computing) |
| 核心资源 | [arXiv:2502.15012](https://arxiv.org/abs/2502.15012)（全文开放获取） · [IEEE Xplore](https://ieeexplore.ieee.org) |

---

## 一、一句话核心摘要

> 图神经网络（GNN）在社交网络分析、推荐系统、分子建模等领域广泛应用——但边缘部署使**模型知识产权和图数据隐私**同时暴露于窃取风险：攻击者可通过链路窃取攻击（Link Stealing Attack）推断图中的敏感关系。GNNVault 首次提出了基于 Intel SGX TEE 的安全 GNN 部署方案，采用"先分区后训练"策略——公共骨干模型运行在非安全区、私有 GNN 矫正器在 SGX Enclave 内部运行——既保护模型参数又保护图数据隐私，精度损失不到 2%。

---

## 二、研究背景与动机

### 2.1 GNN 的隐私威胁模型

GNN 的推理输入不仅包括节点特征，还包括**图的拓扑结构**（邻接矩阵）。这对隐私提出了独特挑战：

- **模型参数泄漏**：攻击者从 API 响应中逆向 GNN 参数，窃取模型 IP
- **链路窃取攻击**：攻击者通过多次查询推断图中哪些节点之间存在边——这在社交网络中直接暴露好友关系等敏感信息

### 2.2 现有防御的不足

| 方法 | 局限 |
|------|------|
| **差分隐私 GNN** | 噪声影响图结构信息传递，精度损失严重 |
| **联邦 GNN** | 无法保护推理阶段的图数据隐私 |
| **TEE for DNN** | 现有 TEE 方案（如 Slalom、Graviton）仅适用于 DNN，未考虑 GNN 的图邻居聚合特性 |

### 2.3 论文贡献

1. **首个 TEE 安全 GNN 部署方案（GNNVault）**：在 Intel SGX 上实现安全 GNN 推理。
2. **"先分区后训练"策略**：公共骨干 + 私有矫正器，最大化 TEE 效率。
3. **抵御链路窃取攻击**：实验验证对 SOTA 链路窃取攻击的有效防御。

---

## 三、提出的解决方案

### 3.1 GNNVault 架构

```
┌──────────────────────────────────┐
│  非安全区（Untrusted）            │
│  ┌──────────────────────────┐    │
│  │ 公共 GNN 骨干模型         │    │
│  │ (如 GCN 前 K-1 层)       │    │
│  └──────────┬───────────────┘    │
│             │ 中间表示            │
│  ┌──────────▼───────────────┐    │
│  │    Intel SGX Enclave     │    │
│  │  ┌─────────────────────┐ │    │
│  │  │ 私有 GNN 矫正器      │ │    │
│  │  │ (最后几层 + 图聚合)  │ │    │
│  │  │ + 敏感图数据(邻接表) │ │    │
│  │  └─────────────────────┘ │    │
│  └──────────────────────────┘    │
└──────────────────────────────────┘
```

### 3.2 "先分区后训练"策略

传统 TEE 方案是"先训练后分区"——这导致分区边界可能破坏模型精度。GNNVault 创新地**在训练前就确定分区边界**，使训练过程适应分区——公共部分学会在有信息损失的情况下仍产生有用表示，私有部分学会从这些表示中提取并精炼。

### 3.3 私有 GNN 矫正器

矫正器在 Enclave 内执行私有图聚合（在私密邻接表上做消息传递），修正公共骨干因无法访问完整图拓扑而产生的误差。

---

## 四、实验评估

| 指标 | 结果 |
|------|------|
| **精度损失** | **< 2%**（可忽略） |
| **链路窃取防御** | 有效抵御 SOTA 链路窃取攻击 |
| **实现平台** | Intel SGX（真实硬件） |
| **GNN 模型** | GCN、GAT、GraphSAGE 等主流架构 |

### 局限性

- **SGX Enclave 内存限制**：当前 SGX 的 EPC 约 128-512MB，限制了图的规模。
- **Enclave 切换开销**：公共→私有边界涉及 Enclave 进入/退出，增加延迟。但对于典型 GNN 推理延迟（毫秒级），这一开销占比可接受。

---

## 五、总结与展望

GNNVault 将 TEE 安全 GNN 推理从概念变为工程实现，`先分区后训练`的策略为其他 TEE+ML 工作提供了可复用的设计范式。

**核心资源**：[arXiv:2502.15012](https://arxiv.org/abs/2502.15012) · [Intel SGX SDK](https://github.com/intel/linux-sgx)

### 相关阅读

- **TEE for ML**：Slalom (USENIX ATC 2023)、Graviton (ASPLOS 2020)
- **链路窃取攻击**：He et al., "LinkTeller: Recovering Private Edges from GNN" (USENIX 2022)
- **图神经网络综述**：Wu et al., "A Comprehensive Survey on GNN" (IEEE TNNLS 2020)
