# STRIDE: Efficient Secure Transformer Inference via Inter-Operator Protocol and Operator Co-Design

**中文标题**：STRIDE：通过算子间协议与算子协同设计的高效安全 Transformer 推理

**所属 Session**：[Session 26: LLM Inference III](index.md) · [ATC 2026](../index.md)

**作者**：Zhengyi Li (Shanghai Jiao Tong University), Yangjie Zhou (National University of Singapore), Zihan Liu (Shanghai Jiao Tong University), Ziyu Xiao (Shanghai Jiao Tong University), Kang Yang (State Key Laboratory of Cryptology), Jiaping Gui (Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University), Yun Lin (Shanghai Jiao Tong University), Jin Song Dong (National University of Singapore), Yu Yu (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University), Ning Liu (Shanghai Jiao Tong University), Jingwen Leng (Shanghai Jiao Tong University)

## 英文摘要
Secure inference based on homomorphic encryption (HE) and secure multi-party computation (MPC) protects both client inputs and model weights in GPT serving. Existing systems follow two paradigms: hybrid HE–MPC uses a type-driven heuristic that maps linear operators to HE and nonlinear operators to MPC, while fully homomorphic encryption (FHE) executes entirely in the ciphertext domain to eliminate communication. Despite strong security guarantees, both remain inefficient in practice. Our profiling shows that the primary bottleneck lies in inter-operator overhead rather than individual operator inefficiency: type-driven protocol assignment and locally optimized layouts leave substantial switching and layout-transformation costs. Stride targets this overhead through two inter-operator optimizations: protocol assignment that accounts for operator affinity and switching cost, and attention refinement that improves HE affinity while preserving layout compatibility with interleaved encoding and offline–online alignment. Beyond these inter-operator optimizations, Stride further accelerates the resulting HE-heavy execution through optimized polynomial evaluation and dependency-driven multi-GPU scheduling. On GPT-2 and LLaMA-7B across three network settings, Stride achieves up to 3.83× speedup over the faster of the two GPU-based baselines, Nexus and BLB, with one GPU per system. With four GPUs, Stride achieves up to 10.62× speedup over the same single-GPU baselines.

## 中文摘要
基于同态加密（HE）和安全多方计算（MPC）的安全推理在 GPT 服务中同时保护客户端输入与模型权重。现有系统遵循两种范式：混合 HE–MPC 使用类型驱动的启发式方法，将线性算子映射到 HE、非线性算子映射到 MPC；而全同态加密（FHE）完全在密文域执行以消除通信。尽管具备强安全保证，两者在实践中仍然低效。我们的剖析表明，主要瓶颈在于算子间开销，而非单个算子效率不足：类型驱动的协议分配和局部优化的布局留下了可观的切换与布局转换开销。Stride 通过两项算子间优化来针对这一开销：考虑算子亲和性与切换开销的协议分配，以及通过交错编码和离线—在线对齐在保持布局兼容性的同时提升 HE 亲和性的注意力细化。在这些算子间优化之外，Stride 还通过优化的多项式求值和依赖驱动的多 GPU 调度进一步加速由此形成的、以 HE 为主的执行。在 GPT-2 与 LLaMA-7B 上、跨三种网络设置，Stride 相比两个基于 GPU 的基线 Nexus 和 BLB 中较快者取得最高 3.83× 加速，此时每个系统各使用一块 GPU。使用四块 GPU 时，Stride 相比相同的单 GPU 基线取得最高 10.62× 加速。

## 英文关键词
Privacy-preserving Machine Learning, GPT, Homomorphic Encryption, Secure Multi-party Computation

## 中文关键词
隐私保护机器学习，GPT，同态加密，安全多方计算

[返回 Session 26](index.md) · [返回 ATC 2026](../index.md)
