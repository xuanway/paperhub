---
title: "ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-accelerator"
  - "fully-homomorphic-encryption"
  - "bootstrapping"
  - "ckks"
---

# ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2506.08461">https://arxiv.org/abs/2506.08461</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>加速器，可自举参数，客户端侧，全同态加密 </p>
</div>

---

## 研究概要
本文面向客户端CKKS同态加密，提出资源高效加速器ABC-FHE，支持自举大参数。设计可重构流式架构，融合统一在线旋转因子生成、片上PRNG与优化蒙哥马利乘法，大幅削减片外访存。28nm实测面积28.638mm²、功耗5.654W，加解密相比CPU提速千倍，超越现有客户端SOTA加速器。

## 背景和动机
1. CKKS全同态加密计算开销是明文万倍，云端服务端加速方案成熟，但客户端编码/加解密成为整体时延瓶颈，占总执行69.4%。
2. 现有客户端FHE加速器仅支持N≤2¹³小多项式，无法满足自举所需2¹⁴~2¹⁶高阶参数，难以支撑多轮密文运算。
3. 传统非流式架构批量输出数据超出客户端DRAM带宽，频繁外部访存引入巨大延迟，旋转因子、随机数全靠片外读取加剧带宽压力。
4. 加解密算子负载失衡，加密端IFFT+NTT运算量约为解密十倍，分离式FFT/NTT硬件面积利用率极低。
5. 通用蒙哥马利乘法器硬件开销大，现有流水线NTT采用radix-2结构，乘法单元冗余，芯片面积浪费严重。

## 相关工作
1. 服务端FHE加速器：聚焦云端大批量同态运算，不适配客户端编码、解密混合浮点FF+整数NTT负载。
2. 现有客户端ASIC/FHE加速器：参数上限低，无流式流水线，旋转因子、随机数预存于片外，带宽瓶颈突出。
3. 独立NT/FFT硬件：两套分离计算单元，硬件复用率差，未针对FHE模数特征优化乘法器。
4. 传统流水线NTT：采用radix-2布局，旋转因子调度冗余，乘法器数量多，芯片面积开销高。
5. RNS分层FHE方案：仅算法层面优化，无配套客户端硬件架构，无法解决访存与算力瓶颈。

## 本文解决方案
### 1 双可重构流式核心整体架构
搭载两组可重构流式处理核心RSC，支持三种调度模式：双加密、双解密、加解密并行；全局双缓冲SRAM流式吞吐，消除DRAM带宽阻塞，适配2¹⁶高阶自举参数。
### 2 可重构傅里叶引擎RFE
单硬件复用实现FP55浮点FFT与44位整数NTT，采用radix-2ⁿ流水线布局；旋转因子调度合并预处理运算，乘法单元数量降低29.7%。
### 3 NTT友好型优化蒙哥马利乘法
基于特制NTT模数简化求逆运算，将三重乘法转化移位加法，相比标准蒙哥马利面积缩减41.2%，优于Barrett算法67.7%。
### 4 片上实时数据生成单元
统一在线旋转因子生成器OTF TF Gen、片上PRNG，无需存储海量预计算参数，片上存储开销降低99.9%，彻底消除随机数/因子片外读取。
### 5 负载感知调度与MSE模块
模块化流引擎MSE统一处理RNS/CRT与逐元素运算；针对加解密算力不均衡特性动态分配双核心算力，提升硬件利用率。

## 实验分析
1. 实验配置：28nm工艺600MHz综合，880KB全局SRAM，多项式阶2¹⁶、24层CKKS参数，基线CPU与多款客户端ASIC加速器。
2. 时延加速：编码加密较CPU提速1112倍，对比SOTA客户端加速器提速214倍；解码解密CPU提速963倍，SOTA提升82倍。
3. 硬件开销：总面积28.638mm²，总功耗5.654W；RFE全套优化后核心面积降低31%。
4. 访存收益：片上实时生成方案相较外部读取延迟下降8.2~9.3倍，8路流水线为带宽最优配置。
5. 参数扩展性：支持2¹³~2¹⁶全系列自举参数，7nm工艺可缩至0.9mm²、功耗2.1W，适配终端设备。

## 研究启发
1. FHE系统优化不能只关注云端同态运算，客户端编码、解密是完整隐私推理关键瓶颈，需专用流式硬件。
2. 客户端存储带宽受限，必须通过片上实时生成随机数、旋转因子减少DRAM访问，而非单纯提升并行度。
3 FFT与NTT硬件高度同源，可重构共享计算单元能大幅削减芯片面积，适配加解密负载不均衡场景。
4 面向FHE定制模数与简化蒙哥马利算法，是降低模乘硬件成本的低成本核心优化手段。
5 流式流水线架构匹配客户端串行输入输出特征，盲目增加并行通道会触发带宽瓶颈，存在最优并行上限。