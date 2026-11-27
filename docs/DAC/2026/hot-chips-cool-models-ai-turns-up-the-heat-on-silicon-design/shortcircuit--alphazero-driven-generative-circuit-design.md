Shortcircuit: Alphazero-Driven Generative Circuit Design
Authors：
[Dimitrios Tsaras](https://63dac.conference-program.com/?post_type=page&p=15&uid=024843)，[Antoine Grosnit](https://63dac.conference-program.com/?post_type=page&p=15&uid=11374733349013157081)，[Lei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=1116530604224312028)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)，[Haitham Bou Ammar](https://63dac.conference-program.com/?post_type=page&p=15&uid=51845031185623802321)，[Mingxuan Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2371953237384098548)

## 中文标题

ShortCircuit：AlphaZero 驱动的生成式电路设计

## 英文摘要

Traditional logic synthesis heuristics have plateaued. We introduce ShortCircuit, a novel transformer-based architecture generating AND-Inverter Graphs (AIGs) directly from truth tables. Unlike prior deep learning efforts, we employ a two-phase training process combining supervised learning and an AlphaZero variant to navigate the doubly exponential state space. Evaluated on 500 8-input truth tables from real-world circuits, ShortCircuit guarantees functional correctness and outperforms the state-of-the-art tool ABC in circuit size. Furthermore, our greedy rollout mechanism achieves a 31× speedup, demonstrating significant efficiency gains.

## 中文摘要

传统逻辑综合启发式方法已趋于停滞。我们提出 ShortCircuit，一种新型基于 Transformer 的架构，可直接由真值表生成与或非图（AIG）。与此前深度学习工作不同，我们采用监督学习与 AlphaZero 变体相结合的两阶段训练过程，以在双指数级状态空间中搜索。在来自真实电路的 500 个 8 输入真值表上评估，ShortCircuit 保证功能正确，并在电路规模上优于当前最优工具 ABC。此外，我们的贪心 rollout 机制实现了 31 倍加速，展现出显著的效率提升。
