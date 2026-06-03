---
title: "An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "fully-homomorphic-encryption"
  - "bfv-scheme"
  - "general-matrix-multiplication"
  - "fpga-accelerator"
  - "polynomial-encoding"
---

# An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4 — Embedded and Cross-Layer Security。针对全同态加密中通用矩阵乘法（GEMM）计算效率低的瓶颈，提出面向 BFV 方案的多项式编码增强数据打包方法，支持异构尺寸输入/权重的灵活打包，并设计专用 FPGA 硬件配合优化的硬件-主机调度，在 MNIST 和 CIFAR-10 上实现最高加速比。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Fully Homomorphic Encryption · BFV Scheme · GEMM · Polynomial Encoding · FPGA Accelerator</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme（面向 B/FV 方案通用矩阵乘法的增强数据打包方法） |
| 作者 | Zijun Jiang, Yangdi Lyu, Xiangchen Meng, Yan Tan |
| 机构 | 论文未明确公开所署机构 |
| 领域 | 硬件安全 / 全同态加密（Hardware Security / Fully Homomorphic Encryption） |
| 投稿方向 | Security（Session: SEC4 — Embedded and Cross-Layer Security） |
| 关键词 | 全同态加密(FHE)、BFV 方案(BFV Scheme)、通用矩阵乘法(GEMM)、多项式编码(Polynomial Encoding)、FPGA 加速器(FPGA Accelerator) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> 全同态加密（FHE）中，通用矩阵乘法（GEMM）——机器学习推理的核心运算——面临着密文域计算效率与数据迁移带宽的双重瓶颈，且标准非线性激活函数在 FHE 中不可用、替代函数往往引入精度损失。本文提出一种面向 BFV 方案的增强多项式编码数据打包方法，支持异构尺寸矩阵的灵活打包，并配合专用 FPGA 硬件与优化的硬件-主机调度策略，在 MNIST 和 CIFAR-10 上实现面向现有方案的显著加速比。

---

## 二、研究背景与动机

### 2.1 行业大背景

FHE 推理——即在加密数据上直接执行神经网络推理——是隐私计算（PPML）的终极目标。然而，GEMM（矩阵乘加）占据了神经网络推理 90% 以上的计算量，在 FHE 中的开销极其惊人：

- **密文膨胀**：BFV/BGV 方案中单个整数被编码为高维多项式（N≥2¹⁴），存储和传输代价巨大。
- **乘法深度受限**：每次密文乘法会同时增大密文噪声和尺寸，必须在乘法累积到一定程度后执行重线性化（Relinearization）和自举（Bootstrapping）。
- **非线性函数适配**：ReLU/Sigmoid 等标准激活函数在 FHE 中需要多项式近似，精度与乘法深度之间存在 trade-off。

### 2.2 数据打包：FHE 效率的命门

在 BFV 方案中，明文是一个 N 维多项式（系数属于 ℤₜ）。**数据打包（Packing）**——将多个明文值编码进一个多项式的不同"槽位"——是实现 SIMD 并行和提高吞吐量的核心技术。对于 GEMM，打包策略直接决定了：
- 一次密文乘法能同时计算多少个标量乘法
- 后续的旋转（Rotation）操作次数和开销

不恰当的打包会导致大量冗余的密文旋转操作，严重拖慢整体吞吐量。

### 2.3 论文动机

现有 BFV GEMM 打包方案存在两个关键不足：
1. **尺寸约束严格**：多数方案假设输入矩阵尺寸与多项式度 N 完全对齐，对"非标准"尺寸的矩阵适配性差。
2. **硬件调度不协同**：打包策略的优化通常不考虑硬件加速器与主机之间的数据搬运调度，导致实际 wall-clock 性能远低于理论峰值。

### 2.4 本文贡献

