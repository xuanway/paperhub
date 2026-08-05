---
title: "FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "trustzone"
  - "fpga"
  - "tee"
  - "soc-fpga"
  - "heterogeneous-computing"
---

# FPGA-TrustZone: Security Extension of TrustZone to FPGA for SoC-FPGA Heterogeneous Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132548">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132548</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 可信执行环境，片上系统FPGA，ARM信任区，安全扩展</p>
</div>


---


## 研究概要
本文提出FPGA-TrustZone安全框架，将ARM TrustZone可信执行环境扩展至SoC-FPGA异构平台。设计FPGA安全监视器、CPU侧扩展监视器、BRAM保护三大核心组件，实现FPGA区域隔离、可信启动、AXI传输加密与BRAM存储加密。ZCU102板实测硬件资源占用低于9%，运算开销18%~23%，可抵御四类跨域攻击。

## 背景和动机
1. ARM TrustZone仅保护CPU，Zynq等SoC-FPGA架构中FPGA逻辑、BRAM、AXI总线存在独立攻击面，缺乏配套TEE隔离方案。
2. 现有FPGA可信方案存在短板：部分不支持FPGA安全启动，部分跨CPU-FPGA通信开销巨大，缺少BRAM硬件加密防护。
3. SoC-FPGA存在四类典型威胁：FPGA内部恶意IP窃取、被攻破FPGA攻击CPU、恶意CPU入侵FPGA、AXI总线窃听篡改。
4. 多FPGA业务并行场景下，IP/存储资源无细粒度隔离，不同任务敏感数据易相互泄露。
5. 现有防护框架硬件开销过高，难以适配资源受限嵌入式FPGA开发板。

## 相关工作
1. RCTEE：支持云端FPGA动态IP部署，但缺少FPGA可信启动与片上BRAM加密机制。
2. SGX-FPGA：打通SGX与FPGA安全通路，未实现FPGA内部多区域隔离，无总线事务校验机制。
3. Ambassy：构建FPGA次级TEE，但未设计安全比特流加载流程，冷启动攻击防护薄弱。
4. TEEOD：为每个应用分配独立FPGA处理器，资源与通信开销极大，工程落地困难。
5. TPM/PUF-TrustZone：仅CPU侧安全增强，无FPGA侧隔离、BRAM加密、非法事务拦截能力。

## 本文解决方案
### 1 三层协同整体架构
CPU侧SM-Extension扩展TrustZone监视器，FPGA端FPGA-SM作为核心管控单元，搭配BRAM Protector存储加密模块，基于AXI AxPROT/AxRegion实现安全域划分。
### 2 FPGA-SM三大核心能力
可信启动：双层AES-GCM加密比特流，芯片PUF生成根密钥，防止镜像篡改窃取；资源隔离：基于DeviceID建立区域访问白名单，拦截跨域非法事务；安全传输：AXI事务加解密，非法访问返回错误或重定向空地址。
### 3 CPU侧SM-Extension
对接原生TrustZone安全世界，提供FPGA区域全生命周期API，完成CPU-FPGA事务加解密、安全指令转发与动态配置。
### 4 BRAM Protector存储防护
融合仲裁+环振荡器PUF生成AES-CBC初始向量，BRAM读写可配置加密开关，密钥隔离在安全监视器，上层区域无法获取。
### 5 全局PM监控单元
实时监测AXI与区域访问行为，捕获非法操作触发中断上报，形成全链路安全数据流管控。

## 实验分析
1. 实验平台：Xilinx ZCU102 MPSoC，对比SGX-FPGA、TPM-TrustZone等主流架构。
2. 硬件资源：PUF仅占0.04%LUT，BRAM加密模块2.47%，FPGA-SM为1.25%，整套框架总资源占用<9%。
3. 时序开销：AES-CBC单轮14.5周期，向量运算开销22.28%、矩阵乘18.59%，并行计算性能损耗更低。
4. 安全对比：独有FPGA可信启动、BRAM加密、非法事务投毒、PMU中断检测能力，可抵御全部四类异构攻击。
5. 功能验证：多隔离区域并发运行无信息泄露，比特流、BRAM、总线数据均密文传输，冷启动攻击失效。

## 研究启发
1. 传统CPU TEE无法覆盖FPGA攻击面，异构SoC需要双向联动的扩展可信架构，兼顾CPU与FPGA安全域。
2. FPGA防护必须覆盖启动、运行、存储、总线全链路，仅逻辑隔离不足以抵御比特流窃取与BRAM数据泄露。
3. 基于AXI原生AxPROT、AxRegion扩展隔离逻辑，无需大幅修改总线，轻量化实现多任务资源分区。
4. PUF是FPGA可信启动与存储加密理想密钥源，可避免硬编码密钥泄露，兼顾安全性与硬件开销。
5. 安全框架需分层开销设计，基础计算模块控制20%以内性能损耗，才能适配边缘嵌入式FPGA业务。



### 相关资源

- **OP-TEE**：[https://github.com/OP-TEE](https://github.com/OP-TEE)
- **ARM TrustZone 技术参考**：[https://developer.arm.com/ip-products/security-ip/trustzone](https://developer.arm.com/ip-products/security-ip/trustzone)
- **Xilinx Zynq 安全**：[https://www.xilinx.com/products/technology/security.html](https://www.xilinx.com/products/technology/security.html)
