Raise the Shields: A Modular RISC-V Extension for Post Quantum Cryptography
Authors：
[Alessandra Dolmeta](https://63dac.conference-program.com/?post_type=page&p=15&uid=0194702780853712304)，[Valeria Piscopo](https://63dac.conference-program.com/?post_type=page&p=15&uid=8421056210509952521)，[Maurizio Martina](https://63dac.conference-program.com/?post_type=page&p=15&uid=363443)，[Guido Masera](https://63dac.conference-program.com/?post_type=page&p=15&uid=237443)，[Michael Hutter](https://63dac.conference-program.com/?post_type=page&p=15&uid=0908236603146800252)

## 中文标题

举盾而御：面向后量子密码的模块化 RISC-V 扩展

## 英文摘要

This work presents a unified RISC-V extension for Post-Quantum Cryptography (PQC) that emphasizes versatility and openness. The design exposes a compact set of custom scalar instructions via the Core-V eXtension Interface (CV-X-IF) and a modular PQ-ALU that accelerates the dominant kernels across hash-, lattice-, and code-based schemes: Keccak processing, randomness sampling, modular and polynomial arithmetic, finite-field operations, and coefficient compression. The system supports algorithms standardized by NIST, ML-KEM, ML-DSA, SLH-DSA, and HQC, as well as candidates under evaluation. The full hardware and software stack is released as open source to enable reproducibility and community reuse. We provide ASIC results from post-synthesis characterization in 65 nm CMOS, reporting instruction-cycle counts, along with power and energy estimates for each custom operation. Overall, the proposed extension delivers a compact (26.3 kGE) and practical path to crypto-agile, energy-efficient PQC on RISC-V while preserving software compatibility and a clean integration into existing cores.

## 中文摘要

本工作提出一种面向后量子密码（PQC）的统一 RISC-V 扩展，强调通用性与开放性。该设计通过 Core-V eXtension Interface（CV-X-IF）提供一组精简的自定义标量指令，并配备模块化的 PQ-ALU，用于加速哈希类、格类与编码类方案中的主导计算内核：Keccak 处理、随机数采样、模运算与多项式运算、有限域运算以及系数压缩。该系统支持 NIST 标准化的算法 ML-KEM、ML-DSA、SLH-DSA 与 HQC，以及仍在评估中的候选算法。完整的硬件与软件栈均已开源发布，以保证可复现性与社区复用。我们给出 65 nm CMOS 工艺下综合后表征的 ASIC 结果，报告指令周期数以及每种自定义运算的功耗与能耗估计。总体而言，所提出的扩展在保持软件兼容性并可干净集成到现有内核的同时，为 RISC-V 上实现密码敏捷、高能效的 PQC 提供了一条紧凑（26.3 kGE）而实用的路径。

## 英文关键词

RISC-V, ISE, Post-Quantum Cryptography, ASIC

## 中文关键词

RISC-V、指令集扩展（ISE）、后量子密码、ASIC
