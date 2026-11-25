FILCO: Flexible Composing Architecture with Real-Time Reconfigurability for DNN Acceleration
Authors：
[Xingzhen Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=63463982556895264651)，[Jinming Zhuang](https://63dac.conference-program.com/?post_type=page&p=15&uid=46754897122762575931)，[Zhuoping Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0190404572782304487)，[Shixin Ji](https://63dac.conference-program.com/?post_type=page&p=15&uid=23773291736995867371)，[Sarah Schultz](https://63dac.conference-program.com/?post_type=page&p=15&uid=77897386372090744871)，[Zheng Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=655143)，[Weisong Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=45532507033613531421)，[Peipei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=621843)

## 中文标题

FILCO：面向 DNN 加速的具备实时可重构性的灵活组合架构

## 英文摘要

With the development of deep neural network (DNN) enabled applications, achieving high hardware resource efficiency on diverse workloads is non-trivial in heterogeneous computing platforms. Prior works discuss dedicated architectures to achieve maximal resource efficiency. However, a mismatch between hardware and workloads always exists in various diverse workloads. Other works discuss overlay architecture that can dynamically switch dataflow for different workloads. However, these works are still limited by flexibility granularity and induce much resource inefficiency. To solve this problem, we propose a flexible composing architecture, FILCO, that can efficiently match diverse workloads to achieve the optimal storage and computation resource efficiency. FILCO can be reconfigured in real-time and flexibly composed into a unified or multiple independent accelerators. We also propose the FILCO framework, including an analytical model with a two-stage DSE that can achieve the optimal design point. We also evaluate the FILCO framework on the 7nm AMD Versal VCK190 board. Compared with prior works, our design can achieve 1.3×∼5× throughput and hardware efficiency on various diverse workloads.

## 中文摘要

随着深度神经网络（DNN）应用的发展，在异构计算平台上针对多样化工作负载实现高硬件资源效率并非易事。已有工作讨论了通过专用架构来达到最大资源效率，然而在各类多样化工作负载中，硬件与负载之间的失配始终存在。另一些工作讨论了可为不同负载动态切换数据流的覆盖（overlay）架构，但这些工作仍受限于灵活性粒度，并造成较多资源低效。为解决该问题，我们提出一种灵活组合架构 FILCO，它能够高效匹配多样化工作负载，以实现最优的存储与计算资源效率。FILCO 可实时重构，并可灵活组合为统一的加速器或多个相互独立的加速器。我们还提出 FILCO 框架，其中包含一个解析模型与可实现最优设计点的两阶段 DSE。我们在 7nm AMD Versal VCK190 开发板上对 FILCO 框架进行了评估。与已有工作相比，我们的设计在各类多样化工作负载上可实现 1.3×∼5× 的吞吐率与硬件效率提升。
