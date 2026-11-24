# InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models

**中文标题**：InfiniLoRA：面向大语言模型的解耦式多 LoRA 服务

**所属 Session**：[Session 10: LLM Inference II](index.md) · [ATC 2026](../index.md)

**作者**：Hongyu Chen (Shanghai Jiao Tong University), Letian Ruan (Shanghai Jiao Tong University), Zilin Xu (Bytedance), Yuchen Li (Singapore Management Univerisity), Xinyu Chen (The Hong Kong University of Science and Technology (Guangzhou)), Bingsheng He (National University of Singapore), Jingwen Leng (Shanghai Jiao Tong University), Jieru Zhao (Shanghai Jiao Tong University), Shixuan Sun (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

## 英文摘要
LoRA enables efficient customization of LLMs and is widely used in multi-tenant and multi-task serving. However, emerging model architectures such as MoE significantly increase LoRA memory cost, making existing coupled LoRA serving designs poorly scalable and prone to tail-latency inflation. We present InfiniLoRA, a disaggregated LoRA serving system that decouples LoRA execution from base-model inference. InfiniLoRA introduces a shared LoRA Server with parallelism-aware execution, SLO-driven provisioning, and critical-path optimizations, including GPU-initiated communication and hardware-specialized LoRA kernels. Experiments show that InfiniLoRA can achieve an average 3.05× increase in serviceable request rate under strict latency SLOs, and improve the percentage of LoRA adapters satisfying the SLO requirement by 54.0%.

## 中文摘要
LoRA 使 LLM 的高效定制成为可能，并被广泛用于多租户和多任务服务。然而，诸如 MoE 之类的新兴模型架构显著增加了 LoRA 的内存开销，使现有的耦合式 LoRA 服务设计可扩展性差且易出现尾延迟膨胀。我们提出 InfiniLoRA，一个解耦式 LoRA 服务系统，它将 LoRA 执行与基础模型推理解耦。InfiniLoRA 引入一个共享的 LoRA 服务器，具备并行度感知的执行、SLO 驱动的资源供给以及关键路径优化，包括 GPU 发起的通信和硬件专用的 LoRA 内核。实验表明，InfiniLoRA 在严格的延迟 SLO 下可将可服务请求速率平均提升 3.05×，并将满足 SLO 要求的 LoRA 适配器比例提升 54.0%。

## 英文关键词
Large language model, Low-rank adaptation, Multi-LoRA serving, Disaggregated inference

## 中文关键词
大语言模型，低秩适配，多 LoRA 服务，解耦推理

[返回 Session 10](index.md) · [返回 ATC 2026](../index.md)
