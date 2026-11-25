How Can Reinforcement Learning Achieve Expert-Level Placement?
Authors：
[Ruo-Tong Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4940691652784141785)，[Ke Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=5778742940083357572)，[Chengrui Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=1804124812119649253)，[Yunqi Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=39267230907048957061)，[Tian Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4489329823386155123)，[Peng Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=40062715754023433431)，[Siyuan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=90130281886321181481)，[Mingxuan Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2371953237384098548)，[Chao Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=16501305373597700161)，[Zhi-Hua Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=70708817356754345571)

## 中文标题

强化学习如何实现专家级布局？

## 英文摘要

Chip placement is a critical step in physical design. While reinforcement learning (RL)-based methods have recently emerged, their training primarily focuses on wirelength optimization, and therefore often fail to achieve expert-quality layouts. We identify the reward design as the primary cause for the performance gap with experts, and instead of formalizing intricate processes, we circumvent this by directly learning from expert layouts to derive a reward model. Our approach starts from the final expert layouts to infer step-by-step expert trajectories. Using these trajectories as demonstrations or preferences, we train a model that captures the latent implicit rewards in expert results. Experiments show that our framework can efficiently learn from even a single design and generalize well to unseen cases.

## 中文摘要

芯片布局是物理设计中的关键步骤。尽管近年来涌现出基于强化学习（RL）的方法，但其训练主要聚焦于线长优化，因而往往无法达到专家级质量的布局。我们指出，奖励设计是与专家水平之间存在性能差距的首要原因；我们没有去形式化那些繁复的过程，而是绕开这一难题，直接从专家布局中学习以推导奖励模型。我们的方法从最终的专家布局出发，反推出逐步的专家轨迹。以这些轨迹作为示范或偏好，我们训练一个模型来捕捉专家结果中隐含的潜在奖励。实验表明，我们的框架即使仅依据单个设计也能高效学习，并能很好地泛化到未见过的案例。
