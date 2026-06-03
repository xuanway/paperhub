---
title: "DeepPUFSCA: Deep learning for Physical Unclonable Function attack based on Side Channel Analysis support"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "physical-unclonable-function"
  - "side-channel-analysis"
  - "deep-learning"
  - "puf-attack"
  - "fpga"
---

# DeepPUFSCA: Deep Learning for PUF Attack Based on Side Channel Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3 — Hardware Security: Attack & Defense。针对物理不可克隆函数（PUF）面对机器学习和侧信道联合攻击的脆弱性，提出 DeepPUFSCA——首个深度融合激励-响应对（CRP）与功耗侧信道信息的深度学习 PUF 攻击模型，在 FPGA 上实现 Arbiter PUF 并采集功耗数据，攻击精度超越所有 ML 基准方法（含集成算法）。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · PUF · Side-Channel Analysis · Deep Learning · Arbiter PUF · FPGA · Hardware Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | DeepPUFSCA: Deep learning for Physical Unclonable Function attack based on Side Channel Analysis support（DeepPUFSCA：基于侧信道分析辅助的深度学习 PUF 攻击） |
| 作者 | Ngoc Phu Doan, Tuan Dung Pham, Zichi Zhang, Hung Viet Tran, Jack Miskelly, Hans Vandierendonck, Anh-Tuan Hoang, Maire O'Neill, Thai Son Mai |
| 机构 | Queen's University Belfast (QUB) |
| 领域 | 硬件安全 / PUF 安全（Hardware Security / PUF Security） |
| 投稿方向 | Security（Session: SEC3 — Hardware Security: Attack & Defense） |
| 关键词 | 物理不可克隆函数(PUF)、侧信道分析(Side-Channel Analysis)、深度学习(Deep Learning)、Arbiter PUF、FPGA |
| 核心资源 | [QUB Pure 预印本](https://pure.qub.ac.uk/en/publications/deeppufsca)（CC BY） · [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132394) |

---

## 一、一句话核心摘要

> 物理不可克隆函数（PUF）利用芯片制造过程中的随机工艺偏差生成唯一"指纹"，是硬件安全的核心原语——但研究发现，单纯依赖激励-响应对（CRP）的机器学习攻击和单纯依赖侧信道（功耗/电磁）的攻击各自存在局限。DeepPUFSCA 首次将两者**深度融合**——在单个深度学习模型中同时输入 CRP 和功耗侧信道迹线进行 PUF 建模攻击，在 FPGA 上自建 Arbiter PUF 并采集实测功耗数据集，攻击精度超越所有 ML 基准方法。

---

## 二、研究背景与动机

### 2.1 PUF：硬件安全的"指纹"

PUF 的原理是利用芯片制造中不可控的随机工艺偏差——两个相同设计的 Arbiter PUF 在两个芯片上会产生完全不同的激励-响应映射。这种"指纹"特性使 PUF 成为：
- **设备认证**：验证芯片身份
- **密钥生成**：从 PUF 响应中提取稳定密钥（需 fuzzy extractor）
- **防伪**：确认芯片来源

### 2.2 PUF 面临的攻击威胁

| 攻击类型 | 方法 | 需求 |
|----------|------|------|
| **CRP 建模攻击** | 收集大量激励-响应对，训练 ML 模型预测未见激励的响应 | 大量 CRP 数据（通常 10³–10⁶ 对） |
| **侧信道攻击** | 测量 PUF 操作期间的功耗/电磁辐射，推断内部信号传播路径 | 物理访问设备 + 测量设备 |
| **联合攻击（DeepPUFSCA）** | 融合 CRP + 功耗侧信道 | CRP 数据 + 物理测量 |

### 2.3 论文的核心洞察

**CRP 和侧信道信息是互补的：**
- CRP 提供了 PUF 的"功能级"行为模型
- 功耗侧信道提供了 PUF 内部信号传播的"物理级"信息——哪条路径快、哪条慢

如果攻击者同时拥有两者，DL 模型可以从"外部行为 + 内部物理过程"两个维度联合建模 PUF，攻击精度天然优于单一信息源。

### 2.4 本文贡献

1. **首次深度融合 CRP + SCA**：提出 DeepPUFSCA，在单个 DL 模型中联合学习激励-响应映射和功耗侧信道特征。
2. **FPGA 实测数据集**：在 FPGA 上实现 Arbiter PUF，采集包含 CRP 和功耗迹线的完整数据集。
3. **超越所有 ML 基准**：攻击精度优于单独的 CRP 建模、SCA 攻击及集成组合方法。

---

## 三、提出的解决方案

### 3.1 Arbiter PUF 原理

Arbiter PUF 的核心是一条对称的延迟链：

- 输入激励比特（Challenge）决定每个开关的信号路径（直通/交叉）
- 两条竞争信号的到达时间差（Δt）由 Arbiter（仲裁器）判决 → 输出响应比特
- Δt 的正负取决于工艺偏差 → 每个 PUF 实例的 CRP 映射是唯一的

### 3.2 DeepPUFSCA 模型架构

```
   ┌──────────────┐     ┌──────────────┐
   │ 激励 (CRP)    │     │ 功耗迹线 (SCA)│
   └──────┬───────┘     └──────┬───────┘
          │                    │
   ┌──────▼───────┐    ┌──────▼───────┐
   │ 激励编码器    │    │ SCA 特征提取  │
   │ (MLP/CNN)    │    │ (Conv1D)     │
   └──────┬───────┘    └──────┬───────┘
          │                    │
          └────────┬───────────┘
                   │
          ┌───────▼────────┐
          │  特征融合层     │
          │ (Concat + FC)  │
          └───────┬────────┘
                   │
          ┌───────▼────────┐
          │  响应预测 (0/1) │
          └────────────────┘
```

**关键设计选择**：
- **激励编码器**：MLP 或小型 CNN，将激励比特向量映射到高维表征
- **SCA 特征提取**：Conv1D 从功耗迹线中捕捉 Arbiter 判决时刻的精细时序特征
- **融合策略**：拼接（Concatenation）后接全连接层，端到端训练

### 3.3 数据采集实验

作者在 FPGA 上实现了 Arbiter PUF，并通过：
1. **CRP 采集**：遍历激励空间记录响应
2. **功耗采集**：使用示波器捕捉每次 PUF 操作的功耗波形（在 Arbiter 判决瞬间有明显电流峰值）
3. **对齐与预处理**：功耗迹线的触发对齐、去噪、归一化

### 3.4 为什么融合更好？信息论视角

从信息论的角度，CRP 建模提供的是 PUF 函数的**条件分布 P(Response | Challenge)**，而功耗侧信道提供的是 PUF 内部状态的**额外互信息 I(Response; Power_Trace | Challenge)**。DeepPUFSCA 的双路模型正是在利用这种条件互信息来缩小预测的不确定性。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| PUF 类型 | Arbiter PUF |
| 实现平台 | FPGA（具体型号见论文正文） |
| 数据集 | 自建 FPGA 实测数据集（CRP + 功耗迹线） |
| 对比基线 | MLP/CNN（仅 CRP）、模板 SCA 攻击、集成方法（CRP 模型 + SCA 模型 的投票/平均） |
| 评估指标 | 响应预测准确率、攻击所需数据量 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **攻击准确率** | DeepPUFSCA **超越所有 ML 基准方法**，包括集成算法 |
| **融合增益** | CRP + SCA 联合训练显著优于单一信息源 |
| **数据效率** | 在相同 CRP 数据量下，融合 SCA 使攻击准确率更快饱和 |

### 4.3 局限性分析

- **功耗测量的物理访问需求**：CRP 建模攻击可以仅通过软件 API 收集数据；而功耗 SCA 需要物理连接示波器——这在真实攻击场景中限制了可扩展性。但一旦攻击者拥有物理访问权限（如恶意内部人员），这种威胁是真实且严重的。
- **功耗迹线的信噪比依赖**：FPGA 平台的噪声底噪和测量设备的精度影响 SCA 特征质量——高端示波器下的结果在低成本硬件上可能无法复现。(个人观点)
- **其他 PUF 类型的适用性**：Arbiter PUF 的延迟竞争机制天然适合功耗分析，但 SRAM PUF 或 Ring Oscillator PUF 的泄漏模式可能不同。

---

## 五、结论与展望

### 5.1 论文结论

DeepPUFSCA 证明了将 CRP 建模与功耗侧信道深度融合是一种比单独使用任一信息源更强的 PUF 攻击范式。这一发现对 PUF 安全评估具有重要启示：PUF 设计者在评估抗攻击能力时，必须同时考虑 CRP 和物理侧信道两个维度的联合威胁。

### 5.2 工业价值

- **PUF 安全评估的升级**：当前 PUF 安全评估通常独立测试 CRP 建模攻击和 SCA 攻击——DeepPUFSCA 证明这种分离式评估低估了真实攻击者的能力。联合评估应成为新的业界标准。
- **PUF 设计启示**：对抗联合攻击需要在两个维度同时加强防护——CRP 混淆（如 XOR Arbiter PUF）+ 功耗掩蔽（如双轨逻辑）。

### 5.3 未来方向

> **联合攻击其他 PUF 类型**：将 CRP + SCA 深度融合方法扩展到 Ring Oscillator PUF、SRAM PUF、Butterfly PUF。
> **EM + 功耗多模态融合**：将电磁辐射也纳入融合模型，构建三模态 PUF 攻击。

---

## 六、个人思考

1. **"孤立的防御假设"是 PUF 安全的最大盲区**：PUF 社区长期将 CRP 攻击和 SCA 攻击视为两个独立威胁，DeepPUFSCA 打破了这堵墙——攻击者永远会选择最有利的组合，防御者不应假设对手只用一种武器。

2. **QUB 团队的 PUF 研究体系化优势**：从 DeepPUFSCA 到之前一批工作，QUB 团队展现了 PUF 攻击研究的体系化——从 FPGA 实测到 DL 方法论到开源数据集，形成了一个完整的评估 pipeline。

---

## 七、相关资源与延伸阅读

- **QUB Pure 预印本**：[https://pure.qub.ac.uk/en/publications/deeppufsca](https://pure.qub.ac.uk/en/publications/deeppufsca)（CC BY）
- **PUF 综述**：Gao et al., "Physical Unclonable Functions" (Nature Electronics, 2020)
- **CRP 建模攻击**：Rührmair et al., "PUF Modeling Attacks on Simulated and Silicon Data" (IEEE TIFS, 2013)
- **Arbiter PUF**：Lim et al., "Extracting Secret Keys from Integrated Circuits" (IEEE TVLSI, 2005)
- **XOR Arbiter PUF**：Suh & Devadas, "Physical Unclonable Functions for Device Authentication" (DAC 2007)
