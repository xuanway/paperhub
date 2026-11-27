TRIDENT: An End-to-End Streaming Accelerator for TriSpGEMM
Authors：
[Yiyue Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=49724142373422070841)，[an Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8134658102074648313)，[Hui Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=4300636291647906825)，[Luchen Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=8082119408632509892)，[Yongzhang Nie](https://63dac.conference-program.com/?post_type=page&p=15&uid=0676071032836028262)，[Runzhang Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2264517209453053895)，[Gaoyang Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=06183709059483082141)，[xia zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5929097945412870424)，[Yongwen Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=55489797828424985261)

## 中文标题

TRIDENT：面向 TriSpGEMM 的端到端流式加速器

## 英文摘要

Triple Sparse General Matrix-Matrix Multiplication (TriSpGEMM) is a major performance bottleneck in scientific computing and graph analytics. Existing domain-specific accelerators support only Sparse General Matrix-Matrix Multiplication (SpGEMM). Performing TriSpGEMM by sequencing two SpGEMM kernels introduces a global synchronization barrier, forces intermediate data to be written to and read from off-chip memory, and leads to frequent pipeline stalls, all of which significantly degrade performance. A natural solution is to design a fused architecture that executes TriSpGEMM directly, but such a design must overcome three key challenges, i.e., pipeline overflow caused by highly irregular and bursty sparse dataflows, locality inefficiency stemming from the trade-off between input reuse and output aggregation, and severe head-of-line blocking due to variable memory access latencies. In this work, we present TRIDENT, a transient-data-centric accelerator for fused TriSpGEMM processing. TRIDENT integrates a hierarchical flow-control mechanism, a hybrid dataflow co-designed with a windowed sparse format, and an out-of-order decoupled execution scheme to ensure pipeline stability, locality efficiency, and latency tolerance. Comprehensive evaluations demonstrate that TRIDENT achieves an average of 3.56× performance speedup over state-of-the-art SpGEMM accelerators, and up to 49.6× and 6.3× improvements over CPU and GPU baselines, respectively.

## 中文摘要

三稀疏通用矩阵乘法（TriSpGEMM）是科学计算与图分析中的主要性能瓶颈。现有的领域专用加速器仅支持稀疏通用矩阵乘法（SpGEMM）。通过串联两个 SpGEMM 内核来执行 TriSpGEMM 会引入全局同步屏障，迫使中间数据写入并从片外存储器读回，并导致流水线频繁停顿，这些都会显著降低性能。一个自然的解决方案是设计直接执行 TriSpGEMM 的融合架构，但此类设计必须克服三个关键挑战，即高度不规则且突发的稀疏数据流所导致的流水线溢出、源于输入复用与输出聚合之间权衡的局部性低效，以及可变访存延迟造成的严重队头阻塞。在本工作中，我们提出 TRIDENT，一个以瞬态数据为中心的加速器，用于融合式 TriSpGEMM 处理。TRIDENT 集成了分层流控机制、与窗口化稀疏格式协同设计的混合数据流，以及乱序解耦执行方案，以确保流水线的稳定性、局部性效率与延迟容忍能力。全面评估表明，TRIDENT 相比最先进的 SpGEMM 加速器平均取得 3.56× 的性能加速，相比 CPU 与 GPU 基线分别最高提升 49.6× 与 6.3×。

## 英文关键词

Sparse Matrix Multiplication, Streaming Accelerator, Hybrid Dataflow

## 中文关键词

稀疏矩阵乘法、流式加速器、混合数据流
