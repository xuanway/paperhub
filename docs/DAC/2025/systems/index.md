# Systems · DAC 2025 (50)

本分类收录 DAC 2025（第62届）Track "Systems" 的论文题目。

## 系统1：自主系统（汽车、机器人、无人机）(6)

SYS1: Autonomous Systems (Automotive, Robotics, Drones) 

### 自主系统中的“自动” (6)

The ‘Auto’ in Autonomous Systems 

- Session Chairs: Abhinav Goel, Oliver Bringmann

> 本次会议展示了将"自动"融入自主系统的创新成果。议题涵盖实时激光雷达里程计、事件驱动传感、脑电控制假肢、安全控制器合成、变异测试以及高效计算的超参数调优。无论是提升机器人、信息物理系统还是人工智能驱动硬件的自主性，本场会议都将探讨塑造未来智能自持系统的前沿研究。

> This session showcases innovations that put the "auto" in autonomous systems. Topics include real-time LiDAR odometry, event-based sensing, EEG-controlled prosthetics, safe controller synthesis, mutation testing and hyperparameter tuning for efficient computing. Whether it's enhancing autonomy in robotics, cyber-physical systems, or AI-driven hardware, this session explores cutting-edge research shaping the future of intelligent, self-sustaining systems.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [LIO-DPC：基于动态位姿链的高精度快速激光雷达惯性里程计<br>LIO-DPC: Accurate and Fast LiDAR-Inertial Odometry with Dynamic Pose Chain](lio_dpc_accurate_and_fast_lidar_inertial_odometry_with_dynamic_pose_chain.md) | 本文提出LIO-DPC激光惯性里程计框架，设计动态位链解耦滤波与图优化，实现并行运算；设计环路稀疏化指标筛选高质量回环约束。在多公开数据集验证，定位RMSE远优于FAST-LIO2、LIO-SAM等SOTA，单帧耗时接近轻量化滤波方案，兼顾实时性与长期精度。|
| [Espresso：利用时空有序特性挖掘事件传感器的稀疏属性<br>Espresso: Exploiting the Sparsity Property in Event Sensors with Spatiotemporal Ordering](espresso_exploiting_the_sparsity_property_in_event_sensors_with_spatiotemporal_ordering.md) | 本文面向时空有序事件流提出Espresso事件视觉加速架构，设计N-Pending-FIFOs解决流顺序失配、移位哈希表削减访存延迟，组合为Event调度器实现稀疏事件流水线处理。Zynq FPGA部署Harris算子实测，最高吞吐量5000fps，比嵌入式GPU快5.1倍、传统行缓冲加速器提速3.3倍。|
| [CognitiveArm：依托具身机器学习实现脑电实时控制假肢机械臂<br>CognitiveArm: Enabling Real-Time EEG-Controlled Prosthetic Arm Using Embodied Machine Learning](cognitivearm_enabling_real_time_eeg_controlled_prosthetic_arm_using_embodied_machine_learning.md) | 本文提出CognitiveArm嵌入式脑控假肢系统，基于实境机器学习实现实时EEG运动想象分类。采用进化搜索获取帕累托最优模型，搭配剪枝/量化压缩，集成Whisper语音指令切换模式。搭载3自由度3D打印假肢，边缘端推理精度最高90.1%，单帧推理低至0.071s，低成本适配肢体残障人群。|
| [基于向量屏障证书、具备形式化保障的学习辅助型安全控制器综合方法<br>Learning-Aided Safe Controller Synthesis with Formal Guarantees via Vector Barrier Certificates](learning_aided_safe_controller_synthesis_with_formal_guarantees_via_vector_barrier_certificates.md) | 本文提出LASAC-VBC方法，融合强化学习、PAC近似与向量障碍证书(VBC)，面向安全关键非线性系统合成带形式化保障控制器。采用Skip多项式网络学习原始约束下VBC，搭配增量SOS后置验证，无需松弛约束丢失可行解。10组基准测试表明，相较SOSTOOLS单障碍证书，验证更快且高维系统可成功求解。|
| [面向商用信息物理系统开发工具链的实时区域变异测试<br>Live Region Mutation Testing for Commercial Cyber-Physical System Development Tool Chain](live_region_mutation_testing_for_commercial_cyber_physical_system_development_tool_chain.md) | 本文提出面向Simulink编译器的LION活区域变异差分测试框架，采用store-revert块对保证数据流等价，结合MCMC采样生成多样化模块序列。通过同源模型多仿真模式输出对比捕获编译缺陷。实验在R2018a、R2021b版本共检出11个缺陷，长期测试稳定版发现16个有效bug，其中12个全新漏洞，检出能力优于SLforge、SLEMI、COMBAT。|
| [MAS-ISP：面向图像信号处理硬件系统的无代理在线超参数优化框架<br>MAS-ISP: A Proxy-Free Online Hyperparameter Optimization Framework for ISP Hardware System](mas_isp_a_proxy_free_online_hyperparameter_optimization_framework_for_isp_hardware_system.md) | 本文提出无代理在线ISP超参优化硬件框架MAS-ISP，基于主从多智能体深度强化学习，无需可微代理模型，解决帧间抖动问题。设计条状卷积核与步感知双缓冲硬件降低CNN开销，FPGA/ASIC分别实现1080P@75/240FPS，图像质量与检测mAP优于代理类SOTA，硬件存储资源大幅削减。|



