CANNON: A CXL-Based Near-Memory Processing Architecture for Approximate Nearest Neighbor Search on Real Hardware
Authors：
[Ganghyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=35646537126922010871)，[Hyeonjun An](https://63dac.conference-program.com/?post_type=page&p=15&uid=49606032637135471301)，[Hyunjoon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=2017454530327266475)，[Rathijit Sen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7258567636304781353)，[Kangkyu Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=3163063524196898172)，[Jinho Baek](https://63dac.conference-program.com/?post_type=page&p=15&uid=6632523455966998204)，[Kwangsik Shin](https://63dac.conference-program.com/?post_type=page&p=15&uid=80295674739184188511)，[Youngpyo Joo](https://63dac.conference-program.com/?post_type=page&p=15&uid=75901890897403339361)，[Kwanghyun Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5064180234446837532)

## 中文标题

CANNON：一种在真实硬件上基于 CXL 的近似最近邻搜索近存处理架构

## 英文摘要

Approximate Nearest Neighbor (ANN) search is a foundational primitive for AI applications such as Retrieval-Augmented Generation (RAG). CPU and GPU-based solutions face scalability bottlenecks due to limited local memory, while a multi-tier architecture using SSDs introduces high latency from coarse-grained I/O, mismatched with fine-grained data access patterns inherent to ANN search. We present CANNON (A CXL-Based Near-Memory Processing Architecture for Approximate Nearest Neighbor Search on Real Hardware), a fully offloaded Near-Memory Processing (NMP) architecture implemented on real CXL hardware. CANNON transforms the ANN search pipeline into a fine-grained, deeply pipelined dataflow architecture to maximize throughput, and introduces asynchronous hashing, a speculative execution mechanism that hides hash-check latency to prevent pipeline stalls. Evaluated on large-scale vector datasets, CANNON achieves up to two orders of magnitude performance improvement over state-of-the-art CPU and GPU baselines.

## 中文摘要

近似最近邻（ANN）搜索是检索增强生成（RAG）等 AI 应用的基础原语。基于 CPU 与 GPU 的方案因本地内存有限而遭遇可扩展性瓶颈，而采用 SSD 的多级架构又因粗粒度 I/O 带来高延迟，与 ANN 搜索固有的细粒度数据访问模式不匹配。我们提出 CANNON，一种在真实 CXL 硬件上实现的完全卸载式近存处理（NMP）架构。CANNON 将 ANN 搜索流水线转化为细粒度、深度流水的数据流架构以最大化吞吐，并引入异步哈希——一种推测执行机制，用于隐藏哈希检查延迟、避免流水线停顿。在大规模向量数据集上的评估表明，CANNON 相较最先进的 CPU 与 GPU 基线性能提升最高达两个数量级。

## 英文关键词

Near-Memory Processing, Approximate Nearest Neighbor Search, CXL

## 中文关键词

近存处理、近似最近邻搜索、CXL
