Fusedot: A Multiplication-Fused Dot Product Accelerator for Efficient LLM Inference
Authors：
[Wenju Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=97083077689760099811)，[Jianhui Yue](https://63dac.conference-program.com/?post_type=page&p=15&uid=677143)，[Pengcheng Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8850503783973072981)，[Yujia Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=01419265174390406431)，[Qinggang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=40659363708189088741)，[Yufei Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=98782252090035527181)，[Jiaqi Zhai](https://63dac.conference-program.com/?post_type=page&p=15&uid=53817510128136941461)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)

## 中文标题

FuseDot：面向高效 LLM 推理的乘法融合点积加速器

## 英文摘要

Weight quantization enables efficient LLM inference but requires mixed-precision computation (e.g., FP16×INT4), which is not efficient in general-purpose processors. Existing accelerators integrate custom mixed-precision arithmetic units but follow the dot-product paradigm, which suffers from numerous multiplications. This work exploits multiplication fusion in low-bit quantization and introduces MFDP, a novel dot-product paradigm that fuses identical-weight multiplications into a single operation. Based on MFDP, we propose FuseDot, an accelerator that optimizes the fusion process by incorporating index-driven generalized matrix multiplication and a hierarchical dual-phase reordering algorithm. Additionally, a cross-PE multiplier-sharing architecture with a half-multiplier scheme further amortizes multiplier costs across multiple PEs. This work achieves 1.51–1.98× performance speedups and 1.19–1.51× higher energy efficiency over state-of-the-art accelerators.

## 中文摘要

权重量化能够支撑高效的 LLM 推理，但需要混合精度计算（例如 FP16×INT4），而这在通用处理器上并不高效。现有加速器虽然集成了定制的混合精度算术单元，但仍遵循点积范式，因而包含大量乘法运算。本工作利用低比特量化中的乘法融合，提出 MFDP——一种将相同权重的乘法融合为单次运算的新型点积范式。基于 MFDP，我们提出 FuseDot 加速器，通过引入索引驱动的广义矩阵乘法与分层双阶段重排序算法来优化融合过程。此外，一种跨 PE 的乘法器共享架构结合半乘法器方案，进一步在多个 PE 之间分摊乘法器开销。与当前最先进的加速器相比，本工作实现了 1.51–1.98 倍的性能加速和 1.19–1.51 倍的能效提升。
