# AI · DAC 2025 (102)

本分类收录 DAC 2025（第62届）Track "AI" 的论文。


## AI1：人工智能/机器学习算法 (24)

AI1: AI/ML Algorithms

### 图与拓扑：人工智能建模的全新前沿领域 (6)

Graphs & Topology: The New Frontier in AI Modeling

- Session Chairs: Yiting Liu, Sercan Aygun

> 本次研讨会探讨基于图与拓扑模型在机器学习应用中的使用。内容涵盖可扩展图神经网络相关论文、基于图的分析在电路稳定性中的应用，以及用于版图图案检测的创新拓扑表示方法。这些论文拓展了利用图模型解决机器学习领域复杂现实问题的研究边界。

> This session explores the use of graph-based and topological models in machine learning applications. It includes papers on scalable graph neural networks, the application of graph-based analysis for circuit stability, and innovative topology representation for layout pattern detection. These papers push the boundaries of leveraging graph-based models for complex real-world problems in machine learning.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [面向量子机器学习动态误差的鲁棒训练<br>Towards Training Robustness Against Dynamic Errors in Quantum Machine Learning](towards_training_robustness_against_dynamic_errors_in_quantum_machine_learning.md) | 本文针对NISQ设备量子噪声时变、各量子比特误差差异大的问题，提出误差无关均衡感知训练方案。采用进化低复杂度搜索定位致命误差，构建兼顾干净样本与最坏致命损失的联合优化目标。在图像分类、词性标注、回归多任务验证，致命精度大幅领先噪声注入基线，各类动态噪声下精度与SOTA噪声感知训练持平。 |
| [CirSTAG：基于图流形的电路稳定性分析<br>CirSTAG: Circuit Stability Analysis on Graph-based Manifolds](cirstag_circuit_stability_analysis_on_graph_based_manifolds.md) | 本文提出CirSTAG谱分析框架，面向EDA电路GNN实现节点/边稳定性量化。基于流形距离映射失真DMD指标，结合谱嵌入与PGM概率图构建高低维输入输出流，推导等价局部Lipschitz稳定分数。时序预测、电路逆向两大电路任务验证，近线性复杂度，可精准定位工艺/拓扑扰动敏感关键电路单元。 |
| [ParGNN：多GPU可扩展图神经网络训练框架<br>ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs](pargnn_a_scalable_graph_neural_network_training_framework_on_multi_gpus.md) | 本文提出多GPU全批量GNN训练框架ParGNN，设计PGALB两级图超划分算法缓解负载失衡，搭配子流水线SP重叠计算与通信。在4类大图数据集测试，相较DGL最高提速21.8倍、相较PipeGCN最高提速2.7倍，收敛精度无损，达到目标精度耗时最短。 |
| [深入版图图案拓扑表征：用于热点检测的新型对比学习框架<br>Delving into Topology Representation for Layout Pattern: A Novel Contrastive Learning Framework for Hotspot Detection](delving_into_topology_representation_for_layout_pattern_a_novel_contrastive_learning_framework_for_hotspot_detection.md) | 本文提出CLI-HD对比学习版图热点检测框架，设计Layout2Seq多边形序列化编码提取几何特征，搭配APE绝对位置嵌入表征拓扑关系。联合图像、序列双编码器做跨模态对比对齐，摒弃全局单一分类边界。ICCAD多基准测试，精度提升0.82%~4.77%，虚警率降低4.9%~23.18%，微调后推理速度达200FPS。 |
| [SuperFast：利用初始知识的快速超网训练<br>SuperFast: Fast Supernet Training using Initial Knowledge](superfast_fast_supernet_training_using_initial_knowledge.md) | 本文提出即插即用SuperFast超网训练方案，核心为先预训练中等规模子网，再通过参数上缩放向完整超网分发先验知识。区别于预训练最大子网的低效思路，在ElasticViT、NASViT两大ViT超网验证，达成同等精度训练速度分别提升1.4×、1.8×，同等训练时长下移动端子网最高提升4个百分点准确率。 |
| [LA-MTL：时延感知的自动化多任务学习<br>LA-MTL: Latency-Aware Automated Multi-Task Learning](la_mtl_latency_aware_automated_multi_task_learning.md) | 本文提出LA-MTL时延感知多任务学习自动搜索框架，设计ALF解析时延代理指标，构建兼顾时延、参数量、任务精度联合损失，配套分层梯度冲突消解策略。支持ResNet/MobileNet/MobileOne多种骨干，在Jetson Orin平台最高降低50%推理时延，参数量压缩超20个百分点，分割/深度估计精度仅浮动±2个百分点。 |


### 大语言模型优化：速度、规模与智能能力 (6)

Optimizing Large Language Models: Speed, Size, and Smarts

- Session Chairs: You Li, Biresh Joardar

> 本场专题聚焦大语言模型（LLMs）推理与通信效率优化领域的各项前沿技术进展。相关论文探讨了模型剪枝、量化、自适应稀疏梯度压缩等优化策略，同时介绍了降低通信开销、提升推理速度的各类实现方案。上述技术能够解决长上下文处理、多模态推理以及芯片级优化层面的诸多难题，对大语言模型落地规模化实际应用起到至关重要的作用。

> This session highlights advancements in optimizing large language models (LLMs) for more efficient inference and communication. The papers cover strategies such as pruning, quantization, and adaptive sparse gradient compression, along with methods to reduce communication costs and improve inference speed. These techniques address challenges in long-context processing, multi-modal inference, and chip-level optimizations, all crucial for scaling LLMs in real-world applications.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Grasp：基于分组的激活稀疏性预测，用于快速LLM推理<br>Grasp: Group-based Prediction of Activation Sparsity for Fast LLM Inference](grasp_group_based_prediction_of_activation_sparsity_for_fast_llm_inference.md) | 本文提出Grasp无训练式激活稀疏预测方法，面向ReLU改造型LLM，在符号比特基础上引入幅值分组与离群点校正。通过正态分布分块加权近似内积，平衡预测精确率与召回率。在Jetson Orin部署ProSparse-Llama7B/13B，相比SparseInfer跳过效率提升11倍，稠密推理加速至1.85倍，精度损失小于1%。 |
| [DuQTTA：解耦幅值与方向的双重量化张量列车适配，用于高效LLM微调<br>DuQTTA: Dual Quantized Tensor-Train Adaptation with Decoupling Magnitude-Direction for Efficient Fine-Tuning of LLMs](duqtta_dual_quantized_tensor_train_adaptation_with_decoupling_magnitude_direction_for_efficient_fine_tuning_of_llms.md) | 本文提出DuQTTA轻量化大模型微调框架，融合张量列车TT分解、双量化DQ、自适应优化AOS与幅值-方向解耦更新。通过TT极大缩减可训练参数量，两级8bit量化降低存储计算，解耦机制解决LoRA幅值方向耦合缺陷。LLaMA系列测试相较LoRA精度提升最高4.44倍，压缩倍率达65倍，适配边缘设备微调部署。 |
| [PacTrain：用于分布式深度学习高效集合通信的剪枝与自适应稀疏梯度压缩<br>PacTrain: Pruning and Adaptive Sparse Gradient Compression for Efficient Collective Communication in Distributed Deep Learning](pactrain_pruning_and_adaptive_sparse_gradient_compression_for_efficient_collective_communication_in_distributed_deep_learning.md) | 本文提出PacTrain分布式训练框架，融合模型剪枝与自适应稀疏梯度压缩。设计梯度稀疏约束GSE与掩码追踪器，各工作器共享全局稀疏掩码，兼容AllReduce原语；搭配三元梯度量化进一步压缩。在带宽受限场景下，相较主流压缩方案训练吞吐提升1.25~8.72倍，最高提速8.72倍，精度损失可控。 |
| [MILLION：通过免疫离群值的KV乘积量化掌控长上下文LLM推理<br>MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization](million_mastering_long_context_llm_inference_via_outlier_immunized_kv_product_quantization.md) | 本文提出MILLION面向长上下文LLM的KV乘积量化推理框架，基于PQ乘积量化天然适配KV通道异常值，规避传统量化解码开销；设计异步量化CUDA流与重构注意力内核，无需单独存储离群样本。在32K上下文下端到端提速2.09倍，4bit量化困惑度损失极小，解决长文本KV缓存内存瓶颈。 |
| [AASD：通过对齐多模态大语言模型中的投机解码实现推理加速<br>AASD: Accelerate Inference by Aligning Speculative Decoding in Multimodal Large Language Models](aasd_accelerate_inference_by_aligning_speculative_decoding_in_multimodal_large_language_models.md) | 本文提出AASD多模态投机解码加速框架，复用目标模型KV缓存并设计KV投影器压缩视觉特征，配套Target-Draft对齐注意力消除训练推理鸿沟。基于LLaVA-7B/13B在多模态任务验证，token接受率达0.62，推理最高提速2倍，无精度损失，轻量易部署。 |
| [ChipAlign：通过测地线插值实现面向芯片设计的大语言模型指令对齐<br>ChipAlign: Instruction Alignment in Large Language Models for Chip Design via Geodesic Interpolation](chipalign_instruction_alignment_in_large_language_models_for_chip_design_via_geodesic_interpolation.md) | 本文提出ChipAlign无训练模型融合方法，基于黎曼流形测地线插值融合芯片专用LLM与通用指令对齐LLM。仅单超参λ，线性计算复杂度，无需额外微调。评测显示在IFEval指令指标较ChipNeMo提升26.6%，OpenROAD、工业芯片QA分别提升3.9%、8.25%，同时完整保留芯片领域专业知识。 |


### 智能系统：人工智能硬件效能的未来 (6)

Smarter Systems: The Future of Hardware Efficiency in AI

- Session Chairs: Chenhui Deng, Liu Cheng

> 本场会议聚焦于提升机器学习系统的内存与硬件运行效率。本次宣讲的论文涵盖硬件组件、内存占用的各类优化方案，同时介绍将量化与剪枝技术应用于神经网络及推荐系统的创新策略，以此降低计算成本与功耗。

