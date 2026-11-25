VALVE: Accelerating Visible Version Searching in HTAP Systems via In-Storage Computing
Authors：
[Yi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=030343)，[Yang Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=54584274695409270301)，[Tianyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4102639928273142851)，[Chenlin Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4213970674159892189)，[Jiaxian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37582528852818661511)，[Kecheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9023677625232671802)，[Jianbin Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=93433401448651566021)，[Rui Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=430343)

## 中文标题

VALVE：通过存内计算加速 HTAP 系统中的可见版本搜索

## 英文摘要

Hybrid Transactional and Analytical Processing (HTAP) workloads are widely deployed in production systems that require real-time analytics over fresh transactional data. Under HTAP workloads, frequent updates lengthen the version chains maintained in disk-based Multi-Version Concurrency Control (MVCC) systems. Longer version chains require Visible Version Searching (VVS) to scan more versions during analytical queries, which amplifies random disk I/O and thus degrades analytical query latency. The emerging In-Storage Computing (ISC) technique offers a promising opportunity to alleviate the I/O burden, especially for the VVS process of disk-based MVCC in HTAP systems. Thus, we propose VALVE, which offloads the VVS process to a Computational Storage Device (CSD) equipped with an FPGA alongside NAND flash chips. VALVE first solves the consistency issue under host-CSD concurrency by a page-level locking mechanism. A frugal skip list is introduced in VALVE to further accelerate the version-chain traversal. We integrate VALVE into PostgreSQL 12.2 to evaluate its effectiveness on real CSD hardware using CH-Benchmark. Experimental results show that VALVE reduces end-to-end scan latency by 37.0% and improves analytical throughput by 29.0%.

## 中文摘要

混合事务与分析处理（HTAP）工作负载广泛部署于需要对新鲜事务数据进行实时分析的生产系统中。在 HTAP 工作负载下，频繁更新会延长基于磁盘的多版本并发控制（MVCC）系统中所维护的版本链。更长的版本链要求可见版本搜索（VVS）在分析查询期间扫描更多版本，从而放大随机磁盘 I/O，并降低分析查询延迟。新兴的存内计算（ISC）技术为缓解 I/O 负担提供了重要机遇，尤其适用于 HTAP 系统中基于磁盘的 MVCC 的 VVS 过程。因此，我们提出了 VALVE，它将 VVS 过程卸载到配有 FPGA 和 NAND 闪存芯片的计算存储设备（CSD）上。VALVE 首先通过页级锁机制解决主机与 CSD 并发情况下的一致性问题。VALVE 还引入了一种精简跳表，以进一步加速版本链遍历。我们将 VALVE 集成到 PostgreSQL 12.2 中，并使用 CH-Benchmark 在真实 CSD 硬件上评估其有效性。实验结果表明，VALVE 将端到端扫描延迟降低 37.0%，并将分析吞吐量提高 29.0%。

## 英文关键词

Hybrid Transactional and Analytical Processing, Multi-Version Concurrency Control, Computational Storage Device

## 中文关键词

混合事务与分析处理、多版本并发控制、计算存储设备
