---
title: "zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "zero-knowledge-proof"
  - "matrix-multiplication"
  - "zksnark"
  - "verifiable-computing"
---

# zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.12217">https://arxiv.org/abs/2504.12217</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/UCF-Lou-Lab-PET/zkformer">https://github.com/UCF-Lou-Lab-PET/zkformer</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 隐私保护与可验证计算，零知识证明，机器学习</p>
</div>

---

## 研究概要
本文提出zkVC高效零知识证明框架，面向矩阵乘法与Transformer推理优化。设计CRPC约束缩减电路将复杂度从O(n³)降至O(n)，搭配PS前缀求和机制进一步削减变量；对SoftMax/GELU做多项式近似。矩阵证明速度提升12倍，ViT等Transformer端到端提速超15倍，支持无可信设置Spartan后端。

## 背景和动机
1. 云ML推理场景下传统zk-SNARK验证矩阵乘法开销极大，中等规模矩阵证明耗时可达数分钟，无法落地ViT、BERT等大模型。
2. 现有vCNN等优化仅针对卷积，无法通用适配矩阵乘，直接套用会激增中间变量，整体效率下降。
3. 标准R1CS电路每个点积对应多条乘法约束，矩阵乘约束规模呈立方增长，成为ZKP性能瓶颈。
4. Transformer的SoftMax、GELU非线性函数难以用算术电路精确表达，现有近似方案精度与开销失衡。
5. 多数验证ML方案依赖交互证明或可信初始化，客户端部署门槛高，缺少透明无交互通用优化方案。

## 相关工作
1. 卷积专用ZKP优化（vCNN/pvCNN）：将卷积转为多项式乘，但无法通用矩阵运算，泛化性差。
2. 通用可验证ML（VeriML/ZEN/zkML）：仅采用量化等轻量优化，未重构矩阵乘电路，提速幅度有限。
3. 交互式zkCNN：证明速度快，但持续双向通信，客户端在线开销大、证明尺寸臃肿。
4. 基础zk-SNARK（Groth16/Spartan）：原生电路未做矩阵专用化简，点积约束数量爆炸。
5. 同态加密推理：仅保证数据隐私，无法提供计算完整性证明，和ZKP目标不兼容。

## 本文解决方案
### 1 CRPC约束缩减多项式电路
利用中间随机变量Z重构矩阵行列多项式，把a×n × n×b矩阵乘的O(n³)约束降至O(n)，保证完备与可靠，消除冗余乘积项，从根源降低R1CS规模。
### 2 PSQ前缀求和查询机制
将点积分步存储前缀和，消除长加法链带来的大量中间变量，R1CS计算开销降低70%，与CRPC组合实现12倍整体加速。
### 3 非线性函数多项式近似
SoftMax输入平移至负数区间，泰勒展开近似指数；GELU采用低阶多项式拟合，仅少量分解与乘法约束即可高精度复现激活效果。
### 4 混合Transformer验证策略
高分辨率图像用无SoftMax线性注意力加速，短序列层保留SoftMax平衡精度；支持Groth16（轻验证）、Spartan（无可信设置）双后端。
### 5 完整端到端验证流水线
适配ViT视觉、BERT语言两类Transformer，整数量化模型兼容，提供可复用电路转换工具链开源实现。

## 实验分析
1. 测试平台：16核AMD线程撕裂者+RTX3090，基准vCNN/ZEN/zkML，分Groth16、Spartan两套密码后端。
2. 矩阵微基准：同等矩阵规模，zkVC证明耗时仅为vCNN的1/12.5，CRPC单独提速9倍，叠加PSQ再提升30%。
3. Transformer视觉：ImageNet ViT证明时长从万秒级降至3457秒，精度仅损失1.7%；CIFAR-10提速40%、精度降幅<2%。
4. NLP任务：BERT系列相比线性注意力方案提速15%，四类GL任务平均精度仅下降约3%。
5. 方案对比：非交互、常数证明尺寸、无需可信初始化、原生支持矩阵/Transformer，综合指标优于所有现有基线。

## 研究启发
1. ZKP性能瓶颈核心在算术电路约束规模，针对矩阵乘这类高频运算重构多项式表示是最优优化路径。
2. 长累加链会引入大量冗余中间变量，前缀求和结构可低成本缩减R1CS变量数。
3. Transformer推理无需全程SoftMax，长短序列分层混合策略可兼顾证明效率与模型精度。
4. 专用电路优化具备通用性，矩阵优化方案可无缝迁移至视觉、NLP各类Transformer架构。
5. 双密码后端设计更适配多云场景：低延迟需求选Groth16，无可信部署场景选用Spartan透明方案。