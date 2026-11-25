Hiband: A Hierarchical Bandwidth-Aware HB-DRAM Accelerator with Array-Level Co-Execution and Reconfigurable NoC for LLM Inference
Authors：
[Huanyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7761256586013904895)，[Yang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7099970319230005875)，[Yutong Su](https://63dac.conference-program.com/?post_type=page&p=15&uid=94777913862125220201)，[Jiaxin Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=121589118336675812)，[Yang Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2905300192189786719)，[Shouyi Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=573143)

## 中文标题

HiBand：具备阵列级协同执行与可重构 NoC 的分层带宽感知 HB-DRAM LLM 推理加速器

## 英文摘要

Hybrid-bonding 3D DRAM (HB-DRAM) delivers massive in-situ bandwidth but shifts LLM accelerator bottlenecks from off-chip memory to the Network-on-Chip (NoC), where decentralized bank-local bandwidth must be coordinated across arrays. We present HiBand, a bandwidth-aware HB-DRAM accelerator that co-designs array-level execution with a four-mode reconfigurable NoC. HiBand combines grouped tensor parallelism and cross-head array-level co-execution to confine most traffic to short-range links while overlapping bandwidth-bound attention with compute-bound feedforward layers. On LLM models mapped to a 32-array HB-DRAM accelerator, HiBand achieves up to 4.28× speedup over an HBM3 GPU-style accelerator and 1.67× speedup over a state-of-the-art HB-DRAM–based NMP design.

## 中文摘要

混合键合 3D DRAM（HB-DRAM）提供了巨大的原位带宽，但也将 LLM 加速器的瓶颈从片外存储转移到片上网络（NoC）——其中分散的 bank 本地带宽必须在各阵列之间加以协调。我们提出 HiBand，一种将阵列级执行与四模式可重构 NoC 协同设计的带宽感知 HB-DRAM 加速器。HiBand 结合分组张量并行与跨 head 的阵列级协同执行，将大部分流量限制在短距离链路上，同时使带宽受限的注意力层与计算受限的前馈层相互重叠。在映射到 32 阵列 HB-DRAM 加速器的 LLM 模型上，HiBand 相比 HBM3 GPU 风格的加速器最高取得 4.28× 的加速，相比最先进的基于 HB-DRAM 的 NMP 设计取得 1.67× 的加速。

## 英文关键词

hybrid bonding, near-memory processing, large language model accelerator, architecture

## 中文关键词

混合键合、近存处理、大语言模型加速器、体系结构
