---
title: "ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "post-quantum-cryptography"
  - "computing-in-memory"
  - "analog-computing"
  - "mceliece"
  - "qc-mdpc"
---

# ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test。针对后量子密码算法 QC-MDPC McEliece 在加密和密钥生成中的数字化性能瓶颈，首次提出基于模拟存内计算（Analog CIM）的加速器 ACIM-QMM，打破传统数字计算范式在 PQC 中的吞吐与能效限制，以极低相对误差实现高效密钥生成与密文加密。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Post-Quantum Cryptography · Computing-in-Memory · Analog Computing · McEliece · QC-MDPC</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem（ACIM-QMM：面向 QC-MDPC McEliece 密码系统的高效模拟存内计算加速器） |
| 作者 | P. Xiao, Z. Wei, S. Du, W. Chang, Q. Hong |
| 机构 | 论文未明确公开所署机构 |
| 领域 | 硬件安全 / 后量子密码学（Hardware Security / Post-Quantum Cryptography） |
| 投稿方向 | Security（Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test） |
| 关键词 | 后量子密码(Post-Quantum Cryptography)、存内计算(Computing-in-Memory)、模拟计算(Analog Computing)、QC-MDPC 码、McEliece 密码系统(McEliece Cryptosystem) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> 随着量子计算威胁的逼近，NIST 正加速后量子密码（PQC）标准化进程。QC-MDPC McEliece 作为一类基于编码的 PQC 候选方案，其密钥生成和加密过程中的大规模稀疏矩阵-向量乘法是核心计算瓶颈。本文首次提出 ACIM-QMM，一款基于**模拟存内计算**的 QC-MDPC McEliece 加速器，利用模拟电路的固有并行性和 Ohm 定律直接完成矩阵运算，从根本上打破了数字计算的吞吐与能效瓶颈，在 256-bit 安全级别下实现了显著优于 SOTA 数字方案的面积和能效指标。

---

## 二、研究背景与动机

### 2.1 行业大背景

后量子密码（PQC）是信息安全领域当前最紧迫的工程任务之一。NIST 已于 2024 年正式发布首批 PQC 标准（CRYSTALS-Kyber、CRYSTALS-Dilithium、SPHINCS+、FALCON），并持续评估基于编码的候选方案（如 Classic McEliece、BIKE、HQC）。其中，**基于准循环中密度校验（QC-MDPC）码的 McEliece 变体**以较小的公钥尺寸和可证明安全性受到广泛关注——但其计算开销是实用化的主要障碍。

### 2.2 QC-MDPC McEliece 的计算特征

McEliece 密码系统基于纠错码的译码困难性构建。QC-MDPC 变体的核心运算包括：

- **密钥生成**：生成稀疏校验矩阵 H，需要大量稀疏矩阵运算和求逆操作。
- **加密**：明文向量与公钥（生成矩阵 G）的乘法，即**稀疏矩阵-向量乘**（SpMV）。
- **解密**：使用私钥和译码算法（如 Bit-Flipping）恢复明文。

其中，加密的 SpMV 操作虽然是 O(n²) 中的线性复杂，但 n 高达数万比特（256-bit 安全约需 n=9,000+），在传统数字电路中需要大量乘法器和加法器，功耗和面积开销显著。

### 2.3 现有方法的局限

| 局限 | 详情 |
|------|------|
| **数字计算范式瓶颈** | 数字电路中的 GF(2) 乘法本质上是按位 AND 操作，n 位的稀疏矩阵乘需要 O(n·d) 个逻辑门（d 为行重），即使 d 很小，绝对数量仍然巨大。 |
| **存储器墙** | 公钥存储和读取需要大量 SRAM 访问，数字加速器的实际性能受限于存储器带宽。 |
| **PQC 硬件加速研究集中在格密码** | 绝大多数 PQC 硬件加速工作（如 Kyber、Dilithium）聚焦于格密码，基于编码的方案硬件加速研究相对匮乏。 |

### 2.4 本文贡献

1. **首次将模拟 CIM 引入 PQC 硬件加速**：提出 ACIM-QMM，利用 ReRAM 等非易失存储器件构成的模拟存内计算阵列直接执行 GF(2) 稀疏矩阵-向量乘法，开创性地将 CIM 范式应用于后量子密码。
2. **打破数字化瓶颈**：模拟计算利用 Ohm 定律和 Kirchhoff 定律在恒定时间内完成乘累加，与矩阵规模无关——这一物理特性对 PQC 的长密钥天然友好。
3. **密钥生成与加密全流程加速**：不仅加速加密操作，还覆盖了密钥生成阶段的计算密集型运算。
4. **低相对误差验证**：在模拟计算固有噪声的条件下，证明了 ACIM-QMM 以可忽略的误差率完成正确的密码运算。

