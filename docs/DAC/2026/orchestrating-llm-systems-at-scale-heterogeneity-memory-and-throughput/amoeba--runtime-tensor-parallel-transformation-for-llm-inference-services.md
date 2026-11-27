Amoeba: Runtime Tensor Parallel Transformation for LLM Inference Services
Authors：
[Haoyu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=9597109705123144414)，[Xue Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=668740429977333188)，[Kun Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=6513626928583874682)，[Yu Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=62581782206070830671)，[Jin Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0415856527684325863)，[Xin Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4855582457088905776)

## 中文标题

Amoeba：面向 LLM 推理服务的运行时张量并行变换

## 英文摘要

In Large Language Model (LLM) inference services, it is challenging to make a parallelism strategy configuration, to efficiently process the requests of variance context lengths. Requests of long context require high degree of parallelism to provide more memory for Key-Value (KV) Cache, while requests of short context prefer low degree of parallelism to increase concurrency, thus improving throughput. To maintain high throughput while supporting large context lengths on demand, we propose Amoeba, a runtime Tensor Parallel (TP) transformation for online LLM inference services, which adaptively adjusts the TP of running instances to align with the dynamics of incoming requests. Evaluations using real-world traces show that Amoeba improves throughput by 1.75×-6.57× compared to state-of-the-art solutions.

## 中文摘要

在大语言模型（LLM）推理服务中，如何配置并行策略以高效处理上下文长度各异的请求极具挑战。长上下文请求需要较高的并行度，以提供更多键值（KV）缓存空间；而短上下文请求则偏好较低的并行度，以提升并发数、进而提高吞吐。为在按需支持长上下文的同时保持高吞吐，我们提出 Amoeba，一种面向在线 LLM 推理服务的运行时张量并行（TP）变换方法，可自适应地调整运行实例的 TP，以匹配到达请求的动态变化。基于真实负载轨迹的评估表明，与最先进方案相比，Amoeba 将吞吐提升 1.75 倍至 6.57 倍。
