LLM-Based Automatic Architecture Optimization for AI Model HLS Implementation on FPGA
Authors：
[Zhe Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6597199993991353509)，[Mingyu Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8621889186359750004)，[Xu He](https://63dac.conference-program.com/?post_type=page&p=15&uid=30892403380736762431)，[Haoying Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888297388604614478)，[Jie Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=7680275012992863785)，[Yao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2298318494409372538)，[Libo Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=114643)

## 中文标题

基于 LLM 的面向 FPGA 上 AI 模型 HLS 实现的自动架构优化

## 英文摘要

High-Level Synthesis (HLS) is a key methodology for AI accelerator designs, yet significant challenges still persist in achieving full automation. Operations like module partitioning, dataflow orchestration, and throughput maximization still require manual intervention at the architectural level. Although recent solutions using compiler optimizations or large language models (LLMs) have aimed to improve automation, they are constrained by three key limitations: rigid architectural adaptability, lack of system-level optimizations, and insufficient support for complex models. To address these issues, we introduce a novel LLM-powered framework that automates the generation and optimization of system-level HLS architectures. The framework takes natural language specifications as input and automatically: (1) generates optimized modular dataflow architectures, (2) refines structures through pattern-based optimization, and (3) produces synthesizable hardware implementations. To our knowledge, this represents the first comprehensive framework to unify LLM-driven architectural synthesis with system-level HLS optimization for AI accelerators. Evaluations across different benchmark suites show that our method provides an 11.78× reduction in system latency on average over current state-of-the-art (SOTA) automatic methods and achieves performance comparable to handcrafted designs.

## 中文摘要

高层综合（HLS）是 AI 加速器设计的关键方法学，但实现完全自动化仍面临重大挑战。模块划分、数据流编排与吞吐率最大化等操作，仍需要在架构层面进行人工干预。尽管近期基于编译器优化或大语言模型（LLM）的方案旨在提升自动化程度，但它们受限于三个关键局限：架构自适应能力僵化、缺乏系统级优化、对复杂模型的支持不足。为解决这些问题，我们提出一个由 LLM 驱动的新型框架，可自动生成并优化系统级 HLS 架构。该框架以自然语言规约作为输入，并自动：(1) 生成经过优化的模块化数据流架构；(2) 通过基于模式的优化精化结构；(3) 产出可综合的硬件实现。据我们所知，这是首个将 LLM 驱动的架构综合与系统级 HLS 优化统一起来、面向 AI 加速器的综合框架。在不同基准套件上的评估表明，与当前最先进的（SOTA）自动化方法相比，我们的方法平均将系统延迟降低 11.78 倍，并达到与手工设计相当的性能。
