# Design · DAC 2025 (114)

本分类收录 DAC 2025（第62届）Track "Design" 的论文。



## DES1：片上系统、异构架构与可重构架构 (24)

DES1: SoC, Heterogeneous, and Reconfigurable Architectures


### 释放加速器的性能潜力：专用集成电路、现场可编程门阵列与存内计算 (8)

Unleashing the Power of Accelerators: ASICs, FPGAs, and PIMs (8)

- Session Chairs: Amir Fakhim Babaei, Ganapati Bhat

> 本场会议探讨面向人工智能及其他应用场景的创新加速器设计，所依托技术涵盖专用集成电路、软硬件协同设计、现场可编程门阵列以及存内计算等多种技术。会议首先介绍一种面向神经网络处理单元、具备缓存感知能力且支持多租户的深度神经网络加速器。第二篇论文提出一种基于现场可编程门阵列、支持多查询操作的可配置内容可寻址存储器架构。随后进入存内计算加速相关议题，第三篇论文搭建了一套协同仿真环境，用于对存内计算架构与片上网络配置开展设计空间探索；紧接着分享一款全新的基于存内计算的大语言模型加速器。之后将介绍一款内存高效的全同态加密处理单元。本场会议最后由三篇报告收尾，分别介绍面向机器视觉与脑机接口应用的专用加速器。

