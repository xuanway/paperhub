Is 2D Gaussian Enough? A Sort-Free 3D Gaussian Splatting Inference Architecture with Geometry Guidance
Authors：
[Yuanfang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2273627475927926002)，[Yu Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=2094123896057450545)，[Runzhou Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=10982574014377407061)，[Jun Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=639243)，[Kun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=565843)

## 中文标题

二维高斯足够吗？一种几何引导的无排序三维高斯泼溅推理架构

## 英文摘要

3D Gaussian Splatting (3DGS) has emerged as the state-of-the-art (SOTA) technique for high-fidelity, real-time novel view synthesis. However, sorting of all contributing primitives fundamentally seri-alizes the rendering process, breaking dataflow parallelism and posing a significant implementation challenge for resource-constrained hardware accelerators. While prior sort-free algorithms based on commutative weighted sums eliminate this dependency, they introduce visual artifacts and have redundant computation. This paper introduces a geometry-guided coarse-to-fine rendering algorithm that fundamentally resolves the trade-off between sorting and computation efficiency. Our method employs a two-stage pipeline: First, a lightweight 2D Gaussian (2DGS) model is rendered via the nearest Gaussian’s color. Subsequently, this depth map is utilized as geometric guidance for the second stage: a sort-free, weighted rendering of the complete 3DGS model. We further propose CODA (A Co-Optimized Depth-guided Architecture), a unified hardware accelerator co-optimized to execute this 2D-3D hybrid pipeline in a deeply pipelined dataflow. By reusing computational resources for both the 2D and the 3D Gaussian rendering pass, CODA maximizes hardware utilization. Experimental results demonstrate that CODA exhibits an 8.4× to 11.6× speedup over the NVIDIA RTX 3060M and a 2.7× to 3.9× speedup over the NVIDIA RTX 4090. When compared with previous 3DGS accelerators, CODA exhibits a 6.1× and 1.3× speedup over the GSCore and Local-GS, respectively.

## 中文摘要

三维高斯泼溅（3DGS）已成为高保真实时新视角合成的最先进（SOTA）技术。然而，对所有有贡献图元进行排序从根本上将渲染过程串行化，破坏了数据流并行性，并给资源受限的硬件加速器带来了重大实现挑战。尽管此前基于可交换加权求和的无排序算法消除了这一依赖，但它们会引入视觉伪影且存在冗余计算。本文提出一种几何引导的由粗到细渲染算法，从根本上化解排序与计算效率之间的权衡。我们的方法采用两阶段流水线：首先，以最近高斯的颜色渲染一个轻量级二维高斯（2DGS）模型。随后，该深度图被用作第二阶段的几何引导：对完整的 3DGS 模型进行无排序的加权渲染。我们进一步提出 CODA（一种协同优化的深度引导架构），这是一种统一硬件加速器，经过协同优化以深度流水化的数据流执行该二维—三维混合流水线。通过在二维与三维高斯渲染两遍中复用计算资源，CODA 最大化了硬件利用率。实验结果表明，CODA 相较于 NVIDIA RTX 3060M 取得 8.4× 至 11.6× 的加速比，相较于 NVIDIA RTX 4090 取得 2.7× 至 3.9× 的加速比。与此前的 3DGS 加速器相比，CODA 相较 GSCore 与 Local-GS 分别取得 6.1× 与 1.3× 的加速比。
