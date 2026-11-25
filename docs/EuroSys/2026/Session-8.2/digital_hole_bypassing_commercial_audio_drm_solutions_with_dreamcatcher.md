---
title: "Digital Hole: Bypassing Commercial Audio DRM Solutions with DReaMcatcher"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Björn Ruytenberg (Vrije Universiteit Amsterdam), Mohammad Sina Karvandi (Vrije U"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# Digital Hole: Bypassing Commercial Audio DRM Solutions with DReaMcatcher

**中文标题：** 数字漏洞：用 DReaMcatcher 绕过商用音频 DRM 方案

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Björn Ruytenberg (Vrije Universiteit Amsterdam), Mohammad Sina Karvandi (Vrije Universiteit Amsterdam), Herbert Bos (Vrije Universiteit Amsterdam), Erik van der Kouwe (Vrije Universiteit Amsterdam), Asia Slowinska (Vrije Universiteit Amsterdam)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803583)

## 英文摘要

Digital Rights Management (DRM) technologies underpin the protection of modern digital content, including music, films, software, games, and e-books, and support multibillion-dollar industries that rely on its effectiveness. In this paper, we question whether this trust in DRM is warranted. In the absence of malicious content-capturing hardware, it rests on the assumption that DRM forces content pirates to resort to the “Analog Hole”, where the conversion from digital to analog and back leads to significant degradation in quality. We show that this assumption is false and that even the most sophisticated designs and hardware-level protection of high-quality audio is fundamentally vulnerable to what we term the software-based “Digital Hole”. In particular, our hypervisor-based solution intercepts digital communication between kernel space and hardware-based audio peripherals—well beyond the reach of audio DRM technology. As an example, we investigate HD Audio–compatible devices and demonstrate that it is possible to dump DRM-protected songs and convert them to lossless audio files across major commercially available streaming services (Netflix, Spotify, etc.), along with a proof-of-concept for effectively extracting and storing protected content. We analyze the technical roots of this weakness, discuss potential countermeasures, and highlight the broader implications for designing more resilient audio DRM systems. Our work underscores that audio DRM, in its current form, cannot fully achieve its intended goals, motivating the community to radically redesign approaches to digital content protection.

## 中文摘要

数字版权管理（DRM）技术支撑着对现代数字内容（包括音乐、电影、软件、游戏和电子书）的保护，并支撑着依赖其有效性的数十亿美元产业。本文质疑这种对 DRM 的信任是否合理。在不存在恶意内容捕获硬件的情况下，这种信任建立在如下假设之上：DRM 迫使内容盗版者只能诉诸“模拟漏洞”（Analog Hole），即数字到模拟再回到数字的转换会导致质量显著下降。我们表明这一假设是错误的，即便是最精巧的设计和硬件级保护的高质量音频，也从根本上面临我们称之为基于软件的“数字漏洞”（Digital Hole）的威胁。具体而言，我们基于 hypervisor 的方案拦截内核空间与硬件音频外设之间的数字通信——这远在音频 DRM 技术的作用范围之外。作为示例，我们研究了兼容 HD Audio 的设备，并证明可以在各大商用流媒体服务（Netflix、Spotify 等）上转储受 DRM 保护的歌曲并将其转换为无损音频文件，同时给出有效提取和存储受保护内容的概念验证。我们分析了这一弱点的技术根源，讨论了可能的对策，并强调了其对设计更具韧性的音频 DRM 系统的更广泛影响。我们的工作强调，当前形式的音频 DRM 无法完全实现其预期目标，这促使业界彻底重新设计数字内容保护的方法。

**英文关键词：** DRM, PCIe Interconnect, virtualization, security

**中文关键词：** DRM、PCIe 互连、虚拟化、安全

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
