Closing the Loop: Hybrid NAS Guided by Analytical and Hardware-Calibrated Quantum Cost Modeling
Authors：
[Muhammad Kashif](https://63dac.conference-program.com/?post_type=page&p=15&uid=525843)，[Alberto Marchisio](https://63dac.conference-program.com/?post_type=page&p=15&uid=363843)，[Muhammad Shafique](https://63dac.conference-program.com/?post_type=page&p=15&uid=560343)

## 中文标题

闭环设计：由解析式与硬件校准量子代价建模引导的混合 NAS

## 英文摘要

Hybrid quantum–classical neural networks (HQNNs) integrate quantum circuits with classical layers, each operating under fundamentally different computational paradigm, which makes hardware-resource estimation challenging. Also, the training of quantum circuits on real devices requires thousands of circuit executions, which is impractical on current NISQ devices. Therefore, most HQNNs are evaluated on classical simulators, with hardware cost approximated using floating-point operations (FLOPs). However, FLOPs and existing quantum resource estimation methods (e.g., gate counts) overlook key quantum hardware-specific factors such as gate durations, limited qubit connectivity, and noise, all of which ultimately determine the true cost and scalability of quantum circuits. In this paper, we propose an analytical quantum cost model that estimates quantum hardware resources using real backend calibration data, incorporating gate durations, routing overheads, and noise-induced sampling inefficiencies. To complement this, we develop a classical cost model that converts FLOPs into device-specific throughput, enabling a unified time-based representation of hardware-resource cost for both subsystems of HQNNs. Building on these analytical models, we present Hyb-HANAS, a hardware-aware hybrid neural architecture search framework, which jointly optimizes accuracy, hardware cost, and parameter count using NSGA-II. Hyb-HANAS identifies Pareto-optimal trade-offs and cross-domain co-adaptation between classical and quantum components of HQNNs. Beyond NAS, the proposed quantum analytical cost model is broadly applicable to quantum hardware benchmarking, compiler evaluation, and training-time estimation of quantum circuits on NISQ devices.

## 中文摘要

混合量子-经典神经网络（HQNN）将量子线路与经典层集成在一起，二者运行于根本不同的计算范式之下，这使得硬件资源估计颇具挑战。此外，在真实设备上训练量子线路需要数千次线路执行，这在当前 NISQ 设备上并不现实。因此，大多数 HQNN 都在经典模拟器上评估，其硬件代价用浮点运算次数（FLOPs）近似。然而，FLOPs 与现有量子资源估计方法（如门计数）忽略了量子硬件特有的关键因素，例如门持续时间、受限的量子比特连通性以及噪声，而这些因素最终决定了量子线路的真实代价与可扩展性。本文提出一种解析式量子代价模型，利用真实后端的校准数据来估计量子硬件资源，并将门持续时间、路由开销以及噪声引发的采样低效纳入其中。作为补充，我们开发了一个经典代价模型，将 FLOPs 转换为器件特定的吞吐率，从而为 HQNN 的两个子系统提供统一的、基于时间的硬件资源代价表示。基于这些解析模型，我们提出 Hyb-HANAS，一个硬件感知的混合神经架构搜索框架，它使用 NSGA-II 联合优化精度、硬件代价与参数量。Hyb-HANAS 能够识别帕累托最优折衷方案，并揭示 HQNN 中经典组件与量子组件之间的跨域协同适配关系。除 NAS 之外，所提出的量子解析代价模型还可广泛适用于量子硬件基准测试、编译器评估以及 NISQ 设备上量子线路的训练时间估计。
