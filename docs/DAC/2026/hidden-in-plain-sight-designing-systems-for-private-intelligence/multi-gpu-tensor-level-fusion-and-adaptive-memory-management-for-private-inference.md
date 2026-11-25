Multi‑GPU Tensor‑Level Fusion and Adaptive Memory Management for Private Inference
Authors：
[Homer Gamil](https://63dac.conference-program.com/?post_type=page&p=15&uid=160343)，[Michail Maniatakos](https://63dac.conference-program.com/?post_type=page&p=15&uid=299443)

## 中文标题

面向隐私推理的多 GPU 张量级融合与自适应内存管理

## 英文摘要

Privacy-preserving machine learning via Fully Homomorphic Encryption (FHE) offers strong data confidentiality guarantees but suffers from prohibitive computational overhead. In this work, we improve the performance of private inference via FHE on multi-GPU environments. We achieve this through three key innovations: (1) an optimized tensor-level FHE library based on the CKKS scheme that fuses low-level encrypted primitives into high-throughput GPU kernels, (2) an adaptive memory manager that dynamically orchestrates encrypted-tensor placement to control peak memory usage, and (3) a multi-GPU execution engine that partitions and balances workloads across devices to maximize utilization under constrained memory budgets. We evaluate our method on representative encrypted-ML benchmarks and compare against state-of-the-art CPU-and GPU-based FHE systems, showing comparable single-GPU results since no existing work provides a multi-GPU implementation. Our eight-GPU configuration achieves strong scaling of 7.14× over the single-GPU execution, which in turn yields a 9.7× end-to-end cumulative improvement over the best prior work. We additionally implement all fused tensor-level operators within a full ResNet-20 inference pipeline on CIFAR-10, demonstrating that the method generalizes beyond MNIST-scale workloads. Results show efficient parallel scaling, with 8-GPU execution on ResNet-20 reaching 7.1× speedup over the state of the art.

## 中文摘要

基于全同态加密（FHE）的隐私保护机器学习提供了强数据机密性保障，但其计算开销高得难以承受。本文在多 GPU 环境下提升基于 FHE 的隐私推理性能，通过三项关键创新实现：(1) 基于 CKKS 方案的优化张量级 FHE 库，将底层加密原语融合为高吞吐 GPU 内核；(2) 自适应内存管理器，动态编排加密张量的放置以控制峰值内存占用；(3) 多 GPU 执行引擎，在受限内存预算下跨设备切分并均衡工作负载，以最大化利用率。我们在代表性加密机器学习基准上评估该方法，并与当前最优的基于 CPU 与 GPU 的 FHE 系统比较；由于尚无多 GPU 实现，单 GPU 结果与之一致。我们的八 GPU 配置相对单 GPU 执行实现了 7.14 倍强扩展，而单 GPU 执行本身已较此前最优工作带来 9.7 倍的端到端累计提升。此外，我们在 CIFAR-10 上完整的 ResNet-20 推理流水线中实现了全部融合张量级算子，表明该方法可推广至 MNIST 规模之外的工作负载。结果表明并行扩展高效：8 GPU 执行 ResNet-20 相比当前最优实现达到 7.1 倍加速。

## 英文关键词

Fully Homomorphic Encryption, Multi-GPU, Encrypted inference

## 中文关键词

全同态加密、多 GPU、加密推理