> This session focuses on improving the efficiency of memory and hardware in machine learning systems. Papers presented here cover methods for optimizing hardware components and memory usage, as well as innovative strategies for applying quantization and pruning techniques to neural networks and recommendation systems, to reduce computational costs and power consumption.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [面向Verilog的投机解码：速度与质量兼得<br>Speculative Decoding for Verilog: Speed and Quality, All in One](speculative_decoding_for_verilog_speed_and_quality_all_in_one.md) | 本文面向Verilog RTL生成提出语法感知推测解码方案，基于AST提取语法关键token并引入[FRAG]分隔符构建专用训练标签，改造多头Medusa架构。在CodeLlama/CodeT5p验证，生成速度最高提速5.05倍，RTLLM基准pass@10指标提升17.19%，同时兼顾生成速度与代码语法、功能正确性。 |
| [PARO：面向视频生成模型的模式感知重排序注意力量化软硬件协同设计<br>PARO: Hardware-software Co-design with Pattern-aware Reorder-based Attention Quantization in Video Generation Models](paro_hardware_software_co_design_with_pattern_aware_reorder_based_attention_quantization_in_video_generation_models.md) | 本文面向3D全注意力视频生成模型提出软硬件协同PARO加速器。设计重排序分块混合精度量化，统一注意力为块对角结构，平均4.8bit无损压缩；配套输出位宽感知混合精度PE阵列。在CogVideoX测试，同等硬件下较A100最高提速2.71×，超同类ASIC加速器6.38~7.05倍，能效显著提升。 |
| [面向内存高效推荐系统的混合嵌入框架<br>Hybrid Embedding Framework for Memory-Efficient Recommendation Systems](hybrid_embedding_framework_for_memory_efficient_recommendation_systems.md) | 本文提出混合嵌入框架HDE解决DLRM推荐模型嵌入表内存爆炸问题。依据访问热度划分冷热嵌入，热向量存紧凑查表，冷向量由DHE哈希网络在线生成；CPU查表与GPU网络并行隐藏计算延迟。Criteo/Avazu数据集内存仅为基线5%，AUC损失极小，训练时延与原生FDE基本持平。 |
| [基于整数二次规划的深度视觉模型混合精度量化<br>Mixed-Precision Quantization for Deep Vision Models with Integer Quadratic Programming](mixed_precision_quantization_for_deep_vision_models_with_integer_quadratic_programming.md) | 本文提出CLADO跨层感知混合精度量化框架，针对现有方法忽略层间量化误差耦合的缺陷，基于二阶泰勒展开拆分单/跨层敏感度，仅前向传播快速求解；将比特分配转化整数二次规划IQP，在ImageNet的CNN与ViT模型验证，同等存储约束下分类精度显著优于HAQ、MPQCO等基线。 |
| [最大化脉冲神经网络能效：动态联合剪枝框架<br>Maximizing Energy Efficiency in Spiking Neural Networks: A Dynamic Joint Pruning Framework](maximizing_energy_efficiency_in_spiking_neural_networks_a_dynamic_joint_pruning_framework.md) | 本文面向脉冲神经网络(SNN)提出动态联合剪枝框架，建立时空突触操作(SOP)量化模型，设计多级掩码实现空间脉冲稀疏、TABN模块挖掘时序冗余，搭配动态正则系数策略联合权重与脉冲剪枝。在CIFAR/ImageNet验证，CIFAR-10最高实现126.38倍SOP压缩，精度仅损失2.15%，大幅降低类脑硬件能耗。 |
| [DCDiff：通过基于扩散的DC系数估计增强JPEG压缩<br>DCDiff: Enhancing JPEG Compression via Diffusion-based DC Coefficients Estimation](dcdiff_enhancing_jpeg_compression_via_diffusion_based_dc_coefficients_estimation.md) | 本文提出DCDiff面向IoT低成本摄像头的JPEG增强方案，发送端丢弃全部DC系数仅保留四角块，接收端基于扩散模型端到端重建DC。设计掩码拉普拉斯损失与频率调制采样，规避传统迭代误差传播。多数据集测试PSNR提升3~6.7dB，压缩率平均提升25%，兼容Raspberry Pi、Cortex-A53低功耗设备，下游任务精度衰减仅0.49%。 |


### 涡轮增压式加速深度学习训练：效率与创新并举 (6)

Turbocharging Deep Learning Training: Efficiency Meets Innovation

- Session Chairs: Fan Yang, Li Shang

> 本专场围绕深度学习训练与推理优化的前沿进展展开，重点聚焦边缘设备性能、低精度训练、神经形态计算以及软硬件协同设计四大方向。本场收录的论文探究了多种高效优化技术，这类技术能够降低模型复杂度、减少能耗并提升模型鲁棒性，进而让边缘设备与专用系统获得更优运行性能。

> This session covers advancements in optimizing deep learning training and inference, with a focus on edge-device performance, low-precision training, neuromorphic computing, and hardware-software co-design. The papers presented here explore efficient techniques that reduce model complexity, energy consumption, and improve robustness, enabling better performance for edge and specialized systems.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [NoiseZO：用于高效仅前向训练的RRAM噪声驱动零阶优化<br>NoiseZO: RRAM Noise-Driven Zero-Order Optimization for Efficient Forward-Only Training](noisezo_rram_noise_driven_zero_order_optimization_for_efficient_forward_only_training.md) | 本文提出NoiseZO，一种利用RRAM固有噪声驱动零阶优化的仅前向存内训练框架。采用双RRAM阵列将器件读写噪声转化ZO扰动，无需反向传播；设计细粒度分块优化提升收敛，支持量化稀疏训练。在MNIST、元音数据集验证，相较传统CMOS反向训练能耗降低21倍。 |
| [APSQ：加法部分和量化与算法-硬件协同设计<br>APSQ: Additive Partial Sum Quantization with Algorithm-Hardware Co-Design](apsq_additive_partial_sum_quantization_with_algorithm_hardware_co_design.md) | 本文提出APSQ增量部分和量化算法与可重构硬件协同架构，针对IS/WS数据流高比特PSUM访存能耗痛点。引入分组策略抑制量化误差，配套RAE可重构引擎。CV/NLP/LLM测试，PSUM压缩至INT8，精度损失最高0.83，访存能耗降低28%-87%，LLaMA2-7B最高节能31.7倍。 |
| [NN-AdderNet：用于超低比特AdderNet量化压缩的非负与稀疏权重优化<br>NN-AdderNet: Nonnegative and Sparse Weight Optimization for Ultra-Low Bitwidth AdderNet Quantization and Compression](nn_addernet_nonnegative_and_sparse_weight_optimization_for_ultra_low_bitwidth_addernet_quantization_and_compression.md) | 本文提出NN-AdderNet非负加法网络，通过等价变换将带符号SAD转为无负权重运算，搭配面向激活量化挖掘权重双重稀疏。采用霍夫曼无损压缩实现4bit甚至更低比特存储，精度仅损失0.3%~1.6%；硬件仿真相较CNN推理延迟降低34.8%~38.6%、能耗显著下降。 |
| [Replay4NCL：用于嵌入式AI系统类脑持续学习的高效记忆回放方法<br>Replay4NCL: An Efficient Memory Replay-based Methodology for Neuromorphic Continual Learning in Embedded AI Systems](replay4ncl_an_efficient_memory_replay_based_methodology_for_neuromorphic_continual_learning_in_embedded_ai_systems.md) | 本文提出Replay4NCL脉冲神经持续学习方法，针对现有SpikingLR时序步长过长、开销大问题，采用短时重放搭配动态神经元阈值与学习率补偿 spike信息损失，搭配最优隐数据插入层策略。SHD增量分类任务验证，旧任务精度90.43%，推理提速4.88倍，内存节省20%、能耗下降36.43%。 |
| [FF-INT8：在边缘设备上进行INT8精度高效Forward-Forward DNN训练<br>FF-INT8: Efficient Forward-Forward DNN Training on Edge Devices with INT8 Precision](ff_int8_efficient_forward_forward_dnn_training_on_edge_devices_with_int8_precision.md) | 本文提出FF-INT8，首个基于前向-前向(FF)算法的INT8边缘低精度训练方案。利用FF分层训练规避反向传播量化误差累积，设计前瞻Look-Ahead损失机制弥补原生FF收敛差缺陷。Jetson Orin Nano实测，对比主流INT8训练，训练提速4.6%、能耗降8.3%、内存减少27%，精度仅小幅损失。 |
| [BirdMoE：利用负载感知双随机量化降低专家混合训练通信成本<br>BirdMoE: Reducing Communication Costs for Mixture-of-Experts Training Using Load-Aware Bi-random Quantization](birdmoe_reducing_communication_costs_for_mixture_of_experts_training_using_load_aware_bi_random_quantization.md) | 本文提出BirdMoE负载感知双随机量化压缩方案，适配MoE分布式all-to-all通信。由无偏随机量化RQ与混合精度MP模块组成，解决压缩开销放大、误差累积、通信不均衡三大痛点。四类CV/NLP MoE任务验证，压缩比4.06~10.44倍，训练提速1.18~5.27倍，模型精度几乎无损。 |




## AI2：人工智能/机器学习应用与基础设施 (20)

AI2: AI/ML Application and Infrastructure

### 蓄势待发，规模跃升！人工智能从边缘计算到云端优化的发展之路 (8)

Ready, Set, Scale! AI's Journey from Edge to Cloud Optimization

- Session Chairs: Jinjun Xiong, Yoichi Tomioka

> 随着人工智能模型复杂度不断提升，对优化模型架构与高效推理机制的需求愈发迫切。本场专题论坛将探讨机器学习模型优化领域的前沿进展，聚焦模型运行效率、规模化扩展与硬件适配优化三大方向。首轮报告将深入介绍提升边缘端机器学习模型运行效率的创新方案；中间环节的报告将把重心转向大规模模型，围绕动态图处理、图神经网络缩放规律等核心难点展开研讨；论坛最后将围绕显卡端优化技术展开分享，展示各类高效调度方案，以满足大模型线上服务严苛的运行需求。本次论坛议题覆盖面广泛，从边缘设备到高性能计算系统，全方位展现机器学习模型优化技术的发展前景。

