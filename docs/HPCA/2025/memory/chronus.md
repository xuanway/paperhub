---
title: "Chronus: 分析与保护工业界DRAM Rowhammer防护方案"
description: "HPCA 2025论文解读：ETH Zürich团队对工业界现役DRAM Rowhammer防护（TRR、PRAC等）进行系统安全性分析，发现多类绕过攻击，并提出Chronus统一防护框架。"
tags: ["HPCA2025", "Rowhammer", "DRAM安全", "TRR", "PRAC", "DDR5", "ETH Zürich"]
---

# Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Chronus 对工业界最前沿的 Rowhammer 防护（JEDEC DDR5 PRAC、Samsung TRR 等）进行全面安全性分析，揭示多类实际可行的绕过攻击，并提出 Chronus 统一防护框架，在安全性和性能之间取得更优权衡。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Rowhammer · DRAM · DDR5 · PRAC · TRR · ETH Zürich · Onur Mutlu</p>
</div>

**作者**：Oğuzhan Canpolat, Giray Yaglikci, Geraldo Francisco de Oliveira, Ataberk Olgun, Nisa Bostanci, Ismail Emir Yuksel, Haocong Luo, Oğuz Ergin, Onur Mutlu  
**机构**：TOBB ETÜ & ETH Zürich; ETH Zürich  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> DDR5 引入的 PRAC（Per-Row Activation Counting）被认为是"最终"Rowhammer 解决方案，但 Chronus 发现 PRAC 的多个实现细节留下安全漏洞，可被针对性攻击绕过，并提出 Chronus 框架修复这些问题。

## 背景与动机

- **DDR5 PRAC 机制**：JEDEC DDR5 规范引入 PRAC，每行 DRAM 行存储激活计数器，当计数超过阈值时触发 Alert Back-off（ABO），强制内存控制器执行受害行刷新
- **工业界的期待**：PRAC 被认为是第一个可在硬件中完全解决 Rowhammer 的方案
- **安全分析的必要性**：PRAC 规范在实现细节上有多处模糊，不同厂商实现可能存在差异，需要系统分析

## PRAC 的安全问题

Chronus 发现以下潜在攻击向量：

1. **计数器溢出攻击**：部分 PRAC 实现使用饱和计数器，激活到最大值后不再增长，攻击者可先让一行计数饱和再持续攻击，触发 ABO 但不刷新受害行
2. **ABO 洪泛**：攻击者通过多行轮流激活，频繁触发 ABO，导致内存控制器忙于处理 ABO 而延迟真正受害行的刷新
3. **时序窗口攻击**：利用 ABO 处理期间的短暂窗口继续激活相邻行

## Chronus 防护框架

- **精确计数**：使用非饱和计数器，结合周期性重置策略
- **ABO 优先级**：为每次 ABO 分配优先级，防止低优先级请求洪泛高优先级刷新
- **保守刷新策略**：ABO 触发时同时刷新攻击行的所有相邻行（+1 到 +3）

## 实验结果

| 方案 | 安全性 | 平均性能开销 | 最坏情况延迟 |
|------|--------|------------|------------|
| 原始 PRAC | 存在漏洞 | 2.1% | 15% |
| Chronus | 安全 | 2.8% | 8% |

## 核心亮点

1. 首次系统分析 DDR5 PRAC 的安全性，发现工业界已部署方案中的漏洞
2. Chronus 框架可作为 DDR5 PRAC 规范的安全补丁
3. 与 ETH Zürich DRAM 安全系列（PARA、TRR-Analysis、BlackSmith）一脉相承

## 局限性

- Chronus 依赖内存控制器固件修改，不能完全在 DRAM 端独立实现
- 某些缓解措施需要 JEDEC 规范修订才能被所有厂商采纳
