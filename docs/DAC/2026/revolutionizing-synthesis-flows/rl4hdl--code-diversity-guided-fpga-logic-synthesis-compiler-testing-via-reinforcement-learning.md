RL4HDL: Code Diversity Guided FPGA Logic Synthesis Compiler Testing Via Reinforcement Learning
Authors：
[Zhihao Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=14857989239938181711)，[Hui Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=3640367788561472502)，[Hui Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=352763845050723954)，[Qian Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=7876162143705117078)，[Furui Zhan](https://63dac.conference-program.com/?post_type=page&p=15&uid=166406047781692196)，[Shikai Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3574330272611439529)

## 中文标题

RL4HDL：代码多样性引导的、基于强化学习的 FPGA 逻辑综合编译器测试

## 英文摘要

Logic Synthesis compilers play an indispensable role in Field Programmable Gate Arrays (FPGAs) design, translating Register-Transfer Level (RTL) designs into gate-level netlists. Defects in logic synthesis compilers may affect the security of final hardware implementations. Existing methods explored several test case generation and mutation approaches for logic synthesis testing but are limited by simple corpora and random strategies. It leads to the redundancy of test cases and further prevents the exploration of defects in logic synthesis compilers. To address the problem, we propose RL4HDL, a new method which uses Reinforcement Learning to guide logic synthesis compiler testing. Specifically, RL4HDL includes three main components, the Diversity Metamorphic Construction Component (DMC) and the Reinforcement Learning Control Component (RLC) and the Differential Testing Component(DTC). To generate diverse HDL test cases, the DMC applies a series of domain-specific metamorphic transformations to a set of seed designs, producing new test cases that are semantically equivalent to the originals while exhibiting richer structural patterns. Then, to reduce redundancy in the generated test cases, the RLC adaptively selects metamorphic transformations based on a reward of embedding-based structural diversity. It is realized by a lightweight bandit-style agent that automatically adjusts the selection probabilities of different transformations so as to avoid repeatedly generating similar test cases. Finally, to reveal defects in logic synthesis compilers, the DTC compiles each candidate HDL test case with multiple logic Synthesis compilers and compares the resulting netlists and simulation traces. If there are any discrepancies between different compilers or between semantically equivalent test cases compiled by the same compiler, the DTC reports these cases as candidate compiler defects. Comprehensive experiments conducted over a three-month period demonstrate the practical effectiveness of our method. We discovered 20 unique defects, including 12 previously unreported defects, which have been confirmed by official developers. Moreover, our approach has been shown to generate more distinct test cases than the state-of-the-art method.

## 中文摘要

逻辑综合编译器在 FPGA 设计中不可或缺，负责将寄存器传输级（RTL）设计转换为门级网表。逻辑综合编译器中的缺陷可能影响最终硬件实现的安全性。现有方法已探索了若干面向逻辑综合测试的测试用例生成与变异方法，但受限于简单的语料库与随机策略，导致测试用例冗余，进而阻碍了对逻辑综合编译器缺陷的深入探索。为解决该问题，我们提出 RL4HDL，一种利用强化学习引导逻辑综合编译器测试的新方法。具体而言，RL4HDL 包含三个主要组成部分：多样性蜕变构造组件（DMC）、强化学习控制组件（RLC）与差分测试组件（DTC）。为生成多样化的 HDL 测试用例，DMC 对一组种子设计施加一系列领域特定的蜕变变换，产生与原设计语义等价但结构模式更丰富的测试用例。随后，为降低所生成测试用例的冗余，RLC 基于嵌入结构多样性的奖励自适应地选择蜕变变换，具体由一个轻量级 bandit 式智能体实现，它自动调整不同变换的选择概率，从而避免反复生成相似的测试用例。最后，为揭示逻辑综合编译器中的缺陷，DTC 用多个逻辑综合编译器分别编译每个候选 HDL 测试用例，并比较所得的网表与仿真轨迹。若不同编译器之间，或同一编译器编译语义等价测试用例的结果之间存在差异，DTC 即把这些用例报告为候选编译器缺陷。在三个月内开展的全面实验证明了该方法的实际有效性：共发现 20 个独特缺陷，其中 12 个此前未被报告，并已得到官方开发者确认。此外，我们的方法已被证明能比最先进方法生成更多彼此不同的测试用例。

## 英文关键词

FPGA Logic Synthesis, Reinforcement Learning, Differential Testing, Compiler Testing

## 中文关键词

FPGA 逻辑综合、强化学习、差分测试、编译器测试