> As AI models grow in complexity, the need for optimized architectures and efficient inference mechanisms becomes more pressing. This session explores cutting-edge advancements in the optimization of machine learning models, with a focus on efficiency, scaling, and hardware optimization. The first set of presentations delves into innovative approaches for enhancing the efficiency of edge ML models. The middle presentations shift the spotlight to large-scale models, addressing key challenges in dynamic graph processing, scaling laws for GNNs. Finally, the session concludes with a look at GPU-side optimizations, showcasing techniques for efficient scheduling to meet the demanding requirements of large model serving. This diverse range of topics provides a comprehensive view of the future of ML model optimization from edge devices to high-performance computing systems.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [短超向量能驱动特征丰富的GNN吗？强化超维计算图表征以构建内存高效GNN<br>Can Short Hypervectors Drive Feature-Rich GNNs? Strengthening the Graph Representation of Hyperdimensional Computing for Memory-efficient GNNs](can_short_hypervectors_drive_feature_rich_gnns_strengthening_the_graph_representation_of_hyperdimensional_computing_for_memory_efficient_gnns.md) | 本文提出CiliaGraph轻量超维计算GNN框架，打破万维超长超向量固有范式，提出PRBF编码、差分聚合、拼接组合三类算子，解决编码失真、图结构偏置、中心节点缺失三大缺陷。仅百维短向量即可完成单样本图分类，相比主流GNN内存平均缩减292倍，训练加速最高313倍，精度与SOTA持平。 |
| [InfScaler：通过非对称自动扩缩容在多加速器边缘设备上实现高效ML推理服务<br>InfScaler: Enabling Efficient ML Inference Serving on Multi-Accelerator Edge Devices via Asymmetric Auto-Scaling](infscaler_enabling_efficient_ml_inference_serving_on_multi_accelerator_edge_devices_via_asymmetric_auto_scaling.md) | 本文提出InfScaler异构多加速器边缘推理服务框架，针对传统全实例对称扩容内存受限问题。设计瓶颈感知非对称自动扩容算法，结合边缘硬件统一内存实现跨加速器无拷贝张量共享。在Jetson Xavier测试，相较主流方案吞吐量最高提升126.59%，内存占用降低27.32%，且满足延迟约束。 |
| [DM-Tune：以高斯混合引导噪声调优实现扩散模型量化<br>DM-Tune: Quantizing Diffusion Models with Mixture-of-Gaussian Guided Noise Tuning](dm_tune_quantizing_diffusion_models_with_mixture_of_gaussian_guided_noise_tuning.md) | 本文提出DM-Tune扩散模型量化框架，打破全精度最优固有认知，设计BF16/FP8浮点混合量化策略。构建三高斯噪声调优头补偿统一FP8量化误差，搭配敏感层筛选、时序/提示感知量化与融合GPU内核。多扩散模型测试，画质、多样性优于FP3，推理速度较SOTA提升5.2倍。 |
| [迈向事件流超分辨的原位类脑计算架构<br>Towards In-Situ Neuromorphic Computing Architecture for Event Stream Super-Resolution](towards_in_situ_neuromorphic_computing_architecture_for_event_stream_super_resolution.md) | 本文面向低分辨率事件相机，首个软硬件协同设计脉冲神经网络超分辨加速器。算法简化SRM神经元、重排卷积时序、定点量化；硬件提出分层架构、KCTR数据流与双流水线实现原位计算，消除层中间存储。28nm流片500MHz，相较GPU提速95.6%，突触操作能耗仅0.546pJ，下游分类精度超98.8%。 |
| [LearnGraph：一种面向动态图处理的学习型架构<br>LearnGraph: A Learning-Based Architecture for Dynamic Graph Processing](learngraph_a_learning_based_architecture_for_dynamic_graph_processing.md) | 本文提出面向动态图的学习型架构LearnGraph，分层设计顶点/边预测学习模型，搭配自适应树存储结构与代价敏感动态调整策略。基于真实与合成图数据集测试，查询吞吐平均提升2.1倍，插入/删除分别提速7倍、5倍，经典图算法总处理时间平均缩短3.5倍。 |
| [原子材料建模中图神经网络的缩放规律<br>Scaling Laws of Graph Neural Networks for Atomistic Materials Modeling](neural_scaling_laws_for_graph_neural_networks_in_atomistic_materials_modeling.md) | 本文面向原子材料建模，探究GNN缩放规律，构建十亿参数等价EGNN基础模型，整合DeepSpeed ZeRO、激活重计算优化HydraGNN。基于1.2TB多源原子数据集开展多组缩放实验，揭示模型规模、数据量、网络宽深与预测误差关系，为大规模材料图训练提供软硬件协同框架。 |
| [VISTA：通过通用局部性感知数据共享优化GPU调度<br>VISTA: Optimizing GPU Scheduling through Versatile Locality-Aware Data Sharing](vista_optimizing_gpu_scheduling_through_versatile_locality_aware_data_sharing.md) | 本文提出VISTA感知GPU调度器，同时挖掘SM间、SM内非相邻CTA/Warp数据共享。设计两级定位追踪器：ISVM轻量模型预测Warp局部性、LSH匹配CTA访存特征。在内存密集型负载验证，相比基线IPC提升48.1%、内存能耗降低51.8%，硬件面积开销不足3%。 |
| [Tropical：通过SLO感知复用提升解耦式LLM服务的SLO达成率<br>Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing](tropical_enhancing_slo_attainment_in_disaggregated_llm_serving_via_slo_aware_multiplexing.md) | 本文提出Tropical调度器，面向LLM分布式推理解决聚合、分离架构各自短板：分离架构预fill排队严重TTFT差，同机架构预fill干扰解码TPOT恶化。设计SLO感知多路复用机制，利用解码时延余量调度预fill，平衡排队与干扰。真实长文本负载下90%SLO达标请求提升2.09倍，相较分离架构P90 TTFT提升9倍。 |


### 人工智能邂逅硅基芯片：依托人工智能驱动创新重塑硬件设计 (6)

AI Meets Silicon: Transforming Hardware Design through AI-Driven Innovation

- Session Chairs: Luis Guerra e Silva, Yutaka Masuda


> 生成式人工智能与电子设计自动化（EDA）的融合，正开启硬件创新的全新时代。本场专题研讨聚焦机器学习模型（尤其是大语言模型LLMs）在硬件设计自动化与量子代码生成领域的前沿进展。研讨开篇将分享利用大语言模型实现硬件设计自动化的相关报告，随后探讨基础模型赋能电子设计自动化的应用潜力，接着介绍依托大语言模型生成量子代码的创新方案；还会深入讲解扩散模型用于合成寄存器传输级（RTL）电路生成的相关实践，最后推出一套多层级、分层式数据集，为硬件设计领域的机器学习研究提供支撑。

> The integration of generative AI into EDA is ushering in a new era of hardware innovation. This session explores cutting-edge advancements in the application of machine learning models, particularly Large Language Models (LLMs), to hardware design automation and quantum code generation. The session begins with presentations on automating hardware design using LLMs. The discussion shifts to the potential of foundation models in enhancing EDA, followed by a novel approach to quantum code generation through LLMs. The session further delves into the use of diffusion models for generating synthetic RTL circuits, and concludes with the introduction of a multi-layered, hierarchical dataset to support machine learning in hardware design.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [自由且公平的硬件：利用LLM实现无版权侵权Verilog生成的路径<br>Free and Fair Hardware: A Pathway to Copyright Infringement-Free Verilog Generation using LLMs](free_and_fair_hardware_a_pathway_to_copyright_infringement_free_verilog_generation_using_llms.md) | 本文面向LLM生成Verilog存在IP版权侵权风险，构建版权违规评测基准，设计自动化数据集清洗流水线，产出合规开源数据集FreeSet（22万+文件），基于该数据集持续预训练得到FreeV模型。测试显示FreeV版权违规率仅3%，在VerilogEval上pass@10相较原Llama提升10.1%。 |
| [利用强化学习增强LLM实现高灵活性硬件生成<br>Hardware Generation with High Flexibility using Reinforcement Learning Enhanced LLMs](hardware_generation_with_high_flexibility_using_reinforcement_learning_enhanced_llms.md) | 本文提出PPA-RTL强化学习大模型硬件生成框架，将综合后功耗、性能、面积作为奖励信号，基于DPO直接偏好优化适配7类硬件PPA优化目标。以Deepseek-coder/RTLCoder为底座，离线EDA构建偏好数据集。SFT-RL方案相较纯SFT，功耗平均降20.97%、时序性能提升14.68%、面积缩减29.05%，语法功能精度损失可控。 |
| [NetTAG：基于文本属性图的RTL与版图对齐网表多模态基础模型<br>NetTAG: A Multimodal RTL-and-Layout-Aligned Netlist Foundation Model via Text-Attributed Graph](nettag_a_multimodal_rtl_and_layout_aligned_netlist_foundation_model_via_text_attributed_graph.md) | 本文提出NetTAG网list多模态基础模型，将电路建模为文本属性图(TAG)，融合LLM文本编码器ExprLLM与图Transformer TAGFormer。设计多层自监督预训练与RTL-版图跨阶段对齐，适配多类功能、物理EDA任务。实验相较GNN、AIG预训练基线精度大幅提升，推理速度优于商用EDA工具。 |
| [通过多智能体优化与量子纠错增强基于LLM的量子代码生成<br>Enhancing LLM-based Quantum Code Generation with Multi-Agent Optimization and Quantum Error Correction](enhancing_llm_based_quantum_code_generation_with_multi_agent_optimization_and_quantum_error_correction.md) | 本文面向量子代码生成提出三智能体协同多Agent框架，融合迭代多轮推理、结构化CoT与量子纠错QEC模块。基于Starcoder微调构建代码生成、语义分析、QEC预测三Agent，自建分层量子测试集验证。SCoT可提升准确率50%，RAG增益仅4%，框架能生成容错量子电路，有效抑制量子噪声。 |
| [SynCircuit：自动生成新的合成RTL电路以支撑电路大数据<br>SynCircuit: Automated Generation of New Synthetic RTL Circuits Can Enable Big Data in Circuits](syncircuit_automated_generation_of_new_synthetic_rtl_circuits_can_enable_big_data_in_circuits.md) | 本文提出SynCircuit RTL合成电路生成框架，分三阶段解决EDA开源电路数据稀缺难题：定向循环图扩散生成、概率引导合法性后处理、MCTS逻辑冗余优化。可生成合规Verilog/VHDL代码，图结构、时序面积特征贴近真实电路。扩充PPA预测训练集后，模型MAPE最低下降10%，显著优于GraphRNN、DVAE等基线。 |
| [PyraNet：面向Verilog的多层级层次化数据集<br>PyraNet: A Multi-Layered Hierarchical Dataset for Verilog](pyranet_a_multi_layered_hierarchical_dataset_for_verilog.md) | 本文提出PyraNet分层Verilog开源数据集与配套微调方案。数据集按代码质量分为六层金字塔结构，搭配分层损失加权+课程学习微调策略。基于CodeLlama、DeepSeek-Coder验证，相较原始基线pass@k最高提升32.6%，超越RTLCoder、OriGen等SOTA模型最高16.7%。 |


### 智能电路，更优算法：人工智能驱动的电路建模与优化创新 (6)

Smart Circuits, Smarter Algorithms: AI-Driven Innovations in Circuit Modeling and Optimization

- Session Chairs: Jun Shiomi, Subhajit Dutta Chowdhury

> 本场分会场深入探讨机器学习在硬件设计各阶段的应用，涵盖模拟电路、时序电路、物理设计与仿真领域。第一组报告聚焦利用人工智能优化模拟电路设计，相关分享围绕模拟混合信号电路寄生电容预测的创新方案展开。第三份报告将研究重心转向时序电路设计，介绍依托机器学习技术、以行为为核心的全新优化方法。随后，会上推出一款物理设计流程推荐工具，展示人工智能如何优化设计流程。本场分会场最后以两场仿真相关报告收尾，分别探究机器学习与SPICE模型的融合方案，以及采用神经网络紧凑建模技术加速设计工艺协同开发的实践路径。

