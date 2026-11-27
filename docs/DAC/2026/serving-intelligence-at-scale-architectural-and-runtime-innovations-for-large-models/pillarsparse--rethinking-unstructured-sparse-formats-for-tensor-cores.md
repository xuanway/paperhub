Pillarsparse: Rethinking Unstructured Sparse Formats for Tensor Cores
Authors：
[Junyu Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0952971446514178056)，[Jue Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=00996801888862961801)，[Zhikuang Xin](https://63dac.conference-program.com/?post_type=page&p=15&uid=1362586061035718928)，[Zhiqiang Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2745014264673353233)，[Zongguo Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6345023331199974325)，[Hongyu Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=92220679855125957011)，[Peng DI](https://63dac.conference-program.com/?post_type=page&p=15&uid=3363019884142162748)，[Yangang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9420739184982212218)

## 中文标题

PillarSparse：重新审视面向张量核的非结构化稀疏格式

## 英文摘要

Accelerating SpMM and SDDMM on Tensor Cores is vital for GNNs and HPC. Current methods suffer from severe bottlenecks, including multi-level pointer chasing, lack of metadata coalescing for vectorization, and high format conversion overhead. We propose PillarSparse with the Pillar CSR format. It organizes non-zeros into "Pillar" (non-zero column) units and uses metadata coalescing to pack all metadata into two integers. This design removes a pointer-chasing level, enables a single vectorized load, and allows a high-speed conversion algorithm using parallel primitives. The co-designed SpMM and SDDMM kernels use warp specialization producer-consumer pipeline and tensor memory accelerator for efficient execution. Experiments show competitive performance.

## 中文摘要

在张量核上加速 SpMM 与 SDDMM 对 GNN 与 HPC 至关重要。现有方法面临严重瓶颈，包括多级指针追逐、缺乏面向向量化的元数据合并，以及较高的格式转换开销。我们提出 PillarSparse 及其 Pillar CSR 格式。该格式将非零元组织为“Pillar”（非零列）单元，并利用元数据合并将所有元数据打包为两个整数。这一设计消除了一级指针追逐，支持单次向量化加载，并允许使用并行原语实现高速的转换算法。协同设计的 SpMM 与 SDDMM kernel 采用 warp 特化的生产者—消费者流水线以及张量内存加速器，以实现高效执行。实验表明其性能具有竞争力。

## 英文关键词

GPU Parallel Algorithm, Tensor Cores, SpMM, SDDMM

## 中文关键词

GPU 并行算法、张量核、SpMM、SDDMM