> This session explores innovative accelerator designs for AI and other applications, leveraging diverse technologies from ASICs and hardware-software co-design to FPGAs and Processing-in-Memory (PIM). The session begins with a cache-aware, multi-tenant DNN accelerator for NPUs. The next paper presents a FPGA-based configurable CAM architecture with multi-query support. Moving to PIM-based acceleration, the next paper explores a co-simulation environment for design space exploration of PIM architectures and Network-on-Chip (NoC) configurations, followed by a presentation on a novel PIM-based LLM accelerator. Next, a memory-efficient Fully Homomorphic Encryption (FHE) processing unit is presented. Finally, the session concludes with three presentations on specialized accelerators targeting vision and brain-computer interface applications.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [CaMDN：提升集成NPU上多租户DNN缓存效率<br>CaMDN: Enhancing Cache Efficiency for Multi-tenant DNNs on Integrated NPUs](camdn_enhancing_cache_efficiency_for_multi_tenant_dnns_on_integrated_npus.md) | 缺少“## 研究概要”标题；文件中为“## 研究概述”：本文针对集成神经网络处理器（NPU）片上系统（SoC）多租户深度神经网络（DNN）共享高速缓存冲突、缓存效率低下问题，提出软硬件协同设计CaMDN。硬件增设专属控制器划分模型隔离缓存区；软件提供缓存感知映射与动态分配算法。实验表明该方案平均访存减少33.4%，模型加速最高2.56倍，硬件面积开销可忽略。 |
| [面向FPGA数据密集应用的可配置DSP型CAM架构<br>Configurable DSP-Based CAM Architecture for Data-Intensive Applications on FPGAs](configurable_dsp_based_cam_architecture_for_data_intensive_applications_on_fpgas.md) | 面向FPGA上数据密集型应用，现有LUT/BRAM型CAM存在资源开销大、扩展性差、不支持多并发查询等缺陷。本文提出基于DSP块的可配置CAM分层架构，单元级支持多查询并行，适配二值/三值/区间匹配。实验资源占用低、访存更新延迟均衡，图三角计数案例平均加速4.92倍，代码已开源。 |
| [HPIM-NoC：面向异构PIM片上网络的先验知识优化框架<br>HPIM-NoC: A Priori-Knowledge-Based Optimization Framework for Heterogeneous PIM-Based NoCs](hpim_noc_a_priori_knowledge_based_optimization_framework_for_heterogeneous_pim_based_nocs.md) | 针对异构PIM片上网络缺少专用仿真与架构搜索工具的问题，本文提出HPIM-NoC协同框架，集成异构PIM-NoC仿真器与先验知识驱动的三段式模拟退火搜索流程，搭配查表、降低仿真频次加速搜索，并定制布局算法。测试显示异构方案FoM最高降低37.41%，搜索速度提升最高2.96倍。 |
| [McPAL：面向LLM的多芯粒HBM-PIM非结构化稀疏推理扩展架构<br>McPAL: Scaling Unstructured Sparse Inference with Multi-Chiplet HBM-PIM Architecture for LLMs](mcpal_scaling_unstructured_sparse_inference_with_multi_chiplet_hbm_pim_architecture_for_llms.md) | 本文提出McPAL多芯粒HBM存算一体架构，面向大语言模型非结构化稀疏推理。设计稀疏矩阵分解与双缓冲蝶形网络适配无规则权重，结合3D垂直、2.5D水平分层芯粒扩展方案。在Llama系列模型测试中，相较A100最高提速3.12倍、能效提升35.66倍，优于现有主流加速器。 |
| [Hypnos：内存高效全同态处理单元<br>Hypnos: Memory Efficient Homomorphic Processing Unit](hypnos_memory_efficient_homomorphic_processing_unit.md) | 本文提出Hypnos内存高效全同态加密处理单元，采用ARM+FPGA异构架构，设计基于RNS分片的同态分页内存管理单元HEPMU，解决传统加速器PCIe传输开销大、内存碎片严重问题。FPGA原型测试下，相较ASIC提速2.58倍、FPGA基线提速4.43倍，通信量缩减3.78倍，能效大幅提升。 |
| [GS-TG：通过瓦片分组减少冗余排序并保持光栅效率的3D高斯渲染加速器<br>GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing Redundant Sorting while Preserving Rasterization Efficiency](gs_tg_3d_gaussian_splatting_accelerator_with_tile_grouping_for_reducing_redundant_sorting_while_preserving_rasterization_efficiency.md) | 本文提出GS-TG瓦片分组3D高斯渲染加速器，解决瓦片尺寸带来的排序与光栅化性能权衡问题。采用大组排序、小瓦片光栅化+比特掩码复用排序结果，无损无需重训，可兼容现有优化。28nm硬件测试相较SOTA最高提速1.54倍，能效提升2.12倍。 |
| [BEVSA：面向多相机系统的实时俯视语义分割加速器<br>BEVSA: A Real-Time Bird's-Eye-View Semantic Segmentation Accelerator for Multi-Camera System](bevsa_a_real_time_bird_s_eye_view_semantic_segmentation_accelerator_for_multi_camera_system.md) | 本文面向自动驾驶多相机BEV语义分割提出异构集群加速器BEVSA。设计分块分层BEV池化集群压缩搜索空间、并行计算；粗细粒度结合零跳过卷积集群挖掘特征稀疏。28nm流片测试，BEV池化提速43.2倍，卷积吞吐提升1.61倍，单集群实时23.1帧，每帧能效提升167.4倍。 |
| [面向脑机接口的可调精度高能效卡尔曼滤波架构<br>An Energy-Efficient Kalman Filter Architecture with Tunable Accuracy for Brain-Computer Interfaces](an_energy_efficient_kalman_filter_architecture_with_tunable_accuracy_for_brain_computer_interfaces.md) | 本文面向脑机接口(BCI)运动解码，提出可配置卡尔曼滤波硬件KalmMind。设计高斯精确求逆与牛顿迭代近似交替计算方案，通过寄存器细调精度、时延权衡。基于RISC-V异构SoC在FPGA验证，相较通用处理器能效提升15.3倍，精度最高提升千倍，适配多类神经数据集。 |
### 回到未来：速度与效率共生之地 (8)

Back to the Future: Where Speed Meets Efficiency (8)

- Session Chairs: Tianhao Cai, Dirk Stroobandt

> 本场会议聚焦硬件加速领域前沿技术进展，围绕现代芯片架构中的计算、内存访问与并行性优化展开研讨。本次收录论文围绕异构可重构加速器与现场可编程门阵列（FPGA）优化开展相关研究，提出了多种核心计算任务加速创新方案。研讨主题涵盖高效稀疏矩阵乘法、分块间并行计算、自适应树形运算、大数模约简、粗粒度可重构阵列（CGRA）编译器映射策略，以及非易失性FPGA的物理设计。上述研究成果共同印证，硬件架构与算法设计层面的创新正引领高性能计算行业发展，不断拓宽各类应用场景下计算速度、运行能效与可扩展性的性能边界。

> This session explores cutting-edge advancements in hardware acceleration, focusing on optimizing computation, memory access, and parallelism in modern architectures. Featuring research on heterogeneous reconfigurable accelerators and FPGA optimization, the papers highlight novel approaches to accelerating key computational tasks. Topics include efficient sparse matrix multiplication, inter-tile parallelism, adaptive tree computations, large number modular reduction, compiler mapping strategies for CGRAs and physical design for nonvolatile FPGAs. Together, these works demonstrate how innovations in hardware and algorithm design are driving the future of high-performance computing, pushing the boundaries of speed, efficiency, and scalability in diverse applications.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [HeteroSVD：基于Versal ACAP的高效SVD协同设计加速器<br>HeteroSVD: Efficient SVD Accelerator on Versal ACAP with Algorithm-Hardware Co-Design](heterosvd_efficient_svd_accelerator_on_versal_acap_with_algorithm_hardware_co_design.md) | 本文面向Versal ACAP异构平台提出HeteroSVD，面向分块Jacobi奇异值分解做软硬件协同加速。设计移位环排序、AIE专属数据流与分层布局，配套精准性能模型与自动DSE框架。VCK190实测相较FPGA延迟最高降1.98倍，对比GPU延迟最高提速7.22倍、能效提升13.18倍。 |
| [VSpGEMM：利用Versal ACAP实现高性能稀疏矩阵乘加速<br>VSpGEMM: Exploiting Versal ACAP for High-Performance SpGEMM Acceleration](vspgemm_exploiting_versal_acap_for_high_performance_spgemm_acceleration.md) | 本文面向Versal ACAP异构平台提出VSpGEMM稀疏矩阵乘法加速器。设计BCSX分块统一稀疏存储格式、多层分块调度、AIE+PL混合归并机制，解决稀疏不规则访存与中间量传输瓶颈。基于SuiteSparse数据集测试，相较同平台CHARM平均提速2.65倍，对比RTX4090 cuSPARSE能效提升33.62倍。 |
| [HiSpTRSV：探索FPGA上SpTRSV的分块级并行加速<br>HiSpTRSV: Exploring Tile-Level Parallelism for SpTRSV Acceleration on FPGAs](hisptrsv_exploring_tile_level_parallelism_for_sptrsv_acceleration_on_fpgas.md) | 本文提出HiSpTRSV，面向HBM FPGA挖掘稀疏三角求解分块间+分块内双层并行。设计细粒度依赖图、流过滤单元、模双向索引均衡负载，配套THLS并行算法。基于Alveo U55C验证，对比FPGA基线平均提速34.3%，相较GPU平均提速3.58倍、能效提升9.59倍。 |
| [面向高效自适应基数树的数据中心化硬件加速器<br>A Data-Centric Hardware Accelerator for Efficient Adaptive Radix Tree](a_data_centric_hardware_accelerator_for_efficient_adaptive_radix_tree.md) | 本文面向自适应基数树（ART）并发读写存在冗余遍历、锁同步开销大的痛点，提出以数据为中心的FPGA加速器DCART。设计CTT处理模型，通过前缀合并操作、捷径缓存、价值感知片上缓存削减开销。基于Alveo U280实现，相较CPU/GPU主流ART方案提速21.1–44.2倍，能效提升71.1–148.9倍。 |
| [ALLMod：通过混合负载探索LUT大数模约简面积效率<br>ALLMod: Exploring Area-Efficiency of LUT-based Large Number Modular Reduction via Hybrid Workloads](allmod_exploring_underline_a_rea_efficiency_of_underline_l_ut_based_underline_l_arge_number_underline_mod_ular_reduction_via_hybrid_workloads.md) | 本文提出ALLMod混合负载大数模约简架构，融合LUT查表法与迭代减法法，将输入高位分配查表、低位迭代运算，设计均衡负载硬件模板与约束驱动设计空间搜索。FPGA验证表明，128/8192比特下面积效率相较传统查表法分别提升1.65倍、3倍，大幅削减BRAM与加法器硬件开销。 |
| [GPS：基于GNN的两阶段CGRA循环预调度映射方法<br>GPS: GNN-Based Two-Stage Pre-Scheduling Loop Mapping Method on CGRAs](gps_gnn_based_two_stage_pre_scheduling_loop_mapping_method_on_cgras.md) | 本文提出GPS两阶段CGRA循环映射方法，融合图同构GNN预调度与模式图匹配映射。先通过GNN预测操作优先级压缩搜索空间，再基于VF3子图同构完成DFG到时域CGRA映射。多基准测试，迭代间隔II优化29.4%~406.7%，编译速度最高提升1106.8倍，适配多尺寸ADRES、HyCube架构。 |
| [Rewire：通过融合式路由范式推进CGRA映射<br>Rewire: Advancing CGRA Mapping Through a Consolidated Routing Paradigm](rewire_advancing_cgra_mapping_through_a_consolidated_routing_paradigm.md) | 本文提出Rewire一体化路由映射范式，突破传统逐节点CGRA映射局限。通过前后向同步传播复用路由信息，交集筛选多节点候选并依托数据流约束剪枝。在PolyBench等测试，相较PF*、SA编译耗时分别缩减4.7/13.5倍，循环启动间隔II性能提升1.3/2.1倍。 |
| [面向高密度非易失FPGA的可布线性感知打包方法<br>Routability-aware Packing for High-density Nonvolatile FPGAs](routability_aware_packing_for_high_density_nonvolatile_fpgas.md) | 本文面向MLC型非易失FPGA(NVFPGA)提出路由感知重打包优化方案，新增Repair阶段搭配输入等价LUT过滤技术。优化插入VTR打包流程，大幅减少耗时的CLB内部路由校验；多基准测试打包耗时平均降低41.48%，同时小幅提升面积与时序性能。 |
### 人工智能、图形处理器与处理器的崛起：新一代架构 (8)

The Rise of AI, GPUs & Processors: The Next-Gen Architectures 

- Session Chairs: Guy Eichler, Sitao Huang

> 本场专题聚焦下一代计算架构演进领域的前沿研究，研究对象涵盖处理器、图形处理器以及人工智能增强型计算系统。相关论文探讨了图形处理器增量划分技术、乱序超标量处理器细粒度指令分析方案，以及面向多模态大语言模型、搭载人工智能扩展模块的多核解决方案。其他研究议题还包括图形处理器子核心高效硬件资源共享、用于微架构设计空间探索的多保真度优化框架（如RISC-V架构）、全新图形处理器内核融合技术，以及张量加速器数据流优化方案。上述研究提出多项创新技术思路，持续突破现代计算系统在性能、可扩展性与能效层面的技术上限。

> This session highlights cutting-edge research on advancing next-gen computing architectures, focusing on processors, GPUs, and AI-enhanced systems. Papers explore incremental partitioning techniques on GPUs, fine-grain instruction analysis in out-of-order superscalar processors, and multi-core solutions with AI extensions for multimodal LLMs. Additional topics include efficient hardware resource sharing in GPU sub-cores, a multi-fidelity optimization framework for microarchitecture design space exploration (e.g., RISCV), new GPU kernel fusion techniques, and dataflow optimizations for tensor accelerators. These works showcase innovative strategies that push the boundaries of performance, scalability, and efficiency in modern computing systems.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [iG-kway：GPU上的增量k路图划分<br>iG-kway: Incremental k-way Graph Partitioning on GPU](ig_kway_incremental_k_way_graph_partitioning_on_gpu.md) | 本文提出首个GPU增量k路图划分器iG-kway，面向CAD动态电路图迭代优化。设计桶列表GPU原生图存储、伪分区均衡与并行细化内核，仅修改受影响顶点。工业与DIMACS图测试，相较全重划分G-kway平均提速84倍，切割质量基本持平。 |
| [FireGuard：面向乱序超标量核的细粒度安全分析通用微架构<br>FireGuard: A Generalized Microarchitecture for Fine-Grained Security Analysis on OoO Superscalar Cores](fireguard_a_generalized_microarchitecture_for_fine_grained_security_analysis_on_ooo_superscalar_cores.md) | 本文提出FireGuard细粒度指令安全分析微架构，适配乱序超标量RISC-V BOOM内核。设计无缓冲数据转发、超标量事件过滤器、无广播分布式映射器，搭配优化ISA编程模型。FPGA与商用SoC验证，多安全检测负载性能开销远低于软件方案，集成至M1-Pro、麒麟960等芯片面积开销不足1%。 |
| [EdgeMM：面向边缘多模态LLM的异构AI扩展多核CPU<br>EdgeMM: Multi-Core CPU with Heterogeneous AI-Extension and Activation-aware Weight Pruning for Multimodal LLMs at Edge](edgemm_multi_core_cpu_with_heterogeneous_ai_extension_and_activation_aware_weight_pruning_for_multimodal_llms_at_edge.md) | 本文提出EdgeMM异构多核RISC-V CPU架构，面向边缘多模态大模型。分计算型脉动阵列核、存内CIM存储型核适配GEMM/GEMV两类算子，配套动态激活感知剪枝与令牌驱动带宽调度。22nm流片验证，相比笔记本RTX306提速2.84倍，能效达0.217token/J。 |
| [ACRS：分区GPU子核的相邻计算资源共享<br>ACRS: Adjacent Computation Resource Sharing among Partitioned GPU Sub-Cores](acrs_adjacent_computation_resource_sharing_among_partitioned_gpu_sub_cores.md) | 本文面向GPU流式多处理器SM子核隔离导致功能单元(FU)利用率低、操作数收集器阻塞问题，提出ACRS相邻计算资源共享框架。设计SF发射、回写两大硬件模块与多种子核配对策略，顺序配对方案效果最优。测试相比基线平均提速14.1%、最高46.4%，能耗降低8.3%，优于现有SOTA调度方案。 |
| [Swift or Exact?：通过多保真偏序预测提升微架构DSE效率<br>Swift or Exact? Boosting Efficient Microarchitecture DSE via Multi-fidelity Partial Order Prediction](swift_or_exact_boosting_efficient_microarchitecture_dse_via_multi_fidelity_partial_order_prediction.md) | 本文提出基于偏序预测的多保真贝叶斯微架构DSE框架，针对架构/RTL/网表三级EDA流程非线性偏差问题。构建非线性高斯融合模型，利用逻辑回归预测PPA排序反转，自适应选择仿真保真度。RISC-V BOOM/Rocket测试，帕累托超体积提升12.9%，收敛速度提升48%，ADRS指标降低57.7%。 |
| [基于准则的数据流优化：面向算子融合张量加速器的通信下界<br>Principle-based Dataflow Optimization for Communication Lower Bound in Operator-Fused Tensor Accelerator](principle_based_dataflow_optimization_for_communication_lower_bound_in_operator_fused_tensor_accelerator.md) | 本文提出基于四条理论准则的数据流优化方法，给出访存下界解析解，并设计FuseCU融合张量加速器。区分同/异NRA融合收益，支持Tile/Column两种融合映射。在BERT、LLaMA2等Transformer测试，相比TPUv4i访存减少63.6%、提速1.33倍，硬件面积仅增12%。 |
| [GoPTX：通过PTX级指令流编织实现细粒度GPU内核融合<br>GoPTX: Fine-grained GPU Kernel Fusion by PTX-level Instruction Flow Weaving](goptx_fine_grained_gpu_kernel_fusion_by_ptx_level_instruction_flow_weaving.md) | 本文提出GoPTX，面向PTX中间层细粒度GPU内核融合。通过合并多内核控制流图、时延感知指令交织、自适应代码分块提升ILP，解决记分板引发的warp停顿。基于A100多基准测试，相较并发基线平均提速11.2%，最高23%，有效提升每周期就绪warp数与硬件利用率。 |
| [DARIS：面向GPU实时DNN推理的超订阅时空调度器<br>DARIS: An Oversubscribed Spatio-Temporal Scheduler for Real-Time DNN Inference on GPUs](daris_an_oversubscribed_spatio_temporal_scheduler_for_real_time_dnn_inference_on_gpus.md) | 本文提出DARIS实时多租户GPU调度器，基于MPS+CUDA流实现空间超分共享，分段暂存实现时序粗粒度抢占，动态MRET替代保守WCET预测。在无批量场景下吞吐量较基线批处理提升15%、优于SOTA调度11.5%，高优先级任务无超时，低优先级丢期率低于2%。 |
## DES2A：存内计算与近存计算电路 (12)

DES2A: In-memory and Near-memory Computing Circuits 

### 加速器设计领域的突破创新：光子、时域与安全导向型人工智能 (6)

Breaking Boundaries in Accelerator Design: Photonic, Time-Domain, and Security-Driven AI (6)

- Session Chairs: Yu Cao, Sumitha George

> 人工智能加速技术的发展已突破传统硅基方案，衍生出光子架构、时域处理架构以及安全增强型架构等全新技术路线。本场专题将展示多项前沿突破成果，包括高速光子张量核心、非线性时域处理技术、基于铁电场效应晶体管（FeFET）的硬件安全方案，以及面向大语言模型（LLM）与组合优化任务的专用AI加速器。上述创新方案依托全新计算范式，持续拓宽AI硬件在运算性能、能效与硬件安全层面的技术边界。

> AI acceleration is evolving beyond conventional silicon, embracing photonic, time-domain, and security-enhanced architectures. This session showcases breakthroughs in high-speed photonic tensor cores, nonlinear time-domain processing, FeFET-based security solutions, and specialized AI accelerators for LLMs and combinatorial optimization. By leveraging novel computing paradigms, these innovations push the boundaries of performance, efficiency, and security in AI hardware design.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [UniCAIM：静动态KV剪枝统一CAM/CIM长上下文LLM推理架构<br>UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference](unicaim_a_unified_cam_cim_architecture_with_static_dynamic_kv_cache_pruning_for_efficient_long_context_llm_inference.md) | 本文提出基于FeFET的UniCAIM统一CAM/CIM架构，融合静态-动态KV缓存剪枝适配长上下文LLM。设计三种工作模式：CAM快速Top-k动态筛选、电荷域CIM累计分数静态淘汰、电流域精确注意力计算。电路测试AEDP相较主流CIM加速器降低8.2~831倍，长文本任务精度接近完整缓存基线。 |
| [P-DAC：面向LLM推理的高能效光子加速器方案<br>P-DAC: Power-Efficient Photonic Accelerators for LLM Inference](p_dac_power_efficient_photonic_accelerators_for_llm_inference.md) | 本文提出P-DAC光子数模转换器，替换光Transformer加速器传统电子DAC，依托光信号加权近似驱动MZM调制器，省去电域转换功耗。数学推导验证误差可控，集成Lightening-Transformer后，8bit场景整机功耗降低47.7%，BERT/DeiT推理能耗最高削减35.4%。 |
| [脉宽入脉宽出通用非线性处理单元：面向时域存内计算<br>A PulseWidth-IN-PulseWidth-Out Universal Nonlinear Processing Element for Time-Domain In-Memory Computing Systems](a_pulsewidth_in_pulsewidth_out_universal_nonlinear_processing_element_for_time_domain_in_memory_computing_systems.md) | 本文面向时域存算(TD-IMC)跨域转换能耗高的痛点，提出脉宽输入输出通用非线性单元PIPO-UNPE。设计两层RRAM-ReLU硬件网络，搭配DLRSE训练策略，自研两类脉冲可编程电流源与低偏差VTC。130nm仿真功耗912μW、吞吐10M NOPS，嵌入TD-IMC后能效提升9.5~25倍，推理精度损失低于0.1%。 |
| [PUFiM：融合PUF与存内计算的高鲁棒FeFET边缘AI安全方案<br>PUFiM: A Robust and Efficient FeFET-Based Security Solution Merging Physical Unclonable Function with Compute-in-Memory for Edge AI](pufim_a_robust_and_efficient_fefet_based_security_solution_merging_physical_unclonable_function_with_compute_in_memory_for_edge_ai.md) | 本文提出基于FeFET的PUFiM一体化架构，将PUF物理密钥生成与存内计算CiM融合在同一MLC阵列。设计四类配套优化抵御建模攻击与密钥泄露，VGG/ResNet测试下密钥泄露95%时推理精度下降超60%，存储密度、能效相较主流安全CiM分别提升9.7倍、1.2倍以上。 |
| [TAXI：基于SOT-MRAM分层聚类的旅行商问题伊辛加速器<br>TAXI: Traveling Salesman Problem Accelerator with X-bar-based Ising Macros Powered by SOT-MRAMs and Hierarchical Clustering](taxi_traveling_salesman_problem_accelerator_with_x_bar_based_ising_macros_powered_by_sot_mrams_and_hierarchical_clustering.md) | 本文提出TAXI基于SOT-MRAM交叉条Ising存内加速器，软硬件协同分层聚类分解大规模TSP。采用器件原生随机切换实现自然退火，各聚类子问题在独立Ising宏内并行求解，无需宏间数据搬运。TSPLIB全规模测试，相较主流分层Ising求解平均提速8倍，85900城市实例最优解仅比精确解长20%。 |
| [混合信号光子SRAM张量核：高速高能效与新型光电ADC<br>A Mixed-Signal Photonic SRAM-based High-Speed Energy-Efficient Photonic Tensor Core with Novel Electro-Optic ADC](a_mixed_signal_photonic_sram_based_high_speed_energy_efficient_photonic_tensor_core_with_novel_electro_optic_adc.md) | 本文基于GF45SPCLO工艺，提出混合信号多比特光子张量核。设计差分耦合pSRAM存储权重，利用WDM实现并行光向量乘；独创独热编码光电eoADC完成光模拟信号数字化。整套架构权重更新速率达20GHz，算力4.10TOPS，能效3.02TOPS/W，适配AI矩阵乘运算。 |
### 燃动人工智能时代：面向下一代存内计算与无乘法加速技术 (6)

AI on Fire: Compute-in-Memory and Multiplication-Free Acceleration for the Next Era

- Session Chairs: Ibrahim (Abe) Elfadel, Akhilesh Jaiswal

> 人工智能硬件正处于发展转折点，行业亟需能效与性能的跨越式革新。本次专题将深入探讨突破性存内计算（CIM）架构、无乘法加速技术以及全新运算范式，这类技术可大幅降低功耗与延迟，同时提升数据吞吐能力。从基于查找表的深度神经网络加速器、混合模数计算，到搭载自旋转移矩磁随机存储器（STT-MRAM）的存内计算方案，一系列创新技术正为人工智能硬件开辟全新发展空间。

> AI hardware is at an inflection point, demanding radical efficiency and performance leaps. This session dives into groundbreaking compute-in-memory (CIM) architectures, multiplication-free acceleration, and novel arithmetic paradigms that slash power and latency while boosting throughput. From LUT-based DNN accelerators to hybrid analog-digital computing and STT-MRAM-powered CIM, these innovations are setting AI hardware ablaze with new possibilities.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [共享参考的模拟累加与存内ADC：高能效低时延存内计算<br>High Energy-efficiency and Low latency In-Memory Computing using Analog Accumulator and In-Memory ADC with shared References](high_energy_efficiency_and_low_latency_in_memory_computing_using_analog_accumulator_and_in_memory_adc_with_shared_references.md) | 本文提出基于双8T SRAM的存内计算宏，融合RWLUDC单元、电荷共享位切片累加BSCHA与共享参考可重构IMADC。65nm工艺下ADC面积开销仅3%，MAC线性度提升23倍，吞吐较PWM提升1.9倍；搭配噪声鲁棒训练，MLP/VGG8/GAT推理精度损失均低于0.8%，峰值能效1146 TOPS/W。 |
| [CREST-CiM：交叉耦合差分STT-MRAM鲁棒二值网络存内计算<br>CREST-CiM: Cross-Coupling-Enhanced Differential STT-MRAM for Robust Computing-in-Memory in Binary Neural Networks](crest_cim_cross_coupling_enhanced_differential_stt_mram_for_robust_computing_in_memory_in_binary_neural_networks.md) | 本文提出CREST-CiM交叉耦合STT-MRAM存内计算单元，面向二值神经网络BNN。采用双MTJ互补存储±1权重，交叉耦合晶体管大幅提升高低电流比至8150。64×64阵列仿真显示读出裕度提升3.4倍、读扰动裕度提升27.6%，ResNet-18推理精度达86.7%，仅小幅面积开销，时延能耗增幅不足1%。 |
| [YOCO：面向大规模AI的混合存内计算与原位8位乘法架构<br>YOCO: A Hybrid In-Memory Computing Architecture with 8-bit Sub-PetaOps/W In-Situ Multiply Arithmetic for Large-Scale AI](yoco_a_hybrid_in_memory_computing_architecture_with_8_bit_sub_petaops_w_in_situ_multiply_arithmetic_for_large_scale_ai.md) | 本文提出YOCO混合ReRAM-SRAM存内计算架构，设计电荷域原位8位乘算IMA与时域累加器，大幅削减ADC/DAC开销。适配Transformer专属流水线，覆盖CNN与大语言模型。电路层面能效123.8 TOPS/W，吞吐量34.9 TOPS；对比主流IMC，平均能效提升3.9~19.9倍，吞吐提升6.8~33.6倍。 |
| [ReSMiPS：基于ReRAM的稀疏混合精度求解器与快速重排算法<br>ReSMiPS: A ReRAM-based Sparse Mixed-precision Solver with Fast Matrix Reordering Algorithm](resmips_a_reram_based_sparse_mixed_precision_solver_with_fast_matrix_reordering_algorithm.md) | 本文提出ReSMiPS基于ReRAM混合精度稀疏求解器，设计FSM矩阵重排算法与IF64存内浮点格式，构建数字-ReRAM混合BiCGSTAB迭代框架。SuiteSparse稀疏矩阵测试残差低于10⁻¹⁵，相较CPU/GPU提速数千倍，能耗降低两个数量级。 |
| [基于查找表的无乘法全数字DNN加速器：自同步流水累加<br>Lookup Table-based Multiplication-free All-digital DNN Accelerator Featuring Self-Synchronous Pipeline Accumulation](lookup_table_based_multiplication_free_all_digital_dnn_accelerator_featuring_self_synchronous_pipeline_accumulation.md) | 本文基于MADDNESS无乘近似矩阵乘法，提出全数字自同步流水线DNN存内加速器。采用动态逻辑BDT编码器、双端口10T-SRAM查表单元，无全局时钟、抗PVT偏差。22nm后仿验证，能效174 TOPS/W、面积效率2.01 TOPS/mm²，相较模拟与数字基线分别提升2.5倍、4倍，分类精度无损。 |
| [WISEDRAM：高可靠位运算型DRAM内加速器<br>WISEDRAM: A Reliable Bitwise In-DRAM Accelerator](wisedram_a_reliable_bitwise_in_dram_accelerator.md) | 本文提出WISEDRAM基于DRAM原位按位加速器，新增一行X专用单元，完全保留标准DRAM读写时序。依托可控差分位线实现XOR/AND/OR等全部按位运算，仅需3个DRAM周期。16nm HSPICE仿真显示，相比主流Ambit、ROC等方案，按位平均延迟降低22%，XOR提速71%，工艺鲁棒性提升77%，面积开销仅1.6%。 |
## DES2B：存内计算与近存计算架构、应用及系统 (34)

DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems 

### 答案藏于内存技术？只是存进内存？单单靠内存？点此文揭晓答案！(6)

The Answer Is In-memory!? In the Memory? Memory? Find Out Here! 

- Session Chairs: Marco Donato, Giacomo Pedretti

> 随着各类数据密集型应用不断将传统计算推向性能极限，存内计算作为一种变革性计算范式应运而生，用以攻克关键的内存墙瓶颈。本次专题将探讨存内计算架构领域的前沿技术进展，展示其在人工智能加速、大规模相似度检索、布尔可满足性问题求解三大方向实现技术革新的潜力。我们将深入剖析多款创新解决方案：基于NAND闪存与动态随机存储器（采用UPMEM方案）的高能效向量检索、自适应混合信号存内布尔可满足性求解器，以及基于内容可寻址存储器、查找表的新型硬件加速器。本专题同时介绍多款业界顶尖仿真框架与随机计算技术，这类技术可大幅提升系统可编程性与运行能效。

> As data-intensive applications push conventional computing to its limits, in-memory computing emerges as a transformative paradigm to overcome critical memory bottlenecks. This session explores cutting-edge advances in compute-in-memory architectures, showcasing their potential to revolutionize AI acceleration, large-scale similarity search, and Boolean satisfiability solving. We delve into innovative solutions including energy-efficient vector search in NAND flash and DRAM (using UPMEM), adaptive mixed-signal in-memory SAT solvers, and novel CAM- and LUT-based accelerators. The session also highlights state-of-the-art simulation frameworks and stochastic computing techniques that significantly enhance programmability and efficiency.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [FeKAN：基于FeFET CAM与LUT的高效KAN加速器<br>FeKAN: Efficient Kolmogorov-Arnold Networks Accelerator Using FeFET-based CAM and LUT](fekan_efficient_kolmogorov_arnold_networks_accelerator_using_fefet_based_cam_and_lut.md) | 本文提出FeKAN铁电存内加速器，软硬件协同优化KAN的B样条激活计算。设计两阶段DSE生成静态码本，搭配CSC稀疏编码、分组流水线，集成FeFET-CAM/LUT/CIM阵列。多模态测试相较CPU、GPU吞吐量最高提升150.68K、4664倍，能效分别提升606.87、11196倍。 |
| [基于混合匹配的NAND闪存大规模向量相似检索节能方案<br>Energy-Efficient Large-Scale Vector Similarity Search in NAND-Flash via Hybrid Matching](energy_efficient_large_scale_vector_similarity_search_in_nand_flash_via_hybrid_matching.md) | 本文提出基于3D NAND的混合匹配VSS架构Hybrid-M，在同一存储串融合精确ES过滤与近似AS检索。配套MLC区间编码、搜索电压偏移、感知训练FAT三项优化。在小样本学习、ANNS任务验证，相较纯AS方案能耗降低67%~83%，精度/召回损失极小。 |
| [Chameleon-SAT：面向多样SAT问题的自适应混合信号存内求解加速器<br>Chameleon-SAT: An Adaptive Boolean Satisfiability Accelerator Using Mixed-Signal In-Memory Computing for Versatile SAT Problems](chameleon_sat_an_adaptive_boolean_satisfiability_accelerator_using_mixed_signal_in_memory_computing_for_versatile_sat_problems.md) | 本文提出Chameleon-SAT混合信号存内ASIC加速器，首款同时支持局部搜索、DPLL、CDCL三类SAT算法。设计自适应算法选择机制与SRAM混合信号存内阵列，适配不同规模、复杂度SAT问题。多基准测试相比CPU提速8.39~90倍，对比现有单算法ASIC，兼容范围与吞吐、能效全面领先。 |
| [面向深度学习的全系统可编程可扩展存内计算仿真框架<br>A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning](a_full_system_programmable_and_extensible_in_memory_computing_simulation_framework_for_deep_learning.md) | 本文提出全系统可编程存算一体仿真框架IMCsim，兼容SRAM/MRAM/Digital三类存算架构，配套可扩展指令集与SNR精度模型，集成QEMU实现周期级仿真。基于22/28nm实测芯片完成校准，在CNN、大模型、扩散模型多负载开展架构探索，还完成28nm轻量化DiT存算芯片设计与版图验证。 |
| [基于ReRAM的全内存随机计算<br>All-in-memory Stochastic Computing using ReRAM](all_in_memory_stochastic_computing_using_reram.md) | 本文提出基于ReRAM的全内存随机计算架构All-in-Memory SC，依托ReRAM器件随机性在阵列内完成随机比特流生成、随机运算、二进制转换全流程。设计优化型内存比特流生成算法与侦察逻辑硬件，规避存储-计算数据搬运开销。图像处理测试相较CMOS、ReRAM基线，吞吐分别提升1.39/2.16倍，能耗降低1.15/2.8倍，故障下图像质量仅平均下降5%。 |
| [UPVSS：近存处理系统中的向量相似检索联合管理<br>UPVSS: Jointly Managing Vector Similarity Search with Near-Memory Processing Systems](upvss_jointly_managing_vector_similarity_search_with_near_memory_processing_systems.md) | 本文提出UPVSS面向商用UPMEM近存处理系统优化IVF向量检索，设计DPU感知聚类划分与协同调度器。均衡分发向量规避DPU内存溢出，就近卸载距离计算削减主机带宽开销，配套WRAM多级缓存充分利用DPU多线程流水线。千万级高维向量测试，相较FAISS平均提速1.95倍，有效缓解冯诺依曼访存瓶颈。 |
### 直击核心、直观可视、清晰表述：新一代人工智能处理技术 (6)

Spike It, See It, Say It: Next-Gen AI Processing 


- Session Chairs: Xueqing Li, Wantong Li

> 本章节探讨新一代硬件架构如何突破内存墙瓶颈，为新兴人工智能系统加速大语言模型、计算机视觉与神经形态计算。第一篇论文提出一款神经形态（基于脉冲）处理器，该处理器采用脉冲追踪双极性积分发放神经元；第二篇论文提出集成图像传感与近传感器磁阻随机存储器（MRAM）处理一体化架构；最后四篇论文呈现前沿研究成果，围绕边缘设备上视觉Transformer（ViT）与大语言模型（LLM）开展算法-硬件协同设计，拓宽边缘人工智能的性能边界，为资源受限场景下视觉与语言模型的高效部署提供全新研究方向。

> This section explores how next-generation hardware architectures are breaking the memory wall to accelerate large language models, computer vision, and neuromorphic computing for emerging AI systems. The first paper proposes a neuromorphic (spike-based) processor, which leverages spike-tracing bipolar-integrate-and-fire neurons. The second paper proposes an integrated image sensing and near-sensor MRAM-based processing architecture. The last four papers present cutting-edge research contributions addressing algorithm-hardware co-design for vision transformers (ViTs) and large language models (LLMs) on edge devices, pushing the boundaries of edge AI, offering new directions for efficient deployment of vision and language models in resource-constrained environments.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [BiNeuroRAM：高能效ReRAM-PIM双极性脉冲神经网络加速器<br>BiNeuroRAM: Energy-Efficient ReRAM-Based PIM for Accurate Bipolar Spiking Neural Network Acceleration](bineuroram_energy_efficient_reram_based_pim_for_accurate_bipolar_spiking_neural_network_acceleration.md) | 本文提出BiNeuroRAM，首款支持ST-BIF双极性神经元的ReRAM存内计算SNN加速器。设计低功耗电压灵敏放大器LPVSA与异步自触发转换器STC，采用无全局时钟微架构，搭配输入/权重稀疏优化。ImageNet ResNet-50准确率达80.9%，相较SOTA吞吐量、能效分别提升2.08倍、2.09倍。 |
| [ResISC：基于余数系统的感知与计算一体化高效边缘AI架构<br>ResISC: Residue Number System-Based Integrated Sensing and Computing for Efficient Edge AI](resisc_residue_number_system_based_integrated_sensing_and_computing_for_efficient_edge_ai.md) | 本文提出基于余数系统(RNS)的端侧感知计算一体化架构ResISC，集成片上余数编码器、SOT-MRAM近存CNN引擎与混合基数单元。设计双通道选择性通道关闭优化，CIFAR-10精度达94.63%，计算量最高缩减89%，相较主流PIM平台功耗提升3.4倍、运行速度最高提速71倍。 |
| [解耦分块注意力与混合存内计算的边缘ViT高效加速器<br>Efficient Edge Vision Transformer Accelerator with Decoupled Chunk Attention and Hybrid Computing-In-Memory](efficient_edge_vision_transformer_accelerator_with_decoupled_chunk_attention_and_hybrid_computing_in_memory.md) | 本文面向边缘像素级密集预测任务，提出算法硬件协同ViT加速器。算法设计解分块注意力DCA降低访存；硬件融合RRAM+SRAM混合CIM，搭配串并行融合调度、双向可重构CIM宏。SegFormer测试最高提速217.1倍，访存缩减1.7~7.4倍，能效提升1.8倍，精度损失不足1%。 |
| [3D-CIMlet：面向边缘LLM推理与持续学习的异构存内芯粒协同设计框架<br>3D-CIMlet: A Chiplet Co-Design Framework for Heterogeneous In-Memory Acceleration of Edge LLM Inference and Continual Learning](3d_cimlet_a_chiplet_co_design_framework_for_heterogeneous_in_memory_acceleration_of_edge_llm_inference_and_continual_learning.md) | 本文提出3D-CIMlet协同设计框架，面向边缘大模型推理与持续学习，融合RRAM/eDRAM异构存内计算芯粒，搭建热感知、存储可靠性感知多尺度建模工具，配套模型-芯粒映射策略。相较传统2D方案，2.5D、3D架构能效分别提升9.3倍、12倍，EDP最高下降92.5%。 |
| [BlockPIM：面向PIM长上下文LLM推理的内存管理优化<br>BlockPIM: Optimizing Memory Management for PIM-enabled Long-Context LLM Inference](blockpim_optimizing_memory_management_for_pim_enabled_long_context_llm_inference.md) | 本文提出BlockPIM跨通道分块内存管理方案，面向长上下文LLM存内推理。设计跨通道KV分块布局，配套轻量化硬件修改与跨通道注意力归约计算，解决现有PIM内存碎片、前缀缓存冗余、上下文长度受限三大痛点。多长文本数据集测试，相较SOTA PIM方案平均吞吐量提升62%。 |
| [PIMPAL：通过DRAM内算术查找加速边缘设备LLM推理<br>PIMPAL: Accelerating LLM Inference on Edge Devices via In-DRAM Arithmetic Lookup](pimpal_accelerating_llm_inference_on_edge_devices_via_in_dram_arithmetic_lookup.md) | 本文提出面向边缘小型LLM的LUT型存内计算架构PIMPAL，用于加速GEMV运算。设计子数组并行查找、局部感知映射LCM、LUT聚合LAG三大机制，解决传统LUT-PIM行激活多、精度受限问题。测试相较pLUTo提速17.8倍，相比PU型PIM面积开销降低40、单位面积性能提升25%。 |
### 存储与算力深度融合，赋能人工智能发展、提升数据处理效率 (8)

Storage Meets Computing Power for Advancing AI and Data Processing Efficiency (8)



- Session Chairs: Arman Roohi, Abhronil Sengupta

> 存内计算（CIM）正逐步发展为一种可实现高效人工智能加速的变革性技术，能够解决数据传输、能效以及计算瓶颈等各类难题。随着图神经网络、点云模型等多种网络拓扑结构推动深度学习持续发展，存内计算架构与配套框架正针对从边缘设备到数据中心的各类应用场景完成优化。本次专题研讨将探究面向k近邻检索、图神经网络、点云神经网络等任务的新型存内计算加速器，同时介绍适用于边缘人工智能的混合存内计算解决方案。此外，内容还涵盖神经网络模型的各类优化方法，并提供一套用于搭建与评测存内计算平台的系统化框架。

> Compute-in-Memory (CIM) is emerging as a transformative approach for efficient AI acceleration, addressing challenges in data movement, energy efficiency, and computational bottlenecks. As deep learning evolves with diverse network topologies like GNNs and point-cloud models, CIM architectures and frameworks are being optimized for a wide range of use cases, from edge devices to data centers. This session explores novel CIM-based accelerators for tasks such as kNN search, graph neural networks, and point cloud neural networks, alongside hybrid CIM solutions for edge AI. It also covers optimization techniques for neural network models and presents a systematic framework for implementing and evaluating CIM platforms.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [PICK：面向点云k近邻检索的SRAM-PIM加速器<br>PICK: An SRAM-based Processing-in-Memory Accelerator for K-Nearest-Neighbor Search in Point Clouds](pick_an_sram_based_processing_in_memory_accelerator_for_k_nearest_neighbor_search_in_point_clouds.md) | 本文提出基于SRAM位串行存内计算的PICK加速器，面向点云kNN搜索。设计位宽裁剪缩短距离计算时延，过滤-选择混合策略适配任意k值，两级流水线并行计算与检索。实测相比SOTA BitNN提速4.17倍、能耗降低4.42倍，高精度场景精度损失可忽略。 |
| [HH-PIM：面向边缘AI设备的异构混合PIM动态功耗性能优化<br>HH-PIM: Dynamic Optimization of Power and Performance with Heterogeneous-Hybrid PIM for Edge AI Devices](hh_pim_dynamic_optimization_of_power_and_performance_with_heterogeneous_hybrid_pim_for_edge_ai_devices.md) | 本文提出HH-PIM异构混合存内计算架构，分为高性能HP与低功耗LP两类MRAM-SRAM混合PIM簇。设计动态DP数据放置算法，在时延约束下最小推理能耗。基于RISC-V处理器与FPGA原型验证，相比传统PIM平均节能60.43%，适配各类动态边缘AI负载。 |
| [先锚定再加速：利用驻留数据推动PIM上的GNN革命<br>Anchor First, Accelerate Next: Revolutionizing GNNs with PIM by Harnessing Stationary Data](anchor_first_accelerate_next_revolutionizing_gnns_with_pim_by_harnessing_stationary_data.md) | 本文提出软硬件协同PIM架构Anchor，遵循“最大化驻留数据、最小化迁移数据”核心准则。设计Mastav图划分算法提升本地驻留顶点占比，配套推拉混合数据流与分层广播规约通信机制。在GCN/GIN/GraphSage测试，相较主流GNN加速器平均提速3.1~13.01倍，能耗降低1.58~14.4倍。 |
| [3D-SubG：面向子图GNN的三维堆叠近存/存内混合加速器<br>3D-SubG: A 3D Stacked Hybrid Processing Near/In-Memory Accelerator for Subgraph GNNs](3d_subg_a_3d_stacked_hybrid_processing_near_in_memory_accelerator_for_subgraph_gnns.md) | 本文提出3D-SubG三维堆叠近存/存内混合加速器，面向子图图神经网络。采用混合键合堆叠逻辑裸片与DRAM裸片，设计比特级非零收集稀疏优化、负载均衡子图映射、分布式全局池化三大技术。22nm流片对比RTX3090Ti，平均性能提升146.11倍，能效提升1171.80倍。 |
| [PIMDup：真实PIM系统上的优化型去重设计<br>PIMDup: An Optimized Deduplication Design on a Real Processing-in-Memory System](pimdup_an_optimized_deduplication_design_on_a_real_processing_in_memory_system.md) | 本文面向UPMEM商用DPU存内硬件提出PIMDup去重系统，解决DPU无互通、乘法低效、上下行带宽失衡、分块边界不一致四大痛点。设计防割裂分段、编码边界向量、局部最大值分块三大优化，VM数据集验证相比CPU基线提速1.67倍，分块结果完全一致。 |
| [面向点式点云神经网络的高效存内计算加速器<br>An Efficient Compute-in-Memory based Accelerator for Point-based Point Cloud Neural Networks](an_efficient_compute_in_memory_based_accelerator_for_point_based_point_cloud_neural_networks.md) | 本文面向边缘点云神经网络提出软硬件协同存算加速器Point-CIM。设计VMP分块+通道最小值基点分解提升偏移比特稀疏，BTQ无硬件开销截断量化，可重构双模CIM单元配合预分解数据流削减片上数据搬运。在PointNet++测试，相较各类基线加速1.69~9.63倍，能效提升3.11~17.32倍。 |
| [NDFT：近数据计算系统上的密度泛函理论软硬件协同加速<br>NDFT: Accelerating Density Functional Theory Calculations via Hardware/Software Co-Design on Near-Data Computing System](ndft_accelerating_density_functional_theory_calculations_via_hardware_software_co_design_on_near_data_computing_system.md) | 本文提出面向LR-TDDFT第一性原理计算的近数据协同框架NDFT，适配CPU-NDP异构架构。设计代价感知任务调度，优化赝势共享存储软硬件协同方案。硅原子多体系仿真表明，大规模体系下相对CPU提速5.2倍、相对GPU提速2.5倍，大幅缓解访存与内存溢出瓶颈。 |
| [CIMFlow：数字CIM系统化设计与评估一体化框架<br>CIMFlow: An Integrated Framework for Systematic Design and Evaluation of Digital CIM Architectures](cimflow_an_integrated_framework_for_systematic_design_and_evaluation_of_digital_cim_architectures.md) | 本文提出CIMFlow一体化数字存内计算设计评估框架，集成分层可扩展ISA、两级编译器、周期精确仿真器。基于DP动态规划划分策略解决SRAM容量瓶颈，覆盖DNN编译到性能全流程评测。对比基线编译方案，推理最高提速2.8倍、能耗降低61.7%，支持多硬件配置设计空间探索。 |
### 厌倦人工智能？面向机器学习之外应用的以内存为中心计算技术 (6)

Need a Break from AI? Memory-centric Computing for Beyond Machine Learning Application

- Session Chairs: Shaahin Angizi, Dinesh Somasekhar

> 近存计算加速与存内计算加速正成为解决数据密集型任务算力瓶颈的主流高效计算范式，其应用场景已超越机器学习领域。本次专题将追溯该技术的发展本源，聚焦存内加速器、近存加速器与存储加速器这类非传统计算架构，探讨面向机器学习以外各类应用的加速方案。具体而言，专题收录的论文涵盖向量相似度检索加速、全同态加密、映射与调度优化算法，以及搭载指令集扩展的缓存内加速器等多个研究方向。

> Near-memory and in-memory acceleration are emerging as powerful paradigms for addressing computational bottlenecks in data-intensive tasks and have applications beyond ML. This session, a fresh look at the roots, covers acceleration of beyond ML applications using unconventional computing architectures with a focus on in-memroy, near-memory and storage accelerators. More specifically, it includes papers ranging from acceleration of vector similarity search, fully homomorphic encryption, algorithms for mapping and scheduling optimization, and in-cache accelerators with ISA extension.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Ares：面向FHE私有集合求交的高性能近存加速器<br>Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection](ares_high_performance_near_storage_accelerator_for_fhe_based_private_set_intersection.md) | 本文软硬件协同设计面向FHE隐私求交的近存加速器Ares，提出延迟重线性化LazyRelin削减冗余运算；硬件划分访存/计算双流水区域，基于SmartSSD近存架构规避PCIe传输瓶颈。实测相比CPU提速47.99倍，超越Poseidon、FAB加速器，能效分别提升7.96倍、10.95倍。 |
| [GraphAccel：基于页打包与投机搜索优化的图检索存储内加速器<br>GraphAccel: An In-Storage Accelerator for Efficient Graph-Based Vector Similarity Search Using Page Packing and Speculative Search Optimization](graphaccel_an_in_storage_accelerator_for_efficient_graph_based_vector_similarity_search_using_page_packing_and_speculative_search_optimization.md) | 本文提出GraphAccel SSD存内向量检索加速器，面向十亿级图结构ANNS。设计基于共享入边权重的图分块页打包算法减少闪存访问，搭配可丢弃投机搜索充分利用SSD通道并行。在SIFT1B等数据集验证，相比DiskANN、DiskANN++延迟分别降低80.5%、73.4%，召回率保持不变。 |
| [CIM-BLAS：面向BLAS的存内计算加速器<br>CIM-BLAS: Computing-in-Memory Accelerator for BLAS](cim_blas_computing_in_memory_accelerator_for_blas.md) | 本文提出首个基于非易失存储的BLAS存内加速器CIM-BLAS，设计统一五阶段浮点流水线解决存内指数对齐难题，配套可配置数据流覆盖一至三级BLAS核心算子。对比V10 GPU，一级/二级算子提速数千倍，三级BLAS能效提升2.6~24.1倍，矩阵规模越大优势越显著。 |
| [分段角度预处理：高精度高效率的存内向量相似检索<br>Segmented Angular Pre-Processing for Accurate and Efficient In-Memory Vector Similarity Search](segmented_angular_pre_processing_for_accurate_and_efficient_in_memory_vector_similarity_search.md) | 本文提出Seg-Cos TCAM内存向量相似度检索框架，面向余弦相似度度量。设计分段余弦度量、角度量化、幅值感知区间生成与莫比乌斯循环编码，无需改动TCAM硬件。小样本/近似检索任务测试，精度提升2.2%，召回提升10%~52%，能效最高提升2倍。 |
| [面向交叉阵列多核CIM系统的高效权重映射与资源调度<br>Efficient Weight Mapping and Resource Scheduling on Crossbar-based Multi-core CIM Systems](efficient_weight_mapping_and_resource_scheduling_on_crossbar_based_multi_core_cim_systems.md) | 本文面向eFlash多核交叉阵列CIM片上系统，设计配套编译层权重映射与资源调度方案。构建多层硬件抽象模型，提出进化式资源调度、ILP加权扩展权重映射。在Yolov5、ResNet等网络实测，整体延迟降低76%，硬件资源利用率提升30%，交叉阵列最高利用率达94.7%。 |
| [ARCANE：面向近存扩展的自适应RISC-V缓存架构<br>ARCANE: Adaptive RISC-V Cache Architecture for Near-memory Extensions](arcane_adaptive_risc_v_cache_architecture_for_near_memory_extensions.md) | 本文提出ARCANE自适应RISC-V近存缓存架构，可直接替换MCU末级缓存，兼具存储与协处理功能。基于CV-X-IF协处理器接口实现自定义矩阵指令卸载，配套缓存运行时管理冲突与DMA搬运。65nm工艺综合，8bit卷积相比标准CPU最高提速84倍，最大面积开销仅41.3%。 |
### 突破壁垒：面向Transformer加速的存内计算技术 (8)

