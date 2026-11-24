# Workload Analysis of a Production BigData-Storage Cluster for ML and Data Analytics

**中文标题**：面向 ML 与数据分析的生产级大数据存储集群负载分析

**所属 Session**：[Session 23: Storage and OS Policies](index.md) · [ATC 2026](../index.md)

**作者**：Runhua Bian (Tsinghua University, ByteDance), Jinxin Liu (ByteDance), Hao Guo (Tsinghua University), Shaoyu Zhang (ByteDance), Liqiang Zhang (ByteDance), Zhongbao Zhang (ByteDance), Jiwu Shu (Tsinghua University), Youyou Lu (Tsinghua University)

## 英文摘要
BigData-Storage, ByteDance’s heavily customized HDFS, supports large-scale Applied Machine Learning (AML) and data analytics workloads, which are still widely used in search, advertising, recommendation systems, and offline analysis of large amounts of data. However, recent studies are missing for the workloads of HDFS and its local filesystem. In this work, we collect workload data from a thousand-node-scale region in a geo-distributed BigData-Storage cluster with five regions. We collect region-level metrics and file metadata. We further sample 60 machines, with 8 disks on each machine, for fine-grained per-disk I/O analysis. Some findings differ from prior conclusions in storage research. We find that file sizes in BigData-Storage generally follow a log-uniform distribution, not a lognormal distribution. For a local filesystem, the major part of the popularity distribution is closer to lognormal than to Zipf-Mandelbrot. Our observations also give suggestions for workload smoothing, garbage file management, filesystem readahead, and fragmentation prevention. Finally, we propose a trace reconstruction method based on workload statistics.

## 中文摘要
BigData-Storage 是字节跳动深度定制的 HDFS，支撑大规模应用机器学习（AML）与数据分析负载，这些负载仍广泛用于搜索、广告、推荐系统以及海量数据的离线分析。然而，近期研究缺乏对 HDFS 及其本地文件系统负载的考察。在本工作中，我们从一个地理分布式、包含五个区域的 BigData-Storage 集群中，收集了千节点规模区域的负载数据。我们采集了区域级指标与文件元数据。我们进一步对 60 台机器（每台配有 8 块磁盘）进行采样，以开展细粒度的逐盘 I/O 分析。部分发现与存储研究此前的结论不同。我们发现 BigData-Storage 中的文件大小总体上服从对数均匀分布，而非对数正态分布。对于本地文件系统，流行度分布的主要部分更接近对数正态分布，而非 Zipf-Mandelbrot 分布。我们的观察还为负载平滑、垃圾文件管理、文件系统预读与碎片预防提供了建议。最后，我们提出了一种基于负载统计的 trace 重建方法。

## 英文关键词
Workload characterization, Distributed storage systems, Filesystems

## 中文关键词
负载刻画，分布式存储系统，文件系统

[返回 Session 23](index.md) · [返回 ATC 2026](../index.md)
