---
title: "FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "trustzone"
  - "fpga"
  - "tee"
  - "soc-fpga"
  - "heterogeneous-computing"
---

# FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test。ARM TrustZone 为 CPU 侧提供了成熟的可信执行环境（TEE），但无法覆盖 SoC-FPGA 异构架构中的 FPGA 侧。本文提出 FPGA-TrustZone——将 TrustZone 安全模型系统性地扩展到 FPGA 可编程逻辑，构建统一的 SoC-FPGA TEE 框架，在真实开发板上实现高性能低开销的安全隔离。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · TrustZone · FPGA · TEE · SoC-FPGA · Heterogeneous Architecture</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture（FPGA-TrustZone：面向 SoC-FPGA 异构架构的 TrustZone 安全扩展至 FPGA） |
| 作者 | Shuchen Wang, Fan Xindong, Xiao Xu, Shupeng Wang, Lei Ju, Zimeng Zhou |
| 机构 | 山东大学等 |
| 领域 | 硬件安全 / FPGA 安全（Hardware Security / FPGA Security） |
| 投稿方向 | Security（Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test） |
| 关键词 | TrustZone、FPGA、可信执行环境(TEE)、SoC-FPGA、异构计算(Heterogeneous Computing) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings） |

---

## 一、一句话核心摘要

> ARM TrustZone 为 CPU 上的可信执行环境（TEE）提供了成熟的安全隔离机制——但当前 SoC-FPGA 异构平台的 FPGA 侧完全暴露在 TrustZone 的保护伞之外：FPGA 上的硬件加速器可以直接访问安全世界的物理内存，打破了 TrustZone 的安全模型。FPGA-TrustZone 首次将 TrustZone 的安全隔离从 CPU 系统性扩展到 FPGA 可编程逻辑，通过硬件-软件协同设计在真实 SoC-FPGA 开发板上实现了统一的 TEE 框架，兼具高安全性与低性能开销。

---

## 二、研究背景与动机

### 2.1 TrustZone 的工作机制

ARM TrustZone 将 CPU 的硬件和软件状态划分为两个"世界"：
- **安全世界（Secure World）**：运行 TEE OS（如 OP-TEE）、处理密钥/加密/认证
- **普通世界（Normal World）**：运行标准 OS（Linux/Android）

关键隔离机制：NS 位（Non-Secure bit）被添加到 AXI 总线的读写事务中——安全世界的物理内存通过 NS=0 标记，总线互连硬件阻止普通世界的 NS=1 事务访问安全内存。

### 2.2 FPGA 侧是 TrustZone 的"阿喀琉斯之踵"

在 Zynq 等 SoC-FPGA 平台上，FPGA 可编程逻辑通过 AXI 主端口直接连接到内存互连。问题：**FPGA 主端口发起的 AXI 事务的 NS 位由 FPGA 逻辑自身决定——恶意或漏洞 FPGA 设计可以将 NS 位设为 0，从而自由访问安全世界内存。**

### 2.3 现有方法的局限

| 方法 | 局限 |
|------|------|
| **系统 MMU (SMMU)** | 需要为 FPGA 单独配置页表，性能开销大、配置复杂 |
| **完全禁用 FPGA 访问安全内存** | 否定了 FPGA 加速安全敏感工作负载（如硬件加密引擎）的价值 |
| **静态分区** | 缺乏灵活性，无法适应动态 TEE 工作负载 |

### 2.4 本文贡献

1. **FPGA-TrustZone 框架**：将 TrustZone 的双世界安全模型扩展到 FPGA 侧。
2. **硬件安全扩展**：在 FPGA 与内存互连之间插入 FPGA-TZ 控制器，强制执行 NS 位策略。
3. **真实硬件验证**：在 SoC-FPGA 开发板上实现并评估，低性能开销。

---

## 三、提出的解决方案

### 3.1 架构

FPGA-TrustZone 的核心是**FPGA-TZ 控制器**——位于 FPGA AXI 主端口与系统内存互连之间：

- **安全世界 FPGA 区域**：用于加速安全敏感计算（如加密、安全启动验证）
- **普通世界 FPGA 区域**：用于常规加速（如视频编解码）
- **FPGA-TZ 控制器**：根据 FPGA 逻辑区域的身份（由配置寄存器决定），强制为 AXI 事务注入正确的 NS 位

### 3.2 动态分区与访问控制

- TEE OS (OP-TEE) 可以通过安全监视器调用（SMC）动态配置 FPGA-TZ 控制器的分区寄存器
- 不同 FPGA 逻辑区域被分配不同的 AXI ID，FPGA-TZ 控制器基于 AXI ID 查找表注入 NS 位
- 物理上阻止普通世界 FPGA 逻辑伪造 NS=0

### 3.3 性能开销

FPGA-TZ 控制器在 AXI 事务路径上只增加一个查找表延迟（1-2 个时钟周期），对 FPGA 加速器的带宽和延迟影响可忽略。

---

## 四、实验评估

| 指标 | 结果 |
|------|------|
| **安全性** | 硬件强制 NS 位策略，恶意 FPGA 逻辑无法绕过 |
| **性能开销** | 低——AXI 路径仅增加 1-2 周期查找延迟 |
| **平台** | 真实 SoC-FPGA 开发板（Zynq 系列） |

### 局限性

- **AXI 协议依赖性**：FPGA-TZ 控制器依赖 AXI 的 NS/AWPROT 信号，对其他总线协议需适配。
- **FPGA 重配置的原子性**：FPGA 部分重配置时，需确保 TZ 分区配置的原子更新。(个人观点)

---

## 五、总结与展望

FPGA-TrustZone 填补了 TrustZone 安全模型在 SoC-FPGA 异构平台上的空白——首次将双世界隔离从 CPU 系统性地扩展到 FPGA 可编程逻辑。这对于将 FPGA 加速器纳入 TEE 安全边界具有重要的工程价值。

### 未来方向

> **与 Confidential Computing 的融合**：将 FPGA-TrustZone 扩展至 CCA (Confidential Compute Architecture) 的 Realm 模型。

### 相关资源

- **OP-TEE**：[https://github.com/OP-TEE](https://github.com/OP-TEE)
- **ARM TrustZone 技术参考**：[https://developer.arm.com/ip-products/security-ip/trustzone](https://developer.arm.com/ip-products/security-ip/trustzone)
- **Xilinx Zynq 安全**：[https://www.xilinx.com/products/technology/security.html](https://www.xilinx.com/products/technology/security.html)
