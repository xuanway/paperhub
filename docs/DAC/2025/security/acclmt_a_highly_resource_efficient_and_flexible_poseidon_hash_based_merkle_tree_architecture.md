---
title: "AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-accelerator"
  - "zero-knowledge-proof"
  - "poseidon-hash"
  - "merkle-tree"
  - "fpga"
---

# AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test。针对零知识证明系统中 Merkle Tree 构建的硬件效率瓶颈，提出 AcclMT——一款基于 Poseidon 哈希的高资源效率灵活硬件架构，采用双引擎（叶节点引擎 + 内部节点引擎）流水线设计，为 ZK 证明生成的实时化奠定硬件基础。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Zero-Knowledge Proof · Poseidon Hash · Merkle Tree · FPGA Accelerator · Hardware Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture（AcclMT：面向 Poseidon 哈希的高资源效率与灵活 Merkle Tree 架构） |
| 作者 | Yifei Feng, Yinlong Li, Changxu Liu, Shiyong Wu, Zheng Wu, Lan Yang, Zhuoyuan Yang, Hao Zhou |
| 机构 | 论文未明确公开所署机构（根据论文信息，推测来自国内高校或研究机构） |
| 领域 | 硬件安全 / 密码学硬件加速（Hardware Security / Cryptographic Hardware） |
| 投稿方向 | Security（Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test） |
| 关键词 | Poseidon 哈希(Poseidon Hash)、Merkle 树(Merkle Tree)、零知识证明(Zero-Knowledge Proof)、FPGA 加速器(FPGA Accelerator)、ZK 友好哈希(ZK-Friendly Hash) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> 零知识证明（ZKP）的证明生成过程中，Merkle Tree 的构建是耗时最长的非代数运算环节之一——传统的 SHA-256/Keccak 哈希在 ZK 电路中会产生数万至数十万约束门，严重拖慢证明速度。本文提出 AcclMT，一款基于 ZK 友好哈希函数 Poseidon 的专用 Merkle Tree 硬件加速器，通过双引擎流水线架构和高度灵活的参数可配置设计，实现了业界领先的资源效率，为 zkEVM、zkRollup 等实时证明场景提供了可行的硬件加速路径。

---

## 二、研究背景与动机

### 2.1 行业大背景

零知识证明（ZKP）正在经历从理论到大规模工业应用的飞跃。zkRollup（如 StarkNet、zkSync、Scroll）使用 ZKP 批量验证数千笔交易；zkEVM 让以太坊兼容的智能合约在 L2 上继承 L1 的安全性；隐私计算（如 Zcash）依赖 ZKP 实现交易金额和身份的隐匿。这些应用的共同需求是：**更快地生成证明**。

证明生成的计算图包含两种主要操作：**代数运算**（MSM、NTT/FFT）和**非代数运算**（哈希函数执行）。前者已被大量硬件加速（如 pipeMSM、Ingonyama 的 GPU 方案），但后者——特别是 Merkle Tree 构建中的海量哈希调用——其加速研究相对滞后。

### 2.2 现有方法回顾与不足

| 局限 | 详情 |
|------|------|
| **传统哈希 ZK 不友好** | SHA-256/Keccak 在 ZK 电路（R1CS/AIR/Plonkish）中展开为大量布尔/算术约束，单个哈希即消耗数千门，Merkle Tree 的 O(logN) 次哈希累积极其昂贵。 |
| **Poseidon 软件实现吞吐不足** | Poseidon 是专为 ZK 设计的哈希函数（基于 Sponge + x^α S-Box），在电路中约束数极少，但纯软件实现（如 Circom 编译后）的吞吐量远不足以支撑实时证明。 |
| **通用硬件方案效率低** | 现有 FPGA/ASIC 加速方案多针对 MSM 或 NTT，缺乏面向 Merkle Tree 工作负载特征（高度流水线化、多层级并行）的专用设计。 |

### 2.3 论文动机

Merkle Tree 构建的独特之处在于其**层级流水线可并行性**：叶节点哈希（第 0 层）可完全并行化，而内部节点（第 1…logN 层）具有生产-消费依赖关系。一个高效的硬件架构需要同时利用这两种并行性，并在 FPGA 有限的 BRAM/DSP 预算下做到灵活的参数适配（不同树高、不同速率需求）。

### 2.4 本文贡献

