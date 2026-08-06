# EDA · DAC 2025 (113)

本分类收录 DAC 2025（第62届）Track "EDA" 的论文。


## EDA1：片上系统与2.5D/3D系统级封装设计方法 (8)

EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package

### 探索未知领域：从芯粒到架构设计与验证 (8)

Exploring the Unchartered: From Chiplets to Architecture and Validation

- Session Chairs: Giuseppe Di Guglielmo, T V Narayanan

> 欢迎来到“探索未知领域”专题会议，本次会议聚焦突破系统探索、设计与验证边界的前沿开创性研究。会议汇集多项创新方案：借助机器学习与人工智能开展多现场可编程门阵列布线及设计空间探索，针对特定工作负载定制片上系统参数；或是以缓存层级与芯粒间互联网络为核心优化多芯粒系统。本次专题还将介绍适用于三维集成系统的多维度物理仿真验证方法、基于Gem5的新型加速器集成方案，以及通过优化指令解码器提升指令集仿真器仿真速度的相关技术。

> Welcome to the session "Explore the Uncharted," diving into pioneering research that pushes the boundaries of system exploration, design and validation. This session brings together innovative approaches for multi-FPGA routing and design space exploration leveraging machine learning and AI to tailor system-on-chip (SoC) parameters to specific workloads; or optimizing multi-chiplet systems, focusing on cache hierarchies and inter-chiplet networks. The session offers validation methods for 3D integrated systems using physics-based multi-faceted simulation, novel Gem5-based accelerator integration opportunities, as well as speeding up ISS simulations through optimized instruction decoders.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [Gem5-AcceSys：支持新型加速器标准互连的系统级探索<br>Gem5-AcceSys: Enabling System-Level Exploration of Standard Interconnects for Novel Accelerators](gem5_accesys_enabling_system_level_exploration_of_standard_interconnects_for_novel_accelerators.md) | 本文基于Gem5扩展Gem5-AcceSys系统仿真框架，原生集成PCIe、SMMU、DMA与异构内存架构，支持RTL/C++两类加速器建模。以Transformer矩阵脉动加速器为测试载体，量化PCIe带宽、包长、主/设备内存对性能影响，给出GEMM/非GEMM workload架构选型阈值，为异构加速器协同设计提供量化依据。 |
| [Adora编译器：面向CGRA高效数据流加速与任务流水的端到端优化<br>Adora Compiler: End-to-End Optimization for High-Efficiency Dataflow Acceleration and Task Pipelining on CGRAs](adora_compiler_end_to_end_optimization_for_high_efficiency_dataflow_acceleration_and_task_pipelining_on_cgras.md) | 本文提出面向CGRA的端到端Adora编译器，基于MLIR与多面体分析，分数据流、任务流两层定制优化，配套快速帕累托寻优算法。支持C/PyTorch/TensorFlow输入，适配RISC-V+CGRA异构SoC。Polybench与AI模型测试表明，相比NSGA-II搜索提速6倍，低功耗CGRA单核算力接近高端CPU，边缘推理能效优势显著。 |
| [基于信息论决策树构造算法的不规则指令集解码器自动生成<br>Automated Generation of Decoders for Irregular Instruction Sets Using Information-Theoretic Decision Trees Construction Algorithms](automated_generation_of_decoders_for_irregular_instruction_sets_using_information_theoretic_decision_trees_construction_algorithms.md) | 本文提出基于信息论决策树的不规则指令集解码器自动生成算法，支持带字段不等式、嵌套特化的ARMv7/MIPS32/SPARC复杂ISA。定义掩码/条件两类决策函数，采用卡方、基尼、熵、信息增益四大分裂指标，分单/多掩码两种构造模式，生成解码器功能完备、译码速度优于主流同类生成方案。 |
| [跃迁前先审视：一种面向受约束高维设计空间探索的自审视贝叶斯优化方法<br>Look Before You Leap: A Self-Review Bayesian Optimization Method for Constrained High-Dimensional Design Space Exploration](look_before_you_leap_a_self_review_bayesian_optimization_method_for_constrained_high_dimensional_design_space_exploration.md) | 本文提出SRBO自检视贝叶斯优化框架，面向含时序约束的RISC-V高维DSE。在局部BO基础上引入师生模型降低代理误差，深度集成多分类器过滤不可行候选。基于BOOM、Rocket两款RISC-V核心测试，同等时间下超体积相较SOTA最高提升41.47倍，能有效规避局部最优、减少无效仿真。 |
| [基于阶段增强贝叶斯优化的高性能计算架构探索<br>High-Performance Computing Architecture Exploration with Stage-Enhanced Bayesian Optimization](high_performance_computing_architecture_exploration_with_stage_enhanced_bayesian_optimization.md) | 本文提出三阶段增强贝叶斯优化算法SEBO，面向7nm Arm Neoverse V1多核处理器PPA多目标架构探索。采用Hammersley转导采样、多核集成信任域高斯代理、并行批量NEHVI采集函数，搭配VPSim+改良McPAT仿真流。STREAM等HPC基准测试，帕累托超体积优于SOTA 1~7%，解集多样性提升最高24%，运行效率翻倍。 |
| [多芯粒系统缓存体系的设计空间探索<br>On Design Space Exploration of Cache System in Multi-Chiplet Systems](on_design_space_exploration_of_cache_system_in_multi_chiplet_systems.md) | 本文面向多芯粒众核系统缓存层级设计空间探索，构建缓存图与芯粒互联拓扑双图模型，基于C-AMAT建立时延、功耗、成本解析模型，提出双层优化算法。交替求解缓存、互联网络子问题，PARSEC等负载测试，相较Zen4、SPR、IntLP执行时间平均分别降低39.7%、39.2%、25.91%。 |
| [从平地到森林：通过RTL层次树探索帕累托最优设计<br>From Flatland to Forest: Exploring Pareto-optimal Design through RTL Hierarchy Trees](from_flatland_to_forest_exploring_pareto_optimal_design_through_rtl_hierarchy_trees.md) | 本文提出基于RTL层次树的微架构DSE框架，摒弃传统扁平参数向量建模，设计加权WL子树核量化硬件结构相似度，搭配核K-means聚类实现并行采样。理论证明该方法样本复杂度优于RBF核；Gemmini RISC-V SoC测试，超体积指标相较SOTA最高提升29.3%，聚类大幅缩短评估耗时。 |
| [面向多FPGA系统的协同裸片级路由器与时分复用优化<br>Synergistic Die-Level Router for Multi-FPGA System with Time-Division Multiplexing Optimization](synergistic_die_level_router_for_multi_fpga_system_with_time_division_multiplexing_optimization.md) | 本文面向时分复用多FPGA系统提出协同裸片级布线器，分均衡初布线、拉格朗日TDM分配两大阶段。设计时延-拥塞平衡寻路、多线程松弛求解、余量感知合法化算法。2023裸片路由竞赛基准测试，相较SOTA关键连接时延降低7.6%，运行速度提升5.761倍。 |
## EDA2：设计验证与确认 (16)

EDA2: Design Verification and Validation

### 探索用于验证与确认的形式化前沿技术 (8)

Exploring the Formal Frontier for Verification and Validation

- Session Chairs: Namrata Shekhar, Enrico Fraccaroli

> 本次分会场聚焦形式化验证领域前沿研究，助力研发适配现代系统验证、效率更高且可靠性更强的工具。内容涵盖各类前沿技术方案，包括高效可满足性问题求解器、符号模型检测与逻辑优化技术，旨在提升验证流程的精准度、可拓展性与自动化水平。现场宣读的论文深入探讨多项创新成果，例如用于子电路识别的混合算法、可满足性模理论计数技术以及证明义务精化方法，展示了应对复杂验证难题的全新研究方向。

> This session presents the forefront of research in formal verification, driving forward the development of more efficient and reliable tools for modern system validation. It covers cutting-edge approaches, including efficient SAT solvers, symbolic model checking, and logic optimization, aimed at improving the accuracy, scalability, and automation of verification processes. Papers presented delve into innovations like hybrid algorithms for subcircuit identification, SMT counting, and proof obligation refinement, highlighting new frontiers in tackling complex verification challenges.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [面向最优功能ECO补丁生成的高效修正信号验证<br>Efficient Rectification Signal Validation for Optimal Functional ECO Patch Generation](efficient_rectification_signal_validation_for_optimal_functional_eco_patch_generation.md) | 本文面向功能ECO补丁优化，提出高效修正信号验证算法。通过量词消去构造近似证明模型，将2QBF问题转化高效1QBF求解；设计可疑得分筛选候选、信号集分组排序与模拟退火早停策略。CAD竞赛基准测试，相较Cadence商用Conformal ECO，补丁规模平均缩减44%，仅需少量补丁生成调用即可得到最优解。 |
| [X-SAT：一种高效的电路型SAT求解器<br>X-SAT: An Efficient Circuit-Based SAT Solver](x_sat_an_efficient_circuit_based_sat_solver.md) | 本文提出面向算术电路的电路型SAT求解器X-SAT。设计结构消元算法将AIG转为XLG图大幅缩减变量，改进VSIDS得到XVSIDS分支策略适配异或密集电路。在算术、非算术两类基准测试，算术电路PAR2相较Kissat提升1.36倍，优于现有电路求解器abc-cirsat 38.26倍，综合求解效率领先。 |
| [超越离散域的近似SMT计数<br>Approximate SMT Counting Beyond Discrete Domains](approximate_smt_counting_beyond_discrete_domains.md) | 本文提出pact混合SMT近似模型计数工具，支持离散+连续变量混合公式，基于哈希分块实现带(ε,δ)理论保证的投影计数。设计三类成对独立哈希，采用对数级SMT调用策略。在14202组SMT基准上，pact求解603例，基线仅13例，最大可计数1.7×10¹9组解，平均相对误差仅3.3%。 |
| [利用关键证明义务实现高效IC3验证<br>Leveraging Critical Proof Obligations for Efficient IC3 Verification](leveraging_critical_proof_obligations_for_efficient_ic3_verification.md) | 本文提出关键证明义务CPO概念，配套两套IC3优化技术：CPO驱动UNSAT核心生成、CPO导向证明义务传播。基于IC3ref、MCer两套求解器实现，在786个HWMCC基准测试，优化后多解决15~20例，CPO识别率、引理传播成功率显著提升，大幅缩短硬件安全模型校验耗时。 |
| [面向LTL的属性驱动并行符号模型检测<br>Property-driven Parallel Symbolic Model Checking of LTL](property_driven_parallel_symbolic_model_checking_of_ltl.md) | 本文提出面向完整LTL的属性驱动并行符号模型检查算法PPSMC，基于公平状态标记拆分嵌套不动点计算，以Büchi自动机状态分配并行工作线程，配套自动扩并行度与任务窃取负载均衡策略。32核环境下相较串行版本加速2.81~17.19倍，对比并行BDD库方案平均提升33.1%，优于显式并行工具LTSmin。 |
| [RE3：基于关系映射抽象的精化关系发现<br>RE3: Finding Refinement Relations with Relational Mapping Abstraction](re3_finding_refinement_relations_with_relational_mapping_abstraction.md) | 本文提出RE3非周期精确时序等价检查算法，基于关系映射抽象RMA与IC3框架，联合调度函数与粘合不变式自动生成精炼关系。自对齐仿真过滤坏状态，可输出可读关系迁移图。基准测试相较SE3不变式规模平均缩减69%，非等价案例求解速度优于SE3，可辅助LLM生成RTL错误定位修复。 |
| [逻辑优化遇见SAT：一种新型电路SAT求解框架<br>Logic Optimization Meets SAT: A Novel Framework for Circuit-SAT Solving](logic_optimization_meets_sat_a_novel_framework_for_circuit_sat_solving.md) | 本文面向电路可满足性CSAT提出EDA协同预处理框架，将逻辑综合建模为强化学习MDP，设计以SAT分支复杂度为目标的定制LUT映射。工业LEC/ATPG基准测试，搭配Kissat、CaDiCaL求解器，总求解时长最高降低63%，可无缝兼容主流CDCL SAT工具。 |
| [H3Match：一种用于子电路识别的混合异构超图匹配方法<br>H3Match: A Hybrid Heterogeneous Hypergraph Matching Method for Subcircuit Identification](h3match_a_hybrid_heterogeneous_hypergraph_matching_method_for_subcircuit_identification.md) | 本文提出混合异构超图匹配框架H3Match用于晶体管级子电路识别。设计电路异构超图表征降低冗余，将匹配简化为有向DAG匹配，采用有向HGNN做近似过滤实现零漏检；构建MINLP精确验证并利用近似结果加速。工业晶体管电路测试，近似精度超98.5%，精确验证提速4.16倍，端到端整体提速7.08倍。 |
### 验证与综合技术未来的规模化拓展、算法学习及并行化实现 (8)

