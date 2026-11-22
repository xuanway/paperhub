---
title: "Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving"
description: "MICRO 2026 · Session 2A · 面向高能效与低成本 LLM 服务的异构神经处理单元自动扩缩容"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Energy Efficiency"
  - "Neural Networks"
---

# Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving

**中文标题：** 面向高能效与低成本 LLM 服务的异构神经处理单元自动扩缩容

**所属 Session：** [Session 2A](index.md) · [MICRO 2026](../index.md)

**作者：** Yuqi Xue, Jichuan Chang, Jian Huang

**来源：** MICRO 2026，pp. 502–521；[DOI](https://doi.org/10.1109/MICRO67795.2026.00049)

## 英文摘要

To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs). These NPU chips have been developed and evolved at an incredibly fast pace. This inevitably produces heterogeneous compute pools backed by different versions of NPU chips. Unfortunately, due to the lack of system and architecture support for managing NPU heterogeneity in the cloud, it is unclear how to best utilize heterogeneous NPUs to maximize the energy and cost efficiency for LLM services. In this paper, we first conduct a characterization study of various generations of NPU chips, using Google TPU chips as an example, to demonstrate the potential benefits in energy and cost efficiency and performance by utilizing heterogeneous NPU chips. To realize these benefits, we present NeuScale, an auto-scaling framework to automatically exploit heterogeneous NPUs for cloud platforms. NeuScale manages heterogeneous NPU resources with a new vPod abstraction, which abstracts the core hardware parameters of different NPU versions and provides compatibility with existing ML frameworks. It makes the best-fit vPod allocations for different LLM inference requests using an intuitive and lightweight roofline-based analysis. It supports fine-grained dynamic NPU resource provisioning by adjusting both the vPod configuration (i.e., scaling up/down) and the number of vPods (e.g., scaling in/out). To validate the benefits of NeuScale at scale, we implement it with a production-level NPU simulator, as well as a real-system prototype based on different generations of Google TPUs. Our evaluation with popular LLMs shows that NeuScale can significantly improve energy/cost efficiency and service-level objective (SLO) satisfaction rate of LLM services by best utilizing heterogeneous NPU resources.

## 中文摘要

为了满足大语言模型（LLM）服务不断增长的计算需求，现代云平台广泛部署了神经处理单元（NPU）。这些 NPU 芯片的开发和发展速度非常快。这不可避免地会产生由不同版本的 NPU 芯片支持的异构计算池。不幸的是，由于缺乏管理云中 NPU 异构性的系统和架构支持，目前尚不清楚如何最好地利用异构 NPU 来最大限度地提高 LLM 服务的能源和成本效率。在本文中，我们首先对各代NPU芯片进行表征研究，以谷歌TPU芯片为例，展示利用异构NPU芯片在能源、成本效率和性能方面的潜在优势。为了实现这些优势，我们推出了 NeuScale，这是一个自动扩展框架，可以自动利用云平台的异构 NPU。 NeuScale 通过新的 vPod 抽象来管理异构 NPU 资源，该抽象抽象了不同 NPU 版本的核心硬件参数，并提供了与现有 ML 框架的兼容性。它使用直观且轻量级的基于屋顶线的分析，为不同的 LLM 推理请求做出最适合的 vPod 分配。它通过调整 vPod 配置（即扩大/缩小）和 vPod 数量（例如扩大/缩小）来支持细粒度的动态 NPU 资源配置。为了大规模验证 NeuScale 的优势，我们使用生产级 NPU 模拟器以及基于不同代 Google TPU 的真实系统原型来实现它。我们对热门 LLM 的评估表明，NeuScale 通过充分利用异构 NPU 资源，可以显着提高 LLM 服务的能源/成本效率和服务水平目标 (SLO) 满意度。

## 中文关键词

神经处理单元；NPU 复用；异构计算；自动扩缩容；大语言模型服务；可持续计算

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/platformxlab/NeuSim/tree/micro26ae](https://github.com/platformxlab/NeuSim/tree/micro26ae)（论文提供的地址；2026-11-10 检查返回 HTTP 404）
- 代码与复现实验仓库：[https://github.com/XZman/micro26ae_supplementary_files](https://github.com/XZman/micro26ae_supplementary_files)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21544640](https://doi.org/10.5281/zenodo.21544640)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2A](index.md) · [MICRO 2026 主页](../index.md)