1. **双引擎流水线架构**：创新性地将 Merkle Tree 构建分解为叶节点哈希引擎（Leaf Hash Engine）和内部节点哈希引擎（Internal Node Engine），实现层级间流水化并行。
2. **高资源效率设计**：通过 Poseidon 哈希核心的算法-硬件协同优化，在给定 FPGA 面积预算下实现最大吞吐量，资源效率优于通用 HLS 方案。
3. **参数灵活可配**：支持不同树高、不同 Poseidon 参数集（如不同轮数与宽度的置换），使同一架构可适配从轻量级 IoT 证明到 zkRollup 批处理证明的多种场景。
4. **完整 FPGA 原型验证**：在真实 FPGA 平台上实现并评估了 AcclMT，证明了其相对于纯软件方案的显著加速。

---

## 三、提出的解决方案

### 3.1 整体架构

AcclMT 的顶层设计围绕"分离关注点"原则展开：

- **叶节点哈希引擎（Leaf Hash Engine）**：以全并行方式处理输入的 Merkle Tree 叶节点（通常是交易哈希或账户状态哈希），将每个叶数据分别送入 Poseidon 置换模块，批量输出第 0 层哈希值。
- **内部节点哈希引擎（Internal Node Engine）**：以流水线方式逐层处理——每层将相邻两个哈希值拼接后送入 Poseidon 置换，输出作为上层的输入。该引擎利用层间"生产者-消费者"的 FIFO 缓冲实现流水线满载。

**设计关键洞察**：叶节点哈希是"宽而浅"（大量独立输入 → 一层哈希），内部节点哈希是"窄而深"（逐层归并 → logN 层）。用两个异构引擎分别优化这两种模式，比用统一引擎去兼顾两者更高效。

### 3.2 Poseidon 哈希硬件化核心挑战

Poseidon 的 Sponge 构造包含 `R_F` 轮完整 S-Box（x^α）+ `R_P` 轮部分 S-Box（仅对单个元素）。硬件化的核心挑战：

1. **S-Box 计算**：x^α（通常 α=5）在 GF(p) 上需要模幂运算——软件中很慢，但在硬件中可通过有限域乘法器链流水化实现。
2. **线性层**：MDS 矩阵乘法——全连接线性变换，是 DSP 使用量的主要来源。
3. **轮函数调度**：完整轮和部分轮的计算量不对称，简单的每轮一硬件模块方案会造成大量空闲。

### 3.3 核心设计技巧

> 由于论文实验细节未在公开摘要中全面展开，以下分析综合了 Poseidon 硬件加速的通用设计原理与论文标题所揭示的设计思路。

- **轮函数折叠（Round Folding）**：不是为每轮实例化独立硬件，而是通过循环迭代复用同一组硬件单元（乘法器 + 加法器），以时间换面积，仅在需要更高吞吐时展开更多轮。
- **MDS 矩阵乘法优化**：利用 MDS 矩阵的循环结构或稀疏性减少乘法次数，优先使用移位-加法替代全乘法。
- **双引擎负载均衡**：通过可配的 FIFO 深度和叶节点批量大小，使 Leaf Engine 和 Internal Node Engine 之间的数据流动速率匹配，减少流水线气泡。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 实验平台 | FPGA（具体型号见论文正文） |
| 目标哈希 | Poseidon 置换（Sponge 构造） |
| Merkle Tree 高度 | 可配置（支持 16–32 层典型范围） |
| 对比基线 | 纯软件 Poseidon 实现、通用 FPGA HLS 方案 |
| 评估指标 | 吞吐量（hashes/s）、资源利用率（LUT/BRAM/DSP）、延迟 |

### 4.2 核心实验结果

| 指标 | 说明 |
|------|------|
| **吞吐量** | 相比纯软件实现实现数量级加速（具体倍数见论文正文） |
| **资源效率** | 在给定 FPGA 面积下实现高于通用 HLS 方案的哈希吞吐密度 |
| **灵活性验证** | 成功适配多种 Poseidon 参数集和树高配置 |

> **注**：完整的性能数和消融实验数据需参阅正式论文（IEEE Xplore）。本文分析基于公开摘要及 ZK 硬件加速领域的通用认知。

### 4.3 与 SOTA 方案对比分析

| 方案 | 类型 | 哈希函数 | 特征 |
|------|------|----------|------|
| AcclMT（本文） | FPGA 加速器 | Poseidon | 双引擎、高资源效率、灵活可配 |
| ZK-Tracer (arXiv 2026) | 异构加速器 | Poseidon | 引用 AcclMT 作为关键基线 |
| 通用 GPU 方案 | GPU 软件 | Poseidon | 高吞吐但延迟大、功耗高 |

