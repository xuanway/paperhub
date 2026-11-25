Alphaplacer: Analog Placement Enhanced by Monte Carlo Tree Search
Authors：
[Yapeng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=1472746777532170421)，[Peng Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=35263480881481101501)，[Mingzi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=24746776806155805071)，[Tinghuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=64168005757594372121)

## 中文标题

AlphaPlacer：由蒙特卡洛树搜索增强的模拟电路布局

## 英文摘要

Analog layout design remains heavily dependent on manual expertise, with placement being the most critical stage requiring extensive time and domain knowledge. Current automated placement techniques face challenges in capturing expert design practices and fall short of practical deployment. To address this limitation, we present AlphaPlacer, a novel MCTS-based analog placement framework that learns from historical layouts to provide expert knowledge-enhanced placement optimization. Our approach formulates analog placement as a hierarchical sequence pair search with MCTS, incorporating a bi-level search tree that decouples floorplan topology from device assignment and a similarity-driven reward mechanism. A pretrained learning framework is also integrated to capture sequence pair distributions from expert layouts. These components collectively enable AlphaPlacer to efficiently explore toward expert-like placements with improved convergence. Experimental results demonstrate that our method significantly outperforms baselines across key metrics including area, wirelength, and post-layout performance.

## 中文摘要

模拟版图设计仍在很大程度上依赖人工经验，其中布局是最关键且需要大量时间与领域知识的阶段。当前的自动布局技术在捕捉专家设计实践方面面临挑战，难以满足实际部署需求。为克服这一局限，我们提出 AlphaPlacer，一个新颖的基于 MCTS 的模拟布局框架，它从历史版图中学习，以提供专家知识增强的布局优化。我们的方法将模拟布局建模为基于 MCTS 的分层序列对搜索，引入将布局拓扑与器件指派解耦的双层搜索树以及相似度驱动的奖励机制。同时集成一个预训练的学习框架，用于从专家版图中捕捉序列对分布。这些组件共同使 AlphaPlacer 能够高效地朝专家级布局探索，并具备更好的收敛性。实验结果表明，我们的方法在面积、线长与版图后性能等关键指标上显著优于基线。
