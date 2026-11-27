Prelude: Priming-Guided State Reconstruction for Efficient FPGA Processor Debugging
Authors：
[Jialin Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=45764671121687500671)，[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Dean You](https://63dac.conference-program.com/?post_type=page&p=15&uid=2160294947484353928)，[Hui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0793243510929650245)，[Yushu Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=3629806380220939574)，[Xinwei Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7117674552267504328)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

Prelude：预热引导的状态重建实现高效的 FPGA 处理器调试

## 英文摘要

Debugging complex FPGA prototypes of modern processors in embedded systems is challenging due to limited signal visibility and significant tracing overhead. Existing approaches struggle to balance execution efficiency with debugging capability, often requiring either expensive continuous tracing or heavyweight snapshots. We propose Prelude, a lightweight snapshot-based debugging framework that records only essential architectural states and memory footprint of the processor on FPGA. During replay, a short visibility warm-up reconstructs internal micro-architectural states, enabling cycle-accurate analysis. Implemented on BOOM and Rocket, Prelude provides comparable visibility to prior work while significantly improving debugging efficiency: 32.88× / 2191.2× speedup over DESSERT / ENCORE on BOOM, and 18.09× / 896.4× on Rocket.

## 中文摘要

在嵌入式系统中调试现代处理器的复杂 FPGA 原型颇具挑战，原因在于信号可见性有限且追踪开销巨大。现有方法难以在执行效率与调试能力之间取得平衡，往往需要昂贵的连续追踪或重量级快照。我们提出 Prelude，一个轻量级的基于快照的调试框架，它在 FPGA 上仅记录处理器必要的架构状态与内存占用。在重放阶段，一段短暂的可见性预热即可重建内部微架构状态，从而实现周期精确的分析。我们在 BOOM 和 Rocket 上实现了 Prelude，其可见性与已有工作相当，同时显著提升了调试效率：在 BOOM 上相较 DESSERT / ENCORE 分别加速 32.88× / 2191.2×，在 Rocket 上分别加速 18.09× / 896.4×。