Breaking Barriers: Compute-in-Memory for Transformer Acceleration (8)


- Session Chairs: Steve Dai, Haitong Li

> 本场会议聚焦存内计算（CIM）架构领域具有突破性的创新技术，该架构旨在加速大规模Transformer模型运算，缓解数据传输瓶颈。内容涵盖多种优化方案，既有面向大语言模型（LLM）注意力计算的存内计算解决方案，也包含适配长上下文推理的高效内存管理方案。会议深入探讨软硬件协同设计技术，包括非规则注意力稀疏化、异常值感知量化、混合专家（MoE）架构、三维混合键合技术以及新型异步执行方案。

> This session highlights groundbreaking innovations in Compute-in-Memory (CIM) architectures designed to accelerate large-scale transformer models and alleviate data transfer bottlenecks. It covers various optimization strategies, from CIM-based solutions for attention computation in large language models (LLMs) to efficient memory management for long-context inference. The session delves into software-hardware co-design techniques, including irregular attention sparsity, outlier-aware quantization, Mixture-of-Experts (MoE) approaches, 3D hybrid bonding, and novel asynchronous execution methods.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [DIAS：树形PIM架构下超长序列Transformer的距离稀疏注意力<br>DIAS: Distance-based Attention Sparsity for Ultra-Long-Sequence Transformer with Tree-like Processing-in-Memory Architecture](dias_distance_based_attention_sparsity_for_ultra_long_sequence_transformer_with_tree_like_processing_in_memory_architecture.md) | 本文提出软硬件协同DIAS框架，包含基于图近似近邻的AKAttention稀疏注意力算法与树形TreePIM存内架构。构建K图筛选Top-K键向量，将解码复杂度降至O(1)；树型交换机扩展大容量高带宽KV缓存。在Llama3-405B百万序列测试，最高提速171.7倍，精度损失小于1%。 |
| [AttenPIM：通过双模式GEMV加速LLM注意力的存内计算架构<br>AttenPIM: Accelerating LLM Attention with Dual-mode GEMV in Processing-in-Memory](attenpim_accelerating_llm_attention_with_dual_mode_gemv_in_processing_in_memory.md) | 本文软硬件协同设计AttenPIM存内计算架构，针对LLM注意力两类GEMV运算设计双模式计算单元，配套KV专用存储布局、头/令牌级并行调度，结合动态分配与算子融合优化。基于28nm工艺验证，对比NeuPIM、AttAcc，速度提升1.13~5.26倍，能耗降低17%~49%。 |
| [SplitSync：高性能DRAM-PIM的Bank Group级分同步机制<br>SplitSync: Bank Group-Level Split-Synchronization for High-Performance DRAM PIM](splitsync_bank_group_level_split_synchronization_for_high_performance_dram_pim.md) | 本文提出SplitSync分同步DRAM存内计算架构，以Bank Group为单位组内同步、组间异步执行，规避tFAW时序约束带来的行激活开销。设计分组独立IO与多组结果锁存，无需大电容/共享累加器。CNN/Transformer/GEMV测试，相较传统、ACT16、异步PIM吞吐分别提升1.70×、1.02×、1.06×，单PU面积开销仅1.5%。 |
| [PIMoE：通过节流感知卸载实现NPU-PIM上的高效MoE部署<br>PIMoE: Towards Efficient MoE Transformer Deployment on NPU-PIM System through Throttle-Aware Task Offloading](pimoe_towards_efficient_moe_transformer_deployment_on_npu_pim_system_through_throttle_aware_task_offloading.md) | 本文提出NPU-PIM异构协同架构PIMoE，面向MoE Transformer推理。设计节流感知任务卸载平衡异构负载，近内存数据压缩器解决稀疏数据布局失配。基于Switch系列模型验证，相较A100提速4.5倍、能效提升13.7倍，优于现有MoE专用加速器1.4倍。 |
| [支持寄存器寻址模式的DRAM内PIM指令集扩展<br>Supporting Register-based Addressing Modes for in-DRAM PIM ISAs](supporting_register_based_addressing_modes_for_in_dram_pim_isas.md) | 本文面向DMA型DRAM存内指令集PISA，提出索引、基偏移两种寄存器寻址模式。基偏移复用指令消除重复下发开销，索引寻址依托片上LUT在PIM内完成激活一元运算，减少CPU-PIM数据搬运。Transformer模型测试最高提速1.94倍，硬件仅增加4.65%面积、8.61%功耗。 |
| [OutlierCIM：具备混合量化与统一FP-INT计算的异常值感知数字CIM LLM加速器<br>OutlierCIM: Outlier-Aware Digital CIM-Based LLM Accelerator with Hybrid-Strategy Quantization and Unified FP-INT Computation](outliercim_outlier_aware_digital_cim_based_llm_accelerator_with_hybrid_strategy_quantization_and_unified_fp_int_computation.md) | 本文提出OutlierCIM，面向LLM激活异常值实现算法-数字存内计算软硬件协同框架。设计异常值分块、混合量化、统一FP-INT运算三大优化，配套可重构双比特CIM宏。28nm流片验证，相较OliVe、Oltron最高提速3.91倍、能效提升4.54倍，支持4bit低精度推理。 |
| [基于3D DRAM-逻辑混合键合的近存LLM推理处理器<br>Near-Memory LLM Inference Processor based on 3D DRAM-to-logic Hybrid Bonding](near_memory_llm_inference_processor_based_on_3d_dram_to_logic_hybrid_bonding.md) | 本文基于3D混合键合(HB)提出近内存LLM推理架构HB-NPU，采用集中控制器与双I/O通路解决分布式控制器面积开销、算力频率受限问题。支持可重构GEMM/GEMV/TS-GEMM数据流，OPT66B仿真相较NPU、DRAM-PIM、异构系统分别提速2.9/3.5/2.5倍，能耗大幅降低。 |
| [SeIM：面向近似最近邻检索的分层存内加速<br>SeIM: In-Memory Acceleration for Approximate Nearest Neighbor Search](seim_in_memory_acceleration_for_approximate_nearest_neighbor_search.md) | 本文提出分层存内加速架构SeIM，面向IVF-PQ量化近似近邻检索。区分访存密集向量/查表运算、计算密集排序任务，分别在DRAM Bank与内存控制器部署专用单元，配套统一执行模型与自适应传输过滤。十亿级向量测试，相较CPU/GPU/ASIC吞吐最高提升268倍、时延降低306倍、能效提升3081倍。 |
## DES3：新型计算模型 (8)