Scaling, Learning, and Parallelizing the Future of Verification and Synthesis

- Session Chairs: Chung-Yang Ric Huang, Nan Wu

> 本场会议研讨设计验证与确认领域的前沿方法，重点围绕可扩展、并行化及基于学习的技术路线展开。宣讲论文涵盖多项创新技术，包括基于图形处理器加速的寄存器传输级仿真、用于片上网络验证的模糊测试框架，以及面向逻辑综合的多智能体引导优化算法。本次研讨聚焦仿真、规模扩展与并行处理相关技术，所展示的研究成果突破了现代验证技术的现有局限，攻克了多项复杂难题，为大规模芯片设计提供了更高效、自动化的解决方案。

> This session explores advanced methods in the verification and validation of design, focusing on scalable, parallel, and learning-driven approaches. Papers presented cover innovations such as GPU-accelerated RTL simulation, fuzzing frameworks for network-on-chip verification, and multi-agent guided optimization for logic synthesis. With a focus on simulation, scaling, and parallelization, the research presented pushes the boundaries of modern verification practices, addressing complex challenges and offering more efficient, automated solutions for large-scale designs.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [InterConFuzz：基于模糊测试的综合NoC验证框架<br>InterConFuzz: A Fuzzing-based Comprehensive NoC Verification Framework](interconfuzz_a_fuzzing_based_comprehensive_noc_verification_framework.md) | 本文提出基于UVM的混合模糊验证框架InterConFuzz，融合覆盖率制导模糊测试与符号执行，通过CFG检查点局部复位减少仿真开销。在OpenTitan TL-UL NoC中检出5类安全漏洞，较SeVNoC多发现3个；内存、算力开销分别降低24.4%、29.5%，覆盖率与主流NoC模糊工具NoCFuzzer持平。 |
| [面向智能体导向测试生成的多核环境状态表征<br>Multicore Environment State Representation for Agent-Directed Test Generation](multicore_environment_state_representation_for_agent_directed_test_generation.md) | 本文面向多核共享存储验证，提出一种基于执行见证的强化学习环境状态表征方案。复用读-写依赖关系定义多核执行见证，设计唯一数值签名编码观测，采用定长动作-观测历史近似马尔可夫状态。基于16/32核MOESI架构测试，相较MTG、RLG等主流方法，收敛速度更快、故障检出耗时大幅缩短。 |
| [GSIM：大规模设计RTL仿真加速<br>GSIM: Accelerating RTL Simulation for Large-Scale Designs](simax_accelerating_rtl_simulation_for_large_scale_design.md) | 本文提出三层优化的RTL仿真器GSIM，从超节点、节点、比特粒度针对四类仿真开销设计优化，改进图划分算法平衡激活开销与活动因子。基于Firrtl编译输出C++仿真代码，可完整仿真香山处理器，相较Verilator最高提速19.94倍，远超ESSENT、Arcilator等同类工具。 |
| [从对错中洞察：用于解决RTL断言失败的大语言模型<br>Insights from Rights and Wrongs: A Large Language Model for Solving Assertion Failures in RTL Design](insights_from_rights_and_wrongs_a_large_language_model_for_solving_assertion_failures_in_rtl_design.md) | 本文提出面向RTL断言故障调试开源领域大模型AssertSolver，设计三段式EDA数据增强流水线构建SVA故障数据集，采用预训练-SFT-DPO三阶段训练，让模型从错误样本中学习。自研SVA-Eval基准测试，pass@1达88.54，较o1-preview提升11.97%，支持输出推理链与精准代码修复。 |
| [GEM：GPU加速的仿真器式RTL模拟<br>GEM: GPU-Accelerated Emulator-Inspired RTL Simulation](gem_gpu_accelerated_emulator_inspired_rtl_simulation.md) | 本文提出仿真器GEM，借鉴FPGA编译流程设计GPU虚拟VLIW布尔处理器，构建完整RTL映射流水线。提出回旋执行层、多阶段划分、时序比特放置等算法，解决SIMT线程分叉、非规整访存痛点。在RISC-V、AI加速器等测试，相较商用仿真器平均提速9.15倍，最高加速64倍，方案开源。 |
| [基于仿真的并行扫掠：组合等价检查新视角<br>Simulation-based Parallel Sweeping: A New Perspective on Combinational Equivalence Checking](simulation_based_parallel_sweeping_a_new_perspective_on_combinational_equivalence_checking.md) | 本文提出基于GPU并行穷举仿真的组合等价检查框架Simulation-based Parallel Sweeping，区别传统SAT Sweeping。设计三维并行穷举仿真、窗口合并、多轮优先割局部函数校验模块，分多阶段迭代化简Miter。EPFL/IWLS大规模电路测试，4组可独立完成验证；GPU引擎搭配ABC平均提速4.89倍，相较商用LEC提升4.88倍。 |
| [MAGCS：用于逻辑综合优化故障检测的多智能体引导配置搜索<br>MAGCS: Multi-Agent Guided Configuration Search for Optimization Fault Detection in Logic Synthesis](magcs_multi_agent_guided_configuration_search_for_optimization_fault_detection_in_logic_synthesis.md) | 文件缺失或格式异常：未找到“## 研究概要”下的单段文本。 |
| [面向数据通路组合等价检查的并行动动态划分<br>Parallel Dynamic Partitioning for Datapath Combinational Equivalence Checking](parallel_dynamic_partitioning_for_datapath_combinational_equivalence_checking.md) | 本文提出PDP-CEC并行动态划分组合等价检查框架，面向乘加等复杂数据通路电路。设计复杂度启发式节点选择实现搜索空间二分拆分，主-监控-工作线程动态调度均衡负载。在工业数据通路基准上，可求解案例数约为基线3倍，加速区间5.11~125.27倍，并行扩展性优异。 |
## EDA3：时序分析与优化 (8)

EDA3: Timing Analysis and Optimization


### 时序预测、分析与优化领域的突破性进展 (6)

Breakthroughs in Timing Prediction, Analysis, and Optimization

- Session Chairs: Zhiyao Xie, Xin Zhao

> 本次会议深入剖析了可解决时序分析、时序预测与时序优化核心难题的创新方法。研讨主题涵盖超快速统计静态时序分析、基于机器学习的时序预测以及先进特征表征技术。此外，会议还探讨了一种可优化时序性能的快速时钟偏移调度算法，以及一套用于缓解密码硬件中毛刺跳变带来安全风险的解决方案。

> This session provides insights into innovative methodologies addressing key challenges in timing analysis, prediction, and optimization. Topics include ultra-fast statistical static timing analysis, machine learning-driven timing prediction, and advanced characterization techniques. Additionally, the session explores a fast clock skew scheduling algorithm for improved timing and an approach to mitigating security risks posed by glitch-induced transitions in cryptographic hardware.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [INSTA：面向工业物理设计应用的超高速可微统计静态时序分析引擎<br>INSTA: An Ultra-Fast, Differentiable, Statistical Static Timing Analysis Engine for Industrial Physical Design Applications](insta_an_ultra_fast_differentiable_statistical_static_timing_analysis_engine_for_industrial_physical_design_applications.md) | 本文提出INSTA，首款与商用签核工具高精度对齐的可微GPU统计STA引擎。一次性从参考工具抽取弧延迟，CUDA内核实现带CPPR/OCV的Top-K时序传播，LSE算子保证可微，提出时序梯度用于全局优化。3nm千万引脚设计0.1s完成时序计算，门控尺寸/布局应用分别实现15%TNS改善、59.4%TNS降幅。 |
| [GTN-Path：通过图变换器波形传播实现高效路径时序预测<br>GTN-Path: Efficient Path Timing Prediction through Waveform Propagation with Graph Transformer](gtn_path_efficient_path_timing_prediction_through_waveform_propagation_with_graph_transformer.md) | 本文提出GTN-Path图变换器时序路径波形预测框架，将标准单元、互连线分层建图，搭配波形逐级传播机制，无需时序库与寄生提取。7nm工艺工业电路测试，路径波形平均误差2.98%、延迟误差2.96%；相对HSPICE提速3510倍，商用签核STA工具提速12倍，仅需30%路径数据即可完成训练。 |
| [基于生成模型的标准单元时序库表征<br>Generative Model Based Standard Cell Timing Library Characterization](generative_model_based_standard_cell_timing_library_characterization.md) | 本文提出基于条件对抗自编码器CAAE的标准单元时序库表征生成模型，解决PVT角点爆炸、SPICE仿真耗时过长问题。以锚点角点时序数据训练，仅需少量仿真样本即可预测增量角完整时序表，无需厂商涉密晶体管网表。SAED14nm等测试，MAE低至0.38ps，整体表征时长缩减42.8%。 |
| [考虑供电网络的真正布线前时序预测<br>Truly Pre-Routing Timing Prediction via Considering Power Delivery Networks](truly_pre_routing_timing_prediction_via_considering_power_delivery_networks.md) | 本文提出融合网表、版图、PDN三模态的布线前时序预测框架，设计IR感知、拥塞感知双编码器，搭配帕累托多模态融合解决梯度冲突。TSMC16nm多电路测试，时序预测平均R²达0.96，推理相较商用工具提速1844倍， unseen电路泛化精度显著优于现有双模模型。 |
| [带动态时序图提取的快速迭代时钟偏斜调度算法<br>A Fast, Iterative Clock Skew Scheduling Algorithm with Dynamic Sequential Graph Extraction](a_fast_iterative_clock_skew_scheduling_algorithm_with_dynamic_sequential_graph_extraction.md) | 本文提出带动态时序图提取的迭代时钟偏移调度算法，通过更新-提取机制仅保留关键时序边，搭配双向遍历延迟求解与后端优化手段。在ICCAD基准测试，时序边提取量减少90.05倍，调度速度提升49.11倍，时序负松弛优化效果优于FPM、IC-CSS等主流方法，线长增量极小。 |
| [GLiTCH诱发跃迁用于安全密码硬件<br>GLiTCH induced Transitions for Secure Crypto-Hardware](glitch_glitch_induced_transitions_for_secure_crypto_hardware.md) | 本文提出GLiTCH安全硬件框架，颠覆消毛刺思路，通过门尺寸几何规划主动调控毛刺：抑制密钥相关毛刺、生成无关噪声毛刺降低侧信道泄露。先仿真定位泄露关键门，再构建GM几何规划求解门尺寸。AES/SM4/CLEIA测试，猜测熵平均提升52.82，面积平均开销38.74%。 |
## EDA4：功耗分析与优化 (8)

