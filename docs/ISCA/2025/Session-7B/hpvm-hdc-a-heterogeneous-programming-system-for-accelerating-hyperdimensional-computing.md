---
title: "HPVM-HDC: A Heterogeneous Programming System for Accelerating Hyperdimensional Computing"
description: "ISCA 2025 · Session 7B · HPVM-HDC：用于加速超维计算的异构编程系统"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# HPVM-HDC: A Heterogeneous Programming System for Accelerating Hyperdimensional Computing

**中文标题：** HPVM-HDC：用于加速超维计算的异构编程系统

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Russel Arbore, Xavier Routh, Abdul Rafae Noor, Akash Kothari, Haichao Yang, Weihong Xu, Sumukh Pinge, Minxuan Zhou, Tajana Rosing, Vikram Adve

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731095) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Hyperdimensional Computing (HDC), a technique inspired by cog- nitive models of computation, has been proposed as an efficient and robust alternative basis for machine learning. HDC programs are often manually written in low-level and target specific languages targeting CPUs, GPUs, and FPGAs—these codes cannot be easily retargeted onto HDC-specific accelerators. No previous program- ming system enables productive development of HDC programs and generates efficient code for several hardware targets. We propose a heterogeneous programming system for HDC: a novel programming language, HDC++, for writing applications using a unified programming model, including HDC-specific primi- tives to improve programmability, and a heterogeneous compiler, HPVM-HDC, that provides an intermediate representation for com- piling HDC programs to many hardware targets. We implement two tuning optimizations, automatic binarization and reduction perforation, that exploit the error resilient nature of HDC. Our eval- uation shows that HPVM-HDC generates performance-competitive code for CPUs and GPUs, achieving a geomean speed-up of 1.17x over optimized baseline CUDA implementations with a geomean reduction in total lines of code of 1.6x across CPUs and GPUs. Ad- ditionally, HPVM-HDC targets an HDC Digital ASIC and an HDC ReRAM accelerator simulator, enabling the first execution of HDC applications on these devices.

## 中文摘要

超维计算（HDC）是一种受认知计算模型启发的技术，作为机器学习领域高效、鲁棒的备选方案。HDC程序通常使用底层、硬件绑定的语言手工编写，面向CPU、GPU、FPGA；这类代码很难迁移到HDC专用加速器上。此前没有编程系统支持HDC程序的高效开发，并为多种硬件后端生成高性能代码。

本文提出面向HDC的异构编程系统：一套全新编程语言HDC++，基于统一编程模型开发应用，内置HDC专属原语，提升开发易用性；配套异构编译器HPVM-HDC，提供中间表示，支持将HDC程序编译到多种硬件平台。我们实现两项调优优化：自动二值化与归约穿孔（reduction perforation），利用HDC本身具备的容错特性。

评测结果表明：HPVM-HDC为CPU、GPU生成的代码性能具备竞争力，对比优化后的CUDA基线实现，几何平均提速1.17倍；同时代码总行数几何平均减少1.6倍。除此之外，HPVM-HDC还支持HDC数字ASIC与HDC RRAM加速器仿真器，首次在这类设备上运行HDC应用。

## 英文关键词

Compilers, Hyperdimensional Computing, Heterogeneous Systems

## 中文关键词

编译器, 超维计算, 异构系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731095)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
