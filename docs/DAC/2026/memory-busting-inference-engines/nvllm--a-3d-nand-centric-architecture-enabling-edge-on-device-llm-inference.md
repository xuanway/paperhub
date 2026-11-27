NVLLM: A 3D NAND-Centric Architecture Enabling Edge on-Device LLM Inference
Authors：
[Mingbo Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=28594594385516440661)，[Changwei Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=02105077707358807011)，[Haoyu Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=3184814767295146712)，[Zhihao Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=7174973163501595746)，[Yizhi Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=38926487645150471441)，[Zhangrui Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=5366601994910713382)，[Weiwei Shan](https://63dac.conference-program.com/?post_type=page&p=15&uid=50810107585664459381)

## 中文标题

NVLLM：面向边缘端侧 LLM 推理的 3D NAND 中心架构

## 英文摘要

The rapid growth of LLMs demands high-throughput, memory-capacity-intensive inference on resource-constrained edge devices, where single-batch decoding remains fundamentally memory-bound. Existing out-of-core GPU-based and SSD-like accelerators are limited by DRAM-bound weight movement and inefficient storage access granularity. We present NVLLM, a 3D NAND-centric inference architecture that offloads feed-forward network (FFN) computation into the Flash while executing attention on lightweight CMOS logic with external DRAM. Through wafer-to-wafer stacking, NVLLM tightly integrates multi-plane 3D NAND with compute pipelines, error correction code (ECC) units, and buffers, enabling page-level FFN weight access without DRAM traversal. All GEMM/GEMV operations are decomposed into dot-product primitives executed by out-of-order PE lanes, operating directly on raw NAND reads with integrated ECC. Attention weights remain in DRAM, and a KVcache-aware scheduler sustains throughput as the context length grows. Evaluated on OPT and LLaMA models with up to 30B parameters, NVLLM achieves a 16.7×–37.9× speedup over A800-based out-of-core inference and up to 4.7× speedup over SSD-like designs, with only 2.7% CMOS area overhead.

## 中文摘要

大语言模型（LLM）的快速增长要求在资源受限的边缘设备上实现高吞吐、存储容量密集的推理，而单批次解码本质上仍受存储带宽约束。现有的核外 GPU 方案与类 SSD 加速器受制于 DRAM 相关的权值搬运以及低效的存储访问粒度。我们提出 NVLLM，一种以 3D NAND 为中心的推理架构，将前馈网络（FFN）计算卸载至 Flash 内部，同时在轻量 CMOS 逻辑上配合外部 DRAM 执行注意力计算。通过晶圆对晶圆键合，NVLLM 将多平面 3D NAND 与计算流水线、纠错码（ECC）单元及缓冲器紧密集成，实现页级 FFN 权值访问而无需途经 DRAM。所有 GEMM/GEMV 运算均被分解为由乱序 PE 通道执行的点积原语，直接作用于经集成 ECC 处理的原始 NAND 读取数据。注意力权重保留在 DRAM 中，KV cache 感知的调度器则随上下文长度增长维持吞吐。在参数量最高达 30B 的 OPT 与 LLaMA 模型上评估，NVLLM 相较基于 A800 的核外推理实现 16.7 倍至 37.9 倍的加速，相较类 SSD 设计最高实现 4.7 倍加速，而 CMOS 面积开销仅为 2.7%。

## 英文关键词

3D NAND Flash, In-Storage Computing, Near-Data Processing, Large Language Models, On-Device AI, Error-Resilient Computing

## 中文关键词

3D NAND 闪存、存内计算、近数据处理、大语言模型、端侧 AI、容错计算
