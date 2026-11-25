Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC
Authors：
[Cunxi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=365743)，[Haoxing Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=172643)

## 中文标题

EDA 工具的自主演化：多智能体自演化 ABC

## 英文摘要

This paper introduces the first self-evolving logic synthesis framework, which leverages Large Language Model (LLM) agents to autonomously improve the source code of ABC, the widely adopted logic synthesis system. Our framework operates on the entire integrated ABC codebase, and the output repository preserves its single-binary execution model and command interface. In the initial evolution cycle, we bootstrap the system using existing prior open-source synthesis components, covering flow tuning, logic minimization, and technology mapping, but without manually injecting new heuristics. On top of this foundation, a team of LLM-based agents iteratively rewrites and evolves specific sub-components of ABC following our “programming guidance“ prompts under a unified correctness and QoR-driven evaluation loop. Each evolution cycle proposes code modifications, compiles the integrated binary, validates correctness, and evaluates quality-of-results (QoR) on multi-suite benchmarks including ISCAS 85/89/99, VTR, EPFL, and IWLS 2005. Through continuous feedback, the system discovers optimizations beyond human-designed heuristics, effectively learning new synthesis strategies that enhance QoR. We detail the architecture of this self-improving system, its integration with ABC, and results demonstrating that the framework can autonomously and progressively improve EDA tool at full million-line scale.

## 中文摘要

本文提出首个自演化逻辑综合框架，利用大语言模型（LLM）智能体自主改进被广泛采用的逻辑综合系统 ABC 的源代码。该框架作用于完整的集成式 ABC 代码库，其输出的代码仓库保持原有的单一二进制执行模型与命令接口。在初始演化周期中，我们利用已有的开源综合组件对系统进行引导式构建，涵盖流程调优、逻辑最小化与技术映射，但并未人为注入新的启发式策略。在此基础上，一组基于 LLM 的智能体在统一的正确性与 QoR 驱动评估循环下，按照我们的“编程指引”提示词迭代地重写并演化 ABC 的特定子组件。每一轮演化都会提出代码修改、编译集成后的二进制、验证正确性，并在包括 ISCAS 85/89/99、VTR、EPFL 与 IWLS 2005 在内的多套基准上评估结果质量（QoR）。通过持续反馈，系统发现了超越人工设计启发式的优化，有效学习到可提升 QoR 的新综合策略。我们详细阐述了这一自改进系统的架构、其与 ABC 的集成方式，并给出实验结果表明该框架能够在百万行规模上自主且逐步地改进 EDA 工具。
