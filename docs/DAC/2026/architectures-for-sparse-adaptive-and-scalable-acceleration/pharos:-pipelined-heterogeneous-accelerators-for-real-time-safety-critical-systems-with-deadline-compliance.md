PHAROS: Pipelined Heterogeneous Accelerators for Real-Time Safety-Critical Systems With Deadline Compliance
Authors：
[Shixin Ji](https://63dac.conference-program.com/?post_type=page&p=15&uid=23773291736995867371)，[Jinming Zhuang](https://63dac.conference-program.com/?post_type=page&p=15&uid=46754897122762575931)，[Sarah Schultz](https://63dac.conference-program.com/?post_type=page&p=15&uid=77897386372090744871)，[Zhuoping Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0190404572782304487)，[Xingzhen Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=63463982556895264651)，[Zheng Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=655143)，[Alex Jones](https://63dac.conference-program.com/?post_type=page&p=15&uid=6012585033674335928)，[Yihui Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=08379597090444027131)，[Peipei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=621843)

## 中文标题

PHAROS：面向截止时间合规的实时安全关键系统的流水线化异构加速器

## 英文摘要

Spatially partitioned heterogeneous accelerators (HAs) are increasingly adopted in embedded systems for their performance and flexibility. Yet most existing HA design frameworks optimize primarily for throughput or quality-of-service (QoS) metrics. They often overlook safety-critical real-time requirements, including hardware support for predictable execution, real-time-aware design space exploration (DSE), and rigorous schedulability analysis. These requirements are essential in safety-critical applications such as smart transportation, where schedulability guarantees directly affect system safety. To address this gap, we present PHAROS, a real-time-centric HA design framework. PHAROS introduces preemption mechanisms and scheduler designs for spatially partitioned HAs under first-in-first-out (FIFO) and earliest-deadline-first (EDF) policies. Leveraging modern real-time theory, we further develop a soft real-time (SRT) schedulability-oriented DSE with objectives and constraints tailored to SRT-schedulability. Through comprehensive modeling, analysis, and evaluation across diverse applications, we show that PHAROS’s schedulability-oriented DSE discovers more feasible configurations for a broader range of task sets than throughput-oriented DSE baselines, while delivering improved realtime performance. We also provide response-time analyses for the supported scheduling algorithms.

## 中文摘要

空间划分的异构加速器（HA）因其性能与灵活性而日益被嵌入式系统所采用。然而，现有大多数 HA 设计框架主要以吞吐率或服务质量（QoS）指标为优化目标，往往忽略了安全关键的实时需求，包括对可预测执行的硬件支持、实时感知的设计空间探索（DSE）以及严格的实时可调度性分析。这些需求在智能交通等安全关键应用中至关重要，因为可调度性保证直接影响系统安全。为弥补这一空白，我们提出 PHAROS，一个以实时性为中心的 HA 设计框架。PHAROS 针对空间划分的 HA，在先进先出（FIFO）和最早截止时间优先（EDF）策略下引入了抢占机制与调度器设计。借助现代实时理论，我们进一步开发了面向软实时（SRT）可调度性的 DSE，其目标与约束均针对 SRT 可调度性而定制。通过在多种应用上开展全面的建模、分析与评估，我们表明 PHAROS 面向可调度性的 DSE 相比面向吞吐率的 DSE 基线，能够为更广泛的任务集发现更多可行配置，同时提供更优的实时性能。我们还给出了所支持调度算法的响应时间分析。
