---
title: "RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rdma"
  - "nic"
  - "covert-channel"
  - "side-channel"
  - "data-center"
---

# RAGNAR: Exploring Volatile-Channel Vulnerabilities on RDMA NIC

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://www.thu-haslab.org/publication/2025-ragnar">https://www.thu-haslab.org/publication/2025-ragnar</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/THU-HAS/Ragnar">https://github.com/THU-HAS/Ragnar</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 易失信道漏洞，侧信道攻击，微架构反向工程，资源竞争利用 </p>
</div>

---


## 研究概要
本文提出RAGNAR，一套基于RNIC硬件资源竞争的易失信道攻击套件。按四层粒度逆向CX4/5/6网卡，设计三类隐蔽信道、两类侧信道攻击。隐蔽信道带宽达PYTHIA的3.2倍，在分布式数据库、内存分离场景可指纹业务、恢复访问地址，识别精度95.6%，现有HARMONIC隔离方案无法防御。

## 背景和动机
1. RDMA广泛用于数据中心内存分离、分布式数据库，但RNIC内部仲裁、地址翻译硬件存在未被挖掘竞争泄露漏洞。
2. 现有RDMA硬件攻击分持久缓存信道、粗粒度性能干扰两类，缺乏基于实时资源竞争的易失信道研究。
3. 主流防御HARMONIC仅覆盖I/II/III层流量粒度，无法拦截地址偏移IV级细粒度泄露，存在防护盲区。
4. PYTHIA依赖片上缓存，可通过大页、缓存随机化缓解，通用性受限，缺少无缓存依赖的新型攻击。
5. 尚无系统四层粒度RNIC逆向方案，无法完整挖掘流量、QP、MR、地址多级竞争带来信息泄露风险。

## 相关工作
1. RDMA性能干扰攻击：基于流量类型、QP数量竞争，仅造成带宽降级，无数据窃取能力，可被HARMONIC防御。
2. PYTHIA持久缓存信道：利用网卡片上缓存构建隐蔽通道，依赖缓存硬件，防护手段较多，带宽偏低。
3. PCIe粗粒度侧信道：仅能获取粗略负载特征，无法还原精确内存访问偏移地址。
4. HARMONIC隔离防御：提供I~III级流量计数器，监控流量、QP、MR资源，但未覆盖地址偏移细粒度特征。
5. 通用互连侧信道：片上NoC、端口竞争攻击，未针对RDMA专用MR、QP、读写操作硬件特性优化。

## 本文解决方案
### 1 四层粒度RNIC逆向分析框架
定义I流量压力、II流量类型、III资源(MR/QP)、IV地址偏移四层粒度；通过上万组微基准测试，发现读写非单调带宽竞争、2的幂次地址延迟周期等硬件漏洞，提出ULI单位延迟增量度量指标。
### 2 三级隐蔽信道攻击套件
1）跨流量优先级信道：利用读写带宽差异编码比特，零误码但速率极低；2）跨MR资源信道：不同内存区竞争区分0/1，CX6最高51.6kbps有效带宽；3）同MR地址偏移信道：基于地址延迟周期性，隐蔽性最强。
### 3 两类真实场景侧信道攻击
1）分布式数据库指纹：监控攻击者带宽波形区分shuffle/join业务；2）内存分离地址窃取：采集ULI轨迹，ResNet18分类恢复受害者访问偏移，精度95.6%。
### 4 跨代网卡兼容攻击逻辑
适配CX4/CX5/CX6三代Mellanox RNIC，攻击不依赖缓存，仅依靠Tx/Rx仲裁、地址翻译单元实时竞争，规避现有缓存类防护。
### 5 现有防御有效性验证
证明HARMONIC仅能阻断I~III层粗粒度攻击，IV层地址级泄露无法被计数器监控拦截，现有隔离方案存在致命缺陷。

## 实验分析
1. 实验环境：AMD/Intel多服务器，CX4/5/6三代RDMA网卡，测试分布式数据库SHERMAN内存分离系统。
2. 隐蔽信道性能：CX6最高有效带宽51.6Kbps，为PYTHIA(20Kbps)的3.2倍；地址级信道误码率低、隐蔽性更强。
3. 数据库指纹：shuffle/join操作带宽波形区分度高，可实时识别后台查询负载类型。
4. 地址窃取：17类地址偏移分类任务平均识别精度95.6%，可完整还原受害者内存访问热点。
5. 防御测试：HARMONIC无法检测地址粒度竞争泄露，现有流量隔离措施完全失效。

## 研究启发
1. RDMA安全防护不能仅监控流量、QP、MR粗粒度指标，地址偏移IV级细粒度硬件竞争是新型高隐蔽攻击面。
2. 基于实时硬件竞争的易失信道比缓存持久信道通用性更强，难以通过内存、缓存优化手段缓解。
3. RNIC内部Tx/Rx仲裁、地址翻译单元的时序周期特性可作为侧信道载体，网卡硬件设计需均衡各地址延迟。
4. 云RDMA集群仅靠硬件资源隔离不足以保护访问模式隐私，需新增地址粒度监控与延迟随机化机制。
5. 评估RDMA硬件安全必须覆盖四层流量粒度，仅做粗粒度性能隔离会留下可被利用的安全盲区。