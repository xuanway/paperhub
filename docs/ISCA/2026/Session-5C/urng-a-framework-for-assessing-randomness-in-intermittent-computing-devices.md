---
title: "µRNG: A Framework for Assessing Randomness in Intermittent Computing Devices"
description: "ISCA 2026 · Session 5C · µRNG: A Framework for Assessing Randomness in Intermittent Computing Devices"
tags:
  - "ISCA2026"
  - "Session 5C"
  - "Crypto and Security"
---

# µRNG: A Framework for Assessing Randomness in Intermittent Computing Devices

**中文标题：** µRNG: 面向间歇计算设备随机性评估的框架

**所属 Session：** [Session 5C](index.md) · [ISCA 2026](../index.md)

**作者：** Prakhar Sah, Matthew Hicks

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Ultra-low Size, Weight, and Power (UlSWaP) devices, capable of energy harvesting and intermittent computation, are enabling the deployment of vast networks of self-powered sensors that integrate seamlessly into our everyday environments. These technologies bring us closer to the horizon of the Fourth Industrial Revolution: a hyper-connected and automated world of smart dust. The combination of pervasive connectivity and physical proximity to sensitive data raises new security challenges. Although lightweight cryptographic protocols exist for resource-constrained systems, their behavior under intermittent power remains poorly understood. While researchers have made significant progress toward realizing practical intermittent computing systems, securing these devices and their communications remains an open problem. We lay the groundwork for securing intermittent computing systems by addressing the foundation of all cryptographic protocols: random number generation. Security protocols rely on random values for key material and nonces, yet the impact of intermittent operation on Random Number Generators (RNGs) is unclear. We survey real-world UlSWaP devices suitable for intermittent computation and observe a wide range of RNG implementations. We show that applying traditional statistical analyses, designed for continuously powered systems with limited attacker access, can yield a false sense of security in intermittent environments. To address this gap, we introduce a systematic framework for assessing and qualifying RNGs under intermittent operation. Using this framework, we evaluate nine UlSWaP device families representative of academic and commercial platforms, spanning 189 devices across manufacturers, cores, operating conditions, and security capabilities. Our analysis finds that 132 devices lack on-chip RNGs, 27 employ RNGs that are insecure under intermittency and environmental influence, and only 23 provide trustworthy entropy sources. We conclude with recommendations for selecting devices to serve as the base for future security-enabled intermittent computing systems.

## 中文摘要

具备能量采集与间歇计算能力的超低尺寸、重量与功耗（UlSWaP）设备，正在推动大规模自供电传感器网络的部署，这些网络可无缝融入我们的日常环境。这些技术让我们更接近第四次工业革命的地平线：一个超连接、自动化的“智能尘埃”世界。无处不在的连通性与对敏感数据的物理近邻性相结合，带来了新的安全挑战。尽管已有面向资源受限系统的轻量级密码协议，但它们在间歇供电下的行为仍鲜为人知。虽然研究者已在实现实用间歇计算系统方面取得重大进展，但保障这些设备及其通信的安全仍是一个未解问题。我们通过处理所有密码协议的基础——随机数生成——为保障间歇计算系统安全奠定基础。安全协议依赖随机值来生成密钥材料与随机数（nonce），然而间歇运行对随机数生成器（RNG）的影响尚不清楚。我们调研了适用于间歇计算的真实 UlSWaP 设备，观察到 RNG 实现方式差异很大。我们表明，采用为持续供电且攻击者访问受限的系统而设计的传统统计分析方法，在间歇环境中可能带来虚假的安全感。为弥补这一空白，我们提出一个系统性框架，用于在间歇运行条件下评估与判定 RNG。利用该框架，我们评估了九个在学术与商业平台上具代表性的 UlSWaP 设备系列，涵盖不同厂商、内核、运行条件与安全能力的 189 款设备。我们的分析发现：132 款设备缺少片上 RNG，27 款所采用的 RNG 在间歇性与环境影响下并不安全，仅 23 款提供了可信的熵源。最后，我们给出了关于如何选择设备以作为未来具备安全能力的间歇计算系统基础的建议。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2026](../index.md)
