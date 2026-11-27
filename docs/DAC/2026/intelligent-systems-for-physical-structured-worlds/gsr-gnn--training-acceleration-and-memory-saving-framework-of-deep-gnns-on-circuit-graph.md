GSR-GNN: Training Acceleration and Memory-Saving Framework of Deep GNNs on Circuit Graph
Authors：
[Yuebo Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=41912880844581482671)，[Shiyang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=997576168751079127)，[Yifei Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=96125799235823812871)，[Vishal Kancharla](https://63dac.conference-program.com/?post_type=page&p=15&uid=8563010051243965279)，[Shaoyi Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=855843)，[Caiwen Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=636843)

## 中文标题

GSR-GNN：面向电路图的深度 GNN 训练加速与显存节省框架

## 英文摘要

Graph Neural Networks (GNNs) show strong promise for circuit analysis, but scaling to modern large-scale circuit graphs is limited by GPU memory and training cost, especially for deep models. We revisit deep GNNs for circuit graphs and show that, when trainable, they significantly outperform shallow architectures, motivating an efficient, domain-specific training framework. We propose Grouped-Sparse-Reversible GNN (GSR-GNN), which enables training GNNs with up to hundreds of layers while reducing both compute and memory overhead. GSR-GNN integrates reversible residual modules with a group-wise sparse nonlinear operator that compresses node embeddings without sacrificing task-relevant information, and employs an optimized execution pipeline to eliminate fragmented activation storage and reduce data movement. On sampled circuit graphs, GSR-GNN achieves up to 87.2% peak memory reduction and over 30× training speedup with negligible degradation in correlation-based quality metrics, making deep GNNs practical for large-scale EDA workloads.

## 中文摘要

图神经网络（GNN）在电路分析中展现出很强的潜力，但将其扩展到现代大规模电路图受限于 GPU 显存与训练开销，对深度模型尤为如此。我们重新审视了面向电路图的深度 GNN，并表明在可训练的情况下，它们显著优于浅层架构，这促使我们构建一个高效、面向特定领域的训练框架。我们提出分组—稀疏—可逆 GNN（Grouped-Sparse-Reversible GNN，GSR-GNN），它能够训练多达数百层的 GNN，同时降低计算与显存开销。GSR-GNN 将可逆残差模块与分组稀疏非线性算子相结合，后者在不牺牲任务相关信息的前提下压缩节点嵌入，并采用优化的执行流水线，以消除碎片化的激活存储并减少数据搬运。在采样的电路图上，GSR-GNN 的峰值显存最多降低 87.2%，训练加速超过 30×，而基于相关性的质量指标几乎没有下降，使深度 GNN 可实际用于大规模 EDA 负载。

## 英文关键词

GNN, EDA, Circuit Design, Reversible Computing

## 中文关键词

GNN、EDA、电路设计、可逆计算
