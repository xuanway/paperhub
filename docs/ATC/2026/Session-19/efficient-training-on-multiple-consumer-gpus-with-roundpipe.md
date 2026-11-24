# Efficient Training on Multiple Consumer GPUs with RoundPipe

**中文标题**：用 RoundPipe 在多个消费级 GPU 上高效训练

**所属 Session**：[Session 19: Model Training](index.md) · [ATC 2026](../index.md)

**作者**：Yibin Luo (Tsinghua University), Shiwei Gao (Tsinghua University), Huichuan Zheng (Tsinghua University), Youyou Lu (Tsinghua University), Jiwu Shu (Tsinghua University)

## 英文摘要
Fine-tuning Large Language Models (LLMs) on consumer-grade GPUs is highly cost-effective, yet constrained by limited GPU memory and slow PCIe interconnects. Pipeline parallelism combined with CPU offloading mitigates these hardware bottlenecks by reducing communication overhead. However, existing PP schedules suffer from an inherent limitation termed the weight binding issue. Binding uneven model stages (e.g., the LM head is large) to GPUs limits the pipeline’s throughput to that of the GPU with the heaviest load, leading to severe pipeline bubbles. In this paper, we propose RoundPipe, a novel pipeline schedule that breaks the weight binding constraint on consumer GPU servers. RoundPipe treats GPUs as a pool of stateless execution workers and dynamically dispatches computation stages across devices in a round-robin manner, achieving a near-zero-bubble pipeline. To ensure training correctness and system efficiency, RoundPipe integrates a priority-aware transfer scheduling engine, a Layerwise Model Consistency Protocol, and an automated layer partitioning algorithm. Evaluations on an 8× RTX 4090 server demonstrate that RoundPipe achieves 1.48–2.16× speedups over state-of-the-art baselines when fine-tuning 1.7B to 32B models. Remarkably, RoundPipe enables LoRA fine-tuning of the Qwen3-235B model with 31K sequence length on a single server. RoundPipe has been open-sourced as a Python library. Project Page: https://thustorage.github.io/RoundPipe/

## 中文摘要
在消费级 GPU 上微调大语言模型（LLM）极具成本效益，但受限于有限的 GPU 内存和缓慢的 PCIe 互连。流水线并行结合 CPU offloading 通过降低通信开销来缓解这些硬件瓶颈。然而，现有 PP 调度存在一个被称为权重绑定问题的固有局限。将不均衡的模型阶段（例如很大的 LM head）绑定到 GPU 上，会使流水线的吞吐受限于负载最重的那块 GPU，导致严重的流水线气泡。本文提出 RoundPipe，一种在消费级 GPU 服务器上打破权重绑定约束的新型流水线调度。RoundPipe 将 GPU 视为一组无状态执行工作者的资源池，以轮转方式在各设备间动态派发计算阶段，从而实现近乎零气泡的流水线。为确保训练正确性与系统效率，RoundPipe 集成了优先级感知的传输调度引擎、逐层模型一致性协议和自动化层划分算法。在 8× RTX 4090 服务器上的评估表明，在微调 1.7B 至 32B 模型时，RoundPipe 相对最先进基线取得 1.48–2.16× 的加速。尤为突出的是，RoundPipe 使 Qwen3-235B 模型能在单台服务器上以 31K 序列长度进行 LoRA 微调。RoundPipe 已作为 Python 库开源。项目主页：https://thustorage.github.io/RoundPipe/

## 英文关键词
LLM training, Pipeline parallel, CPU offloading

## 中文关键词
LLM 训练，流水线并行，CPU offloading

[返回 Session 19](index.md) · [返回 ATC 2026](../index.md)
