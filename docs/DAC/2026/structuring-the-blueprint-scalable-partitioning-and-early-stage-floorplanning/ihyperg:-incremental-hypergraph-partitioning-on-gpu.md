Ihyperg: Incremental Hypergraph Partitioning on GPU
Authors：
[Wan Luan Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=31529313222750401561)，[Aditya Das Sarma](https://63dac.conference-program.com/?post_type=page&p=15&uid=7726790463313317363)，[Che Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3289325791803723644)，[Chih-Chun Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=822843)，[Tsung-Wei Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=026843)

## 中文标题

iHyperG：GPU 上的增量式超图划分

## 英文摘要

Recent advances in GPU-accelerated hypergraph partitioning have achieved substantial performance gains but remain limited to full partitioning. In particular, the lack of support for incrementality is a critical limitation for use in many CAD applications, where circuit hypergraphs iteratively undergo incremental modifications as part of optimization loops. To overcome this limitation, we present iHyperG, the first GPU-parallel incremental 𝑘-way hypergraph partitioner. iHyperG introduces a scalable delta-based hypergraph data structure for efficient incremental modifications on a GPU, along with an effective incremental partitioning algorithm that rebalances partitions in a single pass and refines only cut-critical vertices. Experimental results show that iHyperG achieves average speedups of 190× for modification and 83× for partitioning over a state-of-the-art GPU-parallel hypergraph partitioner, while maintaining comparable partitioning quality.

## 中文摘要

近期 GPU 加速超图划分的进展已带来显著的性能提升，但仍局限于全量划分。特别是，对增量性的支持缺失是其在众多 CAD 应用中使用的关键限制，在这些应用中电路超图会作为优化循环的一部分被迭代地增量修改。为克服这一限制，我们提出 iHyperG，首个 GPU 并行增量式 k 路超图划分器。iHyperG 引入了一种可扩展的基于增量的超图数据结构，以在 GPU 上高效地进行增量修改，并提出了一种有效的增量划分算法，可在单趟中重新平衡分区，并仅对割关键的顶点进行细化。实验结果表明，与最先进的 GPU 并行超图划分器相比，iHyperG 在修改上平均加速 190 倍、在划分上平均加速 83 倍，同时保持相当的划分质量。
