Pipegs: Unlocking 3DGS Pipeline Parallelism via Hierarchical Reuse and Dynamic Partitioning
Authors：
[Xueling Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2620977719502564871)，[Yuzhou Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=5788779660219157624)，[Zhican Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=67813818264358358181)，[Pan Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=02880383341021246181)，[Renda Jian](https://63dac.conference-program.com/?post_type=page&p=15&uid=0476155778749739921)，[Yitian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=13127515961650994351)，[Chen Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9659998036895331133)，[Yang Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2905300192189786719)，[Guanghui He](https://63dac.conference-program.com/?post_type=page&p=15&uid=8245643460890121186)

## 中文标题

PipeGS：通过分层复用与动态划分释放 3DGS 流水线并行性

## 英文摘要

3D Gaussian Splatting (3DGS) delivers high quality and speed for 3D scene reconstruction. However, achieving real-time performance on edge platforms remains challenging due to pipeline inefficiencies. Our profiling reveals two major bottlenecks: (1) insufficient pipeline overlap due to the latency gap between sorting and rasterization, and (2) pipeline parallelism constrained by globally serialized preprocessing. To address these challenges, we present PipeGS, a 3DGS accelerator with algorithm–architecture co-design. At the algorithm level, we propose hierarchical Gaussian reuse, which shortens rasterization latency by eliminating redundant computation and reduces 76.2% of pipeline bubbles. To further unlock full pipeline overlap, we introduce dynamic orthogonal partitioning, which breaks global serial dependencies and hides 63% of preprocessing latency. At the hardware level, PipeGS employs a customized layer-wise pipelined architecture that supports concurrent execution across stages. Implemented on a 28nm technology, PipeGS achieves 1.96∼3.34× on area efficiency, and 1.20∼2.77× on energy efficiency compared with SOTA 3DGS accelerators.

## 中文摘要

3D 高斯泼溅（3DGS）能够高质量、高速度地重建三维场景。然而，由于流水线效率低下，在边缘平台上实现实时性能仍然具有挑战性。我们的分析揭示了两个主要瓶颈：（1）排序与光栅化之间的延迟差距导致流水线重叠不足；（2）全局串行化的预处理限制了流水线并行性。为解决这些问题，我们提出了 PipeGS，一种采用算法-架构协同设计的 3DGS 加速器。在算法层面，我们提出分层高斯复用，通过消除冗余计算缩短光栅化延迟，并减少 76.2% 的流水线气泡。为进一步释放完整的流水线重叠，我们引入动态正交划分，打破全局串行依赖，并隐藏 63% 的预处理延迟。在硬件层面，PipeGS 采用定制的逐层流水线架构，支持各阶段并发执行。PipeGS 在 28nm 工艺上实现，与当前最优的 3DGS 加速器相比，面积效率提升 1.96∼3.34 倍，能效提升 1.20∼2.77 倍。
