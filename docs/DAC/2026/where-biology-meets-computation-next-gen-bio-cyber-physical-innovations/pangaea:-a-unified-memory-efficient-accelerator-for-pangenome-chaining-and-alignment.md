Pangaea: A Unified Memory-Efficient Accelerator for Pangenome Chaining and Alignment
Authors：
[Shilin Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=0987704665240662004)，[Fangzhou Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=39855902917365320031)，[Amir Ahsaei](https://63dac.conference-program.com/?post_type=page&p=15&uid=15852202472703094221)，[Wei Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=578243)，[Hao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=8753587596308129276)

## 中文标题

Pangaea：面向泛基因组链化与比对的内存高效统一加速器

## 英文摘要

Pangenome graphs have emerged as a promising genome representation that combine many genomes into a graph, showing all possible genetic variants in a population. However, mapping DNA sequences to pangenome graphs involves multiple computation stages, from graph indexing to read alignment. Despite significant efforts, current frameworks optimize individual stages in isolation but overlook memory bottlenecks across the entire pipeline of sequence-to-graph mapping, where the intermediate data exchanged between stages contributes up to 86% of total DRAM access. To this end, we posit that the sequence-to-graph pipeline should be optimized as a whole, rather than in isolation, to effectively exploit intermediate data reuse across stages. We propose PanGaea, a novel accelerator that fuses the heterogeneous computing kernels of the sequence-to-graph pipeline, thereby reducing intermediate data exchange between memory-intensive stages and optimizing DRAM access. Specifically, we formulate a memory model for linear chaining, graph chaining, and wavefront alignment, and repurpose graph traversal techniques to partition pangenome graph with improved data locality and parallelism. In addition, we design a new accelerator architecture and dataflow mapping that dynamically support the diverse computation patterns of different sequence-to-graph stages. Compared to state-of-the-art ASIC designs, PanGaea delivers on average 1.47× higher throughput (bp/s), 1.73× better energy efficiency (bp/𝜇J) and 1.62× higher area efficiency (bp/s/mm2).

## 中文摘要

泛基因组图已成为一种有前景的基因组表示方式，它将多个基因组组合为一张图，展现群体中所有可能的遗传变异。然而，将 DNA 序列比对到泛基因组图涉及多个计算阶段，从图索引到 read 比对。尽管已有大量努力，当前框架仍孤立地优化各个阶段，忽视了整条序列到图比对流水线中的内存瓶颈——阶段之间交换的中间数据贡献了高达 86% 的总 DRAM 访问量。为此，我们认为序列到图流水线应作为整体而非孤立地进行优化，以有效利用跨阶段的中间数据重用。我们提出 PanGaea，一种新颖的加速器，它融合序列到图流水线的异构计算内核，从而减少内存密集型阶段之间的中间数据交换并优化 DRAM 访问。具体而言，我们为线性链化、图链化和波前比对建立了内存模型，并重新利用图遍历技术对泛基因组图进行划分，以改善数据局部性和并行性。此外，我们设计了一种新的加速器架构与数据流映射，能够动态支持不同序列到图阶段的多样化计算模式。与最先进的 ASIC 设计相比，PanGaea 平均提供 1.47× 更高的吞吐量（bp/s）、1.73× 更好的能效（bp/μJ）以及 1.62× 更高的面积效率（bp/s/mm²）。
