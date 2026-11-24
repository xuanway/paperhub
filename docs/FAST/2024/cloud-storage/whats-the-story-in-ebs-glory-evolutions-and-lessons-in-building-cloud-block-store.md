---
title: "What's the Story in EBS Glory: Evolutions and Lessons in Building Cloud Block Store"
description: "FAST 2024 · Cloud Storage · 第 277–292 页"
tags:
  - "FAST2024"
  - "Cloud Storage"
---

# What's the Story in EBS Glory: Evolutions and Lessons in Building Cloud Block Store

**中文标题**：EBS 荣耀背后的故事：构建云块存储的演进与经验

**Session**：Cloud Storage · 2024-02-29 09:00–10:15 · Chair：Young-ri Choi（UNIST (Ulsan National Institute of Science and Technology)）

**作者**：Weidong Zhang, Erci Xu, Qiuping Wang, Xiaolu Zhang, Yuesheng Gu, Zhenwei Lu, Tao Ouyang, Guanqun Dai, Wenwen Peng, Zhe Xu, Shuo Zhang, Dong Wu, Yilei Peng, Tianyun Wang, Haoran Zhang, Jiasheng Wang, Wenyuan Yan, Yuanyuan Dong, Wenhui Yao, Zhongjie Wu, Lingjun Zhu, Chao Shi, Yinhu Wang, Rong Liu, Junping Wu, Jiaji Zhu, and Jiesheng Wu, Alibaba Group

**会议**：FAST 2024 · Santa Clara, CA · 第 277–292 页

**论文类型**：Deployed-Systems Paper

**获奖**：Best Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/zhang-weidong](https://www.usenix.org/conference/fast24/presentation/zhang-weidong)

**论文 PDF**：[fast24-zhang-weidong.pdf](https://www.usenix.org/system/files/fast24-zhang-weidong.pdf)

---

## 英文摘要

In this paper, we qualitatively and quantitatively discuss the design choices, production experience, and lessons in building the Elastic Block Storage (EBS) at Alibaba Cloud over the past decade. To cope with hardware advancement and users' demands, we shift our focus from design simplicity in EBS1 to high performance and space efficiency in EBS2, and finally reducing network traffic amplification in EBS3.

In addition to the architectural evolutions, we also summarize the lessons and experiences in development as four topics, including: (i) achieving high elasticity in latency, throughput, IOPS and capacity; (ii) improving availability by minimizing the blast radius of individual, regional, and global failure events; (iii) identifying the motivations and key tradeoffs in various hardware offloading solutions; and (iv) identifying the pros/cons of the alternative solutions and explaining why seemingly promising ideas would not work in practice.

## 中文摘要

本文从定性和定量两方面讨论过去十年在阿里云构建弹性块存储（EBS）时的设计选择、生产经验和教训。为应对硬件进步和用户需求，我们的关注点从 EBS1 的设计简洁性，转向 EBS2 的高性能和空间效率，最终转向 EBS3 中减少网络流量放大。

除架构演进外，我们还将开发中的经验教训总结为四个主题，包括：(i) 在延迟、吞吐量、IOPS 和容量方面实现高弹性；(ii) 通过最小化单个、区域和全局故障事件的影响范围来提高可用性；(iii) 识别各种硬件卸载方案的动机和关键权衡；(iv) 识别备选方案的优缺点，并解释为何看似有前景的想法在实践中行不通。
