Unispike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy
Authors：
[Qinghui Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=98387430263124001381)，[Zhuo Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=83965356734314780011)，[Xin Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=79817732201394814181)，[Ouwen Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=65110909307100705931)，[Ming Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3115283270269396824)，[Pan Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=41713820207793238711)，[Ying Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7495322202395404497)，[Shuiguang Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=83479040981359172041)，[Gang Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=0718372250343937808)

## 中文标题

UniSpike：通过消除地址冗余在神经形态系统上加速脉冲神经网络

## 英文摘要

Many-core neuromorphic systems serve as specialized accelerators for Spiking Neural Networks (SNNs). However, the communication mechanisms in existing neuromorphic systems incur significant traffic and energy overhead due to redundant address transmissions, a bottleneck exacerbated by the short payloads inherent to the spike-based communication nature of SNNs. Specifically, our characterization reveals that in current neuromorphic systems, duplicate address transmissions can account for up to 49% of the total traffic in representative workloads. This paper presents UniSpike, a hardware-software co-design that eliminates address redundancy by aggregating spikes destined for the same core into single, compact packets. UniSpike implements a spike transmission scheduling strategy to enable efficient spike merging, supported by a dedicated hardware architecture for runtime packet assembly and dispatch, as well as a destination-aware SNN partitioning algorithm that maximizes address sharing opportunities. Experimental results demonstrate that on average, UniSpike reduces traffic volume by 1.93×, achieving 1.77× speedup and 1.50× energy efficiency improvement over SOTA designs.

## 中文摘要

众核神经形态系统是脉冲神经网络（SNN）的专用加速器。然而，现有神经形态系统中的通信机制由于冗余的地址传输而带来显著的流量与能耗开销，而 SNN 基于脉冲的通信本质所固有的短载荷进一步加剧了这一瓶颈。具体而言，我们的特征刻画表明，在当前神经形态系统中，重复的地址传输在代表性负载中可占总流量的 49%。本文提出 UniSpike，一种软硬件协同设计，通过将发往同一核的脉冲聚合为单个紧凑数据包来消除地址冗余。UniSpike 实现了脉冲传输调度策略以支持高效的脉冲合并，并辅以用于运行时数据包组装与分发的专用硬件架构，以及一种最大化地址共享机会的目的地感知 SNN 划分算法。实验结果表明，平均而言 UniSpike 将流量减少 1.93 倍，相比 SOTA 设计实现 1.77 倍加速与 1.50 倍能效提升。
