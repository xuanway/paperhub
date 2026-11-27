Seeing the Unseen: Reverse Engineering Hidden PMU Events by Differential Analysis and Simulation Validation
Authors：
[Yihao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3780282084310488084)，[Pengfei Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67100257388396941571)，[Xiaojie Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5309706597496622972)，[Yihao Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=86118471767224013741)，[Chunlu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3018622213155594684)，[Gang Qu](https://63dac.conference-program.com/?post_type=page&p=15&uid=064143)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

洞见未见：通过差分分析与仿真验证逆向解析隐藏的 PMU 事件

## 英文摘要

The Performance Monitoring Unit (PMU) is a significant hardware module of modern processors. Previous studies have disclosed numerous hidden PMU events. However, their underlying microarchitectural semantics remain unexplored, which largely limit their utilization. This paper proposes a reverse engineering framework for deeply understanding the microarchitectural semantics of hidden PMU events. For demonstration, we successfully utilize the framework to reveal microarchitectural behaviors of branch-related events and discover a hidden pattern of UMask Combination in Intel CPUs. Based on the reverse-engineering results, we implement a PMU-based covert channel for Spectre-v1 in SGX and enable a high-precision website fingerprinting attack under resource-constrained conditions.

## 中文摘要

性能监控单元（PMU）是现代处理器中重要的硬件模块。以往研究已披露了大量隐藏的 PMU 事件，但其底层微架构语义仍未被揭示，这在很大程度上限制了它们的利用。本文提出一个逆向工程框架，用于深入理解隐藏 PMU 事件的微架构语义。作为示范，我们成功利用该框架揭示了分支相关事件的微架构行为，并发现了 Intel CPU 中 UMask Combination 的隐藏模式。基于逆向工程结果，我们面向 SGX 中的 Spectre-v1 实现了基于 PMU 的隐蔽信道，并在资源受限条件下实现了高精度的网站指纹攻击。

## 英文关键词

Performance Monitoring Unit, Microarchitecture, Reverse Engineering, Transient Execution, Website Fingerprinting

## 中文关键词

性能监控单元、微架构、逆向工程、瞬态执行、网站指纹
