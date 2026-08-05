---
title: "PastATPG: A Hybrid ATPG Framework for Better Test Compaction with Partial Assignment SAT"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# PastATPG: A Hybrid ATPG Framework for Better Test Compaction with Partial Assignment SAT

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA9: Design for Test and Silicon Lifecycle Management</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132425">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132425</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/sklp-eda-lab/PastATPG">https://github.com/sklp-eda-lab/PastATPG</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合ATPG框架，SAT求解器，测试压缩，监视技术 </p>
</div>


---

## 研究概要
本文提出混合ATPG框架PastATPG，自研PA-MiniSat部分赋值SAT求解器。采用全文字监视与电路自适应分支策略生成含大量X不定位测试向量，统一融合结构与SAT测试压缩流程。标准电路测试，向量数量平均降幅超36%，中小电路速度优于商用ATPG工具。

## 背景和动机
1. 传统SAT-ATPG会对故障传递扇入所有输入做完整0/1赋值，测试向量指定位过多，静态、动态压缩空间极小，向量数量爆炸、测试成本飙升。
2. 主流CDCL求解器依赖双文字监视机制，无法输出含X不定位的部分解，难以适配ATPG压缩需求。
3. 现有SAT压缩方案仅后置优化，未从求解根源增加不定位，反复调用SAT带来巨大时间开销。
4. 结构ATPG与SAT模块割裂，缺少统一压缩流水线，难兼容两类测试向量合并优化。
5. 通用VSIDS分支策略未利用电路拓扑信息，求解故障收敛速度慢。

## 相关工作
1. 传统SAT-ATPG（MiniSat/CaDiCaL）：输出全赋值测试立方体，无原生X位生成能力，压缩收益低。
2. PASSAT多值编码SAT：通过多值CNF引入不定位，但大幅增大公式规模，求解效率暴跌。
3. 动态/静态测试压缩算法：仅后置合并向量，无法从SAT求解阶段预留不定位，迭代开销巨大。
4. MTTG多目标测试生成：分组兼容故障难度高，失败率高，不适合大规模电路。
5. 开源结构ATPG：回溯限制下大量难测故障无法生成向量，依赖SAT兜底但无配套压缩协同机制。

## 本文解决方案
### 1 PA-MiniSat部分赋值SAT求解器
改造MiniSat CDCL架构，区分原始子句与学习子句监视策略：原始子句采用全文字监视，学习子句保留双文字监视；维护未满足子句计数器，一旦全部满足直接返回含X部分解。
### 2 电路自适应VSIDS分支启发式
结合电路门逻辑深度初始化变量活跃度，故障传播通路变量优先分支，缩短冲突搜索路径，提升难测故障求解速度。
### 3 PastATPG混合一体化流水线
先执行结构ATPG，超回溯阈值故障送入PA-MiniSat；统一静态、动态测试压缩模块，结构与SAT生成立方体混合合并。
### 4 双监视平衡优化
全文字监视仅用于短原始子句，规避全监视全局扫描开销，兼顾X生成能力与求解效率。
### 5 兼容工业DFT流程
支持ISCAS/ITC/RISC-V等组合电路，输出标准化测试向量，可对接商用故障仿真工具。

## 实验分析
1. 测试基准：ISCAS85/89、ITC99、RISC-V e203工业核，对比MiniSat、Kissat、CaDiCaL及商用ATPG。
2. X位生成：PA-MiniSat平均可生成35.8%不定输入位，大幅拓宽压缩空间。
3. 压缩效果：相较主流SAT，测试向量平均减少36.8%~41.46%，最优案例仅为原10.71%。
4. 运行速度：中小电路求解速度远超商用工具；大规模冗余电路因全监视存在一定时间开销。
5. 消融验证：全文字监视、电路分支策略两项模块缺一不可，移除后压缩与速度均大幅退化。

## 研究启发
1. SAT-ATPG向量膨胀根源是全赋值约束，需改造底层BCP监视机制，从求解器原生输出不定位，而非后置补救。
2. 分类型文字监视策略可平衡部分赋值能力与SAT运行开销，原始/学习子句差异化设计是高效折中方案。
3. 电路拓扑信息可嵌入分支启发式，针对故障传播路径加速难测故障求解。
4. 结构ATPG与SAT不能分治，统一测试压缩流水线才能最大化向量精简收益。
5. 面向DFT的专用SAT求解器不能照搬通用CDCL实现，需结合测试压缩需求定制底层推理逻辑。
