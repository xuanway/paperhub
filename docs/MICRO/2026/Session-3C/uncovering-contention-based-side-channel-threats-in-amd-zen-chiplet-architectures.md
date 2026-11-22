---
title: "Uncovering Contention-Based Side-Channel Threats in AMD Zen Chiplet Architectures"
description: "MICRO 2026 · Session 3C · 揭示 AMD Zen 芯粒架构中基于资源争用的侧信道威胁"
tags:
  - "MICRO2026"
  - "Side-Channel Attack"
---

# Uncovering Contention-Based Side-Channel Threats in AMD Zen Chiplet Architectures

**中文标题：** 揭示 AMD Zen 芯粒架构中基于资源争用的侧信道威胁

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Yunpeng Xu, Yueteng Yu, Xuanzeng Song, Zongle Huang, Yongpan Liu, Guowei Zhang, Shuwen Deng

**来源：** MICRO 2026，pp. 1099–1114；[DOI](https://doi.org/10.1109/MICRO67795.2026.00086)

## 英文摘要

Chiplet-based design has become a critical approach for overcoming fabrication scalability limitations and boosting manufacturing yield, by assembling processors from multiple smaller, independently produced silicon dies. Among commercially shipped processors, AMD's Zen family stands as one of the most broadly adopted product lines built upon this chiplet-driven architecture. In this work, we systematically analyze the security implications of inter-chiplet and intra-chiplet communication pathways in AMD's Zen chiplet processors, revealing a class of resource-contention side channels spanning diverse internal interconnects. We conduct a systematic end-to-end reverse-engineering study on Zen 4, where we recover on-chiplet and cross-chiplet topology, physical layout, data routing strategies, and the hash functions governing several internal functional units; we additionally validate key results on Zen 2/3/5. Building on these findings, we characterize the properties and exploitability of contention-induced information leakage. Leveraging the derived knowledge, we demonstrate a stateless covert communication channel across cores, achieving effective throughput of up to 3.25 Mbps within a single chiplet and 814 Kbps across chiplets on Zen 4. We further validate the practical severity through multiple side-channel attack scenarios targeting real-world software: website fingerprinting on Alexa Top-100 sites with 87.4% accuracy, full RSA private key extraction with 100% accuracy after 20 votes, and keystroke timing inference with 92% accuracy.

## 中文摘要

基于小芯片的设计已成为通过使用多个较小的独立生产的硅芯片组装处理器来克服制造可扩展性限制并提高制造产量的关键方法。在商用处理器中，AMD 的 Zen 系列是基于这种小芯片驱动架构构建的最广泛采用的产品线之一。在这项工作中，我们系统地分析了 AMD Zen 小芯片处理器中小芯片间和小芯片内通信路径的安全影响，揭示了一类跨越不同内部互连的资源争用侧通道。我们对 Zen 4 进行了系统的端到端逆向工程研究，恢复了 Chiplet 上和跨 Chiplet 拓扑、物理布局、数据路由策略以及管理多个内部功能单元的哈希函数；我们还验证了 Zen 2/3/5 的关键结果。基于这些发现，我们描述了争用引起的信息泄漏的属性和可利用性。利用衍生的知识，我们演示了跨内核的无状态隐蔽通信通道，在单个芯片内实现了高达 3.25 Mbps 的有效吞吐量，在 Zen 4 上跨芯片实现了 814 Kbps。我们通过针对真实世界软件的多个侧信道攻击场景进一步验证了实际严重性：Alexa Top-100 网站上的网站指纹识别准确率达到 87.4%，完整 RSA 私钥提取在 20 次投票后准确率达到 100%，以及击键计时推断准确率高达 92%。

## 中文关键词

侧信道攻击；芯粒；互连争用；AMD Zen

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/THU-HAS/ZENeath-micro-ae](https://github.com/THU-HAS/ZENeath-micro-ae)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
