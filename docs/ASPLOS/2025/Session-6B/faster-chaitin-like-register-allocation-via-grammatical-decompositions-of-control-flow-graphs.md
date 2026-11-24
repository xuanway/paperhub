---
title: "Faster Chaitin-like Register Allocation via Grammatical Decompositions of Control-Flow Graphs"
description: "ASPLOS 2025 · Session 6B · 基于控制流图语法分解的更快类 Chaitin 寄存器分配"
tags:
  - "ASPLOS2025"
  - "Session 6B"
  - "Compilers & Languages"
---

# Faster Chaitin-like Register Allocation via Grammatical Decompositions of Control-Flow Graphs

**中文标题：** 基于控制流图语法分解的更快类 Chaitin 寄存器分配

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xuran Cai (Hong Kong University of Science and Technology), Amir Kafshdar Goharshady (University of Oxford), S. Hitarth (Hong Kong University of Science and Technology), Chun Kit Lam (Hong Kong University of Science and Technology)

**单位：** Hong Kong University of Science and Technology；University of Oxford

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707286) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

It is well-known that control-flow graphs (CFGs) of structured programs are sparse. This sparsity has been previously formalized in terms of graph parameters such as treewidth and pathwidth and used to design faster parameterized algorithms for numerous compiler optimization, model checking and program analysis tasks. In this work, we observe that the known graph sparsity parameters fail to exactly capture the kind of sparsity exhibited by CFGs. For example, while all structured CFGs have a treewidth of at most 7, not every graph with a treewidth of 7 or less is realizable as a CFG. As a result, current parameterized algorithms are solving the underlying graph problems over a more general family of graphs than the CFGs. To address this problem, we design a new but natural concept of graph decomposition based on a grammar that precisely captures the set of graphs that can be realized as CFGs of programs. We show that our notion of decomposition enables the same type of dynamic programming algorithms that are often used in treewidth/pathwidth-based methods. As two concrete applications, using our grammatical decomposition of CFGs, we provide asymptotically more efficient algorithms for two variants of the classical problem of register allocation as defined by Chaitin, i.e. assigning program variables to a limited number of registers such that variables with intersecting lifetimes are not assigned to the same register. Note that Chaitin's formulation of register allocation does not allow live-range splitting. Our algorithms are asymptotically faster not only in comparison with the non-parameterized solutions for these problems, but also Attribution International 4.0 License.. compared to the state-of-the-art treewidth/pathwidth-based approaches in the literature. For minimum-cost register allocation over a fixed number of registers, we provide an algorithm with a runtime of 𝑂(|𝐺| · |V|5·𝑟) where |𝐺| is the size of the program, V is the set of program variables and 𝑟is the number of registers. In contrast, the previous treewidthbased algorithm had a runtime of 𝑂(|𝐺| · |V|16·𝑟). For the decision problem of spill-free register allocation, our algorithm's runtime is 𝑂(|𝐺| ·𝑟5·𝑟+5) whereas the previous works had a runtime of 𝑂(|𝐺| · 𝑟16·𝑟). Finally, we provide extensive experimental results on spillfree register allocation, showcasing the scalability of our approach in comparison to previous state-of-the-art methods. Most notably, our approach can handle real-world instances with up to 20 registers, whereas previous works could only scale to 8. This is a significant improvement since most ubiquitous architectures, such as the x86 family, have 16 registers. For such architectures, our approach is the first-ever exact algorithm that scales up to solve the real-world instances of spill-free register allocation.

## 中文摘要

众所周知，结构化程序的控制流图（CFG）是稀疏的。此前，这种稀疏性已通过树宽（treewidth）与路径宽（pathwidth）等图参数被形式化，并被用于为众多编译器优化、模型检测和程序分析任务设计更快的参数化算法。在本工作中，我们观察到已有的图稀疏性参数无法精确刻画 CFG 所表现出的那种稀疏性。例如，尽管所有结构化 CFG 的树宽至多为 7，但并非每个树宽不超过 7 的图都能实现为某个 CFG。因此，当前的参数化算法是在比 CFG 更一般的图族上求解其底层的图问题。为解决该问题，我们基于一种文法设计了一个全新而自然的图分解概念，该文法精确刻画了可作为程序 CFG 实现的图集合。我们证明，我们所提出的分解概念能够支撑树宽/路径宽方法中常用的那类动态规划算法。作为两个具体应用，利用我们对 CFG 的语法分解，我们为 Chaitin 所定义的经典寄存器分配问题的两个变体给出了渐近更高效的算法，即：将程序变量分配给数量有限的寄存器，使得生命周期相交的变量不会被分配到同一寄存器。需要注意的是，Chaitin 对寄存器分配的表述不允许活跃区间分裂。我们的算法不仅在渐近复杂度上优于这些问题的非参数化解法，也优于文献中基于树宽/路径宽的最先进方法（原文此处夹有 “Attribution International 4.0 License..” 字样）。对于固定寄存器数量下的最小代价寄存器分配，我们给出的算法运行时间为 𝑂(|𝐺| · |V|5·𝑟)，其中 |𝐺| 为程序规模，V 为程序变量集合，𝑟 为寄存器数量。相比之下，此前基于树宽的算法运行时间为 𝑂(|𝐺| · |V|16·𝑟)。对于无溢出寄存器分配的判定问题，我们的算法运行时间为 𝑂(|𝐺| ·𝑟5·𝑟+5)，而此前工作的运行时间为 𝑂(|𝐺| · 𝑟16·𝑟)。最后，我们给出了关于无溢出寄存器分配的大量实验结果，展示了我们的方法相较于此前最先进方法的可扩展性。最值得注意的是，我们的方法能够处理寄存器数量多达 20 的真实实例，而此前的工作只能扩展到 8 个寄存器。这是一个显著的提升，因为大多数无处不在的架构（例如 x86 系列）都只有 16 个寄存器。对于此类架构，我们的方法是首个能够扩展至求解真实无溢出寄存器分配实例的精确算法。

## 英文关键词

Sparsity, Control-flow Graphs, Graph Decompositions, Register Allocation

## 中文关键词

稀疏性；控制流图；图分解；寄存器分配

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707286)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2025](../index.md)