DES3: Emerging Models of ComputatioN

### 面向机器学习及更多领域的模型与硬件 (8)

Models and Hardware for Machine Learning and Beyond

- Session Chairs: Cheng Wang, Jun Shiomi

> 本次研讨将展示八篇面向新型计算模型的硬件与算法设计相关研究成果，覆盖人工智能、机器学习、神经形态计算、生物信息学、近似计算、生物芯片等诸多领域。入选成果面向通用人工智能与机器学习应用，提出了创新算法与硬件架构，同时涵盖向量符号人工智能这类专用人工智能模型。这些成果集中展示了多样化的计算技术，剖析了各类新兴计算范式当前面临的挑战，并介绍了领域内最前沿的解决方案。

> In this session, we will present eight works on hardware and algorithm design for emerging computing models. These span a wide range of areas, including AI, machine learning, neuromorphic computing, bioinformatics, approximate computing, and biochips. The selected works feature novel algorithms and hardware architectures for both general AI and machine learning applications, as well as specialized AI models such as vector symbolic AI. Together, they showcase a diverse array of computing techniques, highlighting the challenges and state-of-the-art solutions within these evolving paradigms.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Pipirima：通过稀疏模式预测加速矩阵代数<br>Pipirima: Predicting Patterns in Sparsity to Accelerate Matrix Algebra](pipirima_predicting_patterns_in_sparsity_to_accelerate_matrix_algebra.md) | 本文提出基于计数器预测的稀疏矩阵加速器Pipirima，设计两类轻量预测器预判矩阵结构与每行非零元数量，解决稀疏计算负载失衡问题。适配SpMV/SpMM，SuiteSparse与BERT稀疏注意力测试，相较Tensaurus、ExTensor分别提速4~6倍、最高40倍，预测硬件面积功耗开销极低。 |
| [FactorHD：面向多对象多类别表示与分解的超维计算模型<br>FactorHD: A Hyperdimensional Computing Model for Multi-Object Multi-Class Representation and Factorization](factorhd_a_hyperdimensional_computing_model_for_multi_object_multi_class_representation_and_factorization.md) | 本文提出FactorHD超维计算模型，面向多对象多层级类-子类分层表征与因式分解。设计捆绑-绑定三层编码规避叠加灾难、二值问题，配套阈值筛选分解算法，复杂度降至O(N_M)。基准测试最高提速5667倍，结合ResNet-18在Cifar-10上因式精度达92.48%。 |
| [面向资源严苛场景的二值向量符号架构整体设计<br>Holistic Design towards Resource-Stringent Binary Vector Symbolic Architecture](holistic_design_towards_resource_stringent_binary_vector_symbolic_architecture.md) | 本文面向资源受限植入式BCI等边缘设备，提出UniVSA软硬件协同二值向量符号计算框架。设计差异化投影、二值卷积特征交互、软集成投票三大算法模块；配套流水线FPGA硬件架构。多类脑电/传感数据集验证，平均分类精度优于LDC等现有VSA，模型内存仅8.31KB，功耗低于0.5W。 |
| [SDISC：具备原位计算的脉冲驱动实时低功耗人机交互系统<br>SDISC: A Spike-Driven Human-Machine Interface with In-Situ Computing for Real-Time Low-Power Interaction](sdisc_a_spike_driven_human_machine_interface_with_in_situ_computing_for_real_time_low_power_interaction.md) | 本文提出SDISC脉冲驱动原位计算人机交互架构，面向EMG肌电信号实时低功耗处理。设计可配置PL-LIF脉冲特征提取、RRAM存内SNN分类器，搭配SAD蒸馏、ALO局部修复缓解器件非理想。实测单样本功耗39.72µW、延迟34µs，长期推理精度稳定约98%。 |
| [ANGraph：面向异步神经形态硬件的GNN性能预测框架<br>ANGraph: A GNN-Based Performance Prediction Framework for Asynchronous Neuromorphic Hardware](angraph_a_gnn_based_performance_prediction_framework_for_asynchronous_neuromorphic_hardware.md) | 本文提出ANGraph异步神经硬件性能预测框架，将系统仿真事件流转为图结构，分别采用GNN（ANGraph-L）、ResNet（ANGraph-P）预测延迟与功耗，构建百万级跨尺度工艺基准。对比TrueAsync仿真，平均R²提升0.69、RMSE下降76%，功耗预测R²达0.98、MAPE仅0.88%，泛化性优异。 |
| [PairGraph：面向高性能并发点对查询的搜索空间感知加速器<br>PairGraph: An Efficient Search-space-aware Accelerator for High-performance Concurrent Pairwise Queries](pairgraph_an_efficient_search_space_aware_accelerator_for_high_performance_concurrent_pairwise_queries.md) | 本文提出面向并发点对点图查询的PairGraph专用加速器，设计感知搜索空间SPM处理模型，通过无冗余共享区域生成、重叠驱动执行挖掘时空局部性。28nm流片仿真验证，对比CPU/GPU与多款图加速器，提速1.67~14.25倍，片上缓存复用大幅降低片外访存与能耗。 |
| [PreDAC：预精炼增强的高效近似计算设计空间探索框架<br>PreDAC: An Efficient Framework of Pre-Refining Enhanced Design Space Exploration for Approximate Computing](predac_an_efficient_framework_of_pre_refining_enhanced_design_space_exploration_for_approximate_computing.md) | 本文提出PreDAC近似计算设计空间探索框架，包含双层预精简流程与代价性能导向DSE算法。构建55类近似乘法器库，基于输入分布筛除冗余设计空间，搭配可调参代价公式与回溯微调。测试下预精简可提速最高87倍，自研DSE相较FPAX提速7.7倍、硬件开销再优化8.8%。 |
| [AutoRE：面向流控微流控生物芯片的贝叶斯自动可靠性增强工具<br>AutoRE: Bayesian-Optimization-based Automatic Reliability Enhancement Tool for Flow-based Microfluidic Biochips](autore_bayesian_optimization_based_automatic_reliability_enhancement_tool_for_flow_based_microfluidic_biochips.md) | 本文提出AutoRE，首款基于贝叶斯优化的流控微流控芯片版图自动可靠性提升工具。在保持拓扑不变前提下分段微调版图，搭配堵塞、泄漏双失效量化模型，采用随机森林代理与logEI采集函数寻优。全部测试用例平均可靠性提升约40%，相比随机搜索寻优效率大幅提升。 |
## DES4：数字与模拟电路 (8)

