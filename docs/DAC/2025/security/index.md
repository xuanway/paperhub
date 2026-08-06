# Security · DAC 2025 (42)

本分类收录 DAC 2025（第62届）Track "Security" 的论文。


## SEC1: 人工智能/机器学习安全与隐私 (12)

SEC1: AI/ML Security/Privacy


### AI遭遇攻击：提升机器学习系统的隐私性、鲁棒性和可信度 (6)

AI Under Attack: Enhancing Privacy, Robustness, and Trust in ML Systems

- Session Chairs: Adnan Siraj Rakin, Ayesha Siddique

> 随着人工智能技术飞速发展，完善可靠的安全防护措施对于降低风险、保护敏感数据至关重要。本次论坛聚焦人工智能安全与隐私保护领域的前沿研究，针对各类机器学习范式下涌现的新型威胁与创新防御方案展开探讨。研讨主题涵盖嵌入式设备上具备抗攻击能力的联邦学习、依托机器遗忘技术实现的隐蔽后门攻击，以及适用于入侵检测系统的持续异常识别技术。本次论坛同时介绍图神经网络的安全推理、保护隐私的协同学习，以及无数据知识蒸馏技术的最新进展。

> With the rapid evolution of AI technologies, ensuring robust security measures is crucial to mitigating risks and safeguarding sensitive data. This session explores cutting-edge research in AI security and privacy, addressing emerging threats and novel defenses across various machine learning paradigms. Topics include resilient federated learning on embedded devices, concealed backdoor attacks using machine unlearning, and continual novelty detection for intrusion detection systems. The session also covers secure inference of graph neural networks, privacy-preserving collaborative learning, and advancements in data-free knowledge distillation.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [弱网受限嵌入式设备上的鲁棒联邦学习<br>Resilient Federated Learning on Embedded Devices with Constrained Network Connectivity](resilient_federated_learning_on_embedded_devices_with_constrained_network_connectivity.md) | 本文提出AdaFL自适应联邦学习框架，先实证发现20%客户端掉线对精度影响微弱、异步陈旧更新危害更大。基于梯度相似度与带宽计算效用分块，动态筛选客户端、自适应梯度压缩。在嵌入式设备实测，通信开销降低60%~78%，精度最高提升30%，额外CPU开销仅0.05%。 |
| [ReVeil：利用机器遗忘对深度神经网络发起无约束隐蔽后门攻击<br>ReVeil: Unconstrained Concealed Backdoor Attack on Deep Neural Networks using Machine Unlearning](reveil_unconstrained_concealed_backdoor_attack_on_deep_neural_networks_using_machine_unlearning.md) | 本文提出ReVeil无约束隐蔽后门攻击，仅污染数据集、无需黑白盒模型与辅助数据。通过高斯噪声生成伪装样本抑制部署前攻击成功率，用户发起机器遗忘请求后即可恢复高后门激活率，可绕过STRIP、Neural Cleanse、Beatrix三类主流后门检测，在4数据集4触发器下验证有效性。 |
| [CND-IDS：入侵检测系统的持续新颖性检测<br>CND-IDS: Continual Novelty Detection for Intrusion Detection Systems](cnd_ids_continual_novelty_detection_for_intrusion_detection_systems.md) | 本文提出CND-IDS无标签持续异常入侵检测框架，由持续特征提取器与PCA重构异常检测器构成。设计融合聚类分离、重建、持续正则的复合损失，仅依靠正常数据训练，无需攻击标签。在4类IoT/网络入侵数据集验证，相比SOTA无监督持续学习方法F1最高提升6.1倍，零日攻击泛化能力提升6.5倍。 |
| [密库中的图：利用可信执行环境保护边缘GNN推理<br>Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment](graph_in_the_vault_protecting_edge_gnn_inference_with_trusted_execution_environment.md) | 本文提出GNNVault，首款面向边缘GNN的TEE安全推理框架，采用训练前拆分策略，构建公共主干与TEE私有校正器。公共主干基于替代图运行于不可信区，真实邻接矩阵与轻量化校正器置于SGX飞地。多图数据集测试精度损失低于2%，可抵御链路窃取攻击，飞地内存占用符合SGX限制，推理开销可控。 |
| [Ensembler：通过选择性集成防御模型反演的协同推理隐私保护<br>Ensembler: Protect Collaborative Inference Privacy from Model Inversion Attack via Selective Ensemble](ensembler_protect_collaborative_inference_privacy_from_model_inversion_attack_via_selective_ensemble.md) | 本文提出Ensembler选择性集成框架，抵御边缘云协同推理下模型逆攻击。云端部署多分支网络，客户端私有选择子集融合特征，搭配分层训练与正则约束。仅客户端保留单层极端轻量化场景仍可防护，相比基线SSIM最高下降43.5%，推理总开销仅4.8%，兼容噪声类隐私防护方案。 |
| [CAE-DFKD：弥合无数据知识蒸馏中的可迁移性鸿沟<br>CAE-DFKD: Bridging the Transferability Gap in Data-Free Knowledge Distillation](cae_dfkd_bridging_the_transferability_gap_in_data_free_knowledge_distillation.md) | 本文提出CAE-DFKD无数据知识蒸馏框架，摒弃图像层操作转向嵌入层优化。设计CEND类别嵌入扩散模块生成结构化潜空间，搭配CNCL嵌入级对比学习，解决合成图质量不均、泛化迁移差问题。多分辨率图像及分割、检测等下游任务验证，精度与迁移能力全面超越现有SOTA。 |


