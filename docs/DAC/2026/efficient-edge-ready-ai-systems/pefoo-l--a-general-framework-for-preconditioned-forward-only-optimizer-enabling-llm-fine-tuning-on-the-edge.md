Pefoo-L: A General Framework for Preconditioned Forward-Only Optimizer Enabling LLM Fine-Tuning on the Edge
Authors：
[Yuanfang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2273627475927926002)，[Yu Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=2094123896057450545)，[Zhinan Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=40507148827179721161)

## 中文标题

PeFoo-L：一个支持边缘端 LLM 微调的预条件前向优化器通用框架

## 英文摘要

Fine-tuning Large Language Models (LLMs) on resource-constrained edge devices is a critical but challenging task, primarily due to the prohibitive memory and computational costs of backpropagation. While forward-only optimizers like MeZO mitigate these costs by eliminating the backward pass, they often suffer from slow and unstable convergence, particularly on loss landscapes with heterogeneous curvature. To address this limitation, we introduce PeFoo, a general framework for preconditioner enhanced forward only optimizer. PeFoo integrates a carefully designed preconditioning strategy into the forward-only paradigm, corrects a fundamental source of bias and instability present in prior work HiZOO. Furthermore, to counteract the memory overhead introduced by the preconditioner itself, we propose PeFoo-L, which employs a layerwise update strategy. This approach constrains preconditioner storage and weight updates to a single layer per iteration, reducing the overall memory footprint and data traffic. Experimental results validate the effectiveness of our framework. In the OPT-1.3B model, PeFoo substantially exceeds the accuracy of leading zeroth-order methods MeZO and HiZOO by 2.7% and 2.1%, respectively. Furthermore, PeFoo-L achieves a memory footprint reduction of over 2.73× and 1.75× compared to Adam and HiZOO, while delivering faster convergence speed compared to MeZO and HiZOO.

## 中文摘要

在资源受限的边缘设备上微调大语言模型（LLM）是一项关键但具有挑战性的任务，主要原因是反向传播的内存与计算开销过高。诸如 MeZO 之类的前向优化器通过消除反向传播缓解了这些开销，但往往收敛缓慢且不稳定，尤其是在曲率异质的损失曲面上。为解决这一局限，我们提出 PeFoo，一个预条件增强的前向优化器通用框架。PeFoo 将精心设计的预条件策略融入前向范式，纠正了此前工作 HiZOO 中存在的根本性偏差与不稳定来源。此外，为抵消预条件器本身引入的内存开销，我们提出 PeFoo-L，采用逐层更新策略。该方法将预条件器存储与权重更新限制在每次迭代的单个层内，从而降低整体内存占用与数据流量。实验结果验证了该框架的有效性。在 OPT-1.3B 模型上，PeFoo 的精度分别大幅超过领先的零阶方法 MeZO 和 HiZOO 达 2.7% 和 2.1%。此外，PeFoo-L 相比 Adam 和 HiZOO 实现超过 2.73 倍和 1.75 倍的内存占用降低，同时相比 MeZO 和 HiZOO 带来更快的收敛速度。
