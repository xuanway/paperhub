Bident: Optical Logic Synthesis via Optimal Configuration of Binary-Combiner Trees
Authors：
[Jun-Wei Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9804347224702030184)，[Iris Hui-Ru Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=839143)，[Kai-Hsiang Chiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4451295109437245587)

## 中文标题

Bident：通过二叉合并器树最优配置的光学逻辑综合

## 英文摘要

Despite decades of success, CMOS technology is increasingly constrained by power dissipation and propagation delay, thus motivating the exploration of photonic integrated circuits as an alternative for high-speed, energy-efficient computing. However, existing optical logic synthesis frameworks rely on an oversimplified efficiency factor model that fails to accurately capture physical attenuation and the hierarchical nature of signal degradation. This work presents Bident, a comprehensive optical logic synthesis framework that provides a physically accurate loss model and achieves optimal combiner configuration. We introduce the binary aggregate model, which explicitly reflects the binary-tree topology and input ordering in multi-input combiners. Based on this model, the Huffman tree optimization guarantees optimal Y-branch combiner configuration without requiring additional hardware resources. Meanwhile, a greedy algorithm optimally employs directional couplers at the leaf layer of a binary-combiner tree to achieve harmonic-mean efficiency at minimal hardware cost. Experimental results demonstrate that Bident achieves superior signal-attenuation reduction and lower switch cost than state-of-the-art methods, using both the conventional efficiency factor model and our binary aggregate model. A schematic-level optical circuit simulation further validates the feasibility and effectiveness of our binary-combiner configurations.

## 中文摘要

尽管 CMOS 技术数十年来取得了巨大成功，但它正日益受到功耗与传播时延的制约，这促使人们探索将光子集成电路作为高速、高能效计算的替代方案。然而，现有光学逻辑综合框架依赖过于简化的效率因子模型，无法准确刻画物理衰减以及信号劣化的层次特性。本文提出 Bident，一个全面的光学逻辑综合框架，它给出物理精确的损耗模型并实现最优的合并器配置。我们引入二叉聚合模型，显式反映多输入合并器中的二叉树拓扑与输入顺序。基于该模型，Huffman 树优化无需额外硬件资源即可保证 Y 分支合并器的最优配置。同时，一种贪心算法在二叉合并器树的叶层最优地使用定向耦合器，以最小硬件代价实现调和平均效率。实验结果表明，无论采用传统效率因子模型还是我们的二叉聚合模型，Bident 相比最先进方法都能实现更优的信号衰减降低与更低的开关代价。原理图级光路仿真进一步验证了我们二叉合并器配置的可行性与有效性。

## 英文关键词

Photonic integrated circuits, logic synthesis, binary-combiner trees

## 中文关键词

光子集成电路、逻辑综合、二叉合并器树
