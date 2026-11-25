Activity-Aware Partitioning for Effective Multi-Threaded Event-Driven RTL Simulation
Authors：
[Kexing Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=32775740145036339851)，[Youwei Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=87467546929157235041)，[Yibo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=227143)，[Weikang Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=828143)，[Pengpeng Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=16680494305368678571)，[Yun (Eric) Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=124143)

## 中文标题

面向高效多线程事件驱动 RTL 仿真的活动度感知划分

## 英文摘要

Register-transfer-level (RTL) simulation is commonly accelerated through multi-threading or event-driven techniques. Ideally, combining them should achieve both high utilization and high efficiency. However, severe load imbalance arises: in event-driven execution, circuit regions exhibit highly uneven activity, leaving many threads idle with very low utilization. Existing multi-threaded RTL partitioning models often optimize for full-cycle execution while ignoring the dynamic activity variation that dominates event-driven workloads. We present P2SIM, a multi-threaded event-driven RTL simulator that incorporates runtime activity information into its partitioning model. Our model augments hypergraph weights with measured activity frequency and correlation, which is efficiently estimated through a lightweight MinHash profiler. By aligning thread assignment with true activity patterns, P2SIM substantially reduces idle time and improves utilization. Across experiments on large benchmarks, P2SIM achieves simulation speeds of 200-400 kHz and up to 8.9× speedup over Verilator.

## 中文摘要

寄存器传输级（RTL）仿真通常通过多线程或事件驱动技术加以加速。理想情况下，将两者结合应能同时实现高利用率与高效率。然而，严重的负载不均衡随之出现：在事件驱动执行中，电路各区域的活动度极不均衡，导致许多线程空闲、利用率很低。现有多线程 RTL 划分模型往往以全周期执行为优化目标，而忽略了主导事件驱动负载的动态活动变化。我们提出 P2SIM，一种将运行时活动信息纳入划分模型的多线程事件驱动 RTL 仿真器。该模型用实测的活动频率与相关性增强超图权重，并通过轻量级 MinHash 剖析器高效估计这些信息。通过使线程分配与真实活动模式相匹配，P2SIM 大幅减少空闲时间并提升利用率。在大型基准上的实验表明，P2SIM 的仿真速度达到 200–400 kHz，相较 Verilator 最高加速 8.9 倍。
