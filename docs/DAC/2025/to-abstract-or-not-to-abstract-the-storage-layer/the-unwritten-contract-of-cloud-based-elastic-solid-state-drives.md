---
title: "The Unwritten Contract of Cloud-based Elastic Solid-State Drives"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# The Unwritten Contract of Cloud-based Elastic Solid-State Drives

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132948">https://ieeexplore.ieee.org/document/11132948</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 弹性固态硬盘，性能表征，反直觉发现，云存储合同 </p>
</div>


---

## 研究概要
本文针对AWS、阿里云两款主流云ESSD开展全面性能表征，提出云弹性SSD隐性性能契约，总结4条反常识观测与5条工程启示。实验对比本地SSD发现ESSD存在时延、GC、读写模式、带宽四大差异化特征，给出云存储软件重构优化方向，并开源评测工具。

## 背景和动机
1. 云EBS采用存算分离架构，ESSD对外兼容块接口，现有文件系统、KV引擎均基于本地SSD优化，未适配云存储底层分布式架构。
2. 目前缺少对主流厂商ESSD完整性能定量分析，业界普遍沿用本地SSD优化逻辑迁移上云，极易出现时延暴涨、资源浪费问题。
3. 本地SSD公认痛点（随机写差、GC剧烈抖动）在ESSD上表现完全不同，现有存储优化策略无法直接复用。
4. 企业上云规模持续扩张，亟需一套完整性能特征结论指导云原生存储软件设计，平衡性能与云付费成本。
5. 缺少标准化ESSD评测框架，难以横向对比不同厂商弹性盘的性能差异。

## 相关工作
1. 本地存储表征研究：针对NVMe SSD、Optane、ZNS盘做性能剖析，仅面向单机本地硬件，不适用存分离云ESSD。
2. 云存储架构论文：介绍EBS底层分布式、多副本实现，但未量化I/O时延、GC、读写吞吐等关键性能指标。
3. 云KV引擎优化：仅针对特定业务做IO限流、分层缓存，未提炼通用ESSD底层硬件特性规律。
4. 云负载轨迹分析：统计真实业务IO分布，未从存储设备底层角度拆解性能根源。
5. 存储契约类研究：提出本地SSD硬件隐性契约，无面向分布式云弹性盘的配套分析工作。

## 本文解决方案
### 1 跨厂商标准化ESSD评测方案
选取AWS io2、阿里云PL3两款高端ESSD，搭配本地三星970 Pro作为对照组；使用FIO覆盖4KB~256KB、QD1~32全粒度随机/顺序读写混合负载。
### 2 四大核心性能观测结论
1. 小IO、浅队列下ESS时延是本地SSD数十至上百倍，增大IO尺寸与队列深度可大幅缩小差距；
2. GC性能衰减出现极晚甚至消失，分布式资源屏蔽块回收抖动；
3. 随机写吞吐优于顺序写，最高提升2.79倍，与本地SSD完全相反；
4. 最大带宽由付费SLA固定，不受读写混合比例影响，IOPS则随块大小变化。
### 3 配套五大软件优化启示
1. 业务尽量合并大IO、提升队列深度削减网络开销；
2. 重新评估本地SSD GC缓解算法的上云价值；
3. 无需再将随机写转顺序写，甚至可主动生成随机负载；
4. 平滑IO峰值，避免超付费带宽触发限流；
5. 重新审视压缩、去重等传统耗CPU优化手段。
### 4 开源通用ESSD评测工具
开放测试框架代码，支持多厂商弹性盘横向性能复现与后续拓展研究。

## 实验分析
1. 实验环境：AWS m6in.xlarge、阿里云ecs.g5.4xlarge，本地Xeon工作站搭载三星970 Pro；负载覆盖纯读/纯写/混合，单盘总写入量达3倍盘容量。
2. 时延指标：4KB QD1场景ESS平均时延最高达本地SSD47.9倍，P99.9延迟超100倍；256KB大IO可将差距压缩至数倍。
3. GC对比：本地SSD写入0.9倍容量吞吐暴跌63%；AWS盘至2.55倍容量才下滑，阿里云全程稳定无明显衰减。
4. 读写吞吐：两款ESS随机写吞吐分别为顺序写1.52倍、2.79倍；本地SSD两者性能接近。
5. 带宽约束：ESS总带宽严格锁定厂商承诺上限，读写占比不改变峰值；本地SSD吞吐随读写比例大幅浮动。

## 研究启发
1. 本地SSD的性能假设不能直接套用于云ESSD，存算分离、分布式多副本带来完全相反的硬件表现。
2. 云存储性能瓶颈不再是闪存内部GC，而是跨集群网络与多层软件栈小IO开销，批量IO是核心优化手段。
3. LSM树等为本地SSD设计的顺序写优化逻辑在上云后收益大幅缩水，甚至产生负收益。
4. 云存储成本与带宽SLA强绑定，削峰、轻量化IO压缩可直接降低付费规格，节约云资源开支。
5. 云存储系统研发需建立专用性能基准，不能沿用本地SSD评测标准与优化思路。
