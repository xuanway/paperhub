---
title: "RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "control-flow-attestation"
  - "mcu"
  - "arm"
  - "embedded-security"
---

# RAP-Track: Efficient Control Flow Attestation via Parallel Tracking in Commodity MCUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC4: Embedded and Cross-Layer Security</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132094">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132094</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 控制流证明，微控制器，并行控制流，低开销运行时证明 </p>
</div>

---

## 研究概要
本文提出RAP-Track，面向商用ARM Cortex-M MCU的并行控制流认证方案。复用片上MTB、DWT追踪硬件与TrustZone，离线静态划分代码区、插入跳转跳板，仅记录非确定分支。相比主流TEE插桩方案运行开销大幅降低，日志体积可控，可抵御ROP/JOP代码复用攻击，原型开源可部署。

## 背景和动机
1. 传统远程认证仅校验静态固件，无法检测运行时ROP/JOP控制流篡改，控制流认证(CFA)可提供执行轨迹可信证据。
2. 主流TEE插桩式CFA需频繁安全/非安全世界上下文切换，分支插桩引入巨大运行时延，不适合资源受限MCU。
3. 原生MTB硬件追踪会记录全部分支，产生海量控制流日志，存储、传输开销极高，无法直接用于CFA。
4. 定制硬件CFA方案需重新流片，无法在现有商用IoT MCU落地；Intel PT追踪仅高端CPU支持，不适用于嵌入式。
5. 缺少基于ARM标准片上追踪单元、兼顾低运行开销与精简日志的通用CFA实现方案。

## 相关工作
1. 定制硬件CFA：新增专用追踪模块，安全高效但无法复用现有商用MCU，部署成本高。
2. TEE插桩类CFA（TRACES等）：所有分支插入安全世界日志调用，频繁上下文切换，性能损耗可达千倍。
3. Intel PT追踪CFA：仅适配x86高端处理器，无ARM嵌入式适配能力，日志冗余问题未解决。
4. LAHEL基于PTM追踪：依赖片外调试端口，生产设备常关闭调试接口，实用性差。
5. MTB用于CFI：仅本地实时阻断违规流，不生成可远程校验的完整认证日志，无法用于CFA场景。

## 本文解决方案
### 1 软硬件协同整体架构
基于Cortex-M33 TrustZone可信根，安全世界部署CFA引擎，复用MTB并行追踪、DWT地址断点自动启停追踪，无需每条分支触发安全调用。
### 2 离线静态代码分区策略
编译后静态分析程序，划分为MTB追踪区(MTBAR)、无追踪区(MTBDR)；确定/固定跳转留在MTBDR，间接/可变分支移入MTBAR。
### 3 分支跳板插桩机制
原确定跳转替换为直达MTBAR的直接跳板，在追踪区执行原始分支指令；区分if、前后向循环设计不同跳板，仅记录必要跳转轨迹。
### 4 DWT自动启停追踪
两组DWT比较器绑定两区地址范围，PC落入MTBAR自动开启MT，进入MTBDR自动关闭，无需软件干预启停。
### 5 日志分段与安全上报
MTB缓冲区设置水印阈值，满时安全世界生成分段认证报告；执行完毕用TZ私钥签名日志、固件哈希与挑战值发送给验证方。

## 实验分析
1. 实验平台：V2M-MPS2 Cortex-M33开发板，超声波、盖革计数器、BEEBs嵌入式基准共7类应用，对比TRACES与原生MTB基线。
2. 运行开销：RAP-Track仅增加2%~62%周期，TRACES最高达1309%，并行硬件追踪消除大量上下文切换损耗。
3. 日志体积：远高于原生MTB但与TRACES持平，多数场景4KB片上缓存即可容纳，无需频繁分段上报。
4. 代码开销：跳板指令带来小幅程序体积增长，在MCU存储约束下可接受。
5. 安全验证：固件哈希锁定内存，间接分支全部记录，攻击者无法篡改控制流且无法伪造签名日志。

## 研究启发
1. ARM商用MCU自带MTB/DWT追踪硬件可低成本实现CFA，无需定制芯片，适合大规模IoT设备部署。
2. 区分确定/非确定分支是精简日志核心，静态代码分区可大幅降低存储与传输压力。
3. 利用DWT硬件自动启停追踪，能完全消除每条分支的安全域切换开销，从根源优化CFA性能。
4. CFI与CFA目标存在本质差异，本地阻断方案不能直接复用为远程轨迹认证方案。
5. 嵌入式安全设计应充分复用厂商标准硬件扩展，避免依赖高开销软件插桩或定制硬件。