---
title: "NetTAG: A Multimodal RTL-and-Layout-Aligned Netlist Foundation Model via Text-Attributed Graph"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# NetTAG: A Multimodal RTL-and-Layout-Aligned Netlist Foundation Model via Text-Attributed Graph

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://zhiyaoxie.com/files/DAC25_NetTAG.pdf">https://zhiyaoxie.com/files/DAC25_NetTAG.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/hkust-zhiyao/NetTAG/tree/main">https://github.com/hkust-zhiyao/NetTAG/tree/main</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 网表基础模型，文本属性图，多模态表示学习，跨阶段对齐 </p>
</div>


---

## 研究概要
本文提出NetTAG网list多模态基础模型，将电路建模为文本属性图(TAG)，融合LLM文本编码器ExprLLM与图Transformer TAGFormer。设计多层自监督预训练与RTL-版图跨阶段对齐，适配多类功能、物理EDA任务。实验相较GNN、AIG预训练基线精度大幅提升，推理速度优于商用EDA工具。

## 背景和动机
1. 现有电路GNN编码器仅支持AIG图，无法处理加法器、MUX等多样标准单元，依赖真值表训练易出现指数级开销。
2. 纯电路大语言模型仅理解文本语义，缺失网表拓扑结构感知，扁平化门级网表编码效果差。
3. 已有预训练模型只聚焦逻辑功能，未融合延迟、功耗等物理参数，难以支撑时序、面积等物理预测任务。
4. RTL、综合网表、版图三阶段电路信息割裂，现有方法无跨阶段嵌入对齐，跨设计泛化能力弱。
5. 传统EDA预测模型为任务定制，通用性差，缺少可统一适配逻辑推理、PPA预估的通用基础模型。

## 相关工作
1. AIG专用图编码器(DeepGate/FGNN)：仅支持与非图，依靠真值表监督，复杂多输入门失效，无物理信息建模。
2. 电路专用LLM：仅解析RTL文本，无法捕捉门间连接拓扑，网表任务表现不佳。
3. 单阶段EDA预测GNN(GNN-RE/ReIGNN)：针对单一任务监督训练，不具备通用预训练能力，无法跨功能/物理任务复用。
4. 版图图学习框架：仅处理布局几何数据，无法关联RTL高层逻辑语义。
5. 传统商用EDA工具：迭代优化耗时极长，早期网表阶段难以精准预估最终版图PPA指标。

## 本文解决方案
### 1 文本属性图(TAG)电路建模
各门节点附加布尔符号表达式+功耗/延迟等物理文本属性；时序电路按寄存器锥分块降低规模，实现跨阶段等价子电路匹配。
### 2 双分支多模态混合架构
ExprLLM双向大模型编码门文本语义；TAGFormer图Transformer融合全局拓扑，增设CLS向量表征完整子电路。配套RTL、版图独立辅助编码器用于对齐。
### 3 分层四组自监督预训练
1.表达式对比学习，增强布尔逻辑理解；2.掩码门重构、图对比、门数量回归捕捉拓扑；3.RTL-网表-版图跨阶段对比对齐损失融合跨层信息。
### 4 两阶段预训练流水线
第一阶段单独预训练ExprLLM逻辑表达；第二冻结LLM权重训练TAGFormer，联合所有图级、跨阶段损失统一优化。
### 5 轻量化下游微调范式
预训练多粒度电路嵌入，搭配简单MLP/XGBoost即可完成门功能识别、寄存器分类、时序松弛、面积功耗四类EDA任务。

## 实验分析
1. 实验环境：ITC99/OpenCores等开源电路数据集，45nm工艺，8×4090+4×A600，对比DeepGate、GNN-RE等SOTA。
2. 功能任务：门功能识别平均精度97%，较基线提升14%；状态寄存器识别均衡精度86%，提升13%。
3. 物理预测：寄存器松弛MAPE降低2%，电路面积、功耗MAPE均降低7%，优于专用时序/功耗GNN。
4. 消融验证：TAG文本属性、四类自监督损失、跨阶段对齐均为核心增益，移除后各项指标显著下滑。
5. 扩展性：增大LLM参数量、扩充电路数据集可稳定提升精度，推理速度比商用EDA流程快约10倍。

## 研究启发
1. 电路表征需融合文本语义与拓扑结构，TAG格式可突破AIG限制，兼容全部标准单元与物理参数。
2. 单一模态(纯GNN/纯LLM)存在固有缺陷，LLM+图Transformer多模态融合是通用电路基础模型核心路线。
3. 引入RTL-网表-版图跨阶段对齐，可打通设计全链路信息，大幅提升早期PPA预测准确度。
4. 分层自监督预训练无需大量人工标注，一套预训练嵌入可覆盖逻辑、物理多类EDA下游任务。
5. 寄存器锥分块策略可解决超大时序电路算力瓶颈，兼顾模型训练效率与全局拓扑表征能力。
