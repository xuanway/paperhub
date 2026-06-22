---
title: "SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme for Efficient Hardware IP Protection"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "logic-locking"
  - "smt-solver"
  - "hardware-ip-protection"
---

# SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。针对逻辑锁定中 SOTA 方案（SFLL + D2PIPs）的可扩展性和安全性挑战，提出 SCONE——结合 SMT 求解器与安全电路编码方案的新一代逻辑锁定技术，在 IBEX 处理器（16K 门）上实现 350× 可扩展性提升，同时抵御 5 种 I/O 或结构攻击。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Logic Locking · SMT Solver · Hardware IP Protection · IBEX</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme（SCONE：基于 SMT 求解器与电路编码方案的逻辑锁定技术） |
| 作者 | Zhaokun Han, Daniel Xing, Kostas Amberiadis (NIST), Ankur Srivastava, Jeyavijayan Rajendran |
| 机构 | Texas A&M / U. Maryland / NIST |
| 领域 | 硬件安全 / 逻辑锁定 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | 逻辑锁定(Logic Locking)、SMT 求解器、硬件 IP 保护、IBEX、可扩展性(Scalability) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132623) |

---

## 一、一句话核心摘要

> 逻辑锁定（Logic Locking）通过在芯片网表中插入密钥控制门来防止 IP 盗用——但 SOTA 方案 SFLL + D2PIPs 在较大设计上可扩展性崩溃（复杂度指数增长），且面临结构攻击的威胁。SCONE 采用 **SMT 求解器**替代枚举式搜索，并用**安全电路编码方案**保证锁定后的电路不泄漏密钥信息，在 IBEX RISC-V 处理器（16K 门）上实现 **350× 可扩展性提升**，同时抵御 5 种已知的 I/O 和结构攻击。

---

## 二、核心方法

### 2.1 SMT 求解器替代枚举

SOTA 方案使用枚举搜索寻找最优的密钥门插入位置——电路规模增长时组合爆炸。SCONE 将密钥门插入建模为 **SMT 约束满足问题**，利用高效 SMT 求解器（如 Z3）在多项式时间内找到满足安全性和开销约束的解。

### 2.2 电路编码方案

为防止攻击者通过结构分析（如子电路识别、信号概率分析）推断密钥，SCONE 引入编码方案使锁定后的电路网表在结构上与原始网表统计不可区分。

### 2.3 实验结果

| 指标 | 结果 |
|------|------|
| **可扩展性提升** | **350×**（IBEX, 16K gates） |
| **抵御攻击** | 5 种 I/O 或结构攻击 |
| 对比基线 | SFLL + D2PIPs (SOTA) |

---

## 三、总结

SCONE 将逻辑锁定的可扩展性从"学术 benchmark"级别推进到"真实处理器核心"级别（IBEX 16K 门）。NIST 的参与表明逻辑锁定在政府级硬件安全供应链中受到的重视。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132623)
