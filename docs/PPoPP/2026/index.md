---
title: "PPoPP 2026 论文集"
description: "PPoPP 2026 官方主会议程的 Session 与论文索引。"
tags:
  - "PPoPP2026"
  - "Computer Systems"
---

# PPoPP 2026

**PPoPP 2026** · 2026年1月31日 - 2月4日 · Sydney, Australia

本索引依据 [PPoPP 2026 官方主会议程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)整理主会 **13 个 Session、51 篇论文**，按官方场次顺序编排。论文标题以会议论文集及官方议程为准。

各论文页面包含作者、摘要、研究要点、ACM DOI 和官方议程链接。获奖信息按官方议程标注整理。

## 获奖论文

- **Best Paper Award**：[Binary Compatible Critical Section Delegation](Session-1/binary_compatible_critical_section_delegation.md)
- **Best Paper Nominee**：[Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads](Session-2/rethinking_thread_scheduling_under_oversubscription_a_user_space_framework_for_coordinating_multi_runtime_and_multi_process_workloads.md)
- **Best Paper Nominee**：[UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees](Session-3/ufo_trees_practical_and_provably_efficient_parallel_batch_dynamic_trees.md)
- **Best Paper Nominee**：[PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation](Session-4/prism_an_efficient_gpu_based_lossy_compression_framework_for_progressive_data_retrieval_with_multi_level_interpolation.md)
- **Best Artifact Award**：[HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff](Session-6/hiercut_enabling_16_bit_format_mixed_precision_for_molecular_dynamics_through_hierarchical_cutoff.md)
- **Best Paper Nominee**：[Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters](Session-7/trojan_horse_aggregate_and_batch_for_scaling_up_sparse_direct_solvers_on_gpu_clusters.md)
- **Best Paper Nominee**：[CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](Session-8/ccl_d_a_high_precision_diagnostic_system_for_slow_and_hang_anomalies_in_large_scale_model_training.md)

## Session 导航 {#session-nav}

点击 Session 可浏览对应论文、作者与研究要点。

| Session | 中文主题 | Session Chair | 论文数 |
| --- | --- | --- | ---: |
| [Session 1: Concurrency Control](Session-1/index.md) | 并发控制 | Madan Musuvathi | 4 |
| [Session 2: Scheduling and Load Balancing](Session-2/index.md) | 调度与负载均衡 | V Krishna Nandivada | 4 |
| [Session 3: Concurrent Data Structures](Session-3/index.md) | 并发数据结构 | Calin Cascaval | 4 |
| [Session 4: GPU and Heterogeneous Computing](Session-4/index.md) | GPU 与异构计算 | Frank Mueller | 4 |
| [Session 5: Stencil and Sparse Matrix Computation](Session-5/index.md) | Stencil 与稀疏矩阵计算 | Shoaib Kamil | 4 |
| [Session 6: Mixed Precision and Quantization](Session-6/index.md) | 混合精度与量化 | Dingwen Tao | 4 |
| [Session 7: Cluster and Cloud Computing](Session-7/index.md) | 集群与云计算 | Ruslan Nikolaev | 4 |
| [Session 8: Distributed Training](Session-8/index.md) | 分布式训练 | Bo Fang | 4 |
| [Session 9: Parallel Algorithms](Session-9/index.md) | 并行算法 | Kenjiro Taura | 4 |
| [Session 10: ML Inference](Session-10/index.md) | 机器学习推理 | Hailong Yang | 4 |
| [Session 11: Graphs and Graph Neural Networks](Session-11/index.md) | 图与图神经网络 | Ali Jannesari | 4 |
| [Session 12: Optimizing Transformers](Session-12/index.md) | Transformer 优化 | Shaoshuai Zhang | 3 |
| [Session 13: Matrix and Linear Algebra Algorithms](Session-13/index.md) | 矩阵与线性代数算法 | William S. Moses | 4 |

## Session 1: Concurrency Control

| English Title | 中文标题 |
| --- | --- |
| [Binary Compatible Critical Section Delegation](Session-1/binary_compatible_critical_section_delegation.md) | 二进制兼容的临界区委派 |
| [Hapax Locks: Scalable Value-Based Mutual Exclusion](Session-1/hapax_locks_scalable_value_based_mutual_exclusion.md) | Hapax Locks：可扩展的基于值互斥锁 |
| [Fixing Non-blocking Data Structures for Better Compatibility with Memory Reclamation Schemes](Session-1/fixing_non_blocking_data_structures_for_better_compatibility_with_memory_reclamation_schemes.md) | 修复非阻塞数据结构以提升其与内存回收方案的兼容性 |
| [Multiverse: Transactional Memory with Dynamic Multiversioning](Session-1/multiverse_transactional_memory_with_dynamic_multiversioning.md) | Multiverse：支持动态多版本控制的事务内存 |

