Drcagent: A Design Rule Aware LLM Agent for DRC Auto-Fix with Adversarial Reinforcement Learning
Authors：
[Zihang Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=42697968922107303481)，[Zhuoheng Wan](https://63dac.conference-program.com/?post_type=page&p=15&uid=96423718310294864561)，[Haodong Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67762242078220399721)，[Kun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=565843)

## 中文标题

drcAgent：一种具备设计规则感知能力、结合对抗强化学习的 DRC 自动修复 LLM 智能体

## 英文摘要

As semiconductor manufacturing advances toward leading-edge nodes, such as 7 nm and below, Design Rule Checking (DRC) and violation correction have emerged as critical bottlenecks in achieving design closure. This challenge arises from intricate geometric constraints and complex rule dependencies, which conventional template-based or heuristic methods are inadequate to resolve efficiently. Moreover, these methods exhibit limited adaptability when migrating to new process nodes. To address these challenges, we propose drcAgent, a novel framework for automated correction of DRC violations. The framework integrates a multimodal Large Language Model (LLM) agent with a Retrieval-Augmented Generation (RAG) mechanism grounded in a Design Rule Knowledge Graph (DRKG). Furthermore, we develop a self-play adversarial reinforcement learning playground in which a Generator and a Fixer co-evolve. Through iterative interaction with commercial EDA tools, the agent progressively refines its correction policy. Experimental results on real-world industrial design cases demonstrate that drcAgent can effectively fix violations, offering a promising new learning-based solution for chip design.

## 中文摘要

随着半导体制造向 7 nm 及以下的先进工艺节点推进，设计规则检查（DRC）与违规修正在实现设计收敛方面已成为关键瓶颈。这一挑战源于复杂的几何约束与规则依赖关系，传统的基于模板或启发式的方法难以高效解决；此外，这些方法在迁移到新工艺节点时适应性有限。为应对这些挑战，我们提出 drcAgent，一个用于自动修复 DRC 违规的新颖框架。该框架将多模态大语言模型（LLM）智能体与基于设计规则知识图谱（DRKG）的检索增强生成（RAG）机制相结合。此外，我们构建了一个自博弈对抗强化学习环境，其中生成器与修复器协同演化。通过与商用 EDA 工具的迭代交互，该智能体逐步精炼其修复策略。在真实工业设计案例上的实验结果表明，drcAgent 能够有效修复违规，为芯片设计提供了一种有前景的、基于学习的新方案。