DES4: Digital and Analog Circuits (8)

### 超大规模集成电路领域的突破：高能效人工智能与革命性电路技术 (8)

Breakthroughs in VLSI: Power-Efficient AI and Revolutionary Circuitry

- Session Chairs: Ioannis Savidis, Kishor Kunal

> 本场专题会议汇集了超大规模集成电路设计、能效优化、人工智能驱动设计自动化以及先进电路领域内的突破性研究与创新成果。会议旨在研讨各类突破技术、电路与系统现有极限的前沿进展，议题涵盖深度神经网络加速器、人工智能驱动设计自动化以及模拟电路设计创新。同时，会议还介绍数字设计领域各类新型节能技术，包括面向机器人感知的概率量子隧穿技术、多功能背面金属层，以及适用于RISC-V内核与视频编码的低功耗解决方案。本次会议全面梳理了塑造半导体技术与电子设计未来的各类挑战、研究方法及重大技术突破。

> This session brings together groundbreaking research and innovative advancements in the fields of VLSI design, power efficiency, AI-driven design automation, and advanced circuitry. The goal is to explore and discuss the latest developments that are pushing the boundaries of technology, circuits, and systems. The session presents topics on DNN accelerators, AI-driven design automation, and innovations in analog circuit design. The session also covers new energy efficient technologies in digital design, including probabilistic quantum tunneling for robotic perception and multifunctional backside metal layers, as well as energy-efficient solutions for RISC-V cores and video coding. It provides a comprehensive overview into the challenges, methodologies, and breakthroughs shaping the future of semiconductor technology and electronic design.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [EPIC：面向电压降额MAC的误差预测与校正<br>EPIC: Error PredIction and Correction for Power-Efficient Voltage Underscaling Multiply-Accumulate Unit](epic_error_prediction_and_correction_for_power_efficient_voltage_underscaling_multiply_accumulate_unit.md) | 本文提出EPIC时序误差预测校正框架，面向电压降额MAC单元。设计预测比特搜索算法、低功耗跳变检测器与传输门短路径填充，搭配可调延迟时钟完成全位纠错。28nm工艺下总面积开销仅8%，最高节电52%；MLP推理同等精度下功耗再降11%，相较同类弹性电路面积节省60%~88%。 |
| [PoP-ECC：面向DNN加速器多比特翻转的鲁棒灵活纠错<br>PoP-ECC: Robust and Flexible Error Correction against Multi-Bit Upsets in DNN Accelerators](pop_ecc_robust_and_flexible_error_correction_against_multi_bit_upsets_in_dnn_accelerators.md) | 本文提出两层纠错码PoP-ECC，并结合逐通道量化形成Q+PoP方案，面向DNN加速器SRAM多比特翻转(MBU)容错。通过虚拟奇偶VP与奇偶之PP两级编码，无需存储VP即可校正相邻双错误DAE。测试相较VAPI最高耐受31.62倍DAE比例，编解码时延、面积功耗开销极低。 |
| [AdreamDCO：AI驱动的稳健高效数字控制振荡器自动化设计<br>AdreamDCO: AI-Driven Robust and Efficient Design Automation for Digitally Controlled Oscillators](adreamdco_ai_driven_robust_and_efficient_design_automation_for_digitally_controlled_oscillators.md) | 本文提出AdreamDCO人机协同AI全自动化DCO设计流程，分主谐振腔、精细调谐两步完成有源无源协同设计。采用迁移学习残差代理模型替代耗时EM/电路仿真，差分进化逆设计快速生成版图，单次训练后80秒输出GDSII，覆盖1–20GHz。22nm流片FoM超192.4dBc/Hz，分辨率低于1.5kHz，优于人工设计。 |
| [EVA：面向新型模拟电路定向发现的高效通用生成引擎<br>EVA: An Efficient and Versatile Generative Engine for Targeted Discovery of Novel Analog Circuits](eva_an_efficient_and_versatile_generative_engine_for_targeted_discovery_of_novel_analog_circuits.md) | 本文提出EVA通用模拟电路生成引擎，采用引脚级欧拉序列表征电路，基于解码器Transformer先无标注预训练学习拓扑连接，再分别用PPO、DPO微调定向生成高性能新电路。覆盖11类模拟电路，电路有效率94、新颖度99，仅需850份标注样本，10次生成内FoM远超同类方法。 |
| [BS-PDN-Last：利用多功能背面金属层实现最优供电网络设计<br>BS-PDN-Last: Towards Optimal Power Delivery Network Design With Multifunctional Backside Metal Layers](bs_pdn_last_towards_optimal_power_delivery_network_design_with_multifunctional_backside_metal_layers.md) | 本文提出BS-PDN-last后端供电版图流程，将电源布线延后至时钟/信号布线完成后，搭配预占位规划与分层补充分布式电源带。解决传统PDN-first流程时钟单元移位、时序恶化矛盾。3nm工艺多芯片验证，总负时序余量降低90%，最高性能提升12%，能效提升18.9%。 |
| [利用概率量子隧穿的混合信号BNN引擎：迈向不确定性感知机器人感知<br>Towards Uncertainty-aware Robotic Perception via Mixed-signal BNN Engine Leveraging Probabilistic Quantum Tunneling](towards_uncertainty_aware_robotic_perception_via_mixed_signal_bnn_engine_leveraging_probabilistic_quantum_tunneling.md) | 本文基于FD-SOI器件量子隧穿效应设计混合信号BNN存内引擎，实现机器人感知不确定性量化。将权重分解为均值与方差模块，集成并行高斯随机单元，单样本能耗仅200f。水下AUV定位测试，相比现有BNN硬件延迟降低千倍，重采样数据量减少4.5倍，硬件面积增幅不足2倍。 |
| [能效顺序RISC-V核上整数与浮点混合负载的双发射执行<br>Dual-Issue Execution of Mixed Integer and Floating-Point Workloads on Energy-Efficient In-Order RISC-V Cores](dual_issue_execution_of_mixed_integer_and_floating_point_workloads_on_energy_efficient_in_order_risc_v_cores.md) | 本文提出COPIFT软硬件协同方法与配套RISC-V ISA扩展，在Snitch顺序RISC-V核上实现整数/浮点混合代码持续双发射，解决原有伪双发射存在指令依赖限制。经蒙特卡洛、 transcendental函数等负载验证，平均加速1.47倍，峰值IPC达1.75，整体能效平均提升1.37倍，硬件面积时序开销可忽略。 |
| [面向视频编码的高精度低成本近似变换加速器<br>A High-Precision and Low-Cost Approximate Transform Accelerator for Video Coding](a_high_precision_and_low_cost_approximate_transform_accelerator_for_video_coding.md) | 针对VVC多变换硬件资源开销大问题，本文挖掘DCT2与DST7矩阵对角聚集特性，最小二乘稀疏优化转换矩阵，搭配矩阵分解优化DCT2，复用移位加法单元构建统一流水线加速器。支持4~32点三类变换，28nm工艺下硬件资源降低44%，码率损失仅0.53%，可实时处理8K@57fps视频编码。 |
## DES5：新兴器件与互连技术 (8)

