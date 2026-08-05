---
title: "An Energy-Efficient High-Utilization Hardware Architecture for Attention Mechanism in Transformer using Balanced Systolic Array and Multi-Row Interleaved Operation Ordering"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# An Energy-Efficient High-Utilization Hardware Architecture for Attention Mechanism in Transformer using Balanced Systolic Array and Multi-Row Interleaved Operation Ordering

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133317">https://ieeexplore.ieee.org/document/11133317</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 注意力机制硬件加速器，平衡脉动阵列，多行交错操作顺序，能效优化 </p>
</div>


---

## 研究概要
本文面向Transformer注意力模块提出纯硬件优化架构：均衡脉动阵列BSA与多行交织调度。BSA融合内外混合乘，采用广播分块、旁路寄存器、Booth共享，阵列利用率达99.5%；多行交织消除中间P缓存高开销。28nm、BERT测试，整体能效提升39%，吞吐量×能效提升38%，SRAM能耗降低31.7%。

## 背景和动机
1. Transformer注意力QK^T、PV矩阵乘是时延与能耗瓶颈，现有优化多依赖稀疏/近似算法，通用性差、绑定特定模型。
2. 传统输入/权重/输出固定脉动阵列无法同时兼顾数据复用、寄存器开销、硬件利用率三者，存在固有折中缺陷。
3. 逐层串行计算需完整存储中间概率矩阵P，片上SRAM读写能耗占比近五成，访存开销巨大。
4. 标准OS阵列卸载阶段产生大量空闲周期，阵列利用率偏低，算力资源浪费严重。
5. 各PE独立配置Booth编码器，存在大量重复编码运算，乘法单元能耗偏高。

## 相关工作
1. 稀疏/近似协同设计加速器：依托token剪枝、近似注意力，算法定制化强，通用场景性能衰减明显。
2. 多重构脉动阵列：切换IS/OS阵列适配前后矩阵乘，但阵列形状不匹配，复用收益受损。
3. 流水线双阵列架构：拆分两套独立阵列分别计算QK、PV，硬件规模翻倍、SRAM访问量激增。
4. 传统OS脉动阵列：外积复用最优，但累加寄存器多、卸载空转，阵列利用率不足97%。
5. 通用CNN脉动阵列：仅面向卷积，未适配注意力QK-PV两段式混合精度计算流程。

## 本文解决方案
### 1 均衡脉动阵列BSA核心设计
采用内外混合乘范式，16×16阵列分4块tile；tile内广播分发数据减少填充周期，tile间脉动传输保证扩展性；每个DPE内置双乘法单元，通过数学推导确定最优阵列尺寸。
### 2 三项硬件能效优化机制
旁路重叠寄存器：计算与结果卸载并行，消除空闲周期；Booth共享编码：每列统一编码复用，编码器由512个降至32个，降低乘法能耗；多粒度数据分块，匹配Q、P片上缓存容量。
### 3 最优复用量化数学模型
建立SRAM访问量计算公式，联立乘法总数约束推导最优行列规模，权衡SRAM读取与累加寄存器能耗，确定b=2为最优单PE乘法数。
### 4 多行交织运算调度
不再完整计算全部QK再算PV，交替处理16行S与对应Z，舍弃大容量临时P缓存，仅保留小块平铺SRAM，大幅削减中间矩阵读写次数。
### 5 完整通用注意力顶层架构
集成BSA、BF16 Softmax单元、分层片上SRAM，INT8乘+INT32累加混合精度流水线，支持任意token长度Transformer，无需算法修改。

## 实验分析
1. 实验环境：28nm工艺、500MHz，BERT-base（token=512），统一512乘加单元对比IS/WS/OS阵列与主流注意力架构。
2. 阵列性能：BSA相比传统OS能效提升40%，硬件利用率最高99.5%；Booth共享额外再降4%总能耗。
3. 访存能耗：多行交织策略相比逐层方案SRAM能耗下降31.7%，消除大容量P临时缓存读写。
4. 综合指标：整套架构相较前人最优方案能效提升39%，吞吐量×能效提升38%。
5. 消融验证：旁路寄存器是利用率提升核心；b=2平衡SRAM与累加器能耗；交织调度无算力损失仅降低访存开销。

## 研究启发
1. 无需依赖稀疏、近似等算法修改，纯硬件脉动阵列与调度优化即可实现通用Transformer加速，兼容性更强。
2. 单一内积/外积阵列难以兼顾复用与资源，内外混合乘分块广播是均衡三者有效思路。
3. 矩阵乘前后两段计算不宜完全串行，交替多行交织可消除大中间矩阵片上存储开销。
4. 脉动阵列卸载阶段空闲是利用率关键短板，旁路寄存器重叠计算/卸载可近乎填满流水线。
5. 阵列级重复运算（如Booth编码）可全局共享，从底层降低算术单元静态与动态功耗。
