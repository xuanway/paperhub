Two Teachers Better Than One: Hardware-Physics Co-Guided Distributed Scientific Machine Learning
Authors：
[Yuchen Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=49780010254254002041)，[Junhuan Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=864743)，[Hao Wan](https://63dac.conference-program.com/?post_type=page&p=15&uid=28724474813256149661)，[Yipei Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9944742228912684782)，[Hanhan Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0297784956624527348)，[Youzuo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=865033496685119077)，[Lei Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=342743)

## 中文标题

两位教师胜于一位：硬件-物理协同引导的分布式科学机器学习

## 英文摘要

Scientific machine learning (SciML) is increasingly applied to infield processing, controlling, and monitoring; however, wide-area sensing, real-time demands, and strict energy and reliability constraints make centralized SciML implementation impractical. Most SciML models assume raw data aggregation at a central node, incurring prohibitively high communication latency and energy costs; yet, distributing models developed for general-purpose ML often breaks essential physical principles, resulting in degraded performance. To address these challenges, we introduce EPIC, a hardware-and physics-co-guided distributed SciML framework, using full-waveform inversion (FWI) as a representative task. EPIC performs lightweight local encoding on end devices and physics-aware decoding at a central node. By transmitting compact latent features rather than high-volume raw data and by using cross-attention to capture inter-receiver wavefield coupling, EPIC significantly reduces communication cost while preserving physical fidelity. Evaluated on a distributed testbed with five end devices and one central node, and across 10 datasets from OpenFWI, EPIC reduces latency by 8.9× and communication energy by 33.8×, while even improving reconstruction fidelity on 8 out of 10 datasets.

## 中文摘要

科学机器学习（SciML）正日益应用于现场处理、控制与监测；然而，广域感知、实时性需求以及严格的能耗与可靠性约束使集中式 SciML 实现不切实际。多数 SciML 模型假设原始数据在中心节点聚合，这带来高得难以承受的通信延迟与能耗开销；而为通用机器学习开发的模型若采用分布式部署，又往往违背基本物理原理，导致性能退化。为应对这些挑战，我们提出 EPIC，一个硬件与物理协同引导的分布式 SciML 框架，并以全波形反演（FWI）作为代表性任务。EPIC 在终端设备上执行轻量级本地编码，在中心节点进行物理感知解码。通过传输紧凑的隐特征而非海量原始数据，并利用交叉注意力捕捉接收器间的波场耦合，EPIC 在保持物理保真度的同时显著降低通信开销。在由五个终端设备与一个中心节点构成的分布式测试床上、基于 OpenFWI 的 10 个数据集评估，EPIC 将延迟降低 8.9×、通信能耗降低 33.8×，甚至在 10 个数据集中的 8 个上还进一步提升了重建保真度。
