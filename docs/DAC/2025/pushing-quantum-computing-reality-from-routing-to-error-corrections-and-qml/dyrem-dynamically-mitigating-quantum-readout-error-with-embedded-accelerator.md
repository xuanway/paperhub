---
title: "DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132635">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132635</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 张量积，读出错误缓解，软件-硬件协同设计，输出稀疏性，专用加速器架构</p>
</div>

---

## 研究概要
本文提出软硬件协同DyREM嵌入式加速器，面向NISQ量子读出误差缓解。利用量子态非零稀疏性，设计动态下采样张量矩阵流，搭配非零态相似度检测消除冗余计算。FPGA实测相较主流方法提速9.6~2000倍，内存线性扩展，保真度提升1.03~1.15倍。

## 背景和动机
1. 读出噪声是NISQ设备最主要误差源，矩阵式误差缓解矩阵规模随量子比特指数膨胀，存储与计算不可行。
2. 现有张量分解方案Mthree/IBU忽略比特串扰，保真度差；QuFEM分组静态，无法适配动态测量比特集合。
3. 主流方案依赖片外大容量缓解矩阵，数据传输带宽瓶颈严重，16比特QAOA中误差缓解占总延迟88%。
4. 缺乏专用硬件挖掘测量概率稀疏性，大量重复张量乘冗余操作，长量子线路推理延迟极高。

## 相关工作
1. Mthree/IBU：单比特2×2子矩阵张量分解，无视比特间串扰，缓解精度低。
2. QuFEM：静态分组张量矩阵，仅支持固定测量比特，动态线路适配性差。
3. SpREM：基于汉明稀疏压缩矩阵，仍需片外存储，数据搬运开销巨大。
4. 机器学习类误差缓解：训练开销大，无法兼容通用张量缓解流程，通用性弱。

## 本文解决方案
### 1. 动态下采样张量数据流
依据当前实测比特集合，对静态分组母矩阵卷积下采样，分为全测/部分测/未测三类分组生成轻量化子矩阵，无需预定义分组。
### 2. 非零态导向压缩计算
挖掘噪声分布稀疏特性，将指数规模缓解矩阵压缩至线性；窗口相似度检测，复用重复张量乘积，减少44%提取操作。
### 3. DyREM专用加速器架构
非零态检测器带提前终止逻辑，分层Mitigation Core阵列；片上4KB FP16缓存存储下采样矩阵，三级乘法流水线并行计算。
### 4. 片上原位张量乘计算
全程片内生成缓解矩阵，消除海量片外矩阵读写，彻底解决带宽瓶颈。

## 实验分析
1. 仿真硬件：Xilinx U50 FPGA 300MHz，测试VQE/QAOA/DJ量子算法，对比Mthree/IBU/QuFEM/SpREM。
2. 延迟吞吐：几何平均提速9.6~2000倍，50比特DJ仅0.083s，吞吐量最高5.31M态/秒。
3. 存储带宽：复杂度线性增长，50比特仅25.4KB；SpREM30比特需9.1TB，DyREM数据传输量指数级降低。
4. 保真度：相比四类基线提升1.03~1.15倍，兼顾比特串扰与动态分组适配。
5. 扩展性：比特规模提升无存储溢出，远超依赖片外方案上限。

## 研究启发
1. 张量误差缓解无需完整全局矩阵，结合动态测量比特做矩阵下采样可大幅削减计算存储开销。
2. 量子测量概率天然稀疏是核心优化抓手，仅计算非零态能把指数复杂度降为线性。
3. 静态分组架构无法适配动态线路，硬件必须支持实时分组重构才能兼顾精度与通用性。
4. 专用片上加速器原位生成缓解矩阵，可彻底消除片外存储带宽瓶颈。
5. 利用态相似度复用张量中间结果，是低功耗嵌入式量子加速的关键冗余消除手段。