# Detecting API Misuses Across Context Boundaries in Linux Kernel Drivers

**中文标题**：检测 Linux 内核驱动中跨上下文边界的 API 误用

**所属 Session**：[Session 24: Kernel Interfaces and Service Reliability](index.md) · [ATC 2026](../index.md)

**作者**：Thomas Fourier (Inria), Julia Lawall (Inria), Baptiste Lepers (Inria)

## 英文摘要
API misuse is a major source of bugs in the Linux kernel. Prior work on detecting such misuses largely focuses on local patterns, such as missing error checks or ordering constraints along a control-flow path. In practice, however, many bugs arise from non-local API interactions that span multiple functions, files, or asynchronous contexts (e.g., a resource acquired in one function and released in another without any control-flow connection). These interactions fall outside the scope of existing analysis. In this paper, we present a novel approach to infer and check API constraints in such non-local settings. We focus on the consistency between API calls. We found bugs in non-local interactions that stem from incorrect arguments being passed to APIs (e.g., passing the wrong buffer size). To detect them, we automatically infer argument consistency constraints across API calls and introduce a scalable methodology to verify these constraints across large codebases. We implement our approach and evaluate it on the Linux kernel. Our analysis uncovers 39 previously unknown bugs, including memory leaks and potential security vulnerabilities.

## 中文摘要
API 误用是 Linux 内核缺陷的一个主要来源。以往针对此类误用的检测工作大多聚焦于局部模式，例如缺失错误检查，或沿某条控制流路径的次序约束。然而在实践中，许多缺陷源于跨越多个函数、文件或异步上下文的非局部 API 交互（例如在一个函数中获取资源、在另一个函数中释放，二者之间没有任何控制流连接）。这些交互超出了现有分析的范围。在本文中，我们提出一种新方法，在此类非局部场景下推断并检查 API 约束。我们关注 API 调用之间的一致性。我们发现了源于向 API 传递错误参数（例如传递错误的缓冲区大小）的非局部交互缺陷。为检测这些缺陷，我们自动推断跨 API 调用的参数一致性约束，并引入一套可扩展的方法以在大型代码库中验证这些约束。我们实现了该方法并在 Linux 内核上进行了评估。我们的分析发现了 39 个此前未知的缺陷，包括内存泄漏和潜在的安全漏洞。

## 英文关键词
static analysis, kernel

## 中文关键词
静态分析，内核

[返回 Session 24](index.md) · [返回 ATC 2026](../index.md)
