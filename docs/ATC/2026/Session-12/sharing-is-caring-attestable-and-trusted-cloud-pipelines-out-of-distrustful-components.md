# Sharing is caring: Attestable and Trusted Cloud Pipelines out of Distrustful Components

**中文标题**：共享即关怀：由互不信任组件构建可认证且可信的云流水线

**所属 Session**：[Session 12: Security and Privacy](index.md) · [ATC 2026](../index.md)

**作者**：Amir Al Sadi (Imperial College London), Sina Abdollahi (Imperial College London), Adrien Ghosn (Microsoft Azure Research), Hamed Haddadi (Imperial College London), Marios Kogias (Imperial College London)

## 英文摘要
The trust model underlying today’s Trusted Execution Environments (TEEs) is inadequate for modern confidential workloads. TEEs protect private memory and attest initial code and configuration, but they neither constrain nor attest the shared channels through which data enters, leaves, or flows between TEEs or with the untrusted host. As a result, confidentiality remains coupled to trust in the functional correctness of all in-TEE code that may access those channels. This trust assumption is increasingly untenable for agentic applications that generate code at runtime and for cloud pipelines composed of mutually distrustful components. A single misuse of a shared channel is enough to leak confidential data and compromise the entire pipeline. We present Mica, a confidential-computing architecture firmware extension that decouples confidentiality from trust in in-TEE code. Mica lets tenants explicitly define, restrict, and attest channel constraints between TEEs and with the untrusted host, including transitive constraints that span an entire pipeline. It further extends attestation from individual TEEs to groups of communicating TEEs, allowing external parties to verify the confidentiality properties induced by those constraints across a whole pipeline. We implement Mica on Arm CCA by extending the Realm Management Monitor with a small policy language, requiring no hardware changes and only minor changes to QEMU and KVM. Our evaluation shows that Mica supports modern confidential agentic applications and pipeline computations without requiring trust in the functional correctness of in-TEE code. Our implementation increases the TCB by only 7% and incurs infrequent setup costs: 2–4% boot-time overhead, approximately 1.5 s for policy upload, and 246–598 ms for group attestation. Once established, Realm communication is direct, uses protected memory, and requires no Mica intervention or software encryption leading to up to 14.5× lower cross-TEE message latency than encrypted communication over untrusted memory.

## 中文摘要
当今可信执行环境（TEE）所依据的信任模型已不足以支撑现代机密负载。TEE 保护私有内存并认证初始代码与配置，但它们既不约束也不认证数据进入、离开 TEE 或在 TEE 之间及与不可信主机之间流动所经过的共享通道。因此，机密性仍然取决于对所有可能访问这些通道的 TEE 内代码的功能正确性的信任。对于在运行时生成代码的智能体应用，以及由互不信任组件构成的云流水线而言，这种信任假设越来越站不住脚。对共享通道的一次误用就足以泄露机密数据并危及整条流水线。我们提出 Mica，一种机密计算架构的固件扩展，它将机密性与对 TEE 内代码的信任解耦。Mica 允许租户显式地定义、限制并认证 TEE 之间以及与不可信主机之间的通道约束，包括跨越整条流水线的传递性约束。它进一步将认证从单个 TEE 扩展到相互通信的 TEE 组，使外部方能够验证这些约束在整条流水线上所施加的机密性属性。我们在 Arm CCA 上实现 Mica，通过一种小型策略语言扩展 Realm Management Monitor，无需硬件改动，仅需对 QEMU 和 KVM 做少量修改。我们的评测表明，Mica 能够支持现代机密智能体应用与流水线计算，而无需信任 TEE 内代码的功能正确性。我们的实现仅使 TCB 增加 7%，并带来不频繁的初始化开销：2–4% 的启动时间开销、约 1.5 s 的策略上传，以及 246–598 ms 的组认证。一旦建立，Realm 间通信是直接的，使用受保护内存，无需 Mica 介入或软件加密，相比在不可信内存上的加密通信，跨 TEE 消息延迟最多降低 14.5 倍。

## 英文关键词
Confidential Computing, Trusted Execution Environment, Attestation

## 中文关键词
机密计算，可信执行环境，远程证明

[返回 Session 12](index.md) · [返回 ATC 2026](../index.md)
