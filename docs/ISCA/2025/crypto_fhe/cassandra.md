---
title: "Cassandra: 密码程序顺序执行高效强制"
description: "ISCA 2025论文解读：Cassandra提出针对密码程序的顺序执行强制机制，防止乱序执行引入的时序侧信道攻击，同时最小化性能开销。"
tags: ["ISCA2025", "密码安全", "侧信道", "顺序执行", "微架构"]
---

# Cassandra: Efficient Enforcement of Sequential Execution for Cryptographic Programs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Cassandra 在微架构层面为密码程序提供顺序执行保证，阻止乱序执行（OoO）引入的时序侧信道泄漏，同时通过精细粒度标注减少不必要的性能损失。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 密码程序安全 · 侧信道防护 · 顺序执行 · NUS</p>
</div>

**作者**：Ali Hajiabadi, Trevor E. Carlson  
**机构**：National University of Singapore (NUS)  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 1B: Crypto & Fully Homomorphic Encryption  

---

## 一句话总结

> 密码程序中的乱序执行是侧信道攻击的根源之一；Cassandra 以最小性能代价强制密码代码区域顺序执行，阻断时序泄漏路径。

## 背景与动机

- **时序侧信道**：现代乱序处理器（OoO）的执行时序依赖数据，攻击者可通过测量密码操作时序恢复密钥
- **现有防御不足**：常量时间编程（constant-time programming）依赖程序员保证，容易出错；现有硬件方案开销大
- **Cassandra 思路**：通过 ISA 扩展标注密码代码区域，微架构在标注范围内强制顺序执行关键操作

## 主要贡献

1. **ISA 扩展**：引入轻量级标注指令，精确圈定需要顺序执行保护的密码代码范围
2. **微架构强制机制**：在乱序核中选择性禁用数据相关的推测执行，不影响标注外代码性能
3. **形式化安全证明**：证明 Cassandra 可阻断特定类别的时序侧信道
4. **低开销实现**：对非密码代码几乎零性能影响，密码代码加速比损失可控

## 实验结果

- 常见密码库（OpenSSL, libsodium）的保护开销 **< 5%**
- 成功防御 AES、RSA、ECC 场景下的时序攻击
- 与完全顺序执行方案相比，性能提升显著

## 关键词

时序侧信道 · 密码程序安全 · 乱序执行 · 常量时间 · 微架构安全 · ISCA 2025
