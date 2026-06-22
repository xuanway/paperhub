---
title: "FastPath: A Hybrid Approach for Efficient Hardware Security Verification"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-verification"
  - "information-leakage"
  - "formal-verification"
  - "microarchitecture"
  - "risc-v"
---

# FastPath: A Hybrid Approach for Efficient Hardware Security Verification

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test。针对硬件安全验证中形式化方法穷举但不规模化、仿真方法快速但不完备的两难，提出 FastPath——混合验证方法论：利用结构分析框架自动化地将仿真效率与形式化穷举性结合，在 cv32e40s RISC-V 处理器上发现此前未知的内部操作数泄漏漏洞。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Hardware Verification · Information Leakage · Formal Verification · RISC-V · Microarchitecture</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | FastPath: A Hybrid Approach for Efficient Hardware Security Verification（FastPath：高效硬件安全验证的混合方法） |
| 作者 | Lucas Deutschmann, Andres Meza, Dominik Stoffel, Wolfgang Kunz (RPTU Kaiserslautern), Ryan Kastner (UC San Diego) |
| 机构 | RPTU Kaiserslautern（德国）/ UC San Diego（美国） |
| 领域 | 硬件安全验证（Hardware Security Verification） |
| 投稿方向 | Security（Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test） |
| 关键词 | 硬件安全验证(Hardware Security Verification)、信息泄漏(Information Leakage)、形式化验证(Formal Verification)、混合方法(Hybrid Approach)、RISC-V |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；作者主页可能提供预印本 |

---

## 一、一句话核心摘要

> 硬件微架构信息泄漏（如 Spectre/Meltdown 类漏洞）的检测面临方法论的"不可能三角"：形式化验证穷举但不可规模化；仿真快速但不完备；动态方法灵活但缺乏穷举保证。FastPath 提出了一种**混合验证方法论**——通过结构分析框架自动识别硬件设计中的关键安全路径，仅在必要时调用形式化验证，其余路径使用仿真快速覆盖，在 cv32e40s RISC-V 处理器上发现此前未知的内部操作数泄漏漏洞，同时大幅降低人工分析工作量。

---

## 二、研究背景与动机

### 2.1 硬件安全验证的"不可能三角"

| 方法 | 穷举性 | 可规模化 | 自动化 |
|------|:---:|:---:|:---:|
| 形式化验证（UPEC等） | ✅ | ❌ 状态爆炸 | ⚠️ 需大量人工 |
| RTL 仿真 | ❌ | ✅ | ✅ |
| 动态 Fuzzing | ❌ | ✅ | ⚠️ |
| **FastPath（混合）** | ✅ | ✅ | ✅ |

### 2.2 现有方法的致命缺陷

- **纯形式化方法（UPEC/IFT）**：能给出"不存在信息泄漏"的数学保证，但计算复杂度随电路规模指数增长——对完整 SoC 不可行。
- **纯仿真方法**：覆盖范围完全取决于测试向量的质量，可能遗漏微妙的瞬态泄漏路径。
- **手动混合**：工程师手工选择"哪些路径需要形式化验证"——效率低、容易遗漏。

### 2.3 论文贡献

1. **结构分析驱动的自动路径筛选**：通过硬件网表的拓扑分析自动识别潜在信息泄漏路径，决定"仿真足够"还是"必须形式化"。
2. **混合验证框架**：仿真处理大部分安全无关路径 → 形式化验证仅攻击关键泄漏路径。
3. **cv32e40s 新漏洞发现**：在 OpenHW Group 的安全 RISC-V 核心中发现此前未知的内部操作数泄漏，并提交了修复。

---

## 三、提出的解决方案

### 3.1 FastPath 混合流程

1. **结构分析**：对处理器网表进行静态分析，标记所有与安全敏感寄存器（如密钥寄存器、PC、栈指针）有数据流/控制流依赖的信号路径。
2. **路径重要性排序**：根据路径的"信息流量"（多少比特从敏感源流向可观测汇）对路径排序。
3. **分层决策**：
   - 低信息流量 + 高结构复杂性 → **仿真覆盖**（穷举不可能也无必要）
   - 高信息流量 + 低结构复杂性 → **形式化穷举**（关键路径，必须保证零泄漏）
   - 中等 → 仿真 + 覆盖率驱动的形式化边界检查
4. **漏洞报告**：形式化验证一旦发现反例（泄漏可能），自动生成最小 trace 供人工确认。

### 3.2 结构分析框架

FastPath 的结构分析基于硬件设计的**信息流图（IFG）**：
- 节点 = 寄存器/内存/端口
- 边 = 组合逻辑路径（带权重：位宽 × 激活概率）
- 目标：找到所有从敏感源到可观测汇的路径，并按总权重排序

### 3.3 cv32e40s 漏洞发现

cv32e40s 是 OpenHW Group 维护的一个安全 RISC-V 核心（用于 IoT/嵌入式）。FastPath 发现**内部操作数泄漏**：某些算术指令的中间结果在特定微架构状态下被缓存在数据路径寄存器中，且该寄存器的值在某些条件分支下可被侧信道观测——直接违反了安全规范中"内部操作数不得通过微架构状态泄漏"的要求。

---

## 四、实验评估

### 4.1 核心结果

| 指标 | 结果 |
|------|------|
| **人工工作量** | 相比纯形式化方法显著减少 |
| **穷举性保证** | 关键安全路径与纯形式化方法同等 |
| **新漏洞发现** | cv32e40s 中此前未知内部操作数泄漏 |
| **可扩展性** | 对完整处理器核心可行（纯形式化无法处理） |

### 4.2 局限性分析

- **结构分析的精度依赖网表质量**：如果门级网表与 RTL 语义有偏差，可能漏标或误标泄漏路径。
- **无法发现时序侧信道**：基于功能的信息流分析不能检测功耗/电磁/时序侧信道泄漏——需要物理层验证。
- **形式化 property 的质量决定检测能力**：仍需要安全工程师正确定义"什么是泄漏"。

---

## 五、总结与展望

FastPath 通过结构分析驱动的混合验证方法论，为硬件安全验证的"不可能三角"提供了一条实际可行的出路。在 cv32e40s 上的新漏洞发现证明了该方法不仅理论上可行，而且具有真实的漏洞发现能力。

**核心资源**：[IEEE Xplore](https://ieeexplore.ieee.org) · RPTU 作者主页 · UC San Diego Kastner Group