1. **增强多项式编码方法**：提出适用于 BFV 方案 GEMM 的通用多项式编码策略，支持不同尺寸输入和权重的灵活数据打包。
2. **硬件-主机协同调度**：设计专用 FPGA 硬件加速器，并通过优化的任务调度策略最小化主机-FPGA 数据传输的停顿。
3. **推理全链路优化**：在 MNIST 和 CIFAR-10 上实现端到端 FHE 推理，在保持推理精度的前提下实现相比现有方案的显著加速。

---

## 三、提出的解决方案

### 3.1 整体架构

方案的总体流程如下：

1. **多项式编码阶段**（主机 CPU）：将输入矩阵和权重矩阵按照增强打包策略编码为 BFV 明文多项式。关键是选择"槽位映射"——输入矩阵的行/列如何映射到多项式系数——以最小化 GEMM 过程中的旋转操作。
2. **密文 GEMM 计算阶段**（FPGA 加速器）：在 FPGA 上执行打包后的密文-明文乘法（或密文-密文乘法）、累加和必要的重线性化。
3. **解码阶段**（主机 CPU）：将计算结果多项式解码回矩阵形式，完成后续的非线性处理。

### 3.2 核心创新点：增强数据打包

#### GEMM 分解与打包策略

对于矩阵乘法 C = A × B，BFV 方案下的核心挑战是将二维矩阵运算映射到一维多项式的 SIMD 乘法上。本文的增强打包方法的关键思路是：

- **行-列乘积的并行化**：将矩阵 A 的行打包为一个多项式，B 的对应列打包为另一个多项式，使一次多项式乘法同时计算一行与一列的内积中的多个元素积。
- **尺寸自适应**：当矩阵维度不是 N 的完美因子时，通过填充（padding）和分段（blocking）策略最优利用多项式槽位，避免因对齐约束导致的槽位浪费。
- **旋转最小化**：通过精心安排打包的多项式布局，使得 GEMM 过程中所需的密文旋转次数最小化——旋转是 FHE 中除乘法外最昂贵的操作。

#### 硬件-主机协同调度

FPGA 加速器的核心设计理念是"计算-传输重叠"：

- **双缓冲**：FPGA 片上 BRAM 采用乒乓缓冲，当一批密文正在计算时，主机预先通过 PCIe DMA 搬运下一批数据。
- **流水化 FHE 算子**：NTT/INTT、模乘累加、重线性化等 FHE 基本算子均在 FPGA 上流水化实现，使 GEMM 的核心循环以接近硬件峰值吞吐率运行。

### 3.3 实现难点

1. **BFV 方案的多项式度约束**：BFV 要求多项式度为 2 的幂（N=2ᵏ），而 GEMM 的维度是任意的。解决方案：开发了自动化的分块（tiling）算法，将任意尺寸 GEMM 分解为适配 N 的子问题，并确保跨分块的密文旋转开销最小。
2. **非线性激活函数的替换精度**：在 FHE 中无法使用 ReLU，改用低阶多项式近似（如 x² 或分段多项式），论文中验证了这些替换在 MNIST/CIFAR-10 上仅引入可忽略的精度损失。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| FHE 方案 | BFV |
| 硬件平台 | Xilinx Alveo U250 FPGA |
| 数据集 | MNIST、CIFAR-10 |
| 网络类型 | 轻量卷积神经网络 / MLP |
| 对比基线 | 现有 BFV GEMM 打包方案 |
| 评估指标 | 推理延迟、吞吐量、精度 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **加速比** | 在 MNIST 和 CIFAR-10 上实现优于现有方案的**最高加速比**（具体倍数见论文正文） |
| **推理精度** | 在 FHE 约束下保持与明文推理相当的分类精度 |
| **硬件-主机协同** | 优化的调度策略有效隐藏数据搬运延迟 |

> **注**：完整的加速比数据和消融实验请参阅论文正文（IEEE Xplore）。

### 4.3 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **限于 BFV 方案**（论文隐含）：打包方法针对 BFV 的明文编码机制（ℤₜ 系数）设计，迁移至 CKKS（浮点近似）或 BGV 需要调整。
- **网络规模受限**（个人观点）：受限于 FHE 的乘法深度预算，当前支持的网络规模仍限于浅层模型；深层网络（如 ResNet-50）需要自举支持，引入额外开销。
- **FPGA 平台的通用性**（个人观点）：Alveo U250 是数据中心级 FPGA，功耗较高；在嵌入式 FPGA 上部署的可行性有待验证。

