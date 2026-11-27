CORE: Compact, Optimized, and Resource-Efficient Compute Engine for FP-INT GEMM Acceleration with Binary Coding Quantization
Authors：
[Chaewon Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=635592578782864441)，[Inseong Hwang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6863641308539424176)，[Beom Jin Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8879131034795688951)，[Hyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=757143)

## 中文标题

CORE：面向二值编码量化的 FP-INT GEMM 加速的紧凑、优化且资源高效计算引擎

## 英文摘要

Recent advances in large language models (LLMs) have led to rapid growth in parameter sizes, exacerbating memory and computational bottlenecks. Weight-only quantization mitigates storage overhead but retains floating-point (FP) activations, resulting in costly FP execution. Binary coding quantization (BCQ) alleviates this by replacing many FP multiplications with additions, yet still relies on FP scaling operations and suffers from limited representational capacity, causing non-trivial accuracy loss. To overcome these limitations, we propose a sum-of-power-of-two scaling factor–based BCQ (SS-BCQ), which approximates FP scaling factors using a small set of power-of-two terms, eliminating FP multiplications via shift–add operations while preserving accuracy. To efficiently support SS-BCQ, we introduce CORE, a fully pipelined FP–INT GEMM engine featuring (i) adaptive block-wise activation scaling to reduce scaling overhead, and (ii) a lightweight processing unit for selectively preserving high-importance weights. On OPT-6.7B, SS-BCQ reduces perplexity by 3.14 over prior BCQ methods. Integrated with CORE, our approach achieves up to 1.41× higher area efficiency (TOPS/𝑚𝑚2) and 2.18× higher energy efficiency (TOPS/W) than state-of-the-art FP–INT accelerators, enabling an efficient low-precision execution path for on-device LLMs.

## 中文摘要

大语言模型（LLM）的最新进展使参数量迅速增长，加剧了存储与计算瓶颈。权重量化缓解了存储开销，但保留浮点（FP）激活，导致执行代价高昂。二值编码量化（BCQ）通过以加法替代大量 FP 乘法来缓解该问题，但仍依赖 FP 缩放操作，且表示能力有限，造成不可忽视的精度损失。为克服这些局限，我们提出基于二次幂和缩放因子的 BCQ（SS-BCQ），它用少量二次幂项近似 FP 缩放因子，通过移位-加法操作消除 FP 乘法，同时保持精度。为高效支持 SS-BCQ，我们提出 CORE，一个全流水的 FP–INT GEMM 引擎，其特点包括：(i) 自适应块级激活缩放以降低缩放开销；(ii) 一个轻量处理单元，用于选择性保留高重要性权重。在 OPT-6.7B 上，SS-BCQ 相比先前的 BCQ 方法将困惑度降低 3.14。与 CORE 相结合，我们的方法相比最先进的 FP–INT 加速器最高取得 1.41× 的面积效率（TOPS/mm²）提升和 2.18× 的能效（TOPS/W）提升，为端侧 LLM 提供了一条高效的低精度执行路径。

## 英文关键词

FP–INT GEMM accelerator, Resource-Efficient Processing unit, Binary coding quantization, Power-of-Two scaling, On-device LLMs

## 中文关键词

FP–INT GEMM 加速器、资源高效处理单元、二值编码量化、二次幂缩放、端侧 LLM
