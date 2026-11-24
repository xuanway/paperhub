# Operating System Policies in the Wild

**中文标题**：真实环境中的操作系统策略

**所属 Session**：[Session 23: Storage and OS Policies](index.md) · [ATC 2026](../index.md)

**作者**：Yushan Qin (UW-Madison), Ananya Virmani (University of Wisconsin--Madison), Sungkar Bolat (student), Ayushi Chaudhary (University of Wisconsin-Madison), Nida Tanveer Ul Hasan (University of Wisconsin--Madison), Mai Zheng (Iowa State University), Sebastian Angel (University of Pennsylvania), Christopher J. Rossbach (UT Austin and Microsoft), Michael Swift (University of Wisconsin--Madison)

## 英文摘要
Operating system policies determine what should happen and when. They have a large impact on performance, and are the subject of much research. However, they are largely discussed in isolation: the single question of what thread to run next on a CPU, or what memory page to replace next. Decades of development in Linux, though, teaches us that OS policies can be both more complicated and simpler; there are also many more than commonly discussed. This paper presents a study of Linux kernel policies across multiple subsystems with the goal of better understanding what they do, how they are implemented, and how readily they can be changed. Using manual code inspection, we identify over 330 policies across the Linux memory management, scheduling, I/O, file, and power subsystems. We identify common implementation styles, such as single and multi-function decisions, inline-code and configurable parameters; common features used for decisions such as local and global state, historical context, and hardware information; common decision types such as selecting objects, identifying attributes, and changing system modes. Taken as a whole, this study presents a comprehensive picture of the diversity and common structures of Linux policies, and serves as a basis for future work in developing new ML-driven policies.

## 中文摘要
操作系统策略决定应该发生什么以及何时发生。它们对性能有巨大影响，也是大量研究的主题。然而，这些策略在很大程度上被孤立地讨论：只是单纯讨论 CPU 上接下来运行哪个线程，或接下来替换哪个内存页。不过，Linux 数十年的发展告诉我们，操作系统策略既可能更复杂，也可能更简单；而且实际存在的策略远多于通常讨论的那些。本文对 Linux 内核跨多个子系统的策略开展研究，目标是更好地理解它们做什么、如何实现，以及改变它们有多容易。通过人工代码审查，我们在 Linux 的内存管理、调度、I/O、文件与电源子系统中识别出 330 多个策略。我们归纳出常见的实现风格，如单函数与多函数决策、内联代码与可配置参数；归纳出决策中常用的信息，如本地与全局状态、历史上下文与硬件信息；并归纳出常见的决策类型，如选择对象、识别属性与切换系统模式。总体而言，本研究全面呈现了 Linux 策略的多样性与共性结构，并为未来开发新的 ML 驱动策略奠定了基础。

## 英文关键词
policy, operating system, scheduling, memory management, file system

## 中文关键词
策略，操作系统，调度，内存管理，文件系统

[返回 Session 23](index.md) · [返回 ATC 2026](../index.md)
