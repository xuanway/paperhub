---
title: "PPoPP 2025 论文集"
description: "PPoPP 2025 官方主会议程的 Session 与论文索引。"
tags:
  - "PPoPP2025"
  - "Computer Systems"
---

# PPoPP 2025

**PPoPP 2025** · 2025年3月1日 - 3月5日 · Las Vegas, NV, USA

本索引依据 [PPoPP 2025 官方主会议程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)整理主会 **11 个 Session、38 篇论文**，按官方场次顺序编排。论文标题以会议论文集及官方议程为准。

各论文页面包含作者、摘要、研究要点、ACM DOI 和官方议程链接。获奖信息按官方议程标注整理。

## 获奖论文

- **Distinguished Paper Award**：[EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs](Session-2/everest_an_effective_and_versatile_runtime_energy_saving_tool_for_gpus.md)
- **Distinguished Paper Award**：[Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures](Session-3/publish_on_ping_a_better_way_to_publish_reservations_in_memory_reclamation_for_concurrent_data_structures.md)
- **Distinguished Paper Award · Best Artifact Award**：[BerryBees: Breadth First Search by Bit-Tensor-Cores](Session-8/berrybees_breadth_first_search_by_bit_tensor_cores.md)

## Session 导航 {#session-nav}

点击 Session 可浏览对应论文、作者与研究要点。

| Session | 中文主题 | Session Chair | 论文数 |
| --- | --- | --- | ---: |
| [Session 1: Graph Neural Networks](Session-1/index.md) | 图神经网络 | Miao Yin | 3 |
| [Session 2: GPU I](Session-2/index.md) | GPU（一） | Xipeng Shen | 3 |
| [Session 3: Concurrent Data Structures and Synchronization I](Session-3/index.md) | 并发数据结构与同步（一） | Yuanhao Wei | 4 |
| [Session 4: Memory](Session-4/index.md) | 内存 | Dong Li | 3 |
| [Session 5: Deep Neural Networks](Session-5/index.md) | 深度神经网络 | Wei Niu | 3 |
| [Session 6: Large Language Models](Session-6/index.md) | 大语言模型 | Minjia Zhang | 3 |
| [Session 7: Scheduling and Resource Management](Session-7/index.md) | 调度与资源管理 | Jie Ren | 3 |
| [Session 8: Tensor Cores](Session-8/index.md) | 张量核 | Jeffrey Vetter | 4 |
| [Session 9: Concurrent Data Structures and Synchronization II](Session-9/index.md) | 并发数据结构与同步（二） | Pengfei Su | 4 |
| [Session 10: GPU II](Session-10/index.md) | GPU（二） | Zhijia Zhao | 4 |
| [Session 11: Parallel Algorithms and Applications](Session-11/index.md) | 并行算法与应用 | Weicong Chen | 4 |

## Session 1: Graph Neural Networks

| English Title | 中文标题 |
| --- | --- |
| [Helios: Efficient Distributed Dynamic Graph Sampling for Online GNN Inference](Session-1/helios_efficient_distributed_dynamic_graph_sampling_for_online_gnn_inference.md) | Helios：面向在线 GNN 推理的高效分布式动态图采样 |
| [Accelerating GNNs on GPU Sparse Tensor Cores through N:M Sparsity-Oriented Graph Reordering](Session-1/accelerating_gnns_on_gpu_sparse_tensor_cores_through_n_m_sparsity_oriented_graph_reordering.md) | 通过面向 N:M 稀疏性的图重排序加速 GPU 稀疏张量核上的 GNN |
| [Adaptive Parallel Training for Graph Neural Networks](Session-1/adaptive_parallel_training_for_graph_neural_networks.md) | 图神经网络的自适应并行训练 |

## Session 2: GPU I

| English Title | 中文标题 |
| --- | --- |
| [RT–BarnesHut: Accelerating Barnes–Hut Using Ray-Tracing Hardware](Session-2/rt_barneshut_accelerating_barnes_hut_using_ray_tracing_hardware.md) | RT–BarnesHut：使用光线追踪硬件加速 Barnes–Hut |
| [EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs](Session-2/everest_an_effective_and_versatile_runtime_energy_saving_tool_for_gpus.md) | EVeREST：高效通用的 GPU 运行时节能工具 |
| [TurboFFT: Co-Designed High-Performance and Fault-Tolerant Fast Fourier Transform on GPUs](Session-2/turbofft_co_designed_high_performance_and_fault_tolerant_fast_fourier_transform_on_gpus.md) | TurboFFT：GPU 上协同设计的高性能容错快速傅里叶变换 |

## Session 3: Concurrent Data Structures and Synchronization I

