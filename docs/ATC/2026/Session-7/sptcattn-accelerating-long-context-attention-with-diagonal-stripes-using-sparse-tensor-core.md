# SptcAttn: Accelerating Long-Context Attention with Diagonal Stripes using Sparse Tensor Core

**中文标题**：SptcAttn：利用稀疏张量核加速对角条带形式的长上下文注意力

**所属 Session**：[Session 7: Long-context and Multimodal LLMs](index.md) · [ATC 2026](../index.md)

**作者**：Chenpeng Wu (Shanghai Jiao Tong University), Qiqi Gu (Shanghai Jiao Tong University), Heng Shi (Shanghai Enflame Technology Co.Ltd; Shanghai Jiao Tong University), Jianguo Yao (Shanghai Jiao Tong University), Haibing Guan (Shanghai Jiao Tong University)

## 英文摘要
Long-context LLM inference is increasingly bottlenecked by attention, whose computational cost grows quadratically with sequence length. To alleviate this, recent research has proposed various sparse attention methods that compute only the important regions of the attention matrix. However, on GPUs, this selection operates at block granularity, where each block is either fully computed or entirely skipped. Blocks that partially overlap the selected regions still compute all entries inside them, introducing redundant work. We observe that this redundancy is not random but inherits the geometric structure of the selected pattern, creating an opportunity for hardware-accelerated sparse execution. We present SptcAttn, a system that exploits this band structure by losslessly mapping it to the 2:4 structured sparsity format of Sparse Tensor Cores (SpTCs), without discarding any score selected by the sparse attention pattern. SptcAttn combines three mechanisms: (1) a deterministic column permutation that converts band matrices into SpTC-compatible layout, (2) a block pair selection strategy that constructs well-formed band tiles from diagonal stripes without tile overlap, and (3) kernel integration that absorbs the permutation and metadata preparation into the fused FlashAttention pipeline without explicit data movement. SptcAttn achieves up to 1.55× kernel speedup over the fastest existing sparse kernel. In end-to-end prefill, it preserves the accuracy of the underlying sparse-attention method and achieves an additional 1.06×–1.08× speedup over MInference for sequence lengths of 200K–500K, with a 6.58× speedup over the dense-attention baseline at a sequence length of 500K.

## 中文摘要
长上下文 LLM 推理日益受限于注意力，其计算开销随序列长度呈二次增长。为缓解这一问题，近期研究提出了多种稀疏注意力方法，仅计算注意力矩阵中的重要区域。然而在 GPU 上，这种选择以块为粒度进行，每个块要么被完整计算，要么被完全跳过。与选中区域部分重叠的块仍会计算其内部的全部条目，从而引入冗余工作。我们观察到这种冗余并非随机，而是继承了被选中模式的几何结构，从而为硬件加速的稀疏执行创造了机会。我们提出 SptcAttn，一个利用该带状结构、将其无损映射到稀疏张量核（SpTC）的 2:4 结构化稀疏格式的系统，且不丢弃稀疏注意力模式所选中的任何分数。SptcAttn 结合三种机制：(1) 一种确定性的列置换，将带状矩阵转换为与 SpTC 兼容的布局；(2) 一种块对选择策略，从对角条带构建良构的带状 tile 且不产生 tile 重叠；(3) 内核集成，将置换与元数据准备吸收进融合的 FlashAttention 流水线，而无需显式数据搬移。SptcAttn 相较现有最快的稀疏内核取得最高 1.55× 的内核加速。在端到端预填充中，它保持了底层稀疏注意力方法的精度，并在 200K–500K 序列长度上相较 MInference 额外取得 1.06×–1.08× 加速，在 500K 序列长度下相较稠密注意力基线取得 6.58× 加速。

## 英文关键词
LLMs, Sparse Attention, Sparse Tensor Core, Structured Sparsity

## 中文关键词
LLM，稀疏注意力，稀疏张量核，结构化稀疏

[返回 Session 7](index.md) · [返回 ATC 2026](../index.md)
