Impart: Integration of Memetic Operations into Multi-Level Framework for Large-k-Way Hypergraph Partitioning
Authors：
[Yugao Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7474132413567388679)，[Zhicheng Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1701010475988725104)，[Shang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888404795171209433)，[Mengming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=69110175844035149381)，[Jing Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=97987884326682291051)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

IMPart：将模因操作集成到多层框架以实现大规模 k 路超图划分

## 英文摘要

The problem of 𝑘-way hypergraph partitioning is fundamental with significant applications in various fields, including VLSI design and scientific computing. State-of-the-art hypergraph partitioners commonly employ a multi-level framework encompassing coarsening, initial partitioning, uncoarsening, and refinement phases. However, many existing methods do not scale well to problems requiring a large number of partitions (i.e., large 𝑘). In pursuit of exceptionally high solution quality, existing memetic approaches often execute their two key operations, recombination and mutation, by invoking separate, standalone multi-level partitioners. This design choice, however, renders them significantly more time-consuming than standard multi-level partitioners. To make such memetic approaches more practical, we propose an advanced memetic framework, IMPart, which introduces novel recombination and mutation operators and integrates them directly into the uncoarsening phase of a single multi-level framework. This transforms the local searches of different granularities in the traditional multi-level framework into a sophisticated, collaborative search. Experimental results on multiple standard benchmarks demonstrate our framework more effectively escapes local optima and explores the global solution space for higher-quality solutions, substantially outperforming all existing hypergraph partitioners for large-𝑘-way hypergraph partitioning. Our framework highlights a new paradigm for the development of advanced hypergraph partitioners.

## 中文摘要

k 路超图划分问题具有基础性地位，在 VLSI 设计与科学计算等诸多领域有着重要应用。最先进的超图划分器通常采用包含粗化、初始划分、解粗化与细化阶段的多层框架。然而，许多现有方法在需要大量分区（即大 k）的问题上难以扩展。为追求极高的解质量，现有模因方法往往通过调用独立的、单独的多层划分器来执行其两个关键操作——重组与变异。然而，这一设计选择使其耗时显著高于标准多层划分器。为使此类模因方法更具实用性，我们提出一种先进的模因框架 IMPart，它引入了新颖的重组与变异算子，并将其直接集成到单一多层框架的解粗化阶段。这将传统多层框架中不同粒度的局部搜索转变为一种复杂的协同搜索。在多个标准基准上的实验结果表明，我们的框架能够更有效地跳出局部最优并探索全局解空间以获得更高质量的解，在大 k 路超图划分上大幅优于所有现有超图划分器。我们的框架为先进超图划分器的开发凸显了一种新范式。
