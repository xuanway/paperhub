Soberdse: Sample-Efficient Design Space Exploration via Learning-Based Algorithm Selection
Authors：
[Lei Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2226383852383608533)，[Shanshan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=09313067550579098671)，[Chenglong Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=521408209843774822)

## 中文标题

SoberDSE：通过基于学习的算法选择实现样本高效的设计空间探索

## 英文摘要

High-Level Synthesis (HLS) is a pivotal electronic design automation (EDA) technology that enables the generation of hardware circuits from high-level language descriptions. A critical step in HLS is Design Space Exploration (DSE), which seeks to identify high-quality hardware architectures under given constraints. However, the enormous size of the design space makes DSE computationally prohibitive. Although numerous algorithms have been proposed to accelerate DSE, our extensive experimental studies reveal that no single algorithm consistently achieves Pareto dominance across all problem instances. Consequently, the inability of any single algorithm to dominate all benchmarks necessitates an automated selection mechanism to identify the best-performing DSE algorithm for each specific case. To address this challenge, we propose the SoberDSE framework, which recommends suitable algorithm based on benchmark characteristics. Experimental results demonstrate that our SoberDSE framework significantly outperforms state-of-the-art heuristic-based DSE algorithms by up to 5.7 × and state-of-the-art learning-based DSE methods by up to 4.2 ×. Furthermore, compared to conventional classification models, SoberDSE delivers superior accuracy in small-sample learning scenarios, with an average enhancement of 35.57% Code and models are available at https://github.com/wslcccc/Sober.

## 中文摘要

高层综合（HLS）是一项关键的电子设计自动化（EDA）技术，能够从高层语言描述生成硬件电路。HLS 中的关键步骤是设计空间探索（DSE），其目标是在给定约束下寻找高质量的硬件架构。然而，设计空间的庞大规模使 DSE 在计算上难以承受。尽管已有大量算法被提出以加速 DSE，但我们的大量实验研究表明，没有任何单一算法能在所有问题实例上始终取得 Pareto 优势。因此，任何单一算法都无法在所有基准上占据主导，这就需要一个自动选择机制，为每个具体案例找出表现最佳的 DSE 算法。为应对这一挑战，我们提出 SoberDSE 框架，它依据基准特征推荐合适的算法。实验结果表明，我们的 SoberDSE 框架显著优于最先进的基于启发式的 DSE 算法（最高达 5.7 倍），也优于最先进的基于学习的 DSE 方法（最高达 4.2 倍）。此外，与传统分类模型相比，SoberDSE 在小样本学习场景下具有更高的准确率，平均提升 35.57%。代码与模型见 https://github.com/wslcccc/Sober。
