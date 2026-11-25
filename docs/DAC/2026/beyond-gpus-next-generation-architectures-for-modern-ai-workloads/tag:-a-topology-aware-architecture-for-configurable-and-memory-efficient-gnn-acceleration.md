TAG: A Topology-Aware Architecture for Configurable and Memory-Efficient GNN Acceleration
Authors：
[Ruoheng Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=26632856850324413081)，[Yichen Ouyang](https://63dac.conference-program.com/?post_type=page&p=15&uid=89498276239292641161)，[Wenneng Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=16739357907061263711)，[Tianji Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=74707823272469307151)，[Yangyi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0075795651172142879)，[Zhiyue Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=69726620015946080811)，[Zhiyong Lai](https://63dac.conference-program.com/?post_type=page&p=15&uid=14006577480732014431)，[Lei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0987755731675252973)，[Fengwei An](https://63dac.conference-program.com/?post_type=page&p=15&uid=45482577157775868271)

## 中文标题

TAG：面向可配置且存储高效的 GNN 加速的拓扑感知架构

## 英文摘要

Graph Neural Networks (GNNs) offer powerful graph-structured data modeling capabilities, yet their acceleration is challenging. Rigid hardware parallelism struggles to accommodate algorithmic diversity and the sparse, irregular topology inherent to GNNs. To resolve this conflict, we propose TAG, a topology-aware GNN accelerator that achieves high performance through synergistic innovations at three levels: dataflow, scheduling, and memory hierarchy. For algorithmic diversity, we employ a configurable, topology-driven dataflow that is aware of both algorithmic needs and graph structure. To mitigate irregularity, a contention-aware scheduler orchestrates irregular memory accesses by reordering them into a conflict-free stream. Furthermore, an algorithm-architecture co-designed memory hierarchy, combined with a coarse-to-fine graph partitioning algorithm, maximizes data reuse from sparse graphs and significantly minimizes off-chip traffic. Evaluations demonstrate that TAG achieves an average of 3.22× speedup and 3.04× energy efficiency over state-of-the-art GNN accelerators.

## 中文摘要

图神经网络（GNN）提供了强大的图结构数据建模能力，但其加速颇具挑战。刚性的硬件并行难以适应 GNN 固有的算法多样性以及稀疏、不规则的拓扑结构。为化解这一矛盾，我们提出 TAG，一种拓扑感知的 GNN 加速器，通过数据流、调度与存储层次三个层面的协同创新实现高性能。针对算法多样性，我们采用可配置、拓扑驱动的数据流，同时感知算法需求与图结构。为缓解不规则性，一种冲突感知调度器将不规则内存访问重排序为无冲突的访问流。此外，算法-架构协同设计的存储层次结合由粗到细的图划分算法，最大化了稀疏图的数据复用，并显著减少了片外访存。评估表明，TAG 相较于最先进的 GNN 加速器平均实现 3.22 倍加速和 3.04 倍的能效提升。
