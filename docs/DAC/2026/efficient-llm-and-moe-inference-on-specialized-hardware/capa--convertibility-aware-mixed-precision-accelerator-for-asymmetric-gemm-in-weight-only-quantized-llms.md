CAPA: Convertibility-Aware Mixed-Precision Accelerator for Asymmetric GEMM in Weight-Only Quantized LLMs
Authors：
[Jihyun Moon](https://63dac.conference-program.com/?post_type=page&p=15&uid=2616483024466107957)，[Insu Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=132743)，[Seungchan Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=51990925849210288371)，[Joon-Sung Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=061143)

## 中文标题

CAPA：面向权重量化 LLM 非对称 GEMM 的可转换性感知混合精度加速器

## 英文摘要

Weight-only quantized large language models (LLMs) have emerged as a standard paradigm for memory-efficient deployment, motivating mixed-precision (FP-INT) arithmetic between integer (INT) quantized weights (Qweights) and floating-point (FP) activations. While FP–INT GEMM accelerators facilitate their execution, prior designs incur high accumulation overheads, underutilize the parallelism of low-precision Qweights, and lack versatility. To address this, we propose CAPA, a convertibility-aware accelerator optimized for asymmetric GEMM, where operands exhibit significant bit-wise precision differences. We introduce Hybrid Delta Block Floating Point (HDBFP), a novel format that converts FP activations to INT while preserving accuracy, thereby maximizing the efficiency of INT-based processing elements (PEs). In addition, our data decomposition scheme significantly enhances computation parallelism for low-precision Qweights within a unified hardware datapath. Together, the CAPA architecture ensures full versatility across common FP16/BF16–INT8/INT4 combinations. Extensive evaluations show that CAPA maintains high accuracy comparable to a GPU baseline across language evaluation benchmarks, improving area efficiency by 3.98× and power efficiency by 4.38× over the FP–FP baseline.

## 中文摘要

权重量化大语言模型（LLM）已成为存储高效部署的标准范式，从而催生了整数（INT）量化权重（Qweight）与浮点（FP）激活之间的混合精度（FP-INT）算术需求。尽管 FP-INT GEMM 加速器便于执行这类运算，但已有设计存在累加开销高、未充分利用低精度 Qweight 的并行性以及通用性不足等问题。为此，我们提出 CAPA，一种面向非对称 GEMM（其操作数之间存在显著的位宽精度差异）优化的可转换性感知加速器。我们提出混合差分块浮点（HDBFP）这一新格式，可在保持精度的同时将 FP 激活转换为 INT，从而最大限度发挥基于 INT 的处理单元（PE）的效率。此外，我们的数据分解方案在统一硬件数据通路中显著提升了低精度 Qweight 的计算并行度。综合而言，CAPA 架构可完整覆盖常见的 FP16/BF16–INT8/INT4 组合，具备充分的通用性。大量评测表明，CAPA 在各项语言评测基准上保持了与 GPU 基线相当的高精度，相比 FP–FP 基线将面积效率提升 3.98×、能效提升 4.38×。
