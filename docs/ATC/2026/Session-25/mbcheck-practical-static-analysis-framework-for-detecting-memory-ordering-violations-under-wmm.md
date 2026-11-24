# MBCheck: Practical Static Analysis Framework for Detecting Memory Ordering Violations under WMM

**中文标题**：MBCheck：在弱内存模型下检测内存定序违规的实用静态分析框架

**所属 Session**：[Session 25: Formal Methods and Verification](index.md) · [ATC 2026](../index.md)

**作者**：Jaidev Shastri (Virginia Tech), Binoy Ravindran (Virginia Tech)

## 英文摘要
Memory-ordering violations in lock-free kernel code, where threads share data without locks, are a high-impact source of faults that are hard to detect and debug. On architectures with a weak memory model (WMM), such as AArch64 and RISC-V, a missing release, a misplaced fence, or an ordinary load in place of an acquire can allow other CPUs to observe partially constructed memory objects. The Linux Kernel Memory Model (LKMM), evaluated with the herd7 tool, is the definitive reference for deciding whether such an outcome is allowed. However, herd7 only decides this for a small multi-threaded program, a litmus test, that a developer writes by hand. As a result, the model covers only a fraction of the millions of cross-function interactions in the kernel. MBCheck addresses this gap. It is an extensible static analysis framework that transforms a complete kernel build into a collection of automatically synthesized litmus tests and evaluates them with herd7. MBCheck reduces each function to the shared accesses around its memory-ordering instructions, discards function pairs that cannot run concurrently, and synthesizes a litmus test for every remaining pair, together with the outcome that a missing ordering would allow. A runtime verifier checks that each litmus test is faithful to the kernel code. For a complete kernel build, MBCheck synthesizes and evaluates about 30,000 litmus tests in under an hour. On Linux v7.3-rc4, we report 47 memory-ordering violations and have submitted 41 patches to the kernel maintainers. Five of the violations have been confirmed so far, and two fixes have been accepted.

## 中文摘要
无锁内核代码中线程在不加锁的情况下共享数据，其中的内存定序违规是一类影响巨大且难以检测和调试的故障来源。在采用弱内存模型（WMM）的架构（如 AArch64 和 RISC-V）上，一个缺失的 release、一个位置不当的 fence，或以普通加载代替 acquire，都可能让其他 CPU 观察到部分构造的内存对象。Linux 内核内存模型（LKMM）配合 herd7 工具进行评估，是判定此类结果是否被允许的权威参考。然而，herd7 只能针对开发者手工编写的小型多线程程序（litmus 测试）做出判定。因此，该模型仅覆盖了内核中数百万次跨函数交互的一小部分。MBCheck 填补了这一空白。它是一个可扩展的静态分析框架，能把一次完整的内核构建转换为一系列自动合成的 litmus 测试，并用 herd7 对它们进行评估。MBCheck 把每个函数约简为其内存定序指令周围的共享访问，丢弃不可能并发执行的函数对，并为每一剩余的函数对合成一个 litmus 测试，同时给出缺失定序所允许的结果。一个运行时验证器检查每个 litmus 测试是否忠实于内核代码。对于一次完整的内核构建，MBCheck 在不到一小时内合成并评估约 30,000 个 litmus 测试。在 Linux v7.3-rc4 上，我们报告了 47 处内存定序违规，并已向内核维护者提交 41 个补丁。目前已有 5 处违规得到确认，两个修复被接受。

## 英文关键词
weak memory models, Linux kernel, AArch64, LKMM, static analysis, LLVM, herd7, litmus testing

## 中文关键词
弱内存模型，Linux 内核，AArch64，LKMM，静态分析，LLVM，herd7，litmus 测试

[返回 Session 25](index.md) · [返回 ATC 2026](../index.md)
