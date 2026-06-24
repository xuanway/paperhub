# Security · DAC 2025 (42)

本分类收录 DAC 2025（第62届）Track "Security" 的论文。


## SEC1: 人工智能/机器学习安全与隐私 (12)

SEC1: AI/ML Security/Privacy


### AI遭遇攻击：提升机器学习系统的隐私性、鲁棒性和可信度 (6)

AI Under Attack: Enhancing Privacy, Robustness, and Trust in ML Systems

- Session Chairs: Adnan Siraj Rakin, Ayesha Siddique

> 随着人工智能技术飞速发展，完善可靠的安全防护措施对于降低风险、保护敏感数据至关重要。本次论坛聚焦人工智能安全与隐私保护领域的前沿研究，针对各类机器学习范式下涌现的新型威胁与创新防御方案展开探讨。研讨主题涵盖嵌入式设备上具备抗攻击能力的联邦学习、依托机器遗忘技术实现的隐蔽后门攻击，以及适用于入侵检测系统的持续异常识别技术。本次论坛同时介绍图神经网络的安全推理、保护隐私的协同学习，以及无数据知识蒸馏技术的最新进展。

> With the rapid evolution of AI technologies, ensuring robust security measures is crucial to mitigating risks and safeguarding sensitive data. This session explores cutting-edge research in AI security and privacy, addressing emerging threats and novel defenses across various machine learning paradigms. Topics include resilient federated learning on embedded devices, concealed backdoor attacks using machine unlearning, and continual novelty detection for intrusion detection systems. The session also covers secure inference of graph neural networks, privacy-preserving collaborative learning, and advancements in data-free knowledge distillation.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [Resilient Federated Learning on Embedded Devices with Constrained Network Connectivity](resilient_federated_learning_on_embedded_devices_with_constrained_network_connectivity.md) | Federated learning, Resilience, Adaptive (联邦学习、鲁棒性、自适应)|
| [ReVeil: Unconstrained Concealed Backdoor Attack on Deep Neural Networks using Machine Unlearning](reveil_unconstrained_concealed_backdoor_attack_on_deep_neural_networks_using_machine_unlearning.md) | Deep Neural Networks, Backdoor Attacks, Machine Unlearning, Concealed Backdoor (深度神经网络，后门攻击，机器遗忘，隐蔽后门)|
| [CND-IDS: Continual Novelty Detection for Intrusion Detection Systems](cnd_ids_continual_novelty_detection_for_intrusion_detection_systems.md) | SEC1: AI/ML Security/Privacy |
| [Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment](graph_in_the_vault_protecting_edge_gnn_inference_with_trusted_execution_environment.md) | SEC1: AI/ML Security/Privacy |
| [Ensembler: Protect Collaborative Inference Privacy from Model Inversion Attack via Selective Ensemble](ensembler_protect_collaborative_inference_privacy_from_model_inversion_attack_via_selective_ensemble.md) | SEC1: AI/ML Security/Privacy |
| [CAE-DFKD: Bridging the Transferability Gap in Data-Free Knowledge Distillation](cae_dfkd_bridging_the_transferability_gap_in_data_free_knowledge_distillation.md) | SEC1: AI/ML Security/Privacy |


### 可信AI加速：机器学习硬件中的安全架构、隐私与韧性 (6)

Trusted AI Acceleration: Secure Architectures, Privacy, and Resilience in ML Hardware

- Session Chairs: Jack Miskelly, Stefano Di Carlo

> 随着人工智能加速器在现代计算体系中愈发不可或缺，保障其安全性与隐私性成为重中之重。本场专题研讨将剖析该领域核心难题，重点围绕侧信道安全漏洞、隐私保护计算技术以及安全深度学习硬件架构设计展开探讨。研讨议题涵盖针对XGBoost加速器的功耗攻击、面向可验证计算的高效零知识证明，以及保障客户端隐私的全同态加密（FHE）加速方案。此外，本场研讨还将介绍软硬件协同设计与轻量级可重构计算驱动的安全深度神经网络加速器，以此保护人工智能领域的知识产权。

