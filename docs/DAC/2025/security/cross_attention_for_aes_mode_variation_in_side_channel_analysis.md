---
title: "Cross-Attention for AES Mode Variation in Side-Channel Analysis"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "side-channel-analysis"
  - "aes"
  - "cross-attention"
  - "domain-adaptation"
  - "deep-learning"
---

# Cross-Attention for AES Mode Variation in Side-Channel Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3 — Hardware Security: Attack & Defense。针对深度学习侧信道分析中 AES 加密模式不匹配导致的跨模式迁移难题，首次提出基于无监督域自适应（UDA）与交叉注意力机制（Cross-Attention）的 DL-SCA 框架，无需目标模式标签即可在 5 种不同 AES 模式下实现鲁棒的跨模式攻击。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Side-Channel Analysis · AES · Cross-Attention · Domain Adaptation · Deep Learning</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Cross-Attention for AES Mode Variation in Side-Channel Analysis（面向 AES 模式变化的交叉注意力侧信道分析） |
| 作者 | Fanliang Hu, Haoyu Ma, Jian Shen, Qingming Jonathan Wu |
| 机构 | 论文未明确公开所署机构 |
| 领域 | 硬件安全 / 侧信道分析（Hardware Security / Side-Channel Analysis） |
| 投稿方向 | Security（Session: SEC3 — Hardware Security: Attack & Defense） |
| 关键词 | 侧信道分析(Side-Channel Analysis)、AES、交叉注意力(Cross-Attention)、域自适应(Domain Adaptation)、深度学习(Deep Learning) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> 深度学习侧信道分析（DL-SCA）的"可移植性"是实用化的最大障碍：攻击者在一种 AES 加密模式（如 ECB）上训练的模型，切换到另一种模式（如 CBC）时性能急剧下降，因为功耗迹线的统计分布随加密模式而变化。本文首次将**无监督域自适应（UDA）与交叉注意力机制**引入 DL-SCA，通过在特征空间对齐不同加密模式的高维功耗迹线，消除模式不匹配导致的分布偏移，在 5 种 AES 模式下实现无需目标模式标签的鲁棒攻击。

---

## 二、研究背景与动机

### 2.1 DL-SCA 的基本原理

深度学习侧信道分析（DL-SCA）利用 CNN/MLP 等模型从芯片的功耗/电磁辐射迹线中学习敏感信息（如 AES 密钥字节）与物理可观测信号之间的统计相关性。相比传统模板攻击和 CPA（相关功耗分析），DL-SCA 能捕捉非线性泄漏模式，攻击效率更高。

### 2.2 可移植性问题：为什么加密模式变化是"杀手"？

AES 有多种工作模式——ECB（电子密码本）、CBC（密码块链接）、CFB（密码反馈）、OFB（输出反馈）、CTR（计数器）。不同模式改变了明文与密文之间的数据流关系，导致：

- **功耗迹线的时间结构不同**：CBC 有 IV 异或、ECB 无；CTR 有计数器递增
- **泄漏点分布不同**：不同模式在不同轮次/操作上产生可区分的泄漏
- **噪声特征不同**：模式改变导致算法层级的"伪信号"被 DL 模型误当作密钥泄漏信号

**结果**：在 ECB 模式上训练的 DL-SCA 模型对 CBC 模式的攻击准确率可能从 95% 暴跌至接近随机猜测水平。

### 2.3 现有方法的局限

| 方法 | 局限 |
|------|------|
| 重新采集目标模式训练数据 | 在实际攻击场景中不可行——攻击者无法"要求"受害者切换到训练所用的加密模式 |
| 多模式混训 | 需要所有模式的已标注功耗迹线（已标注 = 已知密钥），采集代价极高 |
| 传统域自适应 | 直接将 CV 领域的 DANN/MMD 方法迁移到 SCA 迹线效果不佳——SCA 迹线信噪比极低，域偏移细腻 |

### 2.4 本文贡献

1. **首个面向 SCA 的 UDA 框架**：将无监督域自适应引入侧信道分析，解决跨 AES 模式攻击的可移植性难题。
2. **交叉注意力机制**：在源域和目标域功耗迹线之间建立交叉注意力对齐，使模型自动聚焦于模式无关的泄漏特征。
3. **5 种 AES 模式验证**：在 ECB、CBC、CFB、OFB、CTR 五种模式下系统验证了跨模式攻击的鲁棒性。

---

## 三、提出的解决方案

### 3.1 整体架构

该框架是一个典型的 UDA（无监督域自适应）架构：

1. **共享特征提取器**：浅层 CNN（Conv1D 为主）从功耗迹线中提取多尺度时序特征。
2. **交叉注意力模块**：
   - 源域特征（已知模式、已知密钥）和目标域特征（目标模式、未知密钥）进入交叉注意力层
   - 每个域的特征去查询另一个域的特征 → 对齐相关的泄漏模式
   - 注意力权重识别模式间共享的"密钥相关"特征，抑制模式特定的"伪特征"
