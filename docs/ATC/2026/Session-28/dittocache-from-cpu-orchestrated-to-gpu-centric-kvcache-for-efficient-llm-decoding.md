# DittoCache: From CPU-Orchestrated to GPU-Centric KVCache for Efficient LLM Decoding

**中文标题**：DittoCache：从 CPU 编排到以 GPU 为中心的 KVCache 实现高效 LLM 解码

**所属 Session**：[Session 28: LLM Inference IV](index.md) · [ATC 2026](../index.md)

**作者**：Jia He (University of Science and Technology of China; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center), Youhui Bai (University of Science and Technology of China), Jiawei Yi (University of Science and Technology of China), Ping Gong (University of Science and Technology of China), Zewen Jin (University of Science and Technology of China), Shannon Wang (Institute of Artificial Intelligence, Hefei Comprehensive National Science Center), Jiaqi Ruan (University of Science and Technology of China), Jiaan Zhu (University of Science and Technology of China), Pengcheng Wang (Huawei), Haibo Wang (Huawei), Weiguang Wang (Huawei), Xia Zhu (Huawei Technologies Co., Ltd), Cheng Li (University of Science and Technology of China; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center)

## 英文摘要
To cope with the growing memory capacity and bandwidth demands of autoregressive decoding, LLM frameworks offload the KVCache to host memory and retrieve only top-𝑘 KV data to GPU HBM at each step. However, existing designs remain largely CPU driven, creating coupled tradeoffs among cache management overhead, GPU cache hit ratio, miss transfer cost, retrieval granularity, accuracy, and fragmented GPU execution precluding whole-step CUDA Graphs. We present DittoCache, a GPU-centric KVCache subsystem for efficient LLM decoding. DittoCache stores offloaded KV states at token granularity to preserve top-𝑘sparse attention semantics, while managing the on-GPU cache at KV head granularity. It reuses cached top-𝑘KV states across adjacent decoding steps using query similarity, lightweight GPU-side metadata, and head-specific policies that improve cache hit ratio without accuracy loss. For cache misses, DittoCache devises a multi-threaded transfer engine with CPU accessible GPU buffers to efficiently move token-level KV data over PCIe, and hides miss latency with layer wise prefetching. By moving cache management and transfer control to GPU, DittoCache enables whole step CUDA Graph execution and removes CPU-induced launch bubbles. DittoCache is implemented atop SGLang and open-sourced. Evaluated on Llama3 8B and Qwen2.5 14B across Hopper GPU with 800 TFLOPS and A40 GPUs, DittoCache achieves up to 2.87× higher offline decoding throughput on Hopper GPU and 1.59× on A40 over three KVCache subsystems. It supports 1M and 512K token decoding on Hopper GPU and A40, respectively, where all baselines fail. For online serving with high concurrency, Hopper GPU improves decoding throughput by up to 3.94× over full attention.

## 中文摘要
为应对自回归解码日益增长的内存容量与带宽需求，LLM 框架将 KVCache 卸载到主机内存，并在每一步仅将 top-k KV 数据取回 GPU HBM。然而，现有设计在很大程度上仍由 CPU 驱动，从而在缓存管理开销、GPU 缓存命中率、缺失传输成本、检索粒度、精度以及阻碍整步 CUDA Graph 的碎片化 GPU 执行之间形成相互耦合的权衡。我们提出 DittoCache，一个以 GPU 为中心的 KVCache 子系统，用于高效 LLM 解码。DittoCache 以 token 粒度存储卸载的 KV 状态以保持 top-k 稀疏注意力语义，同时以 KV head 粒度管理 GPU 上的缓存。它利用查询相似性、轻量级 GPU 端元数据以及按 head 定制的策略，在相邻解码步之间复用已缓存的 top-k KV 状态，从而在不损失精度的情况下提高缓存命中率。对于缓存缺失，DittoCache 设计了带有 CPU 可访问 GPU 缓冲区的多线程传输引擎，以通过 PCIe 高效搬运 token 级 KV 数据，并利用逐层预取隐藏缺失延迟。通过将缓存管理与传输控制迁移到 GPU，DittoCache 支持整步 CUDA Graph 执行，并消除 CPU 引起的启动气泡。DittoCache 在 SGLang 之上实现并开源。在配备 800 TFLOPS 的 Hopper GPU 与 A40 GPU 上针对 Llama3 8B 和 Qwen2.5 14B 进行评估，相比三种 KVCache 子系统，DittoCache 在 Hopper GPU 上实现最高 2.87× 的离线解码吞吐提升，在 A40 上为 1.59×。它分别支持 Hopper GPU 上的 1M token 解码与 A40 上的 512K token 解码，而所有基线在这些场景下均失败。在高并发在线服务场景中，Hopper GPU 相比全注意力将解码吞吐提升最高 3.94×。

## 英文关键词
KVCache, LLM Decoding, GPU-Centric Caching

## 中文关键词
KVCache，LLM 解码，GPU 中心化缓存

[返回 Session 28](index.md) · [返回 ATC 2026](../index.md)