| English Title | 中文标题 |
| --- | --- |
| [Reciprocating Locks](Session-3/reciprocating_locks.md) | 交替锁 |
| [Aggregating Funnels for Faster Fetch&Add and Queues](Session-3/aggregating_funnels_for_faster_fetch_and_add_and_queues.md) | 聚合式漏斗：加速 Fetch&Add 与队列 |
| [Fairer and More Scalable Reader-Writer Locks by Optimizing Queue Management](Session-3/fairer_and_more_scalable_reader_writer_locks_by_optimizing_queue_management.md) | 通过优化队列管理实现更公平、可扩展的读写锁 |
| [Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures](Session-3/publish_on_ping_a_better_way_to_publish_reservations_in_memory_reclamation_for_concurrent_data_structures.md) | Publish on Ping：并发数据结构内存回收中更优的预约发布方法 |

## Session 4: Memory

| English Title | 中文标题 |
| --- | --- |
| [AC-Cache: A Memory-Efficient Caching System for Small Objects via Exploiting Access Correlations](Session-4/ac_cache_a_memory_efficient_caching_system_for_small_objects_via_exploiting_access_correlations.md) | AC-Cache：利用访问相关性实现的小对象高内存效率缓存系统 |
| [Effectively Virtual Page Prefetching via Spatial-Temporal Patterns for Memory-intensive Cloud Applications](Session-4/effectively_virtual_page_prefetching_via_spatial_temporal_patterns_for_memory_intensive_cloud_applications.md) | 利用时空模式为内存密集型云应用实现有效的虚拟页面预取 |
| [Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion](Session-4/harnessing_inter_gpu_shared_memory_for_seamless_moe_communication_computation_fusion.md) | 利用 GPU 间共享内存实现无缝 MoE 通信-计算融合 |

## Session 5: Deep Neural Networks

| English Title | 中文标题 |
| --- | --- |
| [FlashTensor: Optimizing Tensor Programs by Leveraging Fine-grained Tensor Property](Session-5/flashtensor_optimizing_tensor_programs_by_leveraging_fine_grained_tensor_property.md) | FlashTensor：利用细粒度张量属性优化张量程序 |
| [Mario: Near Zero-cost Activation Checkpointing in Pipeline Parallelism](Session-5/mario_near_zero_cost_activation_checkpointing_in_pipeline_parallelism.md) | Mario：流水线并行中的近零成本激活检查点 |
| [COMPSO: Optimizing Gradient Compression for Distributed Training with Second-Order Optimizers](Session-5/compso_optimizing_gradient_compression_for_distributed_training_with_second_order_optimizers.md) | COMPSO：使用二阶优化器优化分布式训练的梯度压缩 |

## Session 6: Large Language Models

| English Title | 中文标题 |
| --- | --- |
| [MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models](Session-6/marlin_mixed_precision_auto_regressive_parallel_inference_on_large_language_models.md) | MARLIN：大语言模型的混合精度自回归并行推理 |
| [WeiPipe: Weight Pipeline Parallelism for Communication-Effective Long-Context Large Model Training](Session-6/weipipe_weight_pipeline_parallelism_for_communication_effective_long_context_large_model_training.md) | WeiPipe：面向通信高效长上下文大模型训练的权重流水线并行 |
| [ATTNChecker: Highly-Optimized Fault Tolerant Attention for Large Language Model Training](Session-6/attnchecker_highly_optimized_fault_tolerant_attention_for_large_language_model_training.md) | ATTNChecker：面向大语言模型训练的高度优化容错注意力 |

## Session 7: Scheduling and Resource Management

| English Title | 中文标题 |
| --- | --- |
| [SGDRC: Software-Defined Dynamic Resource Control for Concurrent DNN Inference on NVIDIA GPUs](Session-7/sgdrc_software_defined_dynamic_resource_control_for_concurrent_dnn_inference_on_nvidia_gpus.md) | SGDRC：NVIDIA GPU 上并发 DNN 推理的软件定义动态资源控制 |
| [DORADD: Deterministic Parallel Execution in the Era of Microsecond-Scale Computing](Session-7/doradd_deterministic_parallel_execution_in_the_era_of_microsecond_scale_computing.md) | DORADD：微秒级计算时代的确定性并行执行 |
| [WaterWise: Co-optimizing Carbon- and Water-Footprint Toward Environmentally Sustainable Cloud Computing](Session-7/waterwise_co_optimizing_carbon_and_water_footprint_toward_environmentally_sustainable_cloud_computing.md) | WaterWise：协同优化碳与水足迹，迈向环境可持续的云计算 |

## Session 8: Tensor Cores