3. **分类器（S-Box 密钥字节预测）**：仅使用源域标签训练，通过域对齐后的特征在目标域上实现推断。

### 3.2 核心创新：交叉注意力解决 SCA 域偏移

**为什么用交叉注意力而非简单的 MMD 对齐？**

MMD（Maximum Mean Discrepancy）或 CORAL 等传统域对齐方法试图在全局统计层面拉近两个域的分布——这适用于 CV 任务（图片整体风格差异），但对 SCA 迹线可能"矫枉过正"：功耗迹线中有意义的泄漏通常集中在极短的时间窗口（几个时钟周期），全局对齐可能淹没这些局部信息。

交叉注意力的优势在于：
- **局部敏感性**：注意力机制天然地聚焦于迹线中的关键时间位置
- **配对学习**：允许模型学习"源域的 t₁ 时间点对应目标域的 t₂ 时间点"——这对 AES 不同模式下的时序偏移（如在 ECB 是第 10 轮、在 CBC 可能前移到第 9 轮）至关重要

### 3.3 实现难点

1. **低 SNR 下的注意力学习**：SCA 迹线的信噪比极低（单条迹线的信号几乎淹没在噪声中），交叉注意力需要大量迹线来学习稳定的对齐。解决：使用大批量（batch）训练 + 迹线平均增强。
2. **跨模式的泄漏语义一致性**：AES 不同模式下的"同一密钥字节"泄漏在物理上是否真的可对齐？论文通过实验证明了答案——是的，AES S-Box 输出在第一轮和最后一轮的泄漏在不同模式下具有跨模式的物理一致性。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 目标算法 | AES-128 |
| 加密模式 | ECB, CBC, CFB, OFB, CTR（5 种） |
| 功耗迹线采集 | 标准 SCA 实验平台（芯片/FPGA + 示波器） |
| 深度学习模型 | CNN + 交叉注意力 |
| 对比基线 | 无 DA 的 DL-SCA、传统 DA 方法（DANN, MMD） |
| 评估指标 | 猜测熵（Guessing Entropy）、攻击成功率 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **跨模式攻击鲁棒性** | 在 5 种 AES 模式间实现一致的攻击成功率 |
| **对 UDA 的需求** | 交叉注意力 + UDA 显著优于无 DA 和传统 DA 方法 |
| **先验知识需求** | 不需要目标模式的标签或密钥信息 |

### 4.3 局限性分析

- **AES 特化**：交叉注意力的调优可能对 AES 的特定泄漏模型有效，对其他算法（如 SM4、ChaCha20）的泛化性需要验证。
- **硬件平台的迁移**：不同芯片（STM32 vs XMEGA vs FPGA）的功耗特性不同，模式间 + 平台间的双重域偏移是否仍可解决？(个人观点)
- **计算开销**：交叉注意力的额外计算量是否在嵌入式攻击设备（如 ChipWhisperer）上可接受？

---

## 五、结论与展望

### 5.1 论文结论

本文证明了交叉注意力 + UDA 可以有效解决 DL-SCA 中因 AES 加密模式不匹配导致的可移植性问题。在 5 种 AES 模式下的广泛验证表明，该框架在无需目标模式标签的前提下维持了鲁棒的侧信道攻击性能。

### 5.2 工业价值

- **SCA 评估工具的实用化**：安全评估实验室可以使用单一模式的训练数据对不同模式的目标设备进行评估，大幅降低成本。
- **推动 SCA 防御标准升级**：既然跨模式攻击已可行，芯片安全认证（如 Common Criteria）需要将"模式切换防御"纳入评估要求。

### 5.3 未来方向

> **跨算法 + 跨平台的联合 UDA**：将交叉注意力从"跨 AES 模式"扩展到"跨密码算法"（AES → SM4）和"跨硬件平台"（STM32 → FPGA）。

---

## 六、个人思考

1. **SCA 与 CV 的"交叉授粉"正在加速**：交叉注意力最初来自 NLP（Transformer），后被 CV 采纳，现在又进入 SCA——安全硬件社区应保持对 ML 前沿的敏锐度。
2. **"攻击工具的进化"即"防御需求的进化"**：每出现一种新的攻击能力（如跨模式 SCA），就是对手握最低防御要求的一次提升。

---

## 七、相关资源与延伸阅读

- **论文原文**：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **DL-SCA 综述**：Picek et al., "SoK: Deep Learning-Based Physical Side-Channel Analysis" (ACM Computing Surveys, 2023)
- **域自适应方法**：Ganin et al., "Domain-Adversarial Training of Neural Networks" (DANN, JMLR 2016)
- **ChipWhisperer**：[https://github.com/newaetech/chipwhisperer](https://github.com/newaetech/chipwhisperer)（开源 SCA 实验平台）
