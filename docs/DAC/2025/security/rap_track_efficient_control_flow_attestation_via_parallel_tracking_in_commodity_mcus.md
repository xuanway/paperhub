---
title: "RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "control-flow-attestation"
  - "mcu"
  - "arm"
  - "embedded-security"
---

# RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4。针对嵌入式设备控制流认证（CFA）中代码插桩和频繁上下文切换的性能开销问题，提出 RAP-Track——首次利用商用 MCU 已有的 ARM 硬件调试特性（MTB + DWT）在程序执行的同时并行追踪控制流路径，无需插桩即可实现高效远程认证。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Control Flow Attestation · MCU · ARM · Embedded Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs（RAP-Track：利用商用 MCU 并行追踪的高效控制流认证） |
| 作者 | Antonio Joia Neto, Adam Caulfield, Ivan De Oliveira Nunes |
| 机构 | Rochester Institute of Technology (RIT) 等 |
| 领域 | 嵌入式安全（Embedded Security） |
| 投稿方向 | Security（Session: SEC4） |
| 关键词 | 控制流认证(Control Flow Attestation)、MCU、ARM、MTB、DWT、嵌入式安全(Embedded Security) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings） |

---

## 一、一句话核心摘要

> 控制流认证（CFA）允许远程验证嵌入式设备的程序是否按预期路径执行——这对 IoT/工控/汽车等安全关键场景至关重要。但现有 CFA 方案需要**代码插桩**（插入监控指令）或**频繁上下文切换**（运行时↔认证器），引入显著性能开销。RAP-Track 首次利用 ARM MCU 上已有的**Micro Trace Buffer (MTB)**和**Data Watchpoint and Trace (DWT)**硬件模块，在程序正常运行的同时并行追踪控制流——零插桩、零上下文切换。

---

## 二、核心方法

### 2.1 利用现有硬件调试特性

| ARM 特性 | 原用途 | RAP-Track 用途 |
|----------|--------|---------------|
| **MTB** | 调试 trace 缓冲 | 自动记录跳转/分支的目标地址 |
| **DWT** | 数据观察点 | 监控安全关键变量的访问 |

### 2.2 并行追踪原理

MTB 是纯硬件 trace 模块——程序执行的同时，MTB 自动将分支目标地址写入片上 SRAM 缓冲区，完全不干扰 CPU 流水线。RAP-Track 定期读取 MTB 缓冲区内容，与预期控制流图（CFG）比对，发现异常跳转即报警。

**关键优势**：零插桩意味着固件二进制无需修改——RAP-Track 对已有的商用固件完全兼容。

### 2.3 实验

- 开源原型在 ARM Cortex-M MCU 上实现
- 相比 SOTA CFA 方案实现显著的性能提升（具体数据见论文）

---

## 三、总结与展望

RAP-Track 展示了"用现有硬件做安全"的优雅范式——MTB 和 DWT 原本只是为了调试，但在安全架构师的视角下它们成了"免费的"控制流认证加速器。

**相关资源**：[IEEE Xplore](https://ieeexplore.ieee.org) · [ARM Cortex-M MTB 参考](https://developer.arm.com)
