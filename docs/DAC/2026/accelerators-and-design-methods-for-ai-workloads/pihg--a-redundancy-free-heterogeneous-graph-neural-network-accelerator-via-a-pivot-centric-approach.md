PiHG: A Redundancy-Free Heterogeneous Graph Neural Network Accelerator via a Pivot-Centric Approach
Authors：
[Qiyuan Niu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8753923921714171393)，[Yu Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=352543)，[Lin Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=78020243762194525811)，[Zhongtian Long](https://63dac.conference-program.com/?post_type=page&p=15&uid=19546384631662087951)，[Ruida Xin](https://63dac.conference-program.com/?post_type=page&p=15&uid=4484700275928158581)，[Yutao Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6547220790885260596)，[Jin Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0207233704685139242)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)

## 中文标题

PiHG：一种基于枢轴中心方法的无冗余异构图神经网络加速器

## 英文摘要

Heterogeneous Graph Neural Networks (HGNNs) commonly utilize predefined sequences of vertex and edge types (i.e., metapaths) to model composite relations in real-world graphs. Although several solutions have been proposed to support HGNNs, they adopt a source-centric approach that processes metapath instances sharing the same source vertex, while the vertices and edges which are shared by different metapath instances and also beyond the first hop of the same source vertex may be repeatedly processed, incurring irregular memory accesses and redundant edge computations. In this work, we observe that HGNN inference exhibits substantial vertex and edge overlaps across metapath instances, and the metapaths sharing a common pivot vertex (i.e., the center vertex bridging multiple metapaths) exhibit strong spatial similarity that effectively captures these overlaps. Based on these observations, we propose a pivot-centric accelerator named PiHG to effectively support HGNN inference. Specifically, PiHG introduces a novel pivot-centric execution model into accelerator design to concentrate feature accesses and computations around pivot vertices, which enables reusing the feature vectors of overlapped vertices and edges across metapaths and thus eliminating redundant computations and reducing irregular off-chip memory accesses. Experimental results show that, compared with the state-of-the-art software and hardware solutions, PiHG achieves 21.4×, 3.8× speedups and 25.6×, 4.1× energy savings on average, respectively.

## 中文摘要

异构图神经网络（HGNN）通常利用预定义的顶点类型和边类型序列（即元路径）来建模真实世界图中的复合关系。尽管已有多种支持 HGNN 的解决方案被提出，但它们采用以源顶点为中心的方法，即处理共享同一源顶点的元路径实例；而不同元路径实例共享的、且位于同一源顶点第一跳之外的顶点和边可能被重复处理，从而带来不规则的内存访问和冗余的边计算。在本工作中，我们观察到 HGNN 推理在不同元路径实例之间存在大量顶点和边重叠，并且共享同一枢轴顶点（即连接多条元路径的中心顶点）的元路径表现出强烈的空间相似性，能够有效刻画这些重叠。基于上述观察，我们提出了一种以枢轴为中心的加速器 PiHG，以高效支持 HGNN 推理。具体而言，PiHG 将一种新颖的以枢轴为中心的执行模型引入加速器设计，将特征访问和计算集中在枢轴顶点周围，从而能够复用跨元路径的重叠顶点和边的特征向量，进而消除冗余计算并减少不规则的片外内存访问。实验结果表明，与当前最优的软件和硬件方案相比，PiHG 平均分别实现了 21.4 倍、3.8 倍的加速以及 25.6 倍、4.1 倍的能耗节省。
