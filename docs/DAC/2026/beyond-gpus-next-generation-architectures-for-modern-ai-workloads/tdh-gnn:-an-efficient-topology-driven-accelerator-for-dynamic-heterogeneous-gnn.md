TDH-GNN: An Efficient Topology-Driven Accelerator for Dynamic Heterogeneous GNN
Authors：
[Hui Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3656444361754319641)，[Wei Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=178243)，[Ligang He](https://63dac.conference-program.com/?post_type=page&p=15&uid=1529673301716819203)，[Jin Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0207233704685139242)，[Yu Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=352543)，[Zixiao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=35216117385569938501)

## 中文标题

TDH-GNN：面向动态异构图 GNN 的高效拓扑驱动加速器

## 英文摘要

Dynamic Heterogeneous Graph Neural Networks (DHGNNs) capture evolving structural and semantic information through metapath learning over dynamic heterogeneous graphs. However, existing solutions suffer from redundant metapath matching and excessive off-chip communication. To address these inefficiencies, we present TDH-GNN, a topology-driven accelerator for high-performance DHGNN inference. TDH-GNN introduces a hyperedge-centric incremental execution scheme, in which hyperedges encode dependencies among metapath instances to enable incremental metapath updates and eliminate redundant matching and computation. It also caches aggregated features of high-frequency edges to improve memory bandwidth efficiency. Implemented on a Xilinx Alveo U280 FPGA, TDH-GNN achieves average speedups of 143.5x and 42.9x, and average energy savings of 189.2x and 55.8x, over state-of-the-art DHGNN software systems on an Intel CPU and an A100 GPU, respectively. Compared with leading HGNN accelerators, TDH-GNN further delivers average speedups of 4.3x and 2.8x, together with energy savings of 5.9x and 3.7x.

## 中文摘要

动态异构图神经网络（DHGNN）通过在动态异构图上进行元路径学习，捕获不断演化的结构与语义信息。然而，现有方案存在元路径匹配冗余和片外通信过多的问题。为解决这些低效之处，我们提出 TDH-GNN，一种面向高性能 DHGNN 推理的拓扑驱动加速器。TDH-GNN 引入以超边为中心的增量执行方案，其中超边编码元路径实例之间的依赖关系，从而支持增量式元路径更新，并消除冗余的匹配与计算。它还会缓存高频边的聚合特征，以提升内存带宽利用率。TDH-GNN 在 Xilinx Alveo U280 FPGA 上实现，相较于运行在 Intel CPU 和 A100 GPU 上的最先进 DHGNN 软件系统，平均分别取得 143.5 倍和 42.9 倍的加速，以及 189.2 倍和 55.8 倍的能耗节省。与领先的 HGNN 加速器相比，TDH-GNN 还进一步实现平均 4.3 倍和 2.8 倍的加速，以及 5.9 倍和 3.7 倍的能耗节省。
