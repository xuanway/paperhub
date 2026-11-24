# SwiftMPC: Accelerating ML under MPC with Secure-Chip-Assisted One-Way Communication

**中文标题**：SwiftMPC：借助安全芯片辅助的单向通信加速 MPC 下的机器学习

**所属 Session**：[Session 12: Security and Privacy](index.md) · [ATC 2026](../index.md)

**作者**：Tianze Song (Zhejiang University), Chengkun Wei (Zhejiang University), Yichen Tu (Alibaba Cloud), Yangming Zhang (Alibaba Cloud), Heng Cai (Alibaba Cloud), Haiyuan Gao (Alibaba Cloud), Yuyang Cui (Tianjin University), Minghong Tang (Zhejiang University), Jin Shi (Zhejiang University), Tong Chen (Zhejiang University), Yin Zhang (Zhejiang University), Wei Wang (Alibaba Group), Wenzhi Chen (Zhejiang University)

## 英文摘要
Secure multi-party computation (MPC) is a promising foundation for privacy-preserving machine learning. Its deployment for modern ML is limited by communication: Beaver-based multiplication requires bidirectional communication that places network latency directly on the critical path. We present SwiftMPC, a secure-chip-assisted MPC architecture built on a simple protocol insight: if one party sets its first two Beaver-triple components equal to its existing input shares, that party’s masked differences become identically zero and need not be transmitted. Secure multiplication thus becomes one-way, letting communication and computation be pipelined. Such triples cannot be precomputed cryptographically, nor supplied by a trusted third party without reintroducing a round trip. SwiftMPC instead generates them with a secure chip attached to one participant. The chip plays a narrow, fixed-function role limited to triple generation, keeping it simple to verify. We implement SwiftMPC with an FPGA secure-chip prototype and a drop-in runtime compatible with PyTorch-style programming. To better support machine-learning workloads, SwiftMPC further generates Beaver triples at matrix granularity, which reduces triple consumption and communication volume for dominant ML operators. Across representative ML workloads, SwiftMPC completes ResNet-18 inference in 2.22 s at 65 ms network latency, achieving up to 1.64× speedup over the strongest prior hardware-assisted MPC design and up to 125× over software-only MPC.

## 中文摘要
安全多方计算（MPC）是隐私保护机器学习的一项有前景的基础技术。其面向现代机器学习的部署受限于通信：基于 Beaver 三元组的乘法需要双向通信，使网络延迟直接位于关键路径上。我们提出 SwiftMPC，一种安全芯片辅助的 MPC 架构，它建立在一条简洁的协议洞见之上：如果某一方将其 Beaver 三元组的前两个分量设为其已有的输入份额，则该方的掩码差值恒为零，无需传输。于是安全乘法变为单向，使通信与计算得以流水化。这样的三元组既无法通过密码学方式预计算，也无法由可信第三方提供而不重新引入一次往返。SwiftMPC 改为借助附加在某一参与方上的安全芯片来生成它们。该芯片扮演受限的固定功能角色，仅限于三元组生成，从而保持易于验证。我们用 FPGA 安全芯片原型实现了 SwiftMPC，并提供了与 PyTorch 风格编程兼容的可直接替换的运行时。为更好地支持机器学习负载，SwiftMPC 进一步以矩阵为粒度生成 Beaver 三元组，从而减少主要 ML 算子的三元组消耗与通信量。在代表性 ML 负载上，SwiftMPC 在 65 ms 网络延迟下用 2.22 s 完成 ResNet-18 推理，相比最强的已有硬件辅助 MPC 设计最高取得 1.64 倍加速，相比纯软件 MPC 最高取得 125 倍加速。

## 英文关键词
Secure multi-party computation, Privacy-preserving machine learning

## 中文关键词
安全多方计算，隐私保护机器学习

[返回 Session 12](index.md) · [返回 ATC 2026](../index.md)