> This session delves into the application of machine learning across different stages of hardware design, from analog circuits, sequential circuits, physical design, and simulation. The first set of presentations focuses on leveraging AI for optimizing analog circuit design, with talks exploring innovations in parasitic capacitance prediction for AMS circuits. The third presentation shifts focus to sequential circuit design, introducing novel methods for behavior-centric optimization through machine learning techniques. Next, a physical design recipe recommender is presented, showcasing how AI can enhance the design process. Finally, the session concludes with two talks on simulation, examining the integration of machine learning with SPICE models and the use of neural compact modeling for accelerating design-technology co-development.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [AMS电路上的少样本学习及其在寄生电容预测中的应用<br>Few-shot Learning on AMS Circuits and Its Application to Parasitic Capacitance Prediction](few_shot_learning_on_ams_circuits_and_its_application_to_parasitic_capacitance_prediction.md) | 本文提出少-shot图学习框架CircuitGPS用于AMS电路寄生电容预测。将网表建模异构图，采用1跳包围子图采样，设计低成本DSPD位置编码，搭建MPNN+混合图Transformer。预训练做链路预测、微调完成电容回归，零样本泛化全新电路，链路预测精度提升20%以上，电容MAE降低至少0.067。 |
| [将模拟电路表示从工艺中解耦以实现行为导向优化<br>Decoupling Analog Circuit Representation from Technology for Behavior-Centric Optimization](decoupling_analog_circuit_representation_from_technology_for_behavior_centric_optimization.md) | 本文提出行为导向模拟电路优化框架BCOA，将电路用晶体管电气特性解耦工艺依赖，设计电气-尺寸映射方法，构建RBF-KAN小样本代理模型，搭配MC-HV帕累托估计加速多目标优化。基于AnalogGym放大器验证，大小信号FOM提升1.73~2.64倍，工艺迁移速度提升3.5~6.2倍，仿真开销大幅降低。 |
| [MOSS：时序电路多模态表征学习<br>MOSS: Multi-Modal Representation Learning on Sequential Circuits](moss_multi_modal_representation_learning_on_sequential_circuits.md) | 本文提出MOSS时序电路多模态表征学习框架，融合LLM与GNN互补优势。微调代码大模型提取RTL全局语义增强DFF锚点特征；设计自适应聚合器与两阶段异步传播建模时序反馈，搭配本地+全局多模态对齐损失。在100~5000单元工业电路测试，到达时间预测精度达95.2%，大幅超越DeepSeq2基线。 |
| [InsightAlign：基于设计洞察的可迁移物理设计配方推荐器<br>InsightAlign: A Transferable Physical Design Recipe Recommender Based on Design Insights](insightalign_a_transferable_physical_design_recipe_recommender_based_on_design_insights.md) | 本文提出InsightAlign可迁移物理设计配方推荐框架，提取布局时序功耗等专家级设计洞察作为特征，借鉴LLM对齐思想采用边际DPO训练解码器模型。分为离线对齐、在线微调两阶段，在45nm至亚10nm共17个工业设计零样本测试，超95%场景推荐方案优于历史最优，大幅缩短PPA收敛迭代次数。 |
| [基于自注意力到算子学习的3D-IC热仿真<br>Self-Attention To Operator Learning-based 3D-IC Thermal Simulation](self_attention_to_operator_learning_based_3d_ic_thermal_simulation.md) | 本文提出SAU-FNO算子学习框架用于3D IC热仿真，融合FNO、U-Net与自注意力机制，弥补传统FNO高频信息丢失缺陷；引入高低保真迁移学习降低高精度数据集依赖。在三类堆叠3D芯片验证，相较传统有限元工具提速842倍，热预测MSE相比主流算子模型降低50%以上。 |
| [利用神经紧凑建模与数据驱动SPICE仿真加速设计-工艺协同开发<br>Accelerating design-technology co-development using neural compact modeling and data-driven SPICE simulation](accelerating_design_technology_co_development_using_neural_compact_modeling_and_data_driven_spice_simulation.md) | 本文提出融合神经紧凑模型(NCM)与DataSPICE数据驱动仿真的DTCO协同优化框架。基于迁移学习实现器件电气目标快速重定向，搭配W/L/T插值、工艺偏移修正、版图效应子电路适配。15k晶体管电路验证，模型开发周期缩短95%，仿真精度超98.6%，无收敛与性能损失。 |




## AI3：人工智能/机器学习架构设计 (34)

AI3: AI/ML Architecture Design

### Transformers：优化型大语言模型的崛起 (6)

Transformers: Rise of the Optimized Large Language Models

- Session Chairs: Abdelrahman Hosny, Marina Neseem

> 本次会议聚焦transformers与大语言模型优化相关内容。大语言模型本质上由变换器构建而成，transformers依托自注意力机制，在理解序列内部上下文与关联关系方面具备极强性能，因此针对大语言模型的硬件优化工作至关重要。我们将带来一篇角逐最佳论文奖的DRAFT相关报告，该论文提出一种巧妙的硬件技术，通过近似反向传播硬件计算实现能效的大幅提升。其余收录论文涵盖软硬件协同设计、内存内检索技术、注意力机制、长上下文生成，以及低精度数据格式帕累托前沿综述等方向。

> This session is about transformers and large language model optimizations. As LLMs are essentially made of transformers due to their superior effectiveness to understand context and relationships within sequences by using self-attention mechanism, their hardware optimizations are quite important. We have a best paper award candidate presentation for DRAFT, which is about a clever hardware technique that approximates the backpropagation hardware for great energy efficiency improvement. Our other papers cover hardware/algorithm co-design, retrieval-in-memory techniques, attention, long-context generation, and an overview of the pareto-frontier for low-precision data formats.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [SSFT：用于大语言模型结构化稀疏微调的算法与硬件协同设计<br>SSFT: Algorithm and Hardware Co-design for Structured Sparse Fine-Tuning of Large Language Models](ssft_algorithm_and_hardware_co_design_for_structured_sparse_fine_tuning_of_large_language_models.md) | 本文提出软硬件协同SSFT框架，算法层SSFT-Alg挖掘权重梯度行列结构化稀疏，替代无规则稀疏微调；硬件SSFT-Hw配套稀疏感知取数与调度单元，适配LLM微调四阶段流程。在BERT、LLaMA2 7B/13B验证，精度损失低于1%，加速器相较A100吞吐提升51倍、能效提升19倍，超越SOTA TransCODE。 |
| [DRAFT：将反向传播与预训练主干解耦以实现边缘高效Transformer微调<br>DRAFT: Decoupling Backpropagation from Pre-trained Backbone for Efficient Transformer Fine-Tuning on Edge](draft_decoupling_backpropagation_from_pre_trained_backbone_for_efficient_transformer_fine_tuning_on_edge.md) | 本文提出DRAFT软硬件协同框架面向边缘Transformer微调，设计FDA解耦反向传播算法，通过可训练适配器+N:M三值稀疏旁路网络BPN替代主干权重反向路径；配套可重构加速器适配稀疏稠密双数据流。多NLP/CV模型测试，精度损失低于1%，微调平均提速4.9倍、能效提升4.2倍。 |
| [少搬运，快检索：面向语言模型的存内检索架构<br>Move Less, Retrieve Fast: A Retrieval-in-Memory Architecture for Language Models](move_less_retrieve_fast_a_retrieval_in_memory_architecture_for_language_models.md) | 本文提出面向检索增强大模型的存内检索架构Rimast，软硬件协同缓解检索阶段海量数据搬运与不规则访存瓶颈。硬件采用3D堆叠分层PIM定制存内数据流；软件设计无偏数据映射与ILP自适应卸载均衡负载。十亿级嵌入测试下，相较CPU、GPU、专用加速器分别提速273×、55×、2.41×，能耗大幅降低。 |
| [KVO-LLM：提升批量LLM推理长上下文生成吞吐量<br>KVO-LLM: Boosting Long-Context Generation Throughput for Batched LLM Inference](kvo_llm_boosting_long_context_generation_throughput_for_batched_llm_inference.md) | 本文提出算法架构协同优化方案KVO-LLM面向长上下文批量LLM推理。算法端设计DSQ差分量化+HCAP注意力剪枝压缩KV缓存，外部访存削减超91%；硬件采用算子融合与跨批次交织多核心加速器。28nm流片后相较SOTA加速器吞吐量最高7.32倍，能效提升5.52~8.38倍。 |
| [基于均衡脉动阵列与多行交织排序的Transformer注意力高能效高利用率硬件架构<br>An Energy-Efficient High-Utilization Hardware Architecture for Attention Mechanism in Transformer using Balanced Systolic Array and Multi-Row Interleaved Operation Ordering](an_energy_efficient_high_utilization_hardware_architecture_for_attention_mechanism_in_transformer_using_balanced_systolic_array_and_multi_row_interleaved_operation_ordering.md) | 本文面向Transformer注意力模块提出纯硬件优化架构：均衡脉动阵列BSA与多行交织调度。BSA融合内外混合乘，采用广播分块、旁路寄存器、Booth共享，阵列利用率达99.5%；多行交织消除中间P缓存高开销。28nm、BERT测试，整体能效提升39%，吞吐量×能效提升38%，SRAM能耗降低31.7%。 |
| [面向LLM推理的低精度数据格式与MAC架构帕累托前沿探索<br>Finding the Pareto Frontier of Low-Precision Data Formats and MAC Architecture for LLM Inference](finding_the_pareto_frontier_of_low_precision_data_formats_and_mac_architecture_for_llm_inference.md) | 本文系统遍历25000+种MAC硬件设计，对比INT/FP/Posit/LNS/MX/VSQ六类低精度数值格式，以SQNR、面积、能效为指标求解LLM推理帕累托前沿。同等精度下LNS16、MXINT8、VSQINT4相较FP系列能效分别提升1.8×、2.2×、1.9×，同时给出内积、累加位宽等硬件最优配置规律。 |



### 大语言模型与Transformer加速器全解析 (8)

Everything About LLM and Transformer Accelerators

- Session Chairs: Ziang Yin, Yulhwa Kim

> 本次专题将深度探讨面向大语言模型（LLM）与Transformer架构的加速器最新技术进展。参会者将了解硬件与人工智能的交叉领域知识，重点学习通过各类量化及预测优化方案，同步提升计算效率与内存带宽的创新技术。具体而言，本次专题将讲解QKV计算的推测预测机制、包含块浮点与微缩放格式在内的量化方案，以及模型稀疏化处理与稀疏模型的利用方法；同时还会介绍扩散模型加速技术，及其与存内计算架构的融合应用。

