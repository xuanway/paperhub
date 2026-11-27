PS-CAM: An Efficient Content-Addressable Memory Based Accelerator for Point Search in Point Clouds
Authors：
[Xipeng Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=77622918323156792311)，[Shaoxuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3141125778504937866)，[Shanshi Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6654228679299731031)，[Hongwu Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2254571767258993845)

## 中文标题

PS-CAM：一种用于点云中点搜索的高效内容寻址存储器加速器

## 英文摘要

Point-based neural networks have become the mainstream approaches for point cloud processing. However, they heavily rely on computationally intensive neighbor search operations like K-Nearest Neighbors (KNN) and ball query, which create significant bottlenecks for deployment in resource-constrained environments. In this paper, we present PS-CAM, a novel NOR-CAM-based accelerator designed to support both ball-query and KNN efficiently. PS-CAM converts the ball-query operation into a set of range search problems, formulating a one-shot search via the RENÉ range query scheme. To enhance energy efficiency within this scheme, a Two-Level Region-Partitioned (TLRP) technique is adopted, which reduces the number of activated CAM banks simultaneously. For KNN search, PS-CAM employs a progressive method through a series of ball-queries with increasing radius. The search iterations are bounded by the Density-Aware Radius Estimation (DARE) method, which rapidly approximates the KNN-equivalent ball radius (KEBR), thereby drastically reducing the need for repeated queries. Compared with prior works, PS-CAM demonstrates significant performance gains, achieving speedups of 1.25∼1.33× and an energy efficiency improvement of 142× in ball query. For KNN task, PS-CAM delivers speedups of 4.6∼27.2× and energy-efficiency improvements of 7.1∼2578×.

## 中文摘要

基于点的神经网络已成为点云处理的主流方法。然而，它们高度依赖 K 近邻（KNN）与球查询等计算密集的邻域搜索操作，这为在资源受限环境中的部署造成显著瓶颈。本文提出 PS-CAM，一种新型的基于 NOR-CAM 的加速器，旨在高效支持球查询与 KNN。PS-CAM 将球查询操作转化为一组范围搜索问题，并通过 RENÉ 范围查询方案实现一次性搜索。为提升该方案的能效，我们采用两级区域划分（TLRP）技术，减少同时被激活的 CAM 组数量。对于 KNN 搜索，PS-CAM 通过一系列半径递增的球查询采用渐进式方法，搜索迭代次数由密度感知半径估计（DARE）方法限定，该方法快速逼近 KNN 等效球半径（KEBR），从而大幅减少重复查询的需求。与已有工作相比，PS-CAM 展现出显著的性能增益，在球查询中实现 1.25∼1.33 倍加速与 142 倍能效提升。对于 KNN 任务，PS-CAM 带来 4.6∼27.2 倍加速与 7.1∼2578 倍能效提升。

## 英文关键词

point cloud, knn, ball query, content-addressable memory

## 中文关键词

点云、KNN、球查询、内容寻址存储器
