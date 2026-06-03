---
title: "ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "amd-zen"
  - "llc"
  - "cache-side-channel"
  - "reverse-engineering"
---

# ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。首次对 AMD Zen 处理器的非包含性（non-inclusive）LLC 实现实用的缓存侧信道攻击——通过逆向工程 AMD Zen 的 L2/L3 缓存寻址函数（set index、slice mapping、set index），成功构造驱逐集并攻击 OpenSSL AES T-table。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · AMD Zen · LLC · Cache Side-Channel · Reverse Engineering</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors（ZenLeak：面向 AMD Zen 处理器的实用 LLC 侧信道攻击） |
| 作者 | Han Wang, Ming Tang, Quancheng Wang, Ke Xu (Wuhan U.), Yinqian Zhang (SUSTech) |
| 机构 | 武汉大学 / 南方科技大学 |
| 领域 | 硬件安全 / 侧信道 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | AMD Zen、LLC、缓存侧信道(Cache Side-Channel)、逆向工程(Reverse Engineering)、AES |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133253) |

---

## 一、一句话核心摘要

> Intel 处理器的 LLC 侧信道攻击（如 Prime+Probe）已经非常成熟——但 AMD Zen 的**非包含性缓存**（L2 不包含于 L3）使传统驱逐集构造方法完全失效。ZenLeak 首次逆向工程了 AMD Zen 的完整缓存寻址体系（L2 set index → L3 slice → L3 set index），成功构造 AMD 上的可靠驱逐集，并实施了首个针对 AMD Zen 的 LLC 侧信道攻击——从 OpenSSL AES T-table 中成功提取密钥。

---

## 二、核心方法

### 2.1 AMD 非包含性缓存的挑战

- Intel：L2 ⊆ L3 → 驱逐 L3 中的地址自动驱逐 L2
- AMD Zen：L2 非包含 → 不知道 L3 中的物理地址映射 → 传统方法无法构造驱逐集

### 2.2 逆向工程过程

1. 通过微基准测试推断 L2 set index 哈希函数
2. 推断 L3 slice mapping（AMD Zen 使用复杂哈希将地址映射到 L3 slice）
3. 推断 L3 set index 计算
4. 构造能覆盖目标地址的驱逐集

### 2.3 实验结果

| 指标 | 结果 |
|------|------|
| 攻击目标 | OpenSSL AES T-table |
| 平台 | AMD Zen 系列 |
| 结果 | ✅ 成功提取 AES 密钥 |
| 引用 | FWCI=2.20，已被 1 篇论文引用 |

---

## 三、总结

ZenLeak 将 LLC 侧信道攻击从"Intel 专属"扩展到 AMD 阵营，结束了"AMD 不受 Prime+Probe 威胁"的神话。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133253)
