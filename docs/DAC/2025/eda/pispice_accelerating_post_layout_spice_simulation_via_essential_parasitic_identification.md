---
title: "PiSPICE: Accelerating Post-Layout SPICE Simulation via Essential Parasitic Identification"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# PiSPICE: Accelerating Post-Layout SPICE Simulation via Essential Parasitic Identification

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133011">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133011</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://www.ssslab.cn/assets/slides/2025-li-PiSPICE.pdf">https://www.ssslab.cn/assets/slides/2025-li-PiSPICE.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 版图后SPICE仿真，寄生参数建模，灵敏度分析，模型降阶 </p>
</div>


---

## 研究概要
本文提出PiSPICE版图后SPICE仿真加速框架，基于预布局电路伴随灵敏度识别关键寄生。通过伪RC建模划分敏感/非敏感节点，非敏感子网直接合并，敏感子网采用改进PRIMA降阶。运放、ADC等测试，最大误差低于0.78，最高提速17.27倍，电路规模最高缩减93.77倍。

## 背景和动机
1. 先进工艺互连寄生数量爆炸，后仿真矩阵规模极大，内存与耗时开销过高，传统求解难以收敛。
2. 主流DDM分治存在子电路耦合全局瓶颈，随划分数量增加性能急剧下滑。
3. TICER、PRIMA等通用MOR对全量寄生统一化简，未区分寄生对电路影响强弱，化简上限有限。
4. 直接在后布局海量网表做伴随灵敏度计算算力成本极高，无法工业落地。
5. 绝大多数互连寄生对电路频域、时域指标影响微弱，现有方法无针对性剔除机制。

## 相关工作
1. 区域分解DDM：分块并行求解，但跨耦合节点形成全局通信瓶颈，扩展性差。
2. TIC节点消元MOR：通用RC化简，大规模电路生成稠密矩阵，仿真开销上升。
3. PRIMA投影降阶：适合小型子网，原生无法处理奇异电导矩阵，适配性受限。
4. 各类伴随灵敏度工具：仅用于电路优化，未和寄生裁剪、后仿真加速结合。
5. 传统后仿真流程：全部提取寄生参与求解，无分层化简策略，计算冗余严重。

## 本文解决方案
### 1 预布局伪寄生建模
在预布局电路每个节点插入极小值伪对地/耦合电容、互连电阻，完整复现后布局寄生拓扑，规避大规模后网表灵敏度开销。
### 2 节点级伴随灵敏度判别
计算每个节点相连全部寄生平均灵敏度，以全局均值为阈值划分敏感、非敏感两类节点，定位关键互连子网。
### 3 混合寄生化简策略
非敏感子网：电阻短路、电容合并，直接折叠消除冗余节点；敏感子网：基于稀疏重排改进PRIMA求解投影矩阵做模型降阶。
### 4 自适应阈值调节机制
引入安全系数su，用户按需平衡仿真精度与加速倍率，精度优先保留更多寄生，速度优先激进合并。
### 5 同拓扑复用机制
尺寸迭代、蒙特卡洛等拓扑一致电路，灵敏度结果仅计算一次并复用，大幅降低预处理开销。

## 实验分析
1. 测试电路：运放、带隙、SAR ADC、时钟缓冲共9类，节点规模1k~60k，对比原生Spectre、TICER基线。
2. 规模缩减：相较原始电路最高缩减93.77倍，对比TICER最高缩减43.62倍。
3. 加速效果：AC/瞬态仿真整体提速2.06~17.27倍，相对误差上限仅0.78%。
4. 阈值可调：su越大化简越激进、误差上升，su=0.5为精度速度均衡默认值。
5. 复用收益：同拓扑尺寸优化场景，灵敏度单次复用多电路，整体总耗时降低5.26倍。

## 研究启发
1. 后仿真加速无需统一化简全部寄生，利用预布局做灵敏度前置筛选可大幅削减冗余互连。
2. 分治化简思路：弱影响寄生直接折叠、关键子网精细MOR，兼顾速度与仿真精度。
3. 原生PRIMA受奇异电导矩阵限制，搭配稀疏矩阵分块重排可拓展多端口RC子网适配范围。
4. 伴随灵敏度分析前置在轻量预布局网表，是解决海量后网表算力瓶颈的低成本方案。
5. 拓扑复用机制对模拟尺寸迭代、蒙特卡洛批量仿真增益显著，贴合模拟芯片设计流程。