---

## 五、结论与展望

### 5.1 论文结论

本文通过增强多项式数据打包方法，有效地提升了 BFV 方案下 GEMM 运算的密文域计算效率。结合 FPGA 加速器上的硬件-主机协同调度优化，在 MNIST 和 CIFAR-10 的实际 FHE 推理场景中实现了显著加速，证明了"算法-硬件联合优化"在 FHE 实用化中的关键价值。

### 5.2 工业价值

- **FHE 推理的工程化推进**：该工作填补了 BFV GEMM 打包与实际硬件加速之间的鸿沟，为构建实用的 FHE 推理加速器提供了端到端参考设计。
- **打包策略的通用性**：增强打包方法的思想可被迁移至 BGV、CKKS 等其他 FHE 方案的 GEMM 实现。
- **PPML 边缘部署前景**：如果 FPGA 加速器能进一步优化功耗，有望在边缘设备上实现低延迟的隐私保护推理。

### 5.3 未来方向

> **个人延伸分析**：

> - **多方案统一打包框架**：将增强打包方法扩展为 FHE 编译器自动 pass——输入任意矩阵和 FHE 方案参数，自动输出最优打包布局。
> - **自适应深度管理**：集成自举（Bootstrapping）支持，使打包方法能适配任意深度的神经网络。
> - **与 ABC-FHE 等客户端加速器协同**：客户端使用多项式编码进行高效加密，服务端使用专用 FHE ASIC 进行密文 GEMM 计算，构成完整的端-云 FHE 推理链路。

---

## 六、个人思考与启发

1. **"打包"二字承载了整个 FHE 效率的灵魂**：在 FHE 中，数据布局（data layout）的重要性远超传统计算——一次差劲的打包可能让 GEMM 慢 10 倍以上。本文的核心贡献不在于"发明了一个新的数学算子"，而在于"用更好的数学重新组织了数据"，这是系统工程思维的胜利。

2. **FHE 编译器/调度器是一个被低估的方向**：当前 FHE 加速器研究偏重硬件微架构，但本文展示了"算法调度"的同等重要性。未来可能出现类似 TVM/XLA for FHE 的编译优化框架——输入一个 PyTorch 模型，自动生成最优的 FHE 打包 + 算子调度 + 硬件配置。

3. **对复现/后续研究的建议**：
   - 先熟悉主流 FHE 库（如 OpenFHE、Microsoft SEAL）中的 BFV 打包 API，理解"BatchEncoder"的工作机制；
   - 将打包问题建模为一个组合优化问题——最小化旋转次数——本质上是"寻找最佳的行-列槽位映射"，可用 ILP 求解器实验；
   - FPGA 开发建议从 Xilinx Vitis 平台入手，复用 SEAL 的 NTT/模乘参考实现。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：DAC 2025 Proceedings（暂未公开 arXiv 预印本）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **BFV 方案原始论文**：Fan & Vercauteren, "Somewhat Practical Fully Homomorphic Encryption" (Cryptology ePrint 2012)
- **主流 FHE 库**：
  - OpenFHE：[https://github.com/openfheorg/openfhe-development](https://github.com/openfheorg/openfhe-development)
  - Microsoft SEAL：[https://github.com/microsoft/SEAL](https://github.com/microsoft/SEAL)
- **FHE GEMM 相关工作**：
  - Juvekar et al., "GAZELLE: A Low Latency Framework for Secure Neural Network Inference" (USENIX Security 2018)
  - Mishra et al., "Delphi: A Cryptographic Inference Service for Neural Networks" (USENIX Security 2020)
- **Xilinx Alveo U250**：[https://www.xilinx.com/products/boards-and-kits/alveo/u250.html](https://www.xilinx.com/products/boards-and-kits/alveo/u250.html)
