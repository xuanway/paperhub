Per Flow Asynchronous Traffic Shaping in Time Sensitive Networking
Authors：
[Wenxue Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4606982133344778355)，[Tong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3799124989356582886)，[Wanchun Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7674128709140495297)，[Wufan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7321422979631777154)，[Zhen Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=090514408298262433)，[Fengyuan Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=1398029769030912563)

## 中文标题

时间敏感网络中的每流异步流量整形

## 英文摘要

Asynchronous Traffic Shaping (ATS) bounds end-to-end delay in Time-Sensitive Networking (TSN) without relying on global synchronization, but its per-group queuing introduces inter-flow interference that causes large delay jitter for time-critical flows. To address this limitation, we present PFATS, a novel per-flow asynchronous traffic shaping architecture that integrates a per-flow frame eligibility time calculator, per-flow queues, and a Synchronous Shift Register Matrix (SSRM) scheduler. We implement PFATS on an FPGA-based TSN switch, and it supports 192 per-flow queues with only 7.14% additional on-chip memory usage compared to conventional ATS. In realistic TSN scenarios, PFATS achieves microsecond-level end-to-end delays and bounds delay jitter to within 5 µs, while maintaining high throughput.

## 中文摘要

异步流量整形（ATS）无需依赖全局同步即可为时间敏感网络（TSN）提供端到端时延上界，但其按组排队会引入流间干扰，导致时间关键流产生较大的时延抖动。针对这一局限，我们提出 PFATS，一种新颖的每流异步流量整形架构，集成了每流帧资格时间计算器、每流队列以及同步移位寄存器矩阵（SSRM）调度器。我们在基于 FPGA 的 TSN 交换机上实现了 PFATS，与传统 ATS 相比，仅增加 7.14% 的片上存储占用即可支持 192 个每流队列。在真实 TSN 场景中，PFATS 实现微秒级端到端时延，将时延抖动限制在 5 µs 以内，同时保持高吞吐。

## 英文关键词

Time-Sensitive Networking, Asynchronous Traffic Shaping, Per-Flow Queues, Shared Buffer

## 中文关键词

时间敏感网络、异步流量整形、每流队列、共享缓存
