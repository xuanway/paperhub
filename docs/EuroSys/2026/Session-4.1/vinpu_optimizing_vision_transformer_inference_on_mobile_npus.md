---
title: "viNPU: Optimizing Vision Transformer Inference on Mobile NPUs"
description: "EuroSys 2026 · On-Device & Federated Learning · Jeho Lee (Yonsei University), Gunjoong Kim (Yonsei University), Chanyoung Jung ("
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# viNPU: Optimizing Vision Transformer Inference on Mobile NPUs

**中文标题：** viNPU：在移动 NPU 上优化视觉 Transformer 推理

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Jeho Lee (Yonsei University), Gunjoong Kim (Yonsei University), Chanyoung Jung (Yonsei University), Jaehee Kim (Yonsei University), Seonghoon Park (Yonsei University), Hojung Cha (Yonsei University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803619)

## 英文摘要

Vision Transformers (ViTs) have emerged as the dominant architecture for visual understanding, powering Vision Foundation Models (VFMs) that excel in zero-shot prediction across diverse environments in spatial computing applications. These applications demand efficient, on-device execution to meet stringent latency requirements, yet deploying large VFMs on mobile Neural Processing Units (NPUs) presents two critical bottlenecks: performance imbalance between the NPU’s heterogeneous compute units, and severe DRAM access overhead in scaled Transformers due to limited on-chip memory. To address these challenges, we propose viNPU, an inference optimization framework that enables efficient execution of VFMs on mobile NPUs. viNPU incorporates (1) sensitivity-guided mixed-precision quantization that effectively balances accuracy and latency; (2) dataflow optimization to maximize on-chip data locality and hardware utilization; and (3) a profiling-based offline stage to ensure real-time performance on mobile NPUs with minimal accuracy drop. Our evaluation on representative VFMs (e.g., Depth Anything V2, Segment Anything) across commercial mobile devices equipped with Qualcomm Hexagon NPUs demonstrates that viNPU achieves an average 11.5× speedup and up to 44.9× energy savings over baselines, while incurring negligible accuracy degradation compared to floating-point executions.

## 中文摘要

视觉 Transformer（ViT）已成为视觉理解的主导架构，支撑着视觉基础模型（VFM），使其在空间计算应用中跨多样环境出色地完成零样本预测。此类应用要求高效的端侧执行以满足严苛的延迟要求，然而在移动神经处理单元（NPU）上部署大型 VFM 面临两个关键瓶颈：NPU 异构计算单元之间的性能不均衡，以及规模扩大后的 Transformer 因片上内存有限而产生严重的 DRAM 访问开销。为应对这些挑战，我们提出 viNPU，一个使 VFM 能在移动 NPU 上高效执行的推理优化框架。viNPU 包含：(1) 敏感度引导的混合精度量化，有效平衡精度与延迟；(2) 数据流优化，以最大化片上数据局部性和硬件利用率；(3) 基于性能分析的离线阶段，确保在移动 NPU 上以极小的精度损失实现实时性能。我们在配备高通 Hexagon NPU 的商用移动设备上对代表性 VFM（如 Depth Anything V2、Segment Anything）进行评估，结果表明 viNPU 相比基线平均取得 11.5 倍加速和最高 44.9 倍的能耗节省，同时相较浮点执行的精度下降可忽略不计。

**英文关键词：** Mobile, Neural Processing Unit, Heterogeneous Computing, Vision Transformer

**中文关键词：** 移动端、神经处理单元、异构计算、视觉 Transformer

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
