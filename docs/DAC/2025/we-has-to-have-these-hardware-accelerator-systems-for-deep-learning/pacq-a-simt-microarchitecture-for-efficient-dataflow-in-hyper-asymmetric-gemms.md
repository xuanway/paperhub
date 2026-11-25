---
title: "PacQ: A SIMT Microarchitecture for Efficient Dataflow in Hyper-asymmetric GEMMs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PacQ: A SIMT Microarchitecture for Efficient Dataflow in Hyper-asymmetric GEMMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.18627">https://arxiv.org/abs/2502.18627</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 通用矩阵乘法，SIMT微架构，数据流，浮点-整数乘法器 </p>
</div>


---

## 研究概要
本文面向LLM仅权重量化提出PacQ SIMT微架构，解决高低精度非对称GEMM低效问题。提出沿n维权重打包与输出驻留数据流，设计并行FP-INT乘法单元；基于V100类张量核改造，相较传统SIMT最高提速1.99倍，EDP降低81.4%，寄存器访问减少54.3%。

## 背景和动机
1. LLM仅权重量化将权重压缩至INT2/4，激活保留FP1，但传统GPU加载后必须解量化，低比特存储收益在L1/寄存器层完全丢失。
2. 主流框架沿k输入维度打包权重，造成激活重复加载、寄存器频繁驱逐，多批量推理算力受限，访存开销巨大。
3. 标准FP乘法器单次仅完成一组FP-INT乘，低权重并行度不足，无法挖掘打包权重的并行计算潜力。
4. 现有混合精度加速器精度差或依赖LUT，缺少软硬件协同的打包数据流+定制乘单元一体化方案。
5. 多批量LLM推理为计算绑定场景，传统解量化流程带来大量额外运算，严重拖慢吞吐。

## 相关工作
1. 通用FP16张量核：仅支持同等精度GEMM，无法原生处理打包低比特权重，必须解量化后计算。
2. FIGNA：FP-INT计算单元，但未优化打包数据流，无并行多INT权重运算能力。
3. Mix-GEMM：二进制分段混合乘，对高低精度差距极大的超非对称矩阵加速效果差。
4 LUT型低比特加速器：依靠查表完成量化乘，存储开销高，不兼容主流PTQ后量化流程。
5. LLM量化算法（GPTQ/AWQ）：仅优化数值精度，不针对SIMT硬件数据流做协同优化。

## 本文解决方案
### 1 n维权重打包+输出驻留数据流
摒弃传统k维打包，沿输出n维度聚合低比特权重，全程保持打包格式流转；采用输出驻留分块策略，激活一次加载可复用全部打包权重，寄存器访问量下降54.3%。
### 2 并行FP-INT定制乘法单元
挖掘INT权重转FP16的指数/尾数固定规律，单周期完成1个FP16激活与4个INT4/8个INT2并行乘法，复用73%标准FP乘法硬件，仅少量加法器拓展。
### 3 适配超非对称GEMM张量核改造
替换原有FP16乘单元为并行FP-INT模块，加倍加法树，内置累加器预计算激活总和，融合权重偏移减法，消除后处理额外指令。
### 4 配套后量化分组优化
量化分组沿n、k二维划分，减少缩放因子反复读取，困惑度与标准一维分组基本持平，不损失模型精度。
### 5 完整PacQ SIMT架构
复用V100 SM通用流水线，仅修改张量核内部计算单元，L2/L1/寄存器分层原生支持打包INT权重传输，无需额外解量化核心。

## 实验分析
1. 实验环境：32nm工艺RTL综合，CACTI缓存建模，Llama2-7B FFN多批量任务，对比V100基线、k维打包方案、Mix-GEMM。
2. 数据流收益：n维打包相较k维打包寄存器访存最高下降54.3%，激活缓存无频繁驱逐。
3. 计算吞吐：并行FP-INT单元能效相较标准FP乘最高提升6.8倍，整体架构提速1.99倍。
4. 能耗指标：INT2权重场景EDP相较传统解量化基线降低81.4%，INT4降低70.4%。
5. 消融对比：加法树复制2份性价比最优；二维量化分组几乎无精度损失且进一步削减缩放读取开销。

## 研究启发
1. 低比特权重打包维度是易被忽视的关键优化点，沿输出n维打包可大幅提升激活数据复用率。
2. 利用整数转浮点的固定指数、尾数模式，可低成本设计并行混合乘法器，显著提升低权重并行度。
3. 超非对称GEMM不能沿用权重驻留数据流，输出驻留更适配FP激活+INT权重的混合计算场景。
4. 硬件微架构改造可兼容现有量化算法，仅微调量化分组即可协同硬件进一步降访存开销。
5. 仅权重量化的瓶颈不在片外存储，而在L1与寄存器层解量化带来的额外访存与计算开销。