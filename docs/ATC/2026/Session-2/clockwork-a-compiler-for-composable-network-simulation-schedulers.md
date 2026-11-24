# Clockwork: A Compiler for Composable Network Simulation Schedulers

**中文标题**：Clockwork：面向可组合网络仿真调度器的编译器

**所属 Session**：[Session 2: Network Measurement and Simulation](index.md) · [ATC 2026](../index.md)

**作者**：Hao Li (Xi'an Jiaotong University), Yihan Dang (Xi'an Jiaotong University), Danfeng Shan (Xi'an Jiaotong University), Peng Zhang (Xi'an Jiaotong University)

## 英文摘要
The scheduling layer of discrete-event network simulation dominates wall-clock time at scale. A decade of work has produced specialized strategies, but each is locked inside a monolithic system that fuses the strategy with a dedicated runtime and programming model. Implementing a new strategy or combining existing ones requires thousands of lines of bespoke code, risks silent correctness bugs and degraded performance. We present Clockwork, a compiler that turns a declarative scheduling specification into a correct, specialized executor with the following three components: a DSL expresses strategies in tens of lines; a pipeline of IR passes detects and repairs composition conflicts through local rewrites; and a static backend emits a fused executor with no per-event dispatch. Experiments show that Clockwork’s generated executor runs faster than a hand-tuned reference, and on heterogeneous workloads composition finds up to 3.89× gains where a single strategy cannot reach.

## 中文摘要
在大规模场景下，离散事件网络仿真的调度层主导了实际运行时间。十年的研究已产出多种专用策略，但每一种都被锁死在单体式系统之内，该系统把策略与专用的运行时和编程模型融合在一起。实现一种新策略或组合已有策略需要编写数千行定制代码，并带来隐蔽的正确性缺陷与性能下降的风险。我们提出 Clockwork，一个把声明式调度规约转换为正确且专用执行器的编译器，它包含以下三个组成部分：一个 DSL 仅用数十行即可表达策略；一条 IR pass 流水线通过局部改写来检测并修复组合冲突；一个静态后端生成无需逐事件分派的融合执行器。实验表明，Clockwork 生成的执行器比手工调优的参考实现运行更快，并且在异构负载上，组合方式能够获得单一策略无法达到的高达 3.89× 的收益。

## 英文关键词
network simulation, discrete-event simulation, scheduling, compilers, domain-specific languages

## 中文关键词
网络仿真，离散事件仿真，调度，编译器，领域特定语言

[返回 Session 2](index.md) · [返回 ATC 2026](../index.md)
