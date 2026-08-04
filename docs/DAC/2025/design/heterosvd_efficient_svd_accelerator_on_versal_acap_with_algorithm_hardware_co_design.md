---
title: "HeteroSVD: Efficient SVD Accelerator on Versal ACAP with Algorithm-Hardware Co-Design"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# HeteroSVD: Efficient SVD Accelerator on Versal ACAP with Algorithm-Hardware Co-Design


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132878">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132878</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 奇异值分解，Versal ACAP，算法-硬件协同设计，AI引擎，设计空间探索</p>
</div>


---

## 研究概要
本文面向Versal ACAP异构平台提出HeteroSVD，面向分块Jacobi奇异值分解做软硬件协同加速。设计移位环排序、AIE专属数据流与分层布局，配套精准性能模型与自动DSE框架。VCK190实测相较FPGA延迟最高降1.98倍，对比GPU延迟最高提速7.22倍、能效提升13.18倍。

## 背景和动机
1. SVD计算复杂度达立方级，实时通信、推荐系统场景对低时延、高能效需求严苛。
2. 传统FPGA片上存储有限、并行度受限；GPU批量优势强但小矩阵空载功耗高，二者无法同时兼顾时延、吞吐、能效。
3. Versal ACAP集成AIE/PL/PS，但矩阵分块、AIE间带宽、庞大架构设计空间三大难题缺少协同优化方案。
4. 传统环排序与AIE行列非对称拓扑不匹配，大量低效DMA传输挤占带宽，计算资源利用率低下。

## 相关工作
1. FPGA类SVD加速器：仅优化单粒度并行，未利用AIE向量算力，片上存储瓶颈导致吞吐受限。
2. GPU批量SVD方案：大批量吞吐优异，但小规模矩阵内核利用率低，整体功耗极高。
3. 传统Jacobi排序算法（环/轮询）：未适配ACAP AIE硬件拓扑，跨核DMA通信开销巨大。
4. 单一硬件设计工具：无精准性能预估，遍历全设计空间仿真耗时长达数小时，调参效率极低。

## 本文解决方案
### 1 系统级分块SVD重构
基于分块Hestenes-Jacobi算法，将大矩阵拆分子块，正交化、归一化两阶段分别分配orth-AIE、norm-AIE阵列执行。
### 2 算法-硬件协同优化
提出移位环排序，按AIE行列拓扑循环偏移列对排布；输出存储重定向，将DMA远距离传输转为邻居直达访问，大幅削减跨AIE通信。
### 3 分层AIE布局策略
划分正交/归一化/存储三类AIE，按orth-layer、mem-layer分层排布，DMA层中转跨阵列数据，动态转发路由完成块分发。
### 4 自动架构寻优框架
构建双并行度（引擎/任务）性能解析模型，精准测算各类时延；约束资源做两阶段DSE，数分钟输出最优硬件配置。

## 实验分析
1. 测试环境：VCK190开发板，Vitis2023.2，对比XC7V690T FPGA、RTX3090 GPU，矩阵128~1024阶。
2. 时延表现：相对FPGA提速1.27~1.98倍；小矩阵相较GPU最高提速7.22倍，超大矩阵GPU吞吐反超。
3. 能效与功耗：ACAP整机功耗低于39W，相对GPU能效提升4.36~13.18倍，资源占用远少于FPGA。
4. 模型精度：性能模型平均误差仅1.78%，不同批量、频率场景误差不超7.52%，DSE寻优可靠。
5. 参数规律：高Peng适合低时延场景，高Ptask面向高吞吐，但会提升URAM占用与整机功耗。

## 研究启发
1. 异构ACAP加速不能单纯移植现有算法，必须基于AIE行列不对称拓扑重构迭代排序与数据流。
2. 跨AIE通信是核心瓶颈，通过存储重定向规避DMA，相比单纯增加带宽成本更低。
3. 引擎并行与任务并行存在资源互斥，需自动化DSE在时延、吞吐、功耗间做权衡。
4. 解析性能模型可替代周期精准仿真，大幅缩短架构迭代周期，降低开发成本。
5. Versal ACAP在中小矩阵实时计算场景具备GPU、FPGA无可比拟的低时延高能效优势。