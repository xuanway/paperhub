RFIPSA: A Reconfigurable FIP-Based Systolic Array for Various Matrix-Intensive Workloads
Authors：
[Zongfan Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4746469000032463938)，[Dong Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3038164904167606743)，[Weijie Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=1877400008414648506)，[Junyi Mai](https://63dac.conference-program.com/?post_type=page&p=15&uid=7981397643211086745)，[Longyuan Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9862006605408658526)，[Enyi Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3161479413500319301)

## 中文标题

RFIPSA：一种面向多种矩阵密集型负载的基于 FIP 的可重构脉动阵列

## 英文摘要

The growing demands of scientific computing and artificial intelligence require high-throughput, flexible, and efficient matrix computation. Conventional systolic arrays suffer from limited computational density, inefficient handling of sparse data, and low memory efficiency when processing dense, sparse, and convolution workloads. This paper presents a reconfigurable systolic array accelerator based on the fast inner product (FIP) algorithm, which reduces hardware resource consumption while supporting both dense and sparse computation modes. To further accelerate sparse computations, a novel sparse encoding scheme is proposed, enabling the accelerator to identify and skip all-zero input vectors with minimal storage overhead. Additionally, a hardware processing module utilizing the memory-efficient convolution algorithm minimizes data redundancy and bandwidth requirements in convolution workloads. The prototype is implemented in 28nm CMOS technology with a 0.31mm2 core area and a 500MHz operating frequency, achieving a 21.3% area reduction and up to 4.4× and 5.1× speedup for SpGEMM and SpMM over GEMM, respectively.

## 中文摘要

科学计算与人工智能日益增长的需求要求高吞吐、灵活且高效的矩阵计算。传统脉动阵列计算密度受限，对稀疏数据的处理效率不足，在处理稠密、稀疏与卷积负载时存储效率偏低。本文提出一种基于快速内积（FIP）算法的可重构脉动阵列加速器，它在降低硬件资源消耗的同时支持稠密与稀疏两种计算模式。为进一步加速稀疏计算，提出一种新颖的稀疏编码方案，使加速器能够以极小的存储开销识别并跳过全零输入向量。此外，一个采用存储高效卷积算法的硬件处理模块最大限度地降低了卷积负载中的数据冗余与带宽需求。该原型采用 28nm CMOS 工艺实现，核心面积 0.31 mm²，工作频率 500 MHz，面积减少 21.3%，SpGEMM 与 SpMM 相较 GEMM 分别实现最高 4.4 倍与 5.1 倍的加速。

## 英文关键词

Systolic arrays, sparsity, hardware acceleration, matrix multiplication

## 中文关键词

脉动阵列、稀疏性、硬件加速、矩阵乘法
