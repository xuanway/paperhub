# HeadFlow: Scaling Long-Context Training with Head-Group Activation Residency

**中文标题**：HeadFlow：利用头组激活驻留扩展长上下文训练

**所属 Session**：[Session 7: Long-context and Multimodal LLMs](index.md) · [ATC 2026](../index.md)

**作者**：Yixin Song (Shanghai Jiao Tong University), Jianxiang Gao (Shanghai Jiao Tong University), Shuhuai Zhang (Zhejiang University), Zeyu Mi (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

## 英文摘要
Training generative models on long contexts is increasingly bottlenecked by attention activation GPU residency: activations must be on GPU when they are produced and later reused, yet keeping all of them resident limits context length. This paper presents HeadFlow, a runtime system that recasts attention activation management as a head-group lifetime planning problem. HeadFlow exploits a long-context asymmetry: attention compute grows rapidly with sequence length, while each head group’s activation state grows much more slowly, creating windows that can hide movement. It names semantic activation slots, places them across CPU pinned memory, direct GPU–SSD storage, staged GPU–CPU– SSD paths, or recomputation, and executes the resulting plan with asynchronous save, staged prefetch, and load. We implement HeadFlow by extending FlashAttention-compatible operators with plan-aware asynchronous activation movement, and evaluate it across long-context language and multimodal generative training. On text workloads, HeadFlow trains with 512K–1M-token contexts. Its throughput is 1.33×–1.67× that of state-of-the-art sequence-and context-parallel baselines. To our knowledge, HeadFlow is the first system to train a 24B model with full parameters at 1M context on only eight 96GB H20 GPUs. On image and video workloads, the same runtime extends the maximum trainable effective tokens by 4.0× and achieves a 1.32× speedup. Loss and attention-gradient checks confirm that these gains come from exact activation management rather than approximate attention or lossy execution.

## 中文摘要
在长上下文上训练生成模型日益受限于注意力激活在 GPU 中的驻留：激活在产生时以及后续被复用时都必须位于 GPU 上，而让全部激活都保持驻留会限制上下文长度。本文提出 HeadFlow，一个将注意力激活管理重新表述为头组生命周期规划问题的运行时系统。HeadFlow 利用一种长上下文不对称性：注意力计算量随序列长度迅速增长，而每个头组的激活状态增长得慢得多，从而形成可以掩盖数据搬移的时间窗口。它为语义激活槽命名，并将它们放置于 CPU 固定内存、GPU–SSD 直接存储、GPU–CPU–SSD 分级路径或重计算之中，并通过异步保存、分级预取和加载来执行所生成的方案。我们通过为 FlashAttention 兼容算子扩展方案感知的异步激活搬移来实现 HeadFlow，并在长上下文语言与多模态生成训练上对其进行评估。在文本工作负载上，HeadFlow 可训练 512K–1M token 的上下文，其吞吐是当前最优的序列并行与上下文并行基线的 1.33×–1.67×。据我们所知，HeadFlow 是首个仅在八块 96GB H20 GPU 上即以 1M 上下文训练全参数 24B 模型的系统。在图像和视频工作负载上，同一运行时将最大可训练有效 token 数扩展 4.0×，并取得 1.32× 的加速。损失与注意力梯度校验确认这些收益来自精确的激活管理，而非近似注意力或有损执行。

## 英文关键词
long-context training, activation offloading, GPU memory management

## 中文关键词
长上下文训练，激活卸载，GPU 内存管理

[返回 Session 7](index.md) · [返回 ATC 2026](../index.md)
