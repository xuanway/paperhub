---
title: "Measurement-based uncomputation of quantum circuits for modular arithmetic"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Measurement-based uncomputation of quantum circuits for modular arithmetic


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2407.20167">https://arxiv.org/abs/2407.20167</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>模运算，量子计算，电路优化，量子比特，设计自动化 </p>
</div>


---

## 研究概要
本文形式化基于测量的反计算(MBU)技术，面向量子模算术电路优化。对单比特垃圾辅助量子采用X基测量概率化反计算，大幅削减Toffoli门数量。应用于各类模加法电路，Toffoli门降低10%~25%，同时提出区间比较新电路并优化，可用于Shor算法、量子密码分析。

## 背景和动机
1. 量子算术电路运算会产生纠缠垃圾辅助比特，传统共轭反计算需要完整逆电路，Toffoli门开销极高，电路深度大。
2. 模加、模幂是Shor分解、离散对数等核心组件，门数与深度直接影响容错量子机资源消耗。
3. 现有反计算方案必须完整重走计算流程，无法利用测量简化垃圾比特回收，缺少通用可插拔优化理论。
4. 缺少统一框架将测量反计算适配受控、常数型模算术各类衍生电路，区间比较等子电路资源开销未优化。

## 相关工作
1. 传统共轭反计算：执行电路酉逆完全清除垃圾，门开销翻倍，是最通用但成本最高方案。
2. Gidney近似测量反计算：仅给出工程实例，缺少严谨形式化引理，无法通用拓展到模算术体系。
3. VBE/CDKPM/Draper各类量子加法器：仅优化基础加减比较，未配套垃圾比特轻量化反计算。
4. 模乘、模幂优化工作：聚焦主运算门压缩，忽略比较器产生的垃圾比特带来额外Toffoli开销。

## 本文解决方案
### 1 形式化MBU基础引理
针对单比特垃圾函数建立通用测量反计算理论：X基测量50概率直接完成回收，失败仅追加少量单量子门，期望反计算成本减半，提供可插拔标准流程。
### 2 模块化量子算术组件库
统一实现普通/常数/受控加减、比较器，给出各架构Toffoli、CNOT、辅助比特量化开销，支持自由拼接模加法流水线。
### 3 MBU适配各类模加法架构
分别针对VBE、Takahashi、Draper模加推导优化定理，对比较输出垃圾比特应用MBU，期望减少一半比较器门开销。
### 4 新型区间比较量子电路
首次提出判断寄存器数值落在两数之间的子电路，结合MBU实现约16.7% Toffoli门削减，丰富模算术基础单元。

## 实验分析
1. 评估基准：VBE、CDKPM、Gidney、Draper四类模加法架构，统计有无MBU下Toffoli、CNOT、逻辑量子比特数量。
2. 通用模加：MBU降低Toffoli门10%~15%；Takahashi常数模加门数缩减近25%。
3. 衍生电路：受控模加、常数受控模加均获得同等比例资源削减；区间比较电路节省16.7% Toffoli。
4. 组合优势：Gidney加法搭配CDKPM比较器混合架构可进一步平衡量子比特与门开销。
5. 适用范围：优化后的模加可作为底层模块向下传导收益至模乘、模幂、Shor分解电路。

## 研究启发
1. 单比特垃圾辅助比特无需完整逆电路，测量式概率反计算能稳定减半反计算门开销，通用性极强。
2. 模算术电路瓶颈不只在加减主运算，比较器产生的垃圾比特是易被忽略的资源开销点。
3. 量子电路优化需模块化分层设计，基础加减比较单元搭配统一轻量化反计算框架可叠加收益。
4. MBU当前局限于单比特垃圾，多比特场景是重要拓展研究方向。
5. 底层算术子电路门压缩会直接降低上层量子密码分析算法整体硬件需求。
