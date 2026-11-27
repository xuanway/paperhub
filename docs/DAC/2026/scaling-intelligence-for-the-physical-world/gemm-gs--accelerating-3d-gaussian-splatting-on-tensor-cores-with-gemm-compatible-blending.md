GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending
Authors：
[Haomin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=102725310443845334)，[Bowen Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9657746364299696319)，[Fangxin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=318143)，[Zongwu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=073443)，[Xinran Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1829945754236905675)，[Li Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=778143)，[Haibing Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=828243)

## 中文标题

GEMM-GS：基于 GEMM 兼容混合的 Tensor Core 三维高斯溅射加速

## 英文摘要

Neural Radiance Fields (NeRF) enable 3D scene reconstruction from several 2D images but incur high rendering latency via the point-sampling design. 3D Gaussian Splatting (3DGS) improves upon NeRF with explicit scene representation and an optimized pipeline yet still fails to meet practical real-time demands. Existing acceleration methods overlook the evolving Tensor Cores of modern GPUs because the 3DGS pipeline lacks General Matrix Multiplication (GEMM) operations. This paper proposes GEMM-GS, an acceleration approach utilizing Tensor Cores on GPUs via GEMM-friendly blending transformation. It equivalently reformulates the 3DGS blending process into a GEMM-compatible form to utilize Tensor Cores. A high-performance CUDA kernel is designed, integrating a three-stage double-buffered pipeline that overlaps computation and memory access. Extensive experiments show that GEMM-GS achieves 1.42× speedup over vanilla 3DGS and provides an additional 1.47× speedup on average when combining with existing acceleration approaches. Code is released at https://github.com/shieldforever/GEMM-GS.

## 中文摘要

神经辐射场（NeRF）能够由若干二维图像重建三维场景，但其点采样设计带来较高的渲染延迟。三维高斯溅射（3DGS）以显式的场景表示与优化后的流水线改进了 NeRF，但仍无法满足实际的实时性需求。现有加速方法忽视了现代 GPU 不断演进的 Tensor Core，因为 3DGS 流水线缺少通用矩阵乘（GEMM）运算。本文提出 GEMM-GS，一种通过 GEMM 友好的混合变换来利用 GPU Tensor Core 的加速方法。它将 3DGS 的混合过程等价改写为 GEMM 兼容形式，从而得以利用 Tensor Core。本文设计了高性能 CUDA 内核，集成计算与访存相互重叠的三级双缓冲流水线。大量实验表明，GEMM-GS 相较原始 3DGS 实现 1.42× 加速，与现有加速方法结合时可平均额外获得 1.47× 加速。代码见 https://github.com/shieldforever/GEMM-GS。
