Duplication-Aware Retiming and Cell Interface Redesign for Superconductor Circuit Minimization
Authors：
[Panagiotis Papanikolaou](https://63dac.conference-program.com/?post_type=page&p=15&uid=02625032514813632111)，[Alex Vanasse](https://63dac.conference-program.com/?post_type=page&p=15&uid=5487075462165166133)，[Haoran Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=26286204325891086111)，[Georgios Tzimpragos](https://63dac.conference-program.com/?post_type=page&p=15&uid=39707011049484500151)，[Jennifer Volk](https://63dac.conference-program.com/?post_type=page&p=15&uid=1193267610241303399)

## 中文标题

面向超导电路最小化的复制感知重定时与单元接口重构

## 英文摘要

Superconductor electronics have increasingly shifted away from RSFQ and its variants toward logic families that eliminate explicit gate-level clocking. While this transition enables simpler circuits and more efficient architectures, it also introduces an implicit reliance on dual-rail codes, resulting in inherent gate duplication. This work presents a duplication-aware retiming methodology for Josephson junction (JJ) count minimization, co-optimizing register placement and polarity assignment. The approach applies beyond SFQ to any monotonic circuit. We further identify cell interfaces—specifically, interconnect drivers, receivers, and fanout (FO) elements—as dominant contributors to JJ count in each cell. A new amplifier design is introduced to reduce these costs, integrated within existing SFQ cells, experimentally verified, and characterized to form a new SFQ cell library. Our results demonstrate a 63-71% JJ count reduction in single-cycle implementations and 4166% reduction in multi-cycle implementations compared to the prior state-of-the-art. The latter establishes a new Pareto frontier, achieving both shorter critical paths and lower JJ counts than the best-to-date single-cycle implementations.

## 中文摘要

超导电子学正日益从 RSFQ 及其变体转向消除显式门级时钟的逻辑家族。这一转变虽然带来了更简单的电路和更高效的架构，但也引入了对双轨码的隐式依赖，导致固有的门复制。本文提出一种复制感知的重定时方法，用于最小化约瑟夫森结（Josephson junction，JJ）数量，并协同优化寄存器放置与极性分配。该方法不仅适用于 SFQ，也适用于任何单调电路。我们进一步指出，单元接口——具体而言即互连驱动器、接收器与扇出（FO）元件——是每个单元中 JJ 数量的主要贡献者。本文提出一种新的放大器设计以降低这些开销，将其集成到现有 SFQ 单元中，经实验验证与表征后形成新的 SFQ 单元库。结果表明，与先前的最先进工作相比，我们在单周期实现中实现了 63–71% 的 JJ 数量缩减，在多周期实现中实现了 41–66% 的缩减。后者建立了新的 Pareto 前沿，相比迄今最佳的单周期实现，同时获得了更短的关键路径与更低的 JJ 数量。
