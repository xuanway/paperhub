RISCSmith: Finding RISC-V CPU Bugs via Rich Instruction Construction and On-the-Fly Differential Analysis
Authors：
[Xudong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8112718463187443487)，[Yuanliang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=68084503999232733931)，[Zehong Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9867731436752553117)，[Zhen Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=9064435546496561841)，[Fuchen Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4903699100820810442)，[Dalong Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=36921512678161418651)，[Yu Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=572143)

## 中文标题

RISCSmith：通过丰富的指令构造与即时差分分析发现 RISC-V CPU 缺陷

## 英文摘要

Processors are the foundation of all computing systems, yet complex RTL and microarchitectural front ends make logic defects difficult to eliminate and extremely costly to fix after tape-out. Although RISCV fuzzing has revealed many bugs in practice, existing approaches remain limited: they rely on manually maintained instruction models and generate insufficiently rich CPU test programs. Moreover, they lack precise register and memory monitoring, and either perform high-overhead per-instruction differential checks or coarse end-of-program comparisons – both making bug analysis and localization inefficient. In this work, we propose RISCSmith (30K+ Rust LoC), a fuzzing framework aimed at detecting bugs in RISC-V CPUs. First, RISCSmith automatically builds rich instruction models by parsing the RISC-V UnifiedDB to extract structured instruction metadata, resolve inconsistencies, and generate strongly typed models capturing operand roles and runtime semantics. Second, RISCSmith instruments RISC-V implementations with lightweight logging to collect per-instruction register, memory, and exception data, performing on-the-fly differential analysis to pinpoint the first divergence, classify its cause, and minimize the reproducing test case. We implemented and evaluated RISCSmith on six widely used RISC-V CPUs. In total, it uncovered 18 previously unknown bugs. Compared to state-of-the-art CPU fuzzers like Cascade and RISCV-DV, RISCSmith detects 3.5x and 2.6x more bugs and covers 37% and 61% more branches, respectively.

## 中文摘要

处理器是所有计算系统的基础，然而复杂的 RTL 与微架构前端使得逻辑缺陷难以消除，且流片后修复代价极高。尽管 RISC-V 模糊测试在实践中已揭示了许多缺陷，但现有方法仍存在局限：它们依赖人工维护的指令模型，所生成的 CPU 测试程序丰富度不足。此外，它们缺乏精确的寄存器与内存监控，要么执行开销高昂的逐指令差分检查，要么仅做粗粒度的程序末尾比较——这两者都使缺陷分析与定位效率低下。本文提出 RISCSmith（3 万行以上 Rust 代码），一个面向 RISC-V CPU 缺陷检测的模糊测试框架。首先，RISCSmith 通过解析 RISC-V UnifiedDB 自动构建丰富的指令模型，提取结构化指令元数据、消解不一致之处，并生成强类型模型以刻画操作数角色与运行时语义。其次，RISCSmith 对 RISC-V 实现进行插桩以进行轻量级日志记录，采集逐指令的寄存器、内存与异常数据，执行即时差分分析以定位首个分歧点、归类其成因并最小化可复现的测试用例。我们在六款广泛使用的 RISC-V CPU 上实现并评估了 RISCSmith。总体而言，它发现了 18 个此前未知的缺陷。与 Cascade 和 RISCV-DV 等最先进 CPU 模糊测试器相比，RISCSmith 分别多检测出 3.5 倍和 2.6 倍的缺陷，并分别多覆盖 37%和 61%的分支。