EDA4: Power Analysis and Optimization

### 人工智能/机器学习赋能电力与热完整性领域的前沿进展 (8)

Watts Up? AI/ML Enabled Advances in Power and Thermal Integrity

- Session Chairs: Prabal Basu, Noel Daniel Gundi

> 现代芯片组因计算工作量增大而导致能耗上升，这对芯片电源完整性提出了挑战，亟需高效的功耗分析，并深入探索降低整体功耗的方法。鉴于这些发展，本次会议将介绍一系列新技术，用于评估包括IR压降、供电网络、布局布线、热分析和架构优化在内的多种特性。此外，这些研究还利用新型AI/ML建模和设计自动化方法，以优化设计和EDA流程。

> Rising energy levels in modern chipsets due to larger computing workloads challenge the chip power integrity and have necessitated an efficient power analysis and a deeper exploration of methodologies to lower the overall power utilization. In light of these developments, this session presents novel techniques to estimate various attributes including IR drops, power-delivery networks, Place and Route, thermal analysis, and architectural enhancements. Furthermore, these works utilize novel AI/ML modeling and design automation approaches to optimize the design and EDA flow.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [基于嵌套域分解的可扩展电源网格分析前沿并行求解器<br>A Cutting-Edge Parallel Solver for Scalable Power Grid Analysis Using Nested Domain Decomposition](a_cutting_edge_parallel_solver_for_scalable_power_grid_analysis_using_nested_domain_decomposition.md) | 本文提出嵌套区域分解并行电源网格求解器Nested DDM，设计并行舒尔补计算与中间舒尔补分层机制，缓解传统DDM全局稠密矩阵规模爆炸、并行效率瓶颈。在IBMPG/THUPG基准测试，全局求解提速1.70倍，整体求解相较传统DDM加速1.30倍，32线程下较CHOLMOD串行求解器提速8.44倍。 |
| [IRGNN：融合数值解与点云的图学习静态IR压降预测框架<br>IRGNN: A Graph-based Framework Integrating Numerical Solution and Point Cloud for Static IR Drop Prediction](irgnn_a_graph_based_framework_integrating_numerical_solution_and_point_cloud_for_static_ir_drop_prediction.md) | 本文提出IRGNN图学习框架用于静态IR压降预测，融合AMG-PCG数值粗解与版图点云特征，构建专属IRGraph供电网图结构；设计距离注意力NDA层+图Transformer层捕获局部与全局拓扑。ICCAD2023等数据集验证，相较CNN基线MAE最高降低38.67倍，推理速度较数值工具PowerRush提升4.6倍，支持全节点细粒度压降预测。 |
| [LMM-IR：大规模网表感知多模态静态IR压降预测框架<br>LMM-IR: Large-Scale Netlist-Aware Multimodal Framework for Static IR-Drop Prediction](lmm_ir_large_scale_netlist_aware_multimodal_framework_for_static_ir_drop_prediction.md) | 本文提出LMM-IR多模态静态IR压降预测框架，设计大规模网表Transformer(LNT)将SPICE网表转为三维点云，融合版图图像与网表双模态特征，通过交叉注意力融合建模多层供电网拓扑。ICCAD2023数据集测试，平均F1达0.58、MAE最优，推理耗时远低于对比SOTA，可处理十万级节点供电网。 |
| [基于统一序列学习框架的电源网格结构探索<br>Power-Grid Structure Exploration with Unified Sequence-based Learning Framework](power_grid_structure_exploration_with_unified_sequence_based_learning_framework.md) | 本文提出基于序列建模的统一电源网格探索框架，设计PGTransformer预测静态IR压降，搭配MLHS采样与改进NSGA-II多目标优化。将多层供电结构转为序列表征，自动生成帕累托最优PG方案。3nm/2nm工业芯片测试，压降预测平均误差仅0.011%，优化后布线资源占用降低15%，时序裕度提升34%。 |
| [面向IR ECO的实时动态IR压降预测<br>Real-Time Dynamic IR-drop Prediction for IR ECO](real_time_dynamic_ir_drop_prediction_for_ir_eco.md) | 本文面向IR ECO流程提出实时动态IR压降预测框架，设计全局瓦片特征XGBoost模型，开发无仿真快速特征更新方法。3nm工业电路测试，修复单元识别率超96%，平均MAE仅8.75mV；相较商用Voltus提速88倍，传统ML方案提速64倍，支持多ECO候选并行评估。 |
| [ATLAS：用于细粒度时序版图功耗分析的自监督跨阶段网表功耗模型<br>ATLAS: A Self-Supervised and Cross-Stage Netlist Power Model for Fine-Grained Time-Based Layout Power Analysis](atlas_a_self_supervised_and_cross_stage_netlist_power_model_for_fine_grained_time_based_layout_power_analysis.md) | 本文提出ATLAS自监督跨层级网表功耗预测框架，基于轻量化图Transformer编码器，设计五类电路自监督预训练任务，分三类轻量模型微调，仅需综合网表即可预测逐周期版图级功耗。6款300K~600K单元CPU电路验证，总功耗MAPE低于1%，推理速度较传统布局+PTPX流程快千倍。 |
| [NeuralMesh：用于2.5D/3D芯粒热仿真的FEM网格生成神经网络<br>NeuralMesh: Neural Network For FEM Mesh Generation in 2.5D/3D Chiplet Thermal Simulation](neuralmesh_neural_network_for_fem_mesh_generation_in_2_5d_3d_chiplet_thermal_simulation.md) | 本文提出NeuralMesh神经网络有限元网格生成框架，面向2.5D/3D芯粒热仿真。构建增强U-Net预测温度场，融合几何与热梯度自适应加密四面体网格，省去传统迭代细化。工业芯粒测试，网格单元平均减少44%，生成最高提速45倍，热仿真温度误差控制在0.8%以内。 |
| [ASRR-PINN：基于自适应子区域随机重采样的3D-IC热分析PINN方法<br>ASRR-PINN: Adaptive Sub-Regional Random Resampling-Based PINN for Thermal Analysis of 3D-ICs](asrr_pinn_adaptive_sub_regional_random_resampling_based_pinn_for_thermal_analysis_of_3d_ics.md) | 本文提出ASRR-PINN用于3D IC快速热分析，设计自适应子区域随机重采样(ASRR)优化采样分布；傅里叶变换嵌入网络自动满足三维热边界，简化损失函数；搭建简约降维网络实现参数化仿真。测试表明同采样量下最大绝对误差降低56%以上，仿真耗时缩短28%，参数化版本提速超200倍。 |
## EDA5：RTL/逻辑级与高级综合 (20)

EDA5: RTL/Logic Level and High-level Synthesis

### 遵循逻辑：逻辑合成技术的进展 (8)

Follow the Logic: Advances in Logic Synthesis

- Session Chairs: Giovanni De Micheli, Eleonora Testa

> 尽管在逻辑综合与优化领域已有数十年的研究历史，该领域依然保持着高度活跃且发展势头不减，本环节收录的八篇精彩论文便是明证。前两篇论文运用等价图（e-graph）概念，分别用于功能验证和技术映射前的结构偏差消减。随后四篇论文聚焦传统逻辑综合方向，涵盖布尔分解、逻辑重构、电路重构以及主体图结构偏差相关挑战等核心议题。最后两篇论文则提出了近似逻辑综合与最优逻辑电路合成方面的创新方法。

> Despite decades of prior research in logic synthesis and optimization, the field continues to be highly active and progress continues unabated, as evidenced by the eight exciting papers in this session. The first two papers leverage the concept of equivalence graphs (e-graphs) for functional verification and reducing structural bias prior to technology mapping. The next four papers contribute to more traditional logic synthesis thrusts, including Boolean decomposition, logic restructuring, refactoring, and challenges associated with structural bias of the subject graph. The last two papers present innovations in approximate logic synthesis, and synthesis of optimal logic circuits.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [BoolE：通过布尔等式饱和实现精确符号推理<br>BoolE: Exact Symbolic Reasoning via Boolean Equality Saturation](boole_exact_symbolic_reasoning_via_boolean_equality_saturation.md) | 本文提出BoolE布尔等式饱和符号推理框架，基于egg e-graph构建两套重写规则，设计适配多输入多输出全加器的DAG代价提取算法。针对工艺映射后破碎算术电路，可精准还原精确FA单元。在CSA、Booth乘法器测试，精确FA数量较ABC提升3倍以上，集成RevSCA验证工具后最高提速数千倍。 |
| [E-morphic：面向逻辑综合结构探索的可扩展等式饱和<br>E-morphic: Scalable Equality Saturation for Structural Exploration in Logic Synthesis](e_morphic_scalable_equality_saturation_for_structural_exploration_in_logic_synthesis.md) | 本文提出E-morphic可扩展等式饱和逻辑综合框架，解决传统e-graph工具规模受限、提取易陷入局部最优问题。设计DAG直转、解空间剪枝、模拟退火多线程提取、GNN快速代价评估四大核心技术。EPFL基准测试相较工业延迟优化流程，平均面积缩减12.54%、延迟降低7.29%，大电路无超时崩溃。 |
| [EDGE：DBMS赋能的GIG综合布尔分解<br>EDGE: DBMS-Empowered Boolean Decomposition for GIG Synthesis](edge_dbms_empowered_boolean_decomposition_for_gig_synthesis.md) | 本文提出EDGE框架，借助数据库加速多输出布尔分解用于GIG逻辑综合。将分解转化关系代数查询，设计串行/并行分解配套贪心、链式等策略，分层拆解真值表至小规模子函数。IWLS基准测试，分解速度最高提升21倍，优化后AIG节点总数相较主流fx方法降低15%以上。 |
| [保留逻辑块的逻辑重构<br>Logic Restructuring with Preserved Logic Blocks](logic_restructuring_with_preserved_logic_blocks.md) | 本文提出透明盒化逻辑重构方案，对比传统黑盒保护加法器、多路选择器等复合标准单元；设计线级重替换优化算法，仅在盒输入端口做无关心化简。EPFL与工业基准测试，透明盒化映射规模降幅优于黑盒，全流程时序TNS额外优化1.8%，面积、功耗同步改善。 |
| [ELF：通过重构冗余剪枝实现高效逻辑综合<br>ELF: Efficient Logic Synthesis by Pruning Redundancy in Refactoring](elf_efficient_logic_synthesis_by_pruning_redundancy_in_refactoring.md) | 本文提出ELF剪枝框架加速AIG重构算子，设计6维轻量电路特征与小型前馈分类器，提前筛除无优化潜力割集。EPFL与工业电路测试，平均提速3.9倍，面积劣化低于0.27%；分类器工业场景召回95%、精度85%，可拓展至rewrite、重替换等综合算子。 |
| [混合结构选择算子：通过异构表示增强工艺映射<br>Mixed Structural Choice Operator: Enhancing Technology Mapping with Heterogeneous Representations](mixed_structural_choice_operator_enhancing_technology_mapping_with_heterogeneous_representations.md) | 本文提出混合结构选择算子MCH，融合AIG/XMG/MIG等异质逻辑图构建多选网络，按路径分层采用多策略生成等价候选，打通逻辑优化与工艺映射协同。ASIC映射面积降3.73%、延迟降8.94%；FPGA LUT映射刷新EPFL基准多项最优，同时可突破局部最优用于逻辑重构。 |
| [基于排序的多目标近似逻辑综合：蒙特卡洛树搜索方法<br>Rank-based Multi-objective Approximate Logic Synthesis via Monte Carlo Tree Search](rank_based_multi_objective_approximate_logic_synthesis_via_monte_carlo_tree_search.md) | 本文提出基于蒙特卡洛树搜索的排序型多目标近似逻辑综合框架，设计电路非支配排序划分解空间，构建Rank-Transformer预测局部近似变换LAC优劣。在ER、NMED两类误差约束下，相比主流方法平均延时降低25.51%~29.84%、面积缩减15.93%~23.24%，整体运行速度提升1.19~4.16倍。 |
| [Harrow：通过调和均值与整数划分综合光逻辑电路<br>Harrow: Synthesis of Optical Logic Circuits via Harmonic Mean and Integer Partition](harrow_synthesis_of_optical_logic_circuits_via_harmonic_mean_and_integer_partition.md) | 本文提出Harrow光子集成电路逻辑综合框架，针对BDD映射光电路信号衰减问题，基于调和均值优化DC耦合器，整数划分实现开关复制优化，证明“先均值调整再复制”为最优执行顺序。IWLS基准测试，同等开关开销下相较SOTA综合方案效率提升最高192%，光损耗显著降低，运行开销可控。 |
### 机器学习驱动的逻辑综合 (6)

