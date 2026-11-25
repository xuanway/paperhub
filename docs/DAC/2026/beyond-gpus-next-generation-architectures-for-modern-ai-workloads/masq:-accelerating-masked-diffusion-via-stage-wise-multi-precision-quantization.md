MASQ: Accelerating Masked Diffusion via Stage-Wise Multi-Precision Quantization
Authors：
[Seeyeon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=9616063022675742253)，[Jaehun Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=3077417168512292049)，[Sungyeob Yoo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3635845213729137615)，[Joo-Young Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=013143)

## 中文标题

MASQ：通过阶段式多精度量化加速掩码扩散

## 英文摘要

Masked diffusion enables region-specific image synthesis but suffers from computational redundancy, since the entire image is processed each timestep even though only the masked region requires generation. To address this, we introduce MASQ, a hardware–software co-designed accelerator for masked diffusion. Our approach performs stage-wise MXINT8/4/2 precision assignment that dynamically reflects spatial and semantic importance, complemented by timestep-aware scheduling and optimized non-matrix operations. MASQ features a block-wise multi-precision compute engine and mask management unit, efficiently handling our approach. It achieves up to 16.06× and 5.39× speedup and 4.18× and 4.93× energy-efficiency gain over A100 and Orin NX, respectively, while preserving quality.

## 中文摘要

掩码扩散能够实现区域特定的图像合成，但存在计算冗余：尽管只有被掩码的区域需要生成，每个时间步却要对整幅图像进行处理。为此，我们提出 MASQ，一种面向掩码扩散的软硬件协同设计加速器。我们的方法执行阶段式的 MXINT8/4/2 精度分配，动态反映空间与语义重要性，并辅以时间步感知的调度和优化的非矩阵运算。MASQ 具备块级多精度计算引擎和掩码管理单元，可高效支撑我们的方法。它在保持生成质量的同时，相较 A100 和 Orin NX 分别实现最高 16.06 倍和 5.39 倍的加速，以及 4.18 倍和 4.93 倍的能效收益。

## 英文关键词

Masked Diffusion, Quantization, Hardware-software Co-design

## 中文关键词

掩码扩散、量化、软硬件协同设计
