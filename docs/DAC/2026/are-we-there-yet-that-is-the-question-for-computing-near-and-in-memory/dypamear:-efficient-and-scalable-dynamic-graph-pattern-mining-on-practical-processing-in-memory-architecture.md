Dypamear: Efficient and Scalable Dynamic Graph Pattern Mining on Practical Processing-in-Memory Architecture
Authors：
[Yi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7676833668777047982)，[Yu Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=427343)，[Deting Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=04660857733054714841)，[Chaoqiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=29313069671947244431)，[Haifeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=79163521860891548921)，[Xueqi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=77855308624011050141)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)

## 中文标题

DyPamear：面向实用存内处理架构的高效可扩展动态图模式挖掘

## 英文摘要

Dynamic Graph Pattern Mining (DGPM) has been widely applied in various domains. However, existing solutions still suffer from severe memory access bottlenecks due to the irregular and data-intensive nature of DGPM workloads. In this paper, we propose DyPamear, the first full-stack hardware-software co-designed system for accelerating DGPM on practical Processing-in-Memory (PIM) hardware. DyPamear is built atop UPMEM, an emerging commercially available PIM platform. To fully exploit UPMEM’s bandwidth and parallelism, DyPamear introduces a cross-layer design that integrates load-aware task distribution, data-driven asynchronous execution, and a degree-adaptive set intersection kernel to balance load and alleviate architectural constraints. Evaluations on real UPMEM hardware show that DyPamear achieves average speedups of 267.38×, 82.52×, and 8.78× over Cheetah, PimPam, and PSMiner, respectively, and scales nearly linearly to 20,480 DPUs.

## 中文摘要

动态图模式挖掘（DGPM）已在众多领域得到广泛应用。然而，由于 DGPM 负载具有不规则与数据密集的特性，现有方案仍受制于严重的内存访问瓶颈。本文提出 DyPamear，这是首个在实用存内处理（PIM）硬件上加速 DGPM 的全栈软硬件协同设计系统。DyPamear 构建于 UPMEM 之上，后者是一种新兴的商用 PIM 平台。为充分利用 UPMEM 的带宽与并行性，DyPamear 引入跨层设计，融合了负载感知的任务划分、数据驱动的异步执行，以及度数自适应的集合求交内核，从而均衡负载并缓解架构约束。在真实 UPMEM 硬件上的评测表明，DyPamear 相较于 Cheetah、PimPam 与 PSMiner 分别取得 267.38×、82.52× 与 8.78× 的平均加速，并可近线性扩展至 20,480 个 DPU。
