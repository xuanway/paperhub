Orchestrating Dual-Boundaries: An Arithmetic Intensity Inspired Acceleration Framework for Diffusion Language Models
Authors：
[Linye Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=94815805530050268521)，[Wenjue Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3350911479021902453)，[Pingzhi Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2317903889740444707)，[Xiaotian Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=6673128660125261626)，[Le Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=845343)，[Runsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=214343)，[Meng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=414843)

## 中文标题

统筹双重边界：一种受运算强度启发的扩散语言模型加速框架

## 英文摘要

Diffusion-based large language models (dLLMs) have recently gained significant attention for their exceptional performance and inherent potential for parallel decoding. Existing frameworks further enhance its inference efficiency by enabling KV caching. However, its bidirectional attention mechanism necessitates periodic cache refreshes that interleave prefill and decoding phases, both contributing substantial inference cost and constraining achievable speedup. Inspired by the heterogeneous arithmetic intensity of the prefill and decoding phases, we propose ODB-dLLM, a framework that orchestrates dual-boundaries to accelerate dLLM inference. In the prefill phase, we find that the predefined fixed response length introduces heavy yet redundant computational overhead, which affects efficiency. To alleviate this, ODB-dLLM incorporates an adaptive length prediction mechanism that progressively reduces prefill overhead and unnecessary computation. In the decoding phase, we analyze the computational characteristics of dLLMs and propose a dLLM-specific jump-share speculative decoding method to enhance efficiency by reducing the number of decoding iterations. Experimental results demonstrate that ODB-dLLM achieves 46–162× and 2.63–6.30× speedups over the baseline dLLM and Fast-dLLM, respectively, while simultaneously mitigating the accuracy degradation in existing acceleration frameworks.

## 中文摘要

基于扩散的大语言模型（dLLM）近期因其卓越性能与固有的并行解码潜力而备受关注。现有框架进一步通过 KV 缓存提升其推理效率。然而，其双向注意力机制需要周期性刷新缓存，使预填充与解码阶段交替进行，二者都带来可观的推理开销并限制了可获得的加速比。受预填充与解码阶段运算强度差异的启发，我们提出 ODB-dLLM，一个通过统筹双重边界来加速 dLLM 推理的框架。在预填充阶段，我们发现预设的固定响应长度会引入沉重而冗余的计算开销，影响效率。为此，ODB-dLLM 引入自适应长度预测机制，逐步降低预填充开销与不必要的计算。在解码阶段，我们分析了 dLLM 的计算特性，并提出一种 dLLM 专用的 jump-share 投机解码方法，通过减少解码迭代次数提升效率。实验结果表明，ODB-dLLM 相较基线 dLLM 和 Fast-dLLM 分别实现 46–162 倍和 2.63–6.30 倍的加速，同时缓解了现有加速框架中的精度下降问题。