### 4.4 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **仅加速 Merkle Tree 环节**（论文隐含）：AcclMT 聚焦于哈希树构建，不涵盖 MSM 和 NTT 等 ZKP 的其他计算密集型环节。完整的 ZKP 加速器需要与这些模块协同工作。
- **Poseidon 的特异性**（个人观点）：虽然 Poseidon 是当前最流行的 ZK 友好哈希，但新的哈希函数（如 Monolith、Reinforced Concrete）正在涌现。AcclMT 的 Poseidon 专属设计能否平滑迁移至新哈希函数值得关注。
- **FPGA vs ASIC**（个人观点）：FPGA 验证了架构可行性，但 zkRollup 级别的吞吐需求可能需要 ASIC 实现，工艺迁移和功耗优化是后续方向。

---

## 五、结论与展望

### 5.1 论文结论

AcclMT 展示了以 ZK 友好哈希函数 Poseidon 为核心的 Merkle Tree 硬件加速架构。通过双引擎流水线设计和资源高效优化，在 FPGA 平台上实现了显著优于软件方案的性能，为 ZKP 证明系统的实时化提供了关键的硬件组件。

### 5.2 工业价值

- **zkRollup 实时证明**：作为 zkRollup 证明生成的加速组件，AcclMT 有助于缩短 L2 交易的最终确认时间（finality），改善用户体验。
- **嵌入式 ZK 应用**：资源效率优势使 AcclMT 有望部署于资源受限的边缘设备，推动物联网场景下的隐私保护计算。
- **方法论参考价值**：双引擎分离设计范式为其它 ZK 硬件加速器（如 zkVM trace generation）提供了可复用的架构思路（已被 ZK-Tracer 等后续工作引用）。

### 5.3 未来方向

> **个人延伸分析**：

> - **多哈希统一架构**：将双引擎思想扩展为"可替换哈希核心"——通过统一接口接入 Poseidon、Monolith、Griffin 等不同 ZK 友好哈希，提升架构的生命周期。
> - **与 MSM 加速器集成**：将 AcclMT 与现有 MSM/NTT 加速方案整合为完整的 ZKP 协处理器 IP，提供"一站式"硬件证明加速。
> - **ASIC 迁移**：在更先进工艺节点下评估 AcclMT 架构的 ASIC 实现指标（面积、功耗、吞吐），为大规模部署做工程化准备。

---

## 六、个人思考与启发

1. **"专用"优于"通用"的又一例证**：AcclMT 最令人印象深刻的设计选择是放弃支持 SHA-256/Keccak——这在传统硬件安全加速器看来是"功能阉割"，但在 ZKP 的语境下恰恰是最佳决策：Poseidon 在电路中的约束数仅为 SHA-256 的约 1/100，专用硬件加速的性价比远高于通用方案。

2. **ZK 加速正从"学院派"走向"工业化"**：AcclMT 的出现以及被后续工作引用，标志着 ZKP 硬件加速正从 MSM/NTT 的"低垂果实"向 Merkle Tree、Keccak 等更细粒度的模块延伸，产业化的基础设施正在被逐块搭建。

3. **对复现/后续研究的建议**：
   - 先通过软件实现（如 `poseidon-rs`、Circom 中的 Poseidon 模板）理解 Poseidon 置换的 Sponge 构造和轮函数；
   - FPGA 开发建议从 Xilinx Vitis HLS 起步，快速迭代双引擎架构的参数配置；
   - 重点关注 Poseidon 参数选择（安全性 vs 硬件友好度的 trade-off），这直接影响电路深度和 DSP 用量。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：DAC 2025 Proceedings（暂未公开 arXiv 预印本）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **Poseidon 哈希原始论文**：Grassi et al., "Poseidon: A New Hash Function for Zero-Knowledge Proof Systems" (USENIX Security 2021)
- **ZK 硬件加速综述**：Zhang et al., "A Survey of Hardware Acceleration for Zero-Knowledge Proofs" (arXiv)
- **引用 AcclMT 的后续工作**：ZK-Tracer: A High-Performance Heterogeneous Accelerator for Zero-Knowledge VM Trace Generation (2026)
- **开源 Poseidon 实现**：
  - `poseidon-rs`（Rust）：[https://github.com/arnaucube/poseidon-rs](https://github.com/arnaucube/poseidon-rs)
  - `circomlib`（Circom + JS）：[https://github.com/iden3/circomlib](https://github.com/iden3/circomlib)
- **代表性 ZKP 系统**：
  - zkSync：[https://zksync.io/](https://zksync.io/)
  - Scroll：[https://scroll.io/](https://scroll.io/)
  - StarkNet：[https://starknet.io/](https://starknet.io/)
