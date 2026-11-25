---
title: "GSIM: Accelerating RTL Simulation for Large-Scale Designs"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# GSIM: Accelerating RTL Simulation for Large-Scale Designs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://talks-pubs.xiangshan.cc/publications/dac2025-GSIM.pdf">https://talks-pubs.xiangshan.cc/publications/dac2025-GSIM.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> RTL仿真，优化，大规模 </p>
</div>


---

## 研究概要
本文提出三层优化的RTL仿真器GSIM，从超节点、节点、比特粒度针对四类仿真开销设计优化，改进图划分算法平衡激活开销与活动因子。基于Firrtl编译输出C++仿真代码，可完整仿真香山处理器，相较Verilator最高提速19.94倍，远超ESSENT、Arcilator等同类工具。

## 背景和动机
1. 大规模RISC处理器RTL软件仿真速度极低，百万级IR节点设计仅千赫兹，验证迭代周期过长，成为芯片设计瓶颈。
2. 主流Verilator全周期逐节点求值，未利用低电路活动因子，大量静止节点重复计算浪费算力。
3. ESSENT引入激活位跳过静态节点，但超节点分组、节点化简、比特粒度仍存在大量优化空间。
4. 现有划分算法优先割边最小化，无法匹配同步激活节点分组需求，造成活动因子大幅上升。
5. 复位、多比特信号、冗余逻辑等场景缺少针对性化简手段，单周期求值分支、运算开销居高不下。

## 相关工作
1. Verilator：经典全周期仿真，每周期遍历全部节点，多核提升有限，超大处理器仿真效率极低。
2. ESSENT：引入激活位机制，基础超节点分组，但划分策略简单，无节点/比特层深度优化。
3. Arcilator：基于MLIR电路编译，内存开销巨大，无法适配香山等超大设计。
4. Khron：侧重存储访存融合优化，未覆盖逻辑节点与比特粒度仿真开销。
5. RepCut：面向多任务并行仿真，和本文单线程单设计优化方向正交。

## 本文解决方案
### 1 仿真开销四因子建模
量化激活位检测、节点求值、总节点数、活动因子四类核心耗时，作为三层优化目标。
### 2 超节点层优化
改进Kernighan划分，优先将同激活节点归组，约束超节点最大尺寸；批量校验激活位，减少分支判断开销，平衡分组规模与活动因子。
### 3 节点层多类化简
数据流消除别名/死/短路冗余节点；构建代价模型决策节点内联/提取；复位逻辑移至慢路径；常量传播、单热信号等表达式化简。
### 4 比特层节点拆分
逐比特数据流分析，按信号访问子集拆分多比特节点，消除无关后继不必要激活，降低全局活动因子。
### 5 完整GSIM工具链
接收Firrtl输入，图层面执行全部优化，编译生成高性能C++仿真代码，支持自定义超节点尺寸参数。

## 实验分析
1. 测试平台：i9-9900K，基准stuCore/Rocket/BOOM/香山，负载CoreMark、Linux启动、SPEC2006。
2. 速度对比：香山跑Linux提速7.34倍，Rocket跑CoreMark提速19.94倍；仅GSIM可完整仿真香山。
3. 消融实验：超节点优化收益最高，比特拆分对乱序处理器增益显著。
4. 参数实验：超节点最优尺寸20~50，过大/过小均降低仿真性能。
5. 资源开销：GS代码体积小于Verilator，编译发射时间接近，远优于ESSENT、Arcilator。

## 研究启发
1. 大规模电路天然低活动因子，激活位+分层分组是软件仿真提速核心路径。
2. 电路划分不能仅以割边为目标，需同步考虑节点同步激活特征平衡活动因子。
3. 仿真优化需覆盖超节点、逻辑节点、比特三层粒度，单一层次优化收益有限。
4. 复位、多比特不完整访问等电路局部特征针对性化简可大幅削减分支与运算开销。
5. 基于Firrtl的编译式仿真框架可深度图变换，相比Verilog直接编译具备更大优化空间。
