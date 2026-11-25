Z-Paraswap: Co-Optimizing ZNS Parallelism and Swapping for Heterogeneous Graph Neural Network
Authors：
[Shun-Ying Hsieh](https://63dac.conference-program.com/?post_type=page&p=15&uid=82854492570793321471)，[Tseng-Yi Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=379243)，[Yuan-Hao Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=014843)

## 中文标题

Z-Paraswap：面向异构图神经网络的 ZNS 并行性与交换协同优化

## 英文摘要

Zoned Namespace (ZNS) solid-state drives (SSDs) have been widely adopted in database systems, file systems, and large-scale data centers because they expose part of the physical storage layout to the host system. By leveraging this visibility, host software can access correlated data in parallel and eliminate valid-data copying during garbage collection, thereby improving I/O efficiency. To further integrate ZNS SSDs into memory management, prior work developed a Linux-based ZNS swapping mechanism that reserves multiple zones as swap space, extending virtual memory capacity. However, when deploying Heterogeneous Graph Neural Networks (HetGNNs), this mechanism fails to fully exploit ZNS parallelism due to HetGNN’s highly irregular and non-sequential access patterns, which lead to chip-level congestion and long-tail latency. To address this issue, we propose Z-ParaSwap, a ZNS-based Parallelism-Aware Swapping Management framework for HetGNN applications. Z-ParaSwap identifies access correlations in graph data and distributes highly correlated pages across different chips to enhance parallelism and mitigate I/O contention. Experimental results show that Z-ParaSwap reduces average swapping latency by 34% and tail latency by 44%, significantly improving overall HetGNN execution efficiency on ZNS-based systems.

## 中文摘要

分区命名空间（ZNS）固态硬盘（SSD）由于向主机系统暴露了部分物理存储布局，已被广泛应用于数据库系统、文件系统与大规模数据中心。借助这种可见性，主机软件可以并行访问相关联的数据，并消除垃圾回收过程中的有效数据拷贝，从而提升 I/O 效率。为进一步将 ZNS SSD 纳入内存管理，已有工作开发了一种基于 Linux 的 ZNS 交换机制，预留多个分区作为交换空间以扩展虚拟内存容量。然而，在部署异构图神经网络（HetGNN）时，由于 HetGNN 具有高度不规则且非顺序的访问模式，该机制无法充分利用 ZNS 的并行性，从而导致芯片级拥塞与长尾时延。为解决该问题，我们提出 Z-ParaSwap，这是一个面向 HetGNN 应用的基于 ZNS 的并行性感知交换管理框架。Z-ParaSwap 识别图数据中的访问相关性，并将高度相关的页面分散到不同芯片上，以增强并行性并缓解 I/O 争用。实验结果表明，Z-ParaSwap 将平均交换时延降低 34%、尾时延降低 44%，显著提升了 HetGNN 在基于 ZNS 的系统上的整体执行效率。

## 英文关键词

Zoned namespace, ZNS SSD, swapping management, heterogeneous graph neural network

## 中文关键词

分区命名空间、ZNS SSD、交换管理、异构图神经网络
