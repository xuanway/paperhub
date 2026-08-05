---
title: "AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "dnn-accelerator"
  - "merkle-tree"
  - "integrity-authentication"
  - "memory-security"
  - "design-space-exploration"
---

# AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132968">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132968</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 深度神经网络，加速器，批量矩阵乘法，框架 </p>
</div>

---

## 研究概要
本文提出AutoSkewBMT自动化工具链，面向FPGA DNN加速器优化Bonsai默克尔树(BMT)完整性认证。依托哈夫曼类设计空间探索，依据DNN瓦片访问权重倾斜BMT，提升高频计数器校验效率。AlexNet等主流网络实测哈希操作最高削减23%，相比GuardNN、TNPU性能分别提升32%、7%，硬件开销仅小幅增加。

## 背景和动机
1. 边缘FPGA DNN加速器依赖片外DRAM存储特征图/权重，易遭受篡改、重放等内存完整性攻击，需AES+BMT安全防护。
2. 标准均衡BMT读写校验需遍历整条树链，DNN瓦片批量访问带来海量计数器更新，哈希运算开销巨大，严重拖慢推理吞吐。
3. DNN内存访问具备固定瓦片局部性，读写计数器访问频率差异显著，但现有均衡BMT未利用该特性，高频节点校验路径过长。
4. 现有倾斜树方案FAX面向通用CPU，未适配DNN瓦片分块、分层缓存架构，无法自动生成加速器专属BMT配置。
5. GuardNN、TNPU等DNN安全加速器依赖第三方TE或软件调度，完整性校验附加延迟高，缺少独立轻量化BMT优化方案。

## 相关工作
1. 通用BMT硬件：均衡树形结构，读写均完整遍历至根节点，无访问频率感知，DNN场景开销爆炸。
2. FAST倾斜默克尔树：基于CPU程序轨迹离线调树，不支持DNN瓦片访问建模，无分层BMT缓存协同优化。
3. GuardNN/TNPU安全NPU：采用无版本号完整性机制，依赖主机TE，软件调度引入大量额外延迟。
4. ARES/HERMES硬件BMT引擎：仅优化哈希并行流水线，未从树形结构层面降低校验总运算量。
5. Chiron/Occlumency：依托SGX第三方TE保护加速器，软硬件耦合度高，定制灵活性差。

## 本文解决方案
### 1 计数器访问模式生成器
输入网络尺寸、滤波器、全局缓冲区、瓦片参数，自动推导DRAM数据地址映射的加密计数器读写序列，无需仿真采集访问轨迹。
### 2 加权设计空间生成机制
区分读写代价：读权重为1、写权重设M+1（写需串行全树更新），结合瓦片粒度计算每个计数器综合访问权重。
### 3 哈夫曼启发式BMT倾斜探索
采用优先队列将高权重高频计数器向树根靠拢，缩短校验/更新路径；按每层节点占比分配分层BMT缓存容量。
### 4 独立安全硬件模块架构
解耦加速器计算单元与安全模块，集成AES加密、HMAC、计数器缓存、分层BMT缓存，兼容块/瓦片两种完整性粒度。
### 5 预编译静态优化机制
针对固定DNN与加速器参数离线生成最优倾斜BMT，推理阶段无运行时重构开销，安全强度与标准BMT完全一致。

## 实验分析
1. 实验平台：Xilinx U200 FPGA，5层8叉BMT，AES-128+HMAC-SHA256基线，测试AlexNet/VGG16/VGG19/DenseNet/ShuffleNet。
2. 哈希开销：AlexNet哈希运算减少23%，VGG系列降低10%~13.7%，写密集网络收益显著。
3. 推理性能：相较均衡BMT平均提速8%，超GuardNN最高32%、超TNPU最高7%；DenseNet最坏校验流量下降63%。
4. 硬件开销：倾斜BMT引擎LUT仅增加3%，芯片功耗上升不足2%，BRAM资源无额外占用。
5. 负载特征：写操作是BMT核心瓶颈，瓦片粒度、网络计数器总量直接决定倾斜优化收益上限。

## 研究启发
1. DNN加速器内存访问存在强局部性，基于读写代价加权倾斜完整性树，是降低哈希计算的低成本硬件优化思路。
2. 完整性保护瓶颈不在哈希硬件流水线，而在树形校验路径长度，结构优化收益高于单纯并行哈希单元。
3. 面向特定负载静态预优化安全架构，相比运行时动态重构，硬件开销更低、推理延迟更稳定。
4. 分层BMT缓存需配合倾斜树形联合分配，高频节点靠近树根可充分利用缓存截断校验链。
5. 脱离主机TE、独立BMT安全模块可大幅降低软件调度开销，更适配边缘资源受限FPGA推理设备。


## 相关资源

- DNN 加速器建模工具：
  - Timeloop：[https://github.com/NVlabs/timeloop](https://github.com/NVlabs/timeloop)
  - MAESTRO：[https://github.com/maestro-project/maestro](https://github.com/maestro-project/maestro)
