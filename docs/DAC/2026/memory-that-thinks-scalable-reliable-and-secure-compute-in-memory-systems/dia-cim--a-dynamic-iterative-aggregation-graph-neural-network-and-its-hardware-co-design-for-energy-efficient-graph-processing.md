DIA-CIM: A Dynamic Iterative Aggregation Graph Neural Network and Its Hardware Co-Design for Energy-Efficient Graph Processing
Authors：
[Zhaoyang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=01227501524630586601)，[Tianhao Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0982315325103678015)，[Defa Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8404462126916386327)，[yingxuan zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=77437597867770053301)，[Xiaodong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=5645812795333309484)，[Yan Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=6854138202407510315)，[Yang Jun](https://63dac.conference-program.com/?post_type=page&p=15&uid=6386049648875323069)，[Xin Si](https://63dac.conference-program.com/?post_type=page&p=15&uid=06525473388796445)

## 中文标题

DIA-CIM：一种动态迭代聚合图神经网络及其面向高能效图处理的硬件协同设计

## 英文摘要

Graph neural networks (GNNs) are increasingly deployed on large, sparse graphs with growing aggregation complexity and precision demands, which makes data movement and on-chip storage the dominant bottlenecks for conventional GPU-and accelerator-based solutions. This work proposes a Dynamic Iterative Aggregation GNN (DIA-GNN) and a co-designed Computing-in-Memory macro, DIA-CIM, to jointly address these challenges from algorithm and hardware levels. DIA-GNN replaces multi-layer, layer-synchronous aggregation with a few intra-layer, row-sequential iterations that reuse the most recent neighbor features in a Gauss–Seidel–like manner. This approach expands the receptive field with fewer layers and parameters, reducing computation and memory accesses by over 70% while maintaining accuracy on benchmarks such as Cora, CiteSeer, and PubMed. To efficiently support this dataflow, DIA-CIM is a 28 nm, 768 kb digital CIM macro that integrates a CSR(Compressed Sparse Row)-driven output-stationary dataflow, a sparsity-priority BF16 MAC pipeline exploiting both structural and bit-level sparsity, and a refresh-aware eDRAM array with in-place write-back and mantissa sparsification. Fabricated in TSMC 28 nm CMOS, DIA-CIM achieves a peak energy efficiency of 60.01 TFLOPS/W and an area efficiency of 107–272 GFLOPS/mm2. When executing DIA-GNN workloads, it provides up to 83895× energy reduction and 6350× speedup over a CPU baseline, and improves energy efficiency by 3.56× with 2.32× lower latency compared to prior GNN accelerators, demonstrating the effectiveness of asynchronous in-memory aggregation for next-generation graph intelligence processors.

## 中文摘要

图神经网络（GNN）越来越多地部署于大规模稀疏图上，聚合复杂度与精度需求不断增长，使数据搬运与片上存储成为传统 GPU 及基于加速器方案的主要瓶颈。本文提出动态迭代聚合 GNN（DIA-GNN）与协同设计的存内计算宏单元 DIA-CIM，从算法与硬件两个层面共同应对上述挑战。DIA-GNN 以少量层内、行序迭代替代多层、层同步聚合，以类 Gauss–Seidel 的方式复用最新的邻居特征。该方法以更少的层数与参数扩展感受野，在 Cora、CiteSeer 与 PubMed 等基准上保持精度的同时将计算与访存减少 70% 以上。为高效支撑该数据流，DIA-CIM 是一个 28 nm、768 kb 的数字存内计算宏单元，集成了 CSR（压缩稀疏行）驱动的输出驻留数据流、同时利用结构稀疏性与位级稀疏性的稀疏优先 BF16 MAC 流水线，以及支持原地写回与尾数稀疏化的刷新感知 eDRAM 阵列。DIA-CIM 在 TSMC 28 nm CMOS 工艺下流片，峰值能效达 60.01 TFLOPS/W，面积效率为 107–272 GFLOPS/mm2。在执行 DIA-GNN 负载时，相较 CPU 基线可获得最高 83895 倍的能耗降低与 6350 倍的加速；与已有 GNN 加速器相比，能效提升 3.56 倍、延迟降低 2.32 倍，验证了异步存内聚合对下一代图智能处理器的有效性。

## 英文关键词

Graph Neural Network Acceleration; Dynamic Iterative Aggregation; Computing-in-Memory (CIM) Macro

## 中文关键词

图神经网络加速、动态迭代聚合、存内计算（CIM）宏单元