## Session 2: Scheduling and Load Balancing

| English Title | 中文标题 |
| --- | --- |
| [Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads](Session-2/rethinking_thread_scheduling_under_oversubscription_a_user_space_framework_for_coordinating_multi_runtime_and_multi_process_workloads.md) | 重新思考超额订阅下的线程调度：协调多运行时与多进程工作负载的用户态框架 |
| [Waste-Efficient Work Stealing](Session-2/waste_efficient_work_stealing.md) | 减少浪费的工作窃取 |
| [DiggerBees: Depth First Search Leveraging Hierarchical Block-Level Stealing on GPUs](Session-2/diggerbees_depth_first_search_leveraging_hierarchical_block_level_stealing_on_gpus.md) | DiggerBees：利用 GPU 分层块级窃取的深度优先搜索 |
| [PANA: A Fine-Grained Runtime-Adaptive Load Balancing for Parallel SpMV on Multicore CPUs](Session-2/pana_a_fine_grained_runtime_adaptive_load_balancing_for_parallel_spmv_on_multicore_cpus.md) | PANA：多核 CPU 并行 SpMV 的细粒度运行时自适应负载均衡 |

## Session 3: Concurrent Data Structures

| English Title | 中文标题 |
| --- | --- |
| [UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees](Session-3/ufo_trees_practical_and_provably_efficient_parallel_batch_dynamic_trees.md) | UFO Trees：实用且具可证明效率的并行批量动态树 |
| [Sharded Elimination and Combining for Highly-Efficient Concurrent Stacks](Session-3/sharded_elimination_and_combining_for_highly_efficient_concurrent_stacks.md) | 分片消除与合并：构建高效并发栈 |
| [Concurrent Balanced Augmented Trees](Session-3/concurrent_balanced_augmented_trees.md) | 并发平衡增强树 |
| [Parallel Dynamic Spatial Indexes](Session-3/parallel_dynamic_spatial_indexes.md) | 并行动态空间索引 |

## Session 4: GPU and Heterogeneous Computing

| English Title | 中文标题 |
| --- | --- |
| [PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation](Session-4/prism_an_efficient_gpu_based_lossy_compression_framework_for_progressive_data_retrieval_with_multi_level_interpolation.md) | PRISM：基于多级插值的高效 GPU 有损压缩框架，支持渐进式数据检索 |
| [Dynamic Detection of Inefficient Data Mapping Patterns in Heterogeneous OpenMP Applications](Session-4/dynamic_detection_of_inefficient_data_mapping_patterns_in_heterogeneous_openmp_applications.md) | 动态检测异构 OpenMP 应用中的低效数据映射模式 |
| [Root-Down Exposure for Maximal Clique Enumeration on GPUs](Session-4/root_down_exposure_for_maximal_clique_enumeration_on_gpus.md) | 面向 GPU 最大团枚举的自根向下暴露方法 |
| [ROME: Maximizing GPU Efficiency for All-Pairs Shortest Path via Taming Fine-Grained Irregularities](Session-4/rome_maximizing_gpu_efficiency_for_all_pairs_shortest_path_via_taming_fine_grained_irregularities.md) | ROME：驯服细粒度不规则性以提升 GPU 全点对最短路径计算效率 |

## Session 5: Stencil and Sparse Matrix Computation

| English Title | 中文标题 |
| --- | --- |
| [SPIDER: Unleashing Sparse Tensor Cores for Stencil Computation via Strided Swapping](Session-5/spider_unleashing_sparse_tensor_cores_for_stencil_computation_via_strided_swapping.md) | SPIDER：通过跨步交换释放稀疏张量核的 stencil 计算能力 |
| [ASM-SpMM: Unleashing the Potential of Arm SME for Sparse Matrix Multiplication Acceleration](Session-5/asm_spmm_unleashing_the_potential_of_arm_sme_for_sparse_matrix_multiplication_acceleration.md) | ASM-SpMM：释放 Arm SME 加速稀疏矩阵乘法的潜力 |
| [Exploiting Efficient Mapping and Pipelined Execution for Accelerating SpMV on Tensor Cores](Session-5/exploiting_efficient_mapping_and_pipelined_execution_for_accelerating_spmv_on_tensor_cores.md) | 利用高效映射与流水线执行加速张量核上的 SpMV |
| [VDHA: Vector-Driven Hash Aggregation for Sparse Matrix-Sparse Vector Multiplication on GPUs](Session-5/vdha_vector_driven_hash_aggregation_for_sparse_matrix_sparse_vector_multiplication_on_gpus.md) | VDHA：面向 GPU 稀疏矩阵-稀疏向量乘法的向量驱动哈希聚合 |

