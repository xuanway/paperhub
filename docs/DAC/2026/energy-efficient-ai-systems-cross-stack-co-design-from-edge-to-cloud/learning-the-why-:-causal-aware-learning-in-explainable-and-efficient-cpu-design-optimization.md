Learning the "why": Causal-Aware Learning in Explainable and Efficient CPU Design Optimization
Authors：
[Yiyang Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=06084009581977409261)，[Tianning Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2300170291157611981)，[Hongyang Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=78188896139990088211)，[Liangji Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0727537266726571904)，[Yiming Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=1798701986488680989)，[Zhaori Bi](https://63dac.conference-program.com/?post_type=page&p=15&uid=73583865219571285901)，[Changhao yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=791243)，[Xuan Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=002243)

## 中文标题

学习“为什么”：可解释且高效的 CPU 设计优化中的因果感知学习

## 英文摘要

As modern CPUs grow increasingly configurable, design space exploration (DSE) has become essential for navigating complex architectural trade-offs. However, existing DSE approaches predominantly rely on statistical correlations, resulting in opaque decision processes. They cannot clearly explain the underlying causes of how configurations affect PPA outcomes, which in turn reduces designers’ confidence in automated recommendations. To address this limitation, we introduce causal learning into the DSE pipeline and develop CAL-DSE, a framework that constructs a validated causal graph combining statistical evidence with LLM-informed domain knowledge. Building on this structure, the causal graph decomposes the high-dimensional design space, enabling both interpretability and efficient exploration. Experimental results on RISC-V processor show that CAL-DSE achieves up to 4.12× hypervolume improvement while revealing validated causal pathways between design parameters and PPA outcomes.

## 中文摘要

随着现代 CPU 的可配置性不断增强，设计空间探索（DSE）已成为在复杂体系结构权衡中导航的必要手段。然而，现有 DSE 方法主要依赖统计相关性，导致决策过程不透明。它们无法清晰解释配置影响 PPA 结果的深层原因，这反过来削弱了设计者对自动化推荐结果的信任。为克服这一局限，我们将因果学习引入 DSE 流程，开发了 CAL-DSE：该框架构建一个经验证的因果图，将统计证据与 LLM 提供的领域知识相结合。基于这一结构，因果图对高维设计空间进行分解，从而同时实现可解释性与高效探索。在 RISC-V 处理器上的实验结果表明，CAL-DSE 取得高达 4.12 倍的超体积提升，同时揭示了设计参数与 PPA 结果之间经经验证的因果路径。

## 英文关键词

RISC-V Microarchitecture, Design Space Exploration (DSE), Causal learning, Variable Selection, Large language model (LLM)

## 中文关键词

RISC-V 微架构、设计空间探索（DSE）、因果学习、变量选择、大语言模型（LLM）