> This session will provide an in-depth exploration of the latest advancements in accelerators designed for large language models (LLMs) and transformers. Attendees will gain insights into the intersection of hardware and AI, focusing on the innovations that enhance both computational efficiency and memory bandwidth with various quantization and prediction schemes. More specifically, the session covers the speculative and prediction on QKV computations, quantization schemes including block floating point and microscaling format, and how to sparsificate the models and leverage them. It also covers diffusion model acceleration and the intersection with compute-in-memory architecture.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [3D-TokSIM：通过Token驻留存内计算叠加3D内存实现投机式LLM推理<br>3D-TokSIM: Stacking 3D Memory with Token-Stationary Compute-in-Memory for Speculative LLM Inference](3d_toksim_stacking_3d_memory_with_token_stationary_compute_in_memory_for_speculative_llm_inference.md) | 本文提出3D-TokSIM，面向投机解码LLM的3D堆叠存内计算架构。采用混合键合3D DRAM堆叠与Token驻留数据流CIM，配套输出缓存消除、残差缓存压缩优化。TSMC 22nm流片验证，相比RTX309吞吐量提升15.1倍、能效提升324倍，优于脉动阵列型近存方案。 |
| [基于聚类关联阵列Q-K相关性预测的内存高效LLM加速器，实现选择性KV访问<br>A Memory-Efficient LLM Accelerator with Q-K Correlation Prediction using Cluster-Based Associative Array for Selective KV Accessing](a_memory_efficient_llm_accelerator_with_q_k_correlation_prediction_using_cluster_based_associative_array_for_selective_kv_accessing.md) | 本文提出软硬件协同LLM加速器Sella，设计聚类关联阵列预测Q-K相关性，实现选择性KV缓存访存，无需模型微调。硬件分为预测引擎与流水线计算引擎，在Llama2/OPT/Pythia验证，片外访存最高削减66%，相比SpAtten提速2.1倍、对比CPU提速53.5倍，精度损失可忽略。 |
| [Precon：面向包括LLM在内多领域量化深度学习模型加速的可精度转换架构<br>Precon: A Precision-Convertible Architecture for Accelerating Quantized Deep Learning Models across Various Domains Including LLMs](precon_a_precision_convertible_architecture_for_accelerating_quantized_deep_learning_models_across_various_domains_including_llms.md) | 本文提出Precon可精度转换脉动阵列加速器，设计可拆解指数编码FP16格式，统一MAC单元支持INT4-FP16/INT4-INT8/INT4-INT4三类主流量化模式。复用计算电路、块级移位归一化降低硬件开销，适配LLM、CNN、ViT多模型。全领域测试最高提速4.1倍，能耗降低81.4%，兼顾高精度与极致低比特推理。 |
| [RADiT：利用时间步相似性的冗余感知扩散Transformer加速<br>RADiT: Redundancy-Aware Diffusion Transformer Acceleration Leveraging Timestep Similarity](radit_redundancy_aware_diffusion_transformer_acceleration_leveraging_timestep_similarity.md) | 本文提出软硬件协同加速器RADiT，挖掘DiT扩散模型相邻时间步特征相似冗余，设计块级复用计算方案。配套动态阈值DTS模块与4bit压缩对比CCU单元，28nm流片硬件开销极低。图像/视频推理分别提速1.8×、1.7×，能耗下降41%、45.5%，生成画质损失极小。 |
| [SQ-DM：通过激进量化与时间稀疏性加速扩散模型<br>SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity](sq_dm_accelerating_diffusion_models_with_aggressive_quantization_and_temporal_sparsity.md) | 本文提出软硬件协同SQ-DM加速方案，面向EDM扩散模型设计分层混合4bit量化，将SiLU替换为ReLU挖掘时序通道激活稀疏；配套异构稠密-稀疏加速器，集成时序稀疏检测器与通道末地址映射。相比FP16稠密基线最高提速6.91倍，能耗降低51.5%，4bit下图像FID显著优于现有INT4量化方案。 |
| [XShift：联合量化与稀疏化的FPGA高效二值化LLM<br>XShift: FPGA-efficient Binarized LLM with Joint Quantization and Sparsification](xshift_fpga_efficient_binarized_llm_with_joint_quantization_and_sparsification.md) | 本文提出XShift软硬件协同框架面向FPGA二值LLM推理。设计XNOR-Shift编码将乘法转为异或移位；HAOS联合量化稀疏算法精准保留通道离群值；配套三模式XSSA脉动阵列与BSMC高效SoftMax单元。Alveo FPGA实测DSP用量降低10~15倍，推理提速4.17~4.76倍，能效提升6.95~14.29倍，困惑度优于同类低精度方案。 |
| [BBAL：基于双向块浮点量化的大语言模型加速器<br>BBAL: A Bidirectional Block Floating Point-Based Quantization Accelerator for Large Language Models](bbal_a_bidirectional_block_floating_point_based_quantization_accelerator_for_large_language_models.md) | 本文提出双向块浮点BBFP格式与LLM软硬件协同加速器BBAL。BBFP引入标志位与重叠比特缓解传统BFP对齐最大指数带来的量化误差；配套稀疏MAC单元、分段查表非线性模块。TSMC28nm流片验证，同等硬件开销精度比离群感知加速器提升22%，同精度吞吐量较标准BFP提升40%。 |
| [基于修订微缩放格式量化的大语言模型加速算法-硬件协同设计<br>An Algorithm-Hardware Co-design Based on Revised Microscaling Format Quantization for Accelerating Large Language Models](an_algorithm_hardware_co_design_based_on_revised_microscaling_format_quantization_for_accelerating_large_language_models.md) | 本文提出软硬件协同LLM加速方案RMFQ量化算法与RMFA专用加速器。设计两层修正微缩放RMX格式，创新分组方向适配通道离群值；配套适配脉动阵列与硬件编码器。OPT/LLaMA等模型验证，4/6比特量化达到SOTA精度，RMFA相较OliVe提速1.28倍、能耗降低31%，硬件面积开销仅2%。 |



### 柔和式高斯泼溅：高斯泼溅、视频处理与扩散模型 (6)

Flattering Splatting: Gaussian Splatting, Video Processing, and Diffusion

- Session Chairs: Yonggan Fu, Bokyung Kim

> 本次研讨内容围绕三维视频处理、扩散模型、高斯泼溅技术及其内存优化方案展开。随着深度学习相关研究不断深入，学界发现深度学习所使用的模型可迁移应用于视觉计算领域，由此催生了跨学科研究方向。本次内容将讲解适配硬件、高效运行的扩散模型加速方案、三维视频生成模型以及三维高斯泼溅技术。在三篇聚焦高斯泼溅的论文分享完毕后，我们将以一篇衍射光学神经网络相关论文收尾，该论文采用前沿技术手段，解决模型运行速度与能效两大核心难题。

> This session is about 3D video processing, diffusion, Gaussian splatting, and their memory optimizations. As research into deep learning grows, often people have found that the models used in deep learning are transitive to applications in vision computing, thus creating a cross-disciplinary experience. We cover hardware-efficient diffusion acceleration, 3D video generation models, and 3D Gaussian splatting. After our 3 papers that focus on Gaussian splatting, we conclude with a paper about diffractive optical neural network, using an emergent technology technique to attack the issues of speed and energy efficiency.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [MHDiff：基于焦点像素感知量化的内存与硬件高效扩散加速<br>MHDiff: Memory- and Hardware-Efficient Diffusion Acceleration via Focal Pixel Aware Quantization](mhdiff_memory_and_hardware_efficient_diffusion_acceleration_via_focal_pixel_aware_quantization.md) | 本文提出软硬件协同MHDiff扩散模型加速器，提出焦点像素感知量化算法，单步仅首层读取前序特征大幅削减访存；设计打包模块统一混合精度，配套专用PE阵列。28nm流片，相较Cambricon-D、A100、CPU分别提速3.1×、6.2×、38.4×，图像精度损失不足1%，内存流量降低8.1倍。 |
| [借鉴传统视频处理洞见赋能新兴3D视频生成模型：一种全面的注意力感知方法<br>Harnessing Conventional Video Processing Insights for Emerging 3D Video Generation Models: A Comprehensive Attention-aware Way](harnessing_conventional_video_processing_insights_for_emerging_3d_video_generation_models_a_comprehensive_attention_aware_way.md) | 本文提出面向3D视频生成模型的软硬件协同加速框架SIMPICKER。借鉴传统视频编码时空相似性思路，设计帧/Token两级推测算法，搭配LUT混合乘硬件与自适应分组策略。在CogVideoX、Open-Sora验证无画质损失，相对A10平均提速5.21倍、能效提升17.92倍，优于同类专用ASIC加速器。 |
| [StreamingGS：基于体素流式3D高斯泼溅与内存优化及架构支持<br>StreamingGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support](streaminggs_voxel_based_streaming_3d_gaussian_splatting_with_memory_optimization_and_architectural_support.md) | 本文提出软硬件协同STREAMINGGS框架，针对传统分块式3DGS渲染片外DRAM流量过高、移动端无法达到90FPS VR实时需求问题，改用体素为中心流式渲染范式，搭配双层分层过滤、向量量化与边界微调算法；配套专用加速器含VSU体素排序单元、HFU分层滤波单元。在多场景测试，渲染PSNR几乎无损，相比Orin NX移动GPU提速45.7倍、能耗降低62.9%，超越SOTA GSCore加速器2.1倍速度、2.3倍能效。 |
| [GauRast：增强GPU三角形光栅器以加速3D高斯泼溅<br>GauRast: Enhancing GPU Triangle Rasterizers to Accelerate 3D Gaussian Splatting](gaurast_enhancing_gpu_triangle_rasterizers_to_accelerate_3d_gaussian_splatting.md) | 本文提出GauRast增强型GPU光栅器，复用现有三角形渲染硬件适配3DGS高斯光栅瓶颈运算。仅新增少量专用逻辑，芯片总面积开销仅0.2%。在Jetson Orin边缘平台测试，高斯核心运算提速23倍、能效提升24倍，原版3DGS端到端6倍加速，优化版4倍加速，分别达到24FPS、46FPS。 |
| [Local-GS：利用泼溅局部性的无序高斯泼溅训练加速器<br>Local-GS: An Order-Independent Gaussian Splatting Training Accelerator Exploiting Splat Locality](local_gs_an_order_independent_gaussian_splatting_training_accelerator_exploiting_splat_locality.md) | 本文提出Local-GS软硬件协同3D高斯溅射训练加速器，利用高斯局部性与无序渲染算法消除深度排序依赖；设计并行相交单元与高斯中心调度统一渲染核。7nm工艺实现，在多场景下训练速度相较Jetson NX提升26.9~53倍，能效提升三个数量级，画质损失极小。 |
| [多维可重构、物理可组合的混合衍射光神经网络<br>Multi-Dimensional Reconfigurable, Physically Composable Hybrid Diffractive Optical Neural Network](multi_dimensional_reconfigurable_physically_composable_hybrid_diffractive_optical_neural_network.md) | 本文提出多维可组合混合衍射光神经网络MDR-HDONN，解决传统DONN流片后不可重构难题。挖掘波长、相位板姿态、排布等七维可学习硬件参数，融合自由衍射与集成光子张量核；采用Gumbel-Softmax、ALM实现离散配置可微训练。多任务验证，推理较GPU快74倍、能耗低194倍，训练速度提升5倍。 |



### 我们必须配备这些深度学习硬件加速系统！(6)

We Has to Have These Hardware Accelerator Systems for Deep Learning! 

- Session Chairs: Andreas Herkersdorf, Johannes Maximilian Kuehn

> 本场会议围绕深度神经网络的硬件加速系统设计与优化展开。随着深度学习模型规模持续扩大，研发能效最高、吞吐量最优的硬件平台以执行模型任务变得至关重要。本次会议将介绍多款硬件平台：Hydra是一款基于芯粒技术的混合专家推理系统，SynGPU针对GPU完成相关优化；另有三篇论文对众核架构展开研究；最后，SAGA论文聚焦于内存层面的优化工作。

