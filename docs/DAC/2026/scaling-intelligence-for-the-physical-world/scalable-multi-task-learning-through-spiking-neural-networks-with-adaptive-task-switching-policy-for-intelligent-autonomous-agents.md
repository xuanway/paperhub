Scalable Multi-Task Learning Through Spiking Neural Networks with Adaptive Task-Switching Policy for Intelligent Autonomous Agents
Authors：
[Rachmad Vidya Wicaksana Putra](https://63dac.conference-program.com/?post_type=page&p=15&uid=08223451383980792821)，[Avaneesh Devkota](https://63dac.conference-program.com/?post_type=page&p=15&uid=9859261369486752078)，[Muhammad Shafique](https://63dac.conference-program.com/?post_type=page&p=15&uid=560343)

## 中文标题

基于脉冲神经网络与自适应任务切换策略的可扩展多任务学习及其在智能自主体中的应用

## 英文摘要

Training resource-constrained autonomous agents on multiple tasks simultaneously is crucial for adapting to diverse real-world environments. Recent works employ reinforcement learning (RL) approach, but they still suffer from sub-optimal multi-task performance due to task interference. State-of-the-art works employ Spiking Neural Networks (SNNs) to improve RL-based multi-task learning and enable low-power/energy operations through network enhancements and spike-driven data stream processing. However, they rely on fixed task-switching intervals during its training, thus limiting its performance and scalability. To address this, we propose SwitchMT, a novel methodology that employs adaptive task-switching for effective, scalable, and simultaneous multi-task learning. SwitchMT employs the following key ideas: (1) leveraging a Deep Spiking Q-Network with active dendrites and dueling structure, that utilizes task-specific context signals to create specialized sub-networks; and (2) devising an adaptive task-switching policy that leverages both rewards and internal dynamics of the network parameters. Experimental results demonstrate that SwitchMT achieves competitive scores in multiple Atari games (i.e., Pong: -8.8, Breakout: 5.6, and Enduro: 355.2) and longer game episodes as compared to the state-of-the-art. These results also highlight the effectiveness of SwitchMT methodology in addressing task interference without increasing the network complexity, enabling intelligent autonomous agents with scalable multi-task learning capabilities.

## 中文摘要

在资源受限的自主体上同时训练多个任务，对于适应多样化的真实环境至关重要。近期工作采用强化学习（RL）方法，但受任务干扰影响，其多任务性能仍不理想。最先进的工作采用脉冲神经网络（SNN）改进基于 RL 的多任务学习，并通过网络增强与脉冲驱动的数据流处理实现低功耗、低能耗运行。然而，这些方法在训练中依赖固定的任务切换间隔，从而限制了性能与可扩展性。为此，我们提出 SwitchMT，一种采用自适应任务切换的新方法，以实现有效、可扩展且同时进行的多任务学习。SwitchMT 的核心思想包括：（1）利用带有主动树突与对偶结构的深度脉冲 Q 网络，借助任务特定的上下文信号构建专用子网络；（2）设计自适应任务切换策略，同时利用奖励与网络参数的内部动态。实验结果表明，与最先进方法相比，SwitchMT 在多个 Atari 游戏（即 Pong：-8.8、Breakout：5.6、Enduro：355.2）中取得有竞争力的分数，并获得更长的游戏回合。这些结果还凸显了 SwitchMT 方法在不增加网络复杂度的前提下缓解任务干扰的有效性，使智能自主体具备可扩展的多任务学习能力。
