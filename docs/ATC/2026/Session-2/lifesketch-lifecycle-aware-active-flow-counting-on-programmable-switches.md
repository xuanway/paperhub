# LifeSketch: Lifecycle-aware Active Flow Counting on Programmable Switches

**中文标题**：LifeSketch：可编程交换机上生命周期感知的活跃流计数

**所属 Session**：[Session 2: Network Measurement and Simulation](index.md) · [ATC 2026](../index.md)

**作者**：He Huang (Soochow University), Hanwen Zhang (Soochow University), Yang Du (Soochow University), Jia Liu (Nanjing University), Zhongjun Qiu (Soochow University), Yu-E Sun (Soochow University), Yao Tian (The Hong Kong University of Science and Technology), Xiaofang Zhou (The Hong Kong University of Science and Technology), Fu Xiao (Nanjing University of Posts and Telecommunications)

## 英文摘要
Accurate active flow counting is critical for network security and management tasks like DDoS detection and load balancing. Existing sketches approximate active flows as those seen within a fixed or sliding window, systematically misestimating flows due to their inability to track true lifecycle states: they undercount long-lived low-rate flows and overcount short-lived ones due to residual entries. We present LifeSketch, the first hardware-deployable sketch that enables lifecycle-aware active flow counting, bridging the gap between theoretical cardinality estimation and operational needs for real-time lifecycle awareness in high-speed network measurement. LifeSketch explicitly models per-flow state transitions (i.e., active, timeout, and closed) with 𝑂(1) insertion and deletion operations. It combines adaptive flow sampling, a virtual bucket array for compact per-flow state tracking, and a rejuvenation mechanism to stabilize performance under traffic dynamics. We derive a tight error bound and implement LifeSketch on an Intel Tofino switch, overcoming data plane constraints such as circular dependencies. Evaluations on real-world traces show LifeSketch reduces estimation error by up to 46.73× compared to state-of-the-art methods while maintaining line-rate processing.

## 中文摘要
准确的活跃流计数对于 DDoS 检测和负载均衡等网络安全与管理任务至关重要。现有草图把活跃流近似为在固定窗口或滑动窗口内出现过的流，由于无法跟踪真实的生命周期状态而系统性地误估流：它们低估长寿命低速率流，又因残留表项而高估短寿命流。我们提出 LifeSketch，这是首个可硬件部署、能够实现生命周期感知的活跃流计数的草图，弥合了理论基数估计与高速网络测量中对实时生命周期感知的运维需求之间的差距。LifeSketch 以 O(1) 的插入与删除操作显式建模每条流的状态转移（即活跃、超时和关闭）。它结合了自适应流采样、用于紧凑地逐流跟踪状态的虚拟桶数组，以及一种在流量动态变化下稳定性能的复新机制。我们推导了紧致的误差界，并在 Intel Tofino 交换机上实现了 LifeSketch，克服了循环依赖等数据平面约束。在真实世界流量轨迹上的评估表明，与最先进方法相比，LifeSketch 将估计误差最多降低 46.73×，同时保持线速处理。

## 英文关键词
Active flow counting, Flow lifecycle, Programmable networks, Sketching

## 中文关键词
活跃流计数，流生命周期，可编程网络，草图

[返回 Session 2](index.md) · [返回 ATC 2026](../index.md)