DES5: Emerging Device and Interconnect Technologies

### 塑造未来：协同研发面向计算领域及更广范畴的新兴技术 (8)

Shaping Tomorrow: Co-Designing Emerging Technologies for Computing and Beyond 



- Session Chairs: Xunzhao Yin, Doo Seok Jeong

> 人工智能与计算技术飞速迭代，亟需融合硬件、算法与系统的创新协同设计方案。本场专题研讨聚焦新兴技术与协同设计方法交叉领域的前沿研究，研讨议题包含抗漂移神经网络、高速互联标准（CXL，计算快速互联）优化、铁电与自旋轨道力矩磁随机存取存算一体架构、单片三维集成，以及面向生物医学诊断的传感器内计算技术。相关研究围绕能效、可扩展性、性能等行业痛点展开攻关，充分印证协同设计能够释放人工智能及其他领域先进技术的全部潜力，为下一代计算系统的发展奠定基础。

> The rapid evolution of AI and computing demands innovative co-design approaches that integrate hardware, algorithms, and systems. This session explores cutting-edge research at the intersection of emerging technologies and co-design methodologies. Topics include drift-tolerant neural networks, Compute Express Link (CXL) optimization, ferroelectric and SOT-MRAM compute-in-memory architectures, monolithic 3D integration and in-sensor computing for biomedical diagnostics. By addressing challenges such as energy efficiency, scalability, and performance, these works showcase how co-design can unlock the full potential of advanced technologies for AI and other domains, paving the way for next-generation computing systems.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [DBC：面向抗漂移深度神经网络的漂移感知二进制编码<br>DBC: Drift-aware Binary Code for Drift-tolerant Deep Neural Networks](dbc_drift_aware_binary_code_for_drift_tolerant_deep_neural_networks.md) | 本文提出DBC漂移感知二进制编码，适配真实IBM MLC PCM器件。将小数值映射至低漂移可靠单元层级，搭配SCSR单符号单元支持有符号DNN权重，无需辅助比特，可兼容ECC。多视觉、NLP、大模型测试，相比传统格雷码最高提升55.18倍漂移耐受度。 |
| [CXL-Interplay：现代计算系统中CXL干扰机制揭示与表征<br>CXL-Interplay: Unraveling and Characterizing CXL Interference in Modern Computer Systems](cxl_interplay_unraveling_and_characterizing_cxl_interference_in_modern_computer_systems.md) | 本文提出CXL-Interplay评测框架，基于两款真实ASIC/FPGA CXL硬件，系统刻画CXL与主存、SSD之间的相互性能干扰。通过微基准与数据库、LLM等真实负载定位TOR队列、缓存抢占等根因，提出cgroup、内存带宽限制等软件调控方案，最高恢复主存带宽至原始99%。 |
| [VQT-CiM：基于铁电存内计算加速矢量量化增强Transformer<br>VQT-CiM: Accelerating Vector Quantization Enhanced Transfomer with Ferroelectric Compute-in-Memory](vqt_cim_accelerating_vector_quantization_enhanced_transfomer_with_ferroelectric_compute_in_memory.md) | 本文提出基于FeFET存内计算的VQT-CiM架构，采用键值联合矢量量化消除注意力动态矩阵乘与运行时写操作。融合残差/乘积矢量量化缓解精度损失，设计并行RVQ数据流与配套数字外设。BERT系列任务测试，相较主流NVM CiM加速器能效提升3.54倍、吞吐提升4.53倍，模型精度平均仅下降0.8%。 |
| [提升片上学习SOT-MRAM-CIM并行性与能效<br>Enhancing Parallelism and Energy-Efficiency in SOT-MRAM based CIM Architecture for On-Chip Learning](enhancing_parallelism_and_energy_efficiency_in_sot_mram_based_cim_architecture_for_on_chip_learning.md) | 本文面向片上学习场景，提出多端口SOT-MRAM存内计算架构。设计1写6读新型单元，配套批量写权重更新机制、多向量并行推理调度。45nm工艺仿真，相比传统单端口SOT-CIM，时延降低5.82倍、能效提升3.20倍，仅小幅增加芯片面积。 |
| [面向组合优化的铁电存内原位退火器件-算法协同设计<br>Device-Algorithm Co-Design of Ferroelectric Compute-in-Memory In-Situ Annealer for Combinatorial Optimization Problems](device_algorithm_co_design_of_ferroelectric_compute_in_memory_in_situ_annealer_for_combinatorial_optimization_problems.md) | 本文提出基于双栅铁电晶体管(DG FeFET)的存内退火器，软硬件协同设计增量E变换算法，将Ising能量计算复杂度从O(n²)降至O(n)，舍弃指数退火运算。依托背栅可调特性实现片上原位退火，3000节点Max-Cut测试能耗、时延分别降低1716×、8.15倍，求解成功率达98%。 |
| [DANN：面向多生物标志物诊断的传感内衍射声学神经网络<br>DANN: Diffractive Acoustic Neural Network for in-sensor computing system target at multi-biomarker diagnosis](dann_diffractive_acoustic_neural_network_for_in_sensor_computing_system_target_at_multi_biomarker_diagnosis.md) | 本文首次提出基于声表面波SAW的衍射声学神经网络DANN，面向多生物标志物片上传感计算。设计FEA有限元协同梯度训练流水线，通过金属长度调控SAW相位实现网络权重。在抑郁症、前列腺癌诊断任务验证，诊断精度接近临床标准，系统功耗相比传统方案降低66%。 |
| [333-eDRAM：融合IGZO/CNT/硅三类晶体管的单片3D 3T嵌入式DRAM<br>333-eDRAM - 3T Embedded DRAM Leveraging Monolithic 3D Integration of 3 Transistor Types: IGZO, Carbon Nanotube and Silicon FETs](333_edram_3t_embedded_dram_leveraging_monolithic_3d_integration_of_3_transistor_types_igzo_carbon_nanotube_and_silicon_fets.md) | 本文提出333-eDRAM单片三维集成嵌入式DRAM，底层硅CMOS做外设，BEOL堆叠IGZO、CNT两类晶体管构成3T存储单元，融合三种器件优势。7nm工艺搭配Cortex-M0在Embench测试，相较纯硅eDRAM，系统EDP平均提升1.96倍，EADP提升5.15倍。 |
| [具备后端配置存储的单片3D FPGA设计与综合<br>Monolithic 3D FPGA Design and Synthesis with Back-End-of-Line Configuration Memories](monolithic_3d_fpga_design_and_synthesis_with_back_end_of_line_configuration_memories.md) | 本文提出基于BEOL氧化物半导体(AOS)的单片3D FPGA架构，采用W-In₂O₃(n)/SnO(p)晶体管实现配置存储与布线传输门。搭建适配M3D的COFFE与VTR评估流程，7nm工艺下相较传统CMOS FPGA，AT²乘积降低3.4倍，关键路径延迟下降27%，布线功耗减少26%，适配LLM、HDC等负载。 |
## DES6：量子计算 (20)

