---
title: "QRCC: Evaluating Large Quantum Circuits on Small Quantum Computers through Integrated Qubit Reuse and Circuit Cutting"
description: "ASPLOS 2025 · Session 1B · QRCC：通过集成量子比特复用与线路切割在小量子计算机上评估大量子线路"
tags:
  - "ASPLOS2025"
  - "Session 1B"
  - "Quantum Computing"
---

# QRCC: Evaluating Large Quantum Circuits on Small Quantum Computers through Integrated Qubit Reuse and Circuit Cutting

**中文标题：** QRCC：通过集成量子比特复用与线路切割在小量子计算机上评估大量子线路

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Aditya Pawar (Electrical and Computer Engineering Department, University of Pittsburgh), Yingheng Li (Computer Science Department, University of Pittsburgh), Zewei Mo (Computer Science Department, University of Pittsburgh), Yanan Guo (Electrical and Computer Engineering Department, University of Pittsburgh), Xulong Tang (Computer Science Department, University of Pittsburgh), Youtao Zhang (Computer Science Department, University of Pittsburgh), Jun Yang (Electrical and Computer Engineering Department, University of Pittsburgh)

**单位：** Electrical and Computer Engineering Department, University of Pittsburgh；Computer Science Department, University of Pittsburgh

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674179) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Quantum computing has recently emerged as a promising computing paradigm for many application domains. However, the size of quantum circuits that can be run with high fidelity is constrained by the limited quantity and quality of physical qubits. Recently proposed schemes, such as wire cutting and qubit reuse, mitigate the problem but produce sub-optimal results as they address the problem individually. In addition, gate cutting, an alternative circuit-cutting strategy that is suitable for circuits computing expectation values, has not been fully explored in the field. In this paper, we propose QRCC, an integrated approach that exploits qubit reuse and circuit-cutting (including wire cutting and gate cutting) to run large circuits on small quantum computers. Circuit-cutting techniques introduce nonnegligible post-processing overhead, which increases exponentially with the number of cuts. QRCC exploits qubit reuse to find better cutting solutions to minimize the cut numbers and thus the post-processing overhead. Our evaluation results show that on average we reduce the number of cuts by 29% and additional reduction when considering gate cuts.

## 中文摘要

量子计算近来已成为许多应用领域颇具前景的计算范式。然而，能够以高保真度运行的量子线路规模受限于物理量子比特的数量与质量。近期提出的方案，例如线切割与量子比特复用，缓解了这一问题，但由于它们各自独立地处理该问题，所得结果并非最优。此外，门切割作为一种适用于计算期望值的线路的替代性线路切割策略，在该领域尚未得到充分探索。本文提出 QRCC，一种集成方法，它利用量子比特复用与线路切割（包括线切割和门切割）在小量子计算机上运行大线路。线路切割技术会引入不可忽视的后处理开销，该开销随切割数量的增加而呈指数增长。QRCC 利用量子比特复用寻找更好的切割方案，以最小化切割数量，从而降低后处理开销。我们的评估结果表明，平均而言我们将切割数量减少了 29%，并在考虑门切割时获得进一步的降低。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674179)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2025](../index.md)
