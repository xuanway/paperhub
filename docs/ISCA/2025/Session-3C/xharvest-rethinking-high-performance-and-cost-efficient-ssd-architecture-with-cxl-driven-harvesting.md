---
title: "XHarvest: Rethinking High-Performance and Cost-Efficient SSD Architecture with CXL-Driven Harvesting"
description: "ISCA 2025 · Session 3C · XHarvest: CXL驱动的高性能低成本SSD架构"
tags:
  - "ISCA2025"
  - "Session 3C"
  - "Storage"
---

# XHarvest: Rethinking High-Performance and Cost-Efficient SSD Architecture with CXL-Driven Harvesting

**中文标题：** XHarvest: CXL驱动的高性能低成本SSD架构

**所属 Session：** [Session 3C](index.md) · [ISCA 2025](../index.md)

**作者：** Li Peng, Wenbo Wu, Shushu Yi, Xianzhang Chen, Chenxi Wang, Shengwen Liang, Zhe Wang, Nong Xiao, Qiao Li, Mingzhe Zhang, Jie Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731028) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The occasional nature of I/O bursts in production clusters makes the substantial and expensive SSD internal hardware resources (e.g., computation and memory resources) always underutilized, resulting in cost inefficiency. Open-Channel SSD (OCSSD), as a pioneering solution, removes the SSD internal resources but rather leverages the host-side resources to serve I/O requests. Unfortu- nately, it faces adoption obstacles due to the heavy resource con- tention with user applications, hampered host-SSD collaboration, and proprietary firmware leakage risks. Tackling these challenges, we propose XHarvest, a new cost-efficient and high-performance SSD architecture, which harnesses compute express link (CXL) and trusted execution environment (TEE) to facilitate dynamic, effi- cient, and secure host resource harvesting. It reserves moderate SSD internal resources to isolate SSD internal tasks and applications under regular I/O loads while coping with occasional I/O bursts via dynamic host resource harvesting. To this end, XHarvest executes the firmware within the host-side TEE without disclosing sensitive algorithms while leveraging the cache-coherent and fine-grained CXL to build a unified and efficient metadata cache. XHarvest also capitalizes on the CXL and its security feature to enable secure and efficient host-SSD collaboration. The evaluation results show that XHarvest reduces the hardware cost by 31.50% while achieving the same or even higher performance than conventional SSDs. It re- lieves resource contention via dynamic harvesting, reducing 2.27× execution time over OCSSD in memory-intensive tasks.

## 中文摘要

生产集群中I/O突发流量具有偶发性，这使得SSD内部大量昂贵的硬件资源（例如计算和存储资源）长期利用率偏低，造成成本低效。开放通道SSD（OCSSD）作为早期方案，舍弃SSD内部资源，转而利用主机侧资源处理I/O请求。但该方案存在落地障碍：会和用户应用产生严重资源竞争、主机与SSD协同能力受限，同时还存在固件私有逻辑泄露风险。针对上述问题，本文提出XHarvest，一款高性价比、高性能的新型SSD架构。该架构依托计算快速互联（CXL）与可信执行环境（TEE），实现动态、高效且安全的主机资源征用。XHarvest保留适量SSD内部资源，在常规I/O负载下隔离SSD内部任务与上层应用；遇到偶发I/O突发时，动态征用主机资源应对负载。为此，XHarvest将固件运行在主机端TEE内，保护敏感算法不泄露；同时利用支持缓存一致性、细粒度访问的CXL构建统一高效的元数据缓存。XHarvest还借助CXL及其安全特性，实现安全高效的主机-SSD协同。评测结果表明，XHarvest硬件成本降低31.50%，性能不弱于传统SSD甚至更优。该方案通过动态资源征用缓解资源竞争，在内存密集型任务上相比OCSSD将执行时间缩短至原来的1/2.27。

## 英文关键词

SSD Architecture, Compute Express Link, Trusted Execution Environment

## 中文关键词

固态硬盘架构, 计算快速互联（CXL）, 可信执行环境（TEE）

## 代码与研究制品

- [代码仓库](https://github.com/ChaseLab-PKU/XHarvest)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731028)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2025](../index.md)