## SYS2：信息物理系统与物联网设计 (8)

SYS2: Design of Cyber-Physical Systems and IoT 

### 从模拟到威胁：深入探讨信息物理系统与物联网设计 (8)

From Simulation to Threats, a Deep-dive into CPS and IoT Design 

- Session Chairs: Stefano Di Carlo, Hokeun Kim

> 信息物理系统（CPS）与物联网（IoT）设备的设计是公认极具挑战性的工作。本次专题研讨将梳理设计流程中的核心环节，涵盖系统仿真、优化与管理。内容将涵盖多种目标硬件平台，类RISC-V架构至基于现场可编程门阵列（FPGA）的加速器均包含在内。此外，还将介绍先进的设计空间探索算法与任务调度算法，用以解决信息物理系统与物联网应用场景中关键且亟待攻克的核心问题，例如能耗优化与抗攻击可靠性。

> The design of Cyber-Physical Systems (CPS) and Internet of Things (IoT) devices is a well-known challenging process. This session explores key stages of the design flow, including system simulation, optimization, and management. A variety of target platforms, ranging from RISC-V-like architectures to FPGA-based accelerators, will be covered. Additionally, advanced design space exploration and task-scheduling algorithms will be presented to address fundamental and compelling aspects of CPS and IoT scenarios, such as energy awareness and robustness against attacks.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [面向软件定义无线接入网的众核基带收发机快速端到端仿真与探索<br>Fast End-to-End Simulation and Exploration of Many-Core Baseband Transceivers for Software-Defined Radio-Access Networks](fast_end_to_end_simulation_and_exploration_of_many_core_baseband_transceivers_for_software_defined_radio_access_networks.md) | 本文提出基于静态二进制翻译(SBT)的Banshee仿真框架，面向1024核RISC-V TeraPool软件无线电基带芯片，耦合无线信道模型实现端到端5G/6G MIMO MMSE仿真。相比RTL仿真提速千倍，多线程并行最高121倍加速；内置近似时序模型，周期预估平均误差30%，支持低精度算术架构空间快速探索。 |
| [小规模间歇系统：执行模型与设计指南<br>Intermittent Systems at Small Scale: Execution Model and Design Guidelines](intermittent_systems_at_small_scale_execution_model_and_design_guidelines.md) | 本文针对小电容无电池间歇IoT系统，提出含去耦电容缓冲效应的新型执行模型。传统模型忽略片内缓冲电容，能效预测最高偏差5.62倍、易产生不安全检查点；基于模型提出三类软硬件设计准则，静态/动态检查方案平均分别提速3.04倍、2.85倍。 |
| [MEEK：面向真实乱序超标量处理器的异构并行错误检测架构再思考<br>MEEK: Re-thinking Heterogeneous Parallel Error Detection Architecture for Real-World OoO Superscalar Processors](meek_re_thinking_heterogeneous_parallel_error_detection_architecture_for_real_world_ooo_superscalar_processors.md) | 本文提出MEEK异构并行故障检测全栈架构，基于高性能乱序大核+轻量有序小核协同校验。软硬件协同设计低侵入微架构、专用ISA与Linux轻量修改，解决前人仿真未发现的死锁、转发拥塞等瓶颈。28nm综合面积开销25.8%，故障平均检测时延小于1μ，性能远优于锁步、软件校验方案。 |
| [VersaSlot：通过大小槽与在线迁移实现高效细粒度FPGA共享<br>VersaSlot: Efficient Fine-grained FPGA Sharing with Big.Little Slots and Live Migration in FPGA Cluster](versaslot_efficient_fine_grained_fpga_sharing_with_big_little_slots_and_live_migration_in_fpga_cluster.md) | 本文提出VersaSlot时空复用FPGA集群共享系统，创新Big.Little异构槽架构解决DPR串行端口引发的重配阻塞问题。设计双核心调度、自适应槽分配算法，配套跨板低开销热迁移机制。基于ZCU216集群实测，相较SOTA平均响应提速2.19倍，LUT、FF资源利用率分别提升35%、29%。 |
| [功耗受限的印刷神经形态硬件训练<br>Power-Constrained Printed Neuromorphic Hardware Training](power_constrained_printed_neuromorphic_hardware_training.md) | 本文面向柔性印刷神经形态电路(pNC)严格功耗约束场景，提出增广拉格朗日训练框架。构建四类可学习激活函数的数据驱动代理功耗模型，单次训练即可生成帕累托最优功耗精度解集。在13个数据集验证，低功耗下精度功耗比较惩罚基线提升52~59倍，不同激活函数适配差异化功耗场景。 |
| [能量采集物联网数据聚合的信息年龄最小化<br>Age-of-Information Minimization for Data Aggregation in Energy-Harvesting IoTs](age_of_information_minimization_for_data_aggregation_in_energy_harvesting_iots.md) | 本文首次研究能量采集物联网聚合场景下信息年龄(AoI)最小化问题，提出离线AM-Agg调度算法+在线自适应调整双阶段方案。基于能量预测生成基础调度，能量波动时优先传输高价值子数据。仿真与TelosB实测表明，相比DEAS、AMID平均AoI降低75%~89%，在线调整可再缩减11.5%平均AoI。 |
| [基于共形预测的可穿戴物联网不确定性感知能量管理<br>Uncertainty-Aware Energy Management for Wearable IoT Devices with Conformal Prediction](uncertainty_aware_energy_management_for_wearable_iot_devices_with_conformal_prediction.md) | 本文面向可穿戴物联网能量收集随机性难题，提出基于多目标共形预测MTCP的感知能量管理框架。MTCP生成带理论覆盖率的多时段能量不确定区间，搭配蒙特卡洛采样+轻量神经网络逼近最优调度。真实穿戴数据集与硬件验证，决策与理论最优仅差2J，QoS较基线提升25%以上，整机开销极低。 |
| [面向信息物理系统的基于查询黑盒隐蔽传感器攻击<br>Query-Based Black-Box Stealthy Sensor Attacks on Cyber-Physical Systems](query_based_black_box_stealthy_sensor_attacks_on_cyber_physical_systems.md) | 本文面向无系统先验知识的CPS黑盒场景，提出基于查询的隐蔽传感器攻击框架。采用LSTM时序模型拟合残差检测器，结合主动学习生成攻击序列，训练阶段严控告警次数。在四类数值仿真与CARLA自动驾驶平台验证，相较随机搜索、学习基线，查询量大幅减少，可在不触发告警下使系统偏离至危险状态。 |