## Session 6: Mixed Precision and Quantization

| English Title | 中文标题 |
| --- | --- |
| [RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization](Session-6/romeo_mitigating_dual_dimensional_outliers_with_rotated_mixed_precision_quantization.md) | RoMeo：通过旋转混合精度量化缓解双维离群值 |
| [High-Throughput Non-uniformly Quantized 3-bit LLM Inference](Session-6/high_throughput_non_uniformly_quantized_3_bit_llm_inference.md) | 高吞吐非均匀量化 3-bit 大语言模型推理 |
| [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](Session-6/janusquant_accurate_and_efficient_2_bit_kv_cache_quantization_for_long_context_inference.md) | JanusQuant：面向长上下文推理的准确高效 2-bit KV Cache 量化 |
| [HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff](Session-6/hiercut_enabling_16_bit_format_mixed_precision_for_molecular_dynamics_through_hierarchical_cutoff.md) | HierCut：通过分层截断为分子动力学实现 16-bit 格式混合精度 |

## Session 7: Cluster and Cloud Computing

| English Title | 中文标题 |
| --- | --- |
| [Cacheman: A Comprehensive Last-Level Cache Management System for Multi-tenant Clouds](Session-7/cacheman_a_comprehensive_last_level_cache_management_system_for_multi_tenant_clouds.md) | Cacheman：面向多租户云的全面末级缓存管理系统 |
| [zBuffer: Zero-Copy and Metadata-Free Serialization for Fast RPC with Scatter-Gather Reflection](Session-7/zbuffer_zero_copy_and_metadata_free_serialization_for_fast_rpc_with_scatter_gather_reflection.md) | zBuffer：通过 scatter-gather 反射实现快速 RPC 的零拷贝、无元数据序列化 |
| [Scaling GPU-to-CPU Migration for Efficient Distributed Execution on CPU Clusters](Session-7/scaling_gpu_to_cpu_migration_for_efficient_distributed_execution_on_cpu_clusters.md) | 扩展 GPU 到 CPU 的迁移，实现 CPU 集群上的高效分布式执行 |
| [Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters](Session-7/trojan_horse_aggregate_and_batch_for_scaling_up_sparse_direct_solvers_on_gpu_clusters.md) | Trojan Horse：通过聚合与批处理扩展 GPU 集群上的稀疏直接求解器 |

## Session 8: Distributed Training

| English Title | 中文标题 |
| --- | --- |
| [COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training](Session-8/coccl_a_collective_communication_library_supporting_easy_integration_and_configuration_of_customized_compression_for_scalable_llm_training.md) | COCCL：支持便捷集成与配置定制压缩的集合通信库，用于可扩展 LLM 训练 |
| [Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training](Session-8/elastor_elastic_and_efficient_model_partitioning_and_checkpointing_for_fault_tolerant_distributed_training.md) | Elastor：面向容错分布式训练的弹性高效模型划分与检查点 |
| [HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism](Session-8/helixpipe_efficient_distributed_training_of_long_sequence_transformers_with_attention_parallel_pipeline_parallelism.md) | HelixPipe：结合注意力并行与流水线并行，高效分布式训练长序列 Transformer |
| [CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](Session-8/ccl_d_a_high_precision_diagnostic_system_for_slow_and_hang_anomalies_in_large_scale_model_training.md) | CCL-D：大规模模型训练中慢速与挂起异常的高精度诊断系统 |

## Session 9: Parallel Algorithms

| English Title | 中文标题 |
| --- | --- |
| [Pipelonk: Accelerating End-to-End Zero-Knowledge Proof Generation on GPUs for PLONK-Based Protocols](Session-9/pipelonk_accelerating_end_to_end_zero_knowledge_proof_generation_on_gpus_for_plonk_based_protocols.md) | Pipelonk：加速 GPU 上基于 PLONK 协议的端到端零知识证明生成 |
| [ParDiff: Efficiently Parallelizing Reverse-Mode Automatic Differentiation with Direct Indexing](Session-9/pardiff_efficiently_parallelizing_reverse_mode_automatic_differentiation_with_direct_indexing.md) | ParDiff：通过直接索引高效并行化反向模式自动微分 |
| [Faster and Cheaper: Pushing the Sequence Alignment Throughput with Commercial CPUs](Session-9/faster_and_cheaper_pushing_the_sequence_alignment_throughput_with_commercial_cpus.md) | 更快且更经济：利用商用 CPU 提升序列比对吞吐量 |
| [PIM-zd-tree: A Fast Space-Partitioning Index Leveraging Processing-in-Memory](Session-9/pim_zd_tree_a_fast_space_partitioning_index_leveraging_processing_in_memory.md) | PIM-zd-tree：利用近存计算的快速空间划分索引 |