> This session is about hardware accelerator system designs and optimizations for DNNs. As deep learning models become larger and larger, the quest to find the most energy efficient, and throughput optimized hardware platforms to perform model tasks is very important. Here in this session, many hardware platforms are covered. Hydra is a mixture-of-expert inference system using chiplets, SynGPU does its optimizations on GPU. We have 3 other papers that explore many-core architectures. Finally, paper SAGA focuses its optimizations on memory.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Hydra：在芯粒系统上利用专家热度实现高效MoE推理<br>Hydra: Harnessing Expert Popularity for Efficient Mixture-of-Expert Inference on Chiplet System](hydra_harnessing_expert_popularity_for_efficient_mixture_of_expert_inference_on_chiplet_system.md) | 本文面向芯粒架构MoE推理提出软硬件协同Hydra加速器。软件端基于层间专家选择条件概率做热度感知映射，减少全互联通信；硬件采用CAM消除重排稀疏矩阵运算，混合跳过Softmax冗余计算。22nm工艺下，相较RTX3090延迟降低14.2倍、功耗减少169.1倍，优于FLAME等SOTA加速器。 |
| [SynGPU：融合CUDA与位串行张量核以加速GPU上的视觉Transformer<br>SynGPU: Synergizing CUDA and Bit-Serial Tensor Cores for Vision Transformer Acceleration on GPU](syngpu_synergizing_cuda_and_bit_serial_tensor_cores_for_vision_transformer_acceleration_on_gpu.md) | 本文提出SynGPU软硬件协同框架，面向ViT挖掘token间比特稀疏，设计IBA差分稀疏提取与BSDP位串行点积算法；配套新型数据映射与BSTC位串行张量核，解决CUDA/Tensor核寄存器带宽争抢、浮点指数不统一难题。对比A100，图像/视频ViT平均提速2.15~3.95倍，计算密度提升2.49~3.81倍。 |
| [发掘并利用众核DNN加速器中未被充分利用的缓冲资源<br>Discovering and Exploiting Untapped Buffer Resources in Many-Core DNN Accelerators](discovering_and_exploiting_untapped_buffer_resources_in_many_core_dnn_accelerators.md) | 本文提出BufferProspector多层流水线片上缓存分配策略，发现层流水线映射下因DCR差异核心缓存普遍低利用率。设计缓存需求计算器与贪心分配器，复用闲置缓存存储早生成特征图，规避DRAM读写。对比SOTA Tangram框架，平均性能提升2.26倍、能效提升1.44倍，DRAM访问能耗降低47.3%。 |
| [PacQ：用于超非对称GEMM高效数据流的SIMT微架构<br>PacQ: A SIMT Microarchitecture for Efficient Dataflow in Hyper-asymmetric GEMMs](pacq_a_simt_microarchitecture_for_efficient_dataflow_in_hyper_asymmetric_gemms.md) | 本文面向LLM仅权重量化提出PacQ SIMT微架构，解决高低精度非对称GEMM低效问题。提出沿n维权重打包与输出驻留数据流，设计并行FP-INT乘法单元；基于V100类张量核改造，相较传统SIMT最高提速1.99倍，EDP降低81.4%，寄存器访问减少54.3%。 |
| [MetaDSE：跨负载CPU设计空间探索的小样本元学习框架<br>MetaDSE: A Few-Shot Meta-Learning Framework for Cross-Workload CPU Design Space Exploration](metadse_a_few_shot_meta_learning_framework_for_cross_workload_cpu_design_space_exploration.md) | 本文提出MetaDSE少样本元学习CPU跨负载设计空间探索框架，将DSE转化少样本任务，采用MAML元预训练缓解过拟合与数据歧义；设计WAM负载自适应架构掩码算法，脱离负载相似度依赖。基于SPEC CPU2017与GEM5验证，相较SOTA预测误差降低44.3%，少量样本即可完成新负载精准PPA预测。 |
| [SAGA：利用顶点相似性构建GANN的内存高效加速器<br>SAGA: A Memory-Efficient Accelerator for GANN Construction via Harnessing Vertex Similarity](saga_a_memory_efficient_underline_a_ccelerator_for_underline_ga_nn_construction_via_harnessing_vertex_underline_s_imilarity.md) | 本文提出面向GANN图构建的内存高效加速器SAGA，利用顶点特征相似性设计聚类差分量化算法，搭配两级调度与串行进位PE硬件。针对动态建图场景规避传统预计算开销，在多ANN数据集验证，相较CPU/GPU/NDSearch平均提速9.30×/4.87×/4.15×，能耗分别降低35.46×/7.60×/5.15×，精度损耗极低。 |



### 摒弃比特：面向人工智能的创新运算、架构与协同设计 (8)

Skip the Bits!: Innovative Arithmetic, Architecture, Co-Design for AI

- Session Chairs: Debjyoti Bhattacharjee, Minah Lee

> 本次专题研讨将探讨融合替代算术算法、新型架构与协同设计技术的创新方案，以此优化人工智能系统。研讨兼顾理论突破与实践进展，重点阐释全新算术算法与专用硬件（含稀疏处理、近似计算相关技术）如何推动人工智能模型在运算性能与运行效率层面实现提升。具体而言，本次研讨介绍多款面向高效运算的微架构，例如比特稀疏注意力架构、比特级稀疏乘累加架构、稠密-稀疏脉动阵列架构，以及极坐标形式、浮点近似计算等创新算术算法；同时涵盖高斯泼溅、点云处理等新兴加速器架构。

> In this session, we explore innovative strategies that combine alternate arithmetic approaches, novel architectures, and co-design techniques to enhance AI systems. Focusing on both theoretical and practical advancements, the session highlights how new arithmetic methods and specialized hardware, including sparsity handling and approximation, are driving improvements in performance and efficiency for AI models. More specifically, the session presents various microarchitectures for efficient processing such as bit-sparse attention architecture, bit-level sparse MAC architecture, and dense-sparse systolic array architecture, and novel arithmetic such as Polar form and floating-point approximation. It also includes emerging accelerator architectures including Gaussian Splatting and Point-Cloud Processing.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Blaze：具备工作负载编排优化的高效位稀疏注意力架构<br>Blaze: An Efficient Bit-Sparse Attention Architecture With Workload Orchestration Optimization](blaze_an_efficient_bit_sparse_attention_architecture_with_workload_orchestration_optimization.md) | 本文提出Blaze面向注意力的位稀疏加速器，软硬件协同挖掘数值、比特双层稀疏。设计ACB负载调度机制解决PE阵列内外负载失衡，搭配Leading-Booth简化QK计算，搭载可重构位串行PE。BERT系列测试精度损失≤0.9%，性能2.37~6.18倍、能效9.69~43.96倍优于主流注意力加速器，超越AdaS达1.58倍。 |
| [DenSparSA：一种用于稠密与稀疏矩阵乘法的均衡脉动阵列方法<br>DenSparSA: A Balanced Systolic Array Approach for Dense and Sparse Matrix Multiplication](densparsa_a_balanced_systolic_array_approach_for_dense_and_sparse_matrix_multiplication.md) | 本文提出DenSparSA均衡脉动阵列，原生支持单边/双边非稀疏矩阵乘，稀疏管理硬件可门控隔离。设计向量压缩、置换、过滤三类数据流，搭配带缓冲PE单元。45nm流片验证，稀疏场景提速1.9~22倍；稠密模式面积开销15%(BF16)/12%(FP32)，稠密算力效率远超同类稀疏加速器。 |
| [UniCoS：面向CNN与ViT的统一网络-加速器协同搜索框架<br>UniCoS: A Unified Neural and Accelerator Co-Search Framework for CNNs and ViTs](unicos_a_unified_neural_and_accelerator_co_search_framework_for_cnns_and_vits.md) | 本文提出UniCoS统一网络-加速器协同搜索框架，同时支持CNN与ViT。设计无训练梯度一致性精度代理，搭配聚类+剪枝异构数据流硬件搜索，规避超网预训练开销。ImageNet验证，精度提升1.76%、EDP降低3.54倍，搜索速度最高提升48倍，仅需3小时完成全流程协同寻优。 |
| [GSAcc：通过深度推测与高斯中心光栅化加速3D高斯泼溅<br>GSAcc: Accelerate 3D Gaussian Splatting via Depth Speculation and Gaussian-centric Rasterization](gsacc_accelerate_3d_gaussian_splatting_via_depth_speculation_and_gaussian_centric_rasterization.md) | 本文提出软硬件协同加速器GSAcc面向压缩3DGS渲染，设计帧深度推测复用时序信息，高斯中心数据流消除中间存储，搭配并行排序与瓦片驻留光栅硬件。16nm工艺综合，相比RTX8000 PPA提升16600倍、节能48.7倍；超越SOTA GSCore，PPA提升2.3倍、单帧能耗降低2.9倍。 |
| [具备稀疏性感知分层邻域体素搜索与跳过的高吞吐点云加速器<br>High-throughput Point-Cloud Accelerator with Sparsity-aware Hierarchical Neighbor Voxel Search and Skipping](high_throughput_point_cloud_accelerator_with_sparsity_aware_hierarchical_neighbor_voxel_search_and_skipping.md) | 本文面向自动驾驶点云3D稀疏卷积，提出软硬件协同HVSS加速器框架。算法端采用阈值实时体素跳过抑制空洞扩张；硬件设计三级分层并行CAM邻域搜索单元，搭配64×64权重驻留脉动阵列。65nm工艺实测，延迟降低77.7%，相较SPADE、PointAcc能效、吞吐量分别提升1.34×、2.22×，精度仅微增0.48%。 |
| [April：面向神经网络加速器的精度增强浮点近似<br>April: Accuracy-Improved Floating-Point Approximation For Neural Network Accelerators](april_accuracy_improved_floating_point_approximation_for_neural_network_accelerators.md) | 本文提出April软硬件协同框架，基于对数近似FPMA浮点乘法，设计下采样误差补偿与灵活偏置机制，配套可配置脉动阵列。适配FP8/FP16/BF16多种浮点格式，FPGA实测相较INT8阵列面积降低34%-52%，矩阵RMSE最高下降96%，图像模型精度持平甚至优于INT8方案。 |
| [CVMAX：采用极坐标乘法的复值神经网络加速器架构<br>CVMAX: Accelerator Architecture with Polar Form Multiplication for Complex-Valued Neural Networks](cvmax_accelerator_architecture_with_polar_form_multiplication_for_complex_valued_neural_networks.md) | 本文提出面向复值神经网络的软硬件协同加速架构CVMAX，基于极坐标专用移位量化替代传统直角量化。幅值采用2的幂移位量化消去乘法，相位模块化量化降低误差；配套无乘法PE单元，仅用移位、加法与查表。MRI、极化SAR任务验证，4bit配置精度损失极小，同等面积下提速4.44倍、能耗降低75%，PE面积缩减74%。 |
| [基于软硬件协同设计的高效位级稀疏MAC加速FPGA架构<br>An Efficient Bit-level Sparse MAC-accelerated Architecture with SW/HW Co-design on FPGA](an_efficient_bit_level_sparse_mac_accelerated_architecture_with_sw_hw_co_design_on_fpga.md) | 本文面向FPGA提出粒度自适应粗粒度编码+软硬件协同位稀疏MAC加速器。设计LUT友好粗粒度编码规避Booth过度位拆解，配套局部缓冲与松同步阵列架构解决串行乘法负载失衡。Xilinx UltraScale+平台验证，PE面积比位并行架构小2.2倍，相对位并行提速1.04~1.74倍，优于Booth类设计1.40~2.79倍。 |



