---
title: "SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "dnn-accelerator"
  - "hardware-software-codesign"
  - "encryption"
  - "memory-protection"
---

# SeDA: Secure and Efficient DNN Accelerators with Hardware/Software Synergy

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2508.18924">https://arxiv.org/abs/2508.18924</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 内存保护，安全深度神经网络加速器，机密性与完整性，深度神经网络 </p>
</div>

---

## 研究概要
本文提出软硬件协同安全DNN加速器SeDA，针对现有加密多AES引擎硬件开销、完整性校验海量片外访存两大痛点。设计带宽感知加密机制抵御SECA攻击，多层MAC完整性方案防御重排列攻击。在服务器、边缘NPU验证，性能开销降低12%以上，硬件面积功耗开销远低于多引擎方案。

## 背景和动机
1. DNN权重/特征存储于不可信片外DRAM，存在模型窃取、数据篡改、重放攻击风险，需加密+完整性双重防护。
2. 传统并行多AES引擎方案满足带宽，但带来巨大面积、功耗开销，边缘NPU资源难以承载。
3. 单AES搭配整块共享OTP易受SECA单元素碰撞攻击，泄露全部明文数据。
4. 现有完整性方案（Merkle树、单层MAC）产生大量安全元数据，频繁片外读写大幅拖慢推理速度。
5. 层级XOR-MAC易遭RePA重排列攻击，篡改块顺序仍能通过校验，存在安全漏洞；且未适配层内分块重叠、跨层分块差异，产生冗余校验。

## 相关工作
1. SGX类可信内存：基于Merkle树、VN版本号，元数据访存开销极高，不适合高吞吐NPU。
2. MGX/TN：采用粗粒度版本号缓存，减少VN访存，但MAC校验带来显著流量开销，未解决RePA漏洞。
3. Securator：层级XOR-MAC降低元数据，但忽略分块重叠产生重复校验，无法抵御块重排列攻击。
4. GuardNN/SEAL：选择性加密、小规模TCB优化，未同时解决加密硬件资源与完整性访存两大核心瓶颈。
5. 传统并行AES加密：多引擎堆叠提升带宽，硬件成本成倍上升，资源受限边缘设备不适用。

## 本文解决方案
### 1 带宽感知B-AES单引擎加密机制
仅使用一套AES核，复用密钥扩展模块生成多组派生OTP；每个128bit子块分配独立一次性掩码，抵御SECA碰撞攻击。仅增加少量异或门，替代多AES引擎，大幅削减面积功耗。
### 2 最优分块optBlk搜索策略
基于DNN层内重叠、跨层分块尺寸差异，搜索无冗余校验的最优保护粒度，避免重复MAC计算，减少元数据生成量。
### 3 三层分级完整性校验架构
optBlk块级MAC记录块/层/特征/偏移完整位置信息，阻断RePA重排列攻击；同层块MAC异或生成层MAC存入片上SR；全局模型MAC用于推理结束终检。
### 4 软硬件协同调度
软件预计算各层optBlk尺寸，硬件密码引擎并行完成OTP生成与推理乘加计算，校验元数据尽量驻留片上，消除绝大多数片外元数据访问。
### 5 双重攻击防御逻辑
针对SECA：派生多OTP隔离子块；针对RePA：MAC绑定完整空间位置信息，块打乱后校验失败。

## 实验分析
1. 仿真环境：SCALE-Sim2加速器仿真、Ramulator2内存仿真，28nm工艺评估硬件，覆盖CNN/推荐/语音等13类模型，对比SGX/MGX基线。
2. 硬件开销：B-AES单引擎随带宽提升面积/功耗增长平缓，同等吞吐下远优于多T-AES并行方案。
3. 内存流量：SGX-64B流量涨幅超30%，MGX-64B约12.5%，Se仅提升0.12%（服务器）、0.03%（边缘）。
4. 推理性能：服务器NPU开销降低12.26%，边缘NPU降低12.29%，相比SGX、MGX提速显著。
5. 安全验证：可完全阻断SECA、RePA两类针对内存防护的新型攻击，保密性与完整性安全强度与多引擎方案持平。

## 研究启发
1. 无需堆叠多AES引擎，复用AES密钥扩展模块派生多OTP，可在极低硬件开销下满足高带宽加密需求。
2. DNN分块重叠是传统完整性方案冗余根源，层感知最优分块可大幅减少MAC计算与元数据传输。
3. 简单层内块异或MAC存在重排列漏洞，MAC必须绑定完整空间位置信息才能抵御RePA攻击。
4. 安全加速器优化需软硬件协同：软件预处理分块策略，硬件做轻量密码单元，双管齐下降低访存开销。
5. 片上SRAM缓存层级MAC是消除完整性校验片外流量的关键，能实现近零推理性能损耗。