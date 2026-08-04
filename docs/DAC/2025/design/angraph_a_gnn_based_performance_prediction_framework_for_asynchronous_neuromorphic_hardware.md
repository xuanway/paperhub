---
title: "ANGraph: A GNN-Based Performance Prediction Framework for Asynchronous Neuromorphic Hardware"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ANGraph: A GNN-Based Performance Prediction Framework for Asynchronous Neuromorphic Hardware


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11345707">https://ieeexplore.ieee.org/document/11345707</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 异步神经形态硬件，性能预测，图神经网络，基准测试</p>
</div>

---

## 研究概要
本文提出ANGraph异步神经硬件性能预测框架，将系统仿真事件流转为图结构，分别采用GNN（ANGraph-L）、ResNet（ANGraph-P）预测延迟与功耗，构建百万级跨尺度工艺基准。对比TrueAsync仿真，平均R²提升0.69、RMSE下降76%，功耗预测R²达0.98、MAPE仅0.88%，泛化性优异。

## 背景和动机
1. 异步脉冲神经硬件无全局时钟，系统级仿真与门级网表仿真结果偏差极大，TrueAsync延迟MAPE高达50.06%，DSE精度不足。
2. 现有异步电路性能预测依赖传统解析模型，未利用图学习挖掘流水线事件依赖关系，泛化能力差。
3. 异步流水线存在前向、后向、阻塞伪气泡三类事件，普通IR无法完整刻画拥塞时序特征，难以喂入图模型。
4. 缺少覆盖不同网络规模、工艺节点、视觉数据集的标准化预测基准，算法对比缺乏统一标准。

## 相关工作
1. 传统异步电路功耗/时序解析模型：基于状态跳转计数拟合，仅适配小规模电路，跨工艺泛化极差。
2. 基于GNN的同步芯片时序预测：面向有周期数字电路，无法建模异步气泡拥塞事件流。
3. 神经形态系统级仿真器（TrueAsync/CanMore）：仿真速度快，但忽略门级电路细节，时序、功耗预测误差巨大。
4. HLS/布局图性能预测GNN：针对程序、版图图结构，不支持异步握手流水线事件编码。

## 本文解决方案
### 1. 异步事件流转图编码方法
定义前向、后向、伪气泡三类异步事件，设计FSM捕获阻塞等待状态；事件流编码为有向无环异步神经图，超长事件采用复制节点补齐特征维度，统一固定特征向量长度。
### 2. 百万级标准化基准数据集
搭建2×2~8×8Mesh异步SNN硬件RTL，覆盖22/28/65/180nm工艺；搭配MNIST/CIFAR等多任务输入，系统事件流配对VCS门级仿真标签，构建延迟、功耗两大预测数据集。
### 3. ANGraph-L图卷积延迟预测模型
5层均值图卷积堆叠，分层聚合邻域事件特征，全局求和池输出图表征，搭配MLP回归延迟；支持少量样本迁移学习适配新工艺。
### 4. ANGraph-P残差功耗预测模型
双分支ResNet架构，以模块活动矩阵为输入，同时预测静态、动态功耗，总功耗为两者求和，无需图结构输入。
### 5. 端到端预测完整工作流
TrueAsync导出事件JSON→图转换/活动矩阵生成→双模型推理，跳过耗时门级仿真，快速支撑硬件设计空间探索。

## 实验分析
1. 实验配置：PyTorch Geometric搭建模型，Adam优化、Huber损失，跨规模/流量/工艺三类测试集零额外微调验证泛化。
2. 延迟预测：相较TrueAsync，全部数据集平均R²提升0.69、RMSE降低76%；跨尺度平均R²=0.96，新工艺迁移后R²可达0.98。
3. 功耗预测：无对标仿真工具，全数据集平均R²=0.98、MAPE=0.88%，不同规模、工艺下误差稳定。
4. 泛化验证：未重训直接适配2~8核阵列、多视觉数据集、四类制造工艺，无显著精度下滑。
5. 数据集价值：开源百万样本基准，统一异步神经硬件性能预测对比标准。

## 研究启发
1. 异步电路时序偏差根源是系统仿真丢失握手拥塞细节，将气泡阻塞事件完整编码为图是高精度预测关键。
2. 延迟、功耗数据特征结构不同，需分开设计GNN/ResNet专用模型，不可单一网络兼顾两类任务。
3. 图卷积分层聚合可捕捉长流水线事件依赖，少量样本迁移学习能大幅降低新工艺重新标注成本。
4. 统一多尺度、多工艺、多任务基准是领域发展基础，可消除不同方案对比的实验条件差异。
5. 图学习可替代慢速门级仿真，大幅缩短异步神经硬件DSE迭代周期，适配边缘脉冲AI芯片快速迭代。