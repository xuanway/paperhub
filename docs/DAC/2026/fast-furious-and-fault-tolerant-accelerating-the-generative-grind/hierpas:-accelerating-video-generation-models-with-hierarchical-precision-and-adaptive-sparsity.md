HierPAS: Accelerating Video Generation Models with Hierarchical Precision and Adaptive Sparsity
Authors：
[Changxu Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=52175390508353596401)，[Yifan Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=6223656964742460504)，[Ruibin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=26011828880730061001)，[Fan Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=332243)

## 中文标题

HierPAS：以层次化精度与自适应稀疏性加速视频生成模型

## 英文摘要

Diffusion Transformer (DiT)-based video generation models (VGMs) achieve state-of-the-art visual quality through global attention modeling but incur heavy computational overhead due to the quadratic complexity of attention. In high-resolution or long-duration videos, attention often dominates inference latency. However, much of this computation is redundant—many attention scores contribute little to the output and can be safely skipped or approximated. Fully exploiting this redundancy requires (1) identifying important regions in large attention maps, (2) determining adaptive retention ratios across heads and blocks, and (3) handling scores of varying importance efficiently. We present HierPAS, a hardware–software co-optimized design that accelerates VGMs using hierarchical precision and adaptive sparsity. HierPAS employs a lightweight eager attention method to estimate attention patterns and a sampling-based entropy analysis to derive head-wise retention ratios with minimal cost. It applies progressively reduced precision to less critical regions and integrates a configurable top-𝑘engine with a unified multi-precision GEMM engine supporting multiple precisions in one datapath. Evaluations show that HierPAS improves energy efficiency by up to 178× over NVIDIA H20 and 7.7× over state-of-the-art accelerators, with negligible loss in video quality.

## 中文摘要

基于扩散 Transformer（DiT）的视频生成模型（VGM）通过全局注意力建模实现了最先进的视觉质量，但由于注意力的二次复杂度而带来沉重的计算开销。在高分辨率或长时长视频中，注意力往往主导推理延迟。然而，其中大部分计算是冗余的——许多注意力分数对输出的贡献很小，可以被安全地跳过或近似。充分挖掘这种冗余性需要：(1) 在大型注意力图中识别重要区域；(2) 确定跨注意力头与块的自适应保留比例；(3) 高效处理重要性各异的分数。我们提出 HierPAS，一种软硬件协同优化的设计，利用层次化精度与自适应稀疏性加速 VGM。HierPAS 采用轻量级的 eager 注意力方法估计注意力模式，并通过基于采样的熵分析以极小开销推导逐头保留比例。它对不太关键的区域施加逐级降低的精度，并将可配置的 top-k 引擎与支持单条数据通路多种精度的统一多精度 GEMM 引擎集成。评估显示，HierPAS 相比 NVIDIA H20 提升能效最多 178×，相比最先进加速器提升 7.7×，而视频质量损失可忽略不计。
