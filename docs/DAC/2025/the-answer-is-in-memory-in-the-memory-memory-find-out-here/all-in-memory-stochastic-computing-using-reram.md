---
title: "All-in-memory Stochastic Computing using ReRAM"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# All-in-memory Stochastic Computing using ReRAM

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.08340">https://arxiv.org/abs/2504.08340</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>阻变存储器，存内计算，随机计算，随机比特流生成，图像处理 </p>
</div>


---

## 研究概要
本文提出基于ReRAM的全内存随机计算架构All-in-Memory SC，依托ReRAM器件随机性在阵列内完成随机比特流生成、随机运算、二进制转换全流程。设计优化型内存比特流生成算法与侦察逻辑硬件，规避存储-计算数据搬运开销。图像处理测试相较CMOS、ReRAM基线，吞吐分别提升1.39/2.16倍，能耗降低1.15/2.8倍，故障下图像质量仅平均下降5%。

## 背景和动机
1. 传统随机计算(SC)依赖CMOS随机比特流发生器，面积功耗占系统80%，冯诺依曼架构比特流频繁搬运抵消SC低运算开销优势。
2. 现有ReRAM存内随机计算多为混合架构，比特流生成仍依赖片外CMOS，且依赖高损耗ReRAM写随机源，耐久度差。
3. 现有方案难以精准控制比特流相关性，乘法/除法等运算精度受损；ReRAM器件存在阻值漂移、读写故障，传统二进制存算容错差。
4. 缺少端到端纯ReRAM存内SC完整流水线，无法在阵列内完成随机数生成、运算、数模转换闭环。

## 相关工作
1. CMOS随机计算：基于LFSR/Sobol生成比特流，运算简单但生成单元开销巨大，数据搬运能耗高。
2. 混合ReRAM-SC架构：ReRAM仅做运算，随机源外置CMOS，或依靠写切换随机性生成比特流，写损耗严重。
3. SCRAM等存内SC：仅实现部分运算，无法统一控制比特流相关性，无内存内随机转二进制方案。
4. 通用ReRAM存算：采用二进制算术，器件故障会造成高位严重误差，图像任务画质降幅可达47%。

## 本文解决方案
### 1. 端到端纯ReRAM存内SC流水线
阵列划分随机数、比特流、二进制存储分区，全部随机计算三阶段（比特流生成/SC运算/随机转二进制）在内存内完成，无片外比特流传输。
### 2. IMSNG优化型存内比特流生成
基于ReRAM本征真随机数，采用逐位比较逻辑搭配片上锁存器优化，省去大量中间写操作；可自由控制比特流相关性适配加减乘除各类随机运算。
### 3. 侦察逻辑(SL)实现存内随机运算
利用ReRAM并行位运算，将AND/OR/MAJ/MUX/除法电路映射至单次读出操作，替代串行MUX；除法复用锁存器消除中间存储开销。
### 4. 电流累加式随机-二进制转换
利用位线总电流统计1比特数量，搭配片上8位ADC一步完成转换，无需串行计数电路，大幅缩短转换延迟。

## 实验分析
1. 仿真环境：NVMain内存仿真器+45nm CMOS综合，测试图像合成、双线性插值、图像抠图三类SC典型任务。
2. 性能能耗：对比纯CMOS SC吞吐提升1.39倍、能耗降1.15倍；对比二进制ReRAM存算吞吐提升2.16倍、能耗降2.8倍。
3. 精度表现：比特流长度256时各类运算MSE低于0.1%；存在ReRAM故障时图像SSIM平均仅下降5%，二进制存算下降47%。
4. 硬件开销：优化IMSNG相较原始方案减少79%阵列中间写；除法仅增加少量锁存，乘法/加法单次读即可完成。
5. 鲁棒性：SC天然容错特性抵消ReRAM阻值漂移、位翻转，无需额外纠错编码与冗余存储。

## 研究启发
1. 随机计算核心瓶颈不在运算单元，而在比特流生成与跨存储数据搬运，存内全流程一体化是最优优化路径。
2. 复用ReRAM器件本征随机特性替代外置CMOS随机源，可大幅缩减系统面积与功耗，同时规避写损耗缺陷。
3. 侦察逻辑并行位运算高度适配随机计算逐比特独立特性，相比传统串行MUX吞吐提升显著。
4. SC天然容错能力可完美匹配ReRAM非理想器件特性，省去高开销硬件纠错，适合低可靠新兴存储。
5. 内存内电流累加统计是高效随机转二进制方案，避免串行计数器带来的长延迟。
