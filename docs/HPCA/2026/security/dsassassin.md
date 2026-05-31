---
title: "DSASSASSIN: 利用Intel DSA的跨虚拟机侧信道攻击"
description: "HPCA 2026论文解读：首次发现Intel Data Streaming Accelerator（DSA）可被利用实施跨VM侧信道攻击，威胁云计算安全。"
tags: ["HPCA2026", "硬件安全", "侧信道攻击", "Intel DSA", "虚拟化"]
---

# DSASSASSIN: Cross-VM Side-Channel Attacks by Exploiting Intel Data Streaming Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">首次揭示 Intel Data Streaming Accelerator（DSA）可被攻击者利用，在不同虚拟机之间发起侧信道攻击，绕过现有隔离机制。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 硬件安全 · 侧信道攻击 · 云计算安全</p>
</div>

**作者**：Ben Chen, Kunlin Li, Shuwen Deng, Dongsheng Wang, Yun Chen  
**机构**：The Hong Kong University of Science and Technology (Guangzhou), Tsinghua University  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> Intel DSA（数据流加速器）存在侧信道漏洞，攻击者可跨虚拟机边界泄露敏感信息，现有云端隔离机制无法防护。

## 背景与动机

- **问题**：现代服务器广泛部署 Intel DSA 等片上加速器以提升I/O性能，但这些加速器的安全性尚未经过深入审查。
- **现有方案的不足**：VM隔离机制主要关注CPU和内存，对共享加速器资源的侧信道风险缺乏防护。
- **本文思路**：分析DSA的工作机制，发现其内部状态（完成队列、工作队列争用延迟）可被转变为跨VM信道。

## 方法详解

### 核心思想

通过监控 DSA 工作队列（Work Queue）的提交延迟和完成状态，推断同一物理主机上其他 VM 的访问模式，从而泄露信息。

### 攻击向量

1. **争用侧信道**：DSA 工作队列容量有限，测量提交延迟可感知受害VM的DSA使用模式
2. **完成状态监听**：通过轮询共享完成队列状态位推断操作时序
3. **跨VM信息泄露**：结合两种信道，实现对同主机VM的内存访问模式重建

## 实验结果

| 场景 | 信道带宽 | 错误率 |
|------|----------|--------|
| 同物理核心跨VM | ~12 KB/s | < 3% |
| 跨NUMA节点VM | ~4 KB/s | < 7% |
| AES密钥恢复 | — | 成功率 >90% |

## 核心亮点

1. **首次**系统性分析 Intel DSA 的侧信道攻击面
2. 攻击无需 root 权限，普通用户态进程即可实施
3. 揭示加速器安全审查的必要性，对未来硬件设计有重要指导意义

## 局限性

- 攻击依赖DSA工作队列共享，若采用严格VM专属队列可缓解
- 带宽相对有限（KB级），不适合大规模实时数据泄露