### 可信AI加速：机器学习硬件中的安全架构、隐私与韧性 (6)

Trusted AI Acceleration: Secure Architectures, Privacy, and Resilience in ML Hardware

- Session Chairs: Jack Miskelly, Stefano Di Carlo

> 随着人工智能加速器在现代计算体系中愈发不可或缺，保障其安全性与隐私性成为重中之重。本场专题研讨将剖析该领域核心难题，重点围绕侧信道安全漏洞、隐私保护计算技术以及安全深度学习硬件架构设计展开探讨。研讨议题涵盖针对XGBoost加速器的功耗攻击、面向可验证计算的高效零知识证明，以及保障客户端隐私的全同态加密（FHE）加速方案。此外，本场研讨还将介绍软硬件协同设计与轻量级可重构计算驱动的安全深度神经网络加速器，以此保护人工智能领域的知识产权。

> As AI accelerators become increasingly integral to modern computing, ensuring their security and privacy is paramount. This session explores the key challenges in this domain, focusing on side-channel vulnerabilities, privacy-preserving computation techniques, and the design of secure deep learning hardware architectures. Topics include power-based attacks on XGBoost accelerators, efficient zero-knowledge proofs for verifiable computing, and fully homomorphic encryption (FHE) acceleration for client-side privacy. Additionally, the session covers secure DNN accelerators leveraging hardware/software co-design and lightweight reconfigurable computing to protect AI intellectual property.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [利用XGBoost加速器中的功耗侧信道漏洞<br>Exploiting Power Side-Channel Vulnerabilities in XGBoost Accelerator](power_based_side_channel_attack_on_xgboost_accelerator.md) | 本文针对HLS实现的FPGA XGBoost加速器FAXID提出功耗侧信道窃取攻击。利用树节点分支判断产生差异化功耗轨迹，结合二分搜索逆向节点分割特征。Sakura-X板实测，单决策节点平均需36.7万条功耗迹即可还原模型内部特征，证实树型机器学习硬件存在严重模型提取漏洞。 |
| [zkVC：面向隐私与可验证计算的快速零知识证明<br>zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing](zkvc_fast_zero_knowledge_proof_for_private_and_verifiable_computing.md) | 本文提出zkVC高效零知识证明框架，面向矩阵乘法与Transformer推理优化。设计CRPC约束缩减电路将复杂度从O(n³)降至O(n)，搭配PS前缀求和机制进一步削减变量；对SoftMax/GELU做多项式近似。矩阵证明速度提升12倍，ViT等Transformer端到端提速超15倍，支持无可信设置Spartan后端。 |
| [ABC-FHE：支持客户端可自举参数的资源高效全同态加密加速器<br>ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption](abc_fhe_a_resource_efficient_accelerator_enabling_bootstrappable_parameters_for_client_side_fully_homomorphic_encryption.md) | 本文面向客户端CKKS同态加密，提出资源高效加速器ABC-FHE，支持自举大参数。设计可重构流式架构，融合统一在线旋转因子生成、片上PRNG与优化蒙哥马利乘法，大幅削减片外访存。28nm实测面积28.638mm²、功耗5.654W，加解密相比CPU提速千倍，超越现有客户端SOTA加速器。 |
| [SeDA：软硬件协同的安全高效DNN加速器<br>SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy](seda_secure_and_efficient_dnn_accelerators_with_hardware_software_synergy.md) | 本文提出软硬件协同安全DNN加速器SeDA，针对现有加密多AES引擎硬件开销、完整性校验海量片外访存两大痛点。设计带宽感知加密机制抵御SECA攻击，多层MAC完整性方案防御重排列攻击。在服务器、边缘NPU验证，性能开销降低12%以上，硬件面积功耗开销远低于多引擎方案。 |
| [Guarder：稳定轻量可重构的RRAM-PIM DNN知识产权保护加速器<br>Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection](guarder_a_stable_and_lightweight_reconfigurable_rram_based_pim_accelerator_for_dnn_ip_protection.md) | 本文提出软硬件协同框架Guarder，面向RRAM存内DNN加速器解决权重IP窃取与器件随机噪声两大痛点。硬件设计3T2R单元抑制编程偏差，通过可调逆变器电压构建硬件密钥；配套对比训练算法，授权芯片精度损失<2%，未授权设备输出接近随机。180nm仿真相较1T1R架构面积缩减1.41倍、能耗降低2.28倍。 |
| [Quorum：零训练无监督异常检测的量子自编码器方法<br>Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders](quorum_zero_training_unsupervised_anomaly_detection_using_quantum_autoencoders.md) | 本文提出零训练无监督量子异常检测框架Quorum，无需参数优化与梯度计算。采用振幅编码、随机量子自编码器与SWAP测试，结合分桶集成统计打分。在医疗、电力等4类数据集测试，相比训练型QNN平均F1提升23%，对含噪声量子硬件具备强鲁棒性。 |


