---
title: "FAST 2025 论文集"
description: "USENIX 文件与存储技术大会 FAST 2025，Santa Clara, CA"
tags:
  - "FAST2025"
  - "Storage Systems"
---

# FAST 2025

**FAST 2025** · 2025年2月25日 - 2月27日 · Santa Clara, CA

FAST '25 共接受 **36** 篇论文（accepted papers），本目录全部收录，涵盖 **8** 个方向。会议议程与各论文摘要见 [USENIX 技术议程](https://www.usenix.org/conference/fast25/technical-sessions)，全文见 [FAST '25 论文集 PDF](https://www.usenix.org/system/files/fast25_full_proceedings.pdf)。

**论文演示文稿（Slides）**：可在 [FAST '25 官方主议程（Main Program）](https://www.usenix.org/conference/fast25/technical-sessions#tueam)中找到对应论文，点击 Slides 图标或进入论文页面查看；是否提供以官方页面为准。

每个 Session 页面给出该方向的论文速览；单篇论文页面标注中文标题，并以英文摘要（USENIX 官方摘要原文）、中文摘要（对应译文）开篇，随后是研究背景与问题、核心贡献、方法与技术要点、评估与主要结果。中文内容依据 USENIX 官方摘要与论文原文整理，论文标题、作者、页码与数字均以原文为准。

## Session 导航

按会议日程浏览 Session；点击主题名称可查看该场次的论文速览。下方列出论文的中英文标题及已核实的代码链接；研究制品信息参考论文与 [FAST '25 Artifact Evaluation](https://sysartifacts.github.io/fast2025/results)，未列出链接不代表未开源。

| Session | 中文主题 | 论文数 | Session Chair |
| --- | --- | ---: | --- |
| [File Systems](file_systems/index.md) | 文件系统 | 5 | Yu Hua（Huazhong University of Science and Technology） |
| [Cloud Storage](cloud_storage/index.md) | 云存储 | 4 | Ming Zhao（Arizona State University） |
| [Machine Learning and Storage](machine_learning_and_storage/index.md) | 机器学习与存储 | 5 | Kan Wu（Google） |
| [More Machine Learning](more_machine_learning/index.md) | 机器学习专题 | 4 | Ali R. Butt（Virginia Tech） |
| [Hardware Assist](hardware_assist/index.md) | 硬件辅助 | 5 | Kiran Kumar Muniswamy Reddy（Amazon） |
| [Security, Integrity, and Consistency](security_integrity_and_consistency/index.md) | 安全、完整性与一致性 | 5 | Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)） |
| [Compression and Deduplication](compression_and_deduplication/index.md) | 压缩与去重 | 4 | Gala Yadgar（Technion—Israel Institute of Technology） |
| [Storage Diversity and Heterogeneity](storage_diversity_and_heterogeneity/index.md) | 存储多样性与异构性 | 4 | Avani Wildani（Cloudflare and Emory University） |

**最佳论文**：Ananke、Mooncake；**杰出工件奖**：ShiftLock、GogetaFS。

## File Systems

| 英文标题 | 中文标题 |
| --- | --- |
| **最佳论文** · [Fast, Transparent Filesystem Microkernel Recovery with Ananke](file_systems/fast_transparent_filesystem_microkernel_recovery_with_ananke.md) | Ananke：快速、透明的文件系统微内核恢复 |
| [Boosting File Systems Elegantly: A Transparent NVM Write-ahead Log for Disk File Systems](file_systems/boosting_file_systems_elegantly_a_transparent_nvm_write_ahead_log_for_disk_file_systems.md) ([code](https://github.com/BugJLU/NVLog)) | 优雅地加速文件系统：面向磁盘文件系统的透明 NVM 写前日志 |
| [DJFS : Directory-Granularity Filesystem Journaling for CMM-H SSDs](file_systems/djfs_directory_granularity_filesystem_journaling_for_cmm_h_ssds.md) | DJFS：面向 CMM-H SSD 的目录粒度文件系统日志 |
| [ScaleLFS: A Log-Structured File System with Scalable Garbage Collection for Commodity SSDs](file_systems/scalelfs_a_log_structured_file_system_with_scalable_garbage_collection_for_commodity_ssds.md) | ScaleLFS：面向商用 SSD、具备可扩展垃圾回收的日志结构文件系统 |
| [Rethinking the Request-to-IO Transformation Process of File Systems for Full Utilization of High-Bandwidth SSDs](file_systems/rethinking_the_request_to_io_transformation_process_of_file_systems_for_full_utilization_of_high_bandwidth_ssds.md) ([code](https://github.com/YekangZhan/OrchFS)) | 重新审视文件系统的请求到 IO 转换过程：充分利用高带宽 SSD |

## Cloud Storage

| 英文标题 | 中文标题 |
| --- | --- |
| [FlacIO: Flat and Collective I/O for Container Image Service](cloud_storage/flacio_flat_and_collective_i_o_for_container_image_service.md) | FlacIO：面向容器镜像服务的扁平与集体 I/O |
| [Cloudscape: A Study of Storage Services in Modern Cloud Architectures](cloud_storage/cloudscape_a_study_of_storage_services_in_modern_cloud_architectures.md) ([code](https://github.com/WiscADSL/Cloudscape)) | Cloudscape：现代云架构中的存储服务研究 |
| [Maat: Analyzing and Optimizing Overcharge on Blockchain Storage](cloud_storage/maat_analyzing_and_optimizing_overcharge_on_blockchain_storage.md) | Maat：区块链存储过度收费的分析与优化 |
| [Revisiting Network Coding for Warm Blob Storage](cloud_storage/revisiting_network_coding_for_warm_blob_storage.md) ([code](https://github.com/YuchongHu/NCBlob)) | 重新审视温数据 Blob 存储中的网络编码 |

## Machine Learning and Storage

| 英文标题 | 中文标题 |
| --- | --- |
| **最佳论文** · [Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot](machine_learning_and_storage/mooncake_trading_more_storage_for_less_computation_a_kvcache_centric_architecture_for_serving_llm_chatbot.md) | Mooncake：以更多存储换取更少计算——面向 LLM 聊天机器人服务的 KVCache 中心架构 |
| [Towards High-throughput and Low-latency Billion-scale Vector Search via CPU/GPU Collaborative Filtering and Re-ranking](machine_learning_and_storage/towards_high_throughput_and_low_latency_billion_scale_vector_search_via_cpu_gpu_collaborative_filtering_and_re_ranking.md) | 面向高吞吐、低延迟十亿级向量检索的 CPU/GPU 协同过滤与重排序 |
| [IMPRESS: An Importance-Informed Multi-Tier Prefix KV Storage System for Large Language Model Inference](machine_learning_and_storage/impress_an_importance_informed_multi_tier_prefix_kv_storage_system_for_large_language_model_inference.md) | IMPRESS：面向大语言模型推理的重要性感知多层前缀 KV 存储系统 |
| [GPHash: An Efficient Hash Index for GPU with Byte-Granularity Persistent Memory](machine_learning_and_storage/gphash_an_efficient_hash_index_for_gpu_with_byte_granularity_persistent_memory.md) ([code](https://github.com/LighT-chenml/GPHash)) | GPHash：面向字节粒度持久内存 GPU 的高效哈希索引 |
| [GeminiFS: A Companion File System for GPUs](machine_learning_and_storage/geminifs_a_companion_file_system_for_gpus.md) | GeminiFS：面向 GPU 的伴生文件系统 |

## More Machine Learning

| 英文标题 | 中文标题 |
| --- | --- |
| [3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches](more_machine_learning/3l_cache_low_overhead_and_precise_learning_based_eviction_policy_for_caches.md) ([code](https://github.com/optiq-lab/3L-Cache)) | 3L-Cache：低开销且精确的缓存学习型淘汰策略 |
| [LeapGNN: Accelerating Distributed GNN Training Leveraging Feature-Centric Model Migration](more_machine_learning/leapgnn_accelerating_distributed_gnn_training_leveraging_feature_centric_model_migration.md) ([code](https://github.com/ISCS-ZJU/LeapGNN-AE)) | LeapGNN：借助以特征为中心的模型迁移加速分布式 GNN 训练 |
| [HiDPU: A DPU-Oriented Hybrid Indexing Scheme for Disaggregated Storage Systems](more_machine_learning/hidpu_a_dpu_oriented_hybrid_indexing_scheme_for_disaggregated_storage_systems.md) | HiDPU：面向解耦存储系统的 DPU 导向混合索引方案 |
| [PIMLex: A High-Performance Learned Index with Processing-in-Memory](more_machine_learning/pimlex_a_high_performance_learned_index_with_processing_in_memory.md) | PIMLex：基于存内计算的高性能学习型索引 |

## Hardware Assist

| 英文标题 | 中文标题 |
| --- | --- |
| [HaSiS: A Hardware-assisted Single-index Store for Hybrid Transactional and Analytical Processing](hardware_assist/hasis_a_hardware_assisted_single_index_store_for_hybrid_transactional_and_analytical_processing.md) | HaSiS：面向混合事务与分析处理的硬件辅助单索引存储 |
| [AegonKV: A High Bandwidth, Low Tail Latency, and Low Storage Cost KV-Separated LSM Store with SmartSSD-based GC Offloading](hardware_assist/aegonkv_a_high_bandwidth_low_tail_latency_and_low_storage_cost_kv_separated_lsm_store_with_smartssd_based_gc_offloading.md) ([code](https://github.com/CGCL-codes/AegonKV)) | AegonKV：基于 SmartSSD GC 卸载的高带宽、低尾延迟、低存储成本 KV 分离 LSM 存储 |
| [D2FS: Device-Driven Filesystem Garbage Collection](hardware_assist/d2fs_device_driven_filesystem_garbage_collection.md) ([code](https://github.com/ESOS-Lab/D2FS)) | D2FS：设备驱动的文件系统垃圾回收 |
| **杰出工件奖** · [ShiftLock: Mitigate One-sided RDMA Lock Contention via Handover](hardware_assist/shiftlock_mitigate_one_sided_rdma_lock_contention_via_handover.md) ([code](https://github.com/thustorage/shiftlock)) | ShiftLock：通过锁移交缓解单边 RDMA 锁竞争 |
| [Selective On-Device Execution of Data-Dependent Read I/Os](hardware_assist/selective_on_device_execution_of_data_dependent_read_i_os.md) ([code](https://github.com/cssl-unist/sode)) | 数据依赖读 I/O 的选择性设备内执行 |

## Security, Integrity, and Consistency

| 英文标题 | 中文标题 |
| --- | --- |
| [On Scalable Integrity Checking for Secure Cloud Disks](security_integrity_and_consistency/on_scalable_integrity_checking_for_secure_cloud_disks.md) | 面向安全云盘的可扩展完整性校验 |
| [Silhouette: Leveraging Consistency Mechanisms to Detect Bugs in Persistent Memory-Based File Systems](security_integrity_and_consistency/silhouette_leveraging_consistency_mechanisms_to_detect_bugs_in_persistent_memory_based_file_systems.md) ([code](https://github.com/iaoing/Silhouette)) | Silhouette：利用一致性机制检测持久内存文件系统中的缺陷 |
| [OPIMQ: Order Preserving IO stack for Multi-Queue Block Device](security_integrity_and_consistency/opimq_order_preserving_io_stack_for_multi_queue_block_device.md) ([code](https://github.com/ESOS-Lab/OPIMQ)) | OPIMQ：面向多队列块设备的保序 I/O 栈 |
| [AWUPF Rediscovered: Atomic Writes to Unleash Pivotal Fault-Tolerance in SSDs](security_integrity_and_consistency/awupf_rediscovered_atomic_writes_to_unleash_pivotal_fault_tolerance_in_ssds.md) | 重新发现 AWUPF：以原子写释放 SSD 的关键容错能力 |
| [AtomicDisk: A Secure Virtual Disk for TEEs against Eviction Attacks](security_integrity_and_consistency/atomicdisk_a_secure_virtual_disk_for_tees_against_eviction_attacks.md) | AtomicDisk：面向 TEE 的抵御逐出攻击的安全虚拟磁盘 |

## Compression and Deduplication

| 英文标题 | 中文标题 |
| --- | --- |
| [MedFS: Pursuing Low Update Overhead via Metadata-Enabled Delta Compression for Log-structured File System on Mobile Device](compression_and_deduplication/medfs_pursuing_low_update_overhead_via_metadata_enabled_delta_compression_for_log_structured_file_system_on_mobile_device.md) | MedFS：面向移动设备日志结构文件系统、以元数据支持增量压缩降低更新开销 |
| **杰出工件奖** · [Don't Maintain Twice, It's Alright: Merged Metadata Management in Deduplication File System with GogetaFS](compression_and_deduplication/don_t_maintain_twice_it_s_alright_merged_metadata_management_in_deduplication_file_system_with_gogetafs.md) ([code](https://github.com/GogetaFS/GogetaFS-AE)) | 不必重复维护：GogetaFS 去重文件系统中的合并元数据管理 |
| [Archer: Adaptive Memory Compression with Page-Association-Rule Awareness for High-Speed Response of Mobile Devices](compression_and_deduplication/archer_adaptive_memory_compression_with_page_association_rule_awareness_for_high_speed_response_of_mobile_devices.md) | Archer：面向移动设备快速响应的页关联规则感知自适应内存压缩 |
| [VectorCDC: Accelerating Data Deduplication with Vector Instructions](compression_and_deduplication/vectorcdc_accelerating_data_deduplication_with_vector_instructions.md) ([code](https://github.com/UWASL/dedup-bench)) | VectorCDC：利用向量指令加速数据去重 |

## Storage Diversity and Heterogeneity

| 英文标题 | 中文标题 |
| --- | --- |
| [Oasis: An Out-of-core Approximate Graph System via All-Distances Sketches](storage_diversity_and_heterogeneity/oasis_an_out_of_core_approximate_graph_system_via_all_distances_sketches.md) ([code](https://github.com/tsunyuyang/Oasis)) | Oasis：基于全距离草图的外存近似图系统 |
| [PolyStore: Exploiting Combined Capabilities of Heterogeneous Storage](storage_diversity_and_heterogeneity/polystore_exploiting_combined_capabilities_of_heterogeneous_storage.md) ([code](https://github.com/RutgersCSSystems/PolyStore)) | PolyStore：发挥异构存储的联合能力 |
| [Liquid-State Drive: A Case for DNA Block Device for Enormous Data](storage_diversity_and_heterogeneity/liquid_state_drive_a_case_for_dna_block_device_for_enormous_data.md) | 液态驱动器：面向海量数据的 DNA 块设备探索 |
| [DNA data storage: A generative tool for Motif-based DNA storage](storage_diversity_and_heterogeneity/dna_data_storage_a_generative_tool_for_motif_based_dna_storage.md) | DNA 数据存储：面向基序编码 DNA 存储的生成式工具 |
