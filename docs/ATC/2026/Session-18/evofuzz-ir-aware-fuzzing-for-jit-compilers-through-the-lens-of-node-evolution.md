# EvoFuzz: IR-Aware Fuzzing for JIT Compilers through the Lens of Node Evolution

**中文标题**：EvoFuzz：以节点演化为视角的 JIT 编译器 IR 感知模糊测试

**所属 Session**：[Session 18: Programming Languages and Compilers](index.md) · [ATC 2026](../index.md)

**作者**：Jinze Si (Shanghai Jiao Tong University), Yuchen Sun (Shanghai Jiao Tong University), Mingyu Wu (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

## 英文摘要
JIT compilers are core components of modern language virtual machines, and their bugs can crash the VM or silently miscompile programs. Modern JIT compilers perform multiple rounds of optimizations on graph-based intermediate representation (IR), where each round modifies, transforms, or eliminates IR nodes (referred to as node evolution). Bugs arise when the combination of multiple evolution paths violates inherent constraints of the IR. However, existing fuzzing tools lack fine-grained awareness of IR-level node evolution and struggle to construct the compound IR structures required to trigger such evolution, limiting their ability to explore the evolution combination space effectively. We propose EvoFuzz, an IR-aware fuzzing framework for Java virtual machine (JVM) JIT compilers, comprising three components: Node Mutators, which induce IR nodes of different semantic categories through source-level mutations and are portable across compilers; Evolution Profiling, which tracks evolution at the optimization-path granularity and defines a set distance metric as the feedback signal for fuzzing; and Combination-Aware Scheduling, which learns sequential dependencies among mutators via Markov dependencies to optimize mutator selection. We implement EvoFuzz as a practical fuzzing system for production JVMs and evaluate it on multiple versions of OpenJDK HotSpot, OpenJ9, and GraalVM. EvoFuzz discovered 45 bugs, of which 37 have been confirmed and 10 have been fixed by developers. Compared with state-of-the-art JVM fuzzers, EvoFuzz improves code coverage in the HotSpot C2 compiler module by approximately 7%, triggers 1.7–1.9× as many unique optimization paths on average, and achieves 3.0–3.5× the baselines’ median set distance at 12 hours. These results show that node-evolution-aware feedback is an effective signal for exposing correctness bugs in production JIT compilers.

## 中文摘要
JIT 编译器是现代语言虚拟机的核心组件，其缺陷可能导致虚拟机崩溃或悄然错误编译程序。现代 JIT 编译器在基于图的中间表示（IR）上执行多轮优化，每一轮都会修改、变换或消除 IR 节点，这一过程称为节点演化。当多条演化路径的组合违反 IR 的固有约束时，缺陷便会产生。然而，现有模糊测试工具缺乏对 IR 层节点演化的细粒度感知，难以构造触发此类演化所需的复合 IR 结构，从而限制了它们有效探索演化组合空间的能力。我们提出 EvoFuzz，一个面向 Java 虚拟机（JVM）JIT 编译器的 IR 感知模糊测试框架，包含三个组件：节点变异器，通过源码级变异诱导不同语义类别的 IR 节点，并可跨编译器移植；演化画像，在优化路径的粒度上追踪演化，并定义一种集合距离度量作为模糊测试的反馈信号；组合感知调度，通过马尔可夫依赖学习变异器之间的顺序依赖关系，以优化变异器选择。我们将 EvoFuzz 实现为面向生产 JVM 的实用模糊测试系统，并在 OpenJDK HotSpot、OpenJ9 和 GraalVM 的多个版本上进行评估。EvoFuzz 发现了 45 个缺陷，其中 37 个已被确认，10 个已被开发者修复。与最先进的 JVM 模糊测试器相比，EvoFuzz 在 HotSpot C2 编译器模块中将代码覆盖率提升约 7%，平均触发 1.7–1.9× 的唯一优化路径，并在 12 小时时达到基线中位集合距离的 3.0–3.5×。这些结果表明，节点演化感知的反馈是暴露生产 JIT 编译器正确性缺陷的有效信号。

## 英文关键词
JIT Compiler, Fuzzing, Intermediate Representation

## 中文关键词
JIT 编译器，模糊测试，中间表示

[返回 Session 18](index.md) · [返回 ATC 2026](../index.md)
