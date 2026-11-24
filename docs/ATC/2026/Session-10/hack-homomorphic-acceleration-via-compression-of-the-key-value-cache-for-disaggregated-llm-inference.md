# HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference

**中文标题**：HACK：通过压缩键值缓存实现分离式 LLM 推理的同态加速

**所属 Session**：[Session 10: LLM Inference II](index.md) · [ATC 2026](../index.md)

**作者**：Zeyu Zhang (University of Virginia), Haiying Shen (University of Virginia), Shay Vargaftik (VMware Research by Broadcom), Ran Ben Basat (University College London and Broadcom), Michael Mitzenmacher (Harvard University), Minlan Yu (Harvard University)

## 英文摘要
Disaggregated Large Language Model (LLM) inference has gained popularity by decoupling the compute-intensive prefill stage from the memory-intensive decode stage, enabling the use of low-end, compute-focused GPUs for prefill and high-end, memory-rich GPUs for decode. This separation reduces cost while maintaining high throughput. However, transmitting Key-Value (KV) data between the two stages can induce high overhead, especially for long prompts. Additionally, the computation time overhead for prefill and decode is key for optimizing Job Completion Time (JCT), and KV data size can become prohibitive for long prompts and sequences. Existing KV quantization methods alleviate transmission and memory overhead by storing KV in low-bit formats, but attention still runs on dequantized BF16 KV in every iteration, incurring substantial recurring dequantization overhead and offering no reduction in attention compute. We propose Homomorphic Acceleration via Compression of the Key-Value cache (HACK) for disaggregated LLM inference. HACK keeps KV in a highly compressed INT2 form for transmission and caching, and it computes attention directly on the quantized KV. A lightweight approximation in the epilogue replaces per-iteration dequantization. HACK thereby reduces KV transmission, decode-time memory access, and attention computation together. Extensive trace-driven experiments show that HACK reduces average JCT by up to 70.9% compared to the disaggregated LLM inference baseline and by up to 53.5% compared to state-of-the-art KV quantization methods.

## 中文摘要
分离式大语言模型（LLM）推理通过将计算密集的预填充阶段与内存密集的解码阶段解耦而日益流行，使得能够使用低端、偏重计算的 GPU 进行预填充，并使用高端、内存充足的 GPU 进行解码。这种分离在保持高吞吐的同时降低了成本。然而，在两个阶段之间传输键值（KV）数据会带来高开销，尤其是对于长提示。此外，预填充与解码的计算时间开销对于优化作业完成时间（JCT）至关重要，而 KV 数据规模对于长提示和长序列可能变得难以承受。现有的 KV 量化方法通过以低位格式存储 KV 来缓解传输和内存开销，但注意力在每次迭代中仍在反量化后的 BF16 KV 上运行，导致大量重复的反量化开销，且对注意力计算量没有任何削减。我们提出通过压缩键值缓存实现的同态加速（HACK），用于分离式 LLM 推理。HACK 将 KV 以高度压缩的 INT2 形式保存用于传输和缓存，并直接在量化后的 KV 上计算注意力。尾声（epilogue）中的轻量近似替代了每次迭代的反量化。HACK 因此同时减少了 KV 传输、解码时的内存访问和注意力计算。大量 trace 驱动的实验表明，与分离式 LLM 推理基线相比，HACK 将平均 JCT 降低最多 70.9%，与最先进的 KV 量化方法相比降低最多 53.5%。

## 英文关键词
Large Language Models, Disaggregation, KV Cache, Compression

## 中文关键词
大语言模型，分离，KV 缓存，压缩

[返回 Session 10](index.md) · [返回 ATC 2026](../index.md)
