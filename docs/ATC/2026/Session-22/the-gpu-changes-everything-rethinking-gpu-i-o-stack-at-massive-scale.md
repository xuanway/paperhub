# The GPU Changes Everything: Rethinking GPU I/O Stack at Massive Scale

**中文标题**：GPU 改变一切：重新思考超大规模下的 GPU I/O 栈

**所属 Session**：[Session 22: Large-scale AI](index.md) · [ATC 2026](../index.md)

**作者**：Guanyi Chen (The Hong Kong University of Science and Technology (Guangzhou)), Jian Zhang (The Hong Kong University of Science and Technology (Guangzhou))

## 英文摘要
AI and data-intensive applications increasingly rely on ondemand data movement between NVMe SSDs and GPU memory, making an efficient GPU I/O stack critical for performance. Existing GPU-initiated I/O systems enable direct storage access from GPU kernels but largely rely on a thin I/O stack, overlooking key storage management mechanisms such as I/O scheduling, caching, and admission control. Moreover, these mechanisms cannot be directly inherited from CPU-side I/O stacks because massive GPU parallelism and limited HBM capacity fundamentally reshape the I/O stack design space. We present ShaperIO, a GPU-initiated I/O stack that rethinks I/O scheduling, caching, and admission control for massive GPU I/O parallelism. ShaperIO restores write sequentiality to avoid storage fragmentation, eliminates cache eviction stalls, and prevents storage device overload. Our evaluation shows that ShaperIO achieves up to 7.51× higher post-write read bandwidth on microbenchmarks and up to 2.54× end-to-end speedup across BFS, large-scale GNN training, and LLM inference with KV-cache offloading.

## 中文摘要
AI 与数据密集型应用日益依赖 NVMe SSD 与 GPU 内存之间的按需数据移动，这使得高效的 GPU I/O 栈对性能至关重要。现有的 GPU 发起 I/O 系统支持从 GPU kernel 直接访问存储，但大多依赖薄 I/O 栈，忽视了 I/O 调度、缓存与准入控制等关键存储管理机制。此外，这些机制无法直接从 CPU 侧 I/O 栈继承，因为 GPU 的大规模并行性与有限的 HBM 容量从根本上重塑了 I/O 栈的设计空间。我们提出 ShaperIO，一个 GPU 发起的 I/O 栈，针对大规模 GPU I/O 并行重新思考 I/O 调度、缓存与准入控制。ShaperIO 恢复写入的顺序性以避免存储碎片，消除缓存淘汰停顿，并防止存储设备过载。我们的评估表明，ShaperIO 在微基准上实现最高 7.51× 的写后读带宽提升，并在 BFS、大规模 GNN 训练以及带 KV 缓存卸载的 LLM 推理中实现最高 2.54× 的端到端加速。

## 英文关键词
GPU I/O, I/O scheduling, NVMe, Page cache, Admission control

## 中文关键词
GPU I/O，I/O 调度，NVMe，页缓存，准入控制

[返回 Session 22](index.md) · [返回 ATC 2026](../index.md)