ML-Powered Logic Synthesis

- Session Chairs: Peipei Zhou, Cunxi Yu

> 在电子设计自动化（EDA）中应用机器学习（ML）是一个新兴的研究方向，本次会议收录了六篇与这一重要主题相关的论文。前三篇论文利用大语言模型（LLM）生成综合脚本，以及生成Chisel和Verilog硬件描述语言代码。接下来的论文采用生成式人工智能中的扩散模型进行逻辑优化。随后一篇论文涉及多路复用器综合，相比现有技术实现了显著的面积优化。最后一篇论文采用演员-评论家神经网络方法，用于优化动态电压频率调节（DVFS）技术。

> The use of machine learning (ML) in EDA is a burgeoning research direction and this session includes six papers aligned with this important theme. The first three papers make use of large language models (LLMs) for generating synthesis scripts and for generating Chisel and Verilog RTL code. The next paper uses generative AI, a diffusion model, for logic optimization. The next paper is related to multiplexer synthesis, and offers a significant area reduction vs. the state-of-the-art. The last paper uses an actor-critic neural-network approach in the context of optimizing dynamic voltage-frequency scaling (DVFS).


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [ChatLS：用于逻辑综合脚本定制的多模态RAG与思维链框架<br>ChatLS: Multimodal Retrieval-Augmented Generation and Chain-of-Thought for Logic Synthesis Script Customization](chatls_multimodal_retrieval_augmented_generation_and_chain_of_thought_for_logic_synthesis_script_customization.md) | 本文提出ChatLS大语言模型框架，融合电路图GNN多模态RAG与分步CoT推理，自动定制逻辑综合脚本。设计CircuitMentor提取电路层级特征、SynthRAG多源检索、SynthExpert迭代推理三大模块。在多款开源芯片测试，相较GPT-4o、Claude 3.5显著优化时序负松弛，时序收敛能力最优。 |
| [MAGE：自动化RTL代码生成的多智能体引擎<br>MAGE: A Multi-Agent Engine for Automated RTL Code Generation](mage_a_multi_agent_engine_for_automated_rtl_code_generation.md) | 本文提出开源多智能体RTL生成引擎MAGE，划分测试台、RTL生成、评判、调试四类专用智能体；设计高温候选采样与Verilog状态断点调试机制。在VerilogEval基准下功能正确率达95.7，较Claude3.5提升23.3%，大幅提升自然语言转Verilog的语法与功能完备性。 |
| [ReChisel：通过反思机制实现高效自动Chisel代码生成<br>ReChisel: Effective Automatic Chisel Code Generation by LLM with Reflection](rechisel_effective_automatic_chisel_code_generation_by_llm_with_reflection.md) | 本文提出ReChisel智能体系统，面向LLM自动生成Chisel代码。设计编译+仿真双反馈反思迭代机制，新增循环逃逸模块解决迭代停滞问题。在216组标准电路测试，多款大模型生成成功率提升10%~50%，性能对标顶尖Verilog自动生成框架AutoChip。 |
| [基于扩散模型的高效连续逻辑优化<br>Efficient Continuous Logic Optimization with Diffusion Model](efficient_continuous_logic_optimization_with_diffusion_model.md) | 本文提出基于扩散模型的连续逻辑优化框架，将离散变换序列映射至连续隐空间。依托多任务代理模型获取QoR梯度，扩散模型约束隐变量贴合合法变换分布，规避优化后映射失真。EPFL、ISCAS基准测试，相较RL、贝叶斯等离散搜索方法，运行速度提升5~130倍，面积、时序QoR同步更优。 |
| [smaRTLy：基于逻辑推断与结构重建的RTL优化<br>smaRTLy: RTL Optimization with Logic Inferencing and Structural Rebuilding](smartly_rtl_optimization_with_logic_inferencing_and_structural_rebuilding.md) | 本文提出SmaRTLy RTL多路选择树优化工具，包含SAT冗余消除与ADD驱动结构重构两大模块。前者挖掘控制信号逻辑依赖剔除冗余MUX，后者重排case生成多路树减少门数。IWLS/RISC-V基准相较Yosys额外降低8.95%AIG面积，百万门工业电路可多削减47.2%面积。 |
| [通过演员-评论家范式实现集中训练与分散控制的高优化多核系统<br>Centralized Training and Decentralized Control through the Actor-Critic Paradigm for Highly Optimized Multicores](centralized_training_and_decentralized_control_through_the_actor_critic_paradigm_for_highly_optimized_multicores.md) | 本文提出集中训练分布式执行的Actor-Critic多核热控DVFS框架，多Actor分应用独立控频，全局Critic评估交互收益，解决分布式控制器观测不全、决策冲突、热耦合干扰问题。基于真实i9处理器测试，相较TP-DQL、Profit平均性能提升20%、24%，峰值提升34%、65%，热违规极少且开销极低。 |
### 双向审视：高级综合与近似计算的新方向 (6)

Look Both Ways: New Directions in High-Level Synthesis and Approximate Computing

- Session Chairs: Aman Gayasen, Christian Pilato

> 本次会议将展示6篇令人振奋的论文，这些论文阐述了高层次综合（HLS）和近似计算领域的最新进展。在高层次综合方面，四篇论文分别介绍了以下创新成果：HLS生成的异步数据流电路；高效实现推测执行的电路生成技术；利用多时钟域降低功耗的方法；以及硬件加速内核的自动选择机制。最后两篇论文聚焦近似计算领域，首篇提出了自动化设计空间探索方法，用于识别通过近似计算实现面积/功耗优化的潜力设计点；第二篇则介绍了一种高效的二进制到一元数转换新方法。

> This session presents 6 exciting papers describing recent advances in high-level synthesis (HLS) and approximate computing. On the HLS front, four papers describe new contributions to HLS-generated asynchronous dataflow circuits; the generation of circuits that perform speculative execution efficiently; the use of multiple clock domains to reduce power; and, automated selection of kernels for hardware acceleration. The last two papers are related to approximate computing. The first of these automates design-space exploration in HLS to identify design points with high potential for area/power savings from approximation. The next introduces an efficient approach for binary-to-unary number conversion.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [PipeLink：用于数据流高级综合的流水化资源共享系统<br>PipeLink: a pipelined resource sharing system for dataflow high-level synthesis](pipelink_a_pipelined_resource_sharing_system_for_dataflow_high_level_synthesis.md) | 本文提出PipeLink模块化数据流高级综合框架，采用编译-链接两段式流程，设计自适应控制令牌网络ACTN统一实现函数、存储资源流水线共享。基于SEQ/IF/循环三种序列组合生成访问控制流，保障执行序且维持弹性数据流。测试相较商用/学术HLS，平均延迟降至0.62倍、能耗缩减20倍，仅小幅增加版图面积。 |
| [推测式高级综合中的恢复逻辑优化<br>Optimizing Recovery Logic in Speculative High-Level Synthesis](optimizing_recovery_logic_in_speculative_hls.md) | 本文面向SpecHLS推测式高级综合，针对回滚恢复逻辑面积与时序开销过大问题，提出三类IR变换优化：可逆运算简化、后支配分析消除冗余回滚、线性规划最优重定位。在多不规则控制基准测试，硬件资源平均降低10%，有效吞吐平均提升13%，大幅缓解推测电路硬件代价。 |
| [AutoClock：面向FPGA功耗高效HLS设计的自动时钟管理<br>AutoClock: Automated Clock Management for Power-Efficient HLS Designs on FPGAs](autoclock_automated_clock_management_for_power_efficient_hls_designs_on_fpgas.md) | 本文提出AutoClock开源FPGA高层次综合时钟自动化管理框架，适配Vitis HLS。自定义时钟编译指令，ILP求解最优MMCM/PLL/BUFG资源分配；分层贪心门控降低动态功耗，自适应插入多类CDC同步电路，时钟多路复用解决跨域TDM冲突。在Alveo U28验证，时钟门控+多时钟协同优化下动态功耗最高下降74.38%。 |
| [Cayman：控制流与数据访问优化驱动的定制加速器生成<br>Cayman: Custom Accelerator Generation with Control Flow and Data Access Optimization](cayman_custom_accelerator_generation_with_control_flow_and_data_access_optimization.md) | 本文提出Cayman端到端自定义加速器生成框架，基于全局程序结构树wPST自动筛选加速核，DP剪枝算法做面积-帕累托寻优；建模耦合/解耦/片上存储三类访存接口，搭配可重构加速器合并技术。PolyBench等测试下，同等面积相较NOVIA、QsCores分别提速14.4×、8.0×。 |
| [ADVISOR：近似计算友好型高级综合设计空间探索器<br>ADVISOR: Approximate Computing-frienDly High-LeVel Synthesis DesIgn Space ExplORer](advisor_approximate_computing_friendly_high_level_synthesis_design_space_explorer.md) | 本文提出ADVISOR近似友好型HLS设计空间探索框架，设计AFI近似友好指数快速筛选易做近似的硬件微架构，采用模糊变异遍历pragma组合，分两阶段执行：AFI预筛选+分层近似优化。DSP/图像基准测试，相比暴力全近似搜索平均提速68倍，面积缩减效果接近穷尽遍历方案。 |
| [面向低成本一元计算的无比较器比特流生成<br>Comparison-Free Bit-Stream Generation for Cost-Efficient Unary Computing](comparison_free_bit_stream_generation_for_cost_efficient_unary_computing.md) | 本文提出无比较器的一元比特流生成架构，含串行、近似并行、精确并行三类电路。基于递减单元+或门FSM逻辑，摒弃传统计数器与m位比较器。45nm综合测试，单输入面积最高省85%、功耗省92%；在排序、中值滤波等四类一元应用中硬件开销大幅降低。 |
## EDA6：模拟CAD、仿真、验证与测试 (11)