## SYS3: 嵌入式软件 (8)

SYS3: Embedded Software 

### 编程、调试、加速：软件创新 (8)

Program, Debug, Accelerate: Software Innovations 

- Session Chairs: Hoeseok Yang, Younghyun Kim

> 本场研讨会聚焦稀疏矩阵计算、嵌入式人工智能与系统优化领域的前沿进展。研讨议题涵盖：可提升稀疏矩阵运算效率的多模态框架与张量编译器、面向资源受限硬件、用于优化神经网络微调效果的端侧训练技术，以及依托人工智能提升系统安全性与可靠性的各类方案。此外，会议还将介绍创新存储优化方案与高效数据处理方法。此类软件创新将算法革新与硬件适配策略相结合，不断突破嵌入式计算在性能、适配性与安全层面的技术上限。

> This session explores advances in sparse matrix computation, embedded AI, and system optimization. Topics include multimodal frameworks and tensor compilers that enhance sparse matrix operations, on-device training techniques that optimize neural network fine-tuning on constrained hardware, and AI-driven approaches for improving system security and reliability. Additionally, novel storage optimizations and efficient data processing methods will be presented. By integrating algorithmic innovations with hardware-aware strategies, these software innovations push the boundaries of performance, adaptability, and security in embedded computing.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [SSpMV：多模态机器学习赋能的稀疏感知SpMV框架<br>SSpMV: A Sparsity-aware SpMV Framework Empowered by Multimodal Machine Learning](sspmv_a_sparsity_aware_spmv_framework_empowered_by_multimodal_machine_learning.md) | 本文提出面向多核平台的稀疏感知SpMV自适应框架SSpMV，设计多模态神经网络MM-Adapter。提取人工细粒度特征与局部/分布/向量化三类稀疏模态融合预测最优存储格式与超参，覆盖21种SpMV实现。6000+真实矩阵测试，预测精度81.05%，相较MKL平均加速3.08倍，适配x86/鲲鹏多架构。 |
| [输入感知且向量化加速的稀疏张量编译器<br>An Input-Aware Sparse Tensor Compiler Empowered by Vectorized Acceleration](an_input_aware_sparse_tensor_compiler_empowered_by_vectorized_acceleration.md) | 本文提出面向多核CPU的输入感知稀疏张量编译器SpMMTC，依据稀疏矩阵非零分布自适应分块，定制向量化FMA内核，配套专用稀疏存储与稠密打包布局。科学计算与剪枝深度学习矩阵测试，相较MKL、TVM等提速1.21~2.97倍；树莓派稀疏MobileNet推理最高加速1.52倍。 |
| [通过梯度凝缩与交替局部更新实现微型设备模型个性化<br>Enabling On-Tiny-Device Model Personalization via Gradient Condensing and Alternant Partial Update](enabling_on_tiny_device_model_personalization_via_gradient_condensing_and_alternant_partial_update.md) | 本文提出TinyMP端侧模型个性化协同优化框架，包含梯度压缩GC与交替局部更新APU两大核心模块。GC压缩梯度图降低反向传播算力与内存开销且误差有界；APU在线动态筛选关键卷积核交替更新。在OpenMV-H7微型MCU实测，最高提速2.4倍，内存节省80.8%，下游任务精度最高提升30.3%。 |
| [Rust新编程体验：以LLM快慢思考征服未定义行为<br>Unlocking a New Rust Programming Experience: Fast and Slow Thinking with LLMs to Conquer Undefined Behaviors](unlocking_a_new_rust_programming_experience_fast_and_slow_thinking_with_llms_to_conquer_undefined_behaviors.md) | 本文借鉴双过程认知理论，提出RustBrain大模型修复框架，分为快、慢双推理阶段。快推理提取代码特征批量生成修复方案；慢推理搭载多智能体完成分解、验证、抽象推理，配套自适应回滚与反馈自学习。基于Miri数据集测试，修复通过率94.3%、语义可用率80.4%，较SOTA提升30%，修复速度最高为人工专家18倍。 |
| [DroidFuzz：面向嵌入式安卓设备专有驱动的模糊测试<br>DroidFuzz: Proprietary Driver Fuzzing for Embedded Android Devices](droidfuzz_proprietary_driver_fuzzing_for_embedded_android_devices.md) | 本文提出DROIDFUZZ面向嵌入式安卓闭源厂商驱动模糊测试工具，设计HAL预探测、内核-用户关联载荷生成、跨层执行反馈三大核心模块，联合模糊HAL与内核驱动。在7款真实嵌入式设备实测，发现12个厂商确认全新漏洞，内核分支覆盖率相较Syzkaller平均提升17%。 |
| [STREAM：基于时空相似性的可调粒度高效近似中位数<br>STREAM: Spatiotemporal Similarity-based Efficient Approximate Median with Tunable Granularity](stream_spatiotemporal_similarity_based_efficient_approximate_median_with_tunable_granularity.md) | 本文提出STREAM近似中位数算法，挖掘流式数据时空相似性复用分桶结构，设计粗细粒度可调分桶机制。包含粗粒度STREAM-CG与高精度细粒度STREAM-FG两条分支，9类真实/合成数据集测试，精度接近主流算法前提下，平均分别比DDSketch、KLL快4.7倍、10.1倍，最高提速10倍、71.2倍。 |
| [面向交错磁记录的数据去重辅助重定位<br>Enabling Data-Deduplication-Assisted Data Relocation for Interlaced Magnetic Recording](enabling_data_deduplication_assisted_data_relocation_for_interlaced_magnetic_recording.md) | 本文面向交错磁记录(IMR)硬盘提出DADR去重辅助数据重定位方案，利用重复数据引用计数区分静态/可更新数据，结合三阶段Z-Alloc分配机制设计双向轨道交换、主动重分配等模块。仿真测试相较主流Tracklace方案，轨道重写量平均降低41.34%，累计读写延迟减少37.57%。 |
| [位置是关键：利用LLM进行Verilog功能缺陷定位<br>Location is Key: Leveraging LLM for Functional Bug Localization in Verilog Design](location_is_key_leveraging_llm_for_functional_bug_localization_in_verilog_design.md) | 本文基于Deepseek-Coder-16B提出LiK专用大模型，面向Verilog功能故障精准定位。采用持续预训练、监督微调、SimPO强化学习三阶段训练，无需Testbench等EDA验证工具。测试pass@1达93.33%，超越Strider、GPT-o1、Claude3.5；嵌入MEIC修复框架后漏洞修复成功率由76.47%提升至90.54%。 |


