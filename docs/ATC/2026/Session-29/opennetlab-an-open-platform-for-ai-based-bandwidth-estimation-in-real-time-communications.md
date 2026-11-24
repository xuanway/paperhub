# OpenNetLab: An Open Platform for AI-Based Bandwidth Estimation in Real-Time Communications

**中文标题**：OpenNetLab：面向实时通信中基于 AI 的带宽估计的开放平台

**所属 Session**：[Session 29: Networking II](index.md) · [ATC 2026](../index.md)

**作者**：Wenxue Cheng (Microsoft Research), Jeongyoon Eo (Seoul National University & Microsoft Research), Zhixiong Niu (Microsoft Research), Francis Y. Yan (University of Illinois Urbana-Champaign), Rui Gao (Microsoft Research), Ze Gan (Microsoft), Scott Inglis (Microsoft), Vishak Gopal (Microsoft), Byung-Gon Chun (Seoul National University), Ran Shu (Microsoft Research), Peng Cheng (Microsoft Research), Yongqiang Xiong (Microsoft Research)

## 英文摘要
Real-time communications (RTC), such as video conferencing and cloud gaming, rely on bandwidth estimation (BWE) to balance throughput, delay, and loss under diverse network conditions and media workloads. AI-based BWE is a promising direction beyond hand-tuned rules, but progress remains slow and fragmented because each project must rebuild the system support around the model itself: a real RTC stack for running models; environments for training, validation, and real-world evaluation; and artifacts for comparing and improving models. This paper presents OpenNetLab, an open platform for AI-based BWE in RTC. At its core, OpenNetLab provides simulator, emulator, and real-node runtimes for training, validation, and real-world evaluation. The three runtimes share AlphaRTC, which combines the WebRTC stack with a common AI-BWE interface, while runtime-specific Media and Network Engines meet the workflow’s efficiency and fidelity requirements through fast simulation, real-stack emulation, and live-Internet execution. A shared Benchmark defines reproducible cases and metrics, while Open Artifacts support independent deployment, community sharing and contributions, and continual benchmark updates. We evaluate OpenNetLab through matched-replay execution fidelity, training efficiency, and benchmark comparability. A 600-case matched-replay study shows small gaps in network and media outcomes between the OpenNetLab emulator and a WebRTC reference. A PPO training run compresses about 194 call-hours into 23 minutes of simulator time, a roughly 497× speedup. OpenNetLab has powered the MMSys 2021 BWE Challenge and has been used in subsequent published RTC research.

## 中文摘要
视频会议与云游戏等实时通信（RTC）依赖带宽估计（BWE）来在多样化的网络条件与媒体工作负载下平衡吞吐、延迟与丢包。基于 AI 的 BWE 是超越手工调优规则的一个有前景的方向，但其进展仍然缓慢且碎片化，因为每个项目都必须围绕模型本身重建系统支撑：用于运行模型的真实 RTC 协议栈、用于训练、验证与真实世界评估的环境，以及用于比较和改进模型的制品。本文提出 OpenNetLab，一个面向 RTC 中基于 AI 的 BWE 的开放平台。OpenNetLab 的核心是为训练、验证与真实世界评估提供模拟器、仿真器与真实节点运行时。这三种运行时共享 AlphaRTC，后者将 WebRTC 协议栈与通用的 AI-BWE 接口相结合，而各运行时专用的媒体引擎与网络引擎则通过快速模拟、真实协议栈仿真与真实互联网执行来满足工作流对效率与保真度的要求。共享的基准（Benchmark）定义了可复现的用例与指标，而开放制品（Open Artifacts）支持独立部署、社区共享与贡献以及基准的持续更新。我们通过匹配重放（matched-replay）的执行保真度、训练效率与基准可比性来评估 OpenNetLab。一项 600 用例的匹配重放研究表明，OpenNetLab 仿真器与 WebRTC 参考实现在网络与媒体结果上差距很小。一次 PPO 训练运行将约 194 通话小时压缩为 23 分钟的模拟器时间，约合 497× 的加速。OpenNetLab 已支撑 MMSys 2021 BWE Challenge，并已被后续发表的 RTC 研究所使用。

## 英文关键词
Bandwidth Estimation, Real-Time Communications, AI-Based Networking

## 中文关键词
带宽估计，实时通信，AI 网络

[返回 Session 29](index.md) · [返回 ATC 2026](../index.md)
