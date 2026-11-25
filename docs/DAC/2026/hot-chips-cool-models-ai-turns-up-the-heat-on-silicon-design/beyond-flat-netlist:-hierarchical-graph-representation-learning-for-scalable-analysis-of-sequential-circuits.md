Beyond Flat Netlist: Hierarchical Graph Representation Learning for Scalable Analysis of Sequential Circuits
Authors：
[Jingyi Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=83326254599308517121)，[Zhengyuan Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=383743)，[Jiaying Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=148477401016677462)，[Ziyang Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=372843)，[Qiang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=024143)

## 中文标题

超越扁平网表：面向时序电路可扩展分析的分层图表示学习

## 英文摘要

Circuit Representation Learning (CRL) offers a powerful paradigm to guide and optimize core Electronic Design Automation (EDA) tasks, but its practical adoption is hindered by the immense scale of industrial netlists and a failure to explicitly model register-level temporal dynamics. To overcome these barriers, we introduce DeepSeq3, a novel hierarchical framework that abstracts circuits into a two-level representation: fine-grained combinational subgraphs partitioned by flip-flops (FFs), and a high-level SuperNode Graph (SNG) that models the register-transfer structure. A dual Graph Neural Network (GNN) architecture learns representations at both levels, capturing local Boolean logic and global state transitions. Crucially, we introduce a state-centric pre-training scheme that predicts the reachability between FF states, endowing the model with a deep understanding of temporal behavior. Demonstrated on large-scale benchmarks, DeepSeq3’s approach yields superior scalability and richer representations, reducing bounded model checking (BMC) solving time by 18% while guaranteeing correctness.

## 中文摘要

电路表示学习（CRL）为引导与优化电子设计自动化（EDA）核心任务提供了强大范式，但其实际应用受到两方面阻碍：工业网表规模极其庞大，且未能显式建模寄存器级时序动态。为克服这些障碍，我们提出 DeepSeq3，一种新颖的分层框架，将电路抽象为两级表示：由触发器（FF）划分的细粒度组合子图，以及建模寄存器传输结构的高层超节点图（SNG）。双图神经网络（GNN）架构在两级上学习表示，同时捕获局部布尔逻辑与全局状态转移。关键在于，我们提出以状态为中心的预训练方案，预测 FF 状态之间的可达性，使模型对时序行为具备深入理解。在大规模基准上的验证表明，DeepSeq3 的方法具有更优的可扩展性与更丰富的表示，在保证正确性的同时将有界模型检验（BMC）求解时间降低 18%。
