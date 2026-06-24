# Design · DAC 2025 (114)

本分类收录 DAC 2025（第62届）Track "Design" 的论文。



## DES1：片上系统、异构架构与可重构架构 (24)

DES1: SoC, Heterogeneous, and Reconfigurable Architectures


### 释放加速器的性能潜力：专用集成电路、现场可编程门阵列与存内计算 (8)

Unleashing the Power of Accelerators: ASICs, FPGAs, and PIMs (8)

- Session Chairs: Amir Fakhim Babaei, Ganapati Bhat

> 本场会议探讨面向人工智能及其他应用场景的创新加速器设计，所依托技术涵盖专用集成电路、软硬件协同设计、现场可编程门阵列以及存内计算等多种技术。会议首先介绍一种面向神经网络处理单元、具备缓存感知能力且支持多租户的深度神经网络加速器。第二篇论文提出一种基于现场可编程门阵列、支持多查询操作的可配置内容可寻址存储器架构。随后进入存内计算加速相关议题，第三篇论文搭建了一套协同仿真环境，用于对存内计算架构与片上网络配置开展设计空间探索；紧接着分享一款全新的基于存内计算的大语言模型加速器。之后将介绍一款内存高效的全同态加密处理单元。本场会议最后由三篇报告收尾，分别介绍面向机器视觉与脑机接口应用的专用加速器。

> This session explores innovative accelerator designs for AI and other applications, leveraging diverse technologies from ASICs and hardware-software co-design to FPGAs and Processing-in-Memory (PIM). The session begins with a cache-aware, multi-tenant DNN accelerator for NPUs. The next paper presents a FPGA-based configurable CAM architecture with multi-query support. Moving to PIM-based acceleration, the next paper explores a co-simulation environment for design space exploration of PIM architectures and Network-on-Chip (NoC) configurations, followed by a presentation on a novel PIM-based LLM accelerator. Next, a memory-efficient Fully Homomorphic Encryption (FHE) processing unit is presented. Finally, the session concludes with three presentations on specialized accelerators targeting vision and brain-computer interface applications.

| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs](camdn_enhancing_cache_efficiency_for_multi_tenant_dnns_on_integrated_npus.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Configurable DSP-Based CAM Architecture for Data-Intensive Applications on FPGAs](configurable_dsp_based_cam_architecture_for_data_intensive_applications_on_fpgas.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [HPIM-NoC: A Priori-Knowledge-Based Optimization Framework for Heterogeneous PIM-Based NoCs](hpim_noc_a_priori_knowledge_based_optimization_framework_for_heterogeneous_pim_based_nocs.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [McPAL: Scaling Unstructured Sparse Inference with Multi-Chiplet HBM-PIM Architecture for LLMs](mcpal_scaling_unstructured_sparse_inference_with_multi_chiplet_hbm_pim_architecture_for_llms.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Hypnos: Memory Efficient Homomorphic Processing Unit](hypnos_memory_efficient_homomorphic_processing_unit.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing Redundant Sorting while Preserving Rasterization Efficiency](gs_tg_3d_gaussian_splatting_accelerator_with_tile_grouping_for_reducing_redundant_sorting_while_preserving_rasterization_efficiency.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [BEVSA: A Real-Time Bird's-Eye-View Semantic Segmentation Accelerator for Multi-Camera System](bevsa_a_real_time_bird_s_eye_view_semantic_segmentation_accelerator_for_multi_camera_system.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [An Energy-Efficient Kalman Filter Architecture with Tunable Accuracy for Brain-Computer Interfaces](an_energy_efficient_kalman_filter_architecture_with_tunable_accuracy_for_brain_computer_interfaces.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |


### 回到未来：速度与效率共生之地 (8)

Back to the Future: Where Speed Meets Efficiency (8)

- Session Chairs: Tianhao Cai, Dirk Stroobandt

> 本场会议聚焦硬件加速领域前沿技术进展，围绕现代芯片架构中的计算、内存访问与并行性优化展开研讨。本次收录论文围绕异构可重构加速器与现场可编程门阵列（FPGA）优化开展相关研究，提出了多种核心计算任务加速创新方案。研讨主题涵盖高效稀疏矩阵乘法、分块间并行计算、自适应树形运算、大数模约简、粗粒度可重构阵列（CGRA）编译器映射策略，以及非易失性FPGA的物理设计。上述研究成果共同印证，硬件架构与算法设计层面的创新正引领高性能计算行业发展，不断拓宽各类应用场景下计算速度、运行能效与可扩展性的性能边界。

> This session explores cutting-edge advancements in hardware acceleration, focusing on optimizing computation, memory access, and parallelism in modern architectures. Featuring research on heterogeneous reconfigurable accelerators and FPGA optimization, the papers highlight novel approaches to accelerating key computational tasks. Topics include efficient sparse matrix multiplication, inter-tile parallelism, adaptive tree computations, large number modular reduction, compiler mapping strategies for CGRAs and physical design for nonvolatile FPGAs. Together, these works demonstrate how innovations in hardware and algorithm design are driving the future of high-performance computing, pushing the boundaries of speed, efficiency, and scalability in diverse applications.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [HeteroSVD: Efficient SVD Accelerator on Versal ACAP with Algorithm-Hardware Co-Design](heterosvd_efficient_svd_accelerator_on_versal_acap_with_algorithm_hardware_co_design.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [VSpGEMM: Exploiting Versal ACAP for High-Performance SpGEMM Acceleration](vspgemm_exploiting_versal_acap_for_high_performance_spgemm_acceleration.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [HiSpTRSV: Exploring Tile-Level Parallelism for SpTRSV Acceleration on FPGAs](hisptrsv_exploring_tile_level_parallelism_for_sptrsv_acceleration_on_fpgas.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [A Data-Centric Hardware Accelerator for Efficient Adaptive Radix Tree](a_data_centric_hardware_accelerator_for_efficient_adaptive_radix_tree.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [ALLMod: Exploring \underline{A}rea-Efficiency of \underline{L}UT-based \underline{L}arge Number \underline{Mod}ular Reduction via Hybrid Workloads](allmod_exploring_underline_a_rea_efficiency_of_underline_l_ut_based_underline_l_arge_number_underline_mod_ular_reduction_via_hybrid_workloads.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [GPS: GNN-Based Two-Stage Pre-Scheduling Loop Mapping Method on CGRAs](gps_gnn_based_two_stage_pre_scheduling_loop_mapping_method_on_cgras.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Rewire: Advancing CGRA Mapping Through a Consolidated Routing Paradigm](rewire_advancing_cgra_mapping_through_a_consolidated_routing_paradigm.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Routability-aware Packing for High-density Nonvolatile FPGAs](routability_aware_packing_for_high_density_nonvolatile_fpgas.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |


### 人工智能、图形处理器与处理器的崛起：新一代架构 (8)

The Rise of AI, GPUs & Processors: The Next-Gen Architectures 

- Session Chairs: Guy Eichler, Sitao Huang

> 本场专题聚焦下一代计算架构演进领域的前沿研究，研究对象涵盖处理器、图形处理器以及人工智能增强型计算系统。相关论文探讨了图形处理器增量划分技术、乱序超标量处理器细粒度指令分析方案，以及面向多模态大语言模型、搭载人工智能扩展模块的多核解决方案。其他研究议题还包括图形处理器子核心高效硬件资源共享、用于微架构设计空间探索的多保真度优化框架（如RISC-V架构）、全新图形处理器内核融合技术，以及张量加速器数据流优化方案。上述研究提出多项创新技术思路，持续突破现代计算系统在性能、可扩展性与能效层面的技术上限。

> This session highlights cutting-edge research on advancing next-gen computing architectures, focusing on processors, GPUs, and AI-enhanced systems. Papers explore incremental partitioning techniques on GPUs, fine-grain instruction analysis in out-of-order superscalar processors, and multi-core solutions with AI extensions for multimodal LLMs. Additional topics include efficient hardware resource sharing in GPU sub-cores, a multi-fidelity optimization framework for microarchitecture design space exploration (e.g., RISCV), new GPU kernel fusion techniques, and dataflow optimizations for tensor accelerators. These works showcase innovative strategies that push the boundaries of performance, scalability, and efficiency in modern computing systems.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [iG-kway: Incremental k-way Graph Partitioning on GPU](ig_kway_incremental_k_way_graph_partitioning_on_gpu.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [FireGuard: A Generalized Microarchitecture for Fine-Grained Security Analysis on OoO Superscalar Cores](fireguard_a_generalized_microarchitecture_for_fine_grained_security_analysis_on_ooo_superscalar_cores.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [EdgeMM: Multi-Core CPU with Heterogeneous AI-Extension and Activation-aware Weight Pruning for Multimodal LLMs at Edge](edgemm_multi_core_cpu_with_heterogeneous_ai_extension_and_activation_aware_weight_pruning_for_multimodal_llms_at_edge.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [ACRS: Adjacent Computation Resource Sharing among Partitioned GPU Sub-Cores](acrs_adjacent_computation_resource_sharing_among_partitioned_gpu_sub_cores.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Swift or Exact? Boosting Efficient Microarchitecture DSE via Multi-fidelity Partial Order Prediction](swift_or_exact_boosting_efficient_microarchitecture_dse_via_multi_fidelity_partial_order_prediction.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [Principle-based Dataflow Optimization for Communication Lower Bound in Operator-Fused Tensor Accelerator](principle_based_dataflow_optimization_for_communication_lower_bound_in_operator_fused_tensor_accelerator.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [GoPTX: Fine-grained GPU Kernel Fusion by PTX-level Instruction Flow Weaving](goptx_fine_grained_gpu_kernel_fusion_by_ptx_level_instruction_flow_weaving.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |
| [DARIS: An Oversubscribed Spatio-Temporal Scheduler for Real-Time DNN Inference on GPUs](daris_an_oversubscribed_spatio_temporal_scheduler_for_real_time_dnn_inference_on_gpus.md) | DES1: SoC, Heterogeneous, and Reconfigurable Architectures |





## DES2A：存内计算与近存计算电路 (12)

DES2A: In-memory and Near-memory Computing Circuits 

### 加速器设计领域的突破创新：光子、时域与安全导向型人工智能 (6)

Breaking Boundaries in Accelerator Design: Photonic, Time-Domain, and Security-Driven AI (6)

- Session Chairs: Yu Cao, Sumitha George

> 人工智能加速技术的发展已突破传统硅基方案，衍生出光子架构、时域处理架构以及安全增强型架构等全新技术路线。本场专题将展示多项前沿突破成果，包括高速光子张量核心、非线性时域处理技术、基于铁电场效应晶体管（FeFET）的硬件安全方案，以及面向大语言模型（LLM）与组合优化任务的专用AI加速器。上述创新方案依托全新计算范式，持续拓宽AI硬件在运算性能、能效与硬件安全层面的技术边界。

> AI acceleration is evolving beyond conventional silicon, embracing photonic, time-domain, and security-enhanced architectures. This session showcases breakthroughs in high-speed photonic tensor cores, nonlinear time-domain processing, FeFET-based security solutions, and specialized AI accelerators for LLMs and combinatorial optimization. By leveraging novel computing paradigms, these innovations push the boundaries of performance, efficiency, and security in AI hardware design.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference](unicaim_a_unified_cam_cim_architecture_with_static_dynamic_kv_cache_pruning_for_efficient_long_context_llm_inference.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [P-DAC: Power-Efficient Photonic Accelerators for LLM Inference](p_dac_power_efficient_photonic_accelerators_for_llm_inference.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [A PulseWidth-IN-PulseWidth-Out Universal Nonlinear Processing Element for Time-Domain In-Memory Computing Systems](a_pulsewidth_in_pulsewidth_out_universal_nonlinear_processing_element_for_time_domain_in_memory_computing_systems.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [PUFiM: A Robust and Efficient FeFET-Based Security Solution Merging Physical Unclonable Function with Compute-in-Memory for Edge AI](pufim_a_robust_and_efficient_fefet_based_security_solution_merging_physical_unclonable_function_with_compute_in_memory_for_edge_ai.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [TAXI: Traveling Salesman Problem Accelerator with X-bar-based Ising Macros Powered by SOT-MRAMs and Hierarchical Clustering](taxi_traveling_salesman_problem_accelerator_with_x_bar_based_ising_macros_powered_by_sot_mrams_and_hierarchical_clustering.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [A Mixed-Signal Photonic SRAM-based High-Speed Energy-Efficient Photonic Tensor Core with Novel Electro-Optic ADC](a_mixed_signal_photonic_sram_based_high_speed_energy_efficient_photonic_tensor_core_with_novel_electro_optic_adc.md) | DES2A: In-memory and Near-memory Computing Circuits |



### 燃动人工智能时代：面向下一代存内计算与无乘法加速技术 (6)

AI on Fire: Compute-in-Memory and Multiplication-Free Acceleration for the Next Era

- Session Chairs: Ibrahim (Abe) Elfadel, Akhilesh Jaiswal

> 人工智能硬件正处于发展转折点，行业亟需能效与性能的跨越式革新。本次专题将深入探讨突破性存内计算（CIM）架构、无乘法加速技术以及全新运算范式，这类技术可大幅降低功耗与延迟，同时提升数据吞吐能力。从基于查找表的深度神经网络加速器、混合模数计算，到搭载自旋转移矩磁随机存储器（STT-MRAM）的存内计算方案，一系列创新技术正为人工智能硬件开辟全新发展空间。

> AI hardware is at an inflection point, demanding radical efficiency and performance leaps. This session dives into groundbreaking compute-in-memory (CIM) architectures, multiplication-free acceleration, and novel arithmetic paradigms that slash power and latency while boosting throughput. From LUT-based DNN accelerators to hybrid analog-digital computing and STT-MRAM-powered CIM, these innovations are setting AI hardware ablaze with new possibilities.

| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [High Energy-efficiency and Low latency In-Memory Computing using Analog Accumulator and In-Memory ADC with shared References](high_energy_efficiency_and_low_latency_in_memory_computing_using_analog_accumulator_and_in_memory_adc_with_shared_references.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [CREST-CiM: Cross-Coupling-Enhanced Differential STT-MRAM for Robust Computing-in-Memory in Binary Neural Networks](crest_cim_cross_coupling_enhanced_differential_stt_mram_for_robust_computing_in_memory_in_binary_neural_networks.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [YOCO: A Hybrid In-Memory Computing Architecture with 8-bit Sub-PetaOps/W In-Situ Multiply Arithmetic for Large-Scale AI](yoco_a_hybrid_in_memory_computing_architecture_with_8_bit_sub_petaops_w_in_situ_multiply_arithmetic_for_large_scale_ai.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [ReSMiPS: A ReRAM-based Sparse Mixed-precision Solver with Fast Matrix Reordering Algorithm](resmips_a_reram_based_sparse_mixed_precision_solver_with_fast_matrix_reordering_algorithm.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [Lookup Table-based Multiplication-free All-digital DNN Accelerator Featuring Self-Synchronous Pipeline Accumulation](lookup_table_based_multiplication_free_all_digital_dnn_accelerator_featuring_self_synchronous_pipeline_accumulation.md) | DES2A: In-memory and Near-memory Computing Circuits |
| [WISEDRAM: A Reliable Bitwise In-DRAM Accelerator](wisedram_a_reliable_bitwise_in_dram_accelerator.md) | DES2A: In-memory and Near-memory Computing Circuits |


## DES2B：存内计算与近存计算架构、应用及系统 (34)

DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems 

### 答案藏于内存技术？只是存进内存？单单靠内存？点此文揭晓答案！(6)

The Answer Is In-memory!? In the Memory? Memory? Find Out Here! 

- Session Chairs: Marco Donato, Giacomo Pedretti

> 随着各类数据密集型应用不断将传统计算推向性能极限，存内计算作为一种变革性计算范式应运而生，用以攻克关键的内存墙瓶颈。本次专题将探讨存内计算架构领域的前沿技术进展，展示其在人工智能加速、大规模相似度检索、布尔可满足性问题求解三大方向实现技术革新的潜力。我们将深入剖析多款创新解决方案：基于NAND闪存与动态随机存储器（采用UPMEM方案）的高能效向量检索、自适应混合信号存内布尔可满足性求解器，以及基于内容可寻址存储器、查找表的新型硬件加速器。本专题同时介绍多款业界顶尖仿真框架与随机计算技术，这类技术可大幅提升系统可编程性与运行能效。

> As data-intensive applications push conventional computing to its limits, in-memory computing emerges as a transformative paradigm to overcome critical memory bottlenecks. This session explores cutting-edge advances in compute-in-memory architectures, showcasing their potential to revolutionize AI acceleration, large-scale similarity search, and Boolean satisfiability solving. We delve into innovative solutions including energy-efficient vector search in NAND flash and DRAM (using UPMEM), adaptive mixed-signal in-memory SAT solvers, and novel CAM- and LUT-based accelerators. The session also highlights state-of-the-art simulation frameworks and stochastic computing techniques that significantly enhance programmability and efficiency.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [FeKAN: Efficient Kolmogorov-Arnold Networks Accelerator Using FeFET-based CAM and LUT](fekan_efficient_kolmogorov_arnold_networks_accelerator_using_fefet_based_cam_and_lut.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Energy-Efficient Large-Scale Vector Similarity Search in NAND-Flash via Hybrid Matching](energy_efficient_large_scale_vector_similarity_search_in_nand_flash_via_hybrid_matching.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Chameleon-SAT: An Adaptive Boolean Satisfiability Accelerator Using Mixed-Signal In-Memory Computing for Versatile SAT Problems](chameleon_sat_an_adaptive_boolean_satisfiability_accelerator_using_mixed_signal_in_memory_computing_for_versatile_sat_problems.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning](a_full_system_programmable_and_extensible_in_memory_computing_simulation_framework_for_deep_learning.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [All-in-memory Stochastic Computing using ReRAM](all_in_memory_stochastic_computing_using_reram.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [UPVSS: Jointly Managing Vector Similarity Search with Near-Memory Processing Systems](upvss_jointly_managing_vector_similarity_search_with_near_memory_processing_systems.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |


### 直击核心、直观可视、清晰表述：新一代人工智能处理技术 (6)

Spike It, See It, Say It: Next-Gen AI Processing 


- Session Chairs: Xueqing Li, Wantong Li

> 本章节探讨新一代硬件架构如何突破内存墙瓶颈，为新兴人工智能系统加速大语言模型、计算机视觉与神经形态计算。第一篇论文提出一款神经形态（基于脉冲）处理器，该处理器采用脉冲追踪双极性积分发放神经元；第二篇论文提出集成图像传感与近传感器磁阻随机存储器（MRAM）处理一体化架构；最后四篇论文呈现前沿研究成果，围绕边缘设备上视觉Transformer（ViT）与大语言模型（LLM）开展算法-硬件协同设计，拓宽边缘人工智能的性能边界，为资源受限场景下视觉与语言模型的高效部署提供全新研究方向。

> This section explores how next-generation hardware architectures are breaking the memory wall to accelerate large language models, computer vision, and neuromorphic computing for emerging AI systems. The first paper proposes a neuromorphic (spike-based) processor, which leverages spike-tracing bipolar-integrate-and-fire neurons. The second paper proposes an integrated image sensing and near-sensor MRAM-based processing architecture. The last four papers present cutting-edge research contributions addressing algorithm-hardware co-design for vision transformers (ViTs) and large language models (LLMs) on edge devices, pushing the boundaries of edge AI, offering new directions for efficient deployment of vision and language models in resource-constrained environments.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [BiNeuroRAM: Energy-Efficient ReRAM-Based PIM for Accurate Bipolar Spiking Neural Network Acceleration](bineuroram_energy_efficient_reram_based_pim_for_accurate_bipolar_spiking_neural_network_acceleration.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [ResISC: Residue Number System-Based Integrated Sensing and Computing for Efficient Edge AI](resisc_residue_number_system_based_integrated_sensing_and_computing_for_efficient_edge_ai.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Efficient Edge Vision Transformer Accelerator with Decoupled Chunk Attention and Hybrid Computing-In-Memory](efficient_edge_vision_transformer_accelerator_with_decoupled_chunk_attention_and_hybrid_computing_in_memory.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [3D-CIMlet: A Chiplet Co-Design Framework for Heterogeneous In-Memory Acceleration of Edge LLM Inference and Continual Learning](3d_cimlet_a_chiplet_co_design_framework_for_heterogeneous_in_memory_acceleration_of_edge_llm_inference_and_continual_learning.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [BlockPIM: Optimizing Memory Management for PIM-enabled Long-Context LLM Inference](blockpim_optimizing_memory_management_for_pim_enabled_long_context_llm_inference.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [PIMPAL: Accelerating LLM Inference on Edge Devices via In-DRAM Arithmetic Lookup](pimpal_accelerating_llm_inference_on_edge_devices_via_in_dram_arithmetic_lookup.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |

### 存储与算力深度融合，赋能人工智能发展、提升数据处理效率 (8)

Storage Meets Computing Power for Advancing AI and Data Processing Efficiency (8)



- Session Chairs: Arman Roohi, Abhronil Sengupta

> 存内计算（CIM）正逐步发展为一种可实现高效人工智能加速的变革性技术，能够解决数据传输、能效以及计算瓶颈等各类难题。随着图神经网络、点云模型等多种网络拓扑结构推动深度学习持续发展，存内计算架构与配套框架正针对从边缘设备到数据中心的各类应用场景完成优化。本次专题研讨将探究面向k近邻检索、图神经网络、点云神经网络等任务的新型存内计算加速器，同时介绍适用于边缘人工智能的混合存内计算解决方案。此外，内容还涵盖神经网络模型的各类优化方法，并提供一套用于搭建与评测存内计算平台的系统化框架。

> Compute-in-Memory (CIM) is emerging as a transformative approach for efficient AI acceleration, addressing challenges in data movement, energy efficiency, and computational bottlenecks. As deep learning evolves with diverse network topologies like GNNs and point-cloud models, CIM architectures and frameworks are being optimized for a wide range of use cases, from edge devices to data centers. This session explores novel CIM-based accelerators for tasks such as kNN search, graph neural networks, and point cloud neural networks, alongside hybrid CIM solutions for edge AI. It also covers optimization techniques for neural network models and presents a systematic framework for implementing and evaluating CIM platforms.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [PICK: An SRAM-based Processing-in-Memory Accelerator for K-Nearest-Neighbor Search in Point Clouds*](pick_an_sram_based_processing_in_memory_accelerator_for_k_nearest_neighbor_search_in_point_clouds.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [HH-PIM: Dynamic Optimization of Power and Performance with Heterogeneous-Hybrid PIM for Edge AI Devices](hh_pim_dynamic_optimization_of_power_and_performance_with_heterogeneous_hybrid_pim_for_edge_ai_devices.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Anchor First, Accelerate Next: Revolutionizing GNNs with PIM by Harnessing Stationary Data](anchor_first_accelerate_next_revolutionizing_gnns_with_pim_by_harnessing_stationary_data.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [3D-SubG: A 3D Stacked Hybrid Processing Near/In-Memory Accelerator for Subgraph GNNs](3d_subg_a_3d_stacked_hybrid_processing_near_in_memory_accelerator_for_subgraph_gnns.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [PIMDup: An Optimized Deduplication Design on a Real Processing-in-Memory System](pimdup_an_optimized_deduplication_design_on_a_real_processing_in_memory_system.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [An Efficient Compute-in-Memory based Accelerator for Point-based Point Cloud Neural Networks](an_efficient_compute_in_memory_based_accelerator_for_point_based_point_cloud_neural_networks.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [NDFT: Accelerating Density Functional Theory Calculations via Hardware/Software Co-Design on Near-Data Computing System](ndft_accelerating_density_functional_theory_calculations_via_hardware_software_co_design_on_near_data_computing_system.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [CIMFlow: An Integrated Framework for Systematic Design and Evaluation of Digital CIM Architectures](cimflow_an_integrated_framework_for_systematic_design_and_evaluation_of_digital_cim_architectures.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |


### 厌倦人工智能？面向机器学习之外应用的以内存为中心计算技术 (6)

Need a Break from AI? Memory-centric Computing for Beyond Machine Learning Application

- Session Chairs: Shaahin Angizi, Dinesh Somasekhar

> 近存计算加速与存内计算加速正成为解决数据密集型任务算力瓶颈的主流高效计算范式，其应用场景已超越机器学习领域。本次专题将追溯该技术的发展本源，聚焦存内加速器、近存加速器与存储加速器这类非传统计算架构，探讨面向机器学习以外各类应用的加速方案。具体而言，专题收录的论文涵盖向量相似度检索加速、全同态加密、映射与调度优化算法，以及搭载指令集扩展的缓存内加速器等多个研究方向。

> Near-memory and in-memory acceleration are emerging as powerful paradigms for addressing computational bottlenecks in data-intensive tasks and have applications beyond ML. This session, a fresh look at the roots, covers acceleration of beyond ML applications using unconventional computing architectures with a focus on in-memroy, near-memory and storage accelerators. More specifically, it includes papers ranging from acceleration of vector similarity search, fully homomorphic encryption, algorithms for mapping and scheduling optimization, and in-cache accelerators with ISA extension.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection](ares_high_performance_near_storage_accelerator_for_fhe_based_private_set_intersection.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [GraphAccel: An In-Storage Accelerator for Efficient Graph-Based Vector Similarity Search Using Page Packing and Speculative Search Optimization](graphaccel_an_in_storage_accelerator_for_efficient_graph_based_vector_similarity_search_using_page_packing_and_speculative_search_optimization.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [CIM-BLAS: Computing-in-Memory Accelerator for BLAS](cim_blas_computing_in_memory_accelerator_for_blas.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Segmented Angular Pre-Processing for Accurate and Efficient In-Memory Vector Similarity Search](segmented_angular_pre_processing_for_accurate_and_efficient_in_memory_vector_similarity_search.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Efficient Weight Mapping and Resource Scheduling on Crossbar-based Multi-core CIM Systems](efficient_weight_mapping_and_resource_scheduling_on_crossbar_based_multi_core_cim_systems.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [ARCANE: Adaptive RISC-V Cache Architecture for Near-memory Extensions](arcane_adaptive_risc_v_cache_architecture_for_near_memory_extensions.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |


### 突破壁垒：面向Transformer加速的存内计算技术 (8)

Breaking Barriers: Compute-in-Memory for Transformer Acceleration (8)


- Session Chairs: Steve Dai, Haitong Li

> 本场会议聚焦存内计算（CIM）架构领域具有突破性的创新技术，该架构旨在加速大规模Transformer模型运算，缓解数据传输瓶颈。内容涵盖多种优化方案，既有面向大语言模型（LLM）注意力计算的存内计算解决方案，也包含适配长上下文推理的高效内存管理方案。会议深入探讨软硬件协同设计技术，包括非规则注意力稀疏化、异常值感知量化、混合专家（MoE）架构、三维混合键合技术以及新型异步执行方案。

> This session highlights groundbreaking innovations in Compute-in-Memory (CIM) architectures designed to accelerate large-scale transformer models and alleviate data transfer bottlenecks. It covers various optimization strategies, from CIM-based solutions for attention computation in large language models (LLMs) to efficient memory management for long-context inference. The session delves into software-hardware co-design techniques, including irregular attention sparsity, outlier-aware quantization, Mixture-of-Experts (MoE) approaches, 3D hybrid bonding, and novel asynchronous execution methods.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [DIAS: Distance-based Attention Sparsity for Ultra-Long-Sequence Transformer with Tree-like Processing-in-Memory Architecture](dias_distance_based_attention_sparsity_for_ultra_long_sequence_transformer_with_tree_like_processing_in_memory_architecture.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [AttenPIM: Accelerating LLM Attention with Dual-mode GEMV in Processing-in-Memory](attenpim_accelerating_llm_attention_with_dual_mode_gemv_in_processing_in_memory.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [SplitSync: Bank Group-Level Split-Synchronization for High-Performance DRAM PIM](splitsync_bank_group_level_split_synchronization_for_high_performance_dram_pim.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [PIMoE: Towards Efficient MoE Transformer Deployment on NPU-PIM System through Throttle-Aware Task Offloading](pimoe_towards_efficient_moe_transformer_deployment_on_npu_pim_system_through_throttle_aware_task_offloading.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Supporting Register-based Addressing Modes for in-DRAM PIM ISAs](supporting_register_based_addressing_modes_for_in_dram_pim_isas.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [OutlierCIM: Outlier-Aware Digital CIM-Based LLM Accelerator with Hybrid-Strategy Quantization and Unified FP-INT Computation](outliercim_outlier_aware_digital_cim_based_llm_accelerator_with_hybrid_strategy_quantization_and_unified_fp_int_computation.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [Near-Memory LLM Inference Processor based on 3D DRAM-to-logic Hybrid Bonding](near_memory_llm_inference_processor_based_on_3d_dram_to_logic_hybrid_bonding.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |
| [SeIM: In-Memory Acceleration for Approximate Nearest Neighbor Search](seim_in_memory_acceleration_for_approximate_nearest_neighbor_search.md) | DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems |


## DES3：新型计算模型 (8)

DES3: Emerging Models of ComputatioN

### 面向机器学习及更多领域的模型与硬件 (8)

Models and Hardware for Machine Learning and Beyond

- Session Chairs: Cheng Wang, Jun Shiomi

> 本次研讨将展示八篇面向新型计算模型的硬件与算法设计相关研究成果，覆盖人工智能、机器学习、神经形态计算、生物信息学、近似计算、生物芯片等诸多领域。入选成果面向通用人工智能与机器学习应用，提出了创新算法与硬件架构，同时涵盖向量符号人工智能这类专用人工智能模型。这些成果集中展示了多样化的计算技术，剖析了各类新兴计算范式当前面临的挑战，并介绍了领域内最前沿的解决方案。

> In this session, we will present eight works on hardware and algorithm design for emerging computing models. These span a wide range of areas, including AI, machine learning, neuromorphic computing, bioinformatics, approximate computing, and biochips. The selected works feature novel algorithms and hardware architectures for both general AI and machine learning applications, as well as specialized AI models such as vector symbolic AI. Together, they showcase a diverse array of computing techniques, highlighting the challenges and state-of-the-art solutions within these evolving paradigms.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [Pipirima: Predicting Patterns in Sparsity to Accelerate Matrix Algebra](pipirima_predicting_patterns_in_sparsity_to_accelerate_matrix_algebra.md) | DES3: Emerging Models of ComputatioN |
| [FactorHD: A Hyperdimensional Computing Model for Multi-Object Multi-Class Representation and Factorization](factorhd_a_hyperdimensional_computing_model_for_multi_object_multi_class_representation_and_factorization.md) | DES3: Emerging Models of ComputatioN |
| [Holistic Design towards Resource-Stringent Binary Vector Symbolic Architecture](holistic_design_towards_resource_stringent_binary_vector_symbolic_architecture.md) | DES3: Emerging Models of ComputatioN |
| [SDISC: A Spike-Driven Human-Machine Interface with In-Situ Computing for Real-Time Low-Power Interaction](sdisc_a_spike_driven_human_machine_interface_with_in_situ_computing_for_real_time_low_power_interaction.md) | DES3: Emerging Models of ComputatioN |
| [ANGraph: A GNN-Based Performance Prediction Framework for Asynchronous Neuromorphic Hardware](angraph_a_gnn_based_performance_prediction_framework_for_asynchronous_neuromorphic_hardware.md) | DES3: Emerging Models of ComputatioN |
| [PairGraph: An Efficient Search-space-aware Accelerator for High-performance Concurrent Pairwise Queries](pairgraph_an_efficient_search_space_aware_accelerator_for_high_performance_concurrent_pairwise_queries.md) | DES3: Emerging Models of ComputatioN |
| [PreDAC: An Efficient Framework of Pre-Refining Enhanced Design Space Exploration for Approximate Computing](predac_an_efficient_framework_of_pre_refining_enhanced_design_space_exploration_for_approximate_computing.md) | DES3: Emerging Models of ComputatioN |
| [AutoRE: Bayesian-Optimization-based Automatic Reliability Enhancement Tool for Flow-based Microfluidic Biochips](autore_bayesian_optimization_based_automatic_reliability_enhancement_tool_for_flow_based_microfluidic_biochips.md) | DES3: Emerging Models of ComputatioN |


## DES4：数字与模拟电路 (8)

DES4: Digital and Analog Circuits (8)

### 超大规模集成电路领域的突破：高能效人工智能与革命性电路技术 (8)

Breakthroughs in VLSI: Power-Efficient AI and Revolutionary Circuitry

- Session Chairs: Ioannis Savidis, Kishor Kunal

> 本场专题会议汇集了超大规模集成电路设计、能效优化、人工智能驱动设计自动化以及先进电路领域内的突破性研究与创新成果。会议旨在研讨各类突破技术、电路与系统现有极限的前沿进展，议题涵盖深度神经网络加速器、人工智能驱动设计自动化以及模拟电路设计创新。同时，会议还介绍数字设计领域各类新型节能技术，包括面向机器人感知的概率量子隧穿技术、多功能背面金属层，以及适用于RISC-V内核与视频编码的低功耗解决方案。本次会议全面梳理了塑造半导体技术与电子设计未来的各类挑战、研究方法及重大技术突破。

> This session brings together groundbreaking research and innovative advancements in the fields of VLSI design, power efficiency, AI-driven design automation, and advanced circuitry. The goal is to explore and discuss the latest developments that are pushing the boundaries of technology, circuits, and systems. The session presents topics on DNN accelerators, AI-driven design automation, and innovations in analog circuit design. The session also covers new energy efficient technologies in digital design, including probabilistic quantum tunneling for robotic perception and multifunctional backside metal layers, as well as energy-efficient solutions for RISC-V cores and video coding. It provides a comprehensive overview into the challenges, methodologies, and breakthroughs shaping the future of semiconductor technology and electronic design.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [EPIC: Error PredIction and Correction for Power-Efficient Voltage Underscaling Multiply-Accumulate Unit](epic_error_prediction_and_correction_for_power_efficient_voltage_underscaling_multiply_accumulate_unit.md) | DES4: Digital and Analog Circuits |
| [PoP-ECC: Robust and Flexible Error Correction against Multi-Bit Upsets in DNN Accelerators](pop_ecc_robust_and_flexible_error_correction_against_multi_bit_upsets_in_dnn_accelerators.md) | DES4: Digital and Analog Circuits |
| [AdreamDCO: AI-Driven Robust and Efficient Design Automation for Digitally Controlled Oscillators](adreamdco_ai_driven_robust_and_efficient_design_automation_for_digitally_controlled_oscillators.md) | DES4: Digital and Analog Circuits |
| [EVA: An Efficient and Versatile Generative Engine for Targeted Discovery of Novel Analog Circuits](eva_an_efficient_and_versatile_generative_engine_for_targeted_discovery_of_novel_analog_circuits.md) | DES4: Digital and Analog Circuits |
| [BS-PDN-Last: Towards Optimal Power Delivery Network Design With Multifunctional Backside Metal Layers](bs_pdn_last_towards_optimal_power_delivery_network_design_with_multifunctional_backside_metal_layers.md) | DES4: Digital and Analog Circuits |
| [Towards Uncertainty-aware Robotic Perception via Mixed-signal BNN Engine Leveraging Probabilistic Quantum Tunneling](towards_uncertainty_aware_robotic_perception_via_mixed_signal_bnn_engine_leveraging_probabilistic_quantum_tunneling.md) | DES4: Digital and Analog Circuits |
| [Dual-Issue Execution of Mixed Integer and Floating-Point Workloads on Energy-Efficient In-Order RISC-V Cores](dual_issue_execution_of_mixed_integer_and_floating_point_workloads_on_energy_efficient_in_order_risc_v_cores.md) | DES4: Digital and Analog Circuits |
| [A High-Precision and Low-Cost Approximate Transform Accelerator for Video Coding](a_high_precision_and_low_cost_approximate_transform_accelerator_for_video_coding.md) | DES4: Digital and Analog Circuits |


## DES5：新兴器件与互连技术 (8)

DES5: Emerging Device and Interconnect Technologies

### 塑造未来：协同研发面向计算领域及更广范畴的新兴技术 (8)

Shaping Tomorrow: Co-Designing Emerging Technologies for Computing and Beyond 



- Session Chairs: Xunzhao Yin, Doo Seok Jeong

> 人工智能与计算技术飞速迭代，亟需融合硬件、算法与系统的创新协同设计方案。本场专题研讨聚焦新兴技术与协同设计方法交叉领域的前沿研究，研讨议题包含抗漂移神经网络、高速互联标准（CXL，计算快速互联）优化、铁电与自旋轨道力矩磁随机存取存算一体架构、单片三维集成，以及面向生物医学诊断的传感器内计算技术。相关研究围绕能效、可扩展性、性能等行业痛点展开攻关，充分印证协同设计能够释放人工智能及其他领域先进技术的全部潜力，为下一代计算系统的发展奠定基础。

> The rapid evolution of AI and computing demands innovative co-design approaches that integrate hardware, algorithms, and systems. This session explores cutting-edge research at the intersection of emerging technologies and co-design methodologies. Topics include drift-tolerant neural networks, Compute Express Link (CXL) optimization, ferroelectric and SOT-MRAM compute-in-memory architectures, monolithic 3D integration and in-sensor computing for biomedical diagnostics. By addressing challenges such as energy efficiency, scalability, and performance, these works showcase how co-design can unlock the full potential of advanced technologies for AI and other domains, paving the way for next-generation computing systems.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [DBC: Drift-aware Binary Code for Drift-tolerant Deep Neural Networks](dbc_drift_aware_binary_code_for_drift_tolerant_deep_neural_networks.md) | DES5: Emerging Device and Interconnect Technologies |
| [CXL-Interplay: Unraveling and Characterizing CXL Interference in Modern Computer Systems](cxl_interplay_unraveling_and_characterizing_cxl_interference_in_modern_computer_systems.md) | DES5: Emerging Device and Interconnect Technologies |
| [VQT-CiM: Accelerating Vector Quantization Enhanced Transfomer with Ferroelectric Compute-in-Memory](vqt_cim_accelerating_vector_quantization_enhanced_transfomer_with_ferroelectric_compute_in_memory.md) | DES5: Emerging Device and Interconnect Technologies |
| [Enhancing Parallelism and Energy-Efficiency in SOT-MRAM based CIM Architecture for On-Chip Learning](enhancing_parallelism_and_energy_efficiency_in_sot_mram_based_cim_architecture_for_on_chip_learning.md) | DES5: Emerging Device and Interconnect Technologies |
| [Device-Algorithm Co-Design of Ferroelectric Compute-in-Memory In-Situ Annealer for Combinatorial Optimization Problems](device_algorithm_co_design_of_ferroelectric_compute_in_memory_in_situ_annealer_for_combinatorial_optimization_problems.md) | DES5: Emerging Device and Interconnect Technologies |
| [DANN: Diffractive Acoustic Neural Network for in-sensor computing system target at multi-biomarker diagnosis](dann_diffractive_acoustic_neural_network_for_in_sensor_computing_system_target_at_multi_biomarker_diagnosis.md) | DES5: Emerging Device and Interconnect Technologies |
| [333-eDRAM - 3T Embedded DRAM Leveraging Monolithic 3D Integration of 3 Transistor Types: IGZO, Carbon Nanotube and Silicon FETs](333_edram_3t_embedded_dram_leveraging_monolithic_3d_integration_of_3_transistor_types_igzo_carbon_nanotube_and_silicon_fets.md) | DES5: Emerging Device and Interconnect Technologies |
| [Monolithic 3D FPGA Design and Synthesis with Back-End-of-Line Configuration Memories](monolithic_3d_fpga_design_and_synthesis_with_back_end_of_line_configuration_memories.md) | DES5: Emerging Device and Interconnect Technologies |


## DES6：量子计算 (20)

DES6: Quantum Computing 



### 量子电路的核心构建基石：综合、仿真与编译 (6)

Building Pillars of Quantum Circuits: Synthesis, Simulation & Compilation 

- Session Chairs: Alberto Marchisio, Zhiding Liang

> 本次研讨环节围绕量子计算线路综合、量子编译、量子线路仿真以及新型工具开发领域的全新研究成果展开探讨。第一篇论文提出一种融合ZX演算、线路划分与线路综合的全新方法，用于生成量子线路中的脉冲信号。量子布局综合（QLS）是量子程序编译的核心关键步骤；第二篇论文构建了一套已知最优交换门（SWAP）数量的基准测试集，可作为评估框架与研究工具，推动量子布局综合领域的技术发展。图态是一类高纠缠量子态，也是量子信息处理的核心资源，为此第三篇论文基于分治策略，提出一套面向量子发射源-光子图态生成的全新编译框架。第四篇论文设计了一套高效编译框架，该框架主要基于高层泡利基中间表示（IR）处理通用哈密顿量仿真程序，打通具备实用价值的量子应用与可物理实现方案之间的技术壁垒。经典计算机对量子线路的仿真始终是量子计算研究的核心工具，可用于量子算法开发、验证以及经典计算机性能对比；因此第五、第六篇论文分别研究基于联合切割、跨平台（中央处理器CPU、英伟达显卡Nvidia GPU）优化并搭载高性能后端的高效薛定谔形式仿真方案。

> This discussion session discusses new research contributions in quantum computing synthesis, quantum compilation, quantum circuit simulation, and novel tool development. The first paper proposes a novel approach combining ZX-Calculus, circuit partitioning, and circuit synthesis for pulse generation in quantum circuits. Quantum layout synthesis (QLS) is a critical step in quantum program compilation; the second paper introduces a benchmark with a known optimal SWAP count that will work as an evaluation framework and a tool for advancing QLS research. Graph state is a highly entangled quantum state and is a critical resource; therefore, the third paper proposes a novel compilation framework for emitter-photonic graph state generation, leveraging a divide-and-conquer strategy. The fourth paper proposes a highly effective compilation framework that primarily operates at the high-level Pauli-based intermediate representation (IR) for generic Hamiltonian simulation programs, thereby bridging the gap between impactful quantum applications and physically implementable solutions. Classical simulation of quantum circuits remains a central tool for quantum computing research—including developing and testing quantum algorithms as well as comparing classical computers; therefore, the fifth and sixth papers discuss efficient methods for Schrödinger-style simulations based on joint cutting and cross-platform (CPU and Nvidia GPU) optimization and high-performance backend support.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [EPOC: A Novel Pulse Generation Framework Incorporating Advanced Synthesis Techniques for Quantum Circuits](epoc_a_novel_pulse_generation_framework_incorporating_advanced_synthesis_techniques_for_quantum_circuits.md) | DES6: Quantum Computing |
| [Assessing Quantum Layout Synthesis Tools via Known Optimal-SWAP Cost Benchmarks](assessing_quantum_layout_synthesis_tools_via_known_optimal_swap_cost_benchmarks.md) | DES6: Quantum Computing |
| [A Scalable and Robust Compilation Framework for Emitter-Photonic Graph State](a_scalable_and_robust_compilation_framework_for_emitter_photonic_graph_state.md) | DES6: Quantum Computing |
| [Phoenix: Pauli-based High-level Optimization Engine for Instruction Execution on NISQ devices](phoenix_pauli_based_high_level_optimization_engine_for_instruction_execution_on_nisq_devices.md) | DES6: Quantum Computing |
| [Joint Cutting for Hybrid Schrödinger-Feynman Simulation of Quantum Circuits](joint_cutting_for_hybrid_schr_dinger_feynman_simulation_of_quantum_circuits.md) | DES6: Quantum Computing |
| [Versatile Cross-platform Compilation Toolchain for Schrodinger-style Quantum Circuit Simulation](versatile_cross_platform_compilation_toolchain_for_schrodinger_style_quantum_circuit_simulation.md) | DES6: Quantum Computing |


### 推动量子计算落地：从量子线路布线、量子纠错到量子机器学习（QML）(8)

Pushing Quantum Computing Reality from Routing to Error Corrections and QML 


- Session Chairs: Jinglei Cheng, Himanshu Thapliyal


> 本次专题研讨聚焦量子计算领域前沿创新思路，研究方向涵盖量子比特路由、量子比特读出、误差抑制、量子纠错、量子线路等价性校验，以及量子机器学习应用。第一篇论文提出一种全新启发式算法，用于解决量子比特路由难题。量子读出误差是系统最主要的噪声来源，因此第二、三、四篇论文分别给出三类解决方案：基于轻量级神经网络的量子比特读出架构、可扩展高保真三级读出方案，以及软硬件协同设计框架，该框架搭载嵌入式加速器以抑制读出误差。第五篇论文提出一种基于快速伊辛模型的高效量子纠错方法。第六篇论文介绍一套具备变革性的框架，依托ZX演算图抽象实现量子线路等价性校验。第七、八篇论文围绕量子机器学习（QML）展开研究，分别提出振幅嵌入方案，以及一套适配异构量子处理器、兼顾高效性与高精度的训练推理框架。

> This session explores new ideas in quantum computing, focusing on qubit routing, qubit readout, reducing errors, error correction, checking the equivalence of quantum circuits, and using quantum machine learning. The first paper aims to solve the qubit routing problem through a novel heuristic algorithm. Quantum readout error is the most significant source of error; therefore, the second, third, and fourth papers present qubit readout architecture leveraging lightweight neural networks, scalable high-fidelity three-level readout, and a software-hardware co-design approach that mitigates readout errors with an embedded accelerator. The fifth paper presents a fast-Ising model-based approach for efficient quantum error correction. The sixth paper discusses a transformative framework for quantum circuit equivalence checking using ZX calculus-based graph abstractions. The seventh and eighth papers focus on quantum machine learning (QML) through amplitude embedding and a framework for efficient and high-accuracy training and inference on heterogeneous quantum processing units.

| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [DDRoute: a Novel Depth-Driven Approach to the Qubit Routing Problem](ddroute_a_novel_depth_driven_approach_to_the_qubit_routing_problem.md) | DES6: Quantum Computing |
| [KLiNQ: Knowledge Distillation-Assisted Lightweight Neural Network for Qubit Readout on FPGA](klinq_knowledge_distillation_assisted_lightweight_neural_network_for_qubit_readout_on_fpga.md) | DES6: Quantum Computing |
| [Efficient and Scalable Architectures for Multi-level Superconducting Qubit Readout](efficient_and_scalable_architectures_for_multi_level_superconducting_qubit_readout.md) | DES6: Quantum Computing |

| [DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator](dyrem_dynamically_mitigating_quantum_readout_error_with_embedded_accelerator.md) | xxxxxx| 

| [Weighted Range-Constrained Ising-Model Decoder for Quantum Error Correction](weighted_range_constrained_ising_model_decoder_for_quantum_error_correction.md) | DES6: Quantum Computing |
| [ZXNet: ZX Calculus-Driven Graph Neural Network Framework for Quantum Circuit Equivalence Checking](zxnet_zx_calculus_driven_graph_neural_network_framework_for_quantum_circuit_equivalence_checking.md) | DES6: Quantum Computing |
| [EnQode: Fast Amplitude Embedding for Quantum Machine Learning using Classical Data](enqode_fast_amplitude_embedding_for_quantum_machine_learning_using_classical_data.md) | DES6: Quantum Computing |
| [ArbiterQ: Improving QNN Convergency and Accuracy by Applying Personalized Model on Heterogeneous Quantum Devices](arbiterq_improving_qnn_convergency_and_accuracy_by_applying_personalized_model_on_heterogeneous_quantum_devices.md) | DES6: Quantum Computing |



### 量子领域重大突破催生颠覆性应用 (6)

Quantum Breakthroughs Creating Game-Changing Applications 


- Session Chairs: Saurabh Kotiyal, Sanjaya Lohani

> 本次研讨围绕量子计算各类颠覆性应用展开，内容涵盖量子计算在金融领域的落地方案、网络社区检测、量子机器学习相对经典模型的计算优势、量子密码分析，以及面向现实场景的分布式量子计算技术研发。第一篇论文依托全新设计的HHL量子算法架构，求解金融领域的投资组合优化问题。社区检测是网络分析领域的核心研究课题，第二篇论文验证了类量子混合方案在大规模图数据社区检测任务中的应用潜力。第三篇论文证明，相较于纯经典计算模型，混合量子神经网络具备更强的可扩展性与资源利用效率，有望成为处理复杂计算问题的优选方案。第四、五篇论文结合基于测量的逆计算与窗口算术技术，提出适用于量子密码分析的新型量子算术电路。分布式量子计算（DQC）是实现量子计算规模扩容的重要发展路径，因此第六篇论文针对分布式量子计算系统开展软硬件协同设计研究，为该技术在真实业务场景中实现更实用、高效的落地搭建理论与工程基础。

> The session discusses game-changing applications of quantum computing in finance, community detection, computational advantages of quantum machine learning over classical models, quantum cryptanalysis, and developing distributed quantum computing for real-world applications. The first paper solves portfolio optimization problems in finance with the help of a novel design of an HHL quantum algorithm. Community detection is an important problem in network analysis; the second paper demonstrates the potential of hybrid quantum-inspired solutions for advancing community detection in large-scale graph data. The third paper shows that hybrid quantum neural networks provide a more scalable and resource-efficient solution over purely classical models, positioning them as a promising alternative for tackling complex computational problems. The fourth and fifth papers discuss novel quantum arithmetic circuits for quantum cryptanalysis with the help of measurement-based uncomputation and windowed arithmetic. Distributed quantum computing (DQC) offers a promising pathway for scaling up quantum computing; therefore, the sixth paper discusses hardware-software co-design for DQC systems, paving the way for more practical and efficient implementations for real-world applications.



| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [SAPO: Improving the Scalability and Accuracy of Quantum Linear Solver for Portfolio Optimization](sapo_improving_the_scalability_and_accuracy_of_quantum_linear_solver_for_portfolio_optimization.md) | DES6: Quantum Computing |
| [Scalable Community Detection Using QHD and QUBO Formulation](scalable_community_detection_using_qhd_and_qubo_formulation.md) | DES6: Quantum Computing |
| [Computational Advantage in Hybrid Quantum Neural Networks: Myth or Reality?](computational_advantage_in_hybrid_quantum_neural_networks_myth_or_reality.md) | DES6: Quantum Computing |
| [Measurement-based uncomputation of quantum circuits for modular arithmetic](measurement_based_uncomputation_of_quantum_circuits_for_modular_arithmetic.md) | DES6: Quantum Computing |
| [Optimizing windowed arithmetic for quantum attacks against RSA2048](optimizing_windowed_arithmetic_for_quantum_attacks_against_rsa2048.md) | DES6: Quantum Computing |
| [Hardware-Software Co-design for Distributed Quantum Computing](hardware_software_co_design_for_distributed_quantum_computing.md) | DES6: Quantum Computing |

