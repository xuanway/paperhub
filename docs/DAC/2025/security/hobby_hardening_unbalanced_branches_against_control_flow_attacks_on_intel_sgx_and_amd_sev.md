---
title: "HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "control-flow-attack"
  - "intel-sgx"
  - "amd-sev"
  - "tee"
  - "compiler-security"
---

# HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4 — Embedded and Cross-Layer Security。针对 TEE（Intel SGX/AMD SEV）中控制流攻击在源代码级分支平衡防御下的绕过威胁，提出 HoBBy——指令级分支加固编译器工具：通过单步分析方法识别秘密依赖分支中的非平衡指令，并采用"影子化、齿轮化、螺旋化"三种技术加固，在密码库上仅 2.8% 运行时开销即抵御三种 SOTA 攻击。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Control-Flow Attack · Intel SGX · AMD SEV · TEE · Compiler Security</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV（HoBBy：面向 Intel SGX 和 AMD SEV 中控制流攻击的非平衡分支加固） |
| 作者 | Chang Liu, Shuaihu Feng, Yuan Li, Dong Wang, Trevor E. Carlson |
| 机构 | National University of Singapore (NUS) |
| 领域 | 硬件安全 / TEE 安全（Hardware Security / TEE Security） |
| 投稿方向 | Security（Session: SEC4 — Embedded and Cross-Layer Security） |
| 关键词 | 控制流攻击(Control Flow Attack)、Intel SGX、AMD SEV、分支平衡(Branch Balancing)、编译器安全(Compiler Security) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings） |

---

## 一、一句话核心摘要

> Intel SGX 和 AMD SEV 的 TEE 保护了数据和代码的机密性与完整性——但当秘密数据参与分支条件时，分支执行时间的差异（非平衡分支）可通过计时侧信道泄漏秘密。现有源代码级分支平衡防御（如 `cmov` 化、常量时间编程）可以被**指令级微架构效应**绕过——同一 C 语句编译后可能产生不同周期数的指令序列。HoBBy 是首个指令级分支加固编译器工具：单步分析识别秘密依赖分支中的非平衡指令，采用影子化、齿轮化、螺旋化三种独有技术使并行控制流在指令级别不可区分，仅 2.8% 运行时开销。

---

## 二、研究背景与动机

### 2.1 TEE 中的控制流计时攻击

Intel SGX 和 AMD SEV 保护内存中的代码和数据免受特权软件（OS/Hypervisor）的攻击。但它们不保护**执行时间**——攻击者（恶意的 OS）可以通过观测 Enclave 的执行时间推断：

- `if (secret_bit == 1) { heavy_op(); } else { light_op(); }` → 时间差异直接泄漏 secret_bit

### 2.2 源代码级平衡的不足

防御方通常使用常量时间编程：
- 替换条件分支为 `cmov`（条件移动）
- 确保分支两侧执行相同数量的指令

**但编译器优化可能打破平衡**：同一 C 代码经不同优化级别（-O2 vs -O3）可能在分支两侧产生不同周期数的指令序列——使源代码级平衡"名存实亡"。

### 2.3 本文贡献

1. **单步指令级分析**（Single-Step Analysis）：自动识别秘密依赖分支中在微架构层面对称的指令。
2. **三种创新加固技术**：影子化（Shadowing）、齿轮化（Cogging）、螺旋化（Spiraling）。
3. **极低开销**：密码库仅 2.8% 运行时开销，代码膨胀适度。

---

## 三、提出的解决方案

### 3.1 单步分析

HoBBy 作为 LLVM 后处理 pass 运行：
1. 从已编译的二进制反汇编识别所有条件分支
2. 通过污点追踪确定哪些分支条件依赖秘密数据
3. 对秘密依赖分支两侧进行逐对指令匹配，发现非平衡指令

### 3.2 三种加固技术

| 技术 | 原理 | 适用场景 |
|------|------|----------|
| **影子化 (Shadowing)** | 在短路径插入空操作指令（模拟长路径的延迟） | 简单直接，可能增加功耗 |
| **齿轮化 (Cogging)** | 将长路径的指令替换为等延迟的等效序列 | 不增加总指令数 |
| **螺旋化 (Spiraling)** | 通过循环展开/重组使两侧的微架构资源使用模式（如 ALU/内存端口）对称 | 防止资源争用侧信道 |

**核心创新**：这三种技术在指令级别操作（而非源代码级别），确保编译优化不会破坏平衡。

### 3.3 与现有方法的本质区别

| 维度 | 源代码平衡 | HoBBy |
|------|----------|-------|
| 操作层级 | C/C++ 源码 | x86 指令（已编译二进制） |
| 编译器免疫 | ❌ 优化可破坏 | ✅ 在优化后分析加固 |
| 微架构感知 | ❌ | ✅ 考虑执行端口/延迟 |

---

## 四、实验评估

| 指标 | 结果 |
|------|------|
| **运行时开销** | 密码库仅 **2.8%** |
| **代码膨胀** | 适度（具体见论文） |
| **安全验证** | 抵御 3 种 SOTA 控制流攻击 |
| **真实应用** | 4 个真实 TEE 应用 |
| **平台** | Intel SGX + AMD SEV |

### 局限性

- **2.8% 是密码库的平均**：计算密集的非密码应用可能有不同开销特征。
- **代码膨胀**：在存储受限的极简 TEE 上，膨胀的二进制可能是问题。(个人观点)

---

## 五、总结与展望

HoBBy 将 TEE 中控制流攻击的防御从"编译器前的源代码平衡"推进到"编译器后的指令级平衡"，解决了源代码防御被编译优化瓦解的根本问题。2.8% 的开销使其成为实用化的 TEE 加固方案。

### 相关资源

- **Intel SGX SDK**：[https://github.com/intel/linux-sgx](https://github.com/intel/linux-sgx)
- **AMD SEV**：[https://developer.amd.com/sev/](https://developer.amd.com/sev/)
- **LLVM**：[https://llvm.org/](https://llvm.org/)
- **常量时间编程指南**：[https://github.com/veorq/cryptocoding](https://github.com/veorq/cryptocoding)
