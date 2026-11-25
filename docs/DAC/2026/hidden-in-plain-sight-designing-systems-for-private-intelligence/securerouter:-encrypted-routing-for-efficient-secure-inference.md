Securerouter: Encrypted Routing for Efficient Secure Inference
Authors：
[Yukuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8720484507161708868)，[Mengxin Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=7043608771704783242)，[Qian Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=59469293988581540311)

## 中文标题

SecureRouter：面向高效安全推理的加密路由

## 英文摘要

Cryptographically secure neural network inference typically relies on secure computing techniques such as Secure Multi-Party Computation (MPC), enabling cloud servers to process client inputs without decrypting them. Although prior privacy-preserving inference systems co-design network optimizations with MPC, they remain slow and costly, limiting real-world deployment. A major bottleneck is their use of a single, fixed transformer model for all encrypted inputs, ignoring that different inputs require different model sizes to balance efficiency and accuracy. We present SecureRouter, an end-to-end encrypted routing and inference framework that accelerates secure transformer inference through input-adaptive model selection under encryption. SecureRouter establishes a unified encrypted pipeline that integrates a secure router with an MPC-optimized model pool, enabling coordinated routing, inference, and protocol execution while preserving full data and model confidentiality. The framework includes training-phase and inference-phase components: an MPC-cost-aware secure router that predicts per-model utility and cost from encrypted features, and an MPC-optimized model pool whose architectures and quantization schemes are co-trained to minimize MPC communication and computation overhead. Compared to prior work, SecureRouter achieves a latency reduction by 1.95× with negligible accuracy loss, offering a practical path toward scalable and efficient secure AI inference. Our open-source implementation is available at: https://github.com/UCF-ML-Research/SecureRouter

## 中文摘要

密码学安全的神经网络推理通常依赖安全多方计算（MPC）等安全计算技术，使云服务器能够在不解密的情况下处理客户端输入。尽管此前的隐私保护推理系统将网络优化与 MPC 协同设计，但它们仍然速度慢、成本高，限制了实际部署。一个主要瓶颈在于它们对所有加密输入都使用单一固定的 Transformer 模型，忽视了不同输入需要不同模型规模以平衡效率与精度。我们提出 SecureRouter，一个端到端的加密路由与推理框架，通过加密条件下的输入自适应模型选择来加速安全 Transformer 推理。SecureRouter 建立了统一的加密流水线，将安全路由器与经 MPC 优化的模型池集成，从而在保持数据与模型完全机密性的同时，实现路由、推理与协议执行的协同。该框架包含训练阶段与推理阶段的组件：一个 MPC 成本感知的安全路由器，可从加密特征预测每个模型的效用与成本；以及一个经 MPC 优化的模型池，其架构与量化方案经过协同训练以最小化 MPC 的通信与计算开销。与此前工作相比，SecureRouter 在精度损失可忽略的情况下将延迟降低 1.95 倍，为可扩展、高效的安全 AI 推理提供了可行路径。我们的开源实现见：https://github.com/UCF-ML-Research/SecureRouter
