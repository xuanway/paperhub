LOHA: A Latency-Optimized CPU-Storage Hybrid Architecture for Billion-Scale Graph-Based Vector Similarity Search
Authors：
[Seongjoon Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=897341601060338628)，[Junyoung Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=8940500590996894043)，[Donghyun Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26442992668644323331)，[Moohyeon Nam](https://63dac.conference-program.com/?post_type=page&p=15&uid=38992152386416966011)，[Hongchan Roh](https://63dac.conference-program.com/?post_type=page&p=15&uid=7735077436681314066)，[Se-Hyun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=19736077272126647401)，[Moo-Kyoung Chung](https://63dac.conference-program.com/?post_type=page&p=15&uid=23962065558396258211)，[Seungkyu Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=8769941943526644152)

## 中文标题

LOHA：一种面向十亿规模图向量相似性搜索的延迟优化 CPU–存储混合架构

## 英文摘要

Graph-based Approximate Nearest Neighbor Search (GANNS) has been widely adopted for vector retrieval owing to its high scalability and low latency. However, existing GANNS frameworks face severe latency bottlenecks on billion-scale datasets due to excessive SSD I/O. This work presents LOHA, a latency-optimized CPU–storage hybrid architecture for product quantization (PQ)- based billion-scale ANNS. LOHA decouples graph traversal and re-ranking workloads, executing the former on the CPU while offloading the latter to an in-storage accelerator that exploits SSD-level parallelism. Furthermore, a speculative re-ranking mechanism pipelines both stages to minimize idle time and reduce end-to-end latency. Experiments show that LOHA achieves throughput improvements of up to 9.6×, 6.2×, and 4.0× over CPU-, GPU-, and in-storage architectures, respectively.

## 中文摘要

基于图的近似最近邻搜索（GANNS）凭借高可扩展性与低延迟，已被广泛用于向量检索。然而，现有 GANNS 框架在十亿规模数据集上因过度的 SSD I/O 而面临严重延迟瓶颈。本文提出 LOHA，一种面向基于乘积量化（PQ）的十亿规模 ANNS 的延迟优化 CPU–存储混合架构。LOHA 将图遍历与重排序两类负载解耦：前者在 CPU 上执行，后者则卸载至利用 SSD 级并行性的存内加速器。此外，一种推测式重排序机制将两个阶段流水化，以最小化空闲时间并降低端到端延迟。实验表明，LOHA 相较 CPU、GPU 与存内架构分别实现最高 9.6 倍、6.2 倍与 4.0 倍的吞吐提升。
