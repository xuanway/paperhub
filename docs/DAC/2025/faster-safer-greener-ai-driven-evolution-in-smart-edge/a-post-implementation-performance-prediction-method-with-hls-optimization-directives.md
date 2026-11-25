---
title: "A Post-Implementation Performance Prediction Method with HLS Optimization Directives"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# A Post-Implementation Performance Prediction Method with HLS Optimization Directives


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132701">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132701</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高层次综合，指令优化，资源复用，性能预测模型</p>
</div>


---

## 研究概要
本文面向HLS指令优化场景提出实现后性能预测方法，设计Graph Builder构建融合优化指令、硬件资源复用关系的专用图。基于TransformerConv图卷积+聚合池搭建预测模型，预测LUT/FF/CP/功耗/DSP五项指标，误差降至3.87%~8.08%，在未见过内核上泛化能力显著优于现有SOTA。

## 背景和动机
1. HLS循环展开、数组划分等优化指令组合空间爆炸，完整综合布局流程耗时极长，设计空间探索效率极低。
2. 传统解析模型依赖人工提取硬件参数，无法建模多指令间复杂耦合效应。
3. 现有GNN预测仅粗粒度嵌入指令节点，忽略资源复用带来调度阻塞，与真实RTL资源分配偏差大。
4. 主流图网络只聚合节点特征，忽视边携带资源依赖、指令交互关键信息，预测精度不足。

## 相关工作
1. 解析类模型(Lin-analyzer、Comba)：依赖人工硬件参数，难以捕捉HLS启发式优化规则，泛化差。
2. 基础GNN-DSE：仅简单插入指令节点，未建模资源共享调度冲突。
3. IronManPro/HGP：基于基础CDFG建模，缺少资源复用依赖边，无法反映硬件真实时序约束。
4. 传统图注意力网络：消息传递不融合边特征，丢失资源竞争、指令耦合信息。

## 本文解决方案
### 1 指令优化图生成器Graph Builder
基于LLVM IR原始CDFG，叠加指令变换效应，新增**资源复用依赖边(RRD)**，刻画多运算共享DSP/ALU造成的调度等待，完整还原硬件资源分配与时序约束。
### 2 细粒度节点与多类型边特征编码
节点编码操作类型、资源占用、复用标记；区分数据/控制/资源复用三类边，把资源竞争、指令交互信息全部嵌入图拓扑。
### 3 TransformerConv聚合预测网络
采用带边特征自注意力卷积层，三层堆叠后接入全局聚合池融合整张图特征；拼接全局硬件元信息送入MLP，同步输出五项硬件性能指标。
### 4 三阶段完整预测流水线
数据集构建(随机指令采样+Vivado综合打标)→模型训练→推理阶段无需完整布局，直接预测实现后资源、时序、功耗。

## 实验分析
1. 数据集：MachSuite+PolyBench共19套内核，每套1000种指令组合，15套训练、4套未见过内核用于泛化测试。
2. 精度对比：LUT/FF/CP/功耗MAPE分别8.08%、3.87%、4.34%、6.49%，DSP MA仅0.11，全面优于PNA、IronManPro等基线。
3. 消融验证：移除资源复用边后各指标误差显著上升，证明RRD是精度核心增益。
4. 泛化性能：4套陌生内核平均误差远低于对比方法，跨算法场景鲁棒性更强。
5. 仿真工具：Vitis HLS 2023.2综合，Vivado布局布线采集真实性能标签。

## 研究启发
1. HLS性能预测不能只依赖程序数据流，必须补充硬件资源竞争、复用调度关系才能贴近真实实现结果。
2. 图神经网络需要同时利用节点与边特征，带边注意力的TransformerConv比普通GNN更适配电路拓扑建模。
3. 指令间耦合效应无法靠粗粒度节点表示，需要在图中显式建模资源依赖边来还原并行阻塞。
4. 预测模型纳入全局硬件元信息，可大幅提升跨未知内核的泛化能力。
5. 先构造增强型专用图再训练GNN，是低成本加速HLS设计空间探索的有效路线。