EDA6: Analog CAD, Simulation, Verification and Test

### 大语言模型/深度学习驱动的模拟电路设计与分析 (5)

LLM/DL Driven Analog Circuit Design and Analysis

- Session Chairs: Arindam Basu, Markus Olbrich

> 现代模拟集成电路设计面临着复杂性增加、优化、工艺-电压-温度（PVT）变化以及仿真瓶颈等挑战。传统方法难以应对庞大的设计空间和可靠性问题。大型语言模型与深度学习技术通过任务自动化、管理PVT变化以及降低仿真成本来解决这些问题。本次会议将涵盖以下主题：用于考虑工艺变化的强化学习设计、面向系统级优化的迁移学习、通用神经模拟器、GPU加速的无源性强制实施，以及用于IR压降预测的图像-图融合技术，展示人工智能在优化和提升模拟IC设计中的作用。

> Modern analog IC design faces challenges like increasing complexity, optimization, PVT variations, and simulation bottlenecks. Traditional methods struggle with large design spaces and reliability. LLMs and deep learning technologies address these issues by automating tasks, managing PVT variations, and reducing simulation costs. This session will cover the topics reinforcement learning for variation-aware designs, transfer learning for system-level optimization, universal neural simulators, GPU-accelerated passivity enforcement, and image-graph fusion for IR drop prediction, demonstrating AI’s role in optimizing and enhancing analog IC design.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [GLOVA：基于风险敏感强化学习的全局与局部失配感知模拟电路设计<br>GLOVA: Global and Local Variation-Aware Analog Circuit Design with Risk-Sensitive Reinforcement Learning](glova_global_and_local_variation_aware_analog_circuit_design_with_risk_sensitive_reinforcement_learning.md) | 本文提出GLOVA面向PVT全局+局部失配的模拟电路尺寸优化框架，采用风险敏感强化学习搭配集成评价网络，配套μ-σ评估、仿真重排序加速验证。支持角点、本地/全局蒙特卡洛多类工业仿真，DRAM、运放等电路测试，相较主流方法采样效率最高提升80.5倍，总耗时降低76倍，优化成功率100%。 |
| [图引导迁移学习提升模拟/混合信号电路系统级优化效率<br>Graph-Guided Transfer Learning to Boost the Efficiency of System-Level Optimization of Analog/Mixed-Signal Circuits](graph_guided_transfer_learning_to_boost_the_efficiency_of_system_level_optimization_of_analog_mixed_signal_circuits.md) | 本文提出图引导迁移学习模拟混合信号系统级优化框架，融合GAT与DDPG强化学习，设计三层电路图相似度判定规则实现跨拓扑知识迁移。以连续时间ΔΣ ADC为验证对象，相比传统算法功耗最高降低40%；跨架构迁移可减少11倍仿真次数，最优功耗结果提升12.4%。 |
| [INSIGHT：基于自回归Transformer的通用模拟电路神经仿真框架<br>INSIGHT: A Universal Neural Simulator Framework for Analog Circuits with Autoregressive Transformers](insight_a_universal_neural_simulator_framework_for_analog_circuits_with_autoregressive_transformers.md) | 本文提出INSIGHT通用自回归Transformer神经模拟仿真框架，将模拟电路性能预测建模为序列生成任务，设计贪心指标排序策略，搭配LoRA低秩微调实现跨工艺迁移。运放、TIA、LDO等多电路测试，预测R²≥0.95；跨工艺训练数据减少60%，内存降低42%，嵌入RL尺寸优化后SPICE仿真调用量降低100~1000倍。 |
| [G-SpNN：用于神经网络S参数建模的GPU加速无源性强制方法<br>G-SpNN: GPU-Accelerated Passivity Enforcement for S-Parameter Modeling with Neural Networks](g_spnn_gpu_accelerated_passivity_enforcement_for_s_parameter_modeling_with_neural_networks.md) | 本文提出GPU加速G-SpNN框架，将S参数无源宏建模的无源约束优化映射为神经网络训练任务。基于谱分解与PFE变换构造可微网络，搭配LBFGS二阶优化、QR化简损失。对比主流DAO算法，平均提速7.63倍，内存占用降低两个数量级，多端口射频互连建模精度更优。 |
| [一种用于静态IR压降预测的新型图像-图异构融合框架<br>A Novel Image-Graph Heterogeneous Fusion Framework for Static IR Drop Prediction](a_novel_image_graph_heterogeneous_fusion_framework_for_static_ir_drop_prediction.md) | 本文提出IGHF图像-图异构融合框架用于静态IR压降预测，CNN分支LLE+HACG提取多尺度空间特征，GNN分支CVA模块聚合异构高阶拓扑信息，双分支特征融合。在CircuitNet数据集测试，相比MAUNet、IREDGe误差分别降低24.6%、55.0%，迁移学习下泛化能力显著提升。 |
### 模拟电路仿真与优化的创新技术 (6)

Innovative Techniques for Analog Circuit Simulation and Optimization

- Session Chairs: Sheldon Tan, Ibrahim (Abe) Elfadel

> 电路仿真对于模拟电路设计至关重要，但在处理大规模或先进工艺电路时，计算成本高昂。本环节将介绍针对电路仿真与优化核心难题的前沿技术，涵盖布局后SPICE仿真、射频电路仿真以及基于仿真的模拟电路优化等挑战性课题。演讲将展示创新理念，包括加速仿真流程、优化方程求解器内核、降低内存开销以及实现电路尺寸优化的加速方法。

> Circuit simulation is essential for analog circuit design, but suffers from large computational costs when dealing with large-scale or advanced-technology circuits. This session includes the cutting-edge techniques for the hard-core problems of circuit simulation and optimization. They address the challenges on post-layout SPICE simulation, RF circuit simulation, and the simulation based analog circuit optimization. The innovative ideas are presented to accelerate the simulation process, optimize the core of equation solvers, reduce memory cost, and enable optimization speedup for circuit sizing.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [PiSPICE：通过关键寄生识别加速版图后SPICE仿真<br>PiSPICE: Accelerating Post-Layout SPICE Simulation via Essential Parasitic Identification](pispice_accelerating_post_layout_spice_simulation_via_essential_parasitic_identification.md) | 本文提出PiSPICE版图后SPICE仿真加速框架，基于预布局电路伴随灵敏度识别关键寄生。通过伪RC建模划分敏感/非敏感节点，非敏感子网直接合并，敏感子网采用改进PRIMA降阶。运放、ADC等测试，最大误差低于0.78，最高提速17.27倍，电路规模最高缩减93.77倍。 |
| [Me-MPK：通过内存高效矩阵幂内核加速Krylov子空间求解器<br>Me-MPK: Accelerating Krylov Subspace Solvers via Memory-efficient Matrix-Power Kernel](me_mpk_accelerating_krylov_subspace_solvers_via_memory_efficient_matrix_power_kernel.md) | 本文提出内存高效矩阵幂内核Me-MPK，面向多核共享内存架构，统一利用缓存复用与对称矩阵特性。构建统一依赖图，架构感知递归划分结合分隔子图消除冲突；适配s步CG/BiCGStab求解。X86/ARM平台分别平均提速2.00/1.86倍，整机稀疏求解最高提速1.65/1.58倍。 |
| [用于RF电路HB雅可比的新型时域预条件子<br>New Time-Domain Preconditioners for HB Jacobian of RF Circuits](new_time_domain_preconditioners_for_hb_jacobian_of_rf_circuits.md) | 本文面向射频电路谐波平衡(HB)仿真，提出两类新型时域预条件子：混合有限差分预条件子适配强非线性无分布器件电路，时域平均预条件子支持含传输线等分布器件电路；同时提出矩阵范数非线性度量指标，可先验选择预条件。强非线性电路GMRES迭代数与计算耗时平均降幅超2倍。 |
| [用于周期小信号分析的高效回收子空间截断方法<br>Efficient Recycling Subspace Truncation Method for Periodic Small-Signal Analysis](efficient_recycling_subspace_truncation_method_for_periodic_small_signal_analysis.md) | 本文面向射频周期小信号仿真提出Krylov子空间截断复用框架，基于Floquet理论设计子空间筛选策略，搭配最优初值复用方法。解决大规模电路频扫时子空间膨胀、内存溢出、迭代过多问题。工业射频电路测试，同等内存上限下相较GCRO-DR最高提速2.65倍，矩阵向量乘次数显著减少。 |
| [MemSens：通过新型有界误差有损压缩显著降低伴随灵敏度分析内存开销<br>MemSens: Significantly Reducing Memory Overhead in Adjoint Sensitivity Analysis Using Novel Error-Bounded Lossy Compression](memsens_significantly_reducing_memory_overhead_in_adjoint_sensitivity_analysis_using_novel_error_bounded_lossy_compression.md) | 本文提出MemSens误差可控有损压缩框架，面向伴随灵敏度分析电路仿真。设计参考排序平滑、混合预测器、严格误差量化三层压缩流程，适配电路尖峰向量/矩阵数据。集成Xyce仿真器测试，相较主流压缩算法平均压缩比提升百倍级，内存开销降低两个数量级，同时严格保障灵敏度计算精度。 |
| [MARIO：用于模拟电路尺寸优化的超加性多算法协同框架<br>MARIO: A Superadditive Multi-Algorithm Interworking Optimization Framework for Analog Circuit Sizing](mario_a_superadditive_multi_algorithm_interworking_optimization_framework_for_analog_circuit_sizing.md) | 本文提出具备超加性的多算法协同模拟电路尺寸优化框架MAR。融合进化、贝叶斯、无导数优化异构算法，设计MTGP资源重分配、Voronoi数据广播、异步并行三大核心机制。在15款模拟电路与标准测试函数集验证，相比SOTA评估次数提速2.59倍，时间提速1.91倍。 |
## EDA7：物理设计与验证 (24)

EDA7: Physical Design and Verification

### PCB设计、分区与合法化的冒险之旅！(6)

Adventures in PCBs, Partitioning, and Legalization!

- Session Chairs: Ankur Prasad, Yu-Guang Chen

> 系好安全带，开启一段关于PCB布局、分区与合法化的探索之旅！首先，探索PCB全局布局与合法化的创新算法。接着，深入基于图神经网络（GNN）的图分区算法，随后体验一款快速确定性并行超图分割器。然后，研究采用台积电最新FinFlex标准单元的多高度单元合法化技术，以实现更优的功耗-性能-面积（PPA）表现。最后，通过一款针对多电源域设计的二级供电网络优化详细布局工具，为旅程画上完美句号。

