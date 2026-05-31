---
title: "Finesse: 配对密码软硬件协同设计框架"
description: "ISCA 2025论文解读：Finesse提出面向配对密码的敏捷软硬件协同设计框架，通过可重配硬件加速配对运算，覆盖ZKP等多种应用。"
tags: ["ISCA2025", "密码加速", "配对密码", "ZKP", "软硬件协同"]
---

# Finesse: An Agile Design Framework for Pairing-based Cryptography via Software/Hardware Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Finesse 为配对密码（Pairing-based Cryptography）构建灵活的软硬件协同设计框架，通过可重配硬件加速椭圆曲线配对操作，覆盖 ZKP（Groth16、PLONK 等）的高效验证。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 配对密码 · ZKP硬件 · 软硬件协同 · BUPT</p>
</div>

**作者**：Tianwei Pan, Tianao Dai, Jianlei Yang, Hongbin Jing, Yang Su, Zeyu Hao, Xiaotao Jia, Chunming Hu, Weisheng Zhao  
**机构**：Beijing University of Posts and Telecommunications 等  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 1B: Crypto & Fully Homomorphic Encryption  

---

## 一句话总结

> Finesse 通过软硬件协同框架，以可重配加速器高效支持配对密码多种曲线和协议，显著加速 ZKP 证明验证等应用。

## 背景与动机

- **配对密码广泛性**：Groth16、PLONK 等 ZKP 协议和 BLS 签名均依赖双线性配对运算，计算复杂度极高
- **现有方案局限**：专用 ASIC 固定曲线参数，灵活性差；软件实现吞吐量不足，无法满足实际部署需求
- **本文方案**：Agile（敏捷）设计——可重配硬件支持多种曲线（BLS12-381、BN254 等），编译器自动映射操作到硬件

## 主要贡献

1. **统一配对运算抽象**：提出覆盖 Miller Loop 和 Final Exponentiation 的统一计算模型
2. **可重配硬件架构**：模块化乘法器和调度引擎，支持多种有限域参数切换
3. **软件编译框架**：自动将上层 ZKP 协议映射到 Finesse 加速指令
4. **系统集成**：与 RISC-V 流水线集成，实现低延迟配对计算

## 实验结果

- 相比 CPU 软件实现，配对运算加速 **>100×**
- 覆盖 BLS12-381、BN254、BLS12-377 等主流曲线
- ZKP 证明验证吞吐量大幅提升，适用于区块链和隐私计算场景

## 关键词

配对密码 · 双线性配对 · ZKP · 零知识证明 · 软硬件协同 · ISCA 2025
