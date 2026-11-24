# Mosaic: Efficient CPU–GPU Coordinated Block-Sparse Attention for Long-Context Decoding

**中文标题**：Mosaic：面向长上下文解码的高效 CPU–GPU 协同块稀疏注意力

**所属 Session**：[Session 7: Long-context and Multimodal LLMs](index.md) · [ATC 2026](../index.md)

**作者**：Feiyu Yao (Beijing University of Technology), Zhixiong Niu (Microsoft Research), Xiaqing Li (Beijing Jiaotong University), Yongqiang Xiong (Microsoft Research), Juan Fang (Beijing University of Technology), Qian Wang (Beijing University of Technology)

## 英文摘要
Long-context LLM serving increasingly relies on CPU-resident context KV cache, driven by KV offloading and disaggregated prefill–decode execution. Although block-sparse attention reduces KV access, existing designs remain inefficient: GPU-centralized execution fetches selected KV blocks from CPU memory at each decoding step, making it PCIe-bound, while CPU–GPU partitioned execution places CPU-side sparse attention on the critical path, leaving substantial GPU time idle. This paper presents Mosaic, a CPU–GPU coordinated block-sparse attention system for efficient long-context decoding with CPU-resident context KV. Mosaic builds on three key insights: output-contribution-aware KV budgeting, head-specific and granularity-aware sparse configuration, and cross-device coordinated scheduling for sparse tasks over CPU-resident KV. Guided by these insights, Mosaic integrates a lightweight head-property predictor, a granularity– budget selector, and a priority-based scheduler to automatically configure and coordinate sparse attention, preserving output quality while improving efficiency on heterogeneous architectures. Across 2 models, 3 benchmarks, and 40 tasks, Mosaic preserves near-FULL quality while achieving a better overall quality–efficiency tradeoff than the evaluated baselines. Compared with the best-quality fixed Quest configuration, Mosaic improves TPOT by up to 3.7×. We further validate Mosaic across four hardware configurations and in a large-model multi-GPU deployment.

## 中文摘要
长上下文 LLM 服务日益依赖驻留于 CPU 的上下文 KV 缓存，这一趋势由 KV 卸载和预填充–解码分离执行所驱动。尽管块稀疏注意力减少了 KV 访问，现有设计仍然低效：以 GPU 为中心的执行在每个解码步都要从 CPU 内存取回被选中的 KV 块，使其受限于 PCIe 带宽；而 CPU–GPU 分区执行将 CPU 侧的稀疏注意力置于关键路径之上，导致大量 GPU 时间空闲。本文提出 Mosaic，一个面向 CPU 驻留上下文 KV 的高效长上下文解码的 CPU–GPU 协同块稀疏注意力系统。Mosaic 建立在三个关键洞见之上：输出贡献感知的 KV 预算分配、按头定制且粒度感知的稀疏配置，以及针对 CPU 驻留 KV 上稀疏任务的跨设备协同调度。在这些洞见指导下，Mosaic 集成了一个轻量级头属性预测器、一个粒度–预算选择器和一个基于优先级的调度器，来自动配置并协同稀疏注意力，在保持输出质量的同时提升异构架构上的效率。在 2 个模型、3 个基准和 40 个任务上，Mosaic 保持了接近 FULL 的质量，同时取得优于所评估基线的整体质量–效率权衡。与质量最佳的固定 Quest 配置相比，Mosaic 将 TPOT 最多提升 3.7×。我们进一步在四种硬件配置以及大模型多 GPU 部署中验证了 Mosaic。

## 英文关键词
Block-Sparse Attention, Long-Context Decoding, CPU-GPU Coordination

## 中文关键词
块稀疏注意力，长上下文解码，CPU-GPU 协同

[返回 Session 7](index.md) · [返回 ATC 2026](../index.md)
