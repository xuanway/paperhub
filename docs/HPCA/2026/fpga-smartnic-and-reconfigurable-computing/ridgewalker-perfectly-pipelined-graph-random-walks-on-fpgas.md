---
title: "RidgeWalker: Perfectly Pipelined Graph Random Walks on FPGAs"
description: "HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing"
tags:
  - "HPCA2026"
  - "FPGA, SmartNIC, and Reconfigurable Computing"
---

# RidgeWalker: Perfectly Pipelined Graph Random Walks on FPGAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: FPGA, SmartNIC, and Reconfigurable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing</p>
</div>

**论文链接**：
**作者**：Hongshi Tan National University of Singapore , Yao CHEN , Xinyu Chen Hong Kong University of Science and Technology , Qizhen Zhang University of Toronto , Cheng Chen ByteDance, China , Weng-Fai Wong National University of Singapore , Bingsheng He National University of Singapore
**会议**：HPCA 2026

---

## 中文标题

RidgeWalker：FPGA 上完美流水化的图随机游走

## 英文摘要

Graph Random Walks (GRWs) offer efficient approximations of key graph properties and have been widely adopted in many applications. However, GRW workloads are notoriously difficult to accelerate due to their strong data dependencies, irregular memory access patterns, and imbalanced execution behavior. While recent work explores FPGA-based accelerators for GRWs, existing solutions fall far short of hardware potential due to inefficient pipelining and static scheduling. This paper presents RidgeWalker, a high-performance GRW accelerator designed for datacenter FPGAs. The key insight behind RidgeWalker is that the Markov property of GRWs allows decomposition into stateless, fine-grained tasks that can be executed out-of-order without compromising correctness. Building on this insight, RidgeWalker introduces an asynchronous pipeline architecture with a feedback-driven scheduler grounded in queuing theory. This design enables perfect pipelining and adaptive load balancing. We prototype RidgeWalker on FPGAs and evaluate its performance across a range of GRW algorithms and real-world graph datasets. Experimental results demonstrate that RidgeWalker achieves an average speedup of 7.0× over state-of-the-art FPGA solutions and 8.1× over GPU solutions, with peak speedups of up to 71.0× and 22.9×, respectively. The source code is publicly available at https://github.com/Xtra-Computing/RidgeWalker.

## 中文摘要

图随机游走（GRW）能高效近似关键的图属性，已在众多应用中被广泛采用。然而 GRW 负载因强数据依赖、不规则内存访问模式和执行不均衡而极难加速。尽管近期已有面向 GRW 的 FPGA 加速器探索，但受限于低效的流水化与静态调度，现有方案远未发挥硬件潜力。本文提出 RidgeWalker，一款为数据中心 FPGA 设计的高性能 GRW 加速器。其关键洞见是：GRW 的马尔可夫性质允许将其分解为无状态、细粒度的任务，这些任务可乱序执行而不损害正确性。基于此，RidgeWalker 引入异步流水架构，并配备以排队论为基础的反馈驱动调度器，从而实现完美流水化与自适应负载均衡。我们在 FPGA 上构建 RidgeWalker 原型，并在多种 GRW 算法与真实图数据集上评估其性能。实验结果表明，RidgeWalker 相比最先进的 FPGA 方案平均加速 7.0 倍，相比 GPU 方案平均加速 8.1 倍，峰值加速分别可达 71.0 倍和 22.9 倍。源代码已在 https://github.com/Xtra-Computing/RidgeWalker 公开。
