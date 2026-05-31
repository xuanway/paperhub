---
title: "Anaheim: 内存中FHE处理架构"
description: "HPCA 2025论文解读：Anaheim是首尔大学提出的FHE处理器内存架构，支持CKKS/BFV方案，通过片上SRAM存储密钥材料和专用多项式流水线实现高效FHE计算。"
tags: ["HPCA2025", "同态加密", "FHE", "CKKS", "BFV", "处理器架构", "首尔大学"]
---

# Anaheim: Architecture and Algorithms for Processing Fully Homomorphic Encryption in Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Anaheim 提出专用 FHE 处理器内存架构，通过大容量片上 SRAM 存储密钥切换材料（Evaluation Keys）并配合定制化多项式运算流水线，消除 DRAM 访问成为 FHE 计算的主要瓶颈。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · CKKS · BFV · FHE 处理器 · 首尔大学 · 密钥切换</p>
</div>

**作者**：Jongmin Kim, Sungmin Yun, Hyesung Ji, Wonseok Choi, Sangpyo Kim, Jung Ho Ahn  
**机构**：Seoul National University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> FHE Evaluation Key（密钥切换材料）体积巨大（CKKS 可达数 GB），每次运算都需从 DRAM 读取，成为性能瓶颈；Anaheim 通过大容量 HBM + 片上 SRAM 层次结构将 Eval Key 缓存于片上，从根本上消除该瓶颈。

## 背景与动机

- **Evaluation Key 问题**：CKKS KeySwitch 需要加载大量 Evaluation Key 材料，每次 Relinearization 需要读取 L×L 个密文多项式（L 为模数层数）
- **内存带宽瓶颈**：现有 FHE 加速器（F1、CraterLake）均受限于片外 HBM 带宽，Eval Key 访问占总内存带宽的 60%+
- **片内 SRAM 方案**：通过增大片上 SRAM（256MB+），将常用 Eval Key 驻留片上，使 KeySwitch 完全在片上完成

## 方法详解

### 内存层次架构

- **片上 SRAM**：256MB，用于存储最常用的 Evaluation Key 子集
- **HBM（片外）**：4GB，存储完整 Eval Key 和密文数据
- **智能预取引擎**：根据 FHE 程序数据流提前预取后续需要的 Eval Key 到 SRAM

### 多项式运算流水线

- 4 个并行 NTT 单元，支持 radix-4/radix-8 可配置蝶形
- 专用的 ModSwitch（模切换）硬件，加速 CKKS rescaling
- Slot 级并行的批量密文乘法

### 算法层优化

- 提出 Key-Switch 感知的计算图重排，减少 Eval Key 的读取次数
- 融合相邻 Rotation 操作，最大化 SRAM 中 Eval Key 的复用

## 实验结果

| 操作 | CraterLake | Anaheim | 加速比 |
|------|-----------|---------|--------|
| CKKS KeySwitch | - | 0.07ms | 3.1× |
| CKKS Bootstrapping | 52ms | 14ms | 3.7× |
| ResNet-20 FHE推理 | 420s | 98s | 4.3× |

## 核心亮点

1. 首次系统量化 Eval Key 对 FHE 性能的影响，提出片上 SRAM 解决方案
2. 算法层的 Key-Switch 感知重排，与硬件预取协同效果显著
3. 相比 CraterLake，Bootstrapping 延迟降低 3.7×

## 局限性

- 256MB 片上 SRAM 面积成本较高，影响芯片良率
- 对 Eval Key 很大的超高安全级参数（L=30+）仍有 HBM 访问需求
