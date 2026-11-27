---
title: "Marching Page Walks: Batching and Concurrent Page Table Walks for Enhancing GPU Throughput"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# Marching Page Walks: Batching and Concurrent Page Table Walks for Enhancing GPU Throughput

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Jiwon Lee (Yonsei University), Gun Ko (Yonsei University), Myung Kuk Yoon (Ewha Womans University), Ipoom Jeong (Yonsei University), Yunho Oh (Korea University), Won Woo Ro (Yonsei University)
**会议**：HPCA 2025

---

## 中文标题

Marching Page Walks：以批处理与并发页表遍历提升 GPU 吞吐

## 英文摘要

Virtual memory, with the support of address translation hardware, is a key technique in expanding programmability and memory management in GPUs. However, the nature of the GPU execution model heavily pressures its translation hardware, particularly due to a discrepancy in the behavior of page table walkers and thousands of concurrently running threads. In GPU workloads, multiple threads simultaneously access a number of pages necessitating a substantial number of translations whereas each walker handles only a single walk request at a time. Such a limitation significantly increases the queueing latency of walk requests, which we observe as a major bottleneck for servicing page table walks in GPUs. To tackle this challenge, we investigate a design of page walkers that facilitates multiple walk requests to be handled together in batches. Then, we make the following observations: 1) allowing a page walker to issue beyond a single memory request significantly improves the throughput of walkers, and 2) GPU applications tend to concurrently access pages in wide address ranges. By leveraging the above implications, we propose Marching Page Walks (MPW) that effectively mitigate the contention in GPU page table walkers. MPW scans pending walk requests to identify ones that can be grouped together. Then, MPW batches these requests and concurrently handles them by issuing multiple memory instructions. Experiments show that MPW reduces the queueing latency of page walks by 86.7% and improves GPU performance by 55.6% over the baseline design.

## 中文摘要

在地址转换硬件的支持下，虚拟内存是扩展 GPU 可编程性与内存管理的关键技术。然而，GPU 执行模型的特性给其转换硬件带来巨大压力，尤其是页表遍历器的行为与数千个并发运行的线程之间存在不匹配。在 GPU 负载中，多个线程同时访问若干页面，需要大量地址转换，而每个遍历器一次只能处理一个遍历请求。这一限制显著增加了遍历请求的排队延迟，我们观察到这是 GPU 中页表遍历服务的主要瓶颈。为应对这一挑战，我们研究了一种可将多个遍历请求成批一起处理的页遍历器设计。随后我们有以下观察：1）允许页遍历器一次发出超过单个内存请求，可显著提升遍历器的吞吐；2）GPU 应用倾向于并发访问宽地址范围内的页面。基于上述发现，我们提出 Marching Page Walks（MPW），可有效缓解 GPU 页表遍历器中的争用。MPW 扫描待处理的遍历请求，找出可以归为一组的请求，随后将这些请求成批处理，并通过发出多条内存指令并发处理它们。实验表明，相较基线设计，MPW 将页表遍历的排队延迟降低 86.7%，并将 GPU 性能提升 55.6%。
