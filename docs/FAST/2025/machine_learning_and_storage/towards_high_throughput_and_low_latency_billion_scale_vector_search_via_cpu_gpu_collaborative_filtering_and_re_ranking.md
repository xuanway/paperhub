---
title: "Towards High-throughput and Low-latency Billion-scale Vector Search via CPU/GPU Collaborative Filtering and Re-ranking"
description: "FAST 2025 · Machine Learning and Storage · 单张入门级 GPU 加 SSD 做协同过滤与重排序，QPS 最高提升 13.1 倍"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
  - "approximate nearest neighbor search"
  - "SSD-based index"
---

# Towards High-throughput and Low-latency Billion-scale Vector Search via CPU/GPU Collaborative Filtering and Re-ranking

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">十亿级向量检索同时受内存成本、I/O 争用与精度约束。FusionANNS 把原始向量放 SSD、PQ 压缩向量放 GPU 显存、向量 ID 与导航图放内存，以启发式重排序与 I/O 去重压缩访存，QPS 比 SPANN 高 9.4-13.1 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Machine Learning and Storage</p>
</div>

**中文标题**：面向高吞吐、低延迟十亿级向量检索的 CPU/GPU 协同过滤与重排序

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/tian-bing](https://www.usenix.org/conference/fast25/presentation/tian-bing)

**论文 PDF**：[fast25-tian-bing.pdf](https://www.usenix.org/system/files/fast25-tian-bing.pdf)

**作者**：Bing Tian、Haikun Liu、Yuhang Tang（Huazhong University of Science and Technology）；Shihai Xiao（Huawei Technologies Co., Ltd）；Zhuohui Duan、Xiaofei Liao、Hai Jin（Huazhong University of Science and Technology）；Xuecang Zhang、Junhua Zhu（Huawei Technologies Co., Ltd）；Yu Zhang（Huazhong University of Science and Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 171–185 页

**Session**：Machine Learning and Storage · 2025-02-25 15:50–17:30 · Chair：Kan Wu（Google）

**所属 Session**：[Machine Learning and Storage](index.md) · [FAST 2025](../index.md)

**关键词**：approximate nearest neighbor search, SSD-based index, product quantization, CPU/GPU collaboration, re-ranking, I/O deduplication

---

## 英文摘要

Approximate nearest neighbor search (ANNS) has emerged as a crucial component of database and AI infrastructure. Ever-increasing vector datasets pose significant challenges in terms of performance, cost, and accuracy for ANNS services. None of modern ANNS systems can address these issues simultaneously. In this paper, we present FusionANNS, a high-throughput, low-latency, cost-efficient, and high-accuracy ANNS system for billion-scale datasets using SSDs and only one entry-level GPU. The key idea of FusionANNS lies in CPU/GPU collaborative filtering and re-ranking mechanisms, which significantly reduce I/O operations across CPUs, GPU, and SSDs to break through the I/O performance bottleneck. Specifically, we propose three novel designs: (1) multi-tiered indexing to avoid data swapping between CPUs and GPU, (2) heuristic re-ranking to eliminate unnecessary I/Os and computations while guaranteeing high accuracy, and (3) redundant-aware I/O deduplication to further improve I/O efficiency. We implement FusionANNS and compare it with the state-of-the-art SSD-based ANNS system—SPANN and GPU-accelerated in-memory ANNS system—RUMMY. Experimental results show that FusionANNS achieves 1) 9.4-13.1× higher query per second (QPS) and 5.7-8.8× higher cost efficiency compared with SPANN; 2) and 2-4.9× higher QPS and 2.3-6.8× higher cost efficiency compared with RUMMY, while guaranteeing low latency and high accuracy.

## 中文摘要

近似最近邻搜索（ANNS）已成为数据库与 AI 基础设施的关键组件。不断增长的向量数据集给 ANNS 服务的性能、成本与精度带来了重大挑战，而现代 ANNS 系统都无法同时解决这些问题。本文提出 FusionANNS——一个面向十亿级数据集、仅使用 SSD 与一张入门级 GPU 的高吞吐、低延迟、低成本且高精度的 ANNS 系统。FusionANNS 的核心思想是 CPU/GPU 协同过滤与重排序机制，它显著减少 CPU、GPU 与 SSD 之间的 I/O 操作，从而突破 I/O 性能瓶颈。具体而言，本文提出三项新设计：(1) 多级索引，避免 CPU 与 GPU 之间的数据交换；(2) 启发式重排序，在保证高精度的同时消除不必要的 I/O 与计算；(3) 冗余感知的 I/O 去重，进一步提升 I/O 效率。本文实现 FusionANNS，并与最先进的基于 SSD 的 ANNS 系统 SPANN、GPU 加速的内存 ANNS 系统 RUMMY 进行比较。实验结果表明，FusionANNS 相比 SPANN 取得 9.4–13.1 倍的 QPS 与 5.7–8.8 倍的成本效率提升；相比 RUMMY 取得 2–4.9 倍的 QPS 与 2.3–6.8 倍的成本效率提升，同时保证低延迟与高精度。

