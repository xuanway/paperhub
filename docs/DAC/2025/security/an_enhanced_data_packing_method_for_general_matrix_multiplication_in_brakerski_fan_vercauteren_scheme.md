---
title: "An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "fully-homomorphic-encryption"
  - "bfv-scheme"
  - "general-matrix-multiplication"
  - "fpga-accelerator"
  - "polynomial-encoding"
---

# An Enhanced Data Packing Method for General Matrix Multiplication in Brakerski/Fan-Vercauteren Scheme

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC4: Embedded and Cross-Layer Security</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132703">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132703</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 全同态加密，现场可编程门阵列，矩阵乘法</p>
</div>

---

## 研究概要
本文面向BFV同态加密下GEMM计算瓶颈，提出增强多项式打包方案，适配CNN卷积/全连接层，搭配FPGA专用硬件与异构调度。该方案充分利用多项式系数空间、分块处理大矩阵，U250平台实测MNIST、CIFAR推理相较SOTA分别提速4.22×、3.99×，同时提升模型推理精度、缩减密文存储体积。

## 背景和动机
1. FHE加密神经网络依赖大量GEMM运算，传统打包方式多项式利用率低，旋转、模乘操作繁多，计算延迟与噪声堆积问题严重。
2. 密文多项式阶数高、数据膨胀显著，主机-FPGA间PCIe传输带宽成为关键性能瓶颈，现有方案带宽开销巨大。
3. BFV原生不支持ReLU等非线性激活，主流仅用平方近似，带来明显推理精度损失。
4. CPU/GPU同态方案模运算适配差，现有FPGA加速器未优化矩阵批量打包，大矩阵分块策略缺失，扩展性弱。
5. 缺少主机CPU与FPGA协同流水线调度，加密、矩阵计算、解密任务串行，硬件并行资源无法充分释放。

## 相关工作
1. CPU同态推理框架CryptoNets、Lola：软件串行执行，GEMM开销极高，实时推理能力不足。
2. GPU加速TensorF：擅长张量运算，但未针对BF大数模乘定制优化，同态乘法延迟居高不下。
3. FPGA同态加速器Cheetah：依靠权重复制减少旋转，大网络内存带宽压力大，扩展性受限。
4. FxHENN FPGA框架逐像素卷积计算，数据复用差、存储开销极高，未设计矩阵打包优化。
5. coxHE等CKKS硬件：多项式打包策略简单，单多项式承载矩阵数据量少，批量计算效率低。

## 本文解决方案
### 1 分层多项式打包算法
向量内积采用正反系数配对；小矩阵整多项式封装多行列，大矩阵按多项式阶分块拆分，仅保留有效内积系数，大幅减少加密与旋转次数。
### 2 CNN层适配打包扩展
卷积、全连接层动态匹配打包粒度，按通道优先封装权重，区分密文-明文、密文-密文两种计算场景优化打包逻辑。
### 3 RNS基BFV专用FPGA加速器
模块化设计MAU/MMU/CBU计算单元，搭配分级BRAM/URAM存储NTT旋转因子、重线性密钥，支持流水线NTT/模变换运算。
### 4 异构协同推理调度
主机负责打包、加解密、ReLU激活，FPGA卸载核心同态矩阵乘法，异步流水线掩盖PCIe传输延迟，平衡软硬件负载。
### 5 精度优化网络改造
8bit量化模型，用ReLU替代平方激活并加入BN层，在不破坏BFV运算约束前提下提升分类准确率。

## 实验分析
1. 实验平台：Xilinx Alveo U250 FPGA，Vivado综合，BFV多项式阶N=4096，基准含CryptoNets、FxHENN、coxHE。
2. 矩阵性能：各类矩阵规模相较coxHE提速2.37~5.11倍，8192大矩阵相较SEAL软件提速约1.89万倍。
3. 推理指标：密文输入+明文权重MNIST仅0.045s、CIFAR 13.53s，分别较FxHENN提速4.22×、3.99×。
4. 存储开销：CIFAR模型体积相较FxHENN降低93.14%，打包压缩效果显著。
5. 精度与资源：MNIST准确率99.11%、CIFAR 78.99%；FPGA主要LUT占用98.93%，DSP/BRAM资源占用可控。

## 研究启发
1. BFV同态GEMM核心优化方向是提升多项式系数利用率，高效打包可减少加密、旋转等高开销操作。
2. 密文与明文权重场景性能差距明显，隐私需求可分级设计，无需全部密文运算以降低时延。
3. FHE加速器不能只优化计算单元，必须配套分层存储与主机-FPGA流水线调度缓解传输瓶颈。
4. 打包算法需自适应矩阵尺寸，小矩阵整存、大矩阵分块是兼顾效率与硬件约束的通用思路。
5. 同态推理精度与加密开销存在权衡，在BFV允许范围内替换激活函数可显著提升模型分类效果。
