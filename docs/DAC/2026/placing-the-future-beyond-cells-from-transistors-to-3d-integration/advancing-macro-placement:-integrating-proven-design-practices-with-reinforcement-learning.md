Advancing Macro Placement: Integrating Proven Design Practices with Reinforcement Learning
Authors：
[Hsin-Chuan Kuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1495801483674187766)，[Chia-Wei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=8094892521352353851)，[Yi-Ying Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=947513024424840054)，[Tai-Yu Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=5278083211828935302)，[Bo-Jiun Hsu](https://63dac.conference-program.com/?post_type=page&p=15&uid=47180416043703934001)，[Sheng-Tai Tseng](https://63dac.conference-program.com/?post_type=page&p=15&uid=2525388212767876442)，[Chun-Chih Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8062582201764434354)，[Kun-Chin Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6248896659192217929)，[Tailai Tung](https://63dac.conference-program.com/?post_type=page&p=15&uid=226843)

## 中文标题

推进宏单元布局：将经验证的设计实践与强化学习相结合

## 英文摘要

Macro placement is a critical stage in physical design, directly impacting the quality and performance of VLSI circuits. We propose a reinforcement learning (RL)-based macro placement framework that integrates proven design practices through a design-practice-embedded action mask, including peripheral placement, dead space avoidance, and proximal placement for macros with shared design hierarchy and physical footprint. Unlike previous RL-based methods, our method uses macro clusters—formed according to design hierarchy and physical footprint—as the basic placement units, which reduces placement steps and consequently accelerates convergence and improves runtime. The proposed framework also introduces a novel compaction method to minimize wasted area caused by grid granularity, and jointly optimizes macro cluster location and tiling pattern for more effective exploration. Experimental results show that our approach achieves expert-level placement quality and consistently outperforms three leading commercial macro placers on industrial designs, with reduced turnaround time. On public benchmarks, our method achieves up to 25.37% and 39.51% improvements in worst negative slack (WNS) and total negative slack (TNS), respectively, over five state-of-the-art (SOTA) placers. These results demonstrate the effectiveness and real-world applicability of our RL-based framework, paving the way for further advancements in physical design automation.

## 中文摘要

宏单元布局是物理设计中的关键阶段，直接影响 VLSI 电路的质量与性能。我们提出一个基于强化学习（RL）的宏单元布局框架，通过嵌入设计实践的动作掩码将经验证的设计实践融入其中，包括外围式布局、死区规避，以及对共享设计层次与物理占用面积的宏单元实施就近布局。与以往基于 RL 的方法不同，我们的方法以依据设计层次与物理占用面积形成的宏单元簇作为基本布局单元，从而减少了布局步数，进而加速收敛并改善运行时间。该框架还引入一种新颖的压缩方法，以最小化网格粒度造成的面积浪费，并联合优化宏单元簇的位置与铺砌模式，从而实现更有效的探索。实验结果表明，我们的方法达到专家级布局质量，并在工业设计上持续优于三款领先的商业宏单元布局器，同时缩短了交付周期。在公开基准上，我们的方法相比五种先进（SOTA）布局器，在最差负松弛（WNS）与总负松弛（TNS）上分别取得最高 25.37% 与 39.51% 的改善。这些结果证明了我们基于 RL 的框架的有效性与实际适用性，为物理设计自动化的进一步发展铺平了道路。

## 英文关键词

Macro placement, Floorplanning, Machine learning, Deep learning, Reinforcement learning, Chip design

## 中文关键词

宏单元布局、布局规划、机器学习、深度学习、强化学习、芯片设计