| English Title | 中文标题 |
| --- | --- |
| [FlashSparse: Minimizing Computation Redundancy for Fast Sparse Matrix Multiplications on Tensor Cores](Session-8/flashsparse_minimizing_computation_redundancy_for_fast_sparse_matrix_multiplications_on_tensor_cores.md) | FlashSparse：减少计算冗余以加速张量核上的稀疏矩阵乘法 |
| [Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores](Session-8/acc_spmm_accelerating_general_purpose_sparse_matrix_matrix_multiplication_with_gpu_tensor_cores.md) | Acc-SpMM：使用 GPU 张量核加速通用稀疏矩阵乘法 |
| [BerryBees: Breadth First Search by Bit-Tensor-Cores](Session-8/berrybees_breadth_first_search_by_bit_tensor_cores.md) | BerryBees：利用位张量核实现广度优先搜索 |
| [FlashFFTStencil: Bridging Fast Fourier Transforms to Memory-Efficient Stencil Computations on Tensor Core Units](Session-8/flashfftstencil_bridging_fast_fourier_transforms_to_memory_efficient_stencil_computations_on_tensor_core_units.md) | FlashFFTStencil：连接快速傅里叶变换与张量核单元上的内存高效 stencil 计算 |

## Session 9: Concurrent Data Structures and Synchronization II

| English Title | 中文标题 |
| --- | --- |
| [PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search](Session-9/panns_enhancing_graph_based_approximate_nearest_neighbor_search_through_recency_aware_construction_and_parameterized_search.md) | PANNS：通过近期性感知构建与参数化搜索增强基于图的近似最近邻搜索 |
| [Balanced Allocations over Efficient Queues: A Fast Relaxed FIFO Queue](Session-9/balanced_allocations_over_efficient_queues_a_fast_relaxed_fifo_queue.md) | 高效队列上的均衡分配：一种快速的松弛 FIFO 队列 |
| [LibRTS: A Spatial Indexing Library by Ray Tracing](Session-9/librts_a_spatial_indexing_library_by_ray_tracing.md) | LibRTS：基于光线追踪的空间索引库 |
| [Crystality: A Programming Model for Smart Contracts on Parallel EVMs](Session-9/crystality_a_programming_model_for_smart_contracts_on_parallel_evms.md) | Crystality：面向并行 EVM 智能合约的编程模型 |

## Session 10: GPU II

| English Title | 中文标题 |
| --- | --- |
| [Popcorn: Accelerating Kernel K-means on GPUs through Sparse Linear Algebra](Session-10/popcorn_accelerating_kernel_k_means_on_gpus_through_sparse_linear_algebra.md) | Popcorn：通过稀疏线性代数加速 GPU 上的 Kernel K-means |
| [Swift Unfolding of Communities: GPU-Accelerated Louvain Algorithm](Session-10/swift_unfolding_of_communities_gpu_accelerated_louvain_algorithm.md) | 社区快速展开：GPU 加速的 Louvain 算法 |
| [GLUMIN: Fast Connectivity Check Based on LUTs For Efficient Graph Pattern Mining](Session-10/glumin_fast_connectivity_check_based_on_luts_for_efficient_graph_pattern_mining.md) | GLUMIN：基于查找表的快速连通性检查，高效进行图模式挖掘 |
| [Improving Tridiagonalization Performance on GPU Architectures](Session-10/improving_tridiagonalization_performance_on_gpu_architectures.md) | 提升 GPU 架构上的三对角化性能 |

## Session 11: Parallel Algorithms and Applications

| English Title | 中文标题 |
| --- | --- |
| [Jigsaw: Toward Conflict-free Vectorized Stencil Computation by Tessellating Swizzled Registers](Session-11/jigsaw_toward_conflict_free_vectorized_stencil_computation_by_tessellating_swizzled_registers.md) | Jigsaw：通过平铺交错寄存器实现无冲突向量化 stencil 计算 |
| [Semi-StructMG: A Fast and Scalable Semi-Structured Algebraic Multigrid](Session-11/semi_structmg_a_fast_and_scalable_semi_structured_algebraic_multigrid.md) | Semi-StructMG：快速可扩展的半结构化代数多重网格 |
| [SBMGT: Scaling Bayesian Multinomial Group Testing](Session-11/sbmgt_scaling_bayesian_multinomial_group_testing.md) | SBMGT：可扩展的贝叶斯多项式群体检测 |
| [An AI-Enhanced 1km-Resolution Seamless Global Weather and Climate Model to Achieve Year-Scale Simulation Speed using 34 Million Cores](Session-11/an_ai_enhanced_1km_resolution_seamless_global_weather_and_climate_model_to_achieve_year_scale_simulation_speed_using_34_million_cores.md) | 利用 AI 增强的 1 公里分辨率无缝全球天气与气候模型，在 3400 万核上实现年尺度模拟速度 |
