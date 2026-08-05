---
title: "Adora Compiler: End-to-End Optimization for High-Efficiency Dataflow Acceleration and Task Pipelining on CGRAs"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Adora Compiler: End-to-End Optimization for High-Efficiency Dataflow Acceleration and Task Pipelining on CGRAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132391">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132391</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 粗粒度可重构阵列编译器，循环变换 </p>
</div>

---

## 研究概要
本文提出面向CGRA的端到端Adora编译器，基于MLIR与多面体分析，分数据流、任务流两层定制优化，配套快速帕累托寻优算法。支持C/PyTorch/TensorFlow输入，适配RISC-V+CGRA异构SoC。Polybench与AI模型测试表明，相比NSGA-II搜索提速6倍，低功耗CGRA单核算力接近高端CPU，边缘推理能效优势显著。

## 背景和动机
1. CGRA具备字级分时重构、低功耗优势，适合边缘循环/AI任务，但缺少兼顾易用性与深度硬件感知的完整编译器。
2. 开发者不熟悉CGRA存储与PE约束，手写高性能嵌套循环门槛极高，现有工具缺少自动化循环变换。
3. 现有CGRA编译仅优化内核循环，未统筹DMA、重配、多任务流水线、乒乓缓存等系统级任务调度。
4. 循环变换组合空间巨大，盲目搜索开销高，多数优化存在冲突甚至反向降速，缺少有序的优化调度流程。
5. 主流CGRA映射工具仅适配CNN，通用性弱，无统一端到端编译链路，无法覆盖通用循环与NLP模型。

## 相关工作
1. 专用CGRA循环变换工具：仅支持分块、展开单一变换，缺少多变换协同策略，未考虑SPM存储约束。
2. GNN驱动CGRA映射：依赖智能搜索，优化空间无裁剪，寻优耗时极高，无系统任务流水线优化。
3. CNN专用CGRA编译器：仅面向卷积网络，不支持通用嵌套循环、Transformer等复杂计算。
4. 多面体编译(Pluto等)面向CPU/GPU，未适配CGRA分时PE、多Bank SPM、DMA乒乓硬件特征。
5. FPGA高级综合工具：位级重构，与CGRA字级分时架构不匹配，调度逻辑无法复用。

## 本文解决方案
### 1 端到端MLIR编译前端
兼容C、PyTorch、TensorFlow输入，统一转为MLIR中间表示，自动剥离控制流、识别可卸载循环内核，最大化CGRA算力占用。
### 2 数据流层硬件感知循环优化
基于多面体依赖分析实现分块、重排序、展开/融合、DFG重写；根据SPM容量约束自动划分tile，检测写端口冲突选择展开融合规避访存竞争，重构数据流图合并硬件原生算子。
### 3 任务流全系统调度优化
建立跨任务依赖多面体模型，自动插入屏障指令；冗余DMA/配置消除、散射聚集传输、运行时动态重配；多Bank乒乓缓存重叠计算与数据搬运。
### 4 分层快速帕累托寻优算法
筛选重用最优循环排列，遍历三类乒乓缓存策略，依次执行分块、冲突判定、展开策略、DFG生成、任务优化；以II、资源利用率、总传输量为指标筛选前5最优方案，大幅缩减搜索开销。
### 5 异构SoC映射与验证链路
适配RISC-V控制核+多Bank SPM+DMA+CGRA架构，生成可仿真/流片可执行配置文件，支持VCS仿真与FPGA原型验证。

## 实验分析
1. 实验环境：TSMC 40nm 500MHz两种CGRA规格(6×8/12×16)，基准Polybench、ResNet/AlexNet/BERT，对比i7 CPU、Intel Agilex FPGA、NSGA-II搜索算法。
2. 通用循环性能：同等功耗下CGRA单核算力可达i7单核0.42~0.99倍，规整矩阵类加速效果最优；依赖密集类提升有限。
3. AI推理：12×16 CGRA延迟高于10nm FPGA，但面积功耗显著更低，边缘能效更优。
4. 寻优效率：Adora有序优化流程相比NSGA-II穷举搜索平均提速6倍。
5. 消融验证：分块、展开融合、乒乓缓存、冗余指令消除均为关键增益，多层优化叠加大幅降低DMA请求与启动间隔II。

## 研究启发
1. CGRA编译必须软硬件协同，SPM容量、PE端口、分时重构等硬件约束要嵌入多面体变换全过程。
2. 编译优化存在强先后依赖，无序穷举搜索效率极低，定制有序优化流程可大幅压缩寻优空间。
3. 仅做内核循环优化不足以释放CGRA性能，DMA、多任务流水线、动态重配等系统级调度必不可少。
4. 展开融合是解决SPM写端口冲突的关键手段，可在不增加硬件前提下提升并行吞吐。
5. CGRA适配通用循环与大模型具备潜力，轻量化端侧场景相比CPU/FPGA拥有独特能效优势。