## SYS4：嵌入式系统设计工具与方法论 (8)

SYS4: Embedded System Design Tools and Methodologies

### 更快、更安全、更环保：智能边缘的AI驱动进化 (8)

Faster, Safer, Greener: AI-driven Evolution in Smart Edge

- Session Chairs: Peipei Zhou, Pi-Cheng Hsiu

> 本场论坛探讨由人工智能驱动、从加速性能、运行可靠性与绿色可持续性三大维度重塑边缘智能的各类创新技术。内容首先围绕性能加速展开，涵盖三维点云检测加速、无需边缘算力支撑的图像压缩，以及多模型去中心化联邦学习；随后通过Linux运行时完整性度量、自动化硬件验证、带后实现流程的高层次综合技术，阐述系统可靠性增强方案；最后介绍能效预测、架构级功耗建模两大技术，实现系统绿色可持续优化。上述创新技术将驱动新一代智能边缘计算的发展。

> This session explores AI-driven innovations shaping edge intelligence in acceleration, reliability, and sustainability. It begins with acceleration in 3D point cloud detection, edge-compute-free image compression, and multi-model decentralized federated learning. Reliability is then reinforced with Linux runtime integrity measurement, automated hardware verification, and high-level synthesis with post-implementation. It concludes with sustainability through energy-efficient forecasting and architecture-level power modeling. These innovations drive the next generation of smart edge computing.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [DAWN：通过对象感知分区与三维相似过滤加速点云目标检测<br>DAWN: Accelerating Point Cloud Object Detection via Object-Aware Partitioning and 3D Similarity-Based Filtering](dawn_accelerating_point_cloud_object_detection_via_object_aware_partitioning_and_3d_similarity_based_filtering.md) | 本文提出DAWN点云检测加速框架，利用帧间局部相似性过滤冗余点。设计目标感知分块避免物体割裂，搭配轴排序点采样均衡分区粒度，基于并行豪斯多夫距离实现3D相似度快速判别。在主流检测网络平均提速1.59倍，最高1.70倍，平均过滤超50%点，精度损失可忽略。 |
| [Easz：面向资源受限物联网的敏捷Transformer图像压缩框架<br>Easz: An Agile Transformer-based Image Compression Framework for Resource-constrained IoTs](easz_an_agile_transformer_based_image_compression_framework_for_resource_constrained_iots.md) | 本文提出面向资源受限IoT的非对称Transformer图像压缩框架Easz，将计算负载转移至服务端。边缘端设计条件均匀擦除压缩算法，服务端采用两级分块轻量化Transformer重建。可灵活调节压缩率，Jetson TX2实测功耗、内存大幅降低，重建PSNR优于超分方案，兼容JPEG/BPG等传统编码器。 |
| [MMDFL：面向资源受限AIoT的多模型去中心化联邦学习<br>MMDFL: Multi-Model-based Decentralized Federated Learning for Resource-Constrained AIoT Systems](mmdfl_multi_model_based_decentralized_federated_learning_for_resource_constrained_aiot_systems.md) | 本文提出MMDFL多模型去中心化联邦学习框架，面向算力带宽受限AIoT设备。引入漫游模型逐设备遍历训练，设计融合数据、资源、遗忘因子的自适应邻居选择策略。仿真与真实嵌入式集群验证，相较主流DFL算法，通信开销大幅下降，IID/非IID场景分类精度、收敛速度均更优。 |
| [LightRIM：嵌入式Linux内核轻量运行时完整性度量<br>LightRIM: Light Runtime Integrity Measurement for Linux Kernels in Embedded Applications](lightrim_light_runtime_integrity_measurement_for_linux_kernels_in_embedded_applications.md) | 本文面向资源受限嵌入式Linux设备提出轻量级运行时完整性检测框架LightRIM。基于攻击特征提取核心监测对象，设计两级哈希压缩基线库，结合事件触发动态安全值机制；采用模拟退火随机化检测间隔抵御TOCTOU漏洞。测试系统开销低于0.7%，可有效检测代码注入、Rootkit两类主流内核攻击。 |
| [UVLLM：使用大语言模型的自动化通用RTL验证框架<br>UVLLM: An Automated Universal RTL Verification Framework using LLMs](uvllm_an_automated_universal_rtl_verification_framework_using_llms.md) | 本文提出UVLLM通用RTL自动化验证框架，融合LLM与工业UVM验证体系，构建四阶段流水线：预处理、UVM仿真、日志后处理、智能修复。设计动态错误定位、版本回滚、结构化补丁输出机制。自建331条真实RTL错误数据集，语法修复率86.99%、功能修复率71.92%，相较SOTA平均提速10.42倍。 |
| [结合HLS优化指令的实现后性能预测方法<br>A Post-Implementation Performance Prediction Method with HLS Optimization Directives](a_post_implementation_performance_prediction_method_with_hls_optimization_directives.md) | 本文面向HLS指令优化场景提出实现后性能预测方法，设计Graph Builder构建融合优化指令、硬件资源复用关系的专用图。基于TransformerConv图卷积+聚合池搭建预测模型，预测LUT/FF/CP/功耗/DSP五项指标，误差降至3.87%~8.08%，在未见过内核上泛化能力显著优于现有SOTA。 |
| [面向现代异构处理器的争用感知序列能效预测<br>Contention-Aware Forecasting of Energy Efficiency through Sequence-Based Models in Modern Heterogeneous Processors](contention_aware_forecasting_of_energy_efficiency_through_sequence_based_models_in_modern_heterogeneous_processors.md) | 本文提出EffiCast序列预测框架，面向Intel混合异构处理器实现感知资源竞争的能效预测。通过实测分析程序阶段、簇内/簇间竞争对IPJ能效的影响，构建分层时序特征，采用LSTM与Transformer时序模型。真实平台批量推理仅1.82ms，预测RMSE低至1.14，显著优于XGB、浅层神经网络基线。 |
| [AutoPower：通过功耗组解耦实现自动化少样本架构级功耗建模<br>AutoPower: Automated Few-Shot Architecture-Level Power Modeling by Power Group Decoupling](autopower_automated_few_shot_architecture_level_power_modeling_by_power_group_decoupling.md) | 本文提出AutoPower少样本架构级功耗建模框架，基于功耗组解耦思想，分时钟、SRAM、逻辑三大模块独立建模，各模块内部进一步拆分子模型。仅需2组CPU配置训练，预测MAPE低至4.36%、R²达0.96，相比McPAT-Calib误差降低5%，支持细粒度时序功耗曲线预测。 |



