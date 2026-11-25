---
title: "MetaDSE: A Few-Shot Meta-Learning Framework for Cross-Workload CPU Design Space Exploration"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# MetaDSE: A Few-Shot Meta-Learning Framework for Cross-Workload CPU Design Space Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.13568">https://arxiv.org/abs/2504.13568</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 设计空间探索，跨工作负载，预测模型，元学习 </p>
</div>

---

## 研究概要
本文提出MetaDSE少样本元学习CPU跨负载设计空间探索框架，将DSE转化少样本任务，采用MAML元预训练缓解过拟合与数据歧义；设计WAM负载自适应架构掩码算法，脱离负载相似度依赖。基于SPEC CPU2017与GEM5验证，相较SOTA预测误差降低44.3%，少量样本即可完成新负载精准PPA预测。

## 背景和动机
1. CPU微架构参数空间庞大，全仿真开销极高，跨负载迁移学习DSE可减少新负载采样仿真次数。
2. 现有迁移DSE采用普通监督预训练，易跨负载数据歧义发生过拟合，泛化差。
3. 传统知识迁移依赖负载分布相似度，真实SPEC负载差异大，相似假设不成立，适配精度暴跌。
4. 现有方法未区分架构固有参数关联，无关参数交互引入噪声，进一步增大预测误差。
5. 新负载仿真样本稀缺，传统模型微调需要大量标注数据，工程探索成本居高不下。

## 相关工作
1. 同类迁移DSE（TrEnDSE/TrDSE/TrEE）：依靠Wasserstein距离、聚类筛选相似源负载，强依赖负载相似度，泛化受限。
2. 线性拟合类D：简单映射源目标标签，假设分布线性，无法适配复杂CPU非线性PPA关系。
3. 数据增强方案：高斯混合扩充样本，仅缓解数据不均衡，不能解决跨负载歧义与过拟合。
4. 单负载DSE（AttentionDSE）：Transformer代理仅适配单一负载，无跨负载迁移能力。
5. 通用元学习MAML：多用于图像分类，未面向CPU架构参数交互做定制适配。

## 本文解决方案
### 1 元学习MAML预训练流水线
把每种负载视作独立任务，内外双层梯度优化；内层单任务少量梯度微调，外层聚合多任务元损失更新初始化权重，习得通用架构先验，抑制跨负载过拟合。
### 2 Transformer代理预测器
基于AttentionDSE构建代理模型，自注意力层捕捉CPU流水线、缓存等参数复杂交互关系，为掩码生成提供权重依据。
### 3 WAM负载自适应架构掩码算法
提取预训练自注意力权重，筛选跨负载稳定高相关参数交互生成二元掩码；过滤无关参数噪声，知识迁移不再依赖负载相似度。
### 4 两阶段完整DSE流程
预训练阶段多负载元学习获得通用初始化；适配阶段嵌入WAM掩码，仅用少量目标样本微调，快速适配全新程序负载。
### 5 统一评估仿真链路
基于GEM5时序仿真+McPAT功耗建模，结合Simpoint分段采样生成SPEC数据集，支持IPC、功耗多指标预测。

## 实验分析
1. 实验环境：GEM5+McPAT仿真器，SPEC CPU2017基准，乱序CPU全参数设计空间；基线TrEnD、RF、GBRT。
2. 整体精度：MetaDSE相较TrEnDSE整体预测误差降低44.3%；移除WAM后误差上升27%，掩码增益显著。
3. 少样本能力：新负载仅5组样本即可达到高精度，样本扩充性能提升平缓，稀缺场景优势巨大。
4. 消融对比：仅替换Transformer基线提升有限，MAML元预训练+WAM掩码是核心增益组合。
5. 泛化验证：不同IPC、功耗预测任务EV更高、MAPE更低，跨差异极大负载依然稳定。

## 研究启发
1. 跨负载DSE不能基于负载相似度做知识迁移，应挖掘CPU架构固有参数关联，摆脱程序分布约束。
2. 元学习适配少样本架构探索，通过多任务双层梯度学习通用初始化，从根源解决跨负载过拟合问题。
3. Transformer注意力权重可量化参数交互，构造掩码过滤噪声，大幅降低代理模型预测误差。
4. 真实工业负载分布差异显著，基于相似性的传统迁移方案鲁棒性差，架构感知迁移更实用。
5. 软硬件协同DSE可分两阶段解耦通用先验学习与目标负载微调，大幅削减仿真算力开销。
