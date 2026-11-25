Time-Aware Active Calibration and Scheduling for N-Qubit Systems via Bayesian Optimization and Reinforcement Learning
Authors：
[Ziming Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=067079871260242006)，[Tingting Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=5963119447382350714)，[Xiaofei Yue](https://63dac.conference-program.com/?post_type=page&p=15&uid=35117157121865550021)，[Zhaoxuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=49898124216175777231)，[Jianwei Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=13548133920903114011)

## 中文标题

基于贝叶斯优化与强化学习的 N 量子比特系统时间感知主动校准与调度

## 英文摘要

Frequent recalibration of multi-qubit systems is essential to maintain hardware fidelity, but calibration itself is costly and subject to rapid parameter drift. This work presents a novel framework for time-aware active calibration that combines Bayesian Optimization (BO) and Reinforcement Learning (RL) to adaptively schedule and prioritize calibration experiments under uncertainty. We model the calibration landscape as a directed acyclic graph (DAG), where nodes represent hardware parameters (e.g., frequency, amplitude ratio, DRAG, or phase) and edges capture inter-parameter dependencies extracted automatically from Qiskit Experiments metadata. Each parameter’s temporal drift is modeled as an Ornstein-Uhlenbeck (OU) or exponential decay process with uncertainty bounds. The BO agent prioritizes the next calibration target using a time-aware acquisition score that balances expected improvement, predictive uncertainty, and experiment duration under system-level constraints. A parallel RL scheduler coordinates cross-qubit calibration and readout tasks to minimize idle time and avoid conflicts. Our system further incorporates self-triggered recalibration based on online RB/XEB health metrics, enabling autonomous recovery from drift without human intervention. Experimental evaluation on multi-qubit testbeds demonstrates improved calibration efficiency, longer mean time between recalibrations (MTBC), and reduced overall calibration overhead compared to fixed or purely heuristic scheduling baselines.

## 中文摘要

多量子比特系统的频繁重校准对于维持硬件保真度至关重要，但校准本身开销高昂，且参数会快速漂移。本文提出一种新颖的时间感知主动校准框架，将贝叶斯优化（BO）与强化学习（RL）相结合，在不确定性下自适应地安排校准实验并确定其优先级。我们将校准景观建模为有向无环图（DAG），其中节点表示硬件参数（例如频率、幅度比、DRAG 或相位），边刻画参数间的依赖关系，这些依赖关系由 Qiskit Experiments 元数据自动提取得到。每个参数的时间漂移被建模为 Ornstein-Uhlenbeck（OU）过程或指数衰减过程，并附带不确定性边界。BO 智能体借助时间感知采集评分确定下一个校准目标，该评分在系统级约束下权衡期望改进、预测不确定性与实验时长。并行的 RL 调度器协调跨量子比特的校准与读出任务，以最小化空闲时间并避免冲突。本系统进一步引入基于在线 RB/XEB 健康指标的自触发重校准，使系统无需人工干预即可自主从漂移中恢复。在多量子比特测试平台上的实验评估表明：与固定或纯启发式调度基线相比，该方法提升了校准效率、延长了平均重校准间隔（MTBC），并降低了总体校准开销。

## 英文关键词

Active Calibration, Bayesian Optimization, Reinforcement Learning, Multi-Qubit Quantum Systems

## 中文关键词

主动校准、贝叶斯优化、强化学习、多量子比特量子系统
