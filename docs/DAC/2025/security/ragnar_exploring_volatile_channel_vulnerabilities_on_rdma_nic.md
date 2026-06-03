---
title: "RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rdma"
  - "nic"
  - "covert-channel"
  - "side-channel"
  - "data-center"
---

# RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。首次系统探索 RDMA 网卡（NIC）上的硬件争用挥发性信道漏洞——RAGNAR 通过多粒度微基准逆向工程构建隐蔽信道和侧信道攻击，在 ConnectX-5 上实现 3.2× 于 SOTA 的带宽，对分布式数据库和分解式内存实现 95.6% 操作指纹识别准确率。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · RDMA · NIC · Covert Channel · Side-Channel · Data Center</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC（RAGNAR：探索 RDMA 网卡上的挥发性信道漏洞） |
| 作者 | Yunpeng Xu, Yuchen Fan, Teng Ma, Shuwen Deng |
| 机构 | 清华大学等 |
| 领域 | 硬件安全 / 数据中心安全 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | RDMA、NIC、隐蔽信道(Covert Channel)、侧信道(Side-Channel)、数据中心(Data Center) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133127) |

---

## 一、一句话核心摘要

> RDMA（远程直接内存访问）是数据中心高性能通信的基石——绕过 CPU 直接访问远端内存，延迟低至微秒级。但 RDMA 网卡（如 NVIDIA ConnectX-5）内部的硬件资源（DMA 引擎、缓存、PCIe 队列）在多租户共享时产生**硬件争用**——RAGNAR 首次系统性地将这些争用点武器化为挥发性信道（Volatile Channel）：隐蔽信道带宽达 SOTA 的 3.2×，侧信道可对分布式数据库操作实现 95.6% 的指纹识别准确率。

---

## 二、核心方法

### 2.1 多粒度逆向工程

RAGNAR 对 RDMA NIC 进行三层微基准逆向：
- **指令级**：识别不同 RDMA 操作（READ/WRITE/ATOMIC）在硬件资源上的争用指纹
- **缓存级**：NIC 内部 Translation Cache 的命中/缺失模式
- **PCIe 队列级**：多 QP（Queue Pair）共享 PCIe 带宽的时序竞争

### 2.2 实验结果

| 攻击类型 | 指标 | 结果 |
|----------|------|------|
| 隐蔽信道 | 带宽 vs SOTA | **3.2×** |
| 侧信道 | 指纹识别准确率 | **95.6%** |
| 目标 | 分布式数据库、分解式内存 | 操作类型 + 敏感地址恢复 |
| 平台 | ConnectX-5 | 真实硬件 |

### 2.3 威胁场景

- **多租户云数据中心**：不同租户的虚拟机共享同一 RDMA NIC → RAGNAR 允许恶意租户窃取其他租户的 RDMA 操作模式
- **分解式内存**：内存池化架构中，攻击者可推断远端内存页的访问频率和地址

---

## 三、总结与展望

RAGNAR 将"硬件争用侧信道"的战场从 CPU 缓存扩展到了 RDMA NIC——数据中心的每个共享硬件组件都可能是潜在的侧信道源。NVIDIA 和 Intel 的下一代 NIC 需要考虑硬件资源分区隔离。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133127)