## SYS5：嵌入式内存与存储系统 (12)

SYS5: Embedded Memory and Storage Systems

### 利用内存层次结构应对新兴应用与硬件 (6)

Leveraging the Memory Hierarchy for Emerging Applications and Hardware

- Session Chairs: Chun-Feng Wu, Yi Wang

> 本次会议围绕面向数据密集型应用的存储器层次结构管理创新展开探讨，内容涵盖内存计算技术、面向新兴神经网络处理器与图形处理器的缓存管理、多主机间分离式内存的应用方案，以及如何提升内存系统鲁棒性。目前，业界在缩小新型计算架构与内存之间的性能差距方面已取得显著进展。

> This session discusses innovations in memory hierarchy management for data-intensive applications. It explores the use of In-Memory computing, cache management for emerging neural and graphical processors, the use of disaggregated memory across several hosts, and how to make memory robust. Great progress has been shown toward reducing the performance gap between novel computing architectures and memory.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [MIRACLE：结合存内处理与内容寻址存储的多模态信息检索方法<br>MIRACLE: Multimodal Information Retrieval via a Combined In-Memory Processing and Content Addressable Memory Approach](miracle_multimodal_information_retrieval_via_a_combined_in_memory_processing_and_content_addressable_memory_approach.md) | 本文提出MIRACLE混合架构，融合STT-MRAM存内计算(PIM)与内容寻址存储器(CAM)实现多模态检索。利用器件固有随机性实现三元LSH哈希，分段CAM粗筛后余弦精排。在MSCOCO等数据集验证，检索精度与CPU基线持平，延迟降低9.45倍、能耗减少30.2倍。 |
| [REMU：面向在轨深度学习系统的双寻址内存感知辐射仿真<br>REMU: Memory-aware Radiation Emulation via Dual Addressing for In-orbit Deep Learning System](remu_memory_aware_radiation_emulation_via_dual_addressing_for_in_orbit_deep_learning_system.md) | 本文面向星载COTS GPU深度学习场景，提出REMU内存感知辐射仿真器。设计双寻址+位图树架构打通DRAM硬件故障与运行时DNN映射，精准模拟SEU/MCU空间相关比特翻转。在10类卫星DNN、两类遥感任务验证，注入开销由百倍降至3倍，揭示轻量化模型更脆弱、MCU不能等效多SEU等辐射容错规律。 |
| [HIVE：用于加速GPU内存访问的高优先级受害者缓存<br>HIVE: A High-Priority Victim Cache for Accelerating GPU Memory Accesses](hive_a_high_priority_victim_cache_for_accelerating_gpu_memory_accesses.md) | 本文提出HIVE高优先级受害者缓存架构，改变传统后置缓存逻辑，访存请求优先查询受害者缓存再访问L1D。复用空闲寄存器做缓存数据区，搭配BDI压缩与新型替换策略。仿真显示相较基线IPC提升77.1%，对比SOTA Linebacker提升21.7%，片上硬件开销仅3.1%。 |
| [NVR：面向稀疏访存的NPU向量前瞻机制<br>NVR: Vector Runahead on NPUs for Sparse Memory Access](nvr_vector_runahead_on_npus_for_sparse_memory_access.md) | 本文提出NVR面向稀疏DNN NPU的向量前瞻预取硬件机制，采用非侵入解耦架构，复用NPU空闲稀疏单元做前瞻地址推演，配套NSB小缓存。硬件面积开销低于5%，相比主流预取方案缓存缺失平均降低90%，稀疏负载整体加速4倍，同等芯片面积下NS扩容收益远高于L2扩容。 |
| [自由扩展逻辑空间：面向压缩SSD的内存高效映射表设计<br>Expanding Logical Space Freely: A Memory-efficient Mapping Table Design for Compressional SSDs](expanding_logical_space_freely_a_memory_efficient_mapping_table_design_for_compressional_ssds.md) | 本文面向内置压缩SSD提出N-to-1高效L2P映射FTL架构，利用同压缩率连续逻辑页合并映射条目消除PPN冗余，设计升降级机制适配动态压缩比，配套分块分配、复用回收与压缩感知GC。MQsim仿真显示映射表内存平均缩减50%，缓存命中率提升，IO延迟相较DFL基准最高提速2.06倍。 |
| [Sphinx：面向解耦内存并带精简过滤缓存的高性能混合索引<br>Sphinx: A High-Performance Hybrid Index for Disaggregated Memory with Succinct Filter Cache](sphinx_a_high_performance_hybrid_index_for_disaggregated_memory_with_succinct_filter_cache.md) | 本文面向RDMA解耦内存(DM)提出混合索引Sphinx，适配变长键ART结构。内存节点部署内层哈希表打破串行遍历依赖，计算端引入布谷过滤器精简缓存，规避一致性问题。YCS测试下最高性能达SOTA方案7.3倍，内存节点额外开销仅3.3%~4.9，计算端缓存占用极低。 |


