PRS: An Efficient Parallel SAT Framework
Authors：
[Zhihan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7689398188756899571)，[Xindi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=60649551734012876551)，[Yuhang Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=7538889429976925601)，[Congyi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=75318354658300780171)，[Shaowei Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=8937909084464565096)

## 中文标题

PRS：一种高效的并行 SAT 框架

## 英文摘要

The propositional Satisfiability (SAT) problem is fundamental to many applications in Electronic Design Automation (EDA). This paper presents PRS, an efficient and comprehensive parallel SAT framework. We introduce two key techniques to enhance solver performance. The first is a lightweight preprocessing method called Resolution Checking, which efficiently simplifies circuit-encoded CNFs. The second is a new hybrid diversification strategy that combines a Regular Shifting method for the initial branching order with a parallel local search to generate diverse initial variable phases. PRS also supports extensive preprocessing, dynamic clause sharing, reproducible parallel solving, and parallel proof generation. Extensive experiments on the SAT Competition 2025 (SC25) benchmark demonstrate the effectiveness and scalability of our framework: PRS outperforms the SC25 Parallel-Track winner MallobSAT by solving 12 more instances with an 11.4% better PAR2 score, while also achieving a 4.7× speedup on 64 cores.

## 中文摘要

命题可满足性（SAT）问题是电子设计自动化（EDA）中许多应用的基础。本文提出 PRS，一个高效且全面的并行 SAT 框架。我们引入两项关键技术以提升求解器性能。第一是一种称为归结检查（Resolution Checking）的轻量级预处理方法，可高效简化电路编码的 CNF。第二是一种新的混合多样化策略，将用于初始分支顺序的正则移位（Regular Shifting）方法与并行局部搜索相结合，以生成多样化的初始变量相位。PRS 还支持广泛的预处理、动态子句共享、可复现的并行求解以及并行证明生成。在 SAT Competition 2025（SC25）基准上的大量实验证明了我们框架的有效性与可扩展性：PRS 优于 SC25 并行赛道冠军 MallobSAT，多求解 12 个实例，PAR2 得分好 11.4%，并在 64 核上实现 4.7 倍加速。

## 英文关键词

SAT, Parallel, Regular shifting, Preprocessing, Resolution checking

## 中文关键词

SAT、并行、正则移位、预处理、归结检查