## 一句话总结

> 把索引拆成 SSD 上的原始向量、显存里的压缩向量和内存里的向量 ID 三层，让 CPU 只送 ID、GPU 只算距离，重排序还能提前收敛。

## 研究背景与问题

- **三重压力**：十亿级数据集下 ANNS 同时受性能、成本与精度制约，IVF 或图索引往往需要 TB 级内存，TCO 随数据规模快速上升，而检索本身可能占到一次 LLM 查询总延迟的约 50%。
- **已有降本路线各有短板**：SPANN 等分层索引把倒排表放 SSD、只在内存保留质心导航图，延迟虽低但并发吞吐受限，QPS 在 4 个 CPU 线程即到峰值；PQ 最多可省 95% 内存占用，却是有损压缩，难以满足 recall≥90% 的场景。
- **GPU 加速在超大规模上反而变慢**：HBM 容量有限，导致 HBM、主机内存与 SSD 之间大量数据搬运，实验中 SPANN 直接改用 GPU 计算距离时性能下降 10%；把分层索引、PQ 与 GPU 加速简单叠加，结果甚至比只用分层索引的 SPANN 更差。

## 核心贡献

- **多级索引（multi-tiered index）**：SSD 存原始向量，GPU HBM 存 PQ 压缩向量，主机内存只保留各倒排表的向量 ID 与一张导航图，从而支持 CPU/GPU 协同过滤并避免两侧数据交换。
- **启发式重排序（heuristic re-ranking）**：把重排序拆成多个 mini-batch 顺序执行，用轻量反馈控制模型判断后续批次是否还有助于精度，连续批次贡献很小时立即终止。
- **冗余感知 I/O 去重（redundancy-aware I/O deduplication）**：把高相似向量紧凑存放以提升 SSD 上的空间局部性，并据此合并同页 I/O、复用 DRAM 缓冲消除冗余读。
- **系统实现与评估**：在只有一张入门级 GPU 的通用服务器上实现 FusionANNS；现有 ANNS 系统无法同时兼顾吞吐、延迟、成本与精度，FusionANNS 针对这一空白给出完整设计。

## 方法与技术要点

- **查询路径**：主机 CPU 先遍历内存中的导航图找出最近的 top-m 个倒排表，只把这些表的向量 ID（不含向量内容）传给 GPU，GPU 在 HBM 内用 PQ 向量完成距离计算，从而大幅削减 CPU 到 GPU 的传输量。
- **为什么 HBM 装得下**：HBM 里存的是高度压缩的 PQ 向量而不是整条倒排表；SPANN 式的边界向量复制会把索引膨胀到原始向量的 8 倍，这正是压缩后的倒排表仍放不进 HBM 的根因。
- **重排序的收敛控制**：每个 mini-batch 结束后用反馈模型评估精度增益，若连续批次贡献微弱就提前结束，避免为边际收益继续读盘。
- **读取放大的治理**：原始向量只有 128~384 字节，远小于 NVMe 最小读粒度（4 KB），因此先按相似性重排存储布局，使同一 mini-batch 内映射到同一 SSD 页的多个 I/O 合并，后续批次尽量命中 DRAM 缓冲。
- **对比设置**：与基于 SSD 的 SPANN、图索引方案 DiskANN、GPU 加速的内存系统 RUMMY 对比，数据集为 SIFT1B、SPACEV1B 与 DEEP1B，成本按 Amazon 上约 3000 美元的 NVIDIA V100 折算。

## 评估与主要结果

- **吞吐与成本**：相比 SPANN，QPS 高 9.4-13.1 倍、成本效率高 5.7-8.8 倍；相比 RUMMY，QPS 高 2-4.9 倍、成本效率高 2.3-6.8 倍，同时保持低延迟与高精度。
- **QPS/$ 明细**：表 2 中 FusionANNS 在 SIFT1B、SPACEV1B、DEEP1B 上分别为 1.98、2.35、1.01，SPANN 为 0.32、0.41、0.12，RUMMY 为 0.88、1.40、0.15；折算后相比 SPANN、DiskANN、RUMMY 分别提升 5.67-8.78 倍、2-2.5 倍与 2.25-6.82 倍。
- **内存效率**：在 DEEP1B 上，FusionANNS 的 QPS/GB 相比 SPANN、DiskANN、RUMMY 分别提升 13.1 倍、3.8 倍与 32.4 倍（表 3 为 146.16 对 11.17、38.1、4.51）。
- **动机实验**：SPANN 的 QPS 在 4 个线程就达到峰值、增加线程只抬高倒排表处理延迟，且直接改用 GPU 算距离时性能下降 10%，说明瓶颈在跨层数据移动而非算力。

[返回 Machine Learning and Storage](index.md) · [返回 FAST 2025](../index.md)
