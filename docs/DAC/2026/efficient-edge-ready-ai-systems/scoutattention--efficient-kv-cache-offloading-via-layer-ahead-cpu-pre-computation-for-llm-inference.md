Scoutattention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-Computation for LLM Inference
Authors：
[Qiuyang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=323622579239509103)，[Kai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=4695159716933253617)，[Ding Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=06514997359713377851)，[Kai Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9800745582297990579)，[Cheng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=4250260991261251568)，[Zhenyu Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9835823764360201929)，[Peng Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2279293438083666032)，[Jiguang Wan](https://63dac.conference-program.com/?post_type=page&p=15&uid=16715718215064414571)

## 中文标题

ScoutAttention：面向 LLM 推理的通过层提前 CPU 预计算实现的高效 KV Cache 卸载

## 英文摘要

Large language models encounter critical GPU memory capacity constraints during long-context inference, where KV cache memory consumption severely limits decode batch sizes. While existing research has explored offloading KV cache to DRAM, these approaches either demand frequent GPU-CPU data transfers or impose extensive CPU computation requirements, resulting in poor GPU utilization as the system waits for I/O operations or CPU processing to complete. We propose ScoutAttention, a novel KV cache offloading framework that accelerates LLM inference through collaborative GPU-CPU attention computation. To prevent CPU computation from bottlenecking the system, ScoutAttention introduces GPU-CPU collaborative block-wise sparse attention that significantly reduces CPU load. Unlike conventional parallel computing approaches, our framework features a novel layer-ahead CPU pre-computation algorithm, enabling the CPU to initiate attention computation one layer in advance, complemented by asynchronous periodic recall mechanisms to maintain minimal CPU compute load. Experimental results demonstrate that ScoutAttention maintains accuracy within 2.4% of baseline while achieving 2.1x speedup compared to existing offloading methods.

## 中文摘要

大语言模型在长上下文推理过程中面临严峻的 GPU 显存容量限制，其中 KV cache 的内存消耗严重制约了解码批大小。尽管已有研究探索将 KV cache 卸载至 DRAM，但这些方法要么需要频繁的 GPU-CPU 数据传输，要么带来大量 CPU 计算需求，导致系统在等待 I/O 操作或 CPU 处理完成时 GPU 利用率低下。我们提出 ScoutAttention，一种新颖的 KV cache 卸载框架，通过 GPU-CPU 协同注意力计算加速 LLM 推理。为防止 CPU 计算成为系统瓶颈，ScoutAttention 引入 GPU-CPU 协同的块稀疏注意力，显著降低 CPU 负载。与传统并行计算方法不同，我们的框架采用新颖的层提前 CPU 预计算算法，使 CPU 能够提前一层启动注意力计算，并辅以异步周期性召回机制以维持极低的 CPU 计算负载。实验结果表明，ScoutAttention 在精度保持在基线 2.4% 以内的同时，相比现有卸载方法实现 2.1 倍加速。
