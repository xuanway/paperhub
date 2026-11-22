---
title: "Elastic LLM Serving on FPGAs via Partial Reconfiguration: A Case Study Using the FPGA AI Suite"
description: "MICRO 2026 · Session 9A · 通过部分重配置实现 FPGA 上的弹性 LLM 服务：基于 FPGA AI Suite 的案例研究"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "FPGA"
  - "Reconfigurable Computing"
---

# Elastic LLM Serving on FPGAs via Partial Reconfiguration: A Case Study Using the FPGA AI Suite

**中文标题：** 通过部分重配置实现 FPGA 上的弹性 LLM 服务：基于 FPGA AI Suite 的案例研究

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Nachuan Wang, Mike Montano, Hyungyo Kim, Ren Wang, Phillip Swart, Nam Sung Kim

**来源：** MICRO 2026，pp. 3179–3194；[DOI](https://doi.org/10.1109/MICRO67795.2026.00214)

## 英文摘要

GPUs currently dominate large language model (LLM) serving. However, their practical efficiency is increasingly constrained by the prolonged auto-regressive decoding, high cost of storing model weights and key-value caches in device memory, and bursty query loads. These factors lead to substantial over-provisioning in data centers, inflating both operational costs and wasted energy. While modern HBM-equipped FPGAs offer a highly efficient alternative, prior research has only explored its use on small models with static evaluation settings. This narrow focus obscures the true viability of FPGAs in production environments, and leaves their competitiveness against state-of-the-art GPU-based serving systems unproven. This paper bridges the gap by building and evaluating an elastic FPGA-based LLM serving system. We adopt a commercial FPGA AI IP as a representative case study to demonstrate broad architectural applicability, integrate it as a PyTorch backend, and optimize the serving stack with advanced techniques such as prefill-decode disaggregation and continuous batching. Additionally, we introduce the first application of Partial Reconfiguration (PR) to LLM workloads. PR dynamically adapts the accelerator architecture at runtime and shifts compute-to-memory balance in response to workload fluctuations, achieving either up to 1.6× tail latency reduction under bursty query loads, or up to 1.16× power savings in low-QPS regimes. Compared to NVIDIA A100/H100 GPUs running a vLLM serving engine, our system achieves up to 6.2×/13.8× lower cost-per-query and 4.1×/3.7× lower energy-per-query on conversational workloads. On reasoning workloads, it achieves up to 1.4× lower cost- and energy-per-query than A100, and up to 3.4× lower cost-per-query than H100 under relaxed SLOs. These results establish FPGAs as a competitive, elastic platform for modern LLM serving.

## 中文摘要

GPU 目前主导大语言模型（LLM）服务，但长时间的自回归解码、在设备内存中保存模型权重与键值缓存的高成本，以及突发查询负载，日益限制其实用效率。这些因素导致数据中心严重超额配置，推高运营成本并浪费能源。配备高带宽内存（HBM）的现代 FPGA 提供了高效替代方案，但已有研究主要针对静态评估条件下的小型模型。这种有限的研究范围掩盖了 FPGA 在生产环境中的真实可行性，其相对先进 GPU 服务系统的竞争力也未得到证实。本文构建并评估基于 FPGA 的弹性 LLM 服务系统，以弥补这一空白。我们选择商用 FPGA AI IP 作为代表性案例，展示架构方案的广泛适用性；将其集成为 PyTorch 后端，并采用预填充与解码解耦、连续批处理等技术优化服务软件栈。此外，本文首次将部分重配置（PR）用于 LLM 工作负载。PR 根据工作负载波动，在运行时动态调整加速器架构及计算与内存的配比，使突发查询下的尾时延最低降至原来的 1/1.6，或使低 QPS 场景的功耗最低降至原来的 1/1.16。对于对话工作负载，相比运行 vLLM 的 NVIDIA A100/H100 系统，每次查询成本最低分别降至基线的 1/6.2、1/13.8，每次查询能耗最低分别降至 1/4.1、1/3.7。对于推理工作负载，相比 A100，每次查询成本与能耗最低均降至 1/1.4；在较宽松的服务级别目标（SLO）下，相比 H100，每次查询成本最低降至 1/3.4。这些结果表明，FPGA 是现代 LLM 服务中具有竞争力的弹性平台。

## 中文关键词

大语言模型服务；现场可编程门阵列；部分重配置；弹性扩缩容

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/ece-fast-lab/MICRO-2026-AI-Suite](https://github.com/ece-fast-lab/MICRO-2026-AI-Suite)
- 研究制品归档：[https://zenodo.org/records/21541347](https://zenodo.org/records/21541347)

以上入口来自论文正文或 Artifact 附录。

## 来源核对说明

元数据丢失了两组倍数之间的斜线。中文译文按 PDF 分别对应 A100/H100，还原为 6.2×/13.8× 与 4.1×/3.7×。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
