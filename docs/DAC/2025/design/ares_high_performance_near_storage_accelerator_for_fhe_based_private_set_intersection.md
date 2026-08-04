---
title: "Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133120">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133120</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>全同态加密，隐私集合求交，近存储加速器，硬件-软件协同设计，惰性重线性化 </p>
</div>


---

## 研究概要
本文软硬件协同设计面向FHE隐私求交的近存加速器Ares，提出延迟重线性化LazyRelin削减冗余运算；硬件划分访存/计算双流水区域，基于SmartSSD近存架构规避PCIe传输瓶颈。实测相比CPU提速47.99倍，超越Poseidon、FAB加速器，能效分别提升7.96倍、10.95倍。

## 背景和动机
1. FHE-PSI依靠多项式求值完成隐私集合匹配，海量数据库带来巨大计算与IO压力，通用CPU处理延迟极高。
2. 通用FPGA FHE加速器面向通用同态运算，未适配PSI专属多项式求值流程，硬件资源利用率极低。
3. 传统加速器挂接主机，海量加密数据库需经PCI频繁搬运，总线带宽成为核心传输瓶颈。
4. 现有PSI协议每次乘法后立即执行重线性化，但PSI运算层级受限，大量Relin属于冗余高开销操作。

## 相关工作
1. 通用FHE FPGA加速器（Poseidon/FAB）：支持自举、全类型NTT，但无PSI专属数据流优化，资源浪费严重。
2. 通用同态计算芯片（ARK/SHARP）：面向通用加密推理，未针对PSI多项式求值做流水线拆分。
3. 软件FHE-PSI协议（APSI）：仅算法层面优化，无硬件加速，无法处理亿级数据集。
4. 传统PCI外挂加速架构：数据库反复经主机中转，PCI带宽限制大规模PSI吞吐。

## 本文解决方案
### 1. LazyRelin软件算法优化
PSI多项式求值中延迟执行重线性化，同层同态乘法全部完成后仅执行一次Relin，大幅削减最耗时的同态重线性操作，不改动原始PSI协议。
### 2. SmartSSD近存NDP硬件架构
计算逻辑集成存储设备内部，数据库直连本地DRAM，绕过主机PCI瓶颈，支持SSD-FPGA点对点高速数据传输。
### 3. 双分区解耦流水线
划分MB访存区（明文乘、轻量同态加）、CB计算区（NTT、同态乘、Relin），PEIR异步FIFO衔接，无气泡流水。
### 4. 专用CB计算单元
集成8基NTT、巴雷特模乘、分层累加模块，配套EV密钥缓存；FSM调度器对接主机下发查询、回送交集结果。

## 实验分析
1. 实验平台：Samsung SmartSSD(KU15P FPGA)，对比Xe CPU、Poseidon/FAB两类通用FHE加速器，覆盖4档规模数据库。
2. 速度表现：相较CPU平均提速47.99倍；对比FAB性能提升1.93倍，对比Poseidon提升1.79倍，数据集越大增益越明显。
3. 资源开销：Ares LUT/BRAM/DSP资源仅为竞品1/2~1/5，硬件利用率显著更高。
4. 能效指标：以EDP为指标，相比Poseidon能效提升7.96倍，相比FAB提升10.95倍。
5. 消融验证：通用加速器叠加LazyRelin收益仅3%，Ares软硬件协同优化可实现近翻倍加速。

## 研究启发
1. FHE加速不能通用化，需针对PSI等上层密码协议运算特征做软硬件联合裁剪，才能释放硬件潜力。
2. Relin是FHE核心瓶颈，需结合运算图层级特征延迟执行，批量合并高开销同态化简操作。
3. 存储密集与计算密集同态操作天然可解耦，分区域流水线能消除互相等待气泡。
4. 近存NDP架构是大数据加密计算最优路线，避免主机与加速器间反复数据搬运。
5. 通用FHE硬件配套算子过多，针对协议精简计算单元可大幅降低芯片面积与功耗。