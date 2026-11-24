# D-Pingmesh: Dynamic Probing and Fault Localization for Reconfigurable Datacenter Networks

**中文标题**：D-Pingmesh：可重构数据中心网络中的动态探测与故障定位

**所属 Session**：[Session 8: Data Center Networking](index.md) · [ATC 2026](../index.md)

**作者**：Yunze Wei (Tsinghua University), Kaicheng Yang (Huawei), Xiaohui Xie (Tsinghua University), Dunkai Mao (Tsinghua University), Peiying Tao (Huawei), Yikai Zhao (Huawei), Bolong Cui (Huawei), Chen Sun (Huawei), Bingyang Liu (Huawei), Kun Tan (Unaffiliated), Kai Chen (Hong Kong University of Science and Technology), Yong Cui (Tsinghua University)

## 英文摘要
Pingmesh monitors datacenter networks through periodic pings between servers. In reconfigurable datacenter networks, topology engineering (TPE) and traffic engineering (TE) make uniform server-pair probing inefficient: a pinglist wastes budget retesting common paths while missing low-probability interfaces. Frequent control-plane updates further require rapid pinglist refresh, and cause path ambiguity at control-plane boundaries for fault localization. We present D-Pingmesh, a probing and fault-localization system co-designed with the TPE/TE control plane. Its control-plane-aware generator builds task-efficient pinglists by greedily admitting probes with high interface coverage under the current TPE/TE snapshot. An incremental replay-and-repair mechanism updates pinglists across reconfigurations rather than recomputing from scratch. At control-plane boundaries, a Rho-EM localizer jointly infers per-task old/new-path mixture weights and the fault set through EM-style iteration. We evaluate D-Pingmesh on an 8-pod reconfigurable topology under dynamic TPE/TE. At a 0.99 coverage target, D-Pingmesh uses 17.7× fewer tasks than Pingmesh and generates each pinglist about 5.1× faster than RD-Probe. In ns-3 simulation, boundary-aware localization improves micro F1 from 0.871 to 0.953 over the deTector PLL baseline. A testbed deployment demonstrates second-scale fault localization with low host overhead. These results demonstrate that D-Pingmesh is practical for reconfigurable datacenter networks with control-plane-aware monitoring.

## 中文摘要
Pingmesh 通过服务器之间的周期性 ping 来监控数据中心网络。在可重构数据中心网络中，拓扑工程（TPE）与流量工程（TE）使统一的服务器对探测变得低效：一份 pinglist 会把预算浪费在重复测试常见路径上，同时遗漏低概率出现的接口。频繁的控制面更新进一步要求快速刷新 pinglist，并在控制面边界处给故障定位带来路径歧义。我们提出 D-Pingmesh，一个与 TPE/TE 控制面协同设计的探测与故障定位系统。其控制面感知的生成器通过贪心地接纳在当前 TPE/TE 快照下具有高接口覆盖度的探测，构建任务高效的 pinglist。一种增量式重放–修复机制在多次重配置之间更新 pinglist，而非从头重新计算。在控制面边界处，Rho-EM 定位器通过 EM 式迭代联合推断每个任务的旧路径/新路径混合权重与故障集合。我们在动态 TPE/TE 下的 8-pod 可重构拓扑上评估 D-Pingmesh。在 0.99 覆盖目标下，D-Pingmesh 使用的任务数比 Pingmesh 少 17.7×，且生成每份 pinglist 的速度比 RD-Probe 快约 5.1×。在 ns-3 仿真中，边界感知定位相较 deTector PLL 基线将 micro F1 从 0.871 提升至 0.953。测试床部署展示了秒级故障定位与较低的主机开销。这些结果表明，借助控制面感知的监控，D-Pingmesh 对可重构数据中心网络是实用的。

## 英文关键词
Reconfigurable datacenter networks, Active probing, Fault localization

## 中文关键词
可重构数据中心网络，主动探测，故障定位

[返回 Session 8](index.md) · [返回 ATC 2026](../index.md)
