---
title: "LMM-IR: Large-Scale Netlist-Aware Multimodal Framework for Static IR-Drop Prediction"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# LMM-IR: Large-Scale Netlist-Aware Multimodal Framework for Static IR-Drop Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA4: Power Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2511.12581v2">https://arxiv.org/abs/2511.12581v2</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大规模网表处理，多模态融合，静态IR压降预测，Transformer </p>
</div>


---

## 研究概要
本文提出LMM-IR多模态静态IR压降预测框架，设计大规模网表Transformer(LNT)将SPICE网表转为三维点云，融合版图图像与网表双模态特征，通过交叉注意力融合建模多层供电网拓扑。ICCAD2023数据集测试，平均F1达0.58、MAE最优，推理耗时远低于对比SOTA，可处理十万级节点供电网。

## 背景和动机
1. 先进工艺金属电阻激增，全芯片SPICE静态IR仿真耗时数小时，迭代优化算力成本极高，亟需AI加速方案。
2. 现有CNN类IR模型仅处理版图图像模态，丢弃SPICE网表节点电阻、通孔、电流源精细拓扑，全局耦合建模不足，热点预测漏检/误检严重。
3. 传统网格化网表编码丢失多层金属、通孔三维空间关系，无法表征跨层电流传输，百万级网表内存开销巨大。
4. 单模态模型仅依赖电流/距离图，特征维度单一，复杂供电网泛化能力差，隐藏测试用例精度大幅下滑。
5. 缺少端到端多模态融合架构，无法统一网表结构化数据与版图图像特征，两类信息无法互补提升预测精度。

## 相关工作
1. PowerNet/IREDGe：纯U-Net卷积模型，仅输入版图热力图，不解析SPICE网表，丢失电气拓扑细节。
2. IRPnet：自适应卷积核，仍为单图像模态，无网表三维点云表征，跨设计泛化弱。
3. ICCAD2023竞赛一二名方案：引入额外手工特征，但不完整处理原始SPICE网表，缺失细粒度节点信息。
4. 点云EDA模型：仅用于拥塞/DRC，未结合Transformer做供电网电气回归任务。
5. 单流CNN编码器：无跨模态交叉注意力，无法对齐网表与版图空间对应关系。

## 本文解决方案
### 1 三维点云网表表征方案
解析SPICE生成三维点云，每个点存储金属层、坐标、器件类型、电阻/电流值，完整保留通孔跨层连接，无网格信息损失，适配十万级节点规模。
### 2 LNT大规模网表Transformer
基于自注意力提取点云全局拓扑特征，捕捉远距离电源与负载耦合关系，解决CNN感受野受限问题，原生适配不规则供电网络。
### 3 双流多模态编码器
一路CNN编码电流、距离、密度等版图热力图；一路LNT编码网表点云，分别输出高维特征嵌入。
### 4 交叉注意力特征融合模块
跨模态QKV注意力对齐版图与网表空间信息，融合两类互补特征，强化IR热点区域特征权重。
### 5 两阶段训练解码器
先重构预训练统一双模态表征，再微调IR回归；多轮上采样+1×1卷积输出全芯片压降热力图，搭配高斯数据增强提升泛化。

## 实验分析
1. 测试基准：ICCAD2023公开合成+真实供电网，含10组隐藏测试用例，节点规模1.5万~18万，对比IREDGe、IRP、竞赛冠亚军。
2. 精度指标：平均F1=0.58为全场最优，相较竞赛第一名提升20%，MAE持平最优基线；热点识别漏检、误检显著降低。
3. 推理效率：平均TAT仅3.05秒，远低于传统仿真与对比AI模型，大尺寸电路无内存溢出。
4. 消融实验：LNT模块对精度提升贡献最大，其次交叉注意力与数据增强，三者组合性能最优。
5. 泛化能力：隐藏异构测试用例中其他模型精度暴跌，LMM-IR稳定性更强，适配未见过的供电拓扑。

## 研究启发
1. 仅靠版图图像无法完整建模供电网电气耦合，融合原始SPICE网表多模态是提升IR预测关键路径。
2. 三维点云比网格映射更适合不规则多层PDN，可无损保存通孔、分层拓扑，降低大规模网表存储开销。
3. Transformer自注意力能弥补CNN全局建模短板，精准捕捉远距离电源负载压降耦合效应。
4. 跨模态交叉注意力可对齐版图与网表空间特征，实现两类数据信息互补，显著改善热点预测F1分数。
5. 多模态EDA预测框架可统一结构化网表与图像数据，是替代慢速数值仿真的高效工业方案。
