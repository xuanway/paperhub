---
title: "SSBleed: Non-speculative Side-channel Attacks via Speculative Store Bypass on Armv9 CPUs"
description: "HPCA 2026 · Hardware Security and Side-Channel Defenses"
tags:
  - "HPCA2026"
  - "Hardware Security and Side-Channel Defenses"
---

# SSBleed: Non-speculative Side-channel Attacks via Speculative Store Bypass on Armv9 CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Hardware Security and Side-Channel Defenses。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Hardware Security and Side-Channel Defenses</p>
</div>

**论文链接**：
**作者**：Chang Liu Tsinghua University , Hongpei Zheng Tsinghua University , Xin Zhang Peking University , Dapeng Ju Tsinghua University , Dongsheng Wang Tsinghua University , Yinqian Zhang Southern University of Science and Technology , Trevor E. Carlson National University of Singapore
**会议**：HPCA 2026

---

## 中文标题

SSBleed：在 Armv9 CPU 上经由推测存储旁路的非推测侧信道攻击

## 英文摘要

Modern CPUs employ Speculative Store Bypass (SSB) to reduce load latency and improve performance. In response to transient attacks such as Spectre, CPU vendors have also introduced mitigations to prevent incorrect speculation from leaking data. In this work, we show that the SSB on Armv9 CPUs introduces a previously unexplored form of non-speculative data leakage. Specifically, we find that the SSB on Armv9 performance cores is governed by an undocumented predictor. Through reverse engineering, we uncover the design of this predictor and show that it lacks isolation across security domains. Furthermore, existing mitigations such as SSBS are insufficient to prevent leaks. Based on this, we present SSBleed, the first non-speculative side-channel attack via SSB on Armv9 CPUs. We validate the practicality of SSBleed through five case studies, including cross-process RSA signature and key generation attacks on the latest version of MbedTLS and WolfSSL, interrupt detection, and improved data transmission in two transient attacks. Finally, we propose a flush-based mitigation through a kernel patch, which incurs an average performance overhead of 0.46%.

## 中文摘要

现代 CPU 采用推测存储旁路（SSB）来降低加载时延并提升性能。为应对 Spectre 等瞬态攻击，CPU 厂商还引入了防止错误推测泄漏数据的缓解措施。本文表明，Armv9 CPU 上的 SSB 引入了一种此前未被探索的非推测数据泄漏形式。具体而言，我们发现 Armv9 性能核上的 SSB 由一种未公开的预测器控制；通过逆向工程，我们揭示了该预测器的设计，并表明它缺乏跨安全域的隔离。此外，SSBS 等现有缓解措施不足以阻止泄漏。基于此，我们提出 SSBleed，首个在 Armv9 CPU 上经由 SSB 的非推测侧信道攻击。我们通过五个案例研究验证了 SSBleed 的实用性，包括对最新版本 MbedTLS 与 WolfSSL 的跨进程 RSA 签名与密钥生成攻击、中断检测，以及两种瞬态攻击中的数据传递改进。最后，我们提出一种基于内核补丁的冲刷式缓解措施，其平均性能开销为 0.46%。
