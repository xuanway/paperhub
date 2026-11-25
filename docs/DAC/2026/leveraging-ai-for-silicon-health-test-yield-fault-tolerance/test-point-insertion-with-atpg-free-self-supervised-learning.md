Test Point Insertion with ATPG-Free Self-Supervised Learning
Authors：
[Tae-Min Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=6840961426304515871)，[Sung-Hyuk Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=34785340091484601711)，[Jeongyeol Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=52278653599092616061)，[Jiwhan Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=3414433835248581746)，[Nur Touba](https://63dac.conference-program.com/?post_type=page&p=15&uid=80710876505097410571)，[Joon-Sung Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=061143)

## 中文标题

基于无 ATPG 自监督学习的测试点插入

## 英文摘要

Test Point Insertion (TPI) is a critical Design-for-Testability (DFT) technique to reduce test cost, yet optimal insertion remains an NP-hard problem. Conventional heuristics fail to capture global testability in complex reconvergent fanout structures, while modern machine learning (ML) approaches suffer from high ATPG-related costs. This paper presents a TPI framework using ATPG-free Self-Supervised Learning (SSL). Our framework leverages an autoencoder to extract compact functional embeddings directly from random bit sequences, completely bypassing computationally expensive ATPG runs. These embeddings are distributed across the netlist via a propagation model trained on standard cell libraries, ensuring scalability. Testability scores are derived using cosine similarity for controllability and gradient-based saliency for observability, followed by a Fanout-Free Region (FFR)-based Non-Maximum Suppression (NMS) for final test point selection. Experimental results validate the approach, showing a pattern-count reduction superior to the state-of-the-art approach on 9 of 14 benchmarks. The method also achieves the best PC reduction in 8 circuits and provides significant fault coverage gains on difficult benchmarks.

## 中文摘要

测试点插入（TPI）是降低测试成本的一项关键可测性设计（DFT）技术，但最优插入仍是一个 NP 难问题。传统启发式方法无法在复杂的重汇聚扇出结构中刻画全局可测性，而现代机器学习（ML）方法则受制于与 ATPG 相关的高昂成本。本文提出一个采用无 ATPG 自监督学习（SSL）的 TPI 框架。该框架利用自编码器直接从随机比特序列中提取紧凑的功能嵌入，完全绕开计算昂贵的 ATPG 运行；这些嵌入再通过一个在标准单元库上训练的传播模型分布到网表中，从而保证可扩展性。可测性分数分别通过余弦相似度（可控性）与基于梯度的显著性（可观测性）导出，随后采用基于无扇出区域（FFR）的非极大值抑制（NMS）完成最终的测试点选择。实验结果验证了该方法的有效性：在 14 个基准中的 9 个上，其图样数量缩减优于最先进方法；该方法还在 8 个电路中取得最佳的 PC 缩减，并在困难基准上带来显著的故障覆盖率增益。

## 英文关键词

Test Point Insertion, Graph Neural Networks, Saliency Map, Self-supervised Learning, Autoencoder

## 中文关键词

测试点插入、图神经网络、显著性图、自监督学习、自编码器
