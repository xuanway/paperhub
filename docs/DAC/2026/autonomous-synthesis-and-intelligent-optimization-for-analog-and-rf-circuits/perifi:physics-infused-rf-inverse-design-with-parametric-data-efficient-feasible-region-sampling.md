Perifi:physics-Infused RF Inverse Design with Parametric Data-Efficient Feasible-Region Sampling
Authors：
[Siwen Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9387999286901073402)，[Keren Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=829089056373711997)，[Hyunsu Chae](https://63dac.conference-program.com/?post_type=page&p=15&uid=94346853694178630411)，[Zhaori Bi](https://63dac.conference-program.com/?post_type=page&p=15&uid=73583865219571285901)，[Zhiang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=58855218809937126151)，[Changhao Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=791243)，[Xuan Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=002243)

## 中文标题

PeRIFi：融合物理的射频逆向设计及参数化数据高效可行域采样

## 英文摘要

AI-driven inverse design shows promise in synthesizing complex electromagnetic (EM) structures for radio-frequency (RF) circuits. However, existing methods face two fundamental limitations: random topology generation produces physically infeasible layouts, and pixel-based representations encode only topology while ignoring geometric dimensions, forcing dataset regeneration and model retraining when layout scales change. We propose PeRIFi, a physics-constrained and geometry-aware inverse design framework built on three key innovations. (1) Feasibility-aware parameterization integrates B-splines (guaranteeing DC connectivity) with level-set representations (enabling flexible geometric variation), ensuring 100% physically feasible structure generation. (2) Explicit geometric encoding decouples topology from geometric dimensions, allowing a single surrogate model to generalize across multiple layout scales without regenerating datasets. (3) High-dimensional optimization employs Particle Swarm Optimization tailored to the proposed 268-dimensional feasible design space. Experimental results demonstrate substantial data-efficiency gains: with only 5k training samples, PeRIFi attains 62.8% lower MSE and a 6.7% higher 𝑅2 than a pixel-based baseline trained on 20k samples. Furthermore, PeRIFi reduces optimization cost by 22.19%–34.71% and prediction error (MAE) by 58.2% compared with state-of-the-art methods, enabling more accurate and scalable RF inverse design.

## 中文摘要

AI 驱动的逆向设计在合成射频（RF）电路所需的复杂电磁（EM）结构方面展现出前景。然而，现有方法面临两个根本性局限：随机拓扑生成会产生物理不可行的版图；基于像素的表示仅编码拓扑而忽略几何尺寸，导致版图尺度变化时必须重新生成数据集并重新训练模型。我们提出 PeRIFi，一个物理约束且几何感知的逆向设计框架，它建立在三项关键创新之上。(1) 可行性感知的参数化将 B 样条（保证直流连通性）与水平集表示（实现灵活的几何变化）相结合，确保生成 100% 物理可行的结构。(2) 显式几何编码将拓扑与几何尺寸解耦，使单一代理模型能够泛化到多种版图尺度而无需重新生成数据集。(3) 高维优化采用粒子群优化，并针对所提出的 268 维可行设计空间进行定制。实验结果表明数据效率显著提升：仅使用 5k 训练样本，PeRIFi 的 MSE 就比在 20k 样本上训练的像素基线低 62.8%，R² 高 6.7%。此外，与最先进方法相比，PeRIFi 将优化成本降低 22.19%–34.71%，并将预测误差（MAE）降低 58.2%，从而实现更准确、可扩展的射频逆向设计。

## 英文关键词

AI Inverse Design, Impedance Matching, RF

## 中文关键词

AI 逆向设计、阻抗匹配、射频
