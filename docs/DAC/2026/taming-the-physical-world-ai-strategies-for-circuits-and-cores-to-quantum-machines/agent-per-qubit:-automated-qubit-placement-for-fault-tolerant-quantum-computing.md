Agent-Per-Qubit: Automated Qubit Placement for Fault-Tolerant Quantum Computing
Authors：
[Tian Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=23334339175781705661)，[Yang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=62386815676021083061)，[Tan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=1554639927228059913)，[Wan-Su Bao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8323743799509431647)

## 中文标题

Agent-Per-Qubit：面向容错量子计算的自动量子比特布局

## 英文摘要

Quantum computing holds the potential to revolutionize numerous fields, yet the practical execution of quantum circuits depends on an efficient compilation process, including the placement of logical qubits on a quantum chip. This placement is a hard combinatorial problem that often defeats traditional heuristics and manual optimization. We present QAgent, a novel multi-agent reinforcement learning (RL) framework that autonomously optimizes logical qubit layouts on quantum processor. In QAgent, one agent is assigned to each logical qubit, and the agents jointly learn placement policies that minimize circuit execution cost. To address the challenges of sparse rewards and reward hacking, we propose the Breakthrough Return Bonus (BRB), a dynamic reward shaping mechanism that encourages meaningful layout improvements and accelerates convergence. Extensive experiments on diverse quantum circuit benchmarks show that QAgent reduces execution costs by up to 53.9% compared to leading baselines, and significantly enhances circuit success rates. Ablation studies confirm that BRB is essential for stable training and effective policy optimization. These results demonstrate the promise of AI-driven, workload-aware placement for advancing fault-tolerant quantum computing.

## 中文摘要

量子计算有望革新众多领域，但量子电路的实际执行依赖高效的编译过程，其中包括将逻辑量子比特放置到量子芯片上。该布局是一个困难的组合优化问题，传统启发式方法与人工优化往往难以胜任。我们提出 QAgent，一种新颖的多智能体强化学习（RL）框架，可在量子处理器上自主优化逻辑量子比特布局。在 QAgent 中，每个逻辑量子比特分配一个智能体，这些智能体共同学习以最小化电路执行代价的布局策略。为应对稀疏奖励与奖励投机（reward hacking）的挑战，我们提出突破回报奖励（BRB），一种动态奖励塑形机制，鼓励有意义的布局改进并加速收敛。在多样量子电路基准上的大量实验表明，与领先基线相比，QAgent 可将执行代价降低多达 53.9%，并显著提升电路成功率。消融研究证实，BRB 对于稳定训练与有效策略优化不可或缺。这些结果展示了 AI 驱动、工作负载感知的布局在推进容错量子计算方面的潜力。
