# Instrumentation Optimization for Practical Dynamic Race Detection

**中文标题**：面向实用动态数据竞争检测的插桩优化

**所属 Session**：[Session 3: Software Reliability and Bugs](index.md) · [ATC 2026](../index.md)

**作者**：Alexey Paznikov (National University of Singapore), Michael Schwarz (National University of Singapore), Andrey Kogutenko (Saint Petersburg Electrotechnical University "LETI"), Yaroslav Osipov (Saint Petersburg Electrotechnical University "LETI"), Umang Mathur (National University of Singapore)

## 英文摘要
Dynamic data race detectors are successful at flagging concurrency bugs, but their high runtime overhead limits adoption. This overhead stems primarily from pervasive instrumentation of memory accesses – a significant fraction of which is for safe accesses. We address this inefficiency through a compiler-integrated approach that identifies safe accesses using static analysis and eliminates instrumentation for these. We strike a careful balance between analysis precision and cost, to ensure applicability to real-world applications. We show that our optimizations never cause ThreadSanitizer to miss races it would otherwise detect. We further observe that many checks are redundant: They only flag a race if a preceding check has already flagged an equivalent race for the same memory location. We show that, when reporting one representative per class is sufficient, even more instrumentation can be eliminated. Lastly, we introduce a dynamic technique that skips instrumentation when there is only one thread at runtime, even when this could not be determined statically. We integrate these static analyses and program transformations into the ThreadSanitizer race detector based on LLVM. Our experiments on a diverse suite of real-world applications, including Memcached, Redis, SQLite, MySQL, and Chromium, demonstrate that our optimizations reduce the number of instrumentation calls at runtime by up to 91% and yield application-level speedups of up to 1.91×, a geometric-mean Chromium speedup of 1.25× on Blink and 1.14× on Speedometer 3.0, and peak speedups reaching 2.28× on Memcached with two server threads. Our optimizations are in the process of being upstreamed into ThreadSanitizer.

## 中文摘要
动态数据竞争检测器能够成功标记并发缺陷，但其高昂的运行时开销限制了其采用。这一开销主要源于对内存访问的普遍插桩，其中相当大一部分是对安全访问的插桩。我们通过一种与编译器集成的方法解决这一低效问题：利用静态分析识别安全访问，并消除对它们的插桩。我们在分析精度与开销之间谨慎权衡，以确保对真实应用具有适用性。我们表明，我们的优化绝不会导致 ThreadSanitizer 漏报它原本能够检测到的竞争。我们进一步观察到，许多检查是冗余的：只有当先前的检查已针对同一内存位置标记了等价竞争时，它们才会标记竞争。我们表明，当只需为每一类竞争报告一个代表时，还可以消除更多插桩。最后，我们引入一种动态技术：当运行时只有一个线程时跳过插桩，即使这一点无法在静态阶段确定。我们将这些静态分析与程序变换集成到基于 LLVM 的 ThreadSanitizer 竞争检测器中。在包含 Memcached、Redis、SQLite、MySQL 和 Chromium 等多样化真实应用套件上的实验表明，我们的优化将运行时的插桩调用次数最多减少 91%，并带来最高 1.91× 的应用级加速，在 Chromium 上 Blink 的几何平均加速为 1.25×、Speedometer 3.0 上为 1.14×，在具有两个服务器线程的 Memcached 上峰值加速达到 2.28×。我们的优化正在被上游合并进 ThreadSanitizer。

## 英文关键词
data race detection, ThreadSanitizer, static analysis, compiler instrumentation, LLVM

## 中文关键词
数据竞争检测，ThreadSanitizer，静态分析，编译器插桩，LLVM

[返回 Session 3](index.md) · [返回 ATC 2026](../index.md)
