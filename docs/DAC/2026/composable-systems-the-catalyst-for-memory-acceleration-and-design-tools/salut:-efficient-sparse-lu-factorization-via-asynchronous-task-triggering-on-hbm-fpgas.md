SALUT: Efficient Sparse LU Factorization via Asynchronous Task Triggering on HBM FPGAs
Authors：
[Xin Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=48807384520479066901)，[Zhenhua Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7271925089728609761)，[Dan Niu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7884946531263773987)，[Zhou Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=0010570373997881637)，[Cheng Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=204443)

## 中文标题

SALUT：在 HBM FPGA 上通过异步任务触发实现的高效稀疏 LU 分解

## 英文摘要

Sparse LU factorization is a critical kernel in scientific computing. Given its irregular data dependencies and complex computation patterns arising from inherent high sparsity, its acceleration remains largely unexplored on FPGAs. The high concurrency capability offered by High Bandwidth Memory (HBM) has recently presented new opportunities. Nevertheless, accelerating sparse LU factorization on HBM-equipped FPGAs remains non-trivial due to rigid dependency synchronization and imbalanced load. In this paper, we propose SALUT, a high-performance sparse LU factorization accelerator on HBM FPGAs. An asynchronous task activation mechanism is developed to pre-compile complex runtime data dependency resolution into fine-grained dependency management, reducing synchronization overhead and maximizing computation parallelism. Additionally, we design a hardware architecture facilitating stream-aware parallel scheduling by decoupling burdensome dependency resolution from task activation, eliminating serial bottleneck of a centralized scheduler. Finally, a locality-aware dual-queue load balancing strategy ensures data locality and high hardware utilization. Evaluations on 15 sparse matrices show that SALUT’s geometric mean throughput and energy efficiency surpass the NVIDIA cuDSS solver by 4.0× and 6.5× on RTX A6000 GPU, and 3.7× and 4.7× on Tesla V100 GPU, respectively.

## 中文摘要

稀疏 LU 分解是科学计算中的关键内核。由于固有的高稀疏性带来不规则的数据依赖和复杂的计算模式，其在 FPGA 上的加速仍鲜有探索。高带宽内存（HBM）所提供的高并发能力近来带来了新的机遇。然而，由于严格的依赖同步和负载不均衡，在配备 HBM 的 FPGA 上加速稀疏 LU 分解仍然并非易事。本文提出 SALUT，一个在 HBM FPGA 上的高性能稀疏 LU 分解加速器。我们开发了一种异步任务激活机制，将复杂的运行时数据依赖解析预先编译为细粒度依赖管理，从而降低同步开销并最大化计算并行度。此外，我们设计了一种硬件架构，通过将繁重的依赖解析与任务激活解耦来实现流感知的并行调度，消除集中式调度器的串行瓶颈。最后，一种局部性感知的双队列负载均衡策略保证了数据局部性和高硬件利用率。在 15 个稀疏矩阵上的评测表明，SALUT 的几何平均吞吐率和能效在 RTX A6000 GPU 上分别超过 NVIDIA cuDSS 求解器 4.0× 和 6.5×，在 Tesla V100 GPU 上分别超过 3.7× 和 4.7×。

## 英文关键词

Sparse LU factorization, FPGAs, Accelerator, HBM, Asynchronous activation

## 中文关键词

稀疏 LU 分解、FPGA、加速器、HBM、异步激活
