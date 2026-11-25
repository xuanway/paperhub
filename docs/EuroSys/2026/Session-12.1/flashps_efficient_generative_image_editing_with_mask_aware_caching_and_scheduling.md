---
title: "FlashPS: Efficient Generative Image Editing with Mask-aware Caching and Scheduling"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Xiaoxiao Jiang (Hong Kong University of Science and Technology), Suyi Li (Hong K"
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# FlashPS: Efficient Generative Image Editing with Mask-aware Caching and Scheduling

**中文标题：** FlashPS：基于掩码感知缓存与调度的高效生成式图像编辑

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Xiaoxiao Jiang (Hong Kong University of Science and Technology), Suyi Li (Hong Kong University of Science and Technology), Lingyun Yang (Hong Kong University of Science and Technology), Tianyu Feng (Hong Kong University of Science and Technology), Zhipeng Di (Alibaba Group), Weiyi Lu (Alibaba Group), Guoxuan Zhu (Alibaba Group), Xiu Lin (Alibaba Group), Kan Liu (Alibaba Group), Yinghao Yu (Alibaba Group), Tao Lan (Alibaba Group), Guodong Yang (Alibaba Group), Lin Qu (Alibaba Group), Liping Zhang (Alibaba Group), Wei Wang (Hong Kong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769379)

## 英文摘要

Generative image editing using diffusion models has become a prevalent application in today’s AI cloud services. In production environments, image editing typically involves a mask that specifies the regions of an image template to be edited. The use of mask provides direct control over the editing process and introduces sparsity in the model inference. In this paper, we present FlashPS, a system that efficiently serves image editing requests. The key insight behind FlashPS is that image editing only modifies the masked regions of image templates, while preserving the original content in the unmasked areas. Driven by this insight, FlashPS judiciously skips redundant computations associated with the unmask areas by reusing cached intermediate activations from previous inferences. To mitigate the high cache loading overhead, FlashPS employs a bubble-free pipeline scheme that overlaps computation with cache loading. Additionally, to reduce queuing latency in online serving while improving the GPU utilization, FlashPS proposes a novel continuous batching strategy for diffusion model serving, allowing newly arrived requests to join the running batch in just one step of denoising computation, without waiting for the entire batch to complete. As heterogenous masks induce imbalanced load, FlashPS also develops a load balancing strategy that takes into account the loads of both computation and cache loading. Collectively, FlashPS outperforms state-of-the-art diffusion serving systems for image editing, achieving up to 3× higher throughput and reducing average request latency by up to 14.7× while ensuring image quality.

## 中文摘要

使用扩散模型的生成式图像编辑已成为当今 AI 云服务中普遍存在的应用。在生产环境中，图像编辑通常涉及一个掩码，用于指定图像模板中需要编辑的区域。掩码的使用为编辑过程提供了直接控制，并在模型推理中引入了稀疏性。本文提出 FlashPS，一个高效服务图像编辑请求的系统。FlashPS 的核心洞见在于：图像编辑只修改图像模板中被掩码覆盖的区域，同时保留未掩码区域的原始内容。在这一洞见的驱动下，FlashPS 通过复用先前推理中缓存的中间激活值，明智地跳过与未掩码区域相关的冗余计算。为缓解高额的缓存加载开销，FlashPS 采用无气泡流水线方案，将计算与缓存加载重叠。此外，为降低在线服务中的排队延迟并提升 GPU 利用率，FlashPS 提出一种面向扩散模型服务的新型连续批处理策略，使新到达的请求仅需一步去噪计算即可加入正在运行的批次，而无需等待整个批次完成。由于异构掩码会导致负载不均衡，FlashPS 还设计了一种同时考虑计算负载与缓存加载负载的负载均衡策略。总体而言，FlashPS 在保证图像质量的同时优于最先进的图像编辑扩散服务系统，吞吐量最高提升 3 倍，平均请求延迟最多降低 14.7 倍。

**英文关键词：** Generative Image Editing; Model Serving

**中文关键词：** 生成式图像编辑、模型服务

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
