---
title: "SSBleed: ARM Armv9 CPU上通过Speculative Store Bypass的非推测性侧信道攻击"
description: "HPCA 2026论文解读：在ARM Armv9处理器上发现无需推测执行即可利用Speculative Store Bypass实施侧信道攻击的新机制。"
tags: ["HPCA2026", "硬件安全", "ARM", "侧信道", "Speculative Store Bypass"]
---

# SSBleed: Non-speculative Side-channel Attacks via Speculative Store Bypass on Armv9 CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">在 ARM Armv9 处理器上，即使不触发推测执行，仅通过 Speculative Store Bypass 的副作用即可实施侧信道攻击并泄露敏感数据。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 硬件安全 · ARM安全 · 非推测性侧信道</p>
</div>

**作者**：Chang Liu, Hongpei Zheng, Xin Zhang, Dapeng Ju, Dongsheng Wang, Yinqian Zhang, Trevor E. Carlson  
**机构**：Tsinghua University, Southern University of Science and Technology, National University of Singapore  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 在 ARM Armv9 上，Speculative Store Bypass（SSB）即使在非推测路径中也会引发可观测的微架构副作用，攻击者可利用此构建隐蔽信道。

## 背景与动机

- **问题**：Spectre/Meltdown 缓解措施主要针对推测执行路径，但非推测路径的安全性研究不足。
- **现有方案的不足**：SSBD（Speculative Store Bypass Disable）性能开销大（10-40%），且部分平台未默认启用。
- **本文思路**：系统分析 ARM Armv9 的 SSB 行为，发现即使不触发推测执行也能产生可测量的延迟差异。

## 方法详解

### 核心思想

SSB 允许 load 操作在对应 store 提交前提前读取，这一机制在**非推测路径**中也会改变 cache 状态，从而产生时序可观测的信道。

### 攻击步骤

1. 控制 store 指令与 load 指令的依赖关系
2. 利用 SSB 导致的缓存状态变化进行时序测量
3. 通过统计分析重建秘密值（如密钥字节）

## 实验结果

| 攻击目标 | 成功率 | 所需时间 |
|----------|--------|----------|
| AES T表密钥恢复 | 96.3% | < 10s |
| 内存地址推断 | 89.7% | ~30s |

## 核心亮点

1. 首次在 **非推测路径** 中利用 SSB 构建侧信道
2. 绕过了针对推测执行的所有缓解措施
3. 对 ARM Armv9 生态系统（手机、服务器）影响广泛

## 局限性

- 需要对目标程序有一定了解（代码模式）
- 攻击窗口依赖特定的内存访问模式
