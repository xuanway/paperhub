---
title: "A PN-Free Digital SAT Accelerator Using Crossbar Architecture and Frequency-Controlled Counters"
description: "HPCA 2026 · Emerging Compute Paradigms"
tags:
  - "HPCA2026"
  - "Emerging Compute Paradigms"
---

# A PN-Free Digital SAT Accelerator Using Crossbar Architecture and Frequency-Controlled Counters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Emerging Compute Paradigms。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Emerging Compute Paradigms</p>
</div>

**论文链接**：
**作者**：Zhezheng Ren University of Waterloo , Chenao Yuan University of Waterloo , Yuke Zhang University of Toronto , Shiyu Su University of Waterloo
**会议**：HPCA 2026

---

## 中文标题

基于交叉开关架构与频率受控计数器的无 PN 数字 SAT 加速器

## 英文摘要

Boolean satisfiability (SAT) solving is a foundational problem in computer science and serves as a core engine for a wide range of combinatorial optimization tasks. It underpins critical applications across formal verification, electronic design automation (EDA), artificial intelligence (AI) reasoning, cryptanalysis, bioinformatics, and constraint programming. While significant progress has been made in algorithmic improvements, these advances are gradually reaching saturation, motivating increasing attention toward domain-specific hardware accelerators beyond the von Neumann architecture. However, existing hardware SAT accelerators often face significant deployment barriers due to reliance on pseudo-random number (PN) generators, specialized analog components with sufficient intrinsic noise, or unconventional fabrication technologies such as memristors. These limitations hinder scalability, portability, and integration into mainstream digital design flows. This paper presents an intrinsically stochastic, fully digital SAT accelerator inspired by analog mixed-signal crossbar architectures. The proposed design eliminates the need for analog noise sources, PN generators, or true-random number (TN) generators, enabling a fully synthesizable, standard-cell–based implementation compatible with conventional digital flows. Digital counters are employed as “spins”, acting as oscillatory elements that store and flip variable states, thus supporting robust and scalable stochastic behavior. Stochasticity is achieved through a novel polynomial clause-to-variable feedback mechanism, which dynamically modulates oscillator frequencies based on clause satisfaction states, allowing effective exploration of the solution space without external randomness. A highly parallel crossbar structure further accelerates problem-solving by enabling concurrent evaluation of multiple clauses, aided by a proposed polynomial clause-to-variable feedback function. To validate the proposed architecture, we implemented prototypes on FPGA and three ASIC platforms including 12nm FinFET, 22nm and 65nm CMOS technologies. The designs were evaluated on a suite of hard SAT benchmark problems with 20 to 250 variables. Our 22nm ASIC accelerator achieves an approximately 3.06× speedup than the state-of-the-art 28nm 3-SAT accelerator. Compared with prior 65nm designs, ours achieves 100% solvability with comparable runtime. Notably, we present the first 3-SAT accelerator capable of handling 250 variables with 100% solvability, marking a significant advancement in scalability for digital SAT accelerators.

## 中文摘要

布尔可满足性（SAT）求解是计算机科学的基础问题，也是众多组合优化任务的核心引擎，支撑形式验证、电子设计自动化（EDA）、人工智能（AI）推理、密码分析、生物信息学与约束规划等应用。算法层面的进展正逐渐趋于饱和，促使研究转向超越冯·诺依曼架构的领域专用硬件加速器。但现有硬件 SAT 加速器常因依赖伪随机数（PN）生成器、具有足够内在噪声的专用模拟组件或忆阻器等非常规工艺而面临部署障碍，限制了可扩展性、可移植性与融入主流数字设计流程。本文提出受模拟混合信号交叉开关架构启发的内在随机全数字 SAT 加速器，无需模拟噪声源、PN 或 TN 生成器，可实现完全可综合、基于标准单元且兼容常规数字流程。数字计数器被用作“自旋”，即存储并翻转变量状态的振荡元件，支持鲁棒的随机行为；随机性来自新颖的多项式子句到变量反馈机制，依据子句满足状态动态调制振荡器频率，无需外部随机源即可探索解空间；高度并行的交叉开关结构通过并发评估多个子句加速求解。在 FPGA 以及 12nm FinFET、22nm 与 65nm CMOS 三种 ASIC 上实现原型，在变量数 20 至 250 的困难 SAT 基准上评估：22nm ASIC 相较最先进的 28nm 3-SAT 加速器取得约 3.06× 加速，与先前 65nm 设计相比在相当运行时间下达到 100% 可解性，也是首个能以 100% 可解性处理 250 个变量的 3-SAT 加速器，标志着数字 SAT 加速器可扩展性的重要进展。
