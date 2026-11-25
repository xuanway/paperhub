TRACE: Learning to Compute on Circuit Graphs
Authors：
[Ziyang Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=372843)，[Jiaying Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=148477401016677462)，[Jingyi Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=83326254599308517121)，[Qiang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=024143)

## 中文标题

TRACE：在电路图上学习计算

## 英文摘要

Learning to compute, the ability to model the functional behavior of a circuit graph, is a fundamental challenge for graph representation learning. Yet, the dominant paradigm is architecturally mismatched for this task. This flawed assumption, central to mainstream message passing neural networks (MPNNs) and their conventional Transformer-based counterparts, prevents models from capturing the position-aware, hierarchical nature of computation. To resolve this, we introduce TRACE, a new paradigm built on an architecturally sound backbone and a principled learning objective. First, TRACE employs a Hierarchical Transformer that mirrors the step-by-step flow of computation, providing a faithful architectural backbone that replaces the flawed permutation-invariant aggregation. Second, we introduce function shift learning, a novel objective that decouples the learning problem. Instead of predicting the complex global function directly, our model is trained to predict only the function shift, the discrepancy between the true global function and a simple local approximation that assumes input independence. We validate this paradigm on various circuits modalities, including Register Transfer Level graphs, And-Inverter Graphs and post-mapping netlists. Across a comprehensive suite of benchmarks, TRACE substantially outperforms all prior architectures. These results demonstrate that our architecturally-aligned backbone and decoupled learning objective form a more robust paradigm for the fundamental challenge of learning the functional behavior of a circuit graph. Code is available at https://github.com/zyzheng17/TRACE_DAC26.

## 中文摘要

学习计算（learning to compute），即对电路图的功能行为进行建模的能力，是图表示学习中的一项基础性挑战。然而，主流范式在架构上与这一任务并不匹配。这一错误假设是主流消息传递神经网络（MPNN）及其常规 Transformer 对应方法的核心理念，它使模型无法刻画计算所具有的位置感知与层次化特性。为解决这一问题，我们提出 TRACE，一种建立在架构合理的骨干网络与有原则的学习目标之上的新范式。首先，TRACE 采用层次化 Transformer，以映射计算的逐步流动过程，提供一个忠实的架构骨干，取代此前有缺陷的置换不变聚合。其次，我们提出函数偏移学习（function shift learning）这一全新目标，以解耦该学习问题。我们的模型并不直接预测复杂的全局函数，而只预测函数偏移，即真实全局函数与一个假设输入独立的简单局部近似之间的差异。我们在多种电路模态上验证了该范式，包括寄存器传输级（RTL）图、与—反相器图（AIG）以及映射后网表。在全面的基准套件上，TRACE 显著优于所有既有架构。这些结果表明，我们架构对齐的骨干与解耦的学习目标，为学习电路图功能行为这一基础性挑战构成了一种更为稳健的范式。代码见 https://github.com/zyzheng17/TRACE_DAC26 。