DES6: Quantum Computing 



### 量子电路的核心构建基石：综合、仿真与编译 (6)

Building Pillars of Quantum Circuits: Synthesis, Simulation & Compilation 

- Session Chairs: Alberto Marchisio, Zhiding Liang

> 本次研讨环节围绕量子计算线路综合、量子编译、量子线路仿真以及新型工具开发领域的全新研究成果展开探讨。第一篇论文提出一种融合ZX演算、线路划分与线路综合的全新方法，用于生成量子线路中的脉冲信号。量子布局综合（QLS）是量子程序编译的核心关键步骤；第二篇论文构建了一套已知最优交换门（SWAP）数量的基准测试集，可作为评估框架与研究工具，推动量子布局综合领域的技术发展。图态是一类高纠缠量子态，也是量子信息处理的核心资源，为此第三篇论文基于分治策略，提出一套面向量子发射源-光子图态生成的全新编译框架。第四篇论文设计了一套高效编译框架，该框架主要基于高层泡利基中间表示（IR）处理通用哈密顿量仿真程序，打通具备实用价值的量子应用与可物理实现方案之间的技术壁垒。经典计算机对量子线路的仿真始终是量子计算研究的核心工具，可用于量子算法开发、验证以及经典计算机性能对比；因此第五、第六篇论文分别研究基于联合切割、跨平台（中央处理器CPU、英伟达显卡Nvidia GPU）优化并搭载高性能后端的高效薛定谔形式仿真方案。

> This discussion session discusses new research contributions in quantum computing synthesis, quantum compilation, quantum circuit simulation, and novel tool development. The first paper proposes a novel approach combining ZX-Calculus, circuit partitioning, and circuit synthesis for pulse generation in quantum circuits. Quantum layout synthesis (QLS) is a critical step in quantum program compilation; the second paper introduces a benchmark with a known optimal SWAP count that will work as an evaluation framework and a tool for advancing QLS research. Graph state is a highly entangled quantum state and is a critical resource; therefore, the third paper proposes a novel compilation framework for emitter-photonic graph state generation, leveraging a divide-and-conquer strategy. The fourth paper proposes a highly effective compilation framework that primarily operates at the high-level Pauli-based intermediate representation (IR) for generic Hamiltonian simulation programs, thereby bridging the gap between impactful quantum applications and physically implementable solutions. Classical simulation of quantum circuits remains a central tool for quantum computing research—including developing and testing quantum algorithms as well as comparing classical computers; therefore, the fifth and sixth papers discuss efficient methods for Schrödinger-style simulations based on joint cutting and cross-platform (CPU and Nvidia GPU) optimization and high-performance backend support.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [EPOC：融合先进综合技术的量子电路脉冲生成框架<br>EPOC: A Novel Pulse Generation Framework Incorporating Advanced Synthesis Techniques for Quantum Circuits](epoc_a_novel_pulse_generation_framework_incorporating_advanced_synthesis_techniques_for_quantum_circuits.md) | 本文提出EPOC高效量子脉冲生成框架，融合ZX演算、贪心分块、单元门合成与均衡重组优化QOC流程。先图化简压缩电路深度，再平衡分块单元规模，解决细粒度门脉冲时延堆积问题。基于QASMBench测试，相较PAQOC时延降31.74%、传统门基方案降76.80%，整体保真度显著提升。 |
| [基于已知最优SWAP代价基准评估量子布局综合工具<br>Assessing Quantum Layout Synthesis Tools via Known Optimal-SWAP Cost Benchmarks](assessing_quantum_layout_synthesis_tools_via_known_optimal_swap_cost_benchmarks.md) | 本文提出QUBIKOS基准集，是首个具备可证明最优SWAP门数量的量子布局评测电路。设计分节电路构造法生成带确定最优交换开销的量子线路，可量化各类QLS工具最优间隙。在四款主流量子硬件评测，最优间隙随芯片规模激增，还可用于定位路由算法缺陷。 |
| [面向发射光子图态的可扩展鲁棒编译框架<br>A Scalable and Robust Compilation Framework for Emitter-Photonic Graph State](a_scalable_and_robust_compilation_framework_for_emitter_photonic_graph_state.md) | 本文面向发射光子确定性图态编译难题，提出可扩展鲁棒编译框架。采用分治思想结合有限局部补全MIP图划分，子图独立编译后分时调度实现发射源复用，兼顾CNOT数量、电路时长、光子损耗多目标优化。相较基线，CNOT最高缩减52%、电路时长缩短56%，光子损耗抑制最高1.9倍。 |
| [Phoenix：面向NISQ设备的泡利高层优化执行引擎<br>Phoenix: Pauli-based High-level Optimization Engine for Instruction Execution on NISQ devices](phoenix_pauli_based_high_level_optimization_engine_for_instruction_execution_on_nisq_devices.md) | 本文提出面向NISQ设备VQA算法的PHOENIX高层编译引擎，基于二元辛形式BSF统一泡利IR，启发式克利福德变换批量简化泡利串，搭配俄罗斯方块式分组排序。兼容多量子指令集与硬件拓扑，UCCSD/QAOA测试相较主流编译器2Q门、电路深度大幅削减，算法保真误差更低。 |
| [联合切割：混合薛定谔-费曼量子电路仿真方法<br>Joint Cutting for Hybrid Schrödinger-Feynman Simulation of Quantum Circuits](joint_cutting_for_hybrid_schr_dinger_feynman_simulation_of_quantum_circuits.md) | 本文提出联合切割Joint Cutting混合薛定谔-费曼(HSF)量子电路仿真方法。将跨分区门合并为块统一施密特分解，抑制路径数量指数爆炸。基于QAOA电路测试，相较标准HS最高提速4000倍，相比纯薛定谔仿真最高快200倍，开源实现已发布。 |
| [薛定谔风格量子电路仿真的通用跨平台编译工具链<br>Versatile Cross-platform Compilation Toolchain for Schrodinger-style Quantum Circuit Simulation](versatile_cross_platform_compilation_toolchain_for_schrodinger_style_quantum_circuit_simulation.md) | 本文提出CAST跨平台薛定谔量子仿真编译工具链，设计稀疏感知自适应门融合与动态内核生成。基于CircuitTile电路中间结构，依托代价模型适配CPU/GPU，生成LLVM IR与PTX底层代码。32qubit CPU、30qubit GPU基准测试，相较Qiskit、cuQuantum分别最高提速8.03倍、39.3倍，稀疏电路增益尤为显著。 |
### 推动量子计算落地：从量子线路布线、量子纠错到量子机器学习（QML）(8)

