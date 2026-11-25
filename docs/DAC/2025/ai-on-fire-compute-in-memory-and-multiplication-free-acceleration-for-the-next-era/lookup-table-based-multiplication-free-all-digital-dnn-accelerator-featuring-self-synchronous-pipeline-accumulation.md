---
title: "Lookup Table-based Multiplication-free All-digital DNN Accelerator Featuring Self-Synchronous Pipeline Accumulation"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Lookup Table-based Multiplication-free All-digital DNN Accelerator Featuring Self-Synchronous Pipeline Accumulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2506.16800">https://arxiv.org/abs/2506.16800</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>近似矩阵乘法，存内计算，卷积神经网络，静态随机存取存储器，二元决策树 </p>
</div>

---

## 研究概要
本文基于MADDNESS无乘近似矩阵乘法，提出全数字自同步流水线DNN存内加速器。采用动态逻辑BDT编码器、双端口10T-SRAM查表单元，无全局时钟、抗PVT偏差。22nm后仿验证，能效174 TOPS/W、面积效率2.01 TOPS/mm²，相较模拟与数字基线分别提升2.5倍、4倍，分类精度无损。

## 背景和动机
1. DNN推理海量MAC运算，乘法器面积、功耗远高于加法器，访存开销大，存内计算(CIM)是主流优化方向。
2. 模拟CIM易受工艺/电压/温度(PVT)波动干扰，需额外校准电路，多比特扩展成本高。
3. 现有全数字MADDNESS加速器采用标准单元LUT，读写能耗高，编码器依赖全局时钟与大量寄存器，功耗居高不下。
4. 同步流水线受最慢路径限制，PVT偏移会显著拉长关键路径，推理时延不稳定。

## 相关工作
1. 模拟MADDNESS加速器：利用时延链完成PQ量化，能效尚可，但面积开销大、PVT敏感，需后制造校准。
2. 标准数字MADDNESS(Stella Nera)：同步BDT编码器、标准单元查表，编码器与LUT能耗显著偏高。
3. 传统模拟CIM：电流/电压完成乘加，精度随PVT劣化，ADC/DAC带来额外功耗面积。
4. 通用数字MAC加速器：依赖大量乘法阵列，无法消除乘法固有能耗瓶颈。

## 本文解决方案
### 1 自同步异步流水线架构
去除全局时钟，四相位握手通信，各计算块按需执行，不受最长路径约束，天然兼容各类PVT工况。
### 2 动态逻辑BDT编码器
双轨动态比较器仅激活必要分支，省去全局时钟与中间寄存器，PQ量化能耗降低95%，完成输入向LUT地址映射。
### 3 双端口10T-SRAM解码器阵列
内置进位保存加法CSA，列级读完成检测RCD电路，无需灵敏放大器；相比标准单元LUT能耗降低66%，预存权重内积查表。
### 4 分层并行计算宏
多串行计算块，Ns并行输入通道、Ndec并行内核，后端波纹加法树汇总多块查表结果适配CNN推理。

## 实验分析
1. 仿真环境：22nm商用工艺HSPICE后仿，测试0.5~1.0V多电压、多工艺角，基准为模拟MADDNESS、Stella Nera。
2. PPA指标：0.5V最优能效174 TOPS/W，面积效率2.01 TOPS/mm²；Ndec=16实现面积与功耗最优平衡。
3. 对比基线：相较模拟方案能效提升2.5倍，数字基线能效提升4倍；CIFAR-10 ResNet9精度维持92.6%无损失。
4. 资源拆解：解码器占94%能耗、50%~80%面积；编码器占40%~70%时延，异步结构大幅压缩最坏延迟。
5. 扩展性：Ndec提升可分摊编码器开销，但过大RCD树增加延迟，推荐Ndec=16折中配置。

## 研究启发
1. MADDNESS无查表架构的性能瓶颈分别在编码器与存储单元，动态电路+专用10T-SRAM可同步降低两者能耗。
2. 自同步异步流水线完美解决数字电路PVT时延波动问题，无需冗余复制延迟校准单元。
3. 并行度Ns/Ndec存在权衡，并行内核越多分摊编码器开销，但会放大读检测电路延迟。
4. 全数字MADDNESS可兼顾精度、鲁棒性与低功耗，优于易漂移模拟存内计算方案。
5. 近似矩阵乘法硬件优化需编码器、存储、流水线三者协同，单一模块优化收益有限。