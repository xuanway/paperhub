---
title: "Lifetime-Aware Design for Item-Level Intelligence at the Extreme Edge"
description: "ASPLOS 2026 · Session 5B · 面向极致边缘物品级智能的生命周期感知设计"
tags:
  - "ASPLOS2026"
  - "Session 5B"
  - "On-Device & Edge AI"
---

# Lifetime-Aware Design for Item-Level Intelligence at the Extreme Edge

**中文标题：** 面向极致边缘物品级智能的生命周期感知设计

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Shvetank Prakash (Harvard University), Andrew Cheng (Harvard University), Olof Kindgren (Qamcom), Ashiq Ahamed (Pragmatic Semiconductor), Graham Knight (Pragmatic Semiconductor), Jed Kufel (Pragmatic Semiconductor), Francisco Rodriguez (Pragmatic Semiconductor), Arya Tschand (Harvard University), David Kong (Harvard University), Mariam Elgamal (Harvard University), Jerry Huang (Harvard University), Emma Chen (Harvard University), Gage Hills (Harvard University), Richard Price (Pragmatic Semiconductor), Emre Ozer (Pragmatic Semiconductor), Vijay Janapa Reddi (Harvard University)

**单位：** Harvard University；Qamcom；Pragmatic Semiconductor

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790182) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

We present FlexiFlow, a lifetime-aware design framework for item-level intelligence (ILI) where computation is integrated directly into disposable products like food packaging and medical patches. Our framework leverages natively flexible electronics which offer significantly lower costs than silicon but are limited to kHz speeds and several thousands of gates. Our insight is that unlike traditional computing with more uniform deployment patterns, ILI applications exhibit 1000× variation in operational lifetime, fundamentally changing optimal architectural design decisions when considering trillion-item deployment scales. To enable holistic design and optimization, we model the trade-offs between embodied carbon footprint and operational carbon footprint based on application-specific lifetimes. The framework includes: (1) FlexiBench, a workload suite targeting sustainability applications from spoilage detection to health monitoring; (2) FlexiBits, area-optimized RISC-V cores with 1/4/8-bit datapaths achieving 2.65× to 3.50× better energy efficiency per workload execution; and (3) a carbon-aware model that selects optimal architectures based on deployment characteristics. We show that lifetime-aware microarchitectural design can reduce carbon footprint by 1.62×, while algorithmic decisions can reduce carbon footprint by 14.5×. We validate our approach through the first tape-out using a PDK for flexible electronics with fully open-source tools, achieving 30.9 kHz operation. FlexiFlow enables exploration of computing at the Extreme Edge where conventional design methodologies must be reevaluated to account for new constraints and considerations. FlexiFlow is

## 中文摘要

我们提出 FlexiFlow，一个面向物品级智能（item-level intelligence, ILI）的生命周期感知设计框架，其中计算被直接集成到一次性产品中，例如食品包装和医疗贴片。我们的框架利用原生柔性电子器件，其成本显著低于硅，但速度被限制在 kHz 量级、门数仅有数千。我们的洞见是：与部署模式更为均匀的传统计算不同，ILI 应用在运行生命周期上呈现出 1000× 的差异，当考虑万亿件物品的部署规模时，这从根本上改变了最优的体系结构设计决策。为实现整体化的设计与优化，我们基于应用特定的生命周期，对隐含碳足迹（embodied carbon footprint）与运行碳足迹（operational carbon footprint）之间的权衡进行建模。该框架包含：(1) FlexiBench，一个面向从腐败检测到健康监测等可持续性应用的工作负载套件；(2) FlexiBits，面积优化的 RISC-V 核，采用 1/4/8 位数据通路，每次工作负载执行的能效提升 2.65× 至 3.50×；(3) 一个碳感知模型，可根据部署特征选择最优体系结构。我们表明，生命周期感知的微体系结构设计可将碳足迹降低 1.62×，而算法层面的决策可将碳足迹降低 14.5×。我们使用柔性电子 PDK 并完全采用开源工具完成了首次流片，验证了我们的方法，实现了 30.9 kHz 的工作频率。FlexiFlow 使得对极致边缘（Extreme Edge）计算的探索成为可能；在这一场景中，传统设计方法学必须重新审视，以纳入新的约束与考量因素。

## 英文关键词

Extreme Edge; TinyML; Sustainability; Carbon Footprint; RISC-V; Printed and Flexible Electronics; FlexIC; System Analysis and Design

## 中文关键词

极致边缘；TinyML；可持续性；碳足迹；RISC-V；印刷与柔性电子；FlexIC；系统分析与设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790182)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2026](../index.md)
