---
title: "CXL-Interplay: Unraveling and Characterizing CXL Interference in Modern Computer Systems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CXL-Interplay: Unraveling and Characterizing CXL Interference in Modern Computer Systems


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132607">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132607</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>计算快速链接，干扰表征，真实硬件，微基准测试，反向推理分析 </p>
</div>

---

## 研究概要
本文提出CXL-Interplay评测框架，基于两款真实ASIC/FPGA CXL硬件，系统刻画CXL与主存、SSD之间的相互性能干扰。通过微基准与数据库、LLM等真实负载定位TOR队列、缓存抢占等根因，提出cgroup、内存带宽限制等软件调控方案，最高恢复主存带宽至原始99%。

## 背景和动机
1. CXL作为内存扩展标准广泛落地，但CXL、主存DDR、SSD共存时的相互干扰缺乏实测研究，现有仿真仅手动注入延迟，无法还原真实硬件冲突。
2. 已有CXL评测仅单独测设备裸性能，未分析多组件并发下带宽暴跌问题，ntst非临时存储指令带来的干扰尤为严重。
3. 干扰底层机制不明：共享PCIe、CPU LLC与TOR请求队列产生资源争抢，缺少性能计数器逆向溯源分析手段。
4. 缺少可落地的干扰缓解调控方案，数据中心混合内存/存储部署难以保障业务QoS。

## 相关工作
1. CXL仿真工具（CXLMemSim等）：纯软件模拟，无真实ASIC/FPGA硬件验证，无法复现硬件级资源争抢干扰。
2. 现有CXL实测研究（Sun、Tang等）：仅单独评测CXL裸负载，不探究与主存、SSD并发干扰，无干扰缓解策略。
3. 混合内存干扰MT²：面向PMEM与DRAM，不适用于基于PCIe互联的CXL设备场景。
4. CPU缓存/带宽调控技术（CAT、MBA）：未针对CXL跨NUMA访存场景做适配验证。

## 本文解决方案
### 1. 双硬件实测评测平台
搭建两套环境：Montage ASIC CXL+SAS SSD、Intel FPGA CXL+NVMe SSD，覆盖商用与原型CXL硬件，区分NUMA拓扑隔离测试负载。
### 2. 分层干扰评测微基准
设计ld/st/ntst/MOVDIR64B内存指令、随机/顺序读写SSD负载，交叉遍历线程规模，量化双向带宽衰减幅度。
### 3. PMU计数器逆向溯源分析
采集L2/L3缺失延迟、TOR队列占用、内核memmove热点函数，定位LLC抢占、TOR拥塞是干扰核心根源。
### 4. 四类软件干扰缓解策略
基于cgroup限制CXL CPU配额、CPU调频、Intel MBA内存带宽节流；对比缓存分区局限性，量化各方案带宽恢复与性能折中。
### 5. 多类型真实业务负载套件
覆盖文件系统(RocksDB/Filebench)、ML存储、图计算(GAPBS)、内存数据库(Redis)、LLM(TinyLlama)五类典型数据中心负载验证干扰。

## 实验分析
1. 干扰量化：CXL ntst负载对主存带宽抑制最高达93.2%；SSD顺序写比随机写受干扰更严重，MOVDIR64B干扰弱于ntst。
2. 底层根因：CXL流量填满TOR请求队列，大幅拉高L2缺失延迟（最高15.2倍），内核内存拷贝函数耗时上涨近一倍。
3. 负载差异：CXL读负载反而小幅提升部分数据库性能，源于内存指令总量降低；CXL受SSD干扰整体较轻。
4. 调控效果：MBA带宽限制可将主存带宽恢复至原始99%，仅损失5GB/s CXL带宽；CPU配额限制次之，调频恢复效果最差。
5. 硬件差异：ASIC与FPGA CXL设备干扰幅度存在明显区别，底层PCI与内存控制器实现造成性能差异。

## 研究启发
1. CXL部署不能单独测试裸性能，必须混合主存、SSD并发评测，ntst非临时存储是最强干扰源，业务需控制该指令使用。
2. 干扰核心不在PCI共享，而是CPU LLC与TOR请求队列全局资源争抢，跨NUMA CXL流量会污染全部缓存切片。
3. 缓存分区对绕过缓存的ntst指令无效，内存带宽节流是更适配CXL的QoS管控手段。
4. 部分场景CXL读负载可正向加速存储业务，调度器可搭配低强度CXL读负载优化数据库吞吐。
5. CXL硬件设计应新增独立TOR队列、设备侧细粒度带宽控制器，从硬件层隔离跨层内存流量干扰。