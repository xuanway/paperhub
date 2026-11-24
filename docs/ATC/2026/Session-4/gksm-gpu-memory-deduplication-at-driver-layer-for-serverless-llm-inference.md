# gKSM: GPU Memory Deduplication at Driver Layer for Serverless LLM Inference

**中文标题**：gKSM：面向无服务器 LLM 推理的驱动层 GPU 内存去重

**所属 Session**：[Session 4: Serverless and Elastic LLM Inference](index.md) · [ATC 2026](../index.md)

**作者**：Shuheng Gao (University of Science and Technology of China), Fan Guo (MinJiang University), Yongkun Li (University of Science and Technology of China), Ziye Yue (University of Science and Technology of China), Yinlong Xu (University of Science and Technology of China, MinJiang University), John C.S. Lui (The Chinese University of Hong Kong)

## 英文摘要
In serverless LLM inference, cloud providers commonly locate multiple instances on a single GPU to improve utilization. However, each instance independently maintains its model weights and runtime state, making duplicate GPU memory the primary bottleneck. Memory deduplication is a widely-used technique for eliminating duplicate data in CPU systems, but extending it to GPU memory faces fundamental challenges. Effective GPU memory deduplication must avoid redundant data movement between CPU and GPU while preserving write isolation for shared pages without native copy-on-write (COW) support. This paper presents gKSM, a transparent GPU memory deduplication framework for serverless LLM inference. gKSM addresses these challenges through CPU-GPU collaborative hash management that offloads hash computation to GPU kernels, zero-copy model weight deduplication that eliminates duplication before model weight transfer, and a cross-privilege page fault handler that combines a lightweight kernel hook and CUDA Virtual Memory Management (VMM) remapping in the user space. gKSM also designs a stable page scanning algorithm and a reuse-aware placement policy in cluster scale. Experiments show that gKSM reduces GPU memory usage by 59.8% while maintaining high throughput compared to ServerlessLLM. Under memory constrained workloads, gKSM improves aggregate throughput by 2.15× and supports five instances concurrently. In cluster level simulation, gKSM achieves a service rate of 99.97%, compared to 78.2% for SLInfer and 26.9% for ServerlessLLM.

## 中文摘要
在无服务器 LLM 推理中，云提供商通常将多个实例放在单个 GPU 上以提高利用率。然而，每个实例都独立维护自身的模型权重与运行时状态，使重复的 GPU 内存成为主要瓶颈。内存去重是 CPU 系统中消除重复数据的常用技术，但将其扩展到 GPU 内存面临根本性挑战。有效的 GPU 内存去重必须在避免 CPU 与 GPU 之间冗余数据搬移的同时，在缺乏原生写时复制（COW）支持的情况下为共享页面保持写隔离。本文提出 gKSM，一个面向无服务器 LLM 推理的透明 GPU 内存去重框架。gKSM 通过以下方式应对这些挑战：CPU-GPU 协同的哈希管理，将哈希计算卸载到 GPU 内核；零拷贝的模型权重复制（去重），在模型权重传输之前就消除重复；以及跨特权级的缺页处理程序，将轻量级内核钩子与用户空间的 CUDA 虚拟内存管理（VMM）重映射相结合。gKSM 还在集群规模上设计了稳定的页面扫描算法与复用感知的放置策略。实验表明，与 ServerlessLLM 相比，gKSM 在保持高吞吐的同时将 GPU 内存使用量降低 59.8%。在内存受限的负载下，gKSM 将聚合吞吐提升 2.15×，并可同时支持五个实例。在集群级模拟中，gKSM 达到 99.97% 的服务率，而 SLInfer 为 78.2%，ServerlessLLM 为 26.9%。

## 英文关键词
GPU memory management, serverless, memory deduplication, LLM inference

## 中文关键词
GPU 内存管理，无服务器，内存去重，LLM 推理

[返回 Session 4](index.md) · [返回 ATC 2026](../index.md)
