TAMI-MPC: Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference
Authors：
[Zhuoran Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7191674866925192491)，[Hanieh TotonchiAsl](https://63dac.conference-program.com/?post_type=page&p=15&uid=2985932996357231337)，[Yifei Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=23820597004335093861)，[Ebrahim Nouri](https://63dac.conference-program.com/?post_type=page&p=15&uid=48400822746109524851)，[Danella Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5738091544249027789)

## 中文标题

TAMI-MPC：面向高效非线性推理的最小交互 MPC 可信加速

## 英文摘要

Secure multi-party computation (MPC) offers a practical foundation for privacy-preserving machine learning at the edge. However, current MPC systems rely heavily on communication and computation-intensive primitives—such as secure comparison-for nonlinear inference, which are often impractical on resource-constrained platforms. To enable real-time inference under resource-constrained platform, we introduce a Trusted Acceleration of Minimal-Interaction MPC framework, TAMI-MPC, for nonlinear evaluation. Specifically, we reduce communication cost by redesigning the core primitives, leaf comparison and tree merge, reducing the interactive round from log2 𝑛to just 1 per operation. Furthermore, unlike prior work that heavily relies on oblivious transfer (OT), a well-known computational bottleneck, we leverage synchronized seeds inside the TEE to eliminate OT for the vast majority of our designs, along with a correlated-randomness reuse technique that keeps new designs computationally lightweight. To fully realize the potential, we design a specialized accelerator that restructures the dataflow across stages to enable continuous, fine-grained streaming and high parallelism, reducing memory overhead. Our design achieves up to 4.86× speedup on ResNet-50 inference, compared with state-of-the-art CNN frameworks, and achieves up to 7.44× speedup on BERT-base inference, compared with state-of-the-art LLM frameworks.

## 中文摘要

安全多方计算（MPC）为边缘端的隐私保护机器学习提供了实用基础。然而，当前 MPC 系统严重依赖通信与计算密集型原语——例如用于非线性推理的安全比较——这些原语在资源受限平台上往往并不实用。为在资源受限平台上实现实时推理，我们提出一种面向非线性求值的最小交互 MPC 可信加速框架 TAMI-MPC。具体而言，我们通过重新设计核心原语（叶比较与树合并）来降低通信开销，将每次操作的交互轮数从 log2 n 减少到仅 1 轮。此外，与先前严重依赖不经意传输（OT，一个众所周知的计算瓶颈）的工作不同，我们利用 TEE 内部的同步种子在绝大多数设计中消除 OT，并结合相关随机性重用技术，使新设计保持计算轻量。为充分释放潜力，我们设计了一个专用加速器，重构跨阶段的数据流以实现连续、细粒度的流式传输和高并行性，从而降低内存开销。与最先进的 CNN 框架相比，我们的设计在 ResNet-50 推理上实现最高 4.86× 的加速；与最先进的 LLM 框架相比，在 BERT-base 推理上实现最高 7.44× 的加速。

## 英文关键词

Security & Privacy, Multiparty Computation, Trusted Execution Environment, FPGA acceleration

## 中文关键词

安全与隐私、多方计算、可信执行环境、FPGA 加速
