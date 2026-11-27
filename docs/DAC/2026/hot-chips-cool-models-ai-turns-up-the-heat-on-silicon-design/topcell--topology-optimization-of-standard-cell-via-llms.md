TOPCELL: Topology Optimization of Standard Cell via LLMs
Authors：
[Zhan Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=0024652895060329201)，[Yu-Tung Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03281721871298016111)，[Chen Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3397106385903709538)，[Guoheng Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=15614628012582167651)，[Jiaqi Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=4244706356294387379)，[Chia-tung Ho](https://63dac.conference-program.com/?post_type=page&p=15&uid=083643)，[Ang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=155743)，[Haoxing Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=172643)，[Cunxi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=365743)

## 中文标题

TOPCELL：基于 LLM 的标准单元拓扑优化

## 英文摘要

Transistor topology optimization is a critical step in standard cell design, directly dictating diffusion sharing efficiency and downstream routability. However, identifying optimal topologies remains a persistent bottleneck, as conventional exhaustive search methods become computationally intractable with increasing circuit complexity in advanced nodes. This paper introduces TOPCELL, a novel and scalable framework that reformulates high-dimensional topology exploration as a generative task using Large Language Models (LLMs). We employ Group Relative Policy Optimization (GRPO) to fine-tune the model, aligning its topology optimization strategy with logical (circuit) and spatial (layout) constraints. Experimental results within an industrial flow targeting an advanced 2nm technology node demonstrate that TOPCELL significantly outperforms foundation models in discovering routable, physically-aware topologies. When integrated into a state-of-the-art (SOTA) automation flow for a 7nm library generation task, TOPCELL exhibits robust zero-shot generalization and matches the layout quality of exhaustive solvers while achieving an 85.91× speedup.

## 中文摘要

晶体管拓扑优化是标准单元设计中的关键步骤，直接决定扩散共享效率与下游可布线性。然而，随着先进节点中电路复杂度不断提升，传统穷举搜索方法在计算上变得不可行，使得最优拓扑的确定始终是一个难以突破的瓶颈。本文提出 TOPCELL，一个新颖且可扩展的框架，将高维拓扑探索重构为基于大语言模型（LLM）的生成式任务。我们采用组相对策略优化（GRPO）对模型进行微调，使其拓扑优化策略与逻辑（电路）约束和空间（版图）约束相对齐。在面向先进 2nm 工艺节点的工业流程中开展的实验结果表明，TOPCELL 在发现可布线、具备物理感知能力的拓扑方面显著优于基础模型。当集成到面向 7nm 库生成任务的当前最优（SOTA）自动化流程中时，TOPCELL 展现出稳健的零样本泛化能力，在达到穷举求解器版图质量的同时实现了 85.91× 的加速。