> As AI accelerators become increasingly integral to modern computing, ensuring their security and privacy is paramount. This session explores the key challenges in this domain, focusing on side-channel vulnerabilities, privacy-preserving computation techniques, and the design of secure deep learning hardware architectures. Topics include power-based attacks on XGBoost accelerators, efficient zero-knowledge proofs for verifiable computing, and fully homomorphic encryption (FHE) acceleration for client-side privacy. Additionally, the session covers secure DNN accelerators leveraging hardware/software co-design and lightweight reconfigurable computing to protect AI intellectual property.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [Power-Based Side-Channel Attack on XGBoost Accelerator](power_based_side_channel_attack_on_xgboost_accelerator.md) | SEC1: AI/ML Security/Privacy |
| [zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing](zkvc_fast_zero_knowledge_proof_for_private_and_verifiable_computing.md) | SEC1: AI/ML Security/Privacy |
| [ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption](abc_fhe_a_resource_efficient_accelerator_enabling_bootstrappable_parameters_for_client_side_fully_homomorphic_encryption.md) | SEC1: AI/ML Security/Privacy |
| [SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy](seda_secure_and_efficient_dnn_accelerators_with_hardware_software_synergy.md) | SEC1: AI/ML Security/Privacy |
| [Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection](guarder_a_stable_and_lightweight_reconfigurable_rram_based_pim_accelerator_for_dnn_ip_protection.md) | SEC1: AI/ML Security/Privacy |
| [Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders](quorum_zero_training_unsupervised_anomaly_detection_using_quantum_autoencoders.md) | SEC1: AI/ML Security/Privacy |


## SEC2：硬件安全：基础与架构、设计与测试 (12)

SEC2: Hardware Security: Primitives & Architecture, Design & Test

### 处理器领域风平浪静：下一代处理器安全与飞地技术创新 (6)

All Quiet on the Processor Front: Next-Gen Processor Security and Enclave Innovations

- Session Chairs: Samuel Pagliarini, Gang Qu

> 随着计算系统复杂度持续提升，保障中央处理器与基于可信隔离区的架构安全始终是核心要务。本场硬件安全专题论坛展示了针对这类关键系统，围绕安全原语与架构增强技术展开的前沿研究。本次入选论文研究内容涵盖：采用模糊测试技术挖掘中央处理器高危漏洞、提出安全虚拟机架构实用解决方案、分析片上系统（SoC）设计中的安全资产，以及将TrustZone技术拓展应用至异构现场可编程门阵列（FPGA）架构。

