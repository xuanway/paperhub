MoE-Balance: Unleashing the Full Potential of CPU-GPU Heterogeneity for Efficient MoE Inference
Authors：
[Tiantian Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=25857721185657223531)，[Xiaohang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=911243)，[Yingtao Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=510443)，[Amit Kumar Singh](https://63dac.conference-program.com/?post_type=page&p=15&uid=104143)，[Kui Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=130443)

## 中文标题

MoE-Balance：释放 CPU-GPU 异构算力的全部潜力以实现高效 MoE 推理

## 英文摘要

Sparse Mixture-of-Experts (MoE) models offer a powerful way to increase the capacity of large language models without proportionally increasing computation. Yet, their extremely large expert weight parameters create severe memory challenges for consumer-grade GPUs and edge devices. Existing offloading and hybrid CPU–GPU approaches fall short in fully utilizing CPU resources, and their coarse-grained scheduling and poorly overlapped CPU-GPU data transfers leave CPU cores frequently idle, thus causing pipeline bubbles and exacerbating overall system inefficiency. We present MoE-Balance, a system that efficiently utilizes heterogeneous CPU-GPU resources for MoE inference. The key innovations include a fine-grained dynamic scheduler that distributes expert tasks based on real-time load, and a cross-layer prefetching and chunked transfer mechanism that overlaps computation with weight movement via PCIe. Experiments on Mixtral-8×7B show that MoE-Balance achieves 1.6× higher throughput and 37.5% lower end-to-end latency compared with state-of-the-art hybrid baselines, demonstrating strong performance gains under memory-constrained settings.

## 中文摘要

稀疏混合专家（MoE）模型提供了一种强大途径，可在不同比例增加计算量的前提下提升大语言模型容量。然而，其规模极大的专家权重参数给消费级 GPU 与边缘设备带来了严峻的内存挑战。现有卸载与 CPU-GPU 混合方案未能充分利用 CPU 资源，其粗粒度调度与重叠不佳的 CPU-GPU 数据传输使 CPU 核心频繁空闲，从而产生流水线气泡并加剧系统整体低效。我们提出 MoE-Balance，一个高效利用 CPU-GPU 异构资源进行 MoE 推理的系统。其关键创新包括：依据实时负载分配专家任务的细粒度动态调度器，以及通过 PCIe 将计算与权重搬移相重叠的跨层预取与分块传输机制。在 Mixtral-8×7B 上的实验表明，与最先进的混合基线相比，MoE-Balance 吞吐提升 1.6 倍、端到端时延降低 37.5%，在内存受限场景下展现出显著的性能增益。

## 英文关键词

MoE inference, Weight offloading, CPU-GPU hybrid execution

## 中文关键词

MoE 推理、权重卸载、CPU-GPU 混合执行
