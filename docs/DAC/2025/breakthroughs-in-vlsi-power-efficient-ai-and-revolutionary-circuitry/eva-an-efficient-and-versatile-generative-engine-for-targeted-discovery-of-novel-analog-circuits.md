---
title: "EVA: An Efficient and Versatile Generative Engine for Targeted Discovery of Novel Analog Circuits"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# EVA: An Efficient and Versatile Generative Engine for Targeted Discovery of Novel Analog Circuits


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133012">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133012</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模拟电路拓扑发现，生成式人工智能，预训练Transformer，强化学习微调</p>
</div>

---

## 研究概要
本文提出EVA通用模拟电路生成引擎，采用引脚级欧拉序列表征电路，基于解码器Transformer先无标注预训练学习拓扑连接，再分别用PPO、DPO微调定向生成高性能新电路。覆盖11类模拟电路，电路有效率94、新颖度99，仅需850份标注样本，10次生成内FoM远超同类方法。

## 背景和动机
1. 传统模拟电路设计依赖人工经验，现有AI方案多复用已知子模块，难以挖掘全新高性能拓扑，创新能力不足。
2. 现有生成模型表征局限，多用器件级DAG图，无法通用表达各类模拟环路电路，适配电路类型单一。
3. 从零训练需海量带性能标注电路样本，仿真评估开销巨大，样本利用效率极低。
4. 缺少定向优化机制，生成大量无效、低性能电路，仿真筛选成本极高，发现效率差。

## 相关工作
1. LLM类生成（AnalogCoder/Artisan/LaMAGIC）：基于代码/文本生成电路，依赖现有拓扑库，难以产出全新结构，仅支持1~7类电路。
2. CktGNN图生成：自顶向下器件级图模型，仅运用于运放，表征为DAG无法兼容环路模拟拓扑。
3. RF逆设计：二进制矩阵生成电磁结构，不能适配多器件原理图级电路，样本需求超60万份。
4. 通用图生成方法：无模拟电路领域专用序列表征，预训练与定向微调协同机制缺失。

## 本文解决方案
### 1. 引脚级欧拉序列统一表征
以器件引脚为节点，欧拉路径序列化任意模拟电路，突破DAG限制，稀疏存储降低开销，适配全部环路拓扑。
### 2. 两阶段训练框架
无标注海量电路预训练解码器Transformer，学习合法引脚连接规律，大幅降低微调所需标注量；设计专用电路Tokenizer编码引脚符号。
### 3. PPO强化微调方案
构建多层奖励模型区分无效/无关/低性能/高性能电路，Plackett-Luce多排序打分，在线生成样本迭代优化。
### 4. DPO偏好微调方案
基于Bradley-Terry成对偏好损失，静态标注数据集训练，无动态奖励噪声，训练更稳定。
### 5. 定向高性能生成流程
微调后限定电路类型与FoM指标，少量生成即可输出超越传统拓扑的新颖模拟电路。

## 实验分析
1. 实验数据集：11类共3470套真实模拟电路，DFS遍历扩充至23万序列，基线为AnalogCoder、CktGNN等。
2. 有效性：EVA预训练+PPO组合有效率94%，高于全部对比方法；新颖度达99，MMD差距显著更小。
3. 通用性：唯一原生支持11类模拟电路的生成框架，其余基线仅支持1类。
4. 样本效率：仅需850份标注拓扑，相较Artisan等减少数十倍标注需求。
5. 发现效率：10次生成内运放FoM达13647.8，电源转换器3.4，显著优于所有对比模型；消融证明预训练+微调缺一不可。

## 研究启发
1. 通用模拟电路生成不能采用器件DAG，引脚级欧拉序列可完整表达含环路的任意模拟拓扑，是通用表征核心。
2. 无标注预训练是解决模拟电路标注稀缺的关键，先学习拓扑先验可大幅缩减微调样本需求。
3. PPO与DPO各有取舍：PPO生成有效拓扑更多，DPO定向产出高性能电路能力更强，可按需选用。
4. 仅做拓扑生成缺少定向优化会产生大量无效电路，偏好/强化微调能显著降低仿真筛选成本。
5. 面向EDA生成模型需兼顾通用性、新颖度、样本效率三指标，单一优化拓扑生成无法落地工业设计。