## AI4：人工智能/机器学习系统与平台设计 (24)

AI4: AI/ML System and Platform Design

### 兼顾速度与内存：大语言模型加速技术进展 (6)

Balancing Speed and Memory: Advancing LLM Acceleration

- Session Chairs: Chaojian Li, Zhongzhi Yu

> 随着大语言模型（LLM）规模不断扩大，同时优化内存占用与计算吞吐能力变得至关重要。本次分享将介绍六种极具价值的方法，用以解决大语言模型与混合专家模型（MoE）推理过程中的核心瓶颈，其中包括语义感知键值缓存压缩、适配现场可编程门阵列加速的无异常值量化方案，以及中央处理器-图形处理器混合运行策略。除此之外，稀疏注意力均衡、面向状态空间模型的现场可编程门阵列覆层技术、感知算子融合的任务负载优化等全新技术，能够进一步提升处理效率。上述研究成果恰逢其时，可为新一代人工智能加速器的研发提供思路启发，助力其在保障资源利用率的同时实现更高运算性能。

> As LLMs grow in scale, optimizing both memory usage and computational throughput becomes essential. This session introduces six interesting approaches to overcoming key bottlenecks in LLM and MoE inference, including semantic-aware KV cache compression, outlier-free quantization for FPGA acceleration, and hybrid CPU-GPU execution strategies. Additionally, new techniques in sparse attention balancing, FPGA overlays for state-space models, and fusion-aware workload optimization enable more efficient processing. These works comes as a timely effort to inspire next-generation AI accelerators that achieve higher performance while maintaining resource efficiency.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [MambaOPU：面向状态空间对偶Mamba模型的FPGA覆盖处理器<br>MambaOPU: An FPGA Overlay Processor for State-space-duality-based Mamba Models](mambaopu_an_fpga_overlay_processor_for_state_space_duality_based_mamba_models.md) | 本文面向Mamba2（SSD状态空间模型）提出FPGA覆盖处理器MambaOPU，软硬件协同优化算子融合与稀疏计算，设计可重构脉动阵列与稀疏预取单元，实现片上SSD全计算。在多款Mamba2模型验证，相较A100、Xeon CPU归一化吞吐量最高提升880.79×、1812×，能效最高提升24.27×、12908×。 |
| [跨模型融合感知的(gather-matmul-scatter)工作负载优化框架<br>A Cross-model Fusion-aware Framework for Optimizing (gather-matmul-scatter)s Workload](a_cross_model_fusion_aware_framework_for_optimizing_gather_matmul_scatter_s_workload.md) | 本文提出Efficient-GMS跨模型优化框架，统一RGCN、SpConv、MoE共享的gather-matmul-scatter计算模式。设计四类算子融合数据流，性能模型剪枝超90%配置空间，轻量XGBoost自适应选择数据流。在RTX3090/A100验证，RGCN端到端提速1.32x，SpConv提速1.46x，MoE提速1.15x。 |
| [HybriMoE：用于高效MoE推理的CPU-GPU混合调度与缓存管理<br>HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference](hybrimoe_hybrid_cpu_gpu_scheduling_and_cache_management_for_efficient_moe_inference.md) | 本文提出HybriMoE混合CPU-GPU推理框架，解决MoE专家激活不稳定、异构负载失衡问题。设计分层动态调度、收益驱动预取、路由分数缓存三大优化，基于kTransformers实现。在Mixtral/Qwen2/DeepSeek三类MoE模型验证，相较SOTA，Prefill平均提速1.33倍，Decode平均提速1.70倍。 |
| [ClusterKV：在语义空间操控LLM KV缓存以实现可召回压缩<br>ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable Compression](clusterkv_manipulating_llm_kv_cache_in_semantic_space_for_recallable_compression.md) | 本文提出ClusterKV面向长上下文LLM的可召回KV缓存压缩框架，基于Key向量语义聚类替代固定分页筛选。利用余弦距离K-means划分语义簇，仅计算簇中心注意力大幅降低筛选开销，配套异步聚类、GPU定制内核与簇级缓存。32k上下文仅1k-2k缓存预算，推理提速2倍、吞吐提升2.5倍，精度损失极小，优于Quest、InfiniGen。 |
| [DuoQ：一种DSP利用率感知且无离群值的FPGA-LLM加速量化方法<br>DuoQ: A DSP Utilization-aware and Outlier-free Quantization for FPGA-based LLMs Acceleration](duoq_a_dsp_utilization_aware_and_outlier_free_quantization_for_fpga_based_llms_acceleration.md) | 本文提出面向FPGA的DuoQ软硬件协同4bit量化框架，设计跨层等价变换+低语义Token感知算法彻底消除激活离群值，配套DSP感知可重构PE、稀疏编码器与专用非线性处理单元。在LLaMA、OPT系列模型验证，4bit下困惑度大幅优于同类方案，推理最高提速8.8倍、能效提升23.45倍。 |
| [Libra：具备多级负载均衡的混合稀疏注意力加速器<br>Libra: A Hybrid-Sparse Attention Accelerator Featuring Multi-Level Workload Balance](libra_a_hybrid_sparse_attention_accelerator_featuring_multi_level_workload_balance.md) | 本文提出软硬件协同混合稀疏注意力加速器Lib，设计FBS权重分组稀疏、DBQ动态激活量化算法挖掘数值+比特混合稀疏；硬件引入任务池实现多层负载均衡，适配多比特并行运算。TSMC28nm工艺实测，相比Sanger等主流加速器提速1.49~5.89倍，能效提升2.65~10.82倍，精度损失低于1%。 |


### 探索神经网络前沿领域 (6)

Navigating the Frontiers of Neural Networks

- Session Chairs: Kai-Yuan (Kevin) Chao, Amin Firoozshahian

> 本场会议收录六篇创新研究论文，研究核心围绕提升神经网络设计的运行效率与性能表现。论文涵盖的研究主题包括：神经网络架构搜索、面向边缘设备应用的传感器端内压缩、自适应调优负载的性能预测、基于高效位串行处理的加速方案、混合精度算法，以及面向神经符号人工智能的现场可编程门阵列开发框架。上述研究共同印证，新一代技术具备变革性潜力，能够全面提升神经网络驱动系统的运行效率、运算速度、可扩展性与实际效能。

> This session features six papers of innovative research papers focused on advancing the efficiency and performance of neural network designs. Topics cover include neural architecture search, in-sensor compression for edge applications, performance prediction for autotuning workloads, acceleration through efficient bit-serial processing, mixed-precision methods, and FPGA-based framework for neuro-symbolic AI. Together, these works highlight the transformative potential of next-generation technologies in enhancing the efficiency, speed, scalability, and effectiveness of neural network-driven systems.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [NSFlow：面向神经符号AI的端到端FPGA框架与可扩展数据流架构<br>NSFlow: An End-to-End FPGA Framework with Scalable Dataflow Architecture for Neuro-Symbolic AI](nsflow_an_end_to_end_fpga_framework_with_scalable_dataflow_architecture_for_neuro_symbolic_ai.md) | 本文提出NSFlow端到端FPGA神经符号AI加速框架，前端设计生成器解析数据流并两阶段空间探索，后端自适应脉动阵列支持神经网络与VSA符号运算，搭配可重组片上存储与混合精度。在多推理任务验证，相较TX2提速31倍、GPU超2倍、TPU8倍、DPU3倍，符号负载150倍扩展时运行时仅增4倍。 |
| [BitPattern：通过比特模式剪枝实现高效位串行深度神经网络加速<br>BitPattern: Enabling Efficient Bit-Serial Acceleration of Deep Neural Networks through Bit-Pattern Pruning](bitpattern_enabling_efficient_bit_serial_acceleration_of_deep_neural_networks_through_bit_pattern_pruning.md) | 本文提出BitPattern软硬件协同框架，面向位串行DNN加速器设计比特模式剪枝算法与专用解码PE硬件。自定义1:M稀疏比特模式，搭配相似度合并均衡计算负载，配套轻量化解码器。ResNet/ViT验证，模型压缩最高1.72倍，推理提速2.11倍、能耗降低1.86倍，精度损失低于0.8%。 |
| [BLOOM：用于混合精度DNN加速的位切片框架<br>BLOOM: Bit-Slice Framework for DNN Acceleration with Mixed-Precision](bloom_bit_slice_framework_for_dnn_acceleration_with_mixed_precision.md) | 本文提出BLOOM位切片混合精度DNN加速框架，将8bit张量拆分为高低4bit分片并行计算，利用高位天然稀疏，摒弃编解码开销。配套权重驻留脉动阵列，离线均衡高低精度PE负载。CNN/ViT/BERT/GPT2验证，精度损失低于0.1%，相较主流方案提速1.2~4倍，能耗降低24.6%~71.3%。 |
| [ESM：构建硬件感知神经架构搜索高效代理模型的框架<br>ESM: A Framework for Building Effective Surrogate Models for Hardware-Aware Neural Architecture Search](esm_a_framework_for_building_effective_surrogate_models_for_hardware_aware_neural_architecture_search.md) | 本文提出ESM硬件感知代理模型构建框架，面向OFA类超网络NAS实现精准推理时延预测。设计FCC特征组合编码，搭配平衡采样与迭代数据集扩充流程，以MLP构建预测器。在GPU/CPU/嵌入式多硬件、多超网络验证，预测精度最高99%，平衡采样仅需500样本即可收敛，大幅降低数据集采集开销。 |
| [SnapPix：受高效编码启发的边缘视觉传感器内压缩<br>SnapPix: Efficient-Coding--Inspired In-Sensor Compression for Edge Vision](snappix_efficient_coding_inspired_in_sensor_compression_for_edge_vision.md) | 本文提出SNAPPIX传感-算法协同片上压缩系统，借鉴高效编码理论设计任务无关编码曝光(CE)采样模板，搭配适配ViT的分层训练方案；仅少量晶体管改造堆叠图像传感器。在动作识别、视频重建任务验证，同等压缩率下精度优于现有方法，边缘端能耗最高降低15.4倍。 |
| [用于自动调优工作负载性能估计的指令级精确模拟器<br>Introducing Instruction-Accurate Simulators for Performance Estimation of Autotuning Workloads](introducing_instruction_accurate_simulators_for_performance_estimation_of_autotuning_workloads.md) | 本文面向TVM自动调优硬件资源受限问题，提出仿真适配接口与仿真统计分数预测器两大方案。基于gem5指令精确仿真提取缓存、指令特征，训练MLR/DNN/贝叶斯/XGBoost预测器排序调度方案。在x86/ARM/RISC-V验证，最优调度均落在预测前3%，并行仿真可大幅缩短嵌入式设备调优耗时。 |