## SEC2：硬件安全：基础与架构、设计与测试 (12)

SEC2: Hardware Security: Primitives & Architecture, Design & Test

### 处理器领域风平浪静：下一代处理器安全与飞地技术创新 (6)

All Quiet on the Processor Front: Next-Gen Processor Security and Enclave Innovations

- Session Chairs: Samuel Pagliarini, Gang Qu

> 随着计算系统复杂度持续提升，保障中央处理器与基于可信隔离区的架构安全始终是核心要务。本场硬件安全专题论坛展示了针对这类关键系统，围绕安全原语与架构增强技术展开的前沿研究。本次入选论文研究内容涵盖：采用模糊测试技术挖掘中央处理器高危漏洞、提出安全虚拟机架构实用解决方案、分析片上系统（SoC）设计中的安全资产，以及将TrustZone技术拓展应用至异构现场可编程门阵列（FPGA）架构。

> As computing systems become increasingly complex, securing CPUs and enclave-based architectures remains a top priority. This hardware security session showcases cutting-edge research on security primitives and architectural enhancements for these critical systems. The selected papers explore fuzzing-based techniques for identifying critical CPU vulnerabilities, propose practical solutions for secure virtual machine architectures, analyze security assets in System-on-Chip (SoC) designs, and extend TrustZone technology to heterogeneous FPGA architectures.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [IntraFuzz：面向Intel SGX应用的覆盖引导飞地内模糊测试<br>IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications](intrafuzz_coverage_guided_intra_enclave_fuzzing_for_intel_sgx_applications.md) | 本文提出IntraFuzz，首款完全在硬件SGX飞地内执行的覆盖率导向模糊测试框架。基于LibOS解决飞地多进程、监控隔离难题，设计共享内存通信与AEX异常捕获机制。在21款真实SGX程序实测，复现全部已知漏洞并新增6个未披露内存缺陷，平均代码覆盖率相较基线提升2.9%。 |
| [BPUFuzzer：面向RISC-V分支瞬态执行漏洞的高效模糊测试<br>BPUFuzzer: Effective Fuzz Testing for Branching Transient Execution Vulnerabilities of RISC-V CPU](bpufuzzer_effective_fuzz_testing_for_branching_transient_execution_vulnerabilities_of_risc_v_cpu.md) | 本文提出面向RISC-V处理器预硅RTL模糊测试工具BPUFuzzer，基于CFG生成含循环的完整控制流测试用例，设计BPU、RoB微架构感知的适应度与覆盖度指标引导种子筛选。在Boom v3上测试，相较SpecDoctor覆盖提升16.7%，并发现新型Spectre-Loop推测执行漏洞。 |
| [ADVeRL-ELF：利用强化学习生成对抗性ELF恶意样本<br>ADVeRL-ELF: ADVersarial ELF Malware Generation using Reinforcement Learning](adverl_elf_adversarial_elf_malware_generation_using_reinforcement_learning.md) | 本文提出A3C强化学习框架ADVeRL-ELF，面向Linux IoT的ARM ELF恶意样本生成对抗样本。依托GradCAM定位关键代码区，在.text段插入语义NOP保留程序功能，设计两类奖励函数。基于IoTPOT数据集测试，最高攻击成功率59.5%，对抗样本可绕过商用杀毒，用于加固ELF检测模型。 |
| [基于结构分析识别片上系统安全资产<br>Identifying System-on-Chip Security Assets with Structure-Based Analysis](identifying_system_on_chip_security_assets_with_structure_based_analysis.md) | 本文提出基于超流图HFG与DNN的SoC安全资产自动识别框架，解析RTL生成数据流/控制流图，提取20维结构特征向量，采用全连接DNN分类密钥、配置等安全资产。在OpenTitan、OpenPiton两款SoC验证，多类资产分类精度最高99%，二分类区分安全/非安全信号准确率94%，大幅减少人工审查工作量。 |
| [Zion：商用RISC-V处理器上的实用机密虚拟机架构<br>Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors](zion_a_practical_confidential_virtual_machine_architecture_on_commodity_risc_v_processors.md) | 本文提出Zion，一款面向商用无硬件扩展RISC-V的机密虚拟机架构。依托原生PMP/虚拟化扩展，设计短路径CVM模式、分层内存、分离页表共享机制，搭配安全/共享双vCPU降低切换开销。多类负载测试，绝大多数真实应用性能开销低于5%，兼容未修改客户机程序。 |
| [FPGA-TrustZone：面向SoC-FPGA异构架构的TrustZone安全扩展<br>FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture](fpga_trustzone_security_extension_of_trustzone_to_fpga_for_soc_fpga_heterogeneous_architecture.md) | 本文提出FPGA-TrustZone安全框架，将ARM TrustZone可信执行环境扩展至SoC-FPGA异构平台。设计FPGA安全监视器、CPU侧扩展监视器、BRAM保护三大核心组件，实现FPGA区域隔离、可信启动、AXI传输加密与BRAM存储加密。ZCU102板实测硬件资源占用低于9%，运算开销18%~23%，可抵御四类跨域攻击。 |



