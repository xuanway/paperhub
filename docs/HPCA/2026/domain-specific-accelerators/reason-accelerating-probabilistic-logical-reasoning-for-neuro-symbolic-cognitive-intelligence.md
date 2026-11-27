---
title: "REASON: Accelerating Probabilistic Logical Reasoning for Neuro-Symbolic Cognitive Intelligence"
description: "HPCA 2026 · Domain Specific Accelerators"
tags:
  - "HPCA2026"
  - "Domain Specific Accelerators"
---

# REASON: Accelerating Probabilistic Logical Reasoning for Neuro-Symbolic Cognitive Intelligence

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Domain Specific Accelerators。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Domain Specific Accelerators</p>
</div>

**论文链接**：
**作者**：Zishen Wan Georgia Institute of Technology , Che-Kai Liu Georgia Institute of Technology , Jiayi Qian Georgia Institute of Technology , Hanchen Yang Georgia Institute of Technology , Arijit Raychowdhury Georgia Institute of Technology , Tushar Krishna Georgia Institute of Technology
**会议**：HPCA 2026

---

## 中文标题

REASON：加速神经符号认知智能的概率逻辑推理

## 英文摘要

Neuro-symbolic AI systems integrate neural perception with symbolic and probabilistic reasoning to enable data-efficient, interpretable, and robust intelligence beyond purely neural models. Although this compositional paradigm has shown superior performance in domains such as mathematical reasoning, planning, and verification, its deployment remains challenging due to severe inefficiencies in symbolic and probabilistic inference. Through systematic analysis of representative neurosymbolic workloads, we identify probabilistic logical reasoning as the inefficiency bottleneck, characterized by irregular control flow, low arithmetic intensity, uncoalesced memory accesses, and poor hardware utilization on CPUs and GPUs. This paper presents REASON, an integrated acceleration framework for probabilistic logical reasoning in neuro-symbolic AI. At the algorithm level, REASON introduces a unified directed acyclic graph representation that captures common structure across symbolic and probabilistic models, coupled with adaptive pruning and regularization. At the architecture level, REASON features a reconfigurable, tree-based processing fabric optimized for irregular traversal, symbolic deduction, and probabilistic aggregation. At the system level, REASON is tightly integrated with GPU streaming multiprocessors through a programmable interface and multi-level pipeline that efficiently orchestrates neural, symbolic, and probabilistic execution. Evaluated across six neurosymbolic workloads, REASON achieves 12-50× speedup and 310-681× energy efficiency over desktop and edge GPUs under TSMC 28 nm node. REASON enables real-time probabilistic logical reasoning, completing end-to-end tasks in 0.8 s with 6 mm² area and 2.12 W power, demonstrating that targeted acceleration of probabilistic logical reasoning is critical for practical and scalable neuro-symbolic AI and positioning REASON as a foundational system architecture for next-generation cognitive intelligence.

## 中文摘要

神经符号 AI 系统将神经感知与符号及概率推理相结合，从而在纯神经模型之外实现数据高效、可解释且鲁棒的智能。尽管这一组合式范式在数学推理、规划与验证等领域表现更优，但由于符号与概率推理的严重低效，其部署仍具挑战。通过对代表性神经符号负载的系统分析，我们识别出概率逻辑推理是低效瓶颈，其特征为不规则控制流、低算术强度、非合并的访存以及 CPU 与 GPU 上较差的硬件利用率。本文提出 REASON，一个用于神经符号 AI 中概率逻辑推理的集成加速框架。在算法层，它引入统一的有向无环图表示以刻画符号与概率模型间的公共结构，并结合自适应剪枝与正则化；在架构层，它采用可重构的树形处理结构，针对不规则遍历、符号推演与概率聚合优化；在系统层，它通过可编程接口与多级流水线与 GPU 流多处理器紧密集成。在六个神经符号负载上，TSMC 28 nm 工艺下的 REASON 相比桌面与边缘 GPU 取得 12–50 倍加速与 310–681 倍能效提升，以 6 mm² 面积和 2.12 W 功耗在 0.8 s 内完成端到端任务，表明对概率逻辑推理的定向加速对实用可扩展的神经符号 AI 至关重要。
