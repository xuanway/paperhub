---
title: "Fast On-device LLM Inference with NPUs"
description: "ASPLOS 2025 · Session 5C · 基于 NPU 的端侧 LLM 快速推理"
tags:
  - "ASPLOS2025"
  - "Session 5C"
  - "Large Language Models"
---

# Fast On-device LLM Inference with NPUs

**中文标题：** 基于 NPU 的端侧 LLM 快速推理

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Daliang Xu (Key Lab of HCST (PKU), MOE; SCS, Peking University), Hao Zhang (Beijing University of Posts and Telecommunications), Liming Yang (Key Lab of HCST (PKU), MOE; SCS, Peking University), Ruiqi Liu (Key Lab of HCST (PKU), MOE; SCS, Peking University), Gang Huang (Key Lab of HCST (PKU), MOE; SCS, Peking University,National Key Laboratory of Data Space Technology and System), Mengwei Xu (Beijing University of Posts and Telecommunications), Xuanzhe Liu (Key Lab of HCST (PKU), MOE; SCS, Peking University)

**单位：** PKU；Beijing University of Posts and Telecommunications

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707239) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

On-device inference for Large Language Models (LLMs), driven by increasing privacy concerns and advancements of mobile-sized models, has gained significant interest. However, even mobile-sized LLMs (e.g., Gemma-2B) encounter unacceptably high inference latency, often bottlenecked by the prefill stage in tasks like screen UI understanding. We present llm.npu, the first LLM inference system utilizing on-device Neural Processing Unit (NPU) offloading to reduce prefill latency. llm.npu enhances NPU offloading efficiency by re-constructing the prompt and model in three levels: (1) At prompt level, it divides variable-length prompts into multiple fixed-sized chunks while maintaining data dependencies; (2) At tensor level, it identifies and extracts significant outliers to run on the CPU/GPU in parallel with minimal overhead; (3) At block level, it schedules Transformer blocks in an out-of-order manner to the CPU/GPU and NPU based on their hardware affinity and sensitivity to accuracy. Compared to competitive baselines, llm.npu achieves 22.4× faster prefill speed and 30.7× energy savings on average, and up to 32.8× speedup in an end-to-end realworld application. For the first time, llm.npu achieves more than 1,000 tokens/sec prefilling for a billion-sized model.

## 中文摘要

在隐私担忧日益加剧与移动端规模模型不断进步的推动下，面向大语言模型（LLM）的端侧推理已受到广泛关注。然而，即使是移动端规模的 LLM（如 Gemma-2B）也会遇到难以接受的高推理时延，其瓶颈常常是屏幕 UI 理解等任务中的 prefill 阶段。我们提出 llm.npu，这是首个利用端侧神经网络处理器（NPU）卸载来降低 prefill 时延的 LLM 推理系统。llm.npu 通过在三个层次上重构提示词与模型来提升 NPU 卸载效率：（1）在提示词层面，它将变长提示词划分为多个固定大小的块，同时保持数据依赖关系；（2）在张量层面，它识别并提取显著的离群值，以极小开销在 CPU/GPU 上并行执行；（3）在块层面，它依据硬件亲和性与对精度的敏感度，以乱序方式将 Transformer 块调度到 CPU/GPU 与 NPU。与有竞争力的基线相比，llm.npu 平均实现 22.4× 的 prefill 加速和 30.7× 的能耗节省，在端到端真实应用中最高可达 32.8× 加速。llm.npu 首次使十亿参数规模的模型实现超过 1,000 tokens/sec 的 prefill。

## 英文关键词

Mobile computing, large language model, NPU

## 中文关键词

移动计算；大语言模型；NPU

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707239)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2025](../index.md)