> Buckle up for an adventure through the realms of PCBs, partitioning, and legalization! Start by exploring novel algorithms for PCB global placement and legalization. Next, dive into a GNN-based graph partitioning algorithm, followed by a fast deterministic parallel hypergraph partitioner. Then, explore multi-height cell legalization with TSMC's recent FinFlex standard cells that allows for better PPA. End your journey with a detailed placer that optimizes secondary power delivery network for multi-power domain designs.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [面向异构器件的间距约束PCB全局布局<br>Clearance-Constrained PCB Global Placement with Heterogeneous Components](clearance_constrained_pcb_global_placement_with_heterogeneous_components.md) | 本文提出面向异构元器件、带焊盘间距约束的PCB全局布局框架。构建XHPWA布线面积模型、焊盘间距平滑模型、双面密度模型，搭配二次规划合法化工具。学术与工业PCB基准测试，相较主流工具布线总长平均降30%，间距违规减少74%，可布性提升32%。 |
| [考虑高密度异构不规则任意方向器件的约束图PCB合法化<br>Constraint Graph-based PCB Legalization Considering Dense, Heterogeneous, Irregular-Shaped, and Any-Oriented Components](constraint_graph_based_pcb_legalization_considering_dense_heterogeneous_irregular_shaped_and_any_oriented_components.md) | 本文提出基于约束图mTCG的PCB合法化算法，支持双面、任意角度、不规则异型器件与焊盘间距约束。采用多矩形分割近似异形器件，构建改进传递闭包图，搭配MILP优化最小器件位移。工业与开源PCB测试，高密度场景合法化成功率远优于传统XDP，设计规则违规数近乎清零。 |
| [GPart：GNN增强的多层图划分器<br>GPart: A GNN-Enabled Multilevel Graph Partitioner](gpart_a_gnn_enabled_multilevel_graph_partitioner.md) | 本文提出GPart多层图划分框架，融合轻量GNN嵌入与多层粗化、精细化流程，设计无监督瑞利损失捕捉图谱特征。基于Titan23、DIMACS基准测试，相比METIS割尺寸平均降低34.13%~42.92%，内存占用仅为GAP的1/24.6、GenPart的1/12.4，兼顾划分质量与大规模图扩展性。 |
| [BlasPart：面向大规模平衡超图划分的确定性并行划分器<br>BlasPart: A Deterministic Parallel Partitioner for Balanced Large-Scale Hypergraph Partitioning](blaspart_a_deterministic_parallel_partitioner_for_balanced_large_scale_hypergraph_partitioning.md) | 本文提出BlasPart确定性并行超图划分工具，采用两阶段递归二分框架，设计层级自适应平衡约束策略适配大规模多分块场景。区分并行/串行二分流程保证结果确定，优化孤立顶点分配与多解筛选规则。在工业与标准超图测试，4096分块下较Mt-KaHyPar-SDet平均提速3.33倍，划分平衡性显著更优，割质量接近串行hMETIS。 |
| [MIA感知且功耗驱动单元版本替换的FinFlex单元合法化<br>MIA-aware FinFlex Cell Legalization with Power-Driven Cell Version Substitution](mia_aware_finflex_cell_legalization_with_power_driven_cell_version_substitution.md) | 本文面向3nm FinFlex混合行高单元，提出兼顾MIA约束与功耗驱动的合法化算法。分为预处理、DAG布局、DP后处理三阶段，支持同时序功率组内单元版本替换。ICCAD基准测试，相比SOTA总位移平均降低53%，运行时间缩减34%，MIA违规最多消除94%。 |
| [多电源域设计中的次级供电单元感知详细布局<br>Secondary-Power-Cell-Aware Detailed Placement in Multiple Power Domain Designs](secondary_power_cell_aware_detailed_placement_in_multiple_power_domain_designs.md) | 本文面向多电源域电路提出次级电源感知详细布局优化框架，以ILP整数规划为核心搭配被困单元迁移、电源引脚对齐流程。优先将跨域单元靠近目标次级电源条，降低次级PDN线长与布线违规。ISPD2018基准测试，临界次级线长减少11%，总次级线长降低30%，DR违规数量平均下降66%。 |
### 无限路由自助餐 (6)

All You Can Route Buffet


- Session Chairs: Michael Kazda, Stephan Held

> 准备好迎接一系列路由创新的盛宴。时序驱动的斯坦纳树研究在帕累托最优框架和时序约束全局路由中的预言问题中均得到探索。一种新型全局路由模型用基于区域的资源替代了传统的基于边的资源，从而提升了质量并更好地适应增量设计变更。通过基于强化学习的窗口选择策略，详细路由得以优化，实现更具针对性的拆除与重布线。Mr.TPL展示了如何获得卓越的三重图案化路由解决方案。最后，单元内路由与局部详细路由相整合，以提升整体布线质量。

> Prepare for a feast of routing innovations. Timing-driven Steiner trees are explored in both a Pareto-optimal framework and as an oracle problem within timing-constrained global routing. A new global routing model replaces traditional edge-based resources with area-based resources, improving quality and adaptation to incremental design changes. Detailed routing is enhanced through a reinforcement learning-based window selection strategy for more targeted rip-up and reroute. Mr.TPL shows how to achieve superior triple patterning routing solutions. Finally, intra-cell routing is integrated with local detailed routing to enhance overall routing quality.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [PatLabor：时序驱动布线树的帕累托优化<br>PatLabor: Pareto Optimization of Timing-Driven Routing Trees](patlabor_pareto_optimization_of_timing_driven_routing_trees.md) | 本文提出PatLabor时序驱动布线树帕累托优化框架，面向线长与最大时延双目标。基于平滑分析证明实际场景帕累托前沿规模多项式；n≤9引脚采用预查表精确求解，多引脚使用强化学习引导局部搜索。ICCAD-15测试，9引脚网可多获取58.5%帕累托最优解，查表生成速度较FLUTE快441倍。 |
| [面向时序约束全局布线的代价距离Steiner树<br>Cost-Distance Steiner Trees for Timing-Constrained Global Routing](cost_distance_steiner_trees_for_timing_constrained_global_routing.md) | 本文提出代价距离Steiner树快速近似算法，作为时序约束全局布线核心子问题求解器。算法达到O(log t)近似比，时间复杂度O(t(n log n+m))，远优于传统方法；引入分支延迟惩罚模型，搭配多层工程优化。5nm工业芯片测试，相比L1、浅光、Prim-Dijkstra，时序与拥塞指标最优，仅线长小幅增加。 |
| [动态局部用量：全局布线中瓦片内部布线占用的精确模型<br>Dynamic Local Usage: An Accurate Model for Usage of Tile-internal Wiring in Global Routing](dynamic_local_usage_an_accurate_model_for_usage_of_tile_internal_wiring_in_global_routing.md) | 本文提出DLU动态局部布线占用模型用于全局布线，引入尖端扩展惩罚精确刻画单元内部拥挤，配套RC感知斯坦纳树、XY局部优化、分层嵌入算法。在3/5nm工业电路测试，相较传统全局布线，过孔数、布线绕路、DR违规显著下降，时序裕量改善，仅小幅增加全局布线耗时。 |
| [用于增强窗口化拆线重布线的强化学习窗口选择<br>Reinforcement Learning-Driven Window Selection for Enhanced Window-Based Rip-up and Reroute in Chip Detailed Routing](reinforcement_learning_driven_window_selection_for_enhanced_window_based_rip_up_and_reroute_in_chip_detailed_routing.md) | 本文提出基于Maskable PPO强化学习的窗口重布线优化方案，面向详细布线RUR流程。采用SE-ResNet提取版图多层密度特征，动态调整窗口尺寸与撕裂模式，缓解DRV扩散问题。基于ISPD2018基准测试，全部电路实现无DRV布线，总线长平均优化0.07%，通孔数降低2.42%，整体运行时间仅小幅增加0.61%。 |
| [Mr.TPL：用于三重图案化光刻的新型多引脚布线方法<br>Mr.TPL: A New Multi-pin Routing Method for Triple Patterning Lithography](mr_tpl_a_new_multi_pin_routing_method_for_triple_patterning_lithography.md) | 本文提出面向三光刻(TPL)多引脚线网的详细布线算法Mr.TPL，设计3比特多颜色状态并行搜索、回溯着色机制，布线时同步规避冲突与缝合点。在ISPD基准测试，相较主流TPL布线方法颜色冲突减少81.17%、缝合点下降76.89%，最高提速5.4倍，制造可制造性显著提升。 |
| [TransRoute：超越标准单元方法的新型分层晶体管级布线框架<br>TransRoute: A Novel Hierarchical Transistor-Level Routing Framework Beyond Standard-Cell Methodology](transroute_a_novel_hierarchical_transistor_level_routing_framework_beyond_standard_cell_methodology.md) | 本文提出首个大规模晶体管层级分层布线框架TransRoute，突破标准单元抽象限制。分为布局分区、下层CP-SAT布线、上层通用布线三阶段，设计面向终端斯坦纳森林的高效CP-SAT约束模型。两款先进工艺8组测试表明，相较标准单元流程总线长平均降22%、面积降30%，利用率达90%且全流程DRC/LVS合规。 |
### 从FPGA、宏单元到单元级的布局优化 (6)

Squeezing Placement from FPGAs, Macros, Down to the Cell Level

- Session Chairs: Wuxi Li, Bill Swartz

> 从模块级到晶体管级，本场会议为每位与会者准备了布局相关内容。您将了解基于FPGA的CNN加速中的DSP布局、大规模宏单元布局、统一布局布线、改进的拥塞建模，以及构建最新的CFET标准单元库。加入我们，共同探索布局技术的多维度应用，优化先进节点半导体设计。

