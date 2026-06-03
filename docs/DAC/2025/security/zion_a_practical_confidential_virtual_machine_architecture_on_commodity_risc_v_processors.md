---
title: "Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "risc-v"
  - "confidential-computing"
  - "virtual-machine"
  - "pmp"
---

# Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2。首次在商用 RISC-V 处理器上实现机密虚拟机（CVM）架构——无需定制硬件扩展，利用 PMP + 分页混合内存隔离、短路径 CVM 模式和分离页表安全 virtio 共享，真实应用开销 <5%。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · RISC-V · Confidential Computing · Virtual Machine · PMP</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | Zion: A Practical Confidential Virtual Machine Architecture on Commodity RISC-V Processors（Zion：面向商用 RISC-V 处理器的实用机密虚拟机架构） |
| 作者 | Jie Wang, Juan Wang (Wuhan U.), Yinqian Zhang (SUSTech) |
| 机构 | 武汉大学 / 南方科技大学 |
| 领域 | 硬件安全 / 机密计算 |
| 投稿方向 | Security（Session: SEC2） |
| 关键词 | RISC-V、机密计算(Confidential Computing)、虚拟机(Virtual Machine)、PMP、内存隔离(Memory Isolation) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133121) |

---

## 一、一句话核心摘要

> AMD SEV 和 Intel TDX 为 x86 提供了机密虚拟机（CVM）能力——但 RISC-V 生态长期缺乏可部署于**商用现货硬件**（无定制 ISA 扩展）的 CVM 方案。Zion 首次在商用 RISC-V 处理器上实现实用 CVM：利用已有的 **PMP（Physical Memory Protection）+ 分页**构建可扩展内存隔离，通过**短路径 CVM 模式**加速 VM 切换，并设计**分离页表**机制实现安全 virtio 设备共享——真实应用性能开销不到 5%。

---

## 二、核心方法

### 2.1 关键技术

| 组件 | 作用 |
|------|------|
| PMP + 分页混合隔离 | PMP 做粗粒度隔离（安全/非安全内存区域），分页做细粒度管理（VM 内部） |
| 短路径 CVM 模式 | 减少 VM 进入/退出的上下文切换开销 |
| 安全 vCPU 状态机制 | 保护并高效更新虚拟机 CPU 状态 |
| 分离页表 virtio 共享 | 安全地与宿主机共享 virtio 设备数据 |

### 2.2 实验结果

| 指标 | 结果 |
|------|------|
| 应用性能开销 | **< 5%** |
| 硬件要求 | 商用 RISC-V（无需定制扩展） |

---

## 三、总结

Zion 为 RISC-V 打开了一扇通向机密计算的大门——不需要等待 RISC-V CCA 标准成熟和定制芯片流片，当前的商用 RISC-V 硬件即可部署。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133121)
