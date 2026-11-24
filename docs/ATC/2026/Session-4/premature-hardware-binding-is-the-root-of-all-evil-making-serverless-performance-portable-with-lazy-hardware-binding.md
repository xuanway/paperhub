# Premature Hardware Binding is the Root of all Evil! Making Serverless Performance-Portable with Lazy Hardware Binding

**中文标题**：过早的硬件绑定是万恶之源：以惰性硬件绑定实现无服务器性能可移植

**所属 Session**：[Session 4: Serverless and Elastic LLM Inference](index.md) · [ATC 2026](../index.md)

**作者**：Serhii Ivanenko (INESC-ID, Instituto Superior Técnico, University of Lisbon), Carlos Segarra (Imperial College London), Rodrigo Bruno (INESC-ID, Instituto Superior Técnico, University of Lisbon)

## 英文摘要
Modern clouds are characterized by increasing hardware heterogeneity. While exposing hardware complexity to developers enables performance optimizations, it also constrains deployment options and fragments the platform’s resource pool. Conversely, serverless platforms abstract hardware details to increase deployment flexibility. However, this forces developers to compile their applications conservatively to ensure portability, sacrificing significant performance gains of CPU-specific instruction set extensions. To break through this tradeoff, we introduce Mosaic, a serverless platform that decouples portable application logic from performance-critical dependencies. Rather than eagerly bundling applications into a single binary, Mosaic delays binding until the deployment target is known, dynamically injecting pre-compiled, hardware-optimized library implementations tailored to the specific machine. The proposed design offers deployment flexibility, near-optimal performance, and low developer burden. Our evaluation demonstrates that Mosaic matches the throughput of aggressively optimized CPU-bound applications, achieving up to 40% higher throughput than builds without CPU-specific optimizations. Simultaneously, its cross-architecture portability prevents cluster fragmentation, reducing 90th percentile end-to-end scheduling latencies by up to 604× under constrained resources, while its architectural deduplication reduces application storage footprints by over two orders of magnitude.

## 中文摘要
现代云的特征是硬件异构性不断增强。虽然向开发者暴露硬件复杂性可以实现性能优化，但这也限制了部署选项并割裂了平台的资源池。相反，无服务器平台对硬件细节进行抽象以提升部署灵活性，但这迫使开发者以保守方式编译其应用以保证可移植性，从而牺牲了 CPU 特定指令集扩展所带来的显著性能收益。为突破这一权衡，我们提出 Mosaic，一个将可移植的应用逻辑与性能关键的依赖解耦的无服务器平台。Mosaic 不再急切地把应用打包成单个二进制文件，而是将绑定推迟到已知部署目标之时，动态注入针对特定机器定制的、预编译的硬件优化库实现。该设计提供了部署灵活性、接近最优的性能以及较低的开发者负担。我们的评估表明，Mosaic 的吞吐可与激进优化的 CPU 密集型应用相匹敌，相较未使用 CPU 特定优化的构建，吞吐最高提升 40%。同时，其跨架构可移植性避免了集群割裂，在资源受限的情况下使第 90 百分位端到端调度延迟最多降低 604×，而其架构级去重使应用的存储占用减少两个数量级以上。

## 英文关键词
Serverless, Cloud Computing, Hardware Heterogeneity, Performance Portability

## 中文关键词
无服务器，云计算，硬件异构性，性能可移植性

[返回 Session 4](index.md) · [返回 ATC 2026](../index.md)