### 电路与秘密：新兴硬件安全原语与密码加速器 (6)

Of Circuits and Secrets: Emerging Hardware Security Primitives and Cryptographic Accelerators

- Session Chairs: Gang Qu, Qian Wang

> 随着现代硬件系统复杂度持续提升，构建稳健可靠的安全机制变得前所未有的关键。本场硬件安全专题将介绍新兴安全原语与密码加速器。本次收录论文围绕多项前沿技术展开研究：高可靠物理指纹型物理不可克隆函数（PUF）设计与波动传感技术、面向硬件安全的混合验证方案、深度神经网络（DNN）加速器的优化认证机制，以及基于存内计算（CIM）架构的新型密码加速器。

> With the increasing complexity of modern hardware systems, ensuring robust security mechanisms is more critical than ever. This session on hardware security introduces emerging security primitives and cryptographic accelerators. The featured papers explore advancements in reliable physical fingerprint-based PUF designs and fluctuation sensing, hybrid verification techniques for hardware security, optimized authentication mechanisms for deep neural network (DNN) accelerators, and novel architectures for computing-in-memory (CIM)-based cryptographic accelerators.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [AcclMT：高资源效率且灵活的Poseidon哈希默克尔树架构<br>AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture](acclmt_a_highly_resource_efficient_and_flexible_poseidon_hash_based_merkle_tree_architecture.md) | 本文提出资源高效、可灵活配置的AcclMT架构，面向ZKP场景加速Poseidon哈希默克尔树。软硬件协同设计混合全/半轮哈希引擎，搭配分层片上缓存与分层任务调度。28nm实测哈希吞吐相较FPGA方案提速14.3倍，构建默克尔树相对CPU最高提速1665倍，双哈希引擎平均利用率超95%。 |
| [LeakyDSP：利用数字信号处理块感知FPGA电压波动<br>LeakyDSP: Exploiting Digital Signal Processing Blocks to Sense Voltage Fluctuations in FPGAs](leakydsp_exploiting_digital_signal_processing_blocks_to_sense_voltage_fluctuations_in_fpgas.md) | 本文提出LeakyDSP，首个基于FPGA专用DSP块的片上电压传感电路。利用DSP内部加法器、乘法器时序延迟对电压敏感特性，串联DSP搭配IDELAY校准实现电压感知。多租户FPGA场景下可实施AES密钥CPA攻击、构建隐蔽信道，传感灵敏度与布局鲁棒性优于传统TDC基准。 |
| [FastPath：高效硬件安全验证的混合方法<br>FastPath: A Hybrid Approach for Efficient Hardware Security Verification](fastpath_a_hybrid_approach_for_efficient_hardware_security_verification.md) | 本文提出FastPath混合硬件安全验证框架，融合超流图静态分析、信息流仿真IFT、UPEC完备形式化验证三模块，自动化验证硬件数据无泄漏特性。以仿真结果划分证明空间，大幅减少人工迭代开销。在AES、RISC-V cv32e40s、BOOM等设计测试，人工工作量降低36%~100%，并发现cv32e40s未公开操作数侧信道漏洞。 |
| [Re4PUF：抗DNN与侧信道攻击的可靠可重构ReRAM PUF<br>Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks](re4puf_a_reliable_reconfigurable_reram_based_puf_resilient_to_dnn_and_side_channel_attacks.md) | 本文提出Re⁴PUF，基于3T2R分压ReRAM单元的可重构物理不可克隆函数。互补双阻单元抑制温度、读噪声误差，通过调节逆变器电压实现无重编程轻量化重构。180nm流片验证，85℃下BER仅1%，抵御MLP/Transformer建模与探针侧信道攻击，建模成功率接近随机猜测。 |
| [ACIM-QMM：面向QC-MDPC McEliece的高效模拟存内加速器<br>ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem](acim_qmm_efficient_analog_computing_in_memory_accelerator_for_qc_mdpc_mceliece_cryptosystem.md) | 本文提出基于ReRAM的模拟存内加速器ACIM-QMM，面向QC-MDPC McEliece后量子密码，解决模拟电路难以GF(2)矩阵运算难题。设计分块矩阵数据流映射与误差补偿电路，支持80~256位安全等级。相较SOTA硬件提速31.4~288.1倍，256位场景面积效率最高3.12倍、能效提升20.32倍。 |
| [AutoSkewBMT：为DNN加速器自主综合优化完整性认证机制<br>AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators](autoskewbmt_autonomously_synthesizing_optimized_integrity_authentication_mechanism_for_dnn_accelerators.md) | 本文提出AutoSkewBMT自动化工具链，面向FPGA DNN加速器优化Bonsai默克尔树(BMT)完整性认证。依托哈夫曼类设计空间探索，依据DNN瓦片访问权重倾斜BMT，提升高频计数器校验效率。AlexNet等主流网络实测哈希操作最高削减23%，相比GuardNN、TNPU性能分别提升32%、7%，硬件开销仅小幅增加。 |


