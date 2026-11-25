StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis
Authors：
[Prashanth Vijayaraghavan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8623495993470149035)，[Apoorva Nitsure](https://63dac.conference-program.com/?post_type=page&p=15&uid=51282614269421044941)，[Luyao Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=55637762285003126381)，[David Beymer](https://63dac.conference-program.com/?post_type=page&p=15&uid=62278137590077685)，[Ehsan Degan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4767370642411897263)，[Vandana Mukherjee](https://63dac.conference-program.com/?post_type=page&p=15&uid=36808078636678243501)

## 中文标题

StepPRM-RTL：逐步过程奖励引导的 LLM 微调以增强 RTL 综合

## 英文摘要

Automatic generation of RTL code for digital hardware designs remains challenging due to long-horizon reasoning, multi-step dependencies, and strict correctness constraints in Verilog and VHDL. We present StepPRM-RTL, a novel framework that combines stepwise trajectory modeling, process-reward modeling (PRM), and retrieval-augmented fine-tuning (RAFT) to enhance both the functional correctness and reasoning fidelity of LLM-based RTL code generation. StepPRM-RTL constructs stepwise reasoning trajectories from canonical solutions, where each step contains a rationale and incremental code modification. A Process Reward Model (PRM) evaluates intermediate steps, providing dense feedback that guides reinforcement-style updates during RAFT fine-tuning. Monte Carlo Tree Search (MCTS) explores alternative reasoning paths, enriching the training dataset with high-quality trajectories. This integration of stepwise and outcome-aware rewards allows the model to learn both how and why to construct correct RTL, improving long-horizon reasoning beyond standard supervised or outcome-based training. Experimental evaluation on benchmark Verilog and VHDL datasets demonstrates that StepPRM-RTL outperforms the best prior methods by over 10% in functional correctness and reasoning fidelity metrics. Ablation studies confirm that the combination of PRM-guided rewards and stepwise trajectory exploration is key to its performance. StepPRM-RTL generalizes across RTL languages and provides a scalable framework for high-fidelity, interpretable code generation, establishing a new standard for LLM-assisted hardware design automation.

## 中文摘要

数字硬件设计的 RTL 代码自动生成仍具挑战性，其原因在于长程推理、多步依赖以及 Verilog 与 VHDL 中严格的正确性约束。我们提出 StepPRM-RTL，这是一个新颖的框架，融合逐步轨迹建模、过程奖励建模（PRM）与检索增强微调（RAFT），以同时提升基于 LLM 的 RTL 代码生成的功能正确性与推理保真度。StepPRM-RTL 从规范解中构建逐步推理轨迹，其中每一步包含一段推理依据与增量式代码修改。过程奖励模型（PRM）对中间步骤进行评估，提供稠密反馈，用以在 RAFT 微调过程中引导类强化学习的更新。蒙特卡洛树搜索（MCTS）探索备选推理路径，以高质量轨迹丰富训练数据集。这种逐步奖励与结果感知奖励的结合，使模型既能学会如何构建正确的 RTL，也能理解为何如此构建，从而在长程推理上超越标准的监督式训练或基于结果的训练。在基准 Verilog 与 VHDL 数据集上的实验评估表明，StepPRM-RTL 在功能正确性与推理保真度指标上相较此前最佳方法提升超过 10%。消融实验证实，PRM 引导的奖励与逐步轨迹探索的结合是其性能的关键。StepPRM-RTL 可跨 RTL 语言泛化，为高保真、可解释的代码生成提供了可扩展框架，为 LLM 辅助的硬件设计自动化树立了新标准。

## 英文关键词

RTL code generation, Verilog, VHDL, large language models, reinforcement learning, process reward modeling, stepwise reasoning, Monte Carlo Tree Search, MCTS, LLM, RL, RAFT, retrieval-augmented fine-tuning, hardware design automation

## 中文关键词

RTL 代码生成、Verilog、VHDL、大语言模型、强化学习、过程奖励建模、逐步推理、蒙特卡洛树搜索、MCTS、LLM、RL、RAFT、检索增强微调、硬件设计自动化
