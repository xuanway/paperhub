Sparsee: Unlocking Sparsities in Encrypted Sparse Matrix Multiplication via Hardware-Software Co-Design
Authors：
[Yuntao Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=49014375452973569851)，[Xueyan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=851443)，[Song Bian](https://63dac.conference-program.com/?post_type=page&p=15&uid=0474161084960992769)，[Yier Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=0462365807378591021)，[Weisheng Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=061443)

## 中文标题

SparseE：通过软硬件协同设计释放加密稀疏矩阵乘法中的稀疏性

## 英文摘要

Sparse Matrix Multiplication (SpMM) suffers from substantial performance overhead in Fully Homomorphic Encryption (FHE)-based privacy-preserving computing, as encryption obscures matrix sparsity and forces dense computation. To overcome this limitation, we introduce SparseE, a hardware-software co-design framework that enables sparsity-aware SpMM under FHE. Our key contribution is a novel protocol that transforms SpMM into a secure Scatter-Gather-Apply workflow, where a homomorphic permutation network securely gathers data using encrypted indices. This approach ensures computational cost scales with the number of non-zero elements while fully preserving sparsity pattern confidentiality. To further boost performance, we co-design a dedicated accelerator featuring a Homomorphic Permutation Engine based on a hardware-efficient Benes topology—implemented as a Radix-2 Single-Delay Feedback pipeline of HSwitch units—to alleviate on-chip bandwidth constraints. In tandem, a Homomorphic Expansion Engine performs real-time decompression of selector ciphertexts, effectively mitigating storage bottlenecks. Extensive experiments across four representative applications show that SparseE achieves speedups ranging from 2.7× to 192.2×, and energy reductions from 15.5× to 251.5× over state-of-the-art hardware accelerators. The source code for this project is publicly available at https://github.com/yuntao-wei/SparseE.

## 中文摘要

在基于全同态加密（FHE）的隐私保护计算中，稀疏矩阵乘法（SpMM）承受巨大的性能开销，因为加密掩盖了矩阵稀疏性并迫使进行稠密计算。为克服这一局限，我们提出 SparseE，一个软硬件协同设计框架，在 FHE 下实现稀疏感知的 SpMM。我们的关键贡献是一种新颖协议，将 SpMM 转化为安全的“散布-收集-应用”工作流，其中同态置换网络利用加密索引安全地收集数据。该方法确保计算开销随非零元素数量增长，同时完全保持稀疏模式的机密性。为进一步提升性能，我们协同设计了一款专用加速器，其同态置换引擎基于硬件高效的 Benes 拓扑——以由 HSwitch 单元构成的 Radix-2 单延迟反馈流水线实现——以缓解片上带宽约束。同时，同态扩展引擎对选择器密文进行实时解压，有效缓解存储瓶颈。在四类代表性应用上的大量实验表明，SparseE 相较最先进硬件加速器实现 2.7–192.2 倍加速和 15.5–251.5 倍能耗降低。项目源代码公开于 https://github.com/yuntao-wei/SparseE。

## 英文关键词

Sparse Matrix Multiplication, Fully Homomorphic Encryption, Hardware-Software Co-Design, Privacy-Preserving Computing

## 中文关键词

稀疏矩阵乘法、全同态加密、软硬件协同设计、隐私保护计算