## SEC3：硬件安全：攻与防 (12)

SEC3: Hardware Security: Attack & Defense


### 断路器：秘密揭晓！(6)

Circuit Breakers: Secrets Unleashed!

- Session Chairs: Michael Zuzak, Prabuddha Chakraborty

> 在如今的集成电路中，安全隐患潜藏于底层，亟待被发掘。本次DAC专题论坛带来突破性研究，揭示了ARM-FPGA片上系统与AMD Zen处理器中存在的安全漏洞。本场论坛的报告将深入剖析片上传感器漏洞利用方式、末级缓存侧信道攻击，以及零知识证明、近似神经网络、量子电路等前沿技术的完整性风险。论坛还将探讨关键防护方案，强化芯片设计以抵御各类新型威胁。诚邀各位参与这场关乎未来芯片安全的重要研讨，一同打破行业信息壁垒！

> In today's integrated circuits, security threats lurk beneath the surface, waiting to be uncovered. This DAC session presents groundbreaking research exposing vulnerabilities in ARM-FPGA SoCs and AMD Zen processors. Presentations in this session provide deep insights to the exploits of on-chip sensors, last-level cache side channels, and the integrity of innovative technologies including zero-knowledge proofs, approximate neural networks, and quantum circuits. This session will also explore vital countermeasures to strengthen designs against emerging threats. Join us in this essential dialogue on securing circuits for the future — let's break the silence together!


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [AmpereBleed：利用片上电流传感器对ARM-FPGA SoC实施无电路攻击<br>AmpereBleed: Exploiting On-chip Current Sensors for Circuit-Free Attacks on ARM-FPGA SoCs](amperebleed_exploiting_on_chip_current_sensors_for_circuit_free_attacks_on_arm_fpga_socs.md) | 本文提出AmpereBleed无定制电路侧信道攻击，利用ARM-FPGA板载INA226电流传感器与非特权hwmon接口泄露信息。突破传统RO攻击需同驻电路、波动PDN两大前提，电流采样敏感度是RO的261倍；可99.7%指纹DPU、区分RSA1024密钥汉明重量。 |
| [ZenLeak：针对AMD Zen处理器的实用末级缓存侧信道攻击*<br>ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors*](zenleak_practical_last_level_cache_side_channel_attacks_on_amd_zen_processors.md) | 本文提出ZenLeak，面向AMD Zen系列非包容性缓存的跨核LLC缓存侧信道攻击。逆向L2/L3切片与索引哈希函数，设计适配AMD的驱逐集构造算法，利用信号触发私有缓存驱逐，提出Prime+Signal+Probe攻击。在Ryzen 9 5900X攻破OpenSSL AES-T表，多轮投票密钥恢复准确率达100%。 |
| [ZK-Hammer：通过Rowhammer从零知识证明中泄露秘密<br>ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer](zk_hammer_leaking_secrets_from_zero_knowledge_proofs_via_rowhammer.md) | 本文提出ZK-Hammer，首个针对QAP类zk-SNARK的Rowhammer故障注入攻击。利用DRAM位翻转篡改证明生成阶段隐私见证，基于双线性配对推导校正项设计比特恢复算法。在libsnark范围证明场景验证，160条故障迹可泄露超80%秘密信息，上报3个对应CVE并给出算法/硬件防护方案。 |
| [用于侧信道分析的AES模式变化跨注意力方法<br>Cross-Attention for AES Mode Variation in Side-Channel Analysis](cross_attention_for_aes_mode_variation_in_side_channel_analysis.md) | 本文提出CA-SCA跨注意力侧信道分析框架，融合跨注意力与无监督域自适应UDA解决AES不同加密模式间迁移攻击难题。通过MMD损失对齐多模式功耗迹高维特征，仅单源标注数据集即可跨ECB/CBC等5类AES密钥恢复，相比现有方案所需攻击迹大幅减少，跨模式泛化能力显著领先SOTA方法。 |
| [近似神经网络对功耗侧信道攻击的安全性<br>Security of Approximate Neural Networks against Power Side-channel Attack](security_of_approximate_neural_networks_against_power_side_channel_attack.md) | 本文探究近似神经网络PE的功耗侧信道安全性，对比过频、电压缩放、位级近似三种方案。随近似程度提升功耗迹SNR显著下降，MTD成倍增长；电压缩放防护效果最优。提出SPD安全-功耗-时延综合指标，同等误差下电压缩放SPD最高，可作为轻量级抗CPA防御手段。 |
| [TetrisLock：带互锁模式的量子电路拆分编译<br>TetrisLock: Quantum Circuit Split Compilation with Interlocking Patterns](tetrislock_quantum_circuit_split_compilation_with_interlocking_patterns.md) | 本文提出TetrisLock量子电路拆分编译混淆方案，利用量子门可逆性插入成对随机门，采用交错分割模式切分电路为不等量子段子电路。各非可信编译器仅持有局部片段，抵御共谋逆向。基于RevLib测试，电路深度零增长，门数平均增20%，功能精度损失低于1%，大幅提升IP逆向复杂度。 |


