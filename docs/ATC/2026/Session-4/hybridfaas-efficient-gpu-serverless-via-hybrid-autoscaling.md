# HybridFaaS: Efficient GPU Serverless via Hybrid Autoscaling

**中文标题**：HybridFaaS：通过混合自动扩缩实现高效的 GPU 无服务器

**所属 Session**：[Session 4: Serverless and Elastic LLM Inference](index.md) · [ATC 2026](../index.md)

**作者**：Hao Ming (Huazhong University of Science and Technology), Chencheng Ye (Huazhong University of Science and Technology), XIAOFEI LIAO (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Qiang-Sheng Hua (Huazhong University of Science and Technology), Yuanchao Xu (University of California, Santa Cruz)

## 英文摘要
Serverless computing is widely adopted for its simplicity, autoscaling, and fine-grained billing. However, GPU-based serverless frameworks often inherit CPU-oriented designs, leading to inefficiencies in machine learning (ML) inference. Specifically, the keep-warm policy, effective on CPUs, is suboptimal on GPUs due to rigid hardware binding, and replica-based autoscaling incurs significant memory overhead and frequent model swaps, which are amplified by large machine learning models. To address these problems, we propose HybridFaaS, a hybrid autoscaling strategy that combines pipelined and tensor-parallel scaling to save memory with replica-based scaling for flexibility, reducing model swapping overhead without undue scheduling complexity. Evaluations demonstrate that HybridFaaS significantly outperforms state-of-the-art systems with 80-97% higher throughput and 99-147× lower P99 tail latency.

## 中文摘要
无服务器计算因其简单性、自动扩缩与细粒度计费而被广泛采用。然而，基于 GPU 的无服务器框架往往沿用面向 CPU 的设计，导致机器学习（ML）推理中的低效。具体而言，在 CPU 上有效的保温（keep-warm）策略在 GPU 上因僵化的硬件绑定而并非最优，而基于副本的自动扩缩会带来显著的内存开销和频繁的模型换入换出，这些问题会随机器学习模型规模增大而被放大。为解决这些问题，我们提出 HybridFaaS，一种混合自动扩缩策略，它把流水线并行与张量并行的扩缩结合起来以节省内存，并配合基于副本的扩缩以保持灵活性，从而在不引入过度调度复杂度的前提下降低模型换出开销。评估表明，HybridFaaS 显著优于最先进的系统，吞吐高出 80-97%，P99 尾延迟低 99-147×。

## 英文关键词
Serverless computing, GPU inference, Resource scheduling

## 中文关键词
无服务器计算，GPU 推理，资源调度

[返回 Session 4](index.md) · [返回 ATC 2026](../index.md)