## Session 10: ML Inference

| English Title | 中文标题 |
| --- | --- |
| [BEEMS: Boosting Machine Vision Efficiency via Computation Graph-Based Memory Smoothing](Session-10/beems_boosting_machine_vision_efficiency_via_computation_graph_based_memory_smoothing.md) | BEEMS：基于计算图内存平滑提升机器视觉效率 |
| [Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving](Session-10/laser_unlocking_layer_level_scheduling_for_efficient_multi_slo_llm_serving.md) | Laser：通过层级调度实现高效多 SLO 大语言模型服务 |
| [MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models](Session-10/mixfusion_a_patch_level_parallel_serving_system_for_mixed_resolution_diffusion_models.md) | MixFusion：面向混合分辨率扩散模型的块级并行服务系统 |
| [ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models](Session-10/chitudiffusion_a_data_characteristic_aware_serving_system_for_diffusion_models.md) | ChituDiffusion：数据特征感知的扩散模型服务系统 |

## Session 11: Graphs and Graph Neural Networks

| English Title | 中文标题 |
| --- | --- |
| [ElasGNN: An Elastic Training Framework for Distributed GNN Training](Session-11/elasgnn_an_elastic_training_framework_for_distributed_gnn_training.md) | ElasGNN：分布式 GNN 训练的弹性训练框架 |
| [APERTURE: Algorithm-System Co-optimization for Temporal Graph Network Inference](Session-11/aperture_algorithm_system_co_optimization_for_temporal_graph_network_inference.md) | APERTURE：面向时序图网络推理的算法与系统协同优化 |
| [TAC: Cache-Based System for Accelerating Billion-Scale GNN Training on Multi-GPU Platform](Session-11/tac_cache_based_system_for_accelerating_billion_scale_gnn_training_on_multi_gpu_platform.md) | TAC：基于缓存的多 GPU 十亿级 GNN 训练加速系统 |
| [DTMiner: A Data-Centric System for Efficient Temporal Motif Mining](Session-11/dtminer_a_data_centric_system_for_efficient_temporal_motif_mining.md) | DTMiner：面向高效时序模体挖掘的数据中心系统 |

## Session 12: Optimizing Transformers

| English Title | 中文标题 |
| --- | --- |
| [FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism](Session-12/flashattention_t_towards_fully_tensorized_attention_by_exploiting_tensor_vector_parallelism.md) | FlashAttention-T：利用张量-向量并行实现全张量化注意力 |
| [Accelerating Sparse Transformer Inference on GPU](Session-12/accelerating_sparse_transformer_inference_on_gpu.md) | 加速 GPU 上的稀疏 Transformer 推理 |
| [MetaAttention: A Unified and Performant Attention Framework across Hardware Backends](Session-12/metaattention_a_unified_and_performant_attention_framework_across_hardware_backends.md) | MetaAttention：跨硬件后端的统一高性能注意力框架 |

## Session 13: Matrix and Linear Algebra Algorithms

| English Title | 中文标题 |
| --- | --- |
| [Towards Singular Value Decomposition for Rank-Deficient Matrices: An Efficient and Accurate Algorithm on GPU Architectures](Session-13/towards_singular_value_decomposition_for_rank_deficient_matrices_an_efficient_and_accurate_algorithm_on_gpu_architectures.md) | 面向秩亏矩阵的奇异值分解：GPU 架构上的高效准确算法 |
| [A Diagonal Block Memory-Aware Polynomial Preconditioner for Linear and Eigenvalue Solvers](Session-13/a_diagonal_block_memory_aware_polynomial_preconditioner_for_linear_and_eigenvalue_solvers.md) | 面向线性方程与特征值求解器的对角分块内存感知多项式预条件器 |
| [A Distributed Matrix-Block-Vector Multiplication in Presence of System Performance Variability](Session-13/a_distributed_matrix_block_vector_multiplication_in_presence_of_system_performance_variability.md) | 系统性能波动下的分布式矩阵-块向量乘法 |
| [Characterizing Matrix Multiplication Units across General Parallel Patterns in Scientific Computing](Session-13/characterizing_matrix_multiplication_units_across_general_parallel_patterns_in_scientific_computing.md) | 科学计算通用并行模式下的矩阵乘法单元特征分析 |
