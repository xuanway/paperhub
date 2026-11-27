Expcheck: Dynamic Expert-Aware Checkpointing for Mixture-of-Experts Based Models
Authors：
[Guorui Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=079854703497006261)，[Xiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5065485256395697225)，[Keni Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=492143)，[Qiang Su](https://63dac.conference-program.com/?post_type=page&p=15&uid=7158759864933926036)，[Weiwei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=124343)，[Guang Kou](https://63dac.conference-program.com/?post_type=page&p=15&uid=9495046234301990279)，[Chenchen Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=449243)

## 中文标题

ExpCheck：面向混合专家模型的动态专家感知检查点

## 英文摘要

Large-scale Mixture-of-Experts (MoE) models are pivotal in modern AI, yet their massive parameter size creates a “storage wall” for fault tolerance, where limited bandwidth restricts checkpoint frequency and risks significant wasted computation. We present EXPCheck, a dynamic expert-aware checkpointing system designed to resolve the conflict between massive MoE states and limited persistence bandwidth. Grounded in the observation that expert activation is highly imbalanced, EXPCheck employs a novel Aging-then-Greedy Expert Selection (AGES) policy. AGES first enforces an age-based refresh for overdue “cold” experts to prevent indefinite staleness, and then greedily allocates the remaining persistence budget to frequently updated “hot” experts. Implemented on a production-scale training stack, EXPCheck significantly reduces persistence traffic and increases checkpoint frequency by at most 5× compared to full checkpointing, while maintaining downstream model accuracy comparable to standard methods.

## 中文摘要

大规模混合专家（MoE）模型在现代 AI 中至关重要，但其庞大的参数规模为容错带来了“存储墙”：有限带宽限制了检查点频率，并可能导致大量计算浪费。我们提出了 EXPCheck，一种动态专家感知检查点系统，旨在解决海量 MoE 状态与有限持久化带宽之间的冲突。基于专家激活高度不均衡的观察，EXPCheck 采用一种新颖的“先老化后贪心”专家选择（AGES）策略。AGES 首先对超期的“冷”专家强制执行基于年龄的刷新，以防止其无限期陈旧；然后贪心地将剩余持久化预算分配给频繁更新的“热”专家。EXPCheck 已在生产级训练栈上实现，相比完整检查点，它显著减少了持久化流量，并将检查点频率最多提高 5 倍，同时保持下游模型精度与标准方法相当。

## 英文关键词

Checkpointing, Mixture-of-Experts, Large Language Models

## 中文关键词

检查点、混合专家、大语言模型
