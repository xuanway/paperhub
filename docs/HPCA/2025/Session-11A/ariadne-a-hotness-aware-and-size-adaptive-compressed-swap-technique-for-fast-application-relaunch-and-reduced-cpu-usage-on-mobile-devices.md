---
title: "Ariadne: A Hotness-Aware and Size-Adaptive Compressed Swap Technique for Fast Application Relaunch and Reduced CPU Usage on Mobile Devices"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Ariadne: A Hotness-Aware and Size-Adaptive Compressed Swap Technique for Fast Application Relaunch and Reduced CPU Usage on Mobile Devices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Yu Liang (ETH Zürich), Aofeng Shen (ETH Zürich), Chun Jason Xue (MBZUAI), Riwei Pan (City University of Hong Kong), Haiyu Mao (ETH Zürich), Nika Mansouri Ghiasi (ETH Zürich), Qingcai Jiang (ETH Zürich and University of Science and Technology of China), Rakesh Nadig (ETH Zürich), Lei Li (City University of Hong Kong), Rachata Ausavarungnirun (MangoBoost), Mohammad Sadrosadati (ETH Zürich), Onur Mutlu (ETH Zürich)
**会议**：HPCA 2025

---

## 中文标题

Ariadne：面向移动设备应用快速重启与降低 CPU 占用的热感知尺寸自适应压缩交换技术

## 英文摘要

As the memory demands of individual mobile applications continue to grow and the number of concurrently running applications increases, available memory on mobile devices is becoming increasingly scarce. When memory pressure is high, current mobile systems use a RAM-based compressed swap scheme (called ZRAM) to compress unused execution-related data (called anonymous data in Linux) in main memory. This approach avoids swapping data to secondary storage (NAND flash memory) or terminating applications, thereby achieving shorter application relaunch latency. In this paper, we observe that the state-of-the-art ZRAM scheme prolongs relaunch latency and wastes CPU time because it does not differentiate between hot and cold data or leverage different compression chunk sizes and data locality. We make three new observations. First, anonymous data has different levels of hotness. Hot data, used during application relaunch, is usually similar between consecutive relaunches. Second, when compressing the same amount of anonymous data, small-size compression is very fast, while large-size compression achieves a better compression ratio. Third, there is locality in data access during application relaunch. Based on these observations, we propose a hotness-aware and size-adaptive compressed swap scheme, Ariadne, for mobile devices to mitigate relaunch latency and reduce CPU usage. Ariadne incorporates three key techniques. First, a low-overhead hotness-aware data organization scheme aims to quickly identify the hotness of anonymous data without significant overhead. Second, a size-adaptive compression scheme uses different compression chunk sizes based on the data’s hotness level to ensure fast decompression of hot and warm data. Third, a proactive decompression scheme predicts the next set of data to be used and decompresses it in advance, reducing the impact of data swapping back into main memory during application relaunch. We implement and evaluate Ariadne on a commercial smartphone, Google Pixel 7 with the latest Android 14. Our experimental evaluation results show that, on average, Ariadne reduces application relaunch latency by 50% and decreases the CPU usage of compression and decompression procedures by 15% compared to the state-of-the-art compressed swap scheme for mobile devices.

## 中文摘要

随着单个移动应用内存需求不断增长且并发运行的应用数量增加，移动设备的可用内存日益紧张。当内存压力很高时，现有移动系统采用基于 RAM 的压缩交换方案（ZRAM）在主存中压缩未使用的与执行相关的数据（Linux 中称为匿名数据），从而避免将数据换出到 NAND 闪存或终止应用，获得更短的应用重启时延。本文观察到，最先进的 ZRAM 方案延长了重启时延并浪费 CPU 时间，因为它不区分冷热数据，也未利用不同压缩块大小与数据局部性。我们给出三点观察：第一，匿名数据具有不同热度，重启时使用的热数据在连续重启间通常相似；第二，压缩等量匿名数据时，小尺寸压缩很快，而大尺寸压缩有更好的压缩率；第三，重启期间的数据访问存在局部性。据此我们提出面向移动设备的热感知与尺寸自适应压缩交换方案 Ariadne，以降低重启时延并减少 CPU 占用。Ariadne 包含三项技术：低开销的热感知数据组织，快速识别匿名数据热度；按热度级别使用不同压缩块大小的尺寸自适应压缩，保证热数据与温数据快速解压；预测即将使用的数据并提前解压的主动解压，减小数据换回主存的影响。我们在运行 Android 14 的商用智能手机 Google Pixel 7 上实现并评估。结果表明，相比最先进的移动端压缩交换方案，Ariadne 平均将应用重启时延降低 50%，并将压缩与解压过程的 CPU 占用降低 15%。
