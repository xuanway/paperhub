---
title: "Anchor First, Accelerate Next: Revolutionizing GNNs with PIM by Harnessing Stationary Data"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Anchor First, Accelerate Next: Revolutionizing GNNs with PIM by Harnessing Stationary Data

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132411">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132411</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>图神经网络，存内处理，固定数据 </p>
</div>

---

## 研究概要
本文提出软硬件协同PIM架构Anchor，遵循“最大化驻留数据、最小化迁移数据”核心准则。设计Mastav图划分算法提升本地驻留顶点占比，配套推拉混合数据流与分层广播规约通信机制。在GCN/GIN/GraphSage测试，相较主流GNN加速器平均提速3.1~13.01倍，能耗降低1.58~14.4倍。

## 背景和动机
1. 图神经网络拓扑不规则，跨存储单元数据搬运开销是核心性能瓶颈，3D堆叠近存PIM虽缓解片外访存，但跨PIM单元通信损耗仍严重。
2. 现有划分方案驻留顶点占比极低，标准METIS仅35.6%，PIM规模扩大后降至18.7%，大量顶点需跨单元反复传输。
3. 非驻留顶点度数远高于平均节点，传统推拉单一数据流造成多次重复复制，互连能耗占比居高不下。
4. 缺少软硬件一体化协同方案，图划分、计算数据流、片上通信三者独立优化，无法系统性削减跨栈数据迁移。

## 相关工作
1. 传统GNN专用加速器（HyGCN/GROW）：基于片上阵列，未利用PIM近存优势，无法解决跨存储块大规模顶点搬运。
2. 早期PIM-GNN架构（GCIM/Lift）：仅优化存储集成，图划分策略简陋，驻留顶点占比低，无混合数据流优化。
3. 源切割/混合切割图划分（METIS/DBH）：METIS随PIM扩容驻留率暴跌，DBH驻留率上限仅49.8%，未引入模块化聚类提升局部性。
4. 单一推拉数据流方案：仅支持推送或拉取一种聚合模式，非驻留顶点需多次复制，冗余传输量大。

## 本文解决方案
### 1. Max-Min优化准则
确立架构设计核心目标：最大化PIM单元内驻留顶点数量，最小化非驻留顶点跨单元传输次数，作为划分、数据流、通信统一优化依据。
### 2. Mastav混合切割图划分算法
两步执行：先按顶点度数分配边实现混合切割；再基于模块度聚类同社区顶点，约束单簇边数均衡负载，驻留顶点稳定维持62%~70.5%，复杂度O(|E|)。
### 3. 推拉混合聚合数据流
本地驻留顶点采用推送式广播特征；远程非驻留顶点采用拉取式聚合，非驻留数据仅分发一次，配套划分边缘/本地/远程三分区存储管理。
### 4. 分层广播-规约通信硬件
栈内TSV本地广播、蜻蜓拓扑树状全局广播减少副本分发；合并阶段分层规约聚合副本，基片增设组合合并单元、内外通信控制器支撑指令调度。
### 5. 可扩展3D堆叠PIM硬件单元
每个PIM集成MAC聚合阵列、顶点定位器、冲突哈希表；新增Sync/Replic/Merge三类专用指令，适配GNN聚合、合并全流程。

## 实验分析
1. 实验平台：32nm工艺RTL综合，扩展DRAMSim3周期仿真，测试6张真实规模图、三类经典GNN模型，对比HyGCN/GROW/GCIM/Lift。
2. 划分效果：Mastav驻留顶点62%~70.5%，相比DBH提升超20%，数据搬运总量下降38%~40%，负载保持均衡。
3. 性能提升：相对四类基线平均提速3.15×~13.01×，规模越大增益越显著；64栈场景Mastav相较METIS提速7.16倍。
4. 能耗收益：互连、DRAM搬运能耗大幅削减，平均能耗相较基线降低1.58~14.4倍，互连能耗降幅最明显。
5. 硬件开销：单PIM单元面积仅0.18mm²，基片逻辑占芯片10.6%，硬件成本可控，具备规模化部署能力。

## 研究启发
1. PIM加速GNN的核心突破口不是片内计算，而是提升顶点本地驻留率，图划分算法是软硬件协同优化前置关键。
2. 单一推拉数据流存在固有冗余，混合数据流可让非驻留顶点仅分发一次，从源头削减重复数据复制。
3. 跨栈互连通信开销不可忽视，分层广播+树规约可大幅削减多路径重复传输，适配蜻蜓全局网络拓扑。
4. 图划分不能只看切割边数，结合模块度聚类挖掘顶点局部关联，可在均衡负载同时大幅提升驻留顶点比例。
5. 3D堆叠PIM架构优化需分层设计：软件划分负责数据局部性，单元数据流减少单次传输量，全局通信降低跨栈冗余，三层协同才能达到最优能效。