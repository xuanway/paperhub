# DiGiT: Co-Designing GNN Algorithms and Storage I/O for Out-of-Core Training Acceleration

**中文标题**：DiGiT：面向外存训练加速的 GNN 算法与存储 I/O 协同设计

**所属 Session**：[Session 11: Search, Recommender and Graph Systems](index.md) · [ATC 2026](../index.md)

**作者**：Qian Wei (Shandong University), Yi Li (The University of Texas at Dallas), Junchi Ren (Shandong University), Zehao Chen (Shandong University), Zhaoyan Shen (Shandong University), Dongxiao Yu (Shandong University), Bingzhe Li (University of Texas at Dallas)

## 英文摘要
Out-of-core (OOC) Graph Neural Network (GNN) systems enable training billion-node graphs on a single machine by storing graph data on SSDs. To mitigate the data loading overhead caused by frequent SSD accesses, recent OOC GNN systems have adopted GPU-initiated direct storage, allowing GPUs to directly access SSDs without CPU intervention. However, the large volume of small, random I/O operations inherent in GNN training severely limits the utilization of I/O bandwidth, ultimately hurting overall training time. In this paper, we present DiGiT, an algorithm and storage I/O co-designed framework for accelerating OOC GNN training. We propose an I/O-friendly graph reorganization strategy that stores node features sequentially in groups on SSD and a group-aware sampling algorithm that samples each group node as an indivisible unit without sacrificing model accuracy. Together, these strategies make GNN data loading process both algorithm and device efficient. Furthermore, we develop a hierarchical cache mechanism that combines a static hot-node preloading policy with a lightweight dynamic node replacement policy to minimize redundant I/O operations. Experimental results on real-world graphs show that DiGiT reduces training time by up to 47.63% compared to state-of-the-art GPU-initiated OOC GNN baselines, without compromising model accuracy.

## 中文摘要
外存（OOC）图神经网络（GNN）系统通过将图数据存放在 SSD 上，使单机能够训练十亿节点规模的图。为缓解频繁访问 SSD 带来的数据加载开销，近期的 OOC GNN 系统采用了 GPU 发起的直接存储访问，使 GPU 无需 CPU 介入即可直接访问 SSD。然而，GNN 训练固有的海量小粒度随机 I/O 严重限制了 I/O 带宽的利用率，最终拖累整体训练时间。本文提出 DiGiT，一个通过算法与存储 I/O 协同设计来加速 OOC GNN 训练的框架。我们提出一种对 I/O 友好的图重组策略，将节点特征按组连续存放在 SSD 上，并提出组感知采样算法，在不损失模型精度的前提下将每个组内的节点作为不可分割的整体进行采样。这些策略共同使 GNN 数据加载过程在算法层面与设备层面都变得高效。此外，我们设计了一种层次化缓存机制，将静态热节点预加载策略与轻量级动态节点替换策略相结合，以最小化冗余 I/O 操作。在真实图数据上的实验结果表明，在不损失模型精度的前提下，DiGiT 相比最先进的 GPU 发起式 OOC GNN 基线最高将训练时间减少 47.63%。

## 英文关键词
Graph Neural Networks, Out-of-Core Training, Storage I/O

## 中文关键词
图神经网络，外存训练，存储 I/O

[返回 Session 11](index.md) · [返回 ATC 2026](../index.md)
