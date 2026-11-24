# RunaSan: A Rust-Native Sanitizer for Precise and Context-Sensitive Sanitization

**中文标题**：RunaSan：面向精确且上下文敏感的净化的 Rust 原生 Sanitizer

**所属 Session**：[Session 3: Software Reliability and Bugs](index.md) · [ATC 2026](../index.md)

**作者**：Jongyoon Kim (Sungkyunkwan University), Kyuwon Cho (Sungkyunkwan University), Hojoon Lee (Sungkyunkwan University)

## 英文摘要
Rust guarantees memory safety by design and is increasingly used in systems software, yet the use of unsafe Rust can still introduce memory bugs. For this reason, prior works have leveraged sanitizers to detect memory errors stemming from unsafe Rust code. The shared objective is to instrument Rust programs selectively such that only the unsafe portions of code and their propagation are validated. However, previous approaches that retrofit the existing static analysis and sanitizer implementations are limited. They propagate unsafety over LLVM IR, where precision loss occurs due to the erased Rust semantics, and employ a context-insensitive pointer analysis since a context-sensitive one incurs high computational complexity. Moreover, the unsafety propagation is performed solely using static analysis, and thus cannot eliminate redundant checks in safe runtime contexts. We present RunaSan, a Rust-native analysis and instrumentation framework for sanitization of Rust: a context-sensitive sanitizer that keeps its entire analysis on Rust MIR to take advantage of Rust language semantics and evade redundant checks at runtime in safe contexts. RunaSan’s MIR-native unsafety analysis uses Rust semantics for improved precision. A context-sensitive MIR pointer analysis is made feasible through summarization of the Rust standard library. Also, its tagged-pointer scheme allows a pointer’s safety to be recognized by sanitizer checks such that unnecessary checks can be evaded at runtime. RunaSan runs 3.25× faster than AddressSanitizer (ASan) while detecting the same memory safety bugs on a corpus of reproduced bugs.

## 中文摘要
Rust 在设计上保证了内存安全，并越来越多地用于系统软件，但使用 unsafe Rust 仍可能引入内存缺陷。为此，先前的工作利用 sanitizer 来检测源自 unsafe Rust 代码的内存错误。它们的共同目标是选择性地对 Rust 程序插桩，使得只有代码中的 unsafe 部分及其传播得到校验。然而，此前对现有静态分析与 sanitizer 实现进行改造的方法存在局限。它们在 LLVM IR 上传播 unsafety，由于 Rust 语义已被擦除而出现精度损失，并且由于上下文敏感的指针分析会带来很高的计算复杂度，只能采用上下文不敏感的指针分析。此外，unsafety 的传播仅通过静态分析完成，因此无法消除安全运行时上下文中的冗余检查。我们提出 RunaSan，一个用于 Rust 净化的 Rust 原生分析与插桩框架：它是一个上下文敏感的 sanitizer，将全部分析保持在 Rust MIR 上，以利用 Rust 语言语义，并在运行时于安全上下文中规避冗余检查。RunaSan 的 MIR 原生 unsafety 分析利用 Rust 语义提升精度。通过对 Rust 标准库进行摘要，上下文敏感的 MIR 指针分析变得可行。同时，其带标签指针方案使指针的安全性能够被 sanitizer 检查识别，从而在运行时规避不必要的检查。在复现的缺陷语料上，RunaSan 在检测到相同内存安全缺陷的同时，运行速度比 AddressSanitizer（ASan）快 3.25×。

## 英文关键词
Rust, Sanitizer, Memory Safety

## 中文关键词
Rust，Sanitizer，内存安全

[返回 Session 3](index.md) · [返回 ATC 2026](../index.md)