Pushing Quantum Computing Reality from Routing to Error Corrections and QML 


- Session Chairs: Jinglei Cheng, Himanshu Thapliyal


> 本次专题研讨聚焦量子计算领域前沿创新思路，研究方向涵盖量子比特路由、量子比特读出、误差抑制、量子纠错、量子线路等价性校验，以及量子机器学习应用。第一篇论文提出一种全新启发式算法，用于解决量子比特路由难题。量子读出误差是系统最主要的噪声来源，因此第二、三、四篇论文分别给出三类解决方案：基于轻量级神经网络的量子比特读出架构、可扩展高保真三级读出方案，以及软硬件协同设计框架，该框架搭载嵌入式加速器以抑制读出误差。第五篇论文提出一种基于快速伊辛模型的高效量子纠错方法。第六篇论文介绍一套具备变革性的框架，依托ZX演算图抽象实现量子线路等价性校验。第七、八篇论文围绕量子机器学习（QML）展开研究，分别提出振幅嵌入方案，以及一套适配异构量子处理器、兼顾高效性与高精度的训练推理框架。

> This session explores new ideas in quantum computing, focusing on qubit routing, qubit readout, reducing errors, error correction, checking the equivalence of quantum circuits, and using quantum machine learning. The first paper aims to solve the qubit routing problem through a novel heuristic algorithm. Quantum readout error is the most significant source of error; therefore, the second, third, and fourth papers present qubit readout architecture leveraging lightweight neural networks, scalable high-fidelity three-level readout, and a software-hardware co-design approach that mitigates readout errors with an embedded accelerator. The fifth paper presents a fast-Ising model-based approach for efficient quantum error correction. The sixth paper discusses a transformative framework for quantum circuit equivalence checking using ZX calculus-based graph abstractions. The seventh and eighth papers focus on quantum machine learning (QML) through amplitude embedding and a framework for efficient and high-accuracy training and inference on heterogeneous quantum processing units.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [DDRoute：面向量子比特路由的深度驱动方法<br>DDRoute: a Novel Depth-Driven Approach to the Qubit Routing Problem](ddroute_a_novel_depth_driven_approach_to_the_qubit_routing_problem.md) | 本文提出面向NISQ量子线路的深度驱动布线算法DDRoute，配套DDPlace初始映射策略。设计兼顾线路深度的广义距离代价函数，优先并行SWAP降低时序开销。在多款大规模量子芯片测试，相比主流SABRE、t|ket⟩等工具线路深度最高降低70.4%，编译速度提升92.8倍。 |
| [KLiNQ：知识蒸馏辅助的FPGA量子比特读出轻量神经网络<br>KLiNQ: Knowledge Distillation-Assisted Lightweight Neural Network for Qubit Readout on FPGA](klinq_knowledge_distillation_assisted_lightweight_neural_network_for_qubit_readout_on_fpga.md) | 本文提出KLiNQ，面向FPGA设计知识蒸馏轻量化神经网络用于超导量子比特独立读出。搭建大教师网络蒸馏两类定制学生模型，支持电路中间测量。Zynq RFSoC验证，模型参数量削减99%，五比特平均读出保真度约0.91，单比特推理仅32ns，硬件资源开销极低。 |
| [多能级超导量子比特读出的高效可扩展架构<br>Efficient and Scalable Architectures for Multi-level Superconducting Qubit Readout](efficient_and_scalable_architectures_for_multi_level_superconducting_qubit_readout.md) | 本文提出适配超导三能级量子比特的可扩展读出架构，融合多类型匹配滤波器与轻量化神经网络。模型规模相较FNN缩减100倍，FPGA资源占用降低60倍，读出时长缩短20%，读出保真度相对提升6.6%，可快速检测泄漏误差，提升量子纠错可靠性。 |
| [DyREM：借助嵌入式加速器动态缓解量子读出误差<br>DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator](dyrem_dynamically_mitigating_quantum_readout_error_with_embedded_accelerator.md) | 本文提出软硬件协同DyREM嵌入式加速器，面向NISQ量子读出误差缓解。利用量子态非零稀疏性，设计动态下采样张量矩阵流，搭配非零态相似度检测消除冗余计算。FPGA实测相较主流方法提速9.6~2000倍，内存线性扩展，保真度提升1.03~1.15倍。 |
| [用于量子纠错的加权范围约束伊辛模型解码器<br>Weighted Range-Constrained Ising-Model Decoder for Quantum Error Correction](weighted_range_constrained_ising_model_decoder_for_quantum_error_correction.md) | 本文提出WRIM加权范围约束伊辛解码器用于表面码量子纠错。构建多边形区域圈定故障综合征削减建模变量，分档配置伊辛耦合与外场权重，整体复杂度O(n)。对比传统伊辛方案变量缩减97.8倍，D-Wave退火实现微秒级解码，纠错阈值10.7%~11.0%，优于MWPM解码器。 |
| [ZXNet：基于ZX演算驱动图神经网络的量子电路等价验证框架<br>ZXNet: ZX Calculus-Driven Graph Neural Network Framework for Quantum Circuit Equivalence Checking](zxnet_zx_calculus_driven_graph_neural_network_framework_for_quantum_circuit_equivalence_checking.md) | 本文提出ZXNet量子电路等价验证框架，融合ZX演算图表示与图卷积GNN。对ZX图标准化化简并提取节点/边特征，设计基于杰卡德指数的不确定性自适应损失函数。在4–120量子比特电路测试，验证精度99.4%，最高提速62倍，可扩展性、单量子验证耗时、精度相比SOTA分别提升45.83%、42.22%、5.94%。 |
| [EnQode：利用经典数据的快速QML振幅嵌入<br>EnQode: Fast Amplitude Embedding for Quantum Machine Learning using Classical Data](enqode_fast_amplitude_embedding_for_quantum_machine_learning_using_classical_data.md) | 本文提出EnQode快速振幅嵌入框架，面向NISQ量子机器学习。采用硬件适配低深度Ansatz、符号化参数优化、K-Means聚类+迁移学习，所有样本电路深度固定无差异。MNIST/CIFAR等测试，电路深度降45%、双量子门减35%，噪声下保真度提升13%，单样本编译提速36%。 |
| [ArbiterQ：在异构量子设备上通过个性化模型提升QNN收敛与精度<br>ArbiterQ: Improving QNN Convergency and Accuracy by Applying Personalized Model on Heterogeneous Quantum Devices](arbiterq_improving_qnn_convergency_and_accuracy_by_applying_personalized_model_on_heterogeneous_quantum_devices.md) | 本文提出面向异构NISQ量子设备的分布式QNN框架Arbiter。设计模型向量、行为向量统一表征电路硬件特征，提出相似度感知个性化梯度共享训练，以及量子shot细粒度环型调度推理方案。多数据集测试相比SOTA EQC收敛提速4.03倍，训练损失降低7.87%，推理损失减少24.71%。 |
### 量子领域重大突破催生颠覆性应用 (6)

Quantum Breakthroughs Creating Game-Changing Applications 


- Session Chairs: Saurabh Kotiyal, Sanjaya Lohani

> 本次研讨围绕量子计算各类颠覆性应用展开，内容涵盖量子计算在金融领域的落地方案、网络社区检测、量子机器学习相对经典模型的计算优势、量子密码分析，以及面向现实场景的分布式量子计算技术研发。第一篇论文依托全新设计的HHL量子算法架构，求解金融领域的投资组合优化问题。社区检测是网络分析领域的核心研究课题，第二篇论文验证了类量子混合方案在大规模图数据社区检测任务中的应用潜力。第三篇论文证明，相较于纯经典计算模型，混合量子神经网络具备更强的可扩展性与资源利用效率，有望成为处理复杂计算问题的优选方案。第四、五篇论文结合基于测量的逆计算与窗口算术技术，提出适用于量子密码分析的新型量子算术电路。分布式量子计算（DQC）是实现量子计算规模扩容的重要发展路径，因此第六篇论文针对分布式量子计算系统开展软硬件协同设计研究，为该技术在真实业务场景中实现更实用、高效的落地搭建理论与工程基础。

> The session discusses game-changing applications of quantum computing in finance, community detection, computational advantages of quantum machine learning over classical models, quantum cryptanalysis, and developing distributed quantum computing for real-world applications. The first paper solves portfolio optimization problems in finance with the help of a novel design of an HHL quantum algorithm. Community detection is an important problem in network analysis; the second paper demonstrates the potential of hybrid quantum-inspired solutions for advancing community detection in large-scale graph data. The third paper shows that hybrid quantum neural networks provide a more scalable and resource-efficient solution over purely classical models, positioning them as a promising alternative for tackling complex computational problems. The fourth and fifth papers discuss novel quantum arithmetic circuits for quantum cryptanalysis with the help of measurement-based uncomputation and windowed arithmetic. Distributed quantum computing (DQC) offers a promising pathway for scaling up quantum computing; therefore, the sixth paper discusses hardware-software co-design for DQC systems, paving the way for more practical and efficient implementations for real-world applications.



| 中英论文题目 | 研究概要 |
|------------|-----------|
| [SAPO：提升用于投资组合优化的量子线性求解器可扩展性与精度<br>SAPO: Improving the Scalability and Accuracy of Quantum Linear Solver for Portfolio Optimization](sapo_improving_the_scalability_and_accuracy_of_quantum_linear_solver_for_portfolio_optimization.md) | 本文提出SAPO量子投资组合优化方案，基于HHL算法结合金融均值方差理论。设计约束等价缩放大幅降低拉格朗日矩阵条件数，构建SVR最小/最大特征值预测模型自适应配置量子电路。美股多资产数据集测试，相较基础HHL复杂度降低36.94%，精度相比混合HHL提升1.46倍。 |
| [基于QHD与QUBO建模的可扩展社区检测<br>Scalable Community Detection Using QHD and QUBO Formulation](scalable_community_detection_using_qhd_and_qubo_formulation.md) | 本文提出基于量子哈密顿下降(QHD)的分层社区检测算法，将图模块度优化转化为QUBO问题。设计粗化-求解-细化分层流程，依托GPU并行模拟量子隧穿跳出局部最优。多真实图测试，中等密度网络模块度最高提升5.49%，大规模场景相较GUROBI求解速度大幅领先。 |
| [混合量子神经网络中的计算优势：神话还是现实？<br>Computational Advantage in Hybrid Quantum Neural Networks: Myth or Reality?](computational_advantage_in_hybrid_quantum_neural_networks_myth_or_reality.md) | 本文探究混合量子神经网络(HQNN)是否具备计算优势，构建可控螺旋多特征数据集，以FLOPs、参数量双指标对比经典NN与两类HQNN。结果显示随问题复杂度提升，SEL型HQNN算力增幅仅53.1%、参量增幅81.4%，远低于经典网络，证明量子层具备天然计算可扩展性优势。 |
| [基于测量的量子模算术电路反计算方法<br>Measurement-based uncomputation of quantum circuits for modular arithmetic](measurement_based_uncomputation_of_quantum_circuits_for_modular_arithmetic.md) | 本文形式化基于测量的反计算(MBU)技术，面向量子模算术电路优化。对单比特垃圾辅助量子采用X基测量概率化反计算，大幅削减Toffoli门数量。应用于各类模加法电路，Toffoli门降低10%~25%，同时提出区间比较新电路并优化，可用于Shor算法、量子密码分析。 |
| [优化用于RSA2048量子攻击的窗口算术<br>Optimizing windowed arithmetic for quantum attacks against RSA2048](optimizing_windowed_arithmetic_for_quantum_attacks_against_rsa2048.md) | 本文面向Shor算法分解RSA-2048场景，提出四类窗口量子算术优化。采用延迟反计算、选择性查表、初始大窗口、分片窗口策略，查表反计算Toffoli门开销渐近减半。在GE分解框架验证，RSA门数降低1.5%~3.4%，运行时间缩短16%，仅增加12%物理量子比特。 |
| [分布式量子计算的软硬件协同设计<br>Hardware-Software Co-design for Distributed Quantum Computing](hardware_software_co_design_for_distributed_quantum_computing.md) | 本文面向分布式量子计算(DQC)提出软硬件协同架构，划分通信/缓存/数据三类量子比特，采用异步纠缠生成与远程门自适应调度。预存纠缠缓冲平滑资源供给，实时匹配EPR对供需。在TLIM、QAOA、QFT等基准验证，相较无缓冲基线电路深度大幅缩减，输出保真度提升2倍左右。 |
