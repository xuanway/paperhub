---
title: "SystolicAttention: Fusing FlashAttention within a Single Systolic Array"
description: "MICRO 2026 · Session 8C · SystolicAttention：在单个脉动阵列内融合 FlashAttention"
tags:
  - "MICRO2026"
---

# SystolicAttention: Fusing FlashAttention within a Single Systolic Array

**中文标题：** SystolicAttention：在单个脉动阵列内融合 FlashAttention

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Jiawei Lin, Yuanlong Li, Guokai Chen, Thomas Bourgeat

**来源：** MICRO 2026，pp. 2973–2990；[DOI](https://doi.org/10.1109/MICRO67795.2026.00201)

## 英文摘要

Transformer models rely heavily on the scaled dot product attention operation, SDPA, typically implemented as FlashAttention. Characterized by its frequent interleaving of matrix multiplications and softmax operations, FlashAttention fails to fully utilize the compute resources of modern systolic array based accelerators designed for consecutive and large matrix multiplications, an inefficiency that matters most in long context prefill, where SDPA dominates runtime. To close this utilization gap, we propose FSA, a set of area efficient microarchitectural extensions to the weight stationary systolic array, namely a bidirectional datapath, a comparator row, and per PE interpolation units, that fuse the entire FlashAttention onto the array. These additions modify the PEs and datapath of the array but preserve its programming model and incur minimal additional area. Combined with SystolicAttention, an optimized kernel that achieves fine grained and element wise overlapping of FlashAttention operations, FSA maximizes array utilization while preserving the original floating point operation order of FlashAttention. FSA also provides a Python kernel programming interface, enabling users to write custom attention kernels for diverse attention variants. We implement FSA in synthesizable Chisel RTL and evaluate it against commercial and academic systolic array attention baselines. Against AWS NeuronCore v2 and Google TPUv5e, FSA achieves 2.16 times and 5.45 times higher per array utilization of peak FLOPs per second, respectively, and lower measured per head attention latency despite lower peak throughput. Synthesized in 16 nm at 1.5 GHz, FSA adds 12 percent area over a standard weight stationary systolic array. Compared against FLAT and FuseMax in a common Timeloop and Accelergy framework, FSA improves full model long context prefill latency over the conventional FlashAttention mapping, FLAT, by up to 1.68 times, though FuseMax remains faster at substantially higher area cost.

## 中文摘要

Transformer 模型严重依赖于缩放点积注意力运算 SDPA，通常以 FlashAttention 形式实现。 FlashAttention 的特点是频繁交错矩阵乘法和 softmax 运算，它无法充分利用专为连续和大型矩阵乘法设计的基于现代脉动阵列的加速器的计算资源，这种低效率在长上下文预填充中最为严重，其中 SDPA 在运行时占主导地位。为了弥补这一利用差距，我们提出了 FSA，这是一组对权重固定脉动阵列的面积高效微架构扩展，即双向数据路径、比较器行和每个 PE 插值单元，将整个 FlashAttention 融合到阵列上。这些添加修改了阵列的 PE 和数据路径，但保留了其编程模型并占用了最小的额外面积。与 SystolicAttention（一种优化内核，可实现 FlashAttention 操作的细粒度和元素级重叠）相结合，FSA 最大限度地提高了阵列利用率，同时保留了 FlashAttention 的原始浮点操作顺序。 FSA 还提供了 Python 内核编程接口，使用户能够为不同的注意力变体编写自定义注意力内核。我们在可合成的 Chisel RTL 中实施 FSA，并根据商业和学术收缩阵列注意力基线对其进行评估。与 AWS NeuronCore v2 和 Google TPUv5e 相比，FSA 的每阵列每秒峰值 FLOP 利用率分别提高了 2.16 倍和 5.45 倍，尽管峰值吞吐量较低，但测得的每头注意力时延较低。 FSA 采用 16 nm、1.5 GHz 合成，与标准重量的固定心脉式阵列相比，面积增加了 12%。与常见 Timeloop 和 Accelergy 框架中的 FLAT 和 FuseMax 相比，相比传统 FlashAttention 映射 FLAT，FSA 将完整模型长上下文预填充时延最低降至其 1/1.68，尽管 FuseMax 仍然以更高的面积成本保持更快速度。

## 中文关键词

脉动阵列；FlashAttention；注意力融合；数据流优化

## 代码与研究制品

- 代码仓库：[https://github.com/VCA-EPFL/FSA](https://github.com/VCA-EPFL/FSA)
- 代码与复现实验仓库：[https://github.com/VCA-EPFL/chipyard-fsa](https://github.com/VCA-EPFL/chipyard-fsa)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21494973](https://doi.org/10.5281/zenodo.21494973)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
