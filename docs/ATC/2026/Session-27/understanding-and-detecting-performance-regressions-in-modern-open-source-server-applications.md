# Understanding and Detecting Performance Regressions in Modern Open-Source Server Applications

**中文标题**：理解并检测现代开源服务器应用中的性能回退

**所属 Session**：[Session 27: Performance Diagnosis and Operational Repair](index.md) · [ATC 2026](../index.md)

**作者**：Jinze Si (Shanghai Jiao Tong University), Xiaoqian Ma (Shanghai JiaoTong University), Mingyu Wu (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

## 英文摘要
Modern open-source server applications evolve rapidly through frequent code updates, which can introduce performance regressions that gradually degrade application efficiency. Traditional benchmark testing is often too expensive to run after every commit and can miss regressions that manifest only under specific workloads. In this work, we conduct a comprehensive study of 98 real-world performance regressions across 11 widely used open-source systems. We find that many regressions stem from small, seemingly innocuous commits and are triggered only through rarely exercised execution paths. Guided by these insights, we develop Scalpel, a practical performance regression detection tool for large open-source server applications. The core idea is to turn each code change into a targeted regression check: Scalpel reduces benchmark cost by selecting only test cases that reach changed code, and exposes workload-specific regressions by exploring commit-relevant paths, ranking candidate paths with instruction counts, and confirming slowdowns through native re-execution. Our evaluation shows that Scalpel detects 24 of 30 known regressions in our benchmark set. It also exposes 25 new regressions, 12 of which have been confirmed by communities. Across recent commits, Scalpel spends 62 minutes per code-modifying commit on average, achieving 3.5–13× speedup over official benchmark testing.

## 中文摘要
现代开源服务器应用通过频繁的代码更新快速演进，这可能引入性能回退，逐渐降低应用效率。传统基准测试通常代价过高，难以在每次提交后运行，并且可能漏掉仅在特定工作负载下才显现的回退。在本工作中，我们对 11 个广泛使用的开源系统中的 98 个真实性能回退开展了全面研究。我们发现，许多回退源于微小、看似无害的提交，并且仅通过很少被执行的执行路径触发。在这些洞见的指导下，我们开发了 Scalpel，一个面向大型开源服务器应用的实用性能回退检测工具。其核心思想是将每次代码变更转化为一次有针对性的回退检查：Scalpel 仅选择能够到达变更代码的测试用例以降低基准测试成本，并通过探索与提交相关的路径、以指令计数对候选路径排序、以及通过原生重执行确认减速，来暴露特定工作负载下的回退。我们的评测表明，Scalpel 在我们的基准集合中检测出 30 个已知回退中的 24 个。它还暴露了 25 个新回退，其中 12 个已被社区确认。在近期的提交上，Scalpel 平均每个修改代码的提交花费 62 分钟，相比官方基准测试实现 3.5–13× 加速。

## 英文关键词
Performance Regression, Server Applications, Benchmark Testing

## 中文关键词
性能回归，服务器应用，基准测试

[返回 Session 27](index.md) · [返回 ATC 2026](../index.md)
