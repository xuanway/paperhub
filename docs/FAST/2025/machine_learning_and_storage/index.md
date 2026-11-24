---
title: "Machine Learning and Storage · FAST 2025"
description: "FAST 2025 · Machine Learning and Storage · 5 篇论文"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
---

# Machine Learning and Storage · FAST 2025

**中文主题**：机器学习与存储

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-25 15:50–17:30 · **Chair**：Kan Wu（Google）

本 Session 的五篇工作面对同一个约束：模型权重、KVCache 与向量索引的规模都远超显存与内存容量，存储层必须重新进入计算的关键路径。技术路线分化明显——有的把 KVCache 池化成集群级全局缓存并用调度换取吞吐，有的靠只加载重要 KV 或只传递向量 ID 来压缩跨层数据量，还有的重新设计 GPU 直连持久内存与 NVMe 的索引结构和文件接口。代表性结果包括有效请求容量提升 59%~498%、前缀 KV 复用的 TTFT 降低 2.8 倍，以及单张入门级 GPU 上十亿级向量检索 QPS 提升 9.4-13.1 倍。

本 Session 共收录 **5** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| **最佳论文** · [Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot](mooncake_trading_more_storage_for_less_computation_a_kvcache_centric_architecture_for_serving_llm_chatbot.md) | Mooncake：以更多存储换取更少计算——面向 LLM 聊天机器人服务的 KVCache 中心架构 | KVCache 不必留在本地：把集群闲置的 CPU、DRAM、SSD 与 NIC 池化成全局缓存，用更多存储换掉重复的预填充计算。 | [页面](https://www.usenix.org/conference/fast25/presentation/qin) · [PDF](https://www.usenix.org/system/files/fast25-qin.pdf) |
| [Towards High-throughput and Low-latency Billion-scale Vector Search via CPU/GPU Collaborative Filtering and Re-ranking](towards_high_throughput_and_low_latency_billion_scale_vector_search_via_cpu_gpu_collaborative_filtering_and_re_ranking.md) | 面向高吞吐、低延迟十亿级向量检索的 CPU/GPU 协同过滤与重排序 | 把索引拆成 SSD 上的原始向量、显存里的压缩向量和内存里的向量 ID 三层，让 CPU 只送 ID、GPU 只算距离，重排序还能提前收敛。 | [页面](https://www.usenix.org/conference/fast25/presentation/tian-bing) · [PDF](https://www.usenix.org/system/files/fast25-tian-bing.pdf) |
| [IMPRESS: An Importance-Informed Multi-Tier Prefix KV Storage System for Large Language Model Inference](impress_an_importance_informed_multi_tier_prefix_kv_storage_system_for_large_language_model_inference.md) | IMPRESS：面向大语言模型推理的重要性感知多层前缀 KV 存储系统 | 同层各注意力头的重要 token 索引高度重合，因此只读少量 probe head 的 key 就能挑出该加载的前缀 KV。 | [页面](https://www.usenix.org/conference/fast25/presentation/chen-weijian-impress) · [PDF](https://www.usenix.org/system/files/fast25-chen-weijian-impress.pdf) |
| [GPHash: An Efficient Hash Index for GPU with Byte-Granularity Persistent Memory](gphash_an_efficient_hash_index_for_gpu_with_byte_granularity_persistent_memory.md) ([code](https://github.com/LighT-chenml/GPHash)) | GPHash：面向字节粒度持久内存 GPU 的高效哈希索引 | 把一次哈希操作交给整个 warp 协作完成、用 CAS 加槽位状态代替日志、再以冻结式桶缓存挡住 PM 带宽瓶颈。 | [页面](https://www.usenix.org/conference/fast25/presentation/chen-menglei) · [PDF](https://www.usenix.org/system/files/fast25-chen-menglei.pdf) |
| [GeminiFS: A Companion File System for GPUs](geminifs_a_companion_file_system_for_gpus.md) | GeminiFS：面向 GPU 的伴生文件系统 | 不另造通用 GPU 文件系统，而是让 GPU 侧的文件系统与宿主文件系统伴生，元数据随文件走、控制平面两侧并行。 | [页面](https://www.usenix.org/conference/fast25/presentation/qiu) · [PDF](https://www.usenix.org/system/files/fast25-qiu.pdf) |

> 获奖：**最佳论文**。

[返回 FAST 2025](../index.md)
