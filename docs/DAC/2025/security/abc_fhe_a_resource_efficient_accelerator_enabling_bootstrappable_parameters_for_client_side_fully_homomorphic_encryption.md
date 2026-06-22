---
title: "ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-accelerator"
  - "fully-homomorphic-encryption"
  - "bootstrapping"
  - "ckks"
---

# ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track  · Session: SEC1 — AI/ML Security/Privacy）针对全同态加密中客户端自举（Bootstrapping）操作的计算瓶颈，提出 ABC-FHE——一款面积与功耗高效的流式 FHE 加速器，通过可重构傅里叶引擎、片上伪随机数生成器与统一在线旋转因子生成器等创新，在 28nm 工艺下实现编码加密 1112×（vs CPU）和 214×（vs SOTA 客户端加速器）的加速比。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · FHE · Hardware Accelerator · CKKS · Bootstrapping · Streaming Architecture</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption（ABC-FHE：面向客户端全同态加密的资源高效加速器，支持可自举参数） |
| 作者 | Sungwoong Yune, Hyojeong Lee, Adiwena Putra, Hyunjun Cho, Cuong Duong Manh, Jaeho Jeon, Joo-Young Kim（全部来自 KAIST 电气工程学院） |
| 机构 | School of Electrical Engineering, KAIST（韩国科学技术院） |
| 领域 | 硬件安全 / 密码学加速器（Hardware Security） |
| 投稿方向 | Security（Session: SEC1 — AI/ML Security/Privacy） |
| 关键词 | 全同态加密(Fully Homomorphic Encryption)、自举(Bootstrapping)、CKKS 方案、流式架构(Streaming Architecture)、客户端加速器(Client-Side Accelerator) |
| 核心资源 | 论文原文：[arXiv:2506.08461](https://arxiv.org/abs/2506.08461)|

---

## 一、一句话核心摘要

> 全同态加密（FHE）中，客户端侧的编码/加密和解码/解密操作已成为新的性能瓶颈——即使使用 SOTA 客户端加速器，仍占据 ResNet-20 端到端延迟的 69.4%。本文提出 ABC-FHE，一款基于流式架构的资源高效 FHE 加速器，通过可重构傅里叶引擎（同时支持 NTT 与 FFT）、片上 PRNG 和统一在线旋转因子生成器等创新，在 28nm 工艺下仅占用 28.6 mm² 面积和 5.65 W 功耗，实现编码加密 1112×（vs CPU）/ 214×（vs SOTA 客户端加速器）以及解码解密 963×（vs CPU）/ 82×（vs SOTA）的显著加速，首次在客户端侧高效支持可自举参数（N=2¹⁴–2¹⁶）。

---

## 二、研究背景与动机

### 2.1 行业大背景

全同态加密（Fully Homomorphic Encryption, FHE）允许在**加密数据上直接执行任意计算**，从根本上解决了"数据可用不可见"的隐私难题。随着边缘 AI、联邦学习、医疗数据分析等场景对隐私保护的需求激增，FHE 的实用化成为学术界和工业界的共同目标。

然而，FHE 的计算开销极其惊人：密文运算比明文慢约 **10,000 倍**。CKKS 方案（最常用于 AI 应用）中，密文是高达 2¹⁴–2¹⁶ 次的高维多项式，每个系数为数百至上千比特的高精度整数。虽然数论变换（NTT）将多项式乘法的复杂度从 O(N²) 降至 O(NlogN)，但整体开销仍然巨大，专用硬件加速势在必行。

### 2.2 现有方法回顾与不足

FHE 加速器的研究重心长期在**服务端**——F1（MICRO 2021）、CraterLake（ISCA 2022）等 ASIC 将服务端同态计算时间大幅压缩。但这暴露了一个新问题：**当服务端不再成为瓶颈，客户端就成了瓶颈**。论文在 ResNet-20 上的实测显示：

- 客户端加密/解密占用总执行时间的 **69.4%**（即使已使用 SOTA 客户端加速器 [34]）
- 服务端 SOTA ASIC [9] 仅占 30.6%

现有客户端加速器 [3, 10, 22, 34] 存在三个关键局限：

| 局限 | 详情 |
|------|------|
| **参数规模受限** | 仅支持小参数（N=2¹³），无法支撑自举所需的 N≥2¹⁴（通常需 2¹⁶） |
| **非流式架构的 DRAM 带宽瓶颈** | 即使提高计算吞吐量，输出数据速率超出 DRAM 带宽，导致实际延迟不降反升 |
| **直接从 DRAM 取参加剧瓶颈** | SOTA 工作 [34] 从 DRAM 获取参数，进一步挤占本就紧张的带宽 |

### 2.3 论文动机与挑战

客户端的独特之处在于其工作负载特征：**编码加密需要 IFFT + NTT，解码解密需要 FFT + INTT**——即需要同时支持**浮点复数**和**整数模运算**两种截然不同的计算模式。此外，编码加密的工作量约为解码解密的 **10 倍**，这种严重不对称意味着分别为加解密设计独立模块是极大的面积浪费。

### 2.4 本文贡献

1. **客户端 CKKS 工作负载特征分析**：首次系统揭示了加密相关任务（IFFT + NTT）与解密相关任务（FFT + INTT）之间的工作负载不平衡（约 10:1）。
2. **流式可重构架构**：提出基于流式架构的双 RSC（Reconfigurable Streaming Core），支持加解密并行或独立加速，通过可重构傅里叶引擎（RFE）统一处理 NTT/FFT 两种变换。
3. **面积优化三件套**：
   - **统一在线旋转因子生成器（OTF TF Gen）**：NTT 与 FFT 共享同一硬件单元，片上存储需求降低 **99.9%**（仅需约 27 KB）。
   - **NTT 友好 Montgomery 乘法器**：通过素数选择和算法-硬件协同优化，相比 Barrett 乘法器面积减少 **67.7%**。
   - **片上 PRNG**：用 128-bit 种子在线生成掩码、误差和密钥，彻底消除从外部内存读取随机数的需求。
4. **显著性能提升**：28nm 工艺下，编码加密 1112×（vs CPU）/ 214×（vs SOTA 客户端加速器），解码解密 963×（vs CPU）/ 82×（vs SOTA）。

---

## 三、提出的解决方案

### 3.1 整体架构

ABC-FHE 的顶层包含两个同构的**可重构流式核心（RSC）**，支持三种运行模式：加倍加密吞吐、加倍解密吞吐、或同时加解密。全局暂存器（Global Scratchpad）负责从外部内存预取消息或密文，保证两个核心的数据流不断。

每个 RSC 内部包含两个关键引擎：

- **可重构傅里叶引擎（RFE）**：配备 4 条流水化 NTT 通道（PNL），同时支持 I/NTT 和 I/FFT，是系统的计算核心。
- **模运算流式引擎（MSE）**：处理 RNS 编解码、CRT（中国剩余定理）逆变换、逐元素加法和乘法等 SIMD 类操作。

**设计关键洞察**：客户端场景中，单纯提升计算吞吐量而不考虑面积和内存约束是无效的——更大的吞吐量会产生更大输出数据速率，超出 DRAM 带宽后反而引入停顿。ABC-FHE 选择**流式架构**，以恒定吞吐率运行，兼顾性能与面积。

### 3.2 核心创新点详解

#### 创新点 1：可重构傅里叶引擎（RFE）— 一个引擎同时驾驭 NTT 与 FFT

- **解决了什么？** 客户端需要 NTT（整数模运算）做加密，又需要 FFT（浮点复数运算）做解密。传统方案要么用两套独立硬件（面积翻倍），要么用软件回退（性能断崖）。
- **如何实现的？**
  1. **位宽选择**：NTT 使用 44-bit 模运算（得益于 RNS 分解后每级仅需 32–36 bit）；FFT 则从传统 FP64 压缩为**自定义 FP55 格式**（43-bit 尾数），实测自举精度（Boot. prec.）达到 23.39 bits，远超维持 AI 模型精度所需的 19.29 bits 阈值。
  2. **乘法器复用**：复数 FFT 乘法的 `(a+bi)(c+di)` 需要 4 次浮点乘法——恰好与 4 条 PNL 中的模乘法器一一对应，通过可重构控制实现硬件复用。
  3. **Radix-2ⁿ 设计**：通过分析多种 NTT/FFT 配置的乘法器开销，选择 radix-2ⁿ 架构，相比常用的 radix-2 和 radix-2² 分别减少 29.7% 和 22.3% 的乘法器数量。

#### 创新点 2：统一在线旋转因子生成器（OTF TF Gen）— 99.9% 的片上存储削减

- **解决了什么？** NTT/FFT 每级的"旋转因子"（twiddle factor）若全部预存，对于 N=2¹⁶ 需要海量片上 SRAM，这在客户端面积预算下不可接受。SOTA 方案直接从 DRAM 读取，又受限于带宽。
- **如何实现的？** OTF TF Gen 用紧凑的旋转因子种子和步长参数（仅需约 **27 KB**），在运行时动态生成 NTT 和 FFT 各自所需的旋转因子。NTT 与 FFT 共享同一生成器硬件，进一步节省面积。存储缩减超过 **99.9%**。

#### 创新点 3：NTT 友好 Montgomery 乘法器（NTT-Friendly MM）

- **解决了什么？** 模乘法是 NTT 的核心算子，传统 Barrett 或 Montgomery 乘法器面积大、流水线深。在 4 条 PNL 中，乘法器面积被乘以 4，对整体面积影响巨大。
- **如何实现的？** 通过精心构造 NTT 友好素数（形如 Q = 2^p_bw + k·2^{n+1} + 1，其中 k 满足特定稀疏形式），将 Montgomery 约简中的 QInv 乘法转化为**移位-加法**操作。从需要 3 个乘法器降至仅需 1 个（初始乘法不可省略），面积相比 Barrett 减少 **67.7%**，相比标准 Montgomery 减少 **41.2%**。

### 3.3 关键技术细节：Twiddle Factor Scheduling

NTT 的 nega-cyclic 特性要求额外的预处理和后处理（乘 ψ 因子）。ABC-FHE 的关键技巧是将预处理/后处理的乘法与旋转因子合并——通过精心排列信号流图中的旋转因子分布，使得额外的 ψ 乘法被"吸收"进已有的旋转因子乘法中，**不增加任何额外的乘法器**。这一合并技术仅在 radix-2ⁿ 架构下才能保持旋转因子的规律性，这也是选择该架构的根本原因。

### 3.4 实现难点

作者面临的核心挑战是**客户端面积的"三重挤压"**：

1. **计算单元面积**：N=2¹⁶ 时，FFT/NTT 需要大量蝶形单元和乘法器。解决途径：radix-2ⁿ + 可重构复用 + NTT 友好 MM。
2. **存储面积**：旋转因子和随机数若全部预存，SRAM 需求远超预算。解决途径：OTF TF Gen + 片上 PRNG，将存储需求压缩至约 27 KB。
3. **DRAM 带宽**：流式架构产生恒定输出速率，需确保不超过 DRAM 带宽。解决途径：选择适中的并行度（P=8），在吞吐和带宽之间找到平衡点。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 工艺节点 | 28nm |
| 目标频率 | 600 MHz |
| FHE 方案 | CKKS |
| 多项式度 N | 2¹⁴–2¹⁶（支持可自举参数） |
| 对比基线 | CPU、SOTA 客户端加速器 [34] |
| 评估方式 | ASIC 综合（面积 / 功耗）+ 性能建模 |

### 4.2 面积与功耗分解

| 组件 | 面积 (mm²) | 功耗 (W) |
|------|-----------|----------|
| 4× PNL（流水化 NTT 通道） | 10.717 | 1.397 |
| 统一 OTF TF Gen | 0.697 | 0.089 |
| 旋转因子种子存储器 | 0.046 | 0.022 |
| PRNG | — | — |
| MSE（模运算流式引擎） | — | — |
| 全局暂存器及其他 | — | — |
| **总计** | **28.638** | **5.654** |

**关键观察**：4 条 PNL 占据了约 37% 的面积和 25% 的功耗——这是计算核心的必然代价。OTF TF Gen 仅占 0.70 mm²（约 2.4% 面积），以极小代价换来了 99.9% 的存储削减，性价比极高。

### 4.3 核心性能结果

| 操作 | vs CPU | vs SOTA 客户端加速器 [34] |
|------|--------|--------------------------|
| 编码 + 加密（Enc + Encrypt） | **1112×** | **214×** |
| 解码 + 解密（Dec + Decrypt） | **963×** | **82×** |

**性能解读**：

- 编码加密相对于 SOTA 的提升（214×）远大于解码解密（82×），这与工作负载特征高度一致：编码加密的操作量约为解码解密的 10 倍，优化空间更大。
- 相对于 CPU 的提升均超过 900×，证明了专用加速器在 FHE 领域的不可替代性。

### 4.4 消融分析

> 论文通过多项对比分析验证了设计选择：

- **NTT 友好 MM vs Barrett / 标准 Montgomery**：面积分别为 11,328 vs 35,054 vs 19,255 μm²，流水线级数分别为 3 vs 4 vs 3。证明算法-硬件协同优化的有效性。
- **Radix-2ⁿ vs Radix-2 / Radix-2²**：乘法器数量分别减少 29.7% 和 22.3%，验证了架构选择的合理性。
- **FP55 vs FP64**：43-bit 尾数下 Boot. prec. 达到 23.39 bits，超过 19.29 bits 阈值，证明自定义浮点格式的充分性（原论文 Figure 3(c)）。

### 4.5 局限性分析

> 以下分析中，标注"(论文)"的来自原文，标注"(个人观点)"的为合理推论。

- **限于 CKKS 方案**（论文隐含）：ABC-FHE 针对 CKKS 的客户端工作负载进行优化，不直接支持 BGV、BFV 或 TFHE 方案。
- **功耗预算仍偏高**（个人观点）：5.65 W 对于手机类移动设备仍偏高（典型手机 SoC 的 TDP 约 3–5 W）。但对于笔记本电脑或边缘网关而言是可接受的。进一步工艺缩放（如 7nm）有望将功耗降至亚瓦特级。
- **素数选择约束**（论文）：NTT 友好 MM 对素数形式有约束，可支持的加密级数为 20–40 级——论文认为这对实际场景"绰绰有余"，但极端深度的计算可能需要更灵活的素数支持。

---

## 五、结论与展望

### 5.1 论文结论

ABC-FHE 证明了在客户端资源约束下高效支持可自举参数 FHE 的可行性。通过流式架构 + 可重构傅里叶引擎 + OTF TF Gen + NTT 友好 MM + 片上 PRNG 的五重创新组合，在 28nm 工艺下以 28.6 mm² 和 5.65 W 的代价实现了 1112×（编码加密）和 963×（解码解密）相对于 CPU 的加速比，相对 SOTA 客户端加速器也分别达到 214× 和 82×。这意味着 FHE 从"云端专属"向"端云协同"的转变迈出了关键的硬件一步。

### 5.2 工业价值

- **客户端 FHE 的硬件可行性得到验证**：ABC-FHE 首次在真实 ASIC 指标上证明了"客户端 + 可自举参数 + 合理面积功耗"的三角可行，为后续工程化奠定了基础。
- **可复用的设计方法学**：OTF TF Gen + NTT 友好 MM 的协同优化思路具有通用性——面向 FHE 的硬件设计不是"暴力堆计算单元"，而是需要在算法-硬件接口处寻找"免费午餐"。
- **工艺迁移前景**：28nm 是验证节点，若迁移至 7nm 或更先进工艺，功耗有望降至移动设备可接受的范围（<< 1 W）。

### 5.3 未来方向

> **论文作者提出的方向**（已在原文涉及）：
> - 当前设计已充分支持 20–40 级加密深度；未来可探索更灵活的素数选择以支持更多级数。（论文 Section IV-A）

> **个人延伸分析**：
> - **多方案统一架构**：将 RFE 的可重构思想从 NTT/FFT 扩展到支持 BGV/BFV/TFHE 的变换类型，构建"万能 FHE 客户端加速器"。
> - **端云协同 FHE**：客户端 ABC-FHE 处理加密解密 + 服务端 FHE ASIC 处理同态计算，构建完整隐私计算链路。
> - **与 TEE 融合**：将 ABC-FHE 与 TrustZone / SGX 等 TEE 技术结合，在安全世界中执行密钥管理，在加速器中执行密文计算，形成多层防护。

---

## 六、个人思考与启发

1. **"减法设计"的胜利**：ABC-FHE 最令人印象深刻的地方不在于它加了什么，而在于它**减了什么**——旋转因子存储减 99.9%、乘法器面积减 67.7%、外部内存访问减到极致。在面积和功耗受限的客户端场景，"做减法"比"做加法"更难，也更有价值。

2. **算法-硬件协同设计的教科书案例**：NTT 友好 MM 的设计完美展示了"为硬件改算法"的思路——不是拿标准 Montgomery 硬塞进 ASIC，而是从素数选择阶段就开始考虑硬件友好度，最终用移位-加法替代乘法。这种思路值得所有硬件加速器研究者借鉴。

3. **对复现/后续研究的建议**：
   - 先熟悉 OpenFHE 或 Lattigo（Go 语言 CKKS 库）的客户端 API，理解编码加密/解码解密的软件流程；
   - 重点阅读原论文 Section IV-A（RFE 微架构）和 Section IV-B（内存处理），这是创新的核心；
   - 如需复现，28nm 工艺的 PDK 获取可能有门槛，可先在 FPGA（如 Xilinx Alveo）上验证流式架构的可行性，再考虑 ASIC 实现。

---

## 七、相关资源与延伸阅读

- **论文原文（arXiv 预印本）**：[https://arxiv.org/abs/2506.08461](https://arxiv.org/abs/2506.08461)（2025-07 访问；7 页，6 张图）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **FHE 入门综述**：Marcolla et al., "Survey on Fully Homomorphic Encryption: Theory, Applications, and Open Problems"
- **CKKS 原始论文**：Cheon et al., "Homomorphic Encryption for Arithmetic of Approximate Numbers" (ASIACRYPT 2017)
- **主流 FHE 开源库**：
  - OpenFHE：[https://github.com/openfheorg/openfhe-development](https://github.com/openfheorg/openfhe-development)（C++，支持 CKKS/BGV/BFV/TFHE）
  - Lattigo：[https://github.com/tuneinsight/lattigo](https://github.com/tuneinsight/lattigo)（Go 语言，CKKS 实现较完善）
  - Microsoft SEAL：[https://github.com/microsoft/SEAL](https://github.com/microsoft/SEAL)
- **代表性 FHE 加速器**：
  - F1: "F1: A Fast and Programmable Accelerator for Fully Homomorphic Encryption" (MICRO 2021)
  - CraterLake: "CraterLake: A Hardware Accelerator for Efficient Unbounded Computation on Encrypted Data" (ISCA 2022)
- **论文引用参考 [34]（SOTA 客户端加速器）**：待从论文参考文献确认
- **作者机构**：KAIST School of Electrical Engineering
