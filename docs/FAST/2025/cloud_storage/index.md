---
title: "Cloud Storage · FAST 2025"
description: "FAST 2025 · Cloud Storage · 4 篇论文"
tags:
  - "FAST2025"
  - "Cloud Storage"
---

# Cloud Storage · FAST 2025

**中文主题**：云存储

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-25 14:00–15:20 · **Chair**：Ming Zhao（Arizona State University）

本 Session 的四篇论文都先看真实负载，再据此重设数据组织。两篇做大规模测量：Cloudscape 统计 396 个 AWS 架构里存储服务如何被选用与组合，Maat 把链上交易的存储计费下沉到存储操作级别；另外两篇按测量结论改造系统，FlacIO 把容器镜像从磁盘内容镜像改成运行时内存状态镜像，NCBlob 把纠删码从系统化形式换成非系统化形式。收益分别落在冷启动延迟（最高 23 倍）、链上手续费（降低 32%）与修复时间（最高降低 45.0%）上，代价则是少量读吞吐损失与区块处理开销。

本 Session 共收录 **4** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [FlacIO: Flat and Collective I/O for Container Image Service](flacio_flat_and_collective_i_o_for_container_image_service.md) | FlacIO：面向容器镜像服务的扁平与集体 I/O | 容器启动真正要读的内存页是确定的，按服务把这份状态打成扁平镜像，冷启动就从随机小 I/O 变成一次顺序大 I/O。 | [页面](https://www.usenix.org/conference/fast25/presentation/liu-yubo) · [PDF](https://www.usenix.org/system/files/fast25-liu-yubo.pdf) |
| [Cloudscape: A Study of Storage Services in Modern Cloud Architectures](cloudscape_a_study_of_storage_services_in_modern_cloud_architectures.md) ([code](https://github.com/WiscADSL/Cloudscape)) | Cloudscape：现代云架构中的存储服务研究 | 云上存储的真实分布不是文件系统而是对象存储：S3 覆盖 68% 的系统，约一半架构把数据摊在两种以上服务里。 | [页面](https://www.usenix.org/conference/fast25/presentation/satija) · [PDF](https://www.usenix.org/system/files/fast25-satija.pdf) |
| [Maat: Analyzing and Optimizing Overcharge on Blockchain Storage](maat_analyzing_and_optimizing_overcharge_on_blockchain_storage.md) | Maat：区块链存储过度收费的分析与优化 | 手续费按 opcode 收，真实代价却取决于对象是否已在内存里：把计费下沉到存储操作语义，才能既省费又保持共识一致。 | [页面](https://www.usenix.org/conference/fast25/presentation/he) · [PDF](https://www.usenix.org/system/files/fast25-he.pdf) |
| [Revisiting Network Coding for Warm Blob Storage](revisiting_network_coding_for_warm_blob_storage.md) ([code](https://github.com/YuchongHu/NCBlob)) | 重新审视温数据 Blob 存储中的网络编码 | 带宽最优不等于修复最快：块小的时候，系统化 MSR 码的非连续 I/O 才是瓶颈，退回非系统化编码反而更快。 | [页面](https://www.usenix.org/conference/fast25/presentation/gan) · [PDF](https://www.usenix.org/system/files/fast25-gan.pdf) |

[返回 FAST 2025](../index.md)
