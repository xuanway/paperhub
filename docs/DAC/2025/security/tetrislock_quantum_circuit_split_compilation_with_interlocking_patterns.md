---
title: "TetrisLock: Quantum Circuit Split Compilation with Interlocking Patterns"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "quantum-computing"
  - "ip-protection"
  - "circuit-splitting"
  - "compilation"
---

# TetrisLock: Quantum Circuit Split Compilation with Interlocking Patterns

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。针对量子电路中不可信编译器的 IP 窃取威胁，提出 TetrisLock——通过"互锁模式"将量子电路拆分为两个相互依赖的片段，原始电路仅在合并两个片段并消除冗余后才可重建。无需可信编译器、无需插入随机电路、可抵御不同量子比特数的合谋攻击，资源开销极小。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Quantum Computing · IP Protection · Circuit Splitting · Compilation</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | TetrisLock: Quantum Circuit Split Compilation with Interlocking Patterns（TetrisLock：基于互锁模式的量子电路拆分编译） |
| 作者 | Qian Wang, Jayden John, Ben Dong (UC Merced), Yuntao Liu (Lehigh U.) |
| 机构 | UC Merced / Lehigh University |
| 领域 | 量子计算安全 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | 量子电路(Quantum Circuit)、IP 保护、拆分编译(Split Compilation)、互锁模式(Interlocking Patterns) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132682) |

---

## 一、一句话核心摘要

> 量子电路的编译通常外包给不可信的第三方云服务——如何防止编译者窃取或逆向量子算法 IP？TetrisLock 的答案是"互锁拆分"：将量子电路像俄罗斯方块一样拆分为两个相互锁定的独立片段，两者各自不含有完整逻辑，只有合并后才能通过消除冗余恢复原始电路功能。不需要可信编译器、不注入随机填充电路、资源开销极小，且能抵御不同量子比特数的合谋攻击。

---

## 二、核心方法

### 2.1 互锁拆分

- 将每个量子门分配给片段 A 或 B，确保每一方各自看到的电路是"功能不完整"的
- 互锁模式保证：任何人仅拥有一个片段无法推断电路的真实功能

### 2.2 优势

| 特性 | TetrisLock | 传统方案 |
|------|:------:|:------:|
| 需要可信第三方 | ❌ 否 | ✅ 是 |
| 增加电路深度 | 极小 | 可能有显著开销 |
| 防合谋攻击 | ✅ | ❌ |

### 2.3 实验

在 RevLib 量子基准电路上验证；FWCI=2.23（引用率前 10%），已被 1 篇论文引用。

---

## 三、总结

TetrisLock 是量子计算 IP 保护方向的开创性工作，其"互锁拆分"思想可能对经典 EDA 工具链中的 IP 保护也有借鉴意义。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132682)
