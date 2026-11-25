---
title: "GPS: GNN-Based Two-Stage Pre-Scheduling Loop Mapping Method on CGRAs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# GPS: GNN-Based Two-Stage Pre-Scheduling Loop Mapping Method on CGRAs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132509">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132509</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>粗粒度可重构阵列，循环映射，图神经网络，调度 </p>
</div>

---

## 研究概要
本文提出GPS两阶段CGRA循环映射方法，融合图同构GNN预调度与模式图匹配映射。先通过GNN预测操作优先级压缩搜索空间，再基于VF3子图同构完成DFG到时域CGRA映射。多基准测试，迭代间隔II优化29.4%~406.7%，编译速度最高提升1106.8倍，适配多尺寸ADRES、HyCube架构。

## 背景和动机
1. CGRA循环映射属于NP难子图同构问题，传统ILP方案随DFG规模扩张搜索空间指数爆炸，编译耗时极长。
2. 传统ASAP/ALAP预调度策略输出调度质量差，无法得到最小II，硬件并行利用率低。
3. 现有单阶段映射同时分配时序与PE资源，调度灵活性组合空间巨大，计算开销难以落地大型循环。
4. 主流映射器缺少多面体循环变换协同优化，无法从源码层挖掘并行潜力，适配异构CGRA扩展性不足。

## 相关工作
1. ILP类CGRA映射（CGRA-ME）：可生成最优解，但大规模DFG求解时间不可接受，仅适合小型算子。
2. 启发式调度映射（RAMP/LISA）：采用随机/模拟退火策略，调度质量不稳定，难以逼近最优II。
3. 单阶段GNN映射（GEML）：直接端到端完成映射，未拆分调度、匹配两步，搜索空间压缩有限。
4. 传统两阶段调度（CRIMSON）：依赖ASAP随机预调度，优先级无全局最优指导，映射结果劣化明显。

## 本文解决方案
### 1. 两阶段整体编译流水线
基于MLIR搭建完整工具链，前端做多面体循环变换（分块/融合/展开），后端拆分为GNN预调度、模式图匹配映射两大核心阶段。
### 2. GIN图神经网络预调度模块
以ILP最优结果为标签训练排序损失模型，输入DFG结构、ASAP/ALAP特征输出操作优先级；嵌入列表调度器划分就绪/完成节点，大幅压缩时序搜索空间。
### 3. 基于VF3改进模式图匹配映射
迭代提升II构造时域扩展CGRA(TEC)，按匹配概率重排节点、约束剪枝缩小子图匹配范围，快速完成DFG与TEC同构匹配。
### 4. 全栈协同优化
集成多面体循环变换、硬件无关/特定双层优化，支持4×4/8×8/16×16 ADRES、HyCube两类异构CGRA。

## 实验分析
1. 测试平台：128核Xeon+A100，基准含MiBench/EXPRESS，对比CGRA-ME/RAMP/LISA等主流映射器。
2. 映射质量：4×4 ADRES平均II优化29.5%，16×16架构最高提升406.7%；HyCube架构平均性能提升34%。
3. 编译效率：相较CGRA-ME提速最高1106.8倍，大型循环收益显著，小规模因模型加载略有劣势。
4. 消融验证：GNN预调度平均削减92.4%搜索空间，89.9%基准可取得ILP级最优调度；纯ASAP调度性能差距巨大。
5. 扩展性：PE阵列规模越大GPS增益越明显，适配多种主流CGRA硬件拓扑。

## 研究启发
1. 将NP难映射拆分为“预调度+子图匹配”双阶段，是平衡解质量与编译速度的有效路径。
2. GNN可高效学习图调度全局最优优先级，弥补传统贪心调度局部短板，大幅削减时序组合空间。
3. 子图同构匹配需配合节点概率排序、约束剪枝，才能规避暴力枚举带来的高开销。
4. 映射优化不能仅停留在后端，多面体循环变换可从源码释放并行，显著降低映射压力。
5. 编译方案需适配多规格异构CGRA，两阶段架构天然具备良好硬件可移植性。
