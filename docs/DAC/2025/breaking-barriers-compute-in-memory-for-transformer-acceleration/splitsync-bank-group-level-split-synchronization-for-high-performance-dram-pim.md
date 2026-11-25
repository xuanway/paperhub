---
title: "SplitSync: Bank Group-Level Split-Synchronization for High-Performance DRAM PIM"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# SplitSync: Bank Group-Level Split-Synchronization for High-Performance DRAM PIM

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132821">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132821</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 拆分同步，存内处理，行激活</p>
</div>

---

## 研究概要
本文提出SplitSync分同步DRAM存内计算架构，以Bank Group为单位组内同步、组间异步执行，规避tFAW时序约束带来的行激活开销。设计分组独立IO与多组结果锁存，无需大电容/共享累加器。CNN/Transformer/GEMV测试，相较传统、ACT16、异步PIM吞吐分别提升1.70×、1.02×、1.06×，单PU面积开销仅1.5%。

## 背景和动机
1. 传统SIMD式DRAM PIM需同步激活全部Bank，受tFAW时序限制，行激活耗时远超MAC计算，整体吞吐被严重拖累。
2. ACT16-PIM靠大容量稳压电容同时激活16Bank，电路面积开销高达20~25%，硬件成本过高。
3. 异步执行PIM各组需中心共享累加器，GDDR6等大行宽存储下面积开销15~20%，还存在频繁IO冲突、流水线停顿问题。
4. 现有架构无法并行执行广播、读写等多类操作，IO通路成为新性能瓶颈，难以适配多头注意力等小矩阵GEMV负载。

## 相关工作
1. 传统全同步DRAM PIM：单指令控制全部Bank，激活开销占比超50%，时序约束无法规避。
2. ACT16-PIM：电路增加储能电容突破tFAW限制，但电容带来巨大面积损耗。
3. 异步执行AESPA-PIM：Bank独立调度，需全局共享累加器，IO冲突频繁，行优先调度性能衰减明显。
4. 通用GEMV PIM优化：仅侧重权重分块，未从Bank组时序与IO架构解决激活瓶颈。

## 本文解决方案
### 1 Bank Group分层分同步执行机制
每组4个Bank内部同步广播、并行MAC，天然满足tFAW四激活限制；不同Bank组异步错开激活时序，重叠激活与计算，大幅掩盖激活延迟。
### 2 分组独立BG IO+合并IO双层架构
每组配置专属IO通路，支持广播、输入写、结果读取并行执行，消除跨组IO争抢冲突，全局缓冲区分块匹配分组数据布局。
### 3 多组BF16结果锁存扩展
每个PU配备4组独立结果锁存，单DRAM行可存放多组矩阵片段，减少中间结果频繁读出，适配Transformer多头小维度矩阵运算。
### 4 适配分组的GEMV分块与专用MAC指令
权重、输入向量按Bank组对半划分，MAC指令携带行存储数量标识，灵活适配不同尺寸矩阵分块，提升存储行利用率。

## 实验分析
1. 仿真平台：DRAMsim3周期仿真，GDDR6配置，测试GEMV、AlexNet/VGG、BERT/GPT等7类基准。
2. 吞吐表现：平均相较传统PIM提升1.70倍，优于ACT16、异步PIM；神经网络负载增益高于纯GEMV。
3. 面积与能效：单PU仅增加1.5%面积，远低于另外两种方案；运算能耗为传统PIM的86%。
4. 时序鲁棒：tFAW越大、DRAM行宽越高，SplitSync性能优势越显著，最低稳定提速1.15倍。
5. 分块调度：行优先调度适配本架构，不会出现异步PIM的大量停顿，小矩阵任务利用率提升明显。

## 研究启发
1. DRAM原生tFAW时序约束无需电路改造，通过Bank组分层时序调度即可低成本化解。
2. 同步、异步优势可结合：组内同步保留广播复用优势，组间异步重叠激活延迟，规避两类方案硬件缺陷。
3. 分层独立IO是释放多操作并行度核心，单一共享IO架构天然存在冲突瓶颈。
4. 增加少量片上锁存即可减少中间访存，相比大容量共享累加器硬件代价更低。
5. 面向Transformer等多小矩阵负载，需要提升单DRAM行的计算容纳能力，降低数据读写频次。