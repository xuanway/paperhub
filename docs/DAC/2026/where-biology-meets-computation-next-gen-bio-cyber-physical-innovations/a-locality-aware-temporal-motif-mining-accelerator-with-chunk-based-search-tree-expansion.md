A Locality-Aware Temporal Motif Mining Accelerator with Chunk-Based Search Tree Expansion
Authors：
[Yinbo Hou](https://63dac.conference-program.com/?post_type=page&p=15&uid=03705908007634405901)，[Hao Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=12298543507376204381)，[Jin Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0207233704685139242)，[Yu Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=352543)，[Yiling Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=34286353087662208061)，[Hui Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3656444361754319641)，[longlong lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=23483355836215854951)，[Wenbin Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=53184880136571815081)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)

## 中文标题

一种基于块式搜索树扩展的局部性感知时序模体挖掘加速器

## 英文摘要

Mining temporal motifs in temporal graphs is essential for many critical applications. Despite several software/hardware temporal motif mining solutions have been proposed, they still suffer from substantial redundant and irregular off-chip communications due to misaligned search tree expansions across different motif matching tasks. In this work, we observe that different tasks traverse the same temporal graph edges in strict chronological order, exhibiting strong data locality among these tasks. Motivated by this insight, we propose LTMiner, a locality-aware hardware accelerator designed to efficiently handle temporal motif mining. Specifically, LTMiner proposes a novel chunk-based search tree expansion mechanism into the accelerator design to align the graph traversals of different tasks at the granularity of data chunks, substantially boosting the data locality among these tasks for lower data access cost. The results show that LTMiner gains 1.1×–652.6×, 1.8×–70.3× speedups and 3.9×–2050.9×, 1.2×–17.3× energy savings compared to the cutting-edge software and hardware solutions, respectively.

## 中文摘要

时序图中的时序模体挖掘对许多关键应用至关重要。尽管已有若干软件与硬件时序模体挖掘方案被提出，但由于不同模体匹配任务之间的搜索树扩展彼此未对齐，它们仍会产生大量冗余且不规则的片外通信。在本工作中，我们观察到不同任务以严格的时间顺序遍历相同的时序图边，因而这些任务之间表现出很强的数据局部性。受此启发，我们提出 LTMiner，一种旨在高效处理时序模体挖掘的局部性感知硬件加速器。具体而言，LTMiner 在加速器设计中引入一种新颖的基于块的搜索树扩展机制，以数据块为粒度对齐不同任务的图遍历，从而显著提升这些任务间的数据局部性，降低数据访问开销。结果表明，与最先进的软件和硬件方案相比，LTMiner 分别获得 1.1×–652.6×、1.8×–70.3× 的加速，以及 3.9×–2050.9×、1.2×–17.3× 的能耗节省。
