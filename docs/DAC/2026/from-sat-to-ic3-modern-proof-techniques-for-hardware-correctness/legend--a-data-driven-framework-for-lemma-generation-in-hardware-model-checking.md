Legend: A Data-Driven Framework for Lemma Generation in Hardware Model Checking
Authors：
[Mingkai Miao](https://63dac.conference-program.com/?post_type=page&p=15&uid=73231489207753979941)，[Guangyu Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=47184694701655998771)，[Wei Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=178243)，[Hongce Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8262735608385230332)

## 中文标题

Legend：面向硬件模型检测的数据驱动引理生成框架

## 英文摘要

Property checking of RTL designs is a central task in formal verification. Among available engines, IC3/PDR is a widely used backbone whose performance critically depends on inductive generalization—the step that generalizes a concrete counterexample-to-induction (CTI) cube into a lemma. Prior work has explored machine learning to guide this step and achieved encouraging results, yet most methods adopt a per-clause graph analysis paradigm: for each clause they repeatedly build and analyze graphs, incurring heavy overhead and creating a scalability bottleneck. We introduce LeGend, which replaces this paradigm with one-time global representation learning. LeGend pre-trains a domain-adapted self-supervised model to produce latch embeddings that capture global circuit properties. These precomputed embeddings allow a lightweight model to predict high-quality lemmas with negligible overhead, effectively decoupling expensive learning from fast inference. Experiments show LeGend accelerates two state-of-the-art IC3/PDR engines across a diverse set of benchmarks, presenting a promising path to scale up formal verification.

## 中文摘要

RTL 设计的性质检查是形式验证中的核心任务。在可用的引擎中，IC3/PDR 是广泛使用的骨干，其性能关键取决于归纳泛化——即将具体的归纳反例（CTI）立方体泛化为引理的步骤。先前工作已探索用机器学习引导该步骤并取得令人鼓舞的结果，但大多数方法采用逐子句图分析的范式：对每个子句反复构建并分析图，造成沉重开销并形成可扩展性瓶颈。我们提出 LeGend，以一种一次性全局表示学习取代该范式。LeGend 预训练一个域自适应的自监督模型，以产生捕获全局电路特性的锁存器嵌入。这些预计算的嵌入使轻量级模型能够以可忽略的开销预测高质量引理，从而有效将昂贵的学习与快速推理解耦。实验表明，LeGend 在多种基准上加速了两个最先进的 IC3/PDR 引擎，为扩展形式验证规模提供了一条有前景的路径。
