---
title: "LPO: Discovering Missed Peephole Optimizations with Large Language Models"
description: "ASPLOS 2026 · Session 5C · LPO：用大语言模型发现被遗漏的窥孔优化"
tags:
  - "ASPLOS2026"
  - "Session 5C"
  - "Formal Verification"
---

# LPO: Discovering Missed Peephole Optimizations with Large Language Models

**中文标题：** LPO：用大语言模型发现被遗漏的窥孔优化

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhenyang Xu (University of Waterloo), Hongxu Xu (University of Waterloo), Yongqiang Tian (Monash University), Xintong Zhou (University of Waterloo), Chengnian Sun (University of Waterloo)

**单位：** University of Waterloo；Monash University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790184) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Peephole optimization is an essential class of compiler optimizations that targets small, inefficient instruction sequences within programs. By replacing such suboptimal instructions with refined and more optimal sequences, these optimizations not only directly optimize code size and performance, but also enable more transformations in the subsequent optimization pipeline. Despite their importance, discovering new and effective peephole optimizations remains challenging due to the complexity and breadth of instruction sets. Prior approaches either lack scalability or have significant restrictions on the peephole optimizations that they can find. This paper introduces LPO, a novel automated framework to discover missed peephole optimizations. Our key insight is that, Large Language Models (LLMs) are effective at creative exploration but susceptible to hallucinations; conversely, formal verification techniques provide rigorous guarantees but struggle with creative discovery. By synergistically combining the strengths of LLMs and formal verifiers in a closedloop feedback mechanism, LPO can effectively discover verified peephole optimizations that were previously missed. We comprehensively evaluated LPO within LLVM ecosystems. Our evaluation shows that LPO can successfully identify up to 22 out of 25 previously reported missed optimizations in LLVM. In contrast, the recently proposed superoptimizers for LLVM, Souper and Minotaur detected 15 and 3 of them, respectively. More importantly, within eleven months of development and intermittent testing, LPO found 62 missed peephole optimizations, of which 28 were confirmed and an additional 13 had already been fixed in LLVM. These results demonstrate LPO's strong potential to continuously uncover new optimizations as LLMs' reasoning improves.

## 中文摘要

窥孔优化是一类重要的编译器优化，其目标是程序中细小、低效的指令序列。通过用更精巧、更优的序列替换这类次优指令，这些优化不仅直接优化代码体积与性能，还为后续优化流水线中的更多变换创造了条件。尽管其重要性不言而喻，但由于指令集的复杂性与广度，发现新的、有效的窥孔优化仍然充满挑战。先前的方法要么缺乏可扩展性，要么对其能够发现的窥孔优化有显著限制。本文提出 LPO，一个用于发现被遗漏窥孔优化的新自动化框架。我们的关键洞见是：大语言模型（LLM）擅长创造性探索，但容易产生幻觉；相反，形式化验证技术提供严格的保证，却难以进行创造性发现。通过在闭环反馈机制中协同结合 LLM 与形式化验证器各自的优势，LPO 能够有效地发现此前被遗漏且经过验证的窥孔优化。我们在 LLVM 生态系统中全面评估了 LPO。评估表明，LPO 能够成功识别 LLVM 中此前报告的最多 25 个被遗漏优化中的 22 个。相比之下，近期提出的 LLVM 超级优化器 Souper 与 Minotaur 分别检测出其中 15 个和 3 个。更重要的是，在十一个月的开发与间歇性测试中，LPO 发现了 62 个被遗漏的窥孔优化，其中 28 个得到确认，另有 13 个已在 LLVM 中被修复。这些结果表明，随着 LLM 推理能力的提升，LPO 在持续发掘新优化方面具有强大的潜力。

## 英文关键词

compiler, peephole optimization, large language model

## 中文关键词

编译器；窥孔优化；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790184)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2026](../index.md)
