---
title: "LightRIM: Light Runtime Integrity Measurement for Linux Kernels in Embedded Applications"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# LightRIM: Light Runtime Integrity Measurement for Linux Kernels in Embedded Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132602">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132602</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 运行时完整性测量，轻量级哈希，事件触发测量，TOCTOU攻击防护</p>
</div>


---

## 研究概要
本文面向资源受限嵌入式Linux设备提出轻量级运行时完整性检测框架LightRIM。基于攻击特征提取核心监测对象，设计两级哈希压缩基线库，结合事件触发动态安全值机制；采用模拟退火随机化检测间隔抵御TOCTOU漏洞。测试系统开销低于0.7%，可有效检测代码注入、Rootkit两类主流内核攻击。

## 背景和动机
1. 车载、机器人等嵌入式广泛使用Linux内核，内核篡改会引发权限逃逸、设备失控，运行时完整性防护需求迫切。
2. 传统IMA完整性架构全量哈希校验，计算与存储开销巨大，算力稀缺嵌入式设备无法部署。
3. PRIMA、DRIVE等现有方案或依赖定制应用，或仅监测内存镜像，覆盖攻击类型不全，通用性差。
4. 固定周期检测存在TOCTOU漏洞，攻击者可预判窗口完成篡改，现有硬件远程证明方案硬件成本高。
5. 缺少可平衡检测覆盖率、CPU开销、抗TOCTOU能力的轻量化内核完整性方案。

## 相关工作
1. IMA标准完整性架构：遵循TCG规范，但全文件哈希带来极高CPU与存储开销，不适配嵌入式。
2. PRIMA：结合SELinux缩减监测范围，但需改造应用与内核，落地门槛高。
3. DRIVE：仅校验二进制内存镜像，忽略系统调用表等关键内核数据，攻击覆盖不足。
4. Xfilter：LSM全局策略框架，监测粒度粗、系统开销大。
5. 硬件可信启动/远程证明：仅保障开机完整性，无法抵御运行时内核篡改，硬件成本高。

## 本文解决方案
### 1 三阶段整体流水线
部署阶段提取内核不可变关键对象、分段大文件、两级哈希生成可信基线库；运行时基于系统事件动态更新对象安全值；测量阶段用SA算法随机检测间隔，比对哈希告警篡改。
### 2 两级轻量化哈希机制
一级对内核段、系统调用表等对象单独SHA256；二级截取各哈希高32位聚合全局摘要，基线库存储开销下降，单次校验仅需比对聚合值。
### 3 事件触发安全值调度
基于kprobe捕获进程创建、模块加载等高危系统事件，动态提升对应对象检测权重；低安全值对象优先校验，兼顾效率与安全。
### 4 SA优化随机检测算法
拟合CPU开销与检测间隔指数模型，以CPU占用为约束，模拟退火生成随机检测时序，大幅提升TOCTOU攻击检出率。
### 5 自适应粗细粒度切换
系统高负载启用粗粒度聚合校验降开销；空闲时开启细粒度单对象比对，兼顾性能与攻击识别能力。

## 实验分析
1. 测试环境：Ubuntu22.04 Linux5.10，基准IMA，采用LMBench、SPEC CPU2006两套评测集。
2. 哈希开销：两级哈希相比单级哈希CPU占用降低23.7%。
3. 攻击检出：1%CPU约束下优化后检出率从23.1%提升至66.7%；9%资源上限检出接近100%，无假阳性。
4. 性能损耗：SPEC整数负载仅0.49%开销，浮点0.67%；LMB系统调用平均延迟提升8.7%，上下文切换仅增加2.3%。
5. 攻击实测：可精准识别VDSO劫持代码注入、Diamorphine Rootkit篡改系统调用表攻击。

## 研究启发
1. 嵌入式内核完整性无需全量监测，基于ATT&CK攻击链路筛选高危不可变对象，可大幅削减计算负载。
2. 分层聚合哈希是降低基线存储与校验开销高效手段，优先全局摘要快速筛查，异常再细粒度定位篡改点。
3. 静态固定检测周期存在严重TOCTOU缺陷，随机化时序可显著缩小攻击利用窗口。
4. 系统事件可作为安全风险信号，动态调整监测优先级，实现按需轻量化防护。
5. 轻量安全框架需支持负载自适应调度，高负载降粒度、空闲提升检测精度，适配嵌入式算力波动场景。