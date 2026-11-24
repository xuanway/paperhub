# Lightweight Memory Tracing via General Binary Analysis and Offline Reconstruction

**中文标题**：基于通用二进制分析与离线重建的轻量级内存追踪

**所属 Session**：[Session 27: Performance Diagnosis and Operational Repair](index.md) · [ATC 2026](../index.md)

**作者**：Ziheng Liu (University of California, San Diego), Steven Swanson (University of California, San Diego)

## 英文摘要
Memory tracing is an important technique used in hardware design, debugging, system analysis, and memory management. However, tracing many complex applications is impractical due to the high runtime overhead of existing tracing techniques, typically over 30×. This slowdown is especially problematic when tracing one component of a complex system disrupts the execution of the whole system (e.g., a microservice deployed in a datacenter). PTracer is a general binary-level memory tracing tool that reduces tracing overhead by at least an order of magnitude compared to state-of-the-art techniques. Its novel approach breaks tracing into three stages: general static analysis to identify the minimal amount of information required to reconstruct the complete trace, runtime instrumentation to log the information, and offline reconstruction of the memory trace. PTracer can dynamically attach to and detach from running programs, making it more feasible to deploy PTracer in production systems. It has two modes: one optimized for high fidelity and another sacrificing a minor amount of accuracy for better performance. Furthermore, it effectively handles JIT-compiled programs such as JavaScript and Java. Evaluated across diverse benchmarks written in C, Python, Rust, JavaScript and Java, the two modes of PTracer achieve 6× and 3× runtime overhead on average, respectively, while state-of-the-art techniques incur 31× to 152× overhead on average.

## 中文摘要
内存追踪是硬件设计、调试、系统分析和内存管理中使用的一项重要技术。然而，由于现有追踪技术的高运行时开销（通常超过 30×），追踪许多复杂应用并不现实。当追踪复杂系统的一个组件会扰乱整个系统的执行时（例如部署在数据中心的微服务），这种减速尤为严重。PTracer 是一个通用的二进制级内存追踪工具，相比最先进技术将追踪开销降低至少一个数量级。其新颖方法将追踪分解为三个阶段：通用静态分析以确定重建完整追踪所需的最少信息，运行时插桩以记录这些信息，以及离线重建内存追踪。PTracer 可以动态附加到运行中的程序并从其上分离，从而使 PTracer 更易于部署到生产系统。它有两种模式：一种针对高保真度优化，另一种以少量精度损失换取更好的性能。此外，它能有效处理 JavaScript 和 Java 等 JIT 编译的程序。在由 C、Python、Rust、JavaScript 和 Java 编写的多样基准上评测，PTracer 的两种模式平均分别实现 6× 和 3× 的运行时开销，而最先进技术平均产生 31× 至 152× 的开销。

## 英文关键词
memory tracing, binary analysis, Intel PT, dynamic binary instrumentation, cache simulation

## 中文关键词
内存追踪，二进制分析，Intel PT，动态二进制插桩，缓存模拟

[返回 Session 27](index.md) · [返回 ATC 2026](../index.md)
