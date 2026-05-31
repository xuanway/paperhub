---
title: "UniFHE: 支持多样代数结构与均衡内存系统的更快FHE加速器"
description: "HPCA 2026论文解读：UniFHE为全同态加密设计统一加速架构，支持BFV/CKKS/TFHE等多种FHE方案，通过均衡内存系统消除访存瓶颈。"
tags: ["HPCA2026", "同态加密", "FHE加速器", "隐私计算", "CAS"]
---

# UniFHE: Faster Accelerator for FHE with Diverse Algebraic Structure and Balanced Memory System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">UniFHE 通过统一计算引擎支持 BFV、CKKS、TFHE 等主流 FHE 方案，并设计均衡内存层次结构消除数论变换（NTT）的访存瓶颈，端到端加速比达 12.3×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 全同态加密 · FHE加速器 · 隐私计算 · NTT优化</p>
</div>

**作者**：Qingyun Niu, Lutan Zhao, Ming Cai, kai li, Dan Meng, Rui Hou  
**机构**：Key Laboratory of Cyberspace Security Defense, IIE, CAS; University of Chinese Academy of Sciences  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 不同 FHE 方案使用不同的代数结构（环多项式的参数配置差异显著），现有加速器只针对单一方案优化；UniFHE 设计了统一的 NTT 引擎和均衡内存系统，以一套硬件高效支持所有主流 FHE 方案。

## 背景与动机

- **问题**：全同态加密允许对加密数据直接计算，是隐私保护计算的基础，但计算开销比明文计算高 10^4–10^6 倍，严重限制实用性。
- **现有方案的不足**：F1、CraterLake 等 FHE 加速器针对 CKKS 设计，不能高效支持 BFV（整数运算）和 TFHE（布尔电路）；不同方案的参数空间（多项式维度、模数大小）差异导致硬件利用率低。
- **本文思路**：分析三类 FHE 方案的计算共性，设计参数可配置的统一 NTT 引擎，以及针对 FHE 访存模式优化的内存层次。

## 方法详解

### 核心思想

**统一 NTT 引擎**：NTT（数论变换）是 FHE 的核心原语，但不同方案的多项式维度从 2^12 到 2^16 不等。UniFHE 的 NTT 引擎支持动态配置维度和模数，无需硬件重编程。

### 均衡内存系统

FHE 中间值（多项式系数）的访存量巨大且规律性差，针对此设计：
1. 多 Bank 并行访问消除 Bank 冲突
2. 预取引擎隐藏 NTT butterfly 操作的访存延迟
3. 压缩存储减少中间值内存占用

## 实验结果

| FHE方案 | vs. CPU（OpenFHE） | vs. GPU | vs. 专用加速器 |
|---------|------------------|---------|--------------|
| CKKS | 187× | 12.3× | 1.4× |
| BFV | 143× | 9.8× | 2.1× |
| TFHE | 512× | 18.7× | — |

## 核心亮点

1. 首个统一支持三类主流 FHE 方案的专用加速器
2. 均衡内存设计将访存利用率从 45% 提升至 87%
3. 适合云端 FHE 即服务（FHEaaS）部署

## 局限性

- 面积比单一方案专用加速器大约 35%
- TFHE 的 Bootstrapping 仍是最大瓶颈
