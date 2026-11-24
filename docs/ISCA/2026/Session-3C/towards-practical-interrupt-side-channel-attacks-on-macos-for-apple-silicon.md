---
title: "Towards Practical Interrupt Side-Channel Attacks on macOS for Apple Silicon"
description: "ISCA 2026 · Session 3C · Towards Practical Interrupt Side-Channel Attacks on macOS for Apple Silicon"
tags:
  - "ISCA2026"
  - "Session 3C"
  - "Security"
---

# Towards Practical Interrupt Side-Channel Attacks on macOS for Apple Silicon

**中文标题：** 面向 Apple Silicon 的 macOS 实用化中断侧信道攻击

**所属 Session：** [Session 3C](index.md) · [ISCA 2026](../index.md)

**作者：** Xin Zhang, Chang Liu, Jiajun Zou, Yi Yang, Qingni Shen, Zhi Zhang, Trevor E. Carlson

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

In recent years, the high-end CPU landscape has shifted from an x86-dominated market to one increasingly featuring heavyweight Arm designs, most notably Apple’s M-series. While prior work has examined side-channel resilience in the Apple ecosystem, interrupt-based channels remain an open and unexplored area. This is due to Apple’s proprietary hardware and software implementation, the practicality of interrupt side channel attacks are constrained by two open challenges: precise interrupt detection and having a clear understanding of the interrupt delivery mechanism. In this paper, we propose TIDE, a precise interrupt detection technique that exploits an explicit macOS behavior arising from Apple’s Double Map mitigation. Specifically, Double Map overwrites the user-visible x18 register during kernel mapping restoration and interrupt handler branching on user-to-kernel transitions. To prevent kernel information from being accessed by user-space, macOS further clears x18 on kernel-to-user transitions in a subsequent update. Leveraging this behavior, TIDE enables two primitives without reliance on architectural timers: measuring intervals between consecutive interrupts and filtering interrupt-induced noise. Using TIDE, we reverse-engineer Apple’s closed-source interrupt delivery mechanism and reveal that, unlike Linux, Apple’s interrupt controller uniformly distributes shared peripheral interrupts across all active cores. We then demonstrate the benefits of both TIDE itself and the reverse-engineering results through three case studies. First, we fingerprint websites running on Safari with an accuracy of 93.8% in a closed-world setting and 91.2% in an open-world setting, and video fingerprinting with an accuracy of 78.1%. Next, we use TIDE to filter out interrupt noise in counting-thread timers, where TIDE tracks the number of noisy interrupts and only introduces an overhead of only 0.06%. With this, we have sigificiantly improved the SysBumps attack by increasing its success rate from 54% to 81%. Third, we examine the effect of our reverse-engineering results on the loop-counting attack, and find that a compute-intensive thread that generates no interrupts can reduce its accuracy from 94.8% to only 39.3%. By augmenting the training dataset with the number of active cores, we successfully enhance the robustness of the attack, achieving accuracies to 92.8% and 93.6% with and without noise, respectively. Further, we apply TIDE to build a timer-less covert channel with a high bandwidth of 111.65 b/s. Finally, TIDE successfully extracts the keys from Cloudflare’s Interoperable Reusable Cryptographic Library (CIRCL) v1.1.

## 中文摘要

近年来，高端 CPU 格局已从 x86 主导的市场转向越来越多地采用重量级 Arm 设计（最典型的是 Apple 的 M 系列）的局面。尽管已有工作考察了 Apple 生态系统中侧信道的抗性，但基于中断的信道仍是一个开放且尚未被探索的领域。这是由于 Apple 专有的硬件与软件实现，中断侧信道攻击的实用性受制于两个尚未解决的挑战：精确的中断检测，以及对中断投递机制的清晰理解。在本文中，我们提出 TIDE，一种精确的中断检测技术，它利用了 Apple 的 Double Map 缓解措施所引发的一种显式 macOS 行为。具体而言，Double Map 在内核映射恢复以及用户态到内核态转换时的中断处理程序分支过程中，会覆写用户可见的 x18 寄存器。为防止内核信息被用户空间访问，macOS 在后续更新中进一步在内核态到用户态转换时清除 x18。借助这一行为，TIDE 无需依赖架构定时器即可实现两个原语：测量连续中断之间的间隔，以及过滤中断引起的噪声。利用 TIDE，我们对 Apple 闭源的中断投递机制进行了逆向工程，并揭示出：与 Linux 不同，Apple 的中断控制器会将共享外设中断均匀地分发到所有活跃核上。随后，我们通过三个案例研究展示了 TIDE 本身以及逆向工程结果的价值。第一，我们对运行在 Safari 上的网站进行指纹识别，在封闭世界设置下准确率为 93.8%，在开放世界设置下为 91.2%，视频指纹识别的准确率为 78.1%。第二，我们使用 TIDE 过滤计数线程计时器中的中断噪声，TIDE 会跟踪噪声中断的数量，仅引入 0.06% 的开销。借此，我们显著改进了 SysBumps 攻击，将其成功率从 54% 提升至 81%。第三，我们考察了逆向工程结果对循环计数攻击的影响，发现一个不产生任何中断的计算密集型线程可使其准确率从 94.8% 降至仅 39.3%。通过将活跃核数量加入训练数据集，我们成功增强了攻击的鲁棒性，在有噪声与无噪声情况下分别达到 92.8% 和 93.6% 的准确率。此外，我们应用 TIDE 构建了一条无定时器隐蔽信道，带宽高达 111.65 b/s。最后，TIDE 成功从 Cloudflare 的可互操作可复用密码库（CIRCL）v1.1 中提取了密钥。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：zhangxin00/tide](https://github.com/zhangxin00/tide)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2026](../index.md)
