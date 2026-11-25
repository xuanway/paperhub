SSD Reforge: Dynamic Parity Management to Extend SSD Lifetime Under Aging
Authors：
[Ziyu Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=01393546249275967931)，[Yingdi Shan](https://63dac.conference-program.com/?post_type=page&p=15&uid=514397011352868318)，[Jinlei Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5896444217621983522)，[Mingxing Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6600409225009972135)，[Yongwei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5017120961218593028)

## 中文标题

SSD Reforge：老化条件下通过动态校验管理延长 SSD 寿命

## 英文摘要

Flash wear raises raw bit error rate (RBER), limiting SSD lifetime by TBW or P/E cycles. We present SSD Reforge, which dynamically strengthens protection near end-of-life by adding intra-device parity, allowing more lifetime. To handle inter-block reliability heterogeneity, we build an RBER-based error-probability model and derive parity stripe grouping as a combinatorial optimization problem. We design Reliability-Aware Striping (RAS) for efficient grouping and Stripe UPER Leveling (SUPERL) to sustain RAS during subsequent writes. Implemented in FEMU and evaluated with real I/O traces, SSD Reforge increases user TBW by up to 40% on average versus traditional mode at the lifetime limit, significantly extending SSD lifespan.

## 中文摘要

闪存磨损会提高原始误码率（RBER），并通过 TBW 或 P/E 循环限制 SSD 寿命。我们提出 SSD Reforge，它在寿命末期通过增加盘内校验来动态增强保护，从而获得更长的使用寿命。为应对块间可靠性异质性，我们构建了基于 RBER 的错误概率模型，并将校验条带分组推导为一个组合优化问题。我们设计了可靠性感知条带化（RAS）以实现高效分组，并提出条带 UPER 均衡（SUPERL）以在后续写入中维持 RAS。SSD Reforge 在 FEMU 中实现，并使用真实 I/O 轨迹进行评估，在寿命极限处相比传统模式将用户 TBW 平均提升最高 40%，显著延长了 SSD 使用寿命。

## 英文关键词

SSD, Reforge, Reliability, Lifetime

## 中文关键词

SSD、Reforge、可靠性、寿命