> From block level to the transistor level, this session has placement for everyone. Learn about DSP placement for FPGA-based CNN acceleration, large scale macro placement, unified placement and routing, improved congestion modeling, and constructing the latest CFET standard cell libraries. Join us to explore the many facets of placement to optimize advanced-node semiconductor design.

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [DSPlacer：面向FPGA CNN加速器的DSP布局<br>DSPlacer: DSP Placement for FPGA-based CNN accelerator](dsplacer_dsp_placement_for_fpga_based_cnn_accelerator.md) | 本文提出DSPlacer面向FPGA CNN加速器的数据通路DSP专用布局框架，采用GCN区分数据/控制DSP，IDDFS构建通路图，最小费用流求解DSP分配，双层ILP完成级联合法化。在ZCU104平台测试，相较Vivado、AMF-Placer，WNS分别提升32.5%、65.8%，布线规整度显著改善。 |
| [ReMaP：通过递归原型与外围引导重定位实现宏布局<br>ReMaP: Macro Placement by Recursively Prototyping and Periphery-Guided Relocating](remap_macro_placement_by_recursively_prototyping_and_periphery_guided_relocating.md) | 本文提出ReMaP宏布局框架，采用递归原型+外围引导重定位流程，创新ABPlace角度解析算法将宏约束于椭圆优化数据流与重叠代价。分批次固定宏迭代求解，搭配贝叶斯自动调参。基于OpenROAD八组工业测试，相较主流工具WNS/TNS平均提升8.39%、16.57%，自动调参可再优化时序8.75%。 |
| [RUPlace：通过统一布局与布线建模优化可布线性<br>RUPlace: Optimizing Routability via Unified Placement and Routing Formulation](ruplace_optimizing_routability_via_unified_placement_and_routing_formulation.md) | 本文提出RUPlace布线友好全局布局统一优化框架，构建布局-路由联合整数规划模型，基于ADMM双层优化搭配Wasserstein距离正则；设计模块化聚类凸单元膨胀与局部面积微调策略。在CircuitNet、Chipyard基准测试，相较OpenROAD横向拥塞降低4.74倍，运行速度提升3.67倍，布线线长优化7%。 |
| [用于可布线驱动全局布局的可微网络移动与局部拥塞缓解<br>Differentiable Net-Moving and Local Congestion Mitigation for Routability-Driven Global Placement](differentiable_net_moving_and_local_congestion_mitigation_for_routability_driven_global_placement.md) | 本文提出兼顾全局/局部拥塞的可微分析式全局布局框架，融合泊松方程拥塞模型、动量单元膨胀、电源轨引脚可访问密度调整。通过虚拟单元引导网线远离拥塞区，在ISPD2015基准测试，相较Xplace-Route布线违规平均下降40%，总线长与过孔数基本持平。 |
| [具备单元内可布线性保障的互补FET单元综合布局布线框架<br>Comprehensive Placement and Routing Framework with Guaranteed In-Cell Routability for Synthesizing Complementary-FET Cells](comprehensive_placement_and_routing_framework_with_guaranteed_in_cell_routability_for_synthesizing_complementary_fet_cells.md) | 本文面向3nm以下CFET堆叠器件，提出完整单元布局布线框架。设计BFS分块预处理、集成部分布线的SMT放置算法、分阶段金属布线流程。基于ASAP7基准测试，30款单元中7款取得最小宽度，其余单元M2轨道用量与金属总长最优，兼顾可布线性与布局密度。 |
| [利用背面金属布线的CFET单元库综合<br>Synthesis of CFET Cell Library Leveraging Backside Metal Routing](synthesis_of_cfet_cell_library_leveraging_backside_metal_routing.md) | 本文首个在CFET标准单元综合中引入背面BS布线，提出适配堆叠结构的晶体管折叠方案。借助欧拉路径预估CPP下界、动态规划计算前层最小走线，SMT完成单元布线。基于ASAP7基准测试，相较SOTA方案CPP降低1%、M2走线减少45、运行时间缩短19%，且严格遵循SPICE晶体管尺寸约束。 |
### 探索三维空间、时钟树与共享学习 (6)

Navigating 3D, Clock Trees, and Shared Learning

- Session Chairs: Igor Markov, David Chinnery

> 本次会议重点探讨了3D集成电路（IC）设计及时钟树综合（CTS）领域的最新进展，旨在提升功耗与性能表现。在3D IC方面：3D-Flow技术采用网络流算法最小化布局合法化单元位移；DCO-3D运用机器学习预测并降低布线拥塞；GNN-MLS则通过跨层金属共享布线缓解拥塞，在改善时序的同时解决可测试性问题。针对CTS技术，我们研究了利用芯片正反面金属层的布线方案，以及基于强化学习的"枢纽"节点布局方法，以优化时钟偏差、缓冲器数量和走线长度。最后，我们将介绍一种隐私保护的高精度联邦学习框架，推动机器学习在电子设计自动化（EDA）中的深入应用。

> This session highlights advances in 3D IC design and clock tree synthesis (CTS) for improved power and performance. In 3D ICs, 3D-Flow minimizes legalization cell displacement using network flow; DCO-3D uses machine learning to predict and reduce routing congestion; while GNN-MLS mitigates congestion by routing across tiers with metal layer sharing, improving timing while addressing testability issues. For CTS, we explore approaches using front and back-side metal layers and reinforcement learning based "hub" node placement to minimize clock skew, buffering, and wire length. Finally, we look into a privacy-protecting, highly accurate federated learning framework to help advance the use of machine learning in EDA.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [3D-Flow：面向3D IC的流式标准单元合法化<br>3D-Flow: Flow-based Standard Cell Legalization for 3D ICs](3d_flow_flow_based_standard_cell_legalization_for_3d_ics.md) | 本文提出3D-Flow，首款面向3D IC的网络流标准单元合法化工具。构建三维网格流图，采用分支定界搜索最短增广路径消解bin溢出；搭配消圈后优化降低最大位移。基于ICCAD22/23 3D布局基准测试，同等运行速度下平均位移降低13%、最大位移降低43%，线长增量更优。 |
| [DCO-3D：3D集成电路可微拥塞优化<br>DCO-3D: Differentiable Congestion Optimization in 3D ICs](dco_3d_differentiable_congestion_optimization_in_3d_ics.md) | 本文提出DCO-3D面向3D集成电路的可微分拥塞优化流程，构建孪生UNet预测双层芯片布线拥塞，搭配GNN实现三维跨层单元扩散。在3nm六款工业电路测试，相较Pin-3D基线布线溢出最高降47.2%，总负时序裕量改善86.2%，功耗降低5.1%。 |
| [GNN-MLS：通过GNN辅助金属层共享实现混合节点3D IC信号布线<br>GNN-MLS: Signal Routing in Mixed-Node 3D ICs through GNN-Assisted Metal Layer Sharing](gnn_mls_signal_routing_in_mixed_node_3d_ics_through_gnn_assisted_metal_layer_sharing.md) | 本文提出GNN-MLS框架面向异质同构3D IC金属层共享布线优化，将时序超图转为图Transformer模型，采用DGI自监督预训练减少标注开销，精准筛选增益网线。配套两类DFT方案解决跨层开路可测性问题，搭配混合节点3D PDN设计。测试显示时序违例路径削减79%，TNS、WNS分别提升94%、81%。 |
| [一种系统化的双面多目标时钟树综合方法<br>A Systematic Approach for Multi-Objective Double-Side Clock Tree Synthesis](a_systematic_approach_for_multi_objective_double_side_clock_tree_synthesis.md) | 本文提出系统化双面时钟树综合框架，融合分层时钟布线、多目标动态规划同步插入缓冲与nTSV、端点偏移细化三步流程，支持双面金属层协同优化。基于OpenROAD基准测试，相比主流增量方案时延、偏移分别优化2.22×、2.46×，运行速度提升6.922倍，可完成多目标设计空间探索。 |
| [应对成本-偏斜权衡：一种用于枢纽节点选择的自适应学习方法<br>To Tackle Cost-Skew Tradeoff: An Adaptive Learning Approach for Hub Node Selection](to_tackle_cost_skew_tradeoff_an_adaptive_learning_approach_for_hub_node_selection.md) | 本文提出基于自适应强化学习的时钟枢纽节点选择算法，构建Selector、Conductor双网络协同优化代价-偏斜权衡。Selector输出枢纽分布，Conductor评估布线综合收益，迭代生成时钟树。多规模电路测试，相较PD、BST-DME等经典算法，归一化偏斜与总线长同步降低，大规模电路提速显著。 |
| [FedEDA：面向EDA隐私保护机器学习的联邦学习框架<br>FedEDA: Federated Learning Framework for Privacy-Preserving Machine Learning in EDA](fededa_federated_learning_framework_for_privacy_preserving_machine_learning_in_eda.md) | 本文提出FedEDA，首个面向EDA场景的联邦学习聚合算法。利用Rent系数、电路规模等分层电路元数据构造定制正则项，缓解多客户端数据非均衡偏移。在布线可布性、RC寄生、线长三类EDA预测任务验证，相较FedAvg、FedProx、FLNet，回归指标最高提升74.5%，可兼容CNN/MLP/GNN主流EDA模型。 |
## EDA8：面向制造与可靠性的设计 (12)

EDA8: Design for Manufacturing and Reliability

### 从像素到芯片：AI增强的版图与掩模设计 (6)

From Pixels to Chips: AI-Enhanced Layout & Mask Design

- Session Chairs: Iris Hui-Ru Jiang, Luigi Capodieci

> 本次会议将探讨生成式人工智能如何彻底改变半导体设计，尤其是在光刻和掩模优化领域。您将了解到大型视觉模型如何实现全芯片掩模优化，以及自监督深度学习如何加速逆向光刻技术，从而突破分辨率和保真度的极限。我们将展示用于设计规则合规性的人工智能驱动图案生成技术，并探索如何利用元学习实现可泛化的热点检测。了解这些方法如何实现精度感知的良率优化，最终实现更快速、更高效的芯片设计。加入我们，共同见证人工智能在下一代可制造性设计（DFM）中的强大力量！

> This session explores how Generative AI is revolutionizing semiconductor design, particularly in the realm of lithography and mask optimization. Discover how large vision models are enabling full-chip mask optimization and how self-supervised deep learning accelerates inverse lithography, pushing the boundaries of resolution and fidelity. We will showcase AI-driven pattern generation techniques for design rule compliance and explore the use of meta-learning to achieve generalizable hotspot detection. Learn how these approaches enable precision-aware yield optimization and ultimately, faster, more efficient chip design. Join us to witness the power of AI in next-generation DFM!

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [LVM-MO：用于全芯片掩模优化的大型视觉模型先驱<br>LVM-MO: A Large Vision Model Pioneer for Full-Chip Mask Optimization](lvm_mo_a_large_vision_model_pioneer_for_full_chip_mask_optimization.md) | 本文提出面向全版图掩模优化的大视觉模型LVM-MO，构建光刻感知自编码器，采用贴合衍射范围移位窗口注意力，分三阶段千万版图数据训练。支持零样本全版图推理，规避分块拼接失真；对比SOTA，L2/EPE指标平均提升超50%，推理速度提速1000倍，单卡秒级输出完整掩模。 |
| [SSDL-ILT：利用自监督深度学习模型的高效ILT<br>SSDL-ILT: Efficient ILT Utilizing a Self-Supervised Deep Learning Model](ssdl_ilt_efficient_ilt_utilizing_a_self_supervised_deep_learning_model.md) | 本文提出自监督光刻逆成像框架SSDL-ILT，采用注意力R2U-Net网络，构造融合成像误差、工艺波动、掩模复杂度的物理损失函数，仅输入版图即可训练，端到端输出含SRAF优化掩模。ICCAD2013基准测试，成像L2误差平均降30%，推理提速最高12000倍，少样本迁移可适配陌生版图。 |
| [PatternPaint：基于扩散修复的实用版图图案生成<br>PatternPaint: Practical Layout Pattern Generation Using Diffusion-Based Inpainting](patternpaint_practical_layout_pattern_generation_using_diffusion_based_inpainting.md) | 本文提出PatternPaint少样本扩散修复版图生成框架，仅需20份合规版图微调预训练图像大模型。将版图生成拆解多轮修复流程，搭配模板降噪、PCA样本筛选与双掩码迭代机制，无需数值合法化求解。3nm Intel 18A工艺测试，合规率较原生预训练模型提升1.87倍，是唯一适配复杂2D金属规则的生成方案。 |
| [仅需一次样本的异步元学习可泛化光刻热点检测<br>Generalizable Lithographic Hotspot Detection Using Asynchronous Meta-Learning with Only One Shot](generalizable_lithographic_hotspot_detection_using_asynchronous_meta_learning_with_only_one_shot.md) | 本文提出异步元学习光刻热点检测框架，解决CNN模型跨版图泛化差问题。设计异步内外循环更新策略区分特征/分类模块学习率，搭配版图拓扑编码+K-Means少样本采样，仅单张样本即可适配全新设计。在ICCAD2012/2019数据集验证，F1显著领先基线，虚警率稳定低于7.5%。 |
| [准确度并非总是所需：精度感知贝叶斯良率优化<br>Accuracy Is Not Always We Need: Precision-aware Bayesian Yield Optimization](accuracy_is_not_always_we_need_precision_aware_bayesian_yield_optimization.md) | 本文提出PAYO精度感知贝叶斯良率优化框架，以FoM量化估计精度，构建连续自回归CAR模型刻画精度与良率收敛关系，设计多保真度采集策略动态分配仿真资源。在数字/模拟四类电路验证，同等仿真量下故障概率远优于SOTA，仿真开销降低10倍以上。 |
| [通过基数样条实现曲线型光学邻近校正<br>Curvilinear Optical Proximity Correction via Cardinal Spline](curvilinear_optical_proximity_correction_via_cardinal_spline.md) | 本文提出基于基数样条的曲线型OPC框架CardOP，用控制点表征掩模轮廓，依托光刻仿真迭代修正。推导完整曲线MRC校验方法，支持ILT结果拟合修复违规。金属/通孔版图测试EPE平均降低50%，PVB提升4.2%，大规模电路与ILT混合场景均优于现有曲线OPC与商用Calibre。 |
### 欢迎来到硅谷竞技场：驾驭晶体管，驯服良率，驰骋3D封装新边疆 (6)

