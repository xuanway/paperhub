---
title: "Bit-Accurate Modeling of GPU Matrix Multiply-Accumulate Units: Demystifying Numerical Discrepancy and Accuracy"
description: "MICRO 2026 · Session 1A · GPU 矩阵乘累加单元的位精确建模：揭示数值差异与精度问题"
tags:
  - "MICRO2026"
  - "GPU"
  - "Tensor Core"
  - "Numerical Precision"
---

# Bit-Accurate Modeling of GPU Matrix Multiply-Accumulate Units: Demystifying Numerical Discrepancy and Accuracy

**中文标题：** GPU 矩阵乘累加单元的位精确建模：揭示数值差异与精度问题

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Peichen Xie, Shuotao Xu, Yang Wang, Fan Yang, Mao Yang

**来源：** MICRO 2026，pp. 17–31；[DOI](https://doi.org/10.1109/MICRO67795.2026.00018)

## 英文摘要

Modern AI accelerators rely on matrix multiply-accumulate units (MMAUs), such as NVIDIA Tensor Cores and AMD Matrix Cores, to accelerate deep neural network workloads. MMAUs expose only instruction-level or API-level interfaces of matrix multiply-accumulate (MMA) operations, while leaving internal floating-point arithmetic behavior undocumented. Consequently, MMAUs across vendors and architectural generations often produce numerical discrepancies for identical inputs, and sometimes exhibit reduced numerical accuracy that can cause training instability. Diagnosing and understanding the root causes of these effects is challenging without white-box models of their arithmetic behavior. This paper proposes closed-loop feature probing (CLFP), a generic and systematic framework for constructing bit-accurate arithmetic behavior models of MMA operations. Based on this framework, we analyze all MMA instructions on ten GPU architectures spanning NVIDIA Volta through RTX Blackwell and AMD CDNA1 through CDNA3, and derive the first bit-accurate arithmetic models for these MMAUs. Our models explain previously observed cross-platform numerical discrepancies and accuracy issues, enable white-box numerical error analysis, reveal four types of precision bottlenecks and one type of numerical asymmetry, and inform software workarounds as well as design suggestions for future MMAUs. This work is open-source at https://github.com/microsoft/MMA-Sim.

## 中文摘要

现代人工智能加速器依靠 NVIDIA Tensor Core、AMD Matrix Core 等矩阵乘累加单元（MMAU）加速深度神经网络工作负载。这些单元仅通过指令级或 API 级接口暴露矩阵乘累加（MMA）操作，其内部浮点运算行为并未公开。因此，不同厂商或不同架构代际的 MMAU 对相同输入往往产生不同数值结果，有时还会出现数值精度下降，进而导致训练不稳定。缺少运算行为的白盒模型，使这些问题的根因难以诊断和理解。本文提出闭环特征探测（CLFP），一种通用、系统的 MMA 位精确运算行为建模框架。基于该框架，我们分析了涵盖 NVIDIA Volta 至 RTX Blackwell、AMD CDNA1 至 CDNA3 的 10 种 GPU 架构上的全部 MMA 指令，并首次为这些 MMAU 建立位精确算术模型。模型解释了此前观察到的跨平台数值差异与精度问题，支持白盒数值误差分析，揭示了四类精度瓶颈和一类数值不对称性，并为软件规避方案及未来 MMAU 设计提供依据。本研究已开源：https://github.com/microsoft/MMA-Sim。

## 中文关键词

GPU 矩阵乘累加单元；位精确建模；浮点运算；数值精度；跨架构差异

## 代码与研究制品

- 代码仓库：[https://github.com/microsoft/MMA-Sim](https://github.com/microsoft/MMA-Sim)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
