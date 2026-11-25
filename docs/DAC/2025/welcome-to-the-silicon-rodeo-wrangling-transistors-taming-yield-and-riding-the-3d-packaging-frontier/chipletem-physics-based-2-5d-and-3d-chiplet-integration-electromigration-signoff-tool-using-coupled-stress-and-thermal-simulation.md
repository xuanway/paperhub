---
title: "ChipletEM: Physics-Based 2.5D and 3D Chiplet Integration Electromigration Signoff Tool Using Coupled Stress and Thermal Simulation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# ChipletEM: Physics-Based 2.5D and 3D Chiplet Integration Electromigration Signoff Tool Using Coupled Stress and Thermal Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA8: Design for Manufacturing and Reliability</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132600">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132600</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 芯粒集成系统，TSV，可靠性，电迁移，热电协同仿真 </p>
</div>


---

## 研究概要
本文提出面向2.5D/3D芯粒异构集成的电迁移签核工具ChipletEM，融合FVM电热协同求解与FDTD应力求解，耦合电迁移、热迁移、焦耳热多物理场，覆盖空洞成核与生长全阶段。单TSV仿真相较AFD方法误差从22.22%降至5.24%，9芯粒系统仿真证实高功耗模式TSV失效风险显著更高。

## 背景和动机
1. 2.5D/3D芯粒TSV电流密度高、层间温度分布不均，电迁移EM成为核心可靠性失效瓶颈，传统Black经验模型保守且适配性差。
2. 现有TSV电迁移AF模型仅单独分析局部互连，忽略全局芯片非均匀热场、热迁移TM反馈效应，仿真误差大。
3. 多数工具割裂电热与应力仿真，无法刻画空洞生长→电阻上升→焦耳热加剧的正反馈耦合关系。
4. 已有方法仅分析TSV与RDL交界处空洞，未考虑高纵横比TSV内部空洞演化场景。
5. 缺乏面向完整多芯粒系统的多尺度协同仿真流程，难以快速评估全系统TSV长期失效分布。

## 相关工作
1. 经验EM模型（Black/Blech公式）：依赖实验拟合，复杂TSV/多芯场景过于保守，无法刻画空洞动态生长。
2. AFD原子通量TSV模型：仅局部电流分析，缺失全局热场与TM耦合，仿真误差高，未区分两类空洞位置。
3. 通用互连EM仿真工具（EMSPISE）：面向2D平面金属，不兼容TSV圆柱结构与芯粒全局散热架构。
4. 单尺度TSV电热分析：仅局部焦耳热计算，无系统级散热器、芯粒层间传热建模。
5. FEM商用多物理工具：精度高但计算开销极大，难以支撑大规模芯粒批量时序仿真。

## 本文解决方案
### 1 FVM芯粒系统全局电热协同求解器
构建包含散热器、芯粒、TSV、微凸块的多尺度传热模型，离散求解焦耳热与温度依赖电阻率耦合方程，输出全部TSV初始温度与电流密度。
### 2 FDTD多物理EM应力求解器
扩展Korhonen方程融合EM、TM原子通量，分空洞成核、生长两阶段建模；区分TSV内部、TSV-RDL交界两类空洞演化，推导对应电阻增量解析公式。
### 3 解析型TSV局部热求解模型
闭式解析方程刻画TSV轴向温度梯度，快速获取时变电流、热阻分布，避免网格离散巨额开销。
### 4 分步多场耦合迭代框架
每仿真时间步双向传递数据：EM输出空洞体积/电阻变化至热求解；热求解更新温度、电流密度回传EM模块，完整捕捉热-电-应力正反馈。
### 5 完整2.5D芯粒签核流程
全局电热预处理→TSV耦合EM时序仿真→长期电阻退化统计，输出不同年限TSV失效比例，支撑可靠性设计迭代。

## 实验分析
1. 实验环境：AMD 6核平台，MATLAB+C混合实现，单TSV与9芯粒2.5D系统两类测试，对比FEM商用工具、AFD主流方法。
2. 单TSV精度：成核阶段平均误差0.61%，空洞生长阶段2.4%；仅单独EM无热耦合最大误差达26.79%。
3. 与AFD对比：同失效阈值仿真误差由22.22%降至5.24%，误差降幅76.4%，与实测退化曲线高度吻合。
4. 全芯粒系统：低功耗6年仅47%TSV失效，高功耗首年54.25%、6年全部失效；早期失效由温度主导，后期由电流密度主导。
5. 热迁移贡献：成核阶段TM贡献11.4%应力，生长阶段15.83%，不可忽略。

## 研究启发
1. TSV电迁移仿真必须耦合全局芯粒热场与局部焦耳热，割裂电热会大幅低估空洞演化速度。
2. 高纵横比TSV存在内部空洞失效路径，不能仅分析RDL交界单一空洞场景。
3. 解析TSV热模型搭配FDTD应力求解，可在接近FEM精度下大幅降低仿真计算量。
4. 芯粒系统功耗直接决定EM寿命，高低功耗模式TSV失效差距巨大，需分工况做可靠性签核。
5. 热迁移是不可忽略的辅助失效驱动力，多物理双向耦合是精准长期寿命预测的必要条件。
