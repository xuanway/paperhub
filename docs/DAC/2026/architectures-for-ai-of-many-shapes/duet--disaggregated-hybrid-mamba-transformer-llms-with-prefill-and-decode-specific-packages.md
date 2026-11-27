DUET: Disaggregated Hybrid Mamba-Transformer LLMs with Prefill and Decode-Specific Packages
Authors：
[Alish Kanani](https://63dac.conference-program.com/?post_type=page&p=15&uid=1978385912665544943)，[Sangwan Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=0213115296925408431)，[Han Lyu](https://63dac.conference-program.com/?post_type=page&p=15&uid=828409039887576086)，[Jiahao Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=22728027717748567541)，[Jaehyun Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=97353370529684002471)，[Umit Ogras](https://63dac.conference-program.com/?post_type=page&p=15&uid=294443)

## 中文标题

DUET：采用预填充与解码专用封装的解耦式混合 Mamba-Transformer LLM

## 英文摘要

Large language models operate in distinct compute-bound prefill followed by memory bandwidth-bound decode phases. Hybrid Mamba– Transformer models inherit this asymmetry while adding state-space model (SSM) recurrences and element-wise operations that map poorly to matmul-centric accelerators. This mismatch causes performance bottlenecks, showing that a homogeneous architecture cannot satisfy all requirements. We introduce DUET, a disaggregated accelerator that assigns prefill and decode phases to specialized packages. The Prefill package uses systolic array chiplets with off-package memory for efficient large matrix multiplications and long-sequence SSMs. The Decode package uses vector-unit arrays with high-bandwidth in-package memory to accelerate token-by-token SSM and vector–matrix multiplications. Both architectures are runtime configurable to support hybrid models with mixed Mamba and attention layers. Evaluations on Nemotron-H-56B, Zamba2-7B, and Llama3-8B across four workloads show that DUET achieves 4× faster time to first token, 1.4× higher throughput, and 1.5× lower time between tokens over the B200 GPU.

## 中文摘要

大型语言模型的运行分为两个截然不同的阶段：先是计算密集的预填充阶段，随后是内存带宽密集的解码阶段。混合 Mamba–Transformer 模型继承了这种不对称性，同时还引入了状态空间模型（SSM）递推与逐元素运算，而这些运算难以映射到以矩阵乘法为中心的加速器上。这种失配造成了性能瓶颈，表明单一同构架构无法满足全部需求。我们提出 DUET，一种将预填充与解码阶段分配给专用封装的解耦加速器。预填充封装采用带有封装外存储的脉动阵列芯粒，以高效完成大规模矩阵乘法与长序列 SSM。解码封装采用带有高带宽封装内存储的向量单元阵列，以加速逐 token 的 SSM 与向量—矩阵乘法。两种架构均可在运行时重配置，以支持混合 Mamba 层与注意力层的混合模型。在 Nemotron-H-56B、Zamba2-7B 与 Llama3-8B 上跨四种工作负载的评估表明，相较于 B200 GPU，DUET 实现了 4× 更快的首 token 时间、1.4× 更高的吞吐以及 1.5× 更低的 token 间时间。