### 微架构与物理攻击及防御的新前沿 (6)

New Frontiers in Microarchitectural and Physical Attacks and Defenses

- Session Chairs: Tinoosh Mohsenin, Sazadur Rahman

> 现代计算系统正面临日益严峻的微架构攻击与物理攻击威胁，针对此类攻击的防护是至关重要的研究方向。本场硬件安全专题论坛展示了面向新型威胁与防御机制的前沿研究成果。入选论文围绕微架构漏洞展开顶尖安全研究，涵盖利用时序漏洞与推测执行机制发起的攻击、功耗侧信道分析领域的技术进展，以及物理不可克隆函数（PUF）与逻辑锁定相关安全研究。

> Modern computing systems face growing threats from microarchitectural and physical attacks, address these attacks are critical areas of research. This hardware security session showcases novel research on emerging threats and defense mechanisms. The selected papers present state-of-the-art security research on microarchitectural vulnerabilities, including those exploiting timing and speculation, advancements in power side-channel analysis, and security studies on physically unclonable functions (PUFs) and logic locking.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [RAGNAR：探索RDMA网卡上的易失信道漏洞<br>RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC](ragnar_exploring_volatile_channel_vulnerabilities_on_rdma_nic.md) | 本文提出RAGNAR，一套基于RNIC硬件资源竞争的易失信道攻击套件。按四层粒度逆向CX4/5/6网卡，设计三类隐蔽信道、两类侧信道攻击。隐蔽信道带宽达PYTHIA的3.2倍，在分布式数据库、内存分离场景可指纹业务、恢复访问地址，识别精度95.6%，现有HARMONIC隔离方案无法防御。 |
| [数据无关CPU：具备微架构侧信道泄露韧性的处理器<br>Data Oblivious CPU: Micro-architectural Side-channel Leakage-Resilient Processor](data_oblivious_cpu_micro_architectural_side_channel_leakage_resilient_processor.md) | 本文提出Data Oblivious CPU安全处理器架构，基于RISC-V BOOM乱序核实现数据感知动态指令译码。通过页表敏感标记、硬件污点追踪、安全/性能双指令通路，敏感数据执行时旁路缓存、分支预测等微架构单元。FPGA实现仅增加2%硬件资源，无敏感程序性能开销为0，安全负载最高仅25%延时损失，可抵御各类微架构侧信道攻击。 |
| [“OOPS!”：针对Intel SGX与TDX的带外远程功耗侧信道攻击<br>"OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX](oops_out_of_band_remote_power_side_channel_attacks_on_intel_sgx_and_tdx.md) | 本文提出OOPS跨带远程功耗侧信道攻击，针对开启RAPL过滤防护的Intel Sapphire Rapids服务器。逆向PECI协议RdPkgConfig指令，发现PCS能量读数不受噪声过滤；设计PMC同步通道，分别从SGX窃取2048位RSA密钥、从TDX恢复AESNI密钥，证明BMC带外管理接口是新型TEE泄露面。 |
| [POLARIS：用于缓解功耗侧信道泄露的可解释人工智能<br>POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage](polaris_explainable_artificial_intelligence_for_mitigating_power_side_channel_leakage.md) | 本文提出POLARIS可解释AI硬件侧信道防护框架，无需TVLA反复仿真，采用无监督方式自动生成电路训练集，基于SHAP提取电路专属掩码规则，自适应筛选泄漏门插入掩码门。在ISCAS/EPFL等基准测试，相较VALIANT平均泄漏降幅更高，运行速度提升6倍，面积、功耗、时序开销显著降低。 |
| [SCONE：利用SMT求解与电路编码的高效逻辑锁定IP保护技术<br>SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme for Efficient Hardware IP Protection](scone_a_logic_locking_technique_utilizing_smt_solver_and_circuit_encoding_scheme_for_efficient_hardware_ip_protection.md) | 本文提出SCONE逻辑锁定方案，基于SMT求解器与安全电路编码改进SFLL-D2PIP。SMT直接提取D2PIP规避PI表NP难转换，扩展异或编码增大密钥空间，分硬件编码/设计期编码两种实现。在IBEX等电路验证，处理速度提升350倍，可抵御SAT、SPS等五类输入/结构攻击，PPA开销可控。 |
| [DeepPUFSCA：基于侧信道支持的物理不可克隆函数深度学习攻击<br>DeepPUFSCA: Deep learning for Physical Unclonable Function attack based on Side Channel Analysis support](deeppufsca_deep_learning_for_physical_unclonable_function_attack_based_on_side_channel_analysis_support.md) | 本文提出DeepPUFSCA深度学习混合攻击框架，针对宣称抗建模的4×4仲裁PUF，同时输入激励与功耗侧信道轨迹双特征。推导PUF激励、功耗与响应数学关联，双分支网络分别提取两类特征融合预测。FPGA实测最高建模准确率81.11%，相比传统机器学习提升显著，证明侧信道信息可有效强化PUF建模攻击能力。 |



## SEC4：嵌入式与跨层安全 (6)

SEC4: Embedded and Cross-Layer Security

### 突破与守护未来：系统与硬件安全新进展 (6)

Breaking & Securing the Future: Advances in System & Hardware Security

- Session Chairs: Hang Lu, Fengwei Zhang

> 随着网络威胁持续演变、硬件安全漏洞不断暴露，前沿创新解决方案正在重塑安全领域格局。本场专题研讨将深度解析系统安全与硬件抗攻击交叉领域的突破性研究成果，聚焦二者融合方向下的前沿技术探索。我们将围绕多项核心研究展开剖析：面向英特尔SGX与AMD SEV平台的新型控制流攻击防御方案、适配同态加密的优化数据打包技术（用以加速安全计算）、云端现场可编程门阵列（FPGA）中隐蔽时序信道的漏洞挖掘；除此之外，还将介绍面向物联网协议安全的高级模糊测试技术、从车载CAN总线流量中提取情报的逆向工程方法，以及适用于通用商用微控制器（MCU）的高性能控制流认证方案。参会者将全面了解正在定义安全计算未来的各类新型威胁与创新防护手段。

> As cyber threats evolve and hardware vulnerabilities emerge, pioneering solutions are reshaping the landscape of security. Join this session for a deep dive into groundbreaking research at the crossroads of system security and hardware resilience. This session explores cutting-edge research at the intersection of system security and hardware resilience. We will examine novel defenses against control flow attacks on Intel SGX and AMD SEV, optimized data packing for homomorphic encryption to accelerate secure computation, and the discovery of a covert timing channel in cloud FPGAs. Additionally, we will uncover advanced fuzzing techniques for IoT protocol security, reverse engineering methods for extracting intelligence from vehicular CAN bus traffic, and a high-performance approach to control flow attestation in commodity MCUs. Attendees will gain insights into both emerging threats and innovative countermeasures shaping the future of secure computing.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [车载CAN总线的比特级逆向工程<br>On Bit-level Reverse Engineering of Vehicular CAN Bus](on_bit_level_reverse_engineering_of_vehicular_can_bus.md) | 本文提出一套比特级车载CAN总线逆向框架，通过稳态/工况双采集、比特翻转率信号划分、关联ID筛选、定向模糊与控制比特解析实现CAN报文-车辆控制动作精准映射。在特斯拉Model 3、零跑C10/C11验证，单车型识别43类控制行为，树莓派即可轻量化部署，资源开销极低。 |
| [HoBBy：加固Intel SGX与AMD SEV中不平衡分支以抵御控制流攻击<br>HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV](hobby_hardening_unbalanced_branches_against_control_flow_attacks_on_intel_sgx_and_amd_sev.md) | 本文基于LLVM提出编译器加固工具HoBBy，面向SGX/AMD SEV可信区，在指令层平衡密钥相关分支。设计单步污点分析定位不平衡代码，配套指令/数据影子、齿化、螺旋技术统一两路指令、访存、PC特征。密码库运行开销仅2.8%，二进制膨胀0.6%，可将三类前沿控制流攻击成功率降至随机猜测水平。 |
| [CMFuzz：通过配置模型识别与调度实现IoT协议并行模糊测试<br>CMFuzz: Parallel Fuzzing of IoT Protocols by Configuration Model Identification and Scheduling](cmfuzz_parallel_fuzzing_of_iot_protocols_by_configuration_model_identification_and_scheduling.md) | 本文提出CMFUZZ并行物联网协议模糊测试框架，新增配置模型维度。自动提取各类配置并量化参数依赖关系，基于权重聚类分配并行实例。在MQTT、CoAP等6款IoT协议验证，相较Peach、SPFuzz分支覆盖率平均提升34.4%、28.5%，发现14个全新高危漏洞。 |
| [面向云FPGA的新型隐蔽时序信道<br>A Novel Covert Timing Channel for Cloud FPGAs](a_novel_covert_timing_channel_for_cloud_fpgas.md) | 本文提出面向云FPGA的新型隐蔽时序信道，分两阶段窃取加密功耗数据。第一阶段篡改AXI握手时序实现FPGA向vCPU隐传；第二阶段操纵UDP包间隔跨云外传。搭载LDPC最小和解码降低误码，AWS F1实测最低BER仅0.01988，可完成远程功耗分析窃取AES密钥。 |
| [RAP-Track：通过并行跟踪在商用MCU上实现高效控制流认证<br>RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs](rap_track_efficient_control_flow_attestation_via_parallel_tracking_in_commodity_mcus.md) | 本文提出RAP-Track，面向商用ARM Cortex-M MCU的并行控制流认证方案。复用片上MTB、DWT追踪硬件与TrustZone，离线静态划分代码区、插入跳转跳板，仅记录非确定分支。相比主流TEE插桩方案运行开销大幅降低，日志体积可控，可抵御ROP/JOP代码复用攻击，原型开源可部署。 |
| [BFV方案中通用矩阵乘法的增强数据打包方法<br>An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme](an_enhanced_data_packing_method_for_general_matrix_multiplication_in_brakerski_fan_vercauteren_scheme.md) | 本文面向BFV同态加密下GEMM计算瓶颈，提出增强多项式打包方案，适配CNN卷积/全连接层，搭配FPGA专用硬件与异构调度。该方案充分利用多项式系数空间、分块处理大矩阵，U250平台实测MNIST、CIFAR推理相较SOTA分别提速4.22×、3.99×，同时提升模型推理精度、缩减密文存储体积。 |
