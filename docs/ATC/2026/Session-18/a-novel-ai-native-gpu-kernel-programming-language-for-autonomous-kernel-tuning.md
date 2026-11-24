# A Novel AI-Native GPU Kernel Programming Language for Autonomous Kernel Tuning

**中文标题**：一种面向自主内核调优的新型 AI 原生 GPU 内核编程语言

**所属 Session**：[Session 18: Programming Languages and Compilers](index.md) · [ATC 2026](../index.md)

**作者**：Heng Shi (Shanghai Enflame Intelligence Technologies Co.,Ltd.; Shanghai Jiao Tong University), Xiaofeng Guan (Shanghai Enflame Intelligence Technologies Co.,Ltd.; Shanghai Jiao Tong University), Sijie Wu (Shanghai Enflame Intelligence Technologies Co.,Ltd.), Enming Fan (Shanghai Enflame Intelligence Technologies Co.,Ltd.), Chenpeng Wu (Shanghai Jiao Tong University), Qiqi Gu (Shanghai Jiao Tong University), Jiahang Xie (Shanghai Enflame Intelligence Technologies Co.,Ltd.), Guoqing Bao (Shanghai Enflame Intelligence Technologies Co.,Ltd.), Jianguo Yao (Shanghai Jiao Tong University)

## 英文摘要
Autonomous LLM-driven kernel tuners have proliferated in 2025–2026, yet none produces kernels that match vendor libraries on the operators those libraries target, such as cuBLAS GEMM or cuSPARSELt sparse GEMM on Hopper GPUs. Two critical gaps explain this ceiling. First, every existing system tunes parameters within a human-supplied skeleton, so the agent cannot explore architectural alternatives such as warp specialisation, pipeline topology, or persistence mode. Second, the programming substrates these systems rely on impose compounding obstacles: large per-iteration token footprints, coupled code sites that fan a single structural change into many scattered edits, and absent compile-time feedback when a configuration is infeasible. This paper presents the first AI-native GPU kernel programming language, co-designed with AI tuning to close both gaps. In a six-DSL comparison on the same agent, H800 GPU, and iteration budget, our approach is the only programming substrate whose AI-tuned kernels consistently outperform vendor libraries, averaging 1.23× across cuBLAS, CUTLASS, and cuSPARSELt on 95 production shapes. Trajectory analysis shows that the breakthroughs stem from structural kernel discoveries (warp specialisation, pipeline staging, TMA) rather than parameter search alone, enabled by two co-design axes. Syntax–context co-design makes structural edits practical: decoupled primitives yield the fewest code sites per feature, cutting the token footprint 1.6× below equal-expressiveness DSLs and raising compile pass@1 to 85.7% (95.6% pass@5). Compiler–harness co-design amplifies this through compile-time pruning and structured diagnostics, sustaining 82.1% pass@1 on dynamic-shape kernels (Triton 48%) and 82.3% under moderate-capacity models where competing DSLs collapse (Triton 65.8%).

## 中文摘要
由 LLM 驱动的自主内核调优器在 2025—2026 年大量涌现，然而在厂商库所针对的那些算子上，例如 Hopper GPU 上的 cuBLAS GEMM 或 cuSPARSELt 稀疏 GEMM，这些系统没有一个能产出与厂商库相当的内核。两个关键缺口解释了这一性能上限。第一，现有系统都在人工给定的骨架内调优参数，因此智能体无法探索诸如 warp 特化、流水线拓扑或持久化模式之类的架构性替代方案。第二，这些系统所依赖的编程基底带来叠加的障碍：每次迭代巨大的 token 占用、耦合的代码点会把单个结构性改动扩散为大量零散编辑，以及当配置不可行时缺少编译期反馈。本文提出首个 AI 原生 GPU 内核编程语言，它与 AI 调优协同设计，以弥合上述两个缺口。在同一智能体、同一 H800 GPU 和相同迭代预算下进行的六种 DSL 对比中，我们的方法是唯一一种其 AI 调优内核能稳定超过厂商库的编程基底，在 95 个生产形状上相对 cuBLAS、CUTLASS 和 cuSPARSELt 平均达到 1.23×。轨迹分析表明，突破来自结构性内核发现（warp 特化、流水线分级、TMA）而非单纯的参数搜索，这一点由两个协同设计轴所支撑。语法—上下文协同设计使结构性编辑变得可行：解耦的原语对每个特性产生的代码点最少，使 token 占用比同等表达力的 DSL 低 1.6×，并把编译 pass@1 提升至 85.7%（pass@5 为 95.6%）。编译器—运行框架协同设计通过编译期剪枝与结构化诊断进一步放大这一优势，在动态形状内核上保持 82.1% 的 pass@1（Triton 为 48%），在中等容量模型上保持 82.3%，而在同等条件下竞争的 DSL 则大幅下滑（Triton 为 65.8%）。

## 英文关键词
GPU kernel programming language, AI autotuning, autonomous kernel optimisation, LLM agents, structured sparsity

## 中文关键词
GPU 内核编程语言，AI 自动调优，自主内核优化，LLM 智能体，结构化稀疏

[返回 Session 18](index.md) · [返回 ATC 2026](../index.md)
