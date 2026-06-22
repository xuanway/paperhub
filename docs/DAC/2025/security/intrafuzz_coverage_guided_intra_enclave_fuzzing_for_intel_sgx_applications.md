---
title: "IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "intel-sgx"
  - "fuzz-testing"
  - "tee"
  - "vulnerability-discovery"
---

# IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2。针对 Intel SGX 安全飞地内部代码漏洞检测中仿真环境无法复现真实硬件飞地行为的问题，提出 IntraFuzz——首个在真实硬件 SGX Enclave 内部执行的覆盖率引导 Fuzz 测试框架，发现 6 个此前未知漏洞。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Intel SGX · Fuzz Testing · TEE · Vulnerability Discovery · Enclave</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications（IntraFuzz：面向 Intel SGX 应用的覆盖率引导飞地内模糊测试） |
| 作者 | Jinhua Cui, Qiao Peng, Yiwen Yao, Ke Ye, Jiliang Zhang |
| 机构 | Hunan University（湖南大学） |
| 领域 | 硬件安全 / TEE 安全（Hardware Security / TEE Security） |
| 投稿方向 | Security（Session: SEC2） |
| 关键词 | Intel SGX、Fuzz 测试(Fuzz Testing)、飞地内(Intra-Enclave)、覆盖率引导(Coverage-Guided)、漏洞发现(Vulnerability Discovery) |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org/document/11132848/) |

---

## 一、一句话核心摘要

> Intel SGX Enclave 的"堡垒"假设——飞地内部代码是可信的——已被多次打破。但现有自动化漏洞发现工具（如 EnclaveFuzz）**仅在仿真环境**中 Fuzz SGX 边界接口，无法检测飞地内部代码的漏洞（因为仿真无法真实复现硬件 Enclave 的内存加密、远程认证等行为）。IntraFuzz 将 Fuzzer **植入真实硬件 SGX Enclave 内部**，在 Intel Xeon 256GB EPC 上对 21 个真实 SGX 应用进行覆盖率引导 Fuzz，不仅复现了 EnclaveFuzz 的所有已知漏洞，还发现了 6 个此前未知漏洞。

---

## 二、核心方法

### 2.1 为什么需要"飞地内"Fuzz？

| 维度 | 边界 Fuzz（EnclaveFuzz） | IntraFuzz（飞地内） |
|------|----------------------|---------------------|
| 测试目标 | ECALL/OCALL 接口 | Enclave 内部所有代码路径 |
| 执行环境 | 仿真（无真实 Enclave 保护） | 真实硬件 Enclave（EPC 加密、认证） |
| 漏洞覆盖 | 边界输入验证 | 内部逻辑缺陷（如缓冲区溢出、整数溢出） |

### 2.2 技术挑战

- **覆盖率收集**：SGX Enclave 内部无法直接使用 Intel PT / AFL 的覆盖率反馈机制。IntraFuzz 通过轻量级插桩将覆盖率信息从 Enclave 安全传递到外部 Fuzzer。
- **Enclave 崩溃恢复**：SGX 飞地崩溃会导致 Enclave 被销毁——IntraFuzz 需要快速重建 Enclave 并恢复 Fuzz 状态。

### 2.3 实验结果

| 指标 | 结果 |
|------|------|
| 测试应用 | 21 个真实 SGX 应用 |
| 已知漏洞复现 | 全部复现 EnclaveFuzz 发现的漏洞 |
| **新漏洞** | **6 个**此前未知 |
| 硬件平台 | Intel Xeon Scalable, 256GB EPC |

---

## 三、总结

IntraFuzz 将 SGX 漏洞发现从"仿真边界 Fuzz"推进到"真硬件飞地内全覆盖 Fuzz"，6 个新漏洞的发现证明了飞地内部代码的安全性绝非理所当然。

**相关资源**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11132848/) · [Intel SGX SDK](https://github.com/intel/linux-sgx) · [EnclaveFuzz](https://github.com/sslab-gatech/EnclaveFuzz)
