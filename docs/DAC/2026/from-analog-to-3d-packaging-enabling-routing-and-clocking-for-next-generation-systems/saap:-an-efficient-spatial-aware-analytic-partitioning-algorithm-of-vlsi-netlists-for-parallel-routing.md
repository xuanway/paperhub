SAAP: An Efficient Spatial-Aware Analytic Partitioning Algorithm of VLSI Netlists for Parallel Routing
Authors：
[CHEN LIU](https://63dac.conference-program.com/?post_type=page&p=15&uid=6719514636327175475)，[Hongxin Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=7377014744482765095)，[Lang Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=214843)，[Wenchao Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=8051656962245530576)，[Wuxi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6760732440427187845)

## 中文标题

SAAP：面向并行布线的 VLSI 网表高效空间感知解析划分算法

## 英文摘要

As VLSI designs grow in complexity, partitioning is widely adopted to accelerate physical design through parallel computing. However, traditional hypergraph partitioning methods often degrade in performance when applied to 2D layouts due to spatial constraints. For routers with post-placement locations, a spatial-aware partitioning method fully utilizing placement data is preferable. Existing works can only consider soft spatial constraints, leading to a scattered distribution in one partition. We propose SAAP, an analytic partitioning algorithm enforcing hard spatial constraints while efficiently minimizing cut sizes. It includes analytic boundary modeling with regularity-guided simulated annealing and region embedding. Given placed netlists, it generates timing-friendly k-way spatially continuous partitions for parallel routing. Experiments show that it can quickly provide several to dozens of times smaller spatial cut sizes than previous state-of-the-art, with better spatial continuity.

## 中文摘要

随着 VLSI 设计复杂度不断增长，划分被广泛采用以通过并行计算加速物理设计。然而，传统超图划分方法在应用于二维版图时，受空间约束影响往往性能下降。对于已知布局后位置的布线器而言，充分利用布局数据的空间感知划分方法更为可取。已有工作只能考虑软空间约束，导致同一划分内元素分布分散。我们提出 SAAP，一种在强制硬空间约束的同时高效最小化割大小的解析划分算法。它包含解析边界建模、规律性引导的模拟退火以及区域嵌入。给定已完成布局的网表，它可生成时序友好、空间连续的 k 路划分用于并行布线。实验表明，与先前最先进方法相比，它能够快速获得小几倍至数十倍的空间割大小，并具有更好的空间连续性。

## 英文关键词

Partitioning, Physical Design, Analytic Algorithm

## 中文关键词

划分、物理设计、解析算法
