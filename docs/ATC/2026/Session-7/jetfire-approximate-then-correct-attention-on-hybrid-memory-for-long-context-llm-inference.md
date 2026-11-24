# JetFire: Approximate-then-Correct Attention on Hybrid Memory for Long-Context LLM Inference

**中文标题**：JetFire：面向长上下文 LLM 推理的混合内存先近似后校正注意力

**所属 Session**：[Session 7: Long-context and Multimodal LLMs](index.md) · [ATC 2026](../index.md)

**作者**：Feng Yu (National University of Singapore), Hongshi Tan (National University of Singapore), Yao Chen (Huazhong University of Science and Technology), Gustavo Alonso (ETH Zürich), Weng-Fai Wong (National University of Singapore), Bingsheng He (National University of Singapore)

## 英文摘要
Long-context LLM inference is bottlenecked by GPU high-bandwidth memory (HBM), which the key–value (KV) cache rapidly exhausts. Existing designs compress, select, or offload KV entries, exposing trade-offs among HBM use, approximation error, and data movement. Our key insight is that locating the few tokens that dominate attention needs far less precision than computing the output over them: a heavily quantized cache can no longer reproduce the output, yet it still ranks tokens reliably. JetFire exploits this asymmetry with an approximate-then-correct (ATC) attention backend over hybrid memory. A dense low-precision pipeline scans a compact replica of the whole sequence in GPU HBM, fitting long contexts without dropping tokens. A sparse high-precision pipeline on the CPU corrects the dominant tokens from the full-precision replica in host DRAM. The correction overlaps the GPU value phase when transfer and computation fit within it. JetFire remains near-lossless relative to full attention, and JetFire-K3V2 achieves 1.3–3.0× speedup in end-to-end execution time over TurboQuant within vLLM at the largest common contexts. Against offloading-based systems, it achieves 1.4–2.7× speedup over NEO and 13–180× over InfiniGen. JetFire is open-sourced at https://github.com/Xtra-Computing/JetFire.

## 中文摘要
长上下文 LLM 推理受限于 GPU 高带宽内存（HBM），而键值（KV）缓存会迅速将其耗尽。现有设计通过压缩、选择或卸载 KV 条目，在 HBM 占用、近似误差与数据搬移之间呈现权衡。我们的关键洞见是：定位主导注意力的少数 token 所需的精度远低于在这些 token 上计算输出所需的精度——一个高度量化的缓存已无法重现输出，却仍能可靠地对 token 排序。JetFire 利用这一不对称性，在混合内存上实现先近似后校正（ATC）的注意力后端。一条稠密低精度流水线在 GPU HBM 中扫描整个序列的紧凑副本，从而在不丢弃 token 的情况下容纳长上下文。一条运行在 CPU 上的稀疏高精度流水线则从主机 DRAM 中的全精度副本校正主导 token。当传输与计算能够容纳于其中时，校正会与 GPU 的 value 阶段重叠。JetFire 相对全注意力保持近乎无损，且在 vLLM 内、在最大的公共上下文长度下，JetFire-K3V2 相较 TurboQuant 在端到端执行时间上取得 1.3–3.0× 的加速。相较基于卸载的系统，它相较 NEO 取得 1.4–2.7× 加速，相较 InfiniGen 取得 13–180× 加速。JetFire 已开源于 https://github.com/Xtra-Computing/JetFire。

## 英文关键词
Long-context LLM Inference, Approximate-then-Correct Attention, Hybrid Memory

## 中文关键词
长上下文 LLM 推理，先近似后校正注意力，混合内存

## 代码与研究制品

- [code](https://github.com/Xtra-Computing/JetFire)

[返回 Session 7](index.md) · [返回 ATC 2026](../index.md)
