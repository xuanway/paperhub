---
title: "Parallel Integer Sort: Theory and Practice"
description: "PPoPP 2024 Session Parallel Algorithms：DovetailSort：融合整数排序与比较排序思想以利用重复键"
tags:
  - "PPoPP2024"
  - "Session-7"
  - "Parallel Algorithms"
  - "Integer Sort"
  - "Radix Sort"
authors:
  - "Xiaojun Dong"
  - "Laxman Dhulipala"
  - "Yan Gu"
  - "Yihan Sun"
session: "Session 7: Parallel Algorithms"
session_number: 7
session_chair: "Prashant Pandey"
date: "2024-03-05"
time: "15:00–15:20"
room: "Moorfoot"
doi: "10.1145/3627535.3638483"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Parallel Integer Sort: Theory and Practice

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">从理论与实践两方面研究并行整数排序，为一类现有实用整数排序算法给出更紧的理论界，并提出兼顾理论效率与实际性能的新算法 DovetailSort。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 7: Parallel Algorithms</p>
</div>

**作者**：Xiaojun Dong (University of California, Riverside); Laxman Dhulipala (University of Maryland, College Park); Yan Gu, Yihan Sun (University of California, Riverside)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 15:00–15:20 · Session 7: Parallel Algorithms（主席：Prashant Pandey）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638483) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Integer sorting is a fundamental problem in computer science. This paper studies parallel integer sort both in theory and in practice. In theory, we show tighter bounds for a class of existing practical integer sort algorithms, which provides a solid theoretical foundation for their widespread usage in practice and strong performance. In practice, we design a new integer sorting algorithm, DovetailSort, that is theoretically-efficient and has good practical performance. In particular, DovetailSort overcomes a common challenge in existing parallel integer sorting algorithms, which is the difficulty of detecting and taking advantage of duplicate keys. The key insight in DovetailSort is to combine algorithmic ideas from both integer-and comparison-sorting algorithms. In our experiments, DovetailSort achieves competitive or better performance than existing state-of-the-art parallel integer and comparison sorting algorithms on various synthetic and real-world datasets.

## 中文摘要

整数排序是计算机科学中的一个基础问题。本文从理论和实践两方面研究并行整数排序。在理论上，我们为一类现有的实用整数排序算法给出了更紧的界，这为它们在实践中的广泛使用和强劲性能提供了坚实的理论基础。在实践上，我们设计了一种新的整数排序算法 DovetailSort，它具有理论效率且实际性能良好。特别地，DovetailSort 克服了现有并行整数排序算法中的一个常见挑战，即难以检测并利用重复键。DovetailSort 的关键洞见在于结合整数排序和比较排序两类算法的思想。在我们的实验中，DovetailSort 在各种合成和真实数据集上取得了与现有最先进的并行整数排序和比较排序算法相当或更好的性能。

## 英文关键词

Integer Sort, Radix Sort, Parallel Algorithms

## 中文关键词

整数排序；基数排序；并行算法

---

## 一句话总结

> 从理论与实践两方面研究并行整数排序，为一类现有实用整数排序算法给出更紧的理论界，并提出兼顾理论效率与实际性能的新算法 DovetailSort。

## 研究问题

现有并行整数排序算法难以检测并利用重复键，这成为其性能提升的常见障碍；同时一类实用整数排序算法此前缺乏紧致的理论界支撑。

## 方法简述

- 为一类现有实用整数排序算法推导更紧的界，为其在实践中被广泛使用且性能强劲提供坚实的理论基础
- 设计新的整数排序算法 DovetailSort，使其兼具理论效率与良好的实际性能
- 将整数排序与比较排序两类算法的思想相结合，以检测并利用重复键

## 主要结果

- 在多种合成与真实数据集上，DovetailSort 的性能与现有最先进的并行整数排序及比较排序算法相当或更好
- 为一类现有实用整数排序算法建立了更紧的理论界，解释了其实际优异性能

---

> 所属 Session：[Session 7: Parallel Algorithms](index.md) · 返回 [PPoPP 2024 总览](../index.md)