---

## 三、提出的解决方案

### 3.1 整体架构

ACIM-QMM 的核心是一个基于 ReRAM 的**模拟存内计算阵列**，其基本工作原理如下：

1. **公钥矩阵存储**：稀疏二进制公钥矩阵 G 以电导形式（高电导='1'，低电导='0'）直接存储在 ReRAM 交叉杆（Crossbar）阵列中。存储即计算。
2. **明文输入**：明文比特向量以电压形式施加在交叉杆的行线上。
3. **模拟乘累加**：每列的电流输出是各输入电压与对应电导乘积之和（Ohm 定律 + Kirchhoff 电流定律），即完成了向量-矩阵乘法的模拟计算。
4. **阈值判决**：列电流经灵敏放大器与参考阈值比较，输出 GF(2) 运算结果。

**为什么 CIM 适合 QC-MDPC？** QC-MDPC 的矩阵是准循环且稀疏的——这意味着矩阵可以被紧凑地映射到 Crossbar 子阵列，稀疏性减少了需要编程的 ReRAM 单元数量，而循环结构允许通过移位寄存器复用阵列，大幅降低硬件开销。

### 3.2 核心创新点详解

#### 创新点 1：模拟域 GF(2) 乘累加

- **解决了什么？** 数字电路中，n 位 GF(2) 向量-矩阵乘需要 n·d 个 AND 门和加法器；随着 n 增加，面积和功耗线性甚至超线性增长。
- **如何实现的？** 在模拟域，Crossbar 阵列天然完成乘累加——一行电压 × 一列电导 → 电流求和——复杂度 O(1)。关键挑战是灵敏放大器的判决精度，论文通过设计余量（margin）保证了在 ReRAM 器件可变性下的正确判决。

#### 创新点 2：准循环矩阵的高效存储映射

- **解决了什么？** 随意映射将浪费 Crossbar 面积（稀疏矩阵大部分单元为零电导），且循环结构未加利用。
- **如何实现的？** 利用 QC-MDPC 码的准循环结构，将多个循环块以折叠方式映射到单个 Crossbar 子阵列，通过移位寄存器动态选择当前参与计算的行，使物理 Crossbar 尺寸远小于矩阵维数 n。

#### 创新点 3：模拟-数字混合控制

- **设计要点**：模拟 CIM 的前端（DAC/ADC/灵敏放大器）和后端（密钥流调度）均采用数字逻辑控制，形成混合信号 pipeline。数字部分负责精度校准和纠错，确保模拟计算结果的可靠性。

### 3.3 实现难点

1. **ReRAM 可变性管理**：ReRAM 器件的电导编程存在单元间差异。解决方案：多级编程 + 在线校准，以及基于 GF(2) 特性对判决阈值的宽松离。
2. **模拟噪声下的密码正确性**：密码学要求绝对正确（不允许概率性输出）。解决方案：通过增大灵敏放大器判决余量和引入数字后纠错（ECC），将模拟错误率压制到密码学可接受水平（< 2⁻¹²⁸）。
3. **面积与安全级别的平衡**：256-bit 安全需要更大的矩阵 → 更大的 Crossbar。解决方案：准循环折叠映射使 Crossbar 面积与安全级别呈亚线性增长。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 实验平台 | 模拟 CIM 仿真 + ReRAM 器件模型（具体工艺节点见论文正文） |
| 密码方案 | QC-MDPC McEliece（256-bit 安全级别） |
| 对比基线 | SOTA 数字 PQC 硬件加速方案 |
| 评估指标 | 面积效率（Gbps/mm²）、能效（pJ/bit）、延迟、相对误差 |

### 4.2 核心实验结果

| 指标 | 说明 |
|------|------|
| **面积效率** | 在 256-bit 安全级别下优于 SOTA PQC 硬件方案 |
| **能效** | 模拟计算避免数字逻辑的动态功耗，能效比数字方案显著提升（具体倍数见论文正文） |
| **相对误差** | 低至密码学可接受水平，不破坏密码正确性 |
| **灵活性** | 支持多种 QC-MDPC 参数集和密钥尺寸 |

> **注**：完整性能数据和消融实验请参阅正式论文（IEEE Xplore）。

### 4.3 与数字方案的范式级对比

| 维度 | 数字加速器 | ACIM-QMM（模拟 CIM） |
|------|----------|----------------------|
| 矩阵乘法复杂度 | O(n·d) 逻辑门 | O(1) 模拟域计算 |
| 存储与计算 | 分离（SRAM + ALU） | 融合（Crossbar 即存储又计算） |
| 扩展性（n 增大时） | 面积/功耗近线性增长 | 准循环折叠下亚线性增长 |
| 精度 | 精确（数字） | 概率性但可控（模拟 + 数字校正） |