> As computing systems become increasingly complex, securing CPUs and enclave-based architectures remains a top priority. This hardware security session showcases cutting-edge research on security primitives and architectural enhancements for these critical systems. The selected papers explore fuzzing-based techniques for identifying critical CPU vulnerabilities, propose practical solutions for secure virtual machine architectures, analyze security assets in System-on-Chip (SoC) designs, and extend TrustZone technology to heterogeneous FPGA architectures.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications](intrafuzz_coverage_guided_intra_enclave_fuzzing_for_intel_sgx_applications.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [BPUFuzzer: Effective Fuzz Testing for Branching Transient Execution Vulnerabilities of RISC-V CPU](bpufuzzer_effective_fuzz_testing_for_branching_transient_execution_vulnerabilities_of_risc_v_cpu.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [ADVeRL-ELF: ADVersarial ELF Malware Generation using Reinforcement Learning](adverl_elf_adversarial_elf_malware_generation_using_reinforcement_learning.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [Identifying System-on-Chip Security Assets with Structure-Based Analysis](identifying_system_on_chip_security_assets_with_structure_based_analysis.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors](zion_a_practical_confidential_virtual_machine_architecture_on_commodity_risc_v_processors.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture](fpga_trustzone_security_extension_of_trustzone_to_fpga_for_soc_fpga_heterogeneous_architecture.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |



### 电路与秘密：新兴硬件安全原语与密码加速器 (6)

Of Circuits and Secrets: Emerging Hardware Security Primitives and Cryptographic Accelerators

- Session Chairs: Gang Qu, Qian Wang

> 随着现代硬件系统复杂度持续提升，构建稳健可靠的安全机制变得前所未有的关键。本场硬件安全专题将介绍新兴安全原语与密码加速器。本次收录论文围绕多项前沿技术展开研究：高可靠物理指纹型物理不可克隆函数（PUF）设计与波动传感技术、面向硬件安全的混合验证方案、深度神经网络（DNN）加速器的优化认证机制，以及基于存内计算（CIM）架构的新型密码加速器。

> With the increasing complexity of modern hardware systems, ensuring robust security mechanisms is more critical than ever. This session on hardware security introduces emerging security primitives and cryptographic accelerators. The featured papers explore advancements in reliable physical fingerprint-based PUF designs and fluctuation sensing, hybrid verification techniques for hardware security, optimized authentication mechanisms for deep neural network (DNN) accelerators, and novel architectures for computing-in-memory (CIM)-based cryptographic accelerators.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture](acclmt_a_highly_resource_efficient_and_flexible_poseidon_hash_based_merkle_tree_architecture.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [LeakyDSP: Exploiting Digital Signal Processing Blocks to Sense Voltage Fluctuations in FPGAs](leakydsp_exploiting_digital_signal_processing_blocks_to_sense_voltage_fluctuations_in_fpgas.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [FastPath: A Hybrid Approach for Efficient Hardware Security Verification](fastpath_a_hybrid_approach_for_efficient_hardware_security_verification.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks](re4puf_a_reliable_reconfigurable_reram_based_puf_resilient_to_dnn_and_side_channel_attacks.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem](acim_qmm_efficient_analog_computing_in_memory_accelerator_for_qc_mdpc_mceliece_cryptosystem.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |
| [AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators](autoskewbmt_autonomously_synthesizing_optimized_integrity_authentication_mechanism_for_dnn_accelerators.md) | SEC2: Hardware Security: Primitives & Architecture, Design & Test |


## SEC3：硬件安全：攻与防 (12)

SEC3: Hardware Security: Attack & Defense


### 断路器：秘密揭晓！(6)

Circuit Breakers: Secrets Unleashed!

- Session Chairs: Michael Zuzak, Prabuddha Chakraborty

> 在如今的集成电路中，安全隐患潜藏于底层，亟待被发掘。本次DAC专题论坛带来突破性研究，揭示了ARM-FPGA片上系统与AMD Zen处理器中存在的安全漏洞。本场论坛的报告将深入剖析片上传感器漏洞利用方式、末级缓存侧信道攻击，以及零知识证明、近似神经网络、量子电路等前沿技术的完整性风险。论坛还将探讨关键防护方案，强化芯片设计以抵御各类新型威胁。诚邀各位参与这场关乎未来芯片安全的重要研讨，一同打破行业信息壁垒！

> In today's integrated circuits, security threats lurk beneath the surface, waiting to be uncovered. This DAC session presents groundbreaking research exposing vulnerabilities in ARM-FPGA SoCs and AMD Zen processors. Presentations in this session provide deep insights to the exploits of on-chip sensors, last-level cache side channels, and the integrity of innovative technologies including zero-knowledge proofs, approximate neural networks, and quantum circuits. This session will also explore vital countermeasures to strengthen designs against emerging threats. Join us in this essential dialogue on securing circuits for the future — let's break the silence together!


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [AmpereBleed: Exploiting On-chip Current Sensors for Circuit-Free Attacks on ARM-FPGA SoCs](amperebleed_exploiting_on_chip_current_sensors_for_circuit_free_attacks_on_arm_fpga_socs.md) | SEC3: Hardware Security: Attack & Defense |
| [ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors*](zenleak_practical_last_level_cache_side_channel_attacks_on_amd_zen_processors.md) | SEC3: Hardware Security: Attack & Defense |
| [ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer](zk_hammer_leaking_secrets_from_zero_knowledge_proofs_via_rowhammer.md) | SEC3: Hardware Security: Attack & Defense |
| [Cross-Attention for AES Mode Variation in Side-Channel Analysis](cross_attention_for_aes_mode_variation_in_side_channel_analysis.md) | SEC3: Hardware Security: Attack & Defense |
| [Security of Approximate Neural Networks against Power Side-channel Attack](security_of_approximate_neural_networks_against_power_side_channel_attack.md) | SEC3: Hardware Security: Attack & Defense |
| [TetrisLock: Quantum Circuit Split Compilation with Interlocking Patterns](tetrislock_quantum_circuit_split_compilation_with_interlocking_patterns.md) | SEC3: Hardware Security: Attack & Defense |


### 微架构与物理攻击及防御的新前沿 (6)

New Frontiers in Microarchitectural and Physical Attacks and Defenses

- Session Chairs: Tinoosh Mohsenin, Sazadur Rahman

> 现代计算系统正面临日益严峻的微架构攻击与物理攻击威胁，针对此类攻击的防护是至关重要的研究方向。本场硬件安全专题论坛展示了面向新型威胁与防御机制的前沿研究成果。入选论文围绕微架构漏洞展开顶尖安全研究，涵盖利用时序漏洞与推测执行机制发起的攻击、功耗侧信道分析领域的技术进展，以及物理不可克隆函数（PUF）与逻辑锁定相关安全研究。

> Modern computing systems face growing threats from microarchitectural and physical attacks, address these attacks are critical areas of research. This hardware security session showcases novel research on emerging threats and defense mechanisms. The selected papers present state-of-the-art security research on microarchitectural vulnerabilities, including those exploiting timing and speculation, advancements in power side-channel analysis, and security studies on physically unclonable functions (PUFs) and logic locking.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC](ragnar_exploring_volatile_channel_vulnerabilities_on_rdma_nic.md) | SEC3: Hardware Security: Attack & Defense |
| [Data Oblivious CPU: Micro-architectural Side-channel Leakage-Resilient Processor](data_oblivious_cpu_micro_architectural_side_channel_leakage_resilient_processor.md) | SEC3: Hardware Security: Attack & Defense |
| ["OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX](oops_out_of_band_remote_power_side_channel_attacks_on_intel_sgx_and_tdx.md) | SEC3: Hardware Security: Attack & Defense |
| [POLARIS: Explainable Artificial Intelligence for Mitigating Power Side-Channel Leakage](polaris_explainable_artificial_intelligence_for_mitigating_power_side_channel_leakage.md) | SEC3: Hardware Security: Attack & Defense |
| [SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme for Efficient Hardware IP Protection](scone_a_logic_locking_technique_utilizing_smt_solver_and_circuit_encoding_scheme_for_efficient_hardware_ip_protection.md) | SEC3: Hardware Security: Attack & Defense |
| [DeepPUFSCA: Deep learning for Physical Unclonable Function attack based on Side Channel Analysis support](deeppufsca_deep_learning_for_physical_unclonable_function_attack_based_on_side_channel_analysis_support.md) | SEC3: Hardware Security: Attack & Defense |



## SEC4：嵌入式与跨层安全 (6)

SEC4: Embedded and Cross-Layer Security

### 突破与守护未来：系统与硬件安全新进展 (6)

Breaking & Securing the Future: Advances in System & Hardware Security

- Session Chairs: Hang Lu, Fengwei Zhang

> 随着网络威胁持续演变、硬件安全漏洞不断暴露，前沿创新解决方案正在重塑安全领域格局。本场专题研讨将深度解析系统安全与硬件抗攻击交叉领域的突破性研究成果，聚焦二者融合方向下的前沿技术探索。我们将围绕多项核心研究展开剖析：面向英特尔SGX与AMD SEV平台的新型控制流攻击防御方案、适配同态加密的优化数据打包技术（用以加速安全计算）、云端现场可编程门阵列（FPGA）中隐蔽时序信道的漏洞挖掘；除此之外，还将介绍面向物联网协议安全的高级模糊测试技术、从车载CAN总线流量中提取情报的逆向工程方法，以及适用于通用商用微控制器（MCU）的高性能控制流认证方案。参会者将全面了解正在定义安全计算未来的各类新型威胁与创新防护手段。

> As cyber threats evolve and hardware vulnerabilities emerge, pioneering solutions are reshaping the landscape of security. Join this session for a deep dive into groundbreaking research at the crossroads of system security and hardware resilience. This session explores cutting-edge research at the intersection of system security and hardware resilience. We will examine novel defenses against control flow attacks on Intel SGX and AMD SEV, optimized data packing for homomorphic encryption to accelerate secure computation, and the discovery of a covert timing channel in cloud FPGAs. Additionally, we will uncover advanced fuzzing techniques for IoT protocol security, reverse engineering methods for extracting intelligence from vehicular CAN bus traffic, and a high-performance approach to control flow attestation in commodity MCUs. Attendees will gain insights into both emerging threats and innovative countermeasures shaping the future of secure computing.


| 中英论文题目 | 中英关键词 |
|------------|-----------|
| [On Bit-level Reverse Engineering of Vehicular CAN Bus](on_bit_level_reverse_engineering_of_vehicular_can_bus.md) | SEC4: Embedded and Cross-Layer Security |
| [HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV](hobby_hardening_unbalanced_branches_against_control_flow_attacks_on_intel_sgx_and_amd_sev.md) | SEC4: Embedded and Cross-Layer Security |
| [CMFuzz: Parallel Fuzzing of IoT Protocols by Configuration Model Identification and Scheduling](cmfuzz_parallel_fuzzing_of_iot_protocols_by_configuration_model_identification_and_scheduling.md) | SEC4: Embedded and Cross-Layer Security |
| [A Novel Covert Timing Channel for Cloud FPGAs](a_novel_covert_timing_channel_for_cloud_fpgas.md) | SEC4: Embedded and Cross-Layer Security |
| [RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs](rap_track_efficient_control_flow_attestation_via_parallel_tracking_in_commodity_mcus.md) | SEC4: Embedded and Cross-Layer Security |
| [An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme](an_enhanced_data_packing_method_for_general_matrix_multiplication_in_brakerski_fan_vercauteren_scheme.md) | SEC4: Embedded and Cross-Layer Security |
