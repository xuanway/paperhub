---
title: "MemSOS: OS-Guided Selective Memory Mirroring"
description: "HPCA 2026 · Memory System Reliability"
tags:
  - "HPCA2026"
  - "Memory System Reliability"
---

# MemSOS: OS-Guided Selective Memory Mirroring

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory System Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory System Reliability</p>
</div>

**论文链接**：
**作者**：Junghoon Kim Seoul National University & Samsung Electronics , Jongheon Jeong Seoul National University , Seokwon Moon Seoul National University , Seong Hoon Seo Seoul National University , Yeonhong Park Seoul National University , Jinkyu Jeong Yonsei University , Nam Sung Kim UIUC , Jae W. Lee Seoul National University
**会议**：HPCA 2026

---

## 中文标题

MemSOS：操作系统引导的选择性内存镜像

## 英文摘要

Memory errors pose an escalating threat to datacenter reliability as DRAM technology scales to smaller nodes and servers process ever-larger datasets. While Error Correction Code (ECC) provides a first-line defense, uncorrectable errors still cause catastrophic server failures with significant economic impact. Memory mirroring offers complementary protection against these errors, but existing memory mirroring solutions require reserving specific memory regions exclusively for mirroring, which incurs significant capacity overhead and thus limits wide adoption. A recent proposal suggests leveraging free memory space for mirroring, but it leaves a critical research question unanswered: which data to mirror when free memory is limited. Thus, we propose MemSOS, a selective memory mirroring system that dynamically chooses which pages to mirror based on their impact on system reliability. Specifically, MemSOS selects pages to mirror based on their criticality and recency. Criticality is evaluated by examining the page type, while recency serves as a proxy for the likelihood of future access. Our evaluation demonstrates that MemSOS reduces system Failures In Time (FIT) by up to 19,000× compared to a state-of-the-art partial mirroring scheme, while maintaining less than 3% performance overhead. In many cases, MemSOS achieves reliability levels comparable to full mirroring, underscoring its effectiveness in maximizing system availability under limited free memory space.

## 中文摘要

随着 DRAM 工艺向更小节点演进、服务器处理的数据集越来越大，内存错误对数据中心可靠性的威胁不断升级。纠错码（ECC）提供了第一道防线，但不可纠正错误仍会造成灾难性的服务器故障，带来重大经济损失。内存镜像可为此类错误提供补充保护，但现有内存镜像方案需预留专门的内存区域用于镜像，造成显著的容量开销，从而限制了广泛采用。近期有提案建议利用空闲内存空间进行镜像，但留下一个关键研究问题未答：当空闲内存有限时应当镜像哪些数据。为此我们提出 MemSOS，一个选择性内存镜像系统，依据页面影响系统可靠性的程度动态选择要镜像的页面。具体而言，MemSOS 依据页面的关键性与新近性选择镜像对象：关键性通过考察页面类型来评估，新近性则作为未来访问可能性的代理指标。评估表明，与最先进的部分镜像方案相比，MemSOS 将系统单位时间故障数（FIT）最多降低 19,000 倍，同时保持低于 3% 的性能开销。在许多情况下，MemSOS 的可靠性水平可与全镜像相当，凸显其在空闲内存有限时最大化系统可用性的有效性。
