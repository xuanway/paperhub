TRINE: A Token-Aware, Runtime-Adaptive FPGA Inference Engine for Multimodal AI
Authors：
[Hyunwoo Oh](https://63dac.conference-program.com/?post_type=page&p=15&uid=05645374820751851621)，[Hanning Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=902743)，[Sanggeon Yun](https://63dac.conference-program.com/?post_type=page&p=15&uid=49158696194380247701)，[Yang Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=4430450869797847541)，[Suyeon Jang](https://63dac.conference-program.com/?post_type=page&p=15&uid=68835759722959446361)，[Behnam Khaleghi](https://63dac.conference-program.com/?post_type=page&p=15&uid=015443)，[Fei Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=147143)，[Mohsen Imani](https://63dac.conference-program.com/?post_type=page&p=15&uid=377143)

## 中文标题

TRINE：面向多模态 AI 的令牌感知、运行时自适应 FPGA 推理引擎

## 英文摘要

Multimodal stacks that mix ViTs, CNNs, GNNs, and transformer NLP strain embedded platforms because their compute/memory patterns diverge and hard real-time targets leave little slack. TRINE is a single-bitstream FPGA accelerator and compiler that executes end-to-end multimodal inference without reconfiguration. Layers are unified as DDMM/SDDMM/SpMM and mapped to a mode-switchable engine that toggles at runtime among weight/output-stationary systolic, 1×CS SIMD, and a routable adder tree (RADT) on a shared PE array. A width-matched, two-stage top-k unit enables in-stream token pruning, while dependency-aware layer offloading (DALO) overlaps independent kernels across reconfigurable processing units to sustain utilization. Evaluated on Alveo U50 and ZCU104, TRINE reduces latency by up to 22.57× vs. RTX 4090 and 6.86× vs. Jetson Orin Nano at 20–21 W; token pruning alone yields up to 7.8× on ViT-heavy pipelines, and DALO contributes up to 79% throughput improvement. With int8 quantization, accuracy drops remain <2.5% across representative tasks, delivering state-of-the-art latency and energy efficiency for unified vision, language, and graph workloads—in one bitstream.

## 中文摘要

混合 ViT、CNN、GNN 与 Transformer NLP 的多模态栈给嵌入式平台带来巨大压力，因为它们的计算与访存模式存在差异，而硬实时目标又几乎没有余量。TRINE 是一个单比特流 FPGA 加速器兼编译器，无需重新配置即可执行端到端多模态推理。各层被统一为 DDMM/SDDMM/SpMM，并映射到一个模式可切换的引擎上，该引擎在共享 PE 阵列上于权重/输出驻留脉动架构、1×CS SIMD 与可路由加法树（RADT）之间在运行时切换。一个宽度匹配的两级 top-k 单元支持流内令牌剪枝，而依赖感知的层卸载（DALO）在可重构处理单元之间重叠独立内核，以维持利用率。在 Alveo U50 与 ZCU104 上评估，TRINE 在 20–21 W 功耗下相比 RTX 4090 降低延迟最高 22.57×，相比 Jetson Orin Nano 降低 6.86×；仅令牌剪枝一项就在 ViT 密集型流水线上带来最高 7.8× 的收益，DALO 则贡献最高 79% 的吞吐提升。采用 int8 量化后，代表性任务的准确率下降保持在 <2.5%，在单个比特流中为统一的视觉、语言与图负载提供了最先进的延迟与能效。
