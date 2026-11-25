Can Asymmetric Tile Buffering Be Beneficial?
Authors：
[Chengyue Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8677830577208473082)，[Qiran Pang](https://63dac.conference-program.com/?post_type=page&p=15&uid=56156708785528325221)，[Xinrui Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3493096508602149551)，[HyeGang Jun](https://63dac.conference-program.com/?post_type=page&p=15&uid=46533172545495942671)，[Luis Romero](https://63dac.conference-program.com/?post_type=page&p=15&uid=05579552172768078471)，[Endri Taka](https://63dac.conference-program.com/?post_type=page&p=15&uid=5690961798780556857)，[Diana Marculescu](https://63dac.conference-program.com/?post_type=page&p=15&uid=780743)，[Tony Nowatzki](https://63dac.conference-program.com/?post_type=page&p=15&uid=04283612955665418621)，[Pranathi Vasireddy](https://63dac.conference-program.com/?post_type=page&p=15&uid=67740365800935693241)，[Joseph Melber](https://63dac.conference-program.com/?post_type=page&p=15&uid=58586033885568565261)，[Deming Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=914343)，[Jason Cong](https://63dac.conference-program.com/?post_type=page&p=15&uid=322343)

## 中文标题

非对称分块缓冲是否有益？

## 英文摘要

General matrix multiplication (GEMM) is the computational backbone of modern AI workloads, and its efficiency is critically dependent on effective tiling strategies. Conventional approaches employ symmetric tile buffering, where the buffered tile size of the input 𝐴 along the dimension 𝑀matches the output tile size of 𝐶. In this paper, we introduce asymmetric tile buffering (ATB), a simple but powerful technique that decouples the buffered tile dimensions of the input and output operands. We show, for the first time, that ATB is both practical and highly beneficial. We develop an analytical model to show the benefits (higher arithmetic intensity) and costs (higher kernel switching costs) of ATB, providing insight into how to select effective ATB tiling factors. As a case study, we apply ATB to AMD’s latest XDNA2™AI Engine (AIE), establishing a new performance record for XDNA2™AIE.

## 中文摘要

通用矩阵乘法（GEMM）是现代 AI 工作负载的计算核心，其效率关键取决于有效的分块（tiling）策略。传统方法采用对称分块缓冲，即输入 𝐴 沿维度 𝑀 的缓冲块尺寸与输出 𝐶 的分块尺寸相同。本文提出非对称分块缓冲（ATB），一种简单却强大的技术，它解耦了输入与输出操作数的缓冲块维度。我们首次表明，ATB 既实用又极具收益。我们建立了一个分析模型来揭示 ATB 的收益（更高的算术强度）与代价（更高的内核切换开销），从而为如何选择有效的 ATB 分块因子提供了洞见。作为案例研究，我们将 ATB 应用于 AMD 最新的 XDNA2™ AI Engine（AIE），为 XDNA2™ AIE 创造了新的性能纪录。
