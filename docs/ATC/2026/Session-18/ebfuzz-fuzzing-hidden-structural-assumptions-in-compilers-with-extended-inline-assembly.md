# EBFuzz: Fuzzing Hidden Structural Assumptions in Compilers with Extended Inline Assembly

**中文标题**：EBFuzz：用扩展内联汇编模糊测试编译器中的隐藏结构性假设

**官方议程标题**：EBFuzz: Breaking Hidden Structural Assumptions in Compilers via Extended Assembly Injection

**所属 Session**：[Session 18: Programming Languages and Compilers](index.md) · [ATC 2026](../index.md)

**作者**：Jiangchang Wu (State Key Laboratory for Novel Software Technology, Nanjing University), Yibiao Yang (State Key Laboratory for Novel Software Technology, Nanjing University)

## 英文摘要
Compilers are critical infrastructure whose correctness affects every program they translate. Automated compiler testing has uncovered thousands of bugs in production compilers such as GCC and LLVM. However, existing compiler fuzzers primarily explore programs with conventional control-flow and data-flow structures because they generate inputs through ordinary language constructs. Consequently, an important testing dimension remains largely unexplored: the handling of legal but structurally unusual programs. This paper presents EBFuzz, a compiler fuzzer designed to systematically explore this neglected testing dimension. Our key insight is that GNU C extended inline assembly provides a rare mechanism for influencing the control-flow and data-flow information used by compiler analyses. Because the compiler cannot fully analyze the semantics of inline assembly, it must conservatively model the effects described by programmer-provided declarations. EBFuzz exploits this capability to systematically construct legal yet structurally unusual programs through control-flow edge injection and data-flow perturbation. The resulting programs remain valid and compilable, yet are difficult or impossible for existing compiler fuzzers to generate through conventional source-level mutations. We evaluate EBFuzz on GCC and LLVM against representative compiler testing approaches spanning random generation, coverage-guided mutation, and real-world code injection. EBFuzz discovers 80% more unique bugs than the strongest baseline and is the only approach that continues finding new bugs beyond the first fifteen hours of testing. It achieves 5.9 and 5.6 percentage points higher branch coverage on GCC and LLVM, respectively, with the largest gains occurring in compiler components responsible for processing control-flow and data-flow information. Overall, EBFuzz discovered 10 previously unknown compiler bugs, 9 of which have been confirmed or fixed by developers.

## 中文摘要
编译器是关键基础设施，其正确性影响它所翻译的每一个程序。自动化编译器测试已在 GCC 和 LLVM 等生产编译器中发现了数千个缺陷。然而，现有编译器模糊测试器主要通过普通语言构造生成输入，因此只探索具有常规控制流与数据流结构的程序。于是，一个重要测试维度在很大程度上仍未被探索：对合法但结构异常的程序的处理。本文提出 EBFuzz，一个旨在系统探索这一被忽视测试维度的编译器模糊测试器。我们的核心洞见是：GNU C 扩展内联汇编提供了一种罕见机制，可以影响编译器分析所使用的控制流与数据流信息。由于编译器无法完整分析内联汇编的语义，它必须保守地对程序员提供的声明所描述的效果建模。EBFuzz 利用这一能力，通过控制流边注入和数据流扰动，系统地构造合法但结构异常的程序。所生成的程序依然有效且可编译，但现有编译器模糊测试器通过常规源码级变异难以或无法生成它们。我们在 GCC 和 LLVM 上评估 EBFuzz，与涵盖随机生成、覆盖率引导变异和真实代码注入的代表性编译器测试方法进行比较。EBFuzz 发现的唯一缺陷比最强基线多 80%，并且是唯一在测试的最初十五小时之后仍持续发现新缺陷的方法。它在 GCC 和 LLVM 上分别取得高出 5.9 和 5.6 个百分点的分支覆盖率，最大增益出现在负责处理控制流与数据流信息的编译器组件中。总体而言，EBFuzz 发现了 10 个此前未知的编译器缺陷，其中 9 个已被开发者确认或修复。

## 英文关键词
compiler testing, fuzzing, inline assembly

## 中文关键词
编译器测试，模糊测试，内联汇编

[返回 Session 18](index.md) · [返回 ATC 2026](../index.md)
