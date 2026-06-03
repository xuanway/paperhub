---
title: ""OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "intel-sgx"
  - "intel-tdx"
  - "power-side-channel"
  - "out-of-band"
  - "confidential-computing"
---

# "OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。绕过 Intel 对 MSR 功耗遥测的过滤防御，首次利用服务器 BMC 带外管理接口（OOB）获取 Package Configuration Space 中的功耗数据，在 Intel Sapphire Rapids 上对 SGX 和 TDX 实施远程功耗侧信道攻击——恢复 SGX 中 2048-bit RSA 密钥并泄漏 TDX 中 AESNI 密钥。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Intel SGX · Intel TDX · Power Side-Channel · OOB · Confidential Computing</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | "OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX（OOPS!：面向 Intel SGX 和 TDX 的带外远程功耗侧信道攻击） |
| 作者 | Nimish Mishra, Kislay Arya, Sarani Bhattacharya (IIT Kharagpur), Paritosh Saxena (Intel), Debdeep Mukhopadhyay (IIT Kharagpur) |
| 机构 | IIT Kharagpur / Intel |
| 领域 | 硬件安全 / 机密计算 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | Intel SGX、Intel TDX、功耗侧信道(Power Side-Channel)、带外(OOB)、BMC、机密计算(Confidential Computing) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132941) |

---

## 一、一句话核心摘要

> Intel 发现 MSR_PKG_Energy_Status 等功耗遥测寄存器被用于远程功耗侧信道攻击后，引入了 IA32_MISC_PACKAGE_CTLS 过滤机制阻断此类攻击。但 OOPS! 发现了一条**完全绕开该过滤器的秘密通道**：服务器 BMC（基板管理控制器）的带外管理接口可读 Package Configuration Space（PCS）中的功耗数据——该路径完全不在 IA32_MISC_PACKAGE_CTLS 的过滤范围内。在 Intel Sapphire Rapids 上成功恢复 SGX 中的 2048-bit RSA 密钥（单步假设）和泄漏 TDX 中的 AESNI 密钥（无需单步）。

---

## 二、核心方法

### 2.1 带外 vs 带内

| 路径 | 传统 MSR 攻击 | OOPS! OOB 攻击 |
|------|:----------:|:----------:|
| 访问方式 | 带内 RDMSR 指令 | 带外 BMC→PCS |
| 被 IA32_MISC_PACKAGE_CTLS 阻止？ | ✅ 是 | ❌ 否 |
| 权限要求 | Ring 0 (内核) | BMC 网络访问 |

### 2.2 技术路径

1. 逆向工程 BMC→PCS 的带外协议
2. 通过 OOB 接口读取 Package 功耗（只读、无需更高权限）
3. 功耗迹线 → CPA 攻击 → 密钥恢复

### 2.3 实验结果

| 目标 | 环境 | 结果 |
|------|------|------|
| RSA-2048 | MbedTLS in SGX | ✅ 密钥恢复（单步假设） |
| AESNI | TDX (Sapphire Rapids) | ✅ 密钥泄漏（无需单步） |

---

## 三、总结

OOPS! 展示了机密计算安全边界的一个致命盲区：**BMC 是数据中心管理的必要组件，但它本质上是硬件级的后门**——带外访问绕过所有 OS/VMM/Enclave 安全边界。云服务商需要在 BMC 网络隔离和访问审计上加强防线。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132941)
