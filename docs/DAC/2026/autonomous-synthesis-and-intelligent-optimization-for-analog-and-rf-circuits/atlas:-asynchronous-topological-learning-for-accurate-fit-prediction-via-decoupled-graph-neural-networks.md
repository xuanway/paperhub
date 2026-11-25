ATLAS: Asynchronous Topological Learning for Accurate FIT Prediction via Decoupled Graph Neural Networks
Authors：
[Yicheng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=11260621946157510011)，[Mingjun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=67901646550225857321)，[Songwei Pei](https://63dac.conference-program.com/?post_type=page&p=15&uid=59690795422244529011)，[Yuntao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3670065592072189317)，[Zizhen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2120435217578556355)，[Boyu Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=457743043246730093)，[Huawei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=535143)，[Shangguang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=37380539148235035971)

## 中文标题

ATLAS：通过解耦图神经网络实现精确 FIT 预测的异步拓扑学习

## 英文摘要

Safety-critical integrated circuits targeting ISO 26262 ASIL-D require a failure-in-time (FIT) < 10. These physics-based tools for FIT prediction, such as BFIT, are accurate but slow, while ML baselines suffer collapse under long-tail FIT distributions. We propose ATLAS, a decoupled GNN framework that combines a bidirectional asynchronous topological message passing backbone that follows BFIT’s forward and backward propagation, together with RankNet and CalibNet heads. RankNet uses a gap-aware pairwise ranking loss with log-difference weighting and additional emphasis on high-risk samples to identify the top-𝑘% high risk gates. CalibNet employs a dual-domain loss in the log and linear domains with importance weighting to achieve accurate calibration. The proposed design achieves 𝑂(|𝑉| + |𝐸|) complexity, delivering up to 220× speedup over BFIT while reducing normalized hardening area by 53% compared to DeepGate2 on ITC’99 benchmarks, thereby enabling the rapid reliability-aware design of large-scale circuits.

## 中文摘要

面向 ISO 26262 ASIL-D 的安全关键集成电路要求失效率（FIT）< 10。此类基于物理的 FIT 预测工具（如 BFIT）准确但速度慢，而机器学习基线在长尾 FIT 分布下会发生性能崩溃。我们提出 ATLAS，一个解耦的 GNN 框架，它结合了遵循 BFIT 前向与反向传播的双向异步拓扑消息传递主干，以及 RankNet 和 CalibNet 两个预测头。RankNet 采用带对数差加权、并额外强调高风险样本的间隙感知成对排序损失，以识别风险最高的前 𝑘% 门。CalibNet 采用对数域与线性域的双域损失并施加重要性加权，以实现精确校准。所提出的设计达到 𝑂(|𝑉| + |𝐸|) 复杂度，在 ITC’99 基准上相比 BFIT 实现最高 220 倍加速，同时相比 DeepGate2 将归一化加固面积降低 53%，从而支持大规模电路的快速可靠性感知设计。
