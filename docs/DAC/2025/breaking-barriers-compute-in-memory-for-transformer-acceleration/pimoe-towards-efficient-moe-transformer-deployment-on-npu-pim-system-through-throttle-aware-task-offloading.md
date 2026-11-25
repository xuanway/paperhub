---
title: "PIMoE: Towards Efficient MoE Transformer Deployment on NPU-PIM System through Throttle-Aware Task Offloading"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PIMoE: Towards Efficient MoE Transformer Deployment on NPU-PIM System through Throttle-Aware Task Offloading

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132528">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132528</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合专家模型，NPU-PIM异构系统，节流感知任务卸载，近存控制器数据压缩器，大语言模型推理</p>
</div>


---

## 研究概要
本文提出NPU-PIM异构协同架构PIMoE，面向MoE Transformer推理。设计节流感知任务卸载平衡异构负载，近内存数据压缩器解决稀疏数据布局失配。基于Switch系列模型验证，相较A100提速4.5倍、能效提升13.7倍，优于现有MoE专用加速器1.4倍。

## 背景和动机
1. MoE模型门控稀疏路由导致专家token负载极度不均，冷热专家计算特性差异大，通用GPU频繁换参带来海量数据搬运开销。
2. 纯NPU片上缓存容量有限，大专家权重反复加载；纯PIM通道同步约束易形成性能瓶颈，单一硬件难以兼顾冷热专家。
3. NPU适配N:M稀疏稠密计算，PIM原生不支持不规则稀疏存储，二者数据布局不匹配引发片上网络拥塞。
4. 现有NPU-PIM混合方案仅简单按延迟分配任务，未识别通道/算力双重节流瓶颈，负载失衡问题未根治。

## 相关工作
1. IANUS/NeuPIMs：通用NPU-PIM架构，仅统一卸载访存密集GEMV，未针对MoE专家不均衡特性优化。
2. MoNDE/Duplex：面向MoE近数据加速，仅调整参/激活数据搬运，无全局节流感知调度机制。
3. FLAME：FPGA端MoE加速器，缺少HBM PIM高带宽并行支撑，大规模模型吞吐受限。
4. 通用LLM混合芯片（寒武纪-LLM）：聚焦稠密Transformer，未适配Mo稀疏门控与多专家动态负载。

## 本文解决方案
### 1 NPU-PIM异构整体架构
NPU负责稠密门控与高负载热专家计算；AB型PIM-HBM利用存储内并行处理冷专家；配套任务调度器、片上网络与内存控制器协同。
### 2 节流感知任务卸载算法
构建通道、NPU双延迟模型，迭代迁移高token冷专家至NPU，消除PIM通道与NPU加载两类性能节流瓶颈，动态均衡异构负载。
### 3 近内存数据压缩器
基于蝶形置换+LROTC位操作过滤权重零元素，将稀疏数据整理为连续稠密数据包，缓解NoC拥塞，大幅降低传输包数量。
### 4 专家交错映射与流水线同步
专家参数交错分配至各HBM通道，分阶段插入同步屏障，避免PIM/NPU频繁模式切换带来额外开销。

## 实验分析
1. 实验平台：4NPU+2片PIM-HBM，仿真器融合PIMSim、Noxim；测试Switch-Base、Switch-Large两类MoE模型。
2. 性能对比：相比A100平均提速4.5倍；对比SOTA MoNDE加速器提速1.4倍，token越少PIM增益越显著。
3. 能效指标：相较A100能效提升13.7倍，近内存压缩器仅增加20.3%控制器面积。
4. 消融验证：节流调度有效消除通道节流；数据压缩器将网络注入速率减半，拥塞延迟大幅下降。
5. 扩展性：新增PIM-HBM设备可线性扩容专家容量，调度逻辑仅需修改时序寄存器即可适配不同硬件。

## 研究启发
1. MoE冷热专家计算特征完全分化，异构NPU-PIM分工是释放推理吞吐最优路径。
2. 混合架构不能仅做简单任务分流，必须建模通道、算力双重节流瓶颈才能根除负载失衡。
3. PIM与NPU稀疏存储格式天然冲突，内存端轻量化置换压缩电路可低成本打通传输瓶颈。
4. 基于蝶形网络的位级重组硬件，适合N:M稀疏权重规整，无需复杂浮点运算。
5. 高层调度算法硬件可固化，通过可编程时序寄存器适配不同PIM/NPU硬件规格，通用性强。
