STCG: Sparse Tensor Code Generation via Adaptive Tile Scheduling on GPUs with Tensor Cores
Authors：
[Haotian Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=49235609387997067011)，[Yan Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=4176419288101426159)，[Huilong Pi](https://63dac.conference-program.com/?post_type=page&p=15&uid=2726152686101897024)，[KEQIN LI](https://63dac.conference-program.com/?post_type=page&p=15&uid=0311612235283526626)，[Kenli Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=599143)，[Wangdong Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=56643747180580457671)

## 中文标题

STCG：基于自适应分块调度在带 Tensor Core 的 GPU 上生成稀疏张量代码

## 英文摘要

Sparse tensor operations underpin graph neural networks, scientific simulations, and data analytics, yet irregular sparsity leads to highly uneven tile densities and irregular memory access patterns, preventing GPUs from effectively utilizing Tensor Cores and CUDA cores. We present STCG, a compiler–runtime framework for sparse tensor code generation with adaptive tile scheduling on modern GPUs. STCG introduces a four-level IR that separates algebraic lowering, tiling, micro-kernel construction, and heterogeneous kernel assembly. The compiler emits a unified GPU kernel that embeds both WMMA-based Tensor Core micro-kernels and coordinate-indexed FMA kernels under a consistent memory and warp layout, ensuring stable register and shared-memory usage despite irregular sparsity. At runtime, lightweight tile descriptors enable constant-time, per-tile selection between the WMMA and FMA paths, providing data-aware load balancing and eliminating the need for kernel regeneration or manual tuning. On an NVIDIA A100, STCG achieves a 1.13× geometric-mean speedup over the per-dataset best existing method on SpMM and a 5.06× speedup on SpTTM, demonstrating the effectiveness and advancement of our approach across diverse sparsity patterns.

## 中文摘要

稀疏张量运算支撑着图神经网络、科学仿真和数据分析，但不规则稀疏性导致分块密度高度不均、访存模式不规则，使 GPU 无法有效利用 Tensor Core 与 CUDA Core。我们提出 STCG，一个面向现代 GPU 的编译器–运行时框架，用于带自适应分块调度的稀疏张量代码生成。STCG 引入四级 IR，将代数下沉、分块、微内核构建与异构内核组装相互分离。编译器生成统一 GPU 内核，在一致的存储与 warp 布局下嵌入基于 WMMA 的 Tensor Core 微内核和坐标索引的 FMA 内核，从而在不规则稀疏性下仍保持稳定的寄存器与共享内存占用。运行时，轻量级分块描述符支持在 WMMA 与 FMA 路径之间以常数时间逐块选择，实现数据感知的负载均衡，无需重新生成内核或手工调优。在 NVIDIA A100 上，STCG 在 SpMM 上相较各数据集的最优现有方法取得 1.13× 的几何平均加速，在 SpTTM 上取得 5.06× 加速，展示了我们的方法在多种稀疏模式下的有效性与先进性。

## 英文关键词

Irregular Memory Access, Sparse Tensor, Code Generation, Adaptive Tile Scheduling, Tensor Core

## 中文关键词

不规则访存、稀疏张量、代码生成、自适应分块调度、Tensor Core
