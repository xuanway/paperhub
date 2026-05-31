---
title: "Adaptive CHERI Compartmentalization for Heterogeneous Accelerators"
description: "ISCA 2025论文解读：将CHERI能力架构扩展到异构加速器，通过自适应隔离策略保护加速器与主机的交互安全。"
tags: ["ISCA2025", "CHERI", "硬件安全", "隔离", "异构加速器", "Cambridge"]
---

# Adaptive CHERI Compartmentalization for Heterogeneous Accelerators

**作者**：Jianyi Cheng, A. Theodore Markettos, Alexandre Joannou, Paul Metzger, Matthew Naylor, Peter Rugg, Timothy M. Jones  
**机构**：University of Cambridge  
**会议**：ISCA 2025 · Session 10C: Security  

---

## 一句话总结

> CHERI 能力架构在 CPU 上有效阻止内存安全漏洞；本文将 CHERI 扩展到 FPGA/GPU 等异构加速器，设计自适应隔离粒度以平衡安全性与性能。

## 主要贡献

1. **CHERI 加速器扩展**：设计加速器端的能力（capability）检查硬件
2. **自适应隔离**：动态调整隔离粒度（函数级 vs. 模块级），低敏感任务用粗粒度减少开销
3. **FPGA 原型**：在 CHERI-FPGA 平台上验证

## 关键词

CHERI · 硬件安全 · 加速器隔离 · 内存安全 · Cambridge · ISCA 2025
