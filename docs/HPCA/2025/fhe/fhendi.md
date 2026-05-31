---
title: "FHENDI: Near-DRAM FHE加速器"
description: "HPCA 2025论文解读：FHENDI是IBM Research提出的近DRAM FHE加速器，通过编译器生成的FHE应用实现高效多项式运算，相比CPU加速超过100×。"
tags: ["HPCA2025", "同态加密", "FHE", "Near-DRAM", "NMP", "IBM Research", "编译器"]
---

# FHENDI: A Near-DRAM Accelerator for Compiler-Generated Fully Homomorphic Encryption Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">FHENDI 将 FHE 计算下推到 DRAM 近旁，通过编译器自动生成 FHE 应用内核并映射到近内存处理单元，在多项式乘法与 NTT 操作上获得超过 100× 的性能提升。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 同态加密 · 近内存计算 · IBM Research · 编译器辅助</p>
</div>

**作者**：Yongmo Park, Aporva Amarnath, Subhankar Pal, Karthik Swaminathan, Alper Buyuktosunoglu, Hayim Shaul, Ehud Aharoni, Nir Drucker, Wei D. Lu, Omri Soceanu, Pradip Bose  
**机构**：IBM Research; University of Michigan  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> FHE 的计算瓶颈在于大规模多项式操作（NTT、模乘）的内存带宽需求；FHENDI 通过将处理单元置于 DRAM 近旁，配合编译器自动生成映射代码，消除 CPU-DRAM 数据传输瓶颈。

## 背景与动机

- **问题**：全同态加密（FHE）操作涉及大规模多项式（系数数量 2^12 ~ 2^17），主要操作为 NTT（数论变换）和模乘，内存访问量极大。
- **CPU瓶颈**：FHE 操作的计算强度低（arithmetic intensity < 5 FLOP/Byte），完全受制于 DDR 内存带宽，CPU/GPU 均难以充分利用计算资源。
- **近内存加速思路**：将 NTT butterfly 操作、模乘单元直接集成在 DRAM Die 内部，利用片内带宽（远超片外 DDR 带宽）实现加速。

## 方法详解

### 硬件架构

FHENDI 在 3D 堆叠 DRAM（类似 HBM）的 base die 中集成 FHE 处理引擎：

- **NTT Engine**：流水线化的蝶形运算单元，直接在 DRAM bank 级别处理多项式系数
- **ModMul Unit**：支持任意 FHE 模数的 Barrett Reduction 模乘单元
- **Key-Switch Engine**：加速 Relinearization（密钥切换）操作

### 编译器支持

- 扩展 IBM FHE 编译器框架（基于 MLIR），自动识别 FHE 程序中的多项式运算子图
- 将计算内核自动下发到 FHENDI 处理单元，CPU 只负责控制流与标量运算
- 支持 CKKS、BFV、BGV 等主流 FHE 方案

## 实验结果

| 操作 | CPU（Intel Xeon） | FHENDI | 加速比 |
|------|------------------|--------|--------|
| NTT (2^16) | 1.2ms | 0.008ms | 150× |
| CKKS Mul+Rescale | 18ms | 0.12ms | 150× |
| CKKS Bootstrapping | 850ms | 9ms | 94× |
| AES-128 (FHE) | 3.2h | 1.9min | 101× |

## 核心亮点

1. Near-DRAM 方案绕过 DDR 带宽瓶颈，内存内带宽比片外带宽高 10×+
2. 编译器全自动映射，无需手工修改 FHE 程序
3. 与现有 FHE 软件库（HElib、OpenFHE）完全兼容

## 局限性

- 需要特殊 3D 堆叠 DRAM 硬件，量产成本较高
- 对大参数集（N=2^17，用于高安全级别）的支持受片内 SRAM 容量限制
