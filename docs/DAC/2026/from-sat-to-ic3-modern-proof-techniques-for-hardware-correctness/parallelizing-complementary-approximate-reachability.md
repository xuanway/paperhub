Parallelizing Complementary Approximate Reachability
Authors：
[Runxuan Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=66434106349550358901)，[Geguang Pu](https://63dac.conference-program.com/?post_type=page&p=15&uid=318243)，[Jianwen Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=446243)，[Hongtai Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=90623592529889304201)，[Yechuan Xia](https://63dac.conference-program.com/?post_type=page&p=15&uid=4105626510341645338)，[Yi Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6529703879297340459)

## 中文标题

并行化互补近似可达性分析

## 英文摘要

Model checking, especially symbolic algorithms such as IC3/PDR, is a powerful verification technique but is increasingly constrained by single-threaded performance. Existing parallel model checking approaches either rely on redundant portfolio executions or suffer from scalability bottlenecks caused by centralized scheduling. We propose a new parallel paradigm for model checking based on fine-grained task decomposition and a decentralized Work-pulling architecture. A distributed concurrent task repository replaces the central coordinator, enabling worker threads to autonomously acquire tasks and naturally achieve dynamic load balancing. We present the framework design, analyze its parallel mechanisms, and evaluate its performance on representative benchmarks. Our approach achieves notable speedup and demonstrates effective scalability over serial execution.

## 中文摘要

模型检验，尤其是 IC3/PDR 等符号化算法，是一种强大的验证技术，但日益受限于单线程性能。现有的并行模型检验方法要么依赖冗余的 portfolio 式执行，要么因集中式调度而遭遇可扩展性瓶颈。我们提出一种新的并行模型检验范式，基于细粒度任务分解与去中心化的 work-pulling 架构。分布式并发任务仓库取代了中央协调器，使工作线程能够自主获取任务，并自然地实现动态负载均衡。我们给出了框架设计，分析了其并行机制，并在代表性基准上评测了其性能。我们的方法取得了显著加速，并相对串行执行展现出良好的可扩展性。

## 英文关键词

Formal Verification, Model Checking, Parallel Computing

## 中文关键词

形式验证、模型检验、并行计算
