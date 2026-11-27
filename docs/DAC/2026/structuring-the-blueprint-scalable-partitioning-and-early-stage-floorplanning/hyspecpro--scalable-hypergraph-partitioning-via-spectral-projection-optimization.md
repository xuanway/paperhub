Hyspecpro: Scalable Hypergraph Partitioning via Spectral Projection Optimization
Authors：
[Rongjian Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314843)，[Zhuo Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=26257141429540576131)，[Haoxing Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=172643)

## 中文标题

HySpecPro：基于谱投影优化的可扩展超图划分

## 英文摘要

Modern VLSI designs comprise tens of billions of components, making scalable hypergraph partitioning critical for parallel and hierarchical optimization. Although multilevel partitioning remains the dominant paradigm, its coarsening stage can distort structural information—especially in hypergraphs with many high-degree hyperedges—leading to increased refinement overhead and limited scalability. Recent approaches incorporate spectral information to guide coarsening, but only in a heuristic manner, without directly optimizing the partitioning objectives. We introduce HySpecPro, a single-level hypergraph partitioner that performs end-to-end optimization in a spectral embedding space. HySpecPro constructs embeddings from a bipartite Laplacian and performs efficient projection-based search, supported by a fully GPU-accelerated implementation. Experiments show that HySpecPro delivers cut quality comparable to state-of-the-art multilevel methods while scaling linearly with the total hyperedge degree.

## 中文摘要

现代 VLSI 设计包含数百亿个元件，使得可扩展的超图划分对并行与层次化优化至关重要。尽管多层划分仍是主流范式，但其粗化阶段可能扭曲结构信息——尤其是在包含大量高度超边的超图中——从而导致细化开销增加与可扩展性受限。近期方法引入谱信息来引导粗化，但仅以启发式方式进行，并未直接优化划分目标。我们提出 HySpecPro，一个在谱嵌入空间中执行端到端优化的单层超图划分器。HySpecPro 从二分拉普拉斯矩阵构造嵌入，并执行高效的基于投影的搜索，且由全 GPU 加速实现予以支撑。实验表明，HySpecPro 的割质量可与最先进的多层方法相媲美，同时随超边总度线性扩展。
