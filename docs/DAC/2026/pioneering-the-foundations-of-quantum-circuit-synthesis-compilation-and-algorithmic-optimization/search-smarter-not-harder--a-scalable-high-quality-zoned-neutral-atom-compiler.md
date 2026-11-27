Search Smarter, Not Harder: A Scalable, High-Quality Zoned Neutral Atom Compiler
Authors：
[Yannick Stade](https://63dac.conference-program.com/?post_type=page&p=15&uid=624843)，[Lukas Burgholzer](https://63dac.conference-program.com/?post_type=page&p=15&uid=4361888449809363316)，[Robert Wille](https://63dac.conference-program.com/?post_type=page&p=15&uid=487643)

## 中文标题

更聪明而非更费力地搜索：一种可扩展的高质量分区中性原子编译器

## 英文摘要

Zoned neutral atom architectures are emerging as a promising platform for large-scale quantum computing. Their growing scale, however, creates a critical need for efficient and automated compilation solutions. Yet, existing methods fail to scale to the thousands of qubits these devices promise. State-of-the-art compilers, in particular, suffer from immense memory requirements that limit them to small-scale problems. This work proposes a scalable compilation strategy that “searches smarter, not harder”. We introduce Iterative Diving Search (IDS), a goal-directed search algorithm that avoids the memory issues of previous methods, and relaxed routing, an optimization to mitigate atom rearrangement overhead. Our evaluation confirms that this approach compiles circuits with thousands of qubits and, in addition, even reduces rearrangement overhead by 28.1% on average. The complete code is publicly available in open-source as part of the Munich Quantum Toolkit (MQT) at https://github.com/munich-quantum-toolkit/qmap.

## 中文摘要

分区中性原子架构正成为大规模量子计算颇具前景的平台。然而，其规模的不断增长对高效、自动化的编译方案提出了迫切需求。现有方法无法扩展到这类设备所承诺的数千量子比特规模。特别是最先进的编译器受制于巨大的内存需求，只能处理小规模问题。本工作提出一种“更聪明而非更费力”的可扩展编译策略。我们引入迭代下潜搜索（IDS），一种目标导向的搜索算法，避免了先前方法的内存问题；并提出松弛路由，一种用于缓解原子重排开销的优化。我们的评估证实，该方法能够编译包含数千量子比特的线路，并且还将重排开销平均降低 28.1%。完整代码已作为慕尼黑量子工具包（MQT）的一部分在 https://github.com/munich-quantum-toolkit/qmap 上开源发布。

## 英文关键词

quantum computing, optimizing compilers, rydberg atoms, ultra-cold atoms, routing

## 中文关键词

量子计算、优化编译器、里德堡原子、超冷原子、路由
