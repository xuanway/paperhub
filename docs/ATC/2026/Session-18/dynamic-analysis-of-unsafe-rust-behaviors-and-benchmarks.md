# Dynamic Analysis of Unsafe Rust: Behaviors and Benchmarks

**中文标题**：不安全 Rust 的动态分析：行为与基准测试集

**所属 Session**：[Session 18: Programming Languages and Compilers](index.md) · [ATC 2026](../index.md)

**作者**：Jiaye Fang (The George Washington University), Arsalan Bin Najeeb (The George Washington University), Dylan O'Neill (The George Washington University), Prince Noah Johnson (University of Notre Dame), Zhixiao Zhang (The George Washington University), Jie Zhou (The George Washington University)

## 英文摘要
Rust permits the use of unsafe code, which can violate both memory safety and concurrency safety. Prior work investigates unsafe code in Rust projects and provides insights into what, how, and why it is used. However, these studies provide only static metrics about unsafe code, while lacking an understanding of its dynamic behaviors at execution time. In parallel, many security mechanisms have been proposed to mitigate unsafe code in Rust. But the evaluations of these tools are suboptimal due to the lack of a benchmark suite that emphasizes unsafe code. In this paper, we present the first empirical study of the runtime behavior of unsafe code in real-world Rust projects. We develop a dynamic analysis framework that programmers can use to answer key questions about unsafe code at execution time. Moreover, using the dynamic analysis framework, we curate the first benchmark suite specifically designed for evaluating the performance and memory overhead of security defenses against unsafe code in Rust.

## 中文摘要
Rust 允许使用 unsafe 代码，而这类代码可能同时破坏内存安全与并发安全。已有工作考察了 Rust 项目中的 unsafe 代码，并就其被使用的内容、方式与原因提供了洞见。然而这些研究只给出了关于 unsafe 代码的静态度量，缺少对其执行期动态行为的理解。与此同时，已有许多安全机制被提出以缓解 Rust 中 unsafe 代码的风险。但由于缺少一个强调 unsafe 代码的基准测试集，这些工具的评估并不理想。本文首次对真实世界 Rust 项目中 unsafe 代码的运行时行为开展实证研究。我们开发了一个动态分析框架，程序员可用它在执行期回答关于 unsafe 代码的关键问题。此外，借助该动态分析框架，我们构建了首个专门用于评估针对 Rust unsafe 代码的安全防御机制的性能与内存开销的基准测试集。

## 英文关键词
Unsafe Rust, Memory Safety, Dynamic Analysis, Benchmark Suite

## 中文关键词
不安全 Rust，内存安全，动态分析，基准测试集

[返回 Session 18](index.md) · [返回 ATC 2026](../index.md)
