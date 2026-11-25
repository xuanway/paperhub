ARTEMIS: Adaptive RL Test-Time Ensemble for Model Inference in SSD Testing
Authors：
[Kyunghwan Son](https://63dac.conference-program.com/?post_type=page&p=15&uid=7077280282847528875)，[Hyukil Kwon](https://63dac.conference-program.com/?post_type=page&p=15&uid=2294171045744301473)，[Nayeon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=81868835770121983421)，[Sohyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=1874723234698781094)，[Hyelyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=4883666895521331695)，[Sunghee Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=138743)，[Jinje Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=0920486985915778001)，[Hyungdal Kwon](https://63dac.conference-program.com/?post_type=page&p=15&uid=0778309343232650599)，[Yoon Hyeok Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=9480871045561919779)

## 中文标题

ARTEMIS：面向 SSD 测试中模型推理的自适应强化学习测试时集成

## 英文摘要

Solid-State Drives (SSDs) now power data centers, high-performance computing, and artifical intelligence workloads, but the increasing complexity of modern SSD controllers has surpassed the capabilities of traditional rule-based verification, necessitating scalable, data-driven testing methods. In this paper, we present ARTEMIS, a reinforcement learning (RL)-based framework for automatic SSD test case (TC) generation that operates directly on commercial devices. Our contributions are threefold. First, we formulate a novel RL problem, enabling seamless deployment across heterogeneous commercial products without requiring any device-specific customization. Second, to cope with the highly dynamic and non-stationary operating environments of SSDs, we introduce an ensemble-based inference mechanism that aggregates policies learned under diverse workload distributions, thereby improving generalization and robustness. Third, we validate the approach on two representative stress-testing tasks: Meta and User Garbage Collection. We show that the RL-driven tester discovers high-impact TCs that trigger critical blocking garbage collection events more frequently than conventional methods in diverse tasks.

## 中文摘要

固态硬盘（SSD）如今支撑着数据中心、高性能计算和人工智能负载，但现代 SSD 控制器日益增加的复杂度已超出传统基于规则的验证能力，因而需要可扩展的数据驱动测试方法。本文提出 ARTEMIS，一种基于强化学习（RL）的 SSD 测试用例（TC）自动生成框架，可直接在商用设备上运行。本文贡献有三：其一，我们构建了一种新颖的 RL 问题形式，使其无需任何针对特定设备的定制即可无缝部署于异构商用产品；其二，为应对 SSD 高度动态且非平稳的运行环境，我们引入基于集成的推理机制，聚合在多种负载分布下学习到的策略，从而提升泛化性与鲁棒性；其三，我们在两项具有代表性的压力测试任务——Meta 垃圾回收与 User 垃圾回收——上验证了该方法。结果表明，RL 驱动的测试器能够发现高影响力的测试用例，在不同任务中比传统方法更频繁地触发关键的阻塞式垃圾回收事件。

## 英文关键词

Solid-State Drive (SSD), Reinforcement Learning, Automated Testing, Test-time Ensemble

## 中文关键词

固态硬盘（SSD）、强化学习、自动化测试、测试时集成