### 4.4 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **仅覆盖加密与密钥生成**（论文隐含）：解密（Bit-Flipping 译码）涉及复杂的迭代判决，不适合模拟 CIM 直接加速，仍需数字逻辑或软件处理。
- **ReRAM 工艺成熟度**（个人观点）：ReRAM 的工艺变异性和耐久性仍是工业级部署的挑战，但作为概念验证，ACIM-QMM 展示了 CIM 进入 PQC 领域的可行性。
- **与 NIST 标准化进程的耦合**（个人观点）：QC-MDPC 尚未被 NIST 正式标准化（BIKE 和 HQC 仍在评估中），ACIM-QMM 的长期价值取决于上层密码标准的选择。

---

## 五、结论与展望

### 5.1 论文结论

ACIM-QMM 首次将模拟存内计算引入后量子密码硬件加速，以 ReRAM Crossbar 的物理特性直接完成 QC-MDPC McEliece 的矩阵运算，在面积效率和能效两个方面均突破了数字方案的限制，且以可控误差保证了密码运算的正确性。这一工作为 PQC 硬件加速开辟了"模拟计算"这一全新路径。

### 5.2 工业价值

- **PQC 物联网部署的关键使能技术**：对于资源极度受限的 IoT 设备，ACIM-QMM 的能效优势意味着 PQC 可以从云端下沉到传感器端，实现端到端的后量子安全。
- **方法论的跨算法迁移**：CIM+PQC 的思路不仅限于 QC-MDPC——BIKE（同样依赖稀疏矩阵运算）和 HQC（基于 BCH/LDPC 码）也可能从类似架构中受益。
- **为 NIST 第四轮评估提供硬件数据点**：作为 QC-MDPC 方向的首个 CIM 加速器，ACIM-QMM 的硬件指标可能影响 NIST 对基于编码方案的"硬件可部署性"评估。

### 5.3 未来方向

> **个人延伸分析**：

> - **CIM 加速 BIKE/HQC**：将 ACIM-QMM 的架构思想迁移至 BIKE（Bit-Flipping Key Encapsulation）和 HQC（Hamming Quasi-Cyclic），构建统一 CIM 编码 PQC 平台。
> - **CIM for 格密码**：格密码（Kyber/Dilithium）的 NTT 和多项式乘法是否也能受益于 CIM？这是一个开放性研究问题。
> - **ReRAM + 数字协处理**：构建模拟 CIM（稀疏矩阵乘）+ 数字逻辑（Bit-Flipping 译码）的异构 SoC，覆盖 McEliece 的完整加解密流程。

---

## 六、个人思考与启发

1. **"换道超车"的范本**：ACIM-QMM 最令人印象深刻的地方在于——当数字电路领域对 QC-MDPC 矩阵乘法的优化已经"卷"到极致（复用、流水线、并行展开……），作者选择从物理计算范式层面另辟蹊径。模拟 CIM 的 O(1) 矩阵乘是数字电路无论如何都无法超越的物理上限，这种"换道"思维值得所有硬件加速研究者借鉴。

2. **PQC 硬件加速的"蓝海"**：目前 PQC 硬件社区 90% 的注意力在格密码（Kyber/Dilithium），编码密码的硬件加速研究仍是大片空白。ACIM-QMM 证明了这片"蓝海"中蕴藏着范式级创新的机遇——不只是在已有数字加速器上修修补补。

3. **对复现/后续研究的建议**：
   - 从 NeuroSim 或 DNN+NeuroSim 等开源 CIM 仿真框架入手，熟悉 Crossbar 的电学建模；
   - 在 CIM 仿真器中构建 GF(2) 稀疏矩阵-向量乘的模型，验证灵敏放大器判决余量与 BER 的关系；
   - 关注 ReRAM 器件模型中的工艺可变性参数——这会显著影响判决阈值的设置策略。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：DAC 2025 Proceedings（暂未公开 arXiv 预印本）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **QC-MDPC McEliece 相关论文**：Misoczki et al., "MDPC-McEliece: New McEliece Variants from Moderate Density Parity-Check Codes" (ISIT 2013)
- **BIKE 方案**：Aragon et al., "BIKE: Bit Flipping Key Encapsulation"（NIST PQC Round 4 Candidate）
- **CIM 入门综述**：Sebastian et al., "Memory Devices and Applications for In-Memory Computing" (Nature Nanotechnology, 2020)
- **开源 CIM 仿真工具**：NeuroSim（[GitHub](https://github.com/neurosim/DNN_NeuroSim_V2.2)）
- **NIST PQC 标准化**：[https://csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
