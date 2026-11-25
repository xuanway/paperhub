Provably Probabilistic Safe Controller Synthesis for Vision-Based Neural Network Control Systems
Authors：
[Qianlong Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=70178085425443254001)，[Hanrui Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=85923638704603072111)，[Liqian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3045072970783448116)，[Zhengfeng Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=743343)，[Banghu Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=0842902567453871894)，[Ji Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=15807371638189260671)

## 中文标题

面向基于视觉的神经网络控制系统的可证明概率安全控制器综合

## 英文摘要

The prevalence of nonlinear systems in safety-critical domains calls for controllers with safety guarantees, while vision-based control relies on high-dimensional images complicates both decision-making and formal safety analysis under uncertainty. This paper proposes a provably safe controller synthesis method for vision-based neural network control systems. We first employ a conditional generative adversarial network (cGAN) to approximate the mapping from system states to visual observations and combine it with RL-based pretraining to build a verifiable closed-loop structure. A data-driven model quantifies uncertainties from environmental perturbations, while martingale theory guides the learning of a stochastic barrier certificate (SBC) to provide rigorous probabilistic safety bounds. Furthermore, counterexamples from verification are used to alternately refine both the controller and certificate networks, ultimately yielding a controller with formally provable probabilistic safety guarantees. Experimental results on widely studied benchmarks demonstrate the efficiency and effectiveness of our approach.

## 中文摘要

安全关键领域中非线性系统的普遍存在要求控制器具备安全保障，而基于视觉的控制依赖高维图像，这使得不确定性下的决策与形式化安全分析都变得更加复杂。本文提出一种面向基于视觉的神经网络控制系统的可证明安全控制器综合方法。我们首先采用条件生成对抗网络（cGAN）来近似从系统状态到视觉观测的映射，并将其与基于强化学习的预训练相结合，构建可验证的闭环结构。数据驱动模型量化来自环境扰动的不确定性，而鞅理论指导随机屏障证书（SBC）的学习，以提供严格的概率安全界。此外，验证产生的反例被用于交替精化控制器网络与证书网络，最终得到一个具有形式化可证明概率安全保证的控制器。在广泛研究的基准上的实验结果表明了我们方法的效率与有效性。

## 英文关键词

vision-based neural network control system, formal verification, martingales, stochastic barrier certificate, reinforcement learning

## 中文关键词

基于视觉的神经网络控制系统、形式化验证、鞅、随机屏障证书、强化学习
