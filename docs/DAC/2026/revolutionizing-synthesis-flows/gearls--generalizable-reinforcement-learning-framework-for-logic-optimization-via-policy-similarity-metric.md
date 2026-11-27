Gearls: Generalizable Reinforcement Learning Framework for Logic Optimization via Policy Similarity Metric
Authors：
[Yusen Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=8039127628585740211)，[Jiaqi Lyu](https://63dac.conference-program.com/?post_type=page&p=15&uid=37240316804684777851)，[Zhi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8929691451404552405)，[Peng Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=768143)

## 中文标题

GearLS：基于策略相似度度量的可泛化逻辑优化强化学习框架

## 英文摘要

Reinforcement learning (RL) has shown great promise for automating logic optimization, yet its practical adoption is hindered by poor generalization. Existing RL models are often tailored to a specific circuit, requiring costly and time-consuming retraining or tuning for new designs. To overcome this problem, this paper introduces GearLS, a generalizable reinforcement learning framework that produces high-quality timing optimization flows for previously unseen circuits. The Policy Similarity Metric (PSM) is the core of our method, which enables the RL agent to recognize and leverage similarities between states. Operating on logic cones extracted from circuits, which reduces state-space complexity and also serves as powerful data augmentation, makes the framework effective. To bridge the gap between local and global timing objectives, we design a cut weighting scheme to ensure scaling ability of the agent. Experimental results on a diverse set of OpenCores benchmarks demonstrate that compared to the baseline, GearLS achieves a 48.7% reduction in Worst Negative Slack (WNS) and a 73.1% reduction in Total Negative Slack (TNS) on unseen designs, superior to state-of-the-art (SOTA) work, with a speedup up to 9.9×.

## 中文摘要

强化学习（RL）在逻辑优化自动化方面已展现出巨大潜力，但其实际应用仍受泛化能力不足的制约。现有 RL 模型往往针对特定电路定制，面对新设计需进行昂贵且耗时的重新训练或调优。为解决该问题，本文提出 GearLS，一个可泛化的强化学习框架，能够为此前未见过的电路生成高质量的时序优化流程。策略相似度度量（PSM）是本方法的核心，它使 RL 智能体能够识别并利用状态之间的相似性。该方法在从电路中提取的逻辑锥上运行，既降低了状态空间复杂度，又构成强力的数据增强，从而使框架行之有效。为弥合局部与全局时序目标之间的差距，我们设计了割权重方案以确保智能体的可扩展能力。在多样化的 OpenCores 基准上的实验结果表明，与基线相比，GearLS 在未见设计上将最差负裕量（WNS）降低 48.7%，将总负裕量（TNS）降低 73.1%，优于当前最先进（SOTA）工作，加速比最高达 9.9×。

## 英文关键词

Logic synthesis, reinforcement learning, policy similarity metric

## 中文关键词

逻辑综合、强化学习、策略相似度度量