### 大模型崛起：势不可挡 (6)

LLM Uprising: Fast & Furious

- Session Chairs: Shiyu Li, M. Hassan Najafi

> 大语言模型（LLM）早已不再是高科技行业极客圈内的专属术语，如今它已是霸占各大新闻头条的热门词汇，深度融入我们日常生活的方方面面。本场专题分享六篇前沿研究论文，聚焦大语言模型性能与运行效率优化方向。这些论文攻克了大语言模型落地部署、技术融合、运行效能层面的核心难题，研究主题涵盖推理服务优化、高效令牌生成、训练加速，以及可辅助芯片设计人员缩短设计周期、提升设计质量的创新行业应用，充分展现了这类强力模型广泛深远的影响力。

> LLM is no longer a geek's term in the high-tech industry; it is now a buzzword dominating headlines and becoming an integral part of our daily lives. This session presents six leading-edge research papers focused on optimizing the performance and efficiency of LLMs. These papers tackle critical challenges in LLM deployment, technology integration, and operational efficiency. The topics cover optimized inference serving, efficient token generation, accelerated training, and innovative field applications that assist chip designers optimize the design cycle and improve design quality, demonstrating the broad impact of these power models.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [VEDA：通过投票式KV缓存淘汰与数据流灵活加速器实现高效LLM生成<br>VEDA: Efficient LLM Generation Through Voting-based KV Cache Eviction and Dataflow-flexible Accelerator](veda_efficient_llm_generation_through_voting_based_kv_cache_eviction_and_dataflow_flexible_accelerator.md) | 本文提出VEDA端侧LLM专用加速器，实现算法-数据流-硬件三重协同优化。设计投票式KV缓存淘汰算法消除传统指标偏差；提出灵活内外积可重构PE阵列适配动态GEMV；元素串行调度将Softmax/LN硬件开销降至O(1)。28nm流片能效达GPU38.8倍，推理速度提升2.3~10倍，困惑度损失极小。 |
| [LLMShare：通过硬件架构探索优化LLM推理服务<br>LLMShare: Optimizing LLM Inference Serving with Hardware Architecture Exploration](llmshare_optimizing_llm_inference_serving_with_hardware_architecture_exploration.md) | 本文提出LLMShare硬件探索框架，针对Prefill、解码两阶段算力/内存需求差异，构建服务仿真器与多目标贝叶斯DSE。设计内存导向初始化、分层树核GP代理，以EHVI寻帕累托硬件配置。相比商用H100集群，成本降低13%，吞吐量提升4倍以上。 |
| [SSDTrain：将激活卸载到SSD以加速大语言模型训练的框架<br>SSDTrain: An Activation Offloading Framework to SSDs for Faster Large Language Model Training](ssdtrain_an_activation_offloading_framework_to_ssds_for_faster_large_language_model_training.md) | 本文提出SSDTrain面向大模型训练的激活卸载框架，基于NVMe SSD借助GDS直连通路异步搬运激活张量，配套张量去重、数据转发优化，IO与计算完全重叠。兼容PyTorch/Megatron/DeepSpeed，在BERT/GPT/T5测试，激活峰值内存最高降低47%，训练时延几乎无损失，可提升微批次大小、减少流水线气泡。 |
| [LEMOE：用于微架构探索的LLM增强多目标贝叶斯优化<br>LEMOE: LLM-Enhanced Multi-Objective Bayesian Optimization for Microarchitecture Exploration](lemoe_llm_enhanced_multi_objective_bayesian_optimization_for_microarchitecture_exploration.md) | 本文提出LEMOE，面向RISC-V BOOM乱序核设计空间探索，融合LLVM程序特征与大模型构建多目标贝叶斯优化框架。设计程序感知初始化、LLM代理模型与EHVI采集函数，在IPC/功耗双目标优化下，同等迭代超22.8%能效提升，达成最高2.9倍探索加速。 |
| [SpecASR：通过投机解码加速基于LLM的自动语音识别<br>SpecASR: Accelerating LLM-based Automatic Speech Recognition via Speculative Decoding](specasr_accelerating_llm_based_automatic_speech_recognition_via_speculative_decoding.md) | 本文提出SpecASR面向LLM语音识别的推测解码框架，利用音频约束带来大小模型高对齐特性，设计自适应序列、草稿复用、双路稀疏树三大优化。在LibriSpeech数据集验证，相比自回归基线提速3.04~3.79倍，优于通用推测解码1.25~1.84倍，识别字错误率无损失。 |
| [PISA：面向自适应数值类型LLM的高效精度切片框架<br>PISA: Efficient Precision-Slice Framework for LLMs with Adaptive Numerical Type](pisa_efficient_precision_slice_framework_for_llms_with_adaptive_numerical_type.md) | 本文提出PISA精度切片LLM推理框架，将16bit数据拆分为4bit高位+12bit低位，利用高位天然稀疏设计Early Bird早停机制，可跳过低贡献计算。硬件采用无编解码交错脉动阵列，兼容传统加速器。在BERT、LLaMA等模型测试，较主流方案提速1.3~4.3倍，能耗降低14.3%~66.7%，精度损失极小。 |




### 智能算力，极速推理：边缘端人工智能系统优化方案 (6)

Smarter Compute, Faster Inference: Optimizing AI Systems on Edge

- Session Chairs: Xiaoxuan Yang, Shihao Song

> 随着人工智能持续向实时、低资源消耗运算方向发展，在各类硬件平台上同时优化算力与内存占用变得至关重要。本场专题分享将介绍一系列旨在提升边缘端人工智能运行效率的技术，其中包括适配真实场景限制的联邦学习框架、用于缓解推理冷启动问题的前置优化策略，以及可分离内存访问操作的新型数据流传输技术。除此之外，跨层级仿真、面向任务的检测算法以及基于现场可编程门阵列（FPGA）的低延迟图处理全新方案，也将展示软硬件协同设计如何打造更智能、更高速、能效更高的人工智能系统。

> As AI continues to push toward real-time and resource-efficient processing, optimizing both compute and memory across diverse hardware platforms becomes crucial. This session introduces techniques that aim to improve AI efficiency at the edge, including federated learning frameworks that account for real-world constraints, proactive strategies for mitigating inference cold starts, and novel data streaming techniques that decouple memory access. Additionally, new approaches in cross-layer simulation, task-oriented detection, and low-latency graph processing on FPGAs showcase how hardware-software co-design can unlock smarter, faster, and more efficient AI systems.



| 中英论文题目 | 研究概要 |
|------------|-----------|
| [PracMHBench：基于真实边缘设备约束重新评估模型异构联邦学习<br>PracMHBench: Re-evaluating Model-Heterogeneous Federated Learning Based on Practical Edge Device Constraints](pracmhbench_re_evaluating_model_heterogeneous_federated_learning_based_on_practical_edge_device_constraints.md) | 本文提出首个面向真实边缘约束的模型异构联邦学习评测基准PracMHBench，划分宽度/深度/拓扑三层异构，覆盖CV/NLP/HAR多任务，构建算力/通信/内存三类边缘受限场景。以全局精度、收敛时长等多指标系统评测现有MHFL算法，给出不同硬件约束下最优方案选择指南。 |
| [SimPhony：面向异构电子-光子AI系统的器件-电路-架构跨层建模与仿真框架<br>SimPhony: A Device-Circuit-Architecture Cross-Layer Modeling and Simulation Framework for Heterogeneous Electronic-Photonic AI System](simphony_a_device_circuit_architecture_cross_layer_modeling_and_simulation_framework_for_heterogeneous_electronic_photonic_ai_system.md) | 本文开源SimPhony跨层仿真框架，面向异构光电集成AI芯片，搭建器件库与分层架构生成器，支持多类光子张量核统一建模。融合光学多维并行数据流、数据感知能耗、布局感知面积、光链路预算多模块，可与ONN训练工具协同，在GEMM、Transformer任务验证，仿真指标与真实流片结果高度吻合。 |
| [DataMaestro：为数据流加速器带来解耦内存访问的通用高效数据流引擎<br>DataMaestro: A Versatile and Efficient Data Streaming Engine Bringing Decoupled Memory Access To Dataflow Accelerators](datamaestro_a_versatile_and_efficient_data_streaming_engine_bringing_decoupled_memory_access_to_dataflow_accelerators.md) | 本文提出DataMaestro通用解耦数据流引擎，面向DNN加速器分离访存与计算流程。支持N维可编程仿射地址、细粒度预取、运行时切换存储寻址模式，内置可扩展通路实时数据变换。集成矩阵/量化加速器在22nm、FPGA验证，PE利用率接近100%，吞吐量较SOTA提升1.05~21.39倍，仅占系统6.43%面积、15.06%功耗。 |
| [iTaskSense：资源受限环境中的任务导向目标检测<br>iTaskSense: Task-Oriented Object Detection in Resource-Constrained Environments](itasksense_task_oriented_object_detection_in_resource_constrained_environments.md) | 本文提出iTaskSense面向资源受限边缘的任务导向目标检测框架，借助LLM生成任务属性知识图实现少样本泛化，提供蒸馏高精度、量化轻量化双模型方案；设计统一ASIC脉动阵列硬件，兼容CNN分割与ViT推理。实验相较GPU提速3.5倍、能耗降低40%，蒸馏模型专项任务精度较量化版提升15%。 |
| [PaSK：通过GPU主动与选择性内核加载缓解推理冷启动<br>PaSK: Cold Start Mitigation for Inference with Proactive and Selective Kernel Loading on GPUs](pask_cold_start_mitigation_for_inference_with_proactive_and_selective_kernel_loading_on_gpus.md) | 本文提出PASK中间件缓解GPU DNN推理冷启动，核心为主动交错执行与分类内核缓存复用。主动并行内核加载与计算，里程碑后复用已加载通用算子内核规避加载开销；按算子模式分类缓存降低匹配耗时。在AMD MI100测试，相比原生推理引擎平均提速5.62倍，额外运行开销仅1.3%。 |
| [FLAG：基于向量量化的低时延GNN推理服务FPGA系统<br>FLAG: An FPGA-Based System for Low-Latency GNN Inference Service Using Vector Quantization](flag_an_fpga_based_system_for_low_latency_gnn_inference_service_using_vector_quantization.md) | 本文提出基于FPGA的FLAG低延迟GNN推理服务系统，针对图服务预处理开销、邻域爆炸两大瓶颈。离线对背景节点预计算+融合LSH的向量量化压缩，在线设计轻量化聚合算法，配套编码-计算流水FPGA架构。GCN/GraphSAGE/GAT三类模型相较GPU基线平均提速154×、176×、333×，精度损失控制在0.5%以内。 |


