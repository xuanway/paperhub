---
title: "ORANGE: Exploring \underline{O}ckham's \underline{R}azor for Neural Rendering by \underline{A}ccelerating 3DGS on \underline{N}PUs with \underline{GE}MM-Friendly Blending and Balanced Workloads"
description: "HPCA 2026 · 3D Graphics and Rendering Acceleration"
tags:
  - "HPCA2026"
  - "3D Graphics and Rendering Acceleration"
---

# ORANGE: Exploring \underline{O}ckham's \underline{R}azor for Neural Rendering by \underline{A}ccelerating 3DGS on \underline{N}PUs with \underline{GE}MM-Friendly Blending and Balanced Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: 3D Graphics and Rendering Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 3D Graphics and Rendering Acceleration</p>
</div>

**论文链接**：
**作者**：Haomin Li Shanghai Jiao Tong University , Yue Liang Shanghai Jiao Tong University , Fangxin Liu Shanghai Jiao Tong University , Bowen Zhu Shanghai Jiao Tong University , Zongwu Wang Shanghai Jiao Tong University , Yu Feng Shanghai Jiao Tong University , Liqiang Lu Zhejiang University , Li Jiang Shanghai Jiaotong University , Haibing Guan Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

ORANGE：以 GEMM 友好的混合与均衡负载在 NPU 上加速 3DGS，探索神经渲染中的奥卡姆剃刀

## 英文摘要

3D Gaussian Splatting (3DGS) is an emerging neural rendering technique that delivers efficient and high-fidelity rendering, meeting the growing demands of applications such as AR/VR. As 3DGS is increasingly integrated into diverse applications, DNNs are often deployed alongside it to support tasks such as skeletal pose estimation for human avatars or semantic processing for 3D perception. Unfortunately, existing domain-specific accelerators (DSAs) designed for 3DGS excel at rendering but struggle to execute DNN workloads efficiently. Moreover, these DSAs incur significant design and fabrication costs, limiting their practicality. To address these challenges, we propose ORANGE, a novel approach that enables general-purpose DNN-oriented Neural Processing Units (NPUs) to efficiently execute 3DGS without requiring specialized accelerators. The key insight of ORANGE is that we introduce a GEMM-friendly blending process, which reformulates the conventional 3DGS blending operation to fully utilize the matrix multiplication units prevalent in NPUs during rendering. Additionally, to mitigate workload imbalances caused by variable execution latencies across tiles, we develop a sampling-based latency prediction method paired with a tile batching strategy to minimize idle computing resources. Experiments demonstrate that ORANGE achieves up to 1.67× and 15.5× speedup compared to state-of-the-art 3DGS accelerators and the NVIDIA Xavier NX GPU, respectively, in neural rendering tasks. Our approach offers a cost-effective and versatile solution, adhering to the principle of Ockham's Razor by maximizing efficiency without specialized hardware.

## 中文摘要

3D 高斯泼溅（3DGS）是一种新兴的神经渲染技术，可提供高效且高保真的渲染，满足 AR/VR 等应用日益增长的需求。随着 3DGS 日益集成到各类应用中，深度神经网络（DNN）常被一并部署，以支持人体化身的骨骼姿态估计或 3D 感知的语义处理等任务。遗憾的是，现有面向 3DGS 的领域专用加速器（DSA）擅长渲染，却难以高效执行 DNN 负载；此外，此类 DSA 的设计与制造成本高昂，限制了其实用性。为应对这些挑战，我们提出 ORANGE——一种让通用、面向 DNN 的神经网络处理器（NPU）无需专用加速器即可高效执行 3DGS 的新方法。ORANGE 的核心思路是引入 GEMM 友好的混合（blending）过程，将传统 3DGS 混合操作重新表述，从而在渲染时充分利用 NPU 中广泛存在的矩阵乘法单元。此外，为缓解分块（tile）间执行时延差异导致的工作负载不均衡，我们提出基于采样的时延预测方法，并结合分块批处理策略，以最小化计算资源的空闲。实验表明，在神经渲染任务中，ORANGE 相较最先进的 3DGS 加速器与 NVIDIA Xavier NX GPU 分别取得最高 1.67 倍与 15.5 倍加速。该方法无须专用硬件即可最大化效率，秉持奥卡姆剃刀原则，提供了一种高性价比且通用的解决方案。