### 抽象存储层与否 (6)

To Abstract or Not to Abstract the Storage Layer

- Session Chairs: Nima TaheriNejad, Jalil Boukhobza

> 一方面，多项研究力求在保留完善抽象层、减轻应用开发人员负担的前提下，对存储设备进行透明化优化；另一方面，另有部分研究倾向下放更多管控权限，以充分发挥闪存技术所具备的高性能优势，但此举会打破传统抽象层，同时大幅提升系统复杂度。本次专题研讨将围绕分区命名空间设备、计算存储、叠瓦式磁记录等新型存储技术，探讨抽象层级两种不同思路下的创新设计方案。

> While several studies seek to transparently optimize the storage devices by keeping a strong abstraction thus relieving application designers, others tend to give more control to take full advantage of the high performance promised by flash memory technology, thus breaking the traditional abstraction layer at the cost of more complexity. This session explores novel designs on both sides of abstraction level for novel technologies such as zoned namespace devices, computational storage, and Shingled magnetic recording.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [SuperCopyback：重访现代NAND SSD中的回拷机制<br>SuperCopyback: Revisiting Copyback on Modern NAND Flash-based SSDs](supercopyback_revisiting_copyback_on_modern_nand_flash_based_ssds.md) | 本文提出SuperCopyback，解决现代子页、超页、RAIN架构下传统Copyback失效问题。设计轻量硬件MROW实现子页级拷贝回收，配套协同GC调度与重布局RAIN机制。MQSim仿真显示，相较标准GC平均吞吐量提升26.3%，99分位尾延迟降低28.4%，性能接近1ns理想数据迁移场景。 |
| [云端弹性SSD的隐性契约<br>The Unwritten Contract of Cloud-based Elastic Solid-State Drives](the_unwritten_contract_of_cloud_based_elastic_solid_state_drives.md) | 本文针对AWS、阿里云两款主流云ESSD开展全面性能表征，提出云弹性SSD隐性性能契约，总结4条反常识观测与5条工程启示。实验对比本地SSD发现ESSD存在时延、GC、读写模式、带宽四大差异化特征，给出云存储软件重构优化方向，并开源评测工具。 |
| [MiniWear：通过混合持久缓存最小化闪存磨损并延长EF-SMR寿命<br>MiniWear: Minimizing Flash Wear via Hybrid Persistent Cache for Extended EF-SMR Lifetime](miniwear_minimizing_flash_wear_via_hybrid_persistent_cache_for_extended_ef_smr_lifetime.md) | 本文面向嵌入式闪存+SMR混合存储(EF-SMR)闪存磨损严重、寿命短问题，提出MiniWear混合持久缓存协同方案。划分Flash-PC与SMR-PC两级缓存，配套细粒度回收与主动均衡调度。多负载测试最高降低闪存擦除66.67%，同时削减写放大、降低IO响应延迟，兼顾寿命与读写性能。 |
| [Leopard：基于队列并发的硬件直通远程存储访问（面向边缘智能工作站）<br>Leopard: Hardware Pass-Through Remote Storage Access with Queue Concurrency for Edge Intelligent Workstations](leopard_hardware_pass_through_remote_storage_access_with_queue_concurrency_for_edge_intelligent_workstations.md) | 本文面向算力存储受限边缘智能工作站，提出基于FPGA SmartNIC的Leopard硬件直通远程存储框架。自定义NVMe控制器消除主机远程软件栈，多队列并行流水线硬件加速器卸载全链路IO处理。真实负载下延迟较主流方案低1.09~6.04倍，CPU开销大幅降低，远程性能接近本地NVMe。 |
| [FineRR-ZNS：面向ZNS SSD的细粒度读刷新机制<br>FineRR-ZNS: Enabling Fine-Granularity Read Refreshing for ZNS SSDs](finerr_zns_enabling_fine_granularity_read_refreshing_for_zns_ssds.md) | 本文提出FineRR-ZNS细粒度读刷新机制，适配ZNS SSD架构。设计区重映射、区重构两大核心模块，仅对达到读取阈值闪存块执行刷新，规避整区迁移大量有效数据。FEMU仿真基于RocksDB多负载验证，相较基准ZoneRR-ZNS，数据迁移量平均降41.8%、擦除次数减少36.4%、IO吞吐量提升28.2%。 |
| [StreamCSD：通过存储内内容学习实现主机透明SSD流管理<br>StreamCSD: Host-Transparent SSD Stream Management via In-Storage Content Learning](streamcsd_host_transparent_ssd_stream_management_via_in_storage_content_learning.md) | 本文提出StreamCSD面向计算型SSD实现无主机参与自主流管理。以压缩率/香农熵为数据特征，轻量化流式K-means完成内容聚类，搭配GC重映射、生命周期二级映射优化混合寿命页面。仿真与PCIe5硬件实测，多模态AI负载下写放大由1.7降至1.06，吞吐量最高提升74%，无需修改主机系统。 |



