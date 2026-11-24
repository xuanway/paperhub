# HeapLENS: Heap Layout Evaluation & Navigation Suite

**中文标题**：HeapLENS：堆布局评估与导航套件

**所属 Session**：[Session 27: Performance Diagnosis and Operational Repair](index.md) · [ATC 2026](../index.md)

**作者**：Trevor Brown (University of Waterloo), Sean Ovens (University of Waterloo), Gautam Pathak (University of Waterloo)

## 英文摘要
We present HeapLENS, a visualization and profiling tool for spotting memory-layout anti-patterns in multithreaded C/C++ applications. It is built to investigate questions such as: Which object types routinely lie next to tree nodes? Which fields cross cache lines? How do layouts change over time? HeapLENS automatically collects allocation histories with best-effort type information and support for custom user allocators. To make histories with billions of events inspectable, it uses sampling and a novel page fingerprinting technique to cluster and visualize a small set of diverse layouts. We use HeapLENS to identify layout problems, contributing an accepted RocksDB fix, and improving concurrent data structure performance by up to 30.6%. We also give HeapLENS’s text exports to an LLM, which independently investigates layout problems and tests optimizations, improving mean throughput by 4.2% in the Valkey KV-store and approximate nearest-neighbour throughput by up to 9.8% in the HNSWLib vector database.

## 中文摘要
我们提出 HeapLENS，一个用于发现多线程 C/C++ 应用中内存布局反模式的可视化与剖析工具。它的构建旨在探究如下问题：哪些对象类型经常紧邻树节点？哪些字段跨越缓存行？布局如何随时间变化？HeapLENS 自动收集分配历史，附带尽力而为的类型信息，并支持自定义的用户分配器。为使包含数十亿事件的分配历史可被检视，它使用采样和一种新颖的页面指纹技术来聚类并可视化一小组多样的布局。我们使用 HeapLENS 识别布局问题，贡献了一个被接受的 RocksDB 修复，并将并发数据结构性能提升最高 30.6%。我们还将 HeapLENS 的文本导出交给 LLM，由其独立调查布局问题并测试优化，在 Valkey KV 存储中将平均吞吐提升 4.2%，在 HNSWLib 向量数据库中将近似最近邻吞吐提升最高 9.8%。

## 英文关键词
memory layout, heap visualization, memory profiling, cache locality, performance debugging, concurrency

## 中文关键词
内存布局，堆可视化，内存剖析，缓存局部性，性能调试，并发

[返回 Session 27](index.md) · [返回 ATC 2026](../index.md)
