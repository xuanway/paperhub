---
title: "333-eDRAM - 3T Embedded DRAM Leveraging Monolithic 3D Integration of 3 Transistor Types: IGZO, Carbon Nanotube and Silicon FETs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# 333-eDRAM - 3T Embedded DRAM Leveraging Monolithic 3D Integration of 3 Transistor Types: IGZO, Carbon Nanotube and Silicon FETs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132950">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132950</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>嵌入式DRAM，单片三维集成，场效应晶体管 </p>
</div>


---

## 研究概要
本文提出333-eDRAM单片三维集成嵌入式DRAM，底层硅CMOS做外设，BEOL堆叠IGZO、CNT两类晶体管构成3T存储单元，融合三种器件优势。7nm工艺搭配Cortex-M0在Embench测试，相较纯硅eDRAM，系统EDP平均提升1.96倍，EADP提升5.15倍。

## 背景和动机
1. 存储墙是嵌入式系统核心瓶颈，传统硅eDRAM刷新能耗高、单元面积大，各项性能难以同时兼顾。
2. IGZO漏电流极低、保留时间长，但迁移率差读写延迟高；CNT驱动电流大速度快，但无法单独实现长留存存储。
3. 现有存储仅单一器件，无法同时满足高密度、长保留、低漏电、高速读写、低刷新等多重指标。
4. 单片3D工艺可低温在后道堆叠新型器件，但缺少IGZO/CNT/硅三者协同的完整eDRAM单元架构。

## 相关工作
1. 纯硅eDRAM：外设与存储单元均采用硅管，单元面积大、刷新开销高，留存时间受限。
2. 单一IGZO eDRAM：仅解决漏电问题，读写通路速度慢，系统吞吐不足。
3. 碳纳米管数字电路：仅用于逻辑，未与低漏IGZO组合构建高密度存储阵列。
4. 传统3D存储堆叠：多为芯粒键合，非单片BEOL逐层集成，互连密度低、面积开销大。

## 本文解决方案
### 1. 三层器件单片3D堆叠架构
底层硅CMOS实现译码、预充、读出放大等全部存储外设；上层多层BEOL依次集成CNT读写管、IGZO存储管，共享底层硅外围电路，大幅提升存储密度。
### 2. 3T异构存储单元电路
1支IGZO管负责存储，利用极低漏电流延长数据留存；2支CNT分别搭建读、写通路，依靠大驱动电流缩短访存延迟；无深沟槽电容即可正常工作，降低读写能耗。
### 3. 系统级协同优化流程
统一扫掠各器件阈值、过驱动电压等参数，兼顾单元保留时间、读写延迟；支持333-eDRAM与硅SRAM混合分区，按应用差异化留存需求分配存储资源。
### 4. 工艺变异适配设计
基于蒙特卡洛仿真分析IGZO阈值波动对留存时间的影响，设计参数约束方案，保证绝大多数存储单元满足最低数据留存指标。

## 实验分析
1. 仿真平台：7nm ASAP7工艺，搭建定制3D PDK，采用SPICE、周期精确RTL仿真，测试Embench 16套嵌入式基准。
2. 单元硬件收益：333-eDRAM单元面积仅0.019μm²，远小于硅eDRAM的0.041μm²，子阵列、整体存储面积大幅缩减。
3. 系统能效：相比纯硅eDRAM，单应用EDP最高提升2.04倍，全基准平均EDP提升1.96倍，EADP平均提升5.15倍。
4. 存储特性：IGZO带来微秒级长留存，刷新能耗显著下降；CNT将读写关键路径延迟缩短近40%。
5. 混合存储效果：高留存地址划分至小片SRAM，其余使用333-eDRAM，可进一步优化系统综合EADP。

## 研究启发
1. 单一半导体器件无法兼顾存储全部指标，单片3D分层集成多类特色晶体管是存储性能突破关键路径。
2. IGZO适配存储保持通路、CNT适配高速读写通路、硅管适配复杂外设，三者各司其职可同时实现高密度、低漏电、低刷新、高速访问。
3. 嵌入式程序内存留存需求高度不均衡，异构混合存储（eDRAM+SRAM）可针对性削减刷新开销。
4. IGZO阈值工艺变异会剧烈改变留存时间，存储设计必须引入蒙特卡洛仿真做鲁棒性校验。
5. 单片BEOL堆叠相比芯粒3D封装互连密度更高、面积损耗更小，适合嵌入式片上高密度存储场景。