Welcome to the Silicon Rodeo: Wrangling Transistors, Taming Yield, and Riding the 3D Packaging Frontier

- Session Chairs: Qi Sun, Ing-Chao Lin

> 准备好迎接半导体设计新领域的狂野之旅了吗？从驯服CFET和Flip-FET中的晶体管布局，到用AI驱动的多智能体分析来驾驭良率预测这头难以控制的野兽，我们正在围猎现代超大规模集成电路（VLSI）中最棘手的挑战。我们将深入探讨采用YAP超快速良率建模的3D小芯片封装，用SDM-PEB套准曝光后烘烤精度，而现在，借助ChipletEM技术，我们正全力冲刺2.5D和3D集成中的电迁移签核。快上马吧！我们将集结芯片设计领域的最佳创新，确保您的电路不会在流片之路上被甩出赛道！

> Ready for a wild ride through the next frontier of semiconductor design? From wrangling transistor layouts in CFET and Flip-FET to taming the unruly beasts of yield prediction with AI-driven multi-agent analysis, we’re corralling the toughest challenges in modern VLSI. We’ll dive into 3D chiplet packaging with YAP’s ultra-fast yield modeling, lasso post-exposure bake accuracy with SDM-PEB, and now, with ChipletEM, we’re putting the spurs to electromigration signoff in 2.5D and 3D integration. Saddle up as we rustle up the best innovations in chip design, ensuring your circuits don’t get bucked off the road to tape-out!

| 中英论文题目 | 研究概要 |
|------------|-----------|
| [缓解基于互补FET的VLSI设计可布线性问题<br>Mitigating Routability Problems in Complementary-FET-based VLSI Designs](mitigating_routability_problems_in_complementary_fet_based_vlsi_designs.md) | 本文面向5nm以下CFET垂直堆叠工艺，解决单元高度压缩带来引脚可达性、布线拥塞两大布线问题。设计强制M2、留白两类扩展单元，结合DBSCAN热点聚类与局部阻挡增量布局形成端到端流程。测试DRV最高削减71.3%，平均布线违规下降73.9%，同时保留CFET面积优势，时序功耗损失极小。 |
| [利用Flip-FET（FFET）标准单元的设计与工艺协同优化<br>Design and Technology Co-optimization Utilizing Flip-FET (FFET) Standard Cells](design_and_technology_co_optimization_utilizing_flip_fet_ffet_standard_cells.md) | 本文面向3nm以下FFET堆叠器件提出DTCO协同优化流程，设计多引脚分布标准单元生成器，布局阶段单元替换消除Tap单元，双层布线拥塞均衡。7nm ASAP工艺测试，FFET单元相较CFET面积缩减20%~25%，完整流程相比传统CFET流片面积降26%，布线DR违规大幅减少，总线长降低9%。 |
| [用于电路设计的多智能体良率分析<br>Multi-Agent Yield Analysis For Circuit Design](multi_agent_yield_analysis_for_circuit_design.md) | 本文提出基于大模型多智能体良率分析框架YieldAgent，构建三层分层智能体架构，结合RAG领域知识库与TPE超参自适应优化，可按电路、工艺、精度动态组合采样算法。40/12nm 6T-SRAM测试，同等误差下仿真量最高缩减2.9倍，跨拓扑、工艺泛化能力优于传统MC与各类重要采样方法。 |
| [YAP：先进封装的良率建模与仿真<br>YAP: Yield Modeling and Simulation for Advanced Packaging](yap_yield_modeling_and_simulation_for_advanced_packaging.md) | 本文提出面向W2W、D2W混合键合的近解析良率模型YAP，建模套刻误差、铜凹陷、颗粒缺陷三类失效机制，配套物理仿真器做验证。相比高精度仿真速度提升万倍且误差极小，通过多组案例对比两种键合工艺良率差异，支撑先进封装工艺与芯片协同优化。 |
| [SDM-PEB：用于增强曝光后烘烤仿真的空间深度Mamba方法<br>SDM-PEB: Spatial-Depthwise Mamba for Enhanced Post-Exposure Bake Simulation](sdm_peb_spatial_depthwise_mamba_for_enhanced_post_exposure_bake_simulation.md) | 本文提出SDM-PEB深度学习框架用于光刻曝光后烘烤仿真，分层特征提取搭配空间深度Mamba单元捕捉三维光刻胶层间依赖，设计PEB焦点损失与深度散度正则解决数据失衡。28nm工艺测试，相较SOTA DeePEB抑制剂NRMSE降低35%，仿真速度较商用S-Litho快138倍，关键尺寸误差显著下降。 |
| [ChipletEM：基于耦合应力与热仿真的物理驱动2.5D/3D芯粒集成电迁移签核工具<br>ChipletEM: Physics-Based 2.5D and 3D Chiplet Integration Electromigration Signoff Tool Using Coupled Stress and Thermal Simulation](chipletem_physics_based_2_5d_and_3d_chiplet_integration_electromigration_signoff_tool_using_coupled_stress_and_thermal_simulation.md) | 本文提出面向2.5D/3D芯粒异构集成的电迁移签核工具ChipletEM，融合FVM电热协同求解与FDTD应力求解，耦合电迁移、热迁移、焦耳热多物理场，覆盖空洞成核与生长全阶段。单TSV仿真相较AFD方法误差从22.22%降至5.24%，9芯粒系统仿真证实高功耗模式TSV失效风险显著更高。 |
## EDA9：测试设计与硅生命周期管理 (6)

EDA9: Design for Test and Silicon Lifecycle Management


### 从测试到SLM高级解决方案 (6)

From Test to SLM Advanced Solutions

- Session Chairs: Savita Banerjee, Jing-Jia Liou

> 本次会议涵盖了一系列创新解决方案，包括：如何最大化老化SRAM的预测准确性；如何利用机器学习生成现场自测试库；如何进一步优化并行故障模拟与测试压缩的性能；如何在工艺变化下优化NOC的效率；以及如何提高微流体MUX的容错能力。

> This session covers a range of innovative solutions including, how to maximize the prediction accuracy for aging SRAMs; how to utilize machine learning in generating in-field self-test libraries; how to further optimize the performance of parallel fault simulation and test compaction; how to optimize the efficiency of NOCs under process variation; and how to improve the fault tolerance of the microfluidic MUXs.


| 中英论文题目 | 研究概要 |
|------------|-----------|
| [用于SRAM老化的非对称预测测试<br>Asymmetric Predictive Testing for Aging in SRAMs](asymmetric_predictive_testing_for_aging_in_srams.md) | 本文提出SRAM非对称老化预测测试方法，针对缓存多存0引发BTI非对称老化、传统对称字线电压测试过测严重问题，读写0/1施加差异化字线偏压；配套改进重要采样蒙特卡洛仿真。在0.2%欠测约束下，读破坏故障过测降低3.4倍，延迟故障降低2.5倍，综合故障场景降幅达3~5倍，仿真收敛速度提升5倍。 |
| [机器学习驱动的STL生成以增强E/E系统功能安全<br>Machine Learning-Driven STL Generation for Enhancing Functional Safety of E/E Systems](machine_learning_driven_stl_generation_for_enhancing_functional_safety_of_e_e_systems.md) | 本文面向汽车等安全关键E/E系统，提出VAE+RL混合驱动的自动自测试库(STL)生成框架。规避ATPG/BIST侵入式停机测试，生成功能测试向量用于空闲时段在线检测。基于多款工业模块验证，相较随机向量故障覆盖率最高提升57.57，测试效率提升85%，符合ISO26262功能安全规范。 |
| [EPICS：通过强连通分量实现时序电路高效并行模式故障仿真<br>EPICS: Efficient Parallel Pattern Fault Simulation for Sequential Circuits via Strongly Connected Components](epics_efficient_parallel_pattern_fault_simulation_for_sequential_circuits_via_strongly_connected_components.md) | 本文提出EPICS并行模式故障仿真框架，针对时序电路SCC强连通分量瓶颈，融合小回路编译仿真、入度分层展开、惰性事件传播三类优化。工业RISC-V与ITC基准测试，相比商用Z01X平均提速5.94倍，事件量大幅削减且故障覆盖率完全一致。 |
| [PastATPG：基于部分赋值SAT实现更优测试压缩的混合ATPG框架<br>PastATPG: A Hybrid ATPG Framework for Better Test Compaction with Partial Assignment SAT](pastatpg_a_hybrid_atpg_framework_for_better_test_compaction_with_partial_assignment_sat.md) | 本文提出混合ATPG框架PastATPG，自研PA-MiniSat部分赋值SAT求解器。采用全文字监视与电路自适应分支策略生成含大量X不定位测试向量，统一融合结构与SAT测试压缩流程。标准电路测试，向量数量平均降幅超36%，中小电路速度优于商用ATPG工具。 |
| [面向波长路由片上光网络的工艺偏差感知设计优化<br>Process-Variation-Aware Design Optimization for Wavelength-Routed Optical Networks-on-Chip](process_variation_aware_design_optimization_for_wavelength_routed_optical_networks_on_chip.md) | 本文面向波长路由光片上网络(WRONoC)工艺偏差问题，建立微环谐振器(MRR)传输期望解析模型，提出ILP全局优化与适配模拟退火算法，协同优化MRR半径与信号波长，最大化最坏期望传输效率。Light/Snake等拓扑测试，相比不考虑工艺偏差的标称方案，传输损耗最高改善7.51dB。 |
| [FT-MUX：一种容错微流控多路复用器<br>FT-MUX: A Fault-Tolerant Microfluidic Multiplexer](ft_mux_a_fault_tolerant_microfluidic_multiplexer.md) | 本文提出FT-MUX容错微流控多路复用器设计，针对通道阻塞、泄漏两类缺陷推导通用容错编码规则，将设计转化二元等重码最大独立集MIP求解。相比传统冗余备份方案资源效率提升数百倍，10根以上控制通道下，单容错FT-MUX流量通道数量优于无故障标准MUX，规模越大优势越显著。 |
