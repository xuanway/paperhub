---
title: "ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "post-quantum-cryptography"
  - "computing-in-memory"
  - "analog-computing"
  - "mceliece"
  - "qc-mdpc"
---

# ACIM-QMM: Efficient Analog Computing-in-Memory Accelerator for QC-MDPC McEliece Cryptosystem

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133068">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133068</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 阻变存储器，电路设计，模拟存内计算，QC-MDPC McEliece</p>
</div>


---

## 研究概要
本文提出基于ReRAM的模拟存内加速器ACIM-QMM，面向QC-MDPC McEliece后量子密码，解决模拟电路难以GF(2)矩阵运算难题。设计分块矩阵数据流映射与误差补偿电路，支持80~256位安全等级。相较SOTA硬件提速31.4~288.1倍，256位场景面积效率最高3.12倍、能效提升20.32倍。

## 背景和动机
1. 量子计算威胁传统密码，QC-MDPC McEliece作为NIST后量子候选，密钥更小，但GF(2)大规模矩阵运算时延、硬件开销极高。
2. 现有QMM实现基于冯诺依曼数字架构，频繁数据搬移拖慢加密速度，难以适配海量加密业务。
3. 数字存内加速器需大量数模转换，开销大；模拟CIM天然并行矩阵乘，但无法直接实现模2运算，缺少适配方案。
4. ReRAM阵列存在器件偏差、线路电阻、噪声等非理想效应，模拟计算误差累积会导致密码运算失效，缺少补偿机制。
5. 现有PQC存内方案多面向格基算法，无专门适配码基QMM的模拟存内架构。

## 相关工作
1. McEliece数字/FPGA硬件：仅优化数字流水线，受访存瓶颈限制，高安全等级下延迟、面积开销爆炸。
2. 数字存内PQC加速器：基于MRAM/ReRAM数字计算，频繁DAC/ADC转换，并行度低，不利用模拟阵列单步矩阵计算优势。
3. 通用模拟存内计算：擅长连续值运算，无GF(2)模2矩阵分块映射逻辑，无法用于码基密码。
4. ReRAM非理想特性研究：仅分析误差来源，未结合密码矩阵运算设计硬件补偿电路。
5. 其他后量子密码硬件：面向Kyber、Dilithium格基方案，矩阵维度、运算逻辑与QMM不兼容，无法复用。

## 本文解决方案
### 1 GF(2)分块矩阵数据流映射方案
将校验矩阵拆分为三角+置换子块，推导分块求逆、分乘算子；把大矩阵分解适配有限尺寸ReRAM交叉阵列，让模拟电路完成模2向量矩阵乘。
### 2 双核心模拟存内模块架构
设计BlockMat-Inv求逆模块、BlockMat-Mul乘法模块，采用2T1 ReRAM阵列，通过运放构造等效0/1电导矩阵，原生实现GF(2)运算。
### 3 模块化归约模拟电路
集成ADC/运放/开关阵列，将模拟电流输出转化模2数字结果，完成密码最后取模操作。
### 4 多维度模拟误差补偿机制
可调补偿电阻、叠加补偿电压，抵消线路电阻、器件偏差、噪声带来的计算偏差，将相对误差控制在千分之一以内。
### 5 全安全等级兼容设计
架构适配80/128/256位三类安全参数，完整支持QMM密钥生成与加密全流程。

## 实验分析
1. 仿真环境：TSMC 180nm/65nm工艺，Cadence仿真，注入线阻、器件偏差、噪声等非理想干扰。
2. 计算精度：误差补偿后Inv/Mul模块相对误差降至10⁻³以下，不影响密码运算正确性。
3. 速度对比：对比主流FPGA/数字PQC硬件，提速31.4~288.1倍；相较A800 GPU最高提速300万倍。
4. 硬件指标：256位安全等级下，面积效率最高为同类PQC硬件3.12倍，能效提升20.32倍。
5. 开销拆解：运算放大器占功耗75%，DAC/ADC面积占比高，是后续优化靶点。

## 研究启发
1. 模拟存内计算适配码基PQC核心难点是GF(2)模运算，分块三角矩阵分解是突破路径。
2. ReRAM非理想效应不可忽略，需在模拟运算链路内置硬件补偿，否则累积误差破坏密码输出。
3. 相较数字CIM，模拟阵列单步并行矩阵乘能大幅消除访存与数模转换开销，高安全等级优势更显著。
4. 码基、格基后量子密码矩阵逻辑差异巨大，专用存内架构性能远优于通用PIM设计。
5. 模拟加速器功耗瓶颈集中在运算放大器，降低运放规模/电压是进一步提升能效的关键方向。
