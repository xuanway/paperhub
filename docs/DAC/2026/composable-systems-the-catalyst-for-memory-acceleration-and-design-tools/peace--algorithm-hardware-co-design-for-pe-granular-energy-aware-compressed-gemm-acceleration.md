PEACE: Algorithm–hardware Co-Design for PE-Granular Energy-Aware Compressed GEMM Acceleration
Authors：
[yueting Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=875843)，[Terry Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=682771833433219534)，[He Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=09655647616325659501)，[Zheng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=88592381613098896281)，[Ngai Wong](https://63dac.conference-program.com/?post_type=page&p=15&uid=127343)，[Weisheng Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=061443)

## 中文标题

PEACE：面向 PE 粒度能效感知压缩 GEMM 加速的算法–硬件协同设计

## 英文摘要

General matrix-matrix multiplication (GEMM) remains the dominant computational kernel in transformer-based large language model (LLM) inference. However, large-scale matrices with irregular sparsity limit energy efficiency by hindering regular data access and efficient processing element (PE)-array execution. To address this challenge, we present PEACE, an algorithm-hardware co-design for energy-aware compressed GEMM at the PE-array granularity. PEACE-Alg exploits column-wise energy distribution to restructure large matrices into compressed formats aligned with hardware execution. To support PEACE-Alg, we design PEACE-Hw, which integrates RISC-V ISA extensions, metadata-guided operand scheduling, a reconfigurable systolic PE array, and dedicated partial-sum accumulation support. Experimental results show that PEACE occupies 2.705 mm2 in a 14 nm ASIC, achieves 1.60×–1.67× speedup over a RISC-V core baseline across 14 transformer-based LLMs. Compared with state-of-the-art designs, PEACE achieves 4.4× PE density, 1.79× average speedup, and 2.53× energy efficiency.

## 中文摘要

通用矩阵乘法（GEMM）仍是基于 Transformer 的大语言模型（LLM）推理中的主导计算内核。然而，具有不规则稀疏性的大规模矩阵阻碍了规则的数据访问和高效的 PE 阵列执行，从而限制了能效。为应对这一挑战，我们提出 PEACE，一种在 PE 阵列粒度上进行能效感知压缩 GEMM 的算法–硬件协同设计。PEACE-Alg 利用按列的能耗分布，将大规模矩阵重构为与硬件执行对齐的压缩格式。为支持 PEACE-Alg，我们设计了 PEACE-Hw，它集成了 RISC-V ISA 扩展、元数据引导的操作数调度、可重构脉动 PE 阵列以及专用的部分和累加支持。实验结果表明，PEACE 在 14 nm ASIC 中占用 2.705 mm2，在 14 个基于 Transformer 的 LLM 上相较 RISC-V 核基线实现 1.60×–1.67× 的加速。与最先进的设计相比，PEACE 实现了 4.4× 的 PE 密度、1.79× 的平均加速和 2.53× 的能效提升。

## 英文关键词

GEMM, RISC-V Extension, LLM Inference, Energy Efficiency

## 中文关键词

GEMM、RISC-V 扩展、LLM 推理、能效
