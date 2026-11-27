---
title: "Secret Caching Sauce for High-Performance Secure Memory"
description: "HPCA 2026 · DRAM Security and Reliability"
tags:
  - "HPCA2026"
  - "DRAM Security and Reliability"
---

# Secret Caching Sauce for High-Performance Secure Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: DRAM Security and Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM Security and Reliability</p>
</div>

**论文链接**：
**作者**：Xu Jiang Huazhong University of Science and Technology , Xueliang Wei Huazhong University of Science and Technology , YiFei Qu Huazhong University of Science and Technology , Dan Feng Huazhong University of Science and Technology, China , Yulai Xie Huazhong University of Science and Technology , Wei Tong Huazhong University of Science and Technology, China
**会议**：HPCA 2026

---

## 中文标题

高性能安全内存的缓存秘方

## 英文摘要

In modern secure memory systems, confidentiality and integrity protection add additional metadata (called security metadata) that are accessed during memory data accesses. Security metadata are cached in on-chip metadata caches to reduce the access cost. However, prior studies overlook the differences between security metadata caching and data caching. Metadata caches are managed similarly to data caches. We identify three special features of security metadata caching. Due to these features, existing management methods face two problems. First, there are frequent security metadata accesses and many metadata cache misses, because the best metric (i.e., reuse distance) used to select replacement victims in data caches is suboptimal for metadata caches. Second, the miss penalty is large since misses suffer from long security metadata update and verification chains. The two problems significantly increase data access latency, thereby degrading system performance. We propose SECRET, a security metadata oriented cache management framework. SECRET reduces accesses and misses by selecting victims based on a new metric superior to reuse distances, called the connections between cached security metadata. We identify this metric by developing an optimal replacement decision search approach and analyzing the optimal decisions. SECRET reduces the miss penalty by actively breaking update chains and parallelizing verification chains. Experimental results show that SECRET reduces the data read (write) latency by 30.2% (59.9%) and improves system performance by 26.2% compared with the state-of-the-art designs.

## 中文摘要

在现代安全内存系统中，机密性与完整性保护会引入额外的元数据（称为安全元数据），它们在访存时被访问。安全元数据被缓存在片上的元数据缓存中以降低访问开销。然而，已有研究忽视了安全元数据缓存与数据缓存之间的差异，元数据缓存仍按数据缓存的方式管理。我们总结了安全元数据缓存的三个特殊性质，这些性质使现有管理方法面临两个问题。第一，安全元数据访问频繁且缓存缺失很多，因为数据缓存中用于选择替换牺牲块的度量（即复用距离）对元数据缓存而言并非最优。第二，缺失代价很高，因为缺失需经历冗长的安全元数据更新与验证链。这两个问题显著增加数据访问时延，从而降低系统性能。我们提出 SECRET，一个面向安全元数据的缓存管理框架。SECRET 依据一种优于复用距离的新度量，即被缓存安全元数据之间的连接关系，来选择牺牲块，从而减少访问与缺失。我们通过开发最优替换决策搜索方法并分析最优决策来发现该度量。SECRET 还通过主动打断更新链并并行化验证链来降低缺失代价。实验结果表明，与最先进设计相比，SECRET 将数据读（写）时延降低 30.2%（59.9%），并将系统性能提升 26.2%。