## SYS6：时间关键与容错系统设计 (8)

SYS6: Time-Critical and Fault-Tolerant System Design

### 准时无误，经久耐用：关键系统设计的新前沿 (8)

Right on Time, Built to Last: New Frontiers in Critical System Design

- Session Chairs: Jiaqi Gu, Antonino Tumeo

> 随着系统复杂度不断提升，保障实时性能与容错能力兼备，对系统可靠性和运行效率而言至关重要。本次专题分享聚焦前沿研究，围绕故障恢复、实时处理以及高效内存利用展开探讨。研讨主题涵盖面向CXL内存的高级纠错码、大模型推理中的统计容错技术，以及无服务器工作流的自动化资源配置。其他重点内容包括时间感知流量整形（兆比特至千比特换算）、自主系统的有向无环图建模、内存故障预测管理、通用图形处理器图处理的故障注入，以及实时多核系统的灵活差错检测。欢迎参与本次分享，一同探究高可靠实时系统设计领域的最新研究成果。

> As systems grow more complex, ensuring both time-critical performance and fault tolerance becomes essential for reliability and efficiency. This session showcases cutting-edge research tackling fault resilience, real-time processing, and efficient memory utilization. Topics include advanced ECC for CXL memory, statistical fault tolerance in LLM inference, and automated resource configuration for serverless workflows. Additional highlights cover time-aware traffic shaping (Megabits to Kilobits), DAG modeling for autonomous systems, predictive memory failure management, fault injection for GPGPU graph processing, and flexible error detection in real-time multi-core systems. Join us to explore the latest breakthroughs in resilient, real-time system design.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [MemSeer：利用故障差异与多粒度预测的超大规模异构x86/ARM集群内存故障预测<br>MemSeer: Leveraging Memory Failure Distinctions and Multi-Grained Prediction in Ultra-Scale Heterogeneous X86/ARM Clusters](memseer_leveraging_memory_failure_distinctions_and_multi_grained_prediction_in_ultra_scale_heterogeneous_x86_arm_clusters.md) | 本文基于超大规模x86/ARM异构集群真实内存故障日志，提出MemSeer多粒度内存故障预测框架。区分两类架构故障时空差异，分层实现DIMM、服务器、页/行三级预测，设计四类特征与规则融合预测器。实测F1相较SOTA提升17.3%，线上集群VM中断平均降低24.2%。 |
| [CXL-ECC：基于LRC的高效CXL内存扩展控制器端ECC，提升DRAM纠错可靠性与性能<br>CXL-ECC: an Efficient LRC-based on-CXL-Memory-eXpander-Controller ECC to Enhance Reliability and Performance of DRAM Error Correction](cxl_ecc_an_efficient_lrc_based_on_cxl_memory_expander_controller_ecc_to_enhance_reliability_and_performance_of_dram_error_correction.md) | 本文提出CXL-ECC，在CXL内存扩展控制器MXC内置基于LRC的跨通道ECC。将奇偶校验计算卸载至MX内部，消除CXL链路额外带宽开销；LRC兼顾局部/全局纠错，支持多随机故障与通道失效。仿真显示相比主流方案可靠性提升109倍，链路带宽开销降至3.4%，系统性能提升12%。 |
| [从兆比特到千比特：面向TSN的内存高效时间感知整形<br>Megabits Down to Kilobits: Memory-Efficient Time-Aware Shaping for TSN](megabits_down_to_kilobits_memory_efficient_time_aware_shaping_for_tsn.md) | 本文面向TSN标准TAS时间感知整形器内存爆炸问题，提出METAS内存高效架构。摒弃传统逐帧存储门控表，采用每流持久规则+帧临时规则动态生成方案，搭配PIFO硬件队列。FPGA实测支持1024流时内存从14.34Mbits降至288Kbits，仅小幅增加逻辑，时延抖动维持微/纳秒级实时性能。 |
| [AARC：面向无服务工作流的亲和感知自动资源配置<br>AARC: Automated Affinity-aware Resource Configuration for Serverless Workflows](aarc_automated_affinity_aware_resource_configuration_for_serverless_workflows.md) | 本文提出AARC亲和感知无服务工作流自动资源配置框架，解耦CPU与内存分配。由图调度器提取DAG关键路径，优先级配置器分层寻优，严格满足端到端SLO。在三类典型工作流测试，相较贝叶斯优化、MAFF梯度下降，搜索耗时降低85.8%~89.6%，运行成本削减49.6%~61.7%。 |
| [FlexStep：实现多/众核实时系统的灵活错误检测<br>FlexStep: Enabling Flexible Error Detection in Multi/Many-core Real-time Systems](flexstep_enabling_flexible_error_detection_in_multi_many_core_real_time_systems.md) | 本文提出软硬件协同FlexStep多众核实时容错框架，突破LockStep/HMR核绑定、同步校验局限。新增寄存器检查点等微架构单元，配套定制ISA与分区EDF调度，支持异步、可抢占、按需选择性校验。FPGA实测性能减速仅1.07%，面积/功耗开销分别为2.21%、2.89%，任务可调度性大幅优于传统方案。 |
| [GraphFI：面向GPGPU图处理的高效故障注入框架<br>GraphFI: An Efficient Fault Injection Framework for Graph Processing on GPGPUs](graphfi_an_efficient_fault_injection_framework_for_graph_processing_on_gpgpus.md) | 本文面向GPU图处理提出GraphFI分层故障注入框架，挖掘图迭代、拓扑、算法三层故障相似与单调特性，设计ID/TD/MD三级剪枝策略逐层压缩故障空间。在SSSP、PageRank等四类图算法验证，故障空间平均压缩至原5%，相较主流工具提速2.1~15.2倍，可靠性评估误差仅1%左右。 |
| [自主系统DAG模型构建方法<br>Construction of DAG Models for Autonomous Systems](construction_of_dag_models_for_autonomous_systems.md) | 本文面向自动驾驶、无人机等自主系统多周期时触发任务链，提出全新DAG构建与DRM化简方法。借助克罗内克积生成超周期完整任务依赖图，基于平均等待时间删减冗余边，复杂度降至O(n²)。在HEFT、PEFT调度下，端到端平均响应时间较Floyd优化方案降低约9.6%，适配动态任务场景。 |
| [ReaLM：基于统计算法容错的可靠高效大语言模型推理<br>ReaLM: Reliable and Efficient Large Language Model Inference with Statistical Algorithm-Based Fault Tolerance](realm_reliable_and_efficient_large_language_model_inference_with_statistical_algorithm_based_fault_tolerance.md) | 本文提出软硬件协同容错框架ReaLM，面向 systolic阵列LLM加速器。先大规模故障注入量化LLM固有容错特性，区分敏感/弹性计算单元；设计统计型ABFT机制，仅对临界误差触发重计算。14nm综合面积开销1.42%、功耗1.79%，最低电压场景困惑度退化从18.54降至0.29，最高节能35.83%。 |
