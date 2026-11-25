---
title: "GTN-Path: Efficient Path Timing Prediction through Waveform Propagation with Graph Transformer"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# GTN-Path: Efficient Path Timing Prediction through Waveform Propagation with Graph Transformer

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA3: Timing Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132846">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132846</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 静态时序分析，图Transformer网络，波形预测，机器学习 </p>
</div>


---

## 研究概要
本文提出GTN-Path图变换器时序路径波形预测框架，将标准单元、互连线分层建图，搭配波形逐级传播机制，无需时序库与寄生提取。7nm工艺工业电路测试，路径波形平均误差2.98%、延迟误差2.96%；相对HSPICE提速3510倍，商用签核STA工具提速12倍，仅需30%路径数据即可完成训练。

## 背景和动机
1. 先进工艺下GBA时序悲观、PBA耗时久，NLDM/CSM时序库插值外推带来精度损失，和SPICE仿真存在5%以上偏差。
2. HSPICE晶体管级波形仿真精度最高，但计算量爆炸，大规模时序路径仿真周期极长。
3. 传统STA依赖时序库构建、互连线寄生提取，两类流程均占用海量存储与计算资源。
4. 现有GCN/GAT时序预测仅预估单点延迟，无法输出完整上升/下降波形，难以匹配签核波形分析需求。
5. 普通图神经网络仅捕获局部邻接关系，无法建模整条时序路径长距离信号传递依赖。

## 相关工作
1. GBA/PBA静态时序：基于查表时序库，存在固有悲观性、波形精度不足问题。
2. HSPICE晶体管仿真：精度达标但仿真速度极慢，不适合全路径批量分析。
3. GCN/GAT时序预测：仅输出延迟标量，未精细化建模分段互连线，缺失完整波形预测能力。
4. Transformer布线前延迟模型：无单元晶体管、分段互连线细粒度图表征，后布局场景精度不足。
5. CSM电流源时序工具：波形计算开销巨大，时序库生成存储成本极高。

## 本文解决方案
### 1 分层电路图建模机制
晶体管、互连线分段分别构建节点，区分PMOS/NMOS、各类金属段节点特征；融合拉普拉斯特征、器件尺寸、布线几何；通过融合边串联单元图与互连线子图，完整表征时序路径拓扑。
### 2 边感知多头图变换器编码器
多头注意力同时融入节点、边特征，搭配残差层与位置编码捕捉路径长距离依赖；输出全局电路嵌入，解决传统GNN长时序建模短板。
### 3 逐级波形传播解码器
按信号流向逐单元推理输出波形，以上一级预测波形作为下一级输入；预测13等分VDD电压时序点，自动区分上升/下降沿波形。
### 4 轻量化训练流程
仅抽取30%时序路径做SPICE标注训练，剩余70%全量路径用于测试；MSE损失对齐HSPICE黄金波形，无需全量电路仿真标注。
### 5 去库时序预测流水线
跳过时序库生成、StarRC寄生提取步骤，布局网表直接建图推理波形，大幅削减EDA前置流程开销。

## 实验分析
1. 实验环境：7nm ASAP PDK，3套工业后布局电路，V100 GPU，对比HSPICE、商用PrimeTime STA、GCN/GAT基线。
2. 精度指标：未知测试路径波形MARE=2.98%，延迟MARE=2.96%；细粒度互连线建模可提升预测精度近80%。
3. 加速性能：相较HSPICE平均提速3510×，商用签STA提速12×；单电路推理仅数秒，模型训练2小时内完成。
4. 消融对比：移除互连线细粒度建模后波形误差上涨79%；纯GCN/GAT基线波形误差均超4%，劣于GTN-Path。
5. 工程优势：无需时序库与寄生文件，省去TB级存储开销，适配大规模全路径签核时序分析。

## 研究启发
1. 先进工艺时序分析不能仅预测单点延迟，完整波形预测是消除STA悲观性的关键手段。
2. 时序路径存在长距离信号耦合，图Transformer相比GCN/GAT更适合全局时序特征提取。
3. 互连线分段精细建模是提升后布局波形精度的核心，简化互连线会带来巨大预测偏差。
4. ML时序方案可摆脱传统时序库、寄生提取两大高成本EDA流程，显著缩短时序收敛迭代周期。
5. 少量SPICE标注样本即可训练高精度波形模型，大幅降低黄金仿真的数据采集成本。