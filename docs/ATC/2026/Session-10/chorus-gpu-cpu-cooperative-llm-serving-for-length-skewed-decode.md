# Chorus: GPU–CPU Cooperative LLM Serving for Length-Skewed Decode

**中文标题**：Chorus：面向长度偏斜解码的 GPU–CPU 协同 LLM 服务

**所属 Session**：[Session 10: LLM Inference II](index.md) · [ATC 2026](../index.md)

**作者**：Dong Chen (Hong Kong University of Science and Technology), Yukun Zhou (Hong Kong University of Science and Technology), Sheng Yao (Hong Kong University of Science and Technology), Ruichuan Chen (Nokia Bell Labs), Binhang Yuan (Hong Kong University of Science and Technology), Shuai Wang (Hong Kong University of Science and Technology), Luping Wang (Alibaba Group), Cheng Huang (Alibaba Group), Guodong Yang (Alibaba Group), Liping Zhang (Alibaba Group), Wei Wang (Hong Kong University of Science and Technology)

## 英文摘要
Online LLM serving is increasingly constrained by GPU memory capacity during decode. In length-skewed workloads, a small fraction of long requests keeps large key-value (KV) caches resident across many decode steps, exhausting GPU high-bandwidth memory (HBM), throttling admission, and reducing goodput for the short-request majority. At the same time, GPU servers provision substantial CPU and DRAM resources, and recent Intel CPUs add Advanced Matrix Extensions (AMX) for matrix-heavy kernels. The challenge is to use these host resources without placing CPU work on the per-token GPU critical path. We present Chorus, a GPU–CPU cooperative serving system that uses AMX-equipped CPUs as a second decode lane for long requests with persistent KV state. Chorus keeps prefill and short-request decode on GPUs, offloads selected long-request decode once to distributed AMX CPU groups, and releases the corresponding GPU KV pages so the GPU lane can admit more short requests. To satisfy online service level objectives (SLOs), Chorus combines pressure-aware offload admission, tensor-parallel AMX decode that aggregates CPU compute and memory bandwidth, and AMX kernels specialized for small, mixed-length decode batches. Across popular LLMs and production-derived workloads, Chorus achieves the highest SLO-attaining goodput among baselines, improving peak goodput over SGLang by up to 1.26×. At the same offered load, Chorus delivers 1.3–11.4× SGLang’s goodput when GPU-only serving enters time-to-first-token (TTFT) collapse, and improves over CPU-offload baselines by up to 4.3×.

## 中文摘要
在线 LLM 服务在解码阶段日益受到 GPU 内存容量的制约。在长度偏斜的工作负载中，一小部分长请求会在许多解码步中常驻大容量的键值（KV）缓存，耗尽 GPU 高带宽内存（HBM），抑制请求准入，并降低占多数的短请求的有效吞吐（goodput）。与此同时，GPU 服务器配置了大量的 CPU 和 DRAM 资源，且近期的 Intel CPU 增加了面向矩阵密集型内核的高级矩阵扩展（AMX）。挑战在于使用这些主机资源的同时，不把 CPU 工作放到逐 token 的 GPU 关键路径上。我们提出 Chorus，一个 GPU–CPU 协同的服务系统，它把配备 AMX 的 CPU 作为第二条解码通道，用于具有持久 KV 状态的长请求。Chorus 将预填充和短请求解码保留在 GPU 上，将选定的长请求解码一次性卸载到分布式 AMX CPU 组，并释放相应的 GPU KV 页，使 GPU 通道能够准入更多短请求。为满足在线服务等级目标（SLO），Chorus 结合了压力感知的卸载准入、聚合 CPU 算力与内存带宽的张量并行 AMX 解码，以及专为小型、混合长度解码批次定制的 AMX 内核。在流行的 LLM 和生产环境衍生的负载上，Chorus 在基线中取得最高的满足 SLO 的有效吞吐，相比 SGLang 将峰值有效吞吐提升最多 1.26×。在相同的提供负载下，当纯 GPU 服务出现首 token 时间（TTFT）崩溃时，Chorus 的有效吞吐是 SGLang 的 1.3–11.4×，并相比 CPU 卸载基线提升最多 4.3×。

## 英文关键词
large language model serving, heterogeneous CPU–GPU systems, long-context inference, Intel AMX

## 中文关键词
大语言模型服务，异构 CPU–GPU 系统，长上下文推理，Intel AMX

[返回 Session 10](index.md) · [返回 ATC 2026](../index.md)
