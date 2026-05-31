---
title: "SpecASan: 利用推测地址消毒缓解瞬态执行攻击"
description: "ISCA 2025论文解读：SpecASan将地址消毒（AddressSanitizer）思想引入推测执行路径，在不影响正常执行性能的前提下阻止Spectre等瞬态执行攻击。"
tags: ["ISCA2025", "推测执行攻击", "Spectre", "地址消毒", "安全", "UCR"]
---

# SpecASan: Mitigating Transient Execution Attacks Using Speculative Address Sanitization

**作者**：Saber Ganjisaffar, Esmaeil Mohmmadian Koruyeh, Jason Zellmer, Hodjat Asghari Esfeden, Chengyu Song, Nael Abu-Ghazaleh, Esmaeil Mohmmadian Koruyeh  
**机构**：UC Riverside (UCR)  
**会议**：ISCA 2025 · Session 10C: Security  

---

## 一句话总结

> Spectre 等瞬态执行攻击利用推测路径读取越界内存；SpecASan 在推测路径上动态插入边界检查（类似 ASan），阻止越界访问在微架构侧信道中泄露。

## 主要贡献

1. **推测路径 ASan**：在推测执行的访存操作旁并行检查地址合法性
2. **低延迟集成**：检查与推测执行并行，不在关键路径上
3. **防御范围**：覆盖 Spectre v1、Spectre-PHT 等主要变体

## 实验结果

- SPEC CPU2017 性能开销 **< 3%**（远低于 LFENCE 等软件缓解方案）
- 成功阻断已知 Spectre PoC 攻击

## 关键词

Spectre · 推测执行 · 瞬态执行攻击 · AddressSanitizer · UCR · ISCA 2025
