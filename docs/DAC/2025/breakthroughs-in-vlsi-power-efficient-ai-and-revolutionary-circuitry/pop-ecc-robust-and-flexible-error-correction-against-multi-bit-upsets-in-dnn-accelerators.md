---
title: "PoP-ECC: Robust and Flexible Error Correction against Multi-Bit Upsets in DNN Accelerators"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PoP-ECC: Robust and Flexible Error Correction against Multi-Bit Upsets in DNN Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133373">https://ieeexplore.ieee.org/document/11133373</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 可靠性，纠错码，静态随机存取存储器，深度神经网络</p>
</div>

---

## 研究概要
本文提出两层纠错码PoP-ECC，并结合逐通道量化形成Q+PoP方案，面向DNN加速器SRAM多比特翻转(MBU)容错。通过虚拟奇偶VP与奇偶之PP两级编码，无需存储VP即可校正相邻双错误DAE。测试相较VAPI最高耐受31.62倍DAE比例，编解码时延、面积功耗开销极低。

## 背景和动机
1. 自动驾驶、航天安全型DNN芯片片上SRAM占比极高，先进工艺粒子撞击极易引发多比特相邻翻转DAE，权重错误会大幅降低推理精度。
2. 传统单比特ECC、权重空值、VAPI等方案对MBU校正能力弱，高错误率下模型精度断崖下跌。
3. 常规ECC冗余位存储面积开销大；层量化精度损失严重，逐通道量化可在低比特下维持精度，未与强ECC结合。
4. 现有两级ECC直接保护原始数据，冗余开销高，缺少轻量化虚拟奇偶分层纠错架构。

## 相关工作
1. 基础二进制ECC(汉明/BCH)、RS码：仅针对单/少量随机错，对成片相邻DAE校正效率低，冗余比特多。
2. Weight Nulling：1位奇偶仅检错，双比特错无法识别，错误权重直接置零，高误码率精度崩溃。
3. VAPI值感知奇偶：利用权重闲置比特存校验，仅支持块内1组双错，DAE耐受上限低、量化精度损失大。
4. LOT/RATT两层ECC：直接对原始数据分层编码，存储冗余开销大，未适配DNN权重量化特性。

## 本文解决方案
### 1 两级PoP-ECC纠错架构
第一层为虚拟奇偶VP：由6比特权重高5位生成4bit VP，可覆盖全部单/双位错误，VP不存入内存；第二层RS编码PP保护VP，仅存储权重+PP，大幅缩减冗余存储。
### 2 Q+PoP量化容错协同方案
采用逐通道6比特量化，相比层量化平均精度损失仅1.02%，释放存储空间用于存放PP校验位，平衡存储开销与推理精度。
### 3 定制编解码流水线
编码仅单层异或生成VP，再RS生成PP；解码先重生成VP，通过PP修复受损VP，再用VP还原出错权重，最低位噪声忽略不影响精度。
### 4 可配置纠错粒度
可调整PP数量适配不同误码场景，针对DAE主导的先进工艺做定制化VP生成矩阵，区分关键高位与容错最低位。

## 实验分析
1. 测试负载：ResNet50、MobileNet V2、RegNet-X8GF，对比Weight Nulling、VAPI两套主流DNN容错方案。
2. 精度表现：无错时Q+PoP平均精度仅降1.02%，远优于VAPI的7.44%精度损失。
3. 容错能力：相较VAPI可承受最高3.16倍单比特误码、最高31.62倍DAE比例，误码率至3e-3精度降幅仍低于0.1%。
4. 硬件开销：28nm工艺编码器0.65ns、解码器1.56ns；编码器面积92μm²、解码器1760μm²，功耗合计1.28mW，开销可忽略。
5. 消融对比：逐通道量化是维持基线精度核心，两级VP-PP分层是提升MBU耐受的关键。

## 研究启发
1. DNN权重最低比特噪声对精度影响极小，可针对性简化校验电路，仅保护高权重关键比特。
2. 不存储中间虚拟校验值的分层ECC能大幅降低存储冗余，适配SRAM面积受限AI加速器。
3. 量化与纠错码必须协同设计，逐通道量化比层量化能为ECC预留空间同时控制精度损耗。
4. 面向先进工艺的容错方案需重点优化相邻多比特DAE校正能力，传统单比特ECC已无法满足可靠性需求。
5. 校验中间层采用短符号RS码，硬件编解码电路面积与时延开销远低于长码方案。
