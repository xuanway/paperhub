# GPipeANN: Taming Throughput-Latency Tradeoff in GPU-SSD ANNS

**中文标题**：GPipeANN：驾驭 GPU-SSD ANNS 中的吞吐-延迟权衡

**所属 Session**：[Session 11: Search, Recommender and Graph Systems](index.md) · [ATC 2026](../index.md)

**作者**：Puqing Wu (Nanjing University and Renmin University of China), Minhui Xie (Nanjing University), Yiheng Tong (Renmin University of China), Jie Yin (Tencent Inc.), Sen Yang (Tencent Inc.), Yunpeng Chai (Renmin University of China)

## 英文摘要
Billion-scale Approximate Nearest Neighbor Search (ANNS) increasingly adopts a GPU-SSD architecture, where GPU fetches and processes fine-grained, SSD-resident data ondemand. However, since GPUs lack native support for I/O scheduling, existing ANNS systems are trapped in a severe throughput-latency tradeoff. They either delegate scheduling to best-effort host drivers, achieving high throughput but suffering severe latency inflation due to interference, or poll I/O completion directly inside the kernel, which achieves low latency but starves GPU utilization. This paper demonstrates that this tradeoff is not fundamental. Our key insight is that ANNS exhibits strict per-hop performance predictability in both computation and I/O, which can make scheduling lightweight enough to be onloaded directly into the GPU kernel. We thus present GPipeANN, which deterministically and lightly switches among multiple query contexts at hop boundaries to achieve perfect compute-I/O overlap. Evaluations on billion-scale datasets show GPipeANN shifts the Pareto frontier, achieving high throughput and low latency simultaneously. GPipeANN is available at https://github.com/ruc-system/GPipeANN.

## 中文摘要
十亿规模的近似最近邻搜索（ANNS）日益采用 GPU-SSD 架构，由 GPU 按需取回并处理驻留在 SSD 上的细粒度数据。然而，由于 GPU 缺乏对 I/O 调度的原生支持，现有 ANNS 系统陷入严重的吞吐-延迟权衡：它们要么将调度交给尽力而为的主机驱动，虽获得高吞吐，却因相互干扰而承受严重的延迟膨胀；要么在内核中直接轮询 I/O 完成，虽获得低延迟，却使 GPU 利用率陷入饥饿。本文表明这一权衡并非本质上的必然。我们的关键洞见是：ANNS 在计算和 I/O 两方面都表现出严格的逐跳性能可预测性，这可使调度足够轻量，从而能够直接下沉（onload）到 GPU 内核中。据此我们提出 GPipeANN，它在跳边界上确定性地、轻量地在多个查询上下文之间切换，从而实现计算与 I/O 的完美重叠。在十亿规模数据集上的评测表明，GPipeANN 推移了帕累托前沿，同时实现高吞吐与低延迟。GPipeANN 已在 https://github.com/ruc-system/GPipeANN 开源。

## 英文关键词
Approximate Nearest Neighbor Search, GPU-SSD, Throughput-Latency Tradeoff

## 中文关键词
近似最近邻搜索，GPU-SSD，吞吐-延迟权衡

## 代码与研究制品

- [code](https://github.com/ruc-system/GPipeANN)

[返回 Session 11](index.md) · [返回 ATC 2026](../index.md)
