---
title: "Five Minutes of DDoS Brings down Tor: DDoS Attacks on the Tor Directory Protocol and Mitigations"
description: "EuroSys 2026 · Security · Zhongtang Luo (Purdue University), Jianting Zhang (Purdue University), Akshat Ne"
tags:
  - "EuroSys2026"
  - "Security"
---

# Five Minutes of DDoS Brings down Tor: DDoS Attacks on the Tor Directory Protocol and Mitigations

**中文标题：** 五分钟 DDoS 即可击垮 Tor：针对 Tor 目录协议的 DDoS 攻击及缓解措施

**所属 Session：** [Session 6.1: Security](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security</p>
</div>

**作者**：Zhongtang Luo (Purdue University), Jianting Zhang (Purdue University), Akshat Neerati (Purdue University), Aniket Kate (Supra Research / Purdue University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803607)

## 英文摘要

The Tor network offers network anonymity to its users by routing their traffic through a sequence of relays. A group of nine directory authorities maintains information about all available relay nodes using a distributed directory protocol. We observe that the current protocol makes a strong synchrony assumption, which makes it vulnerable to natural as well as adversarial non-synchronous communication scenarios over the Internet. In this paper, we show that it is possible to cause a failure in the Tor directory protocol by targeting a majority of the authorities for only five minutes using a well-executed distributed denial-of-service (DDoS) attack. We demonstrate this attack in a controlled environment and show that it is cost-effective for as little as $53.28 per month to disrupt the protocol and to effectively bring down the entire Tor network. To mitigate this problem, we consider the popular partial synchrony assumption that ensures protocol security even when the network delays are large and unknown initially. We design a new Tor directory protocol that leverages a standard partial-synchronous consensus protocol to solve this problem, while also proving its security. We have implemented a prototype in Rust, demonstrating comparable performance to the current protocol.

## 中文摘要

Tor 网络通过将用户流量沿一系列中继路由来为其用户提供网络匿名性。由九个目录权威组成的小组使用分布式目录协议维护所有可用中继节点的信息。我们观察到，当前协议做出了强同步假设，这使其容易受到互联网上自然发生的以及对抗性的非同步通信场景的影响。在本文中，我们表明，通过精心执行的分布式拒绝服务（DDoS）攻击，仅针对多数权威机构持续五分钟，就有可能使 Tor 目录协议发生故障。我们在受控环境中演示了该攻击，并表明其成本极低——每月仅需 53.28 美元即可破坏该协议并有效击垮整个 Tor 网络。为缓解此问题，我们考虑常用的部分同步假设，该假设即使在网络延迟很大且初始未知时也能保证协议安全。我们设计了一个新的 Tor 目录协议，利用标准的部分同步共识协议来解决此问题，同时证明了其安全性。我们用 Rust 实现了原型，表现出与当前协议相当的性能。

**英文关键词：** Tor, Denial-of-Service Attack, Directory Protocol, Partial Synchrony, Consensus

**中文关键词：** Tor、拒绝服务攻击、目录协议、部分同步、共识

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
