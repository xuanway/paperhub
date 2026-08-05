---
title: "Power-Grid Structure Exploration with Unified Sequence-based Learning Framework"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Power-Grid Structure Exploration with Unified Sequence-based Learning Framework

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA4: Power Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133066">https://ieeexplore.ieee.org/document/11133066</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 电源网格结构，序列化表示，Transformer预测器，多目标优化 </p>
</div>


---

## 研究概要
本文提出基于序列建模的统一电源网格探索框架，设计PGTransformer预测静态IR压降，搭配MLHS采样与改进NSGA-II多目标优化。将多层供电结构转为序列表征，自动生成帕累托最优PG方案。3nm/2nm工业芯片测试，压降预测平均误差仅0.011%，优化后布线资源占用降低15%，时序裕度提升34%。

## 背景和动机
1. 先进工艺晶体管与金属间距差距扩大，IR压降、布线拥堵问题突出，初始供电网格直接决定后端收敛难度。
2. 不同IP功率密度差异大，单一PG结构易出现IR违规或布线资源浪费，人工迭代耗时可达数周。
3. 现有ML压降模型仅适配固定供电结构，难以捕捉多层金属、交错/直列柱型架构间耦合影响，预测精度不足。
4. 传统优化仅局部微调PG金属，无法全局遍历各类层堆叠架构，可行方案搜索空间狭窄。
5. 多密度场景缺少自适应IR阈值缩放机制，人工调参成本高，难以批量生成适配供电方案。

## 相关工作
1. U-Net/CNN类IR预测模型：基于网格图像建模，无法表征多层金属柱型堆叠结构跨层关联，细微PG变化预测误差大。
2. XGBoost等树型模型：仅提取离散特征，丢失层序上下文依赖，泛化能力弱。
3. LSTM时序模型：存在梯度消失问题，长多层供电序列建模精度受限。
4. 局部PG微调算法：仅修改单一层金属宽度/间距，不全局探索完整堆叠架构。
5. 传统多目标布线优化：未针对供电网格专用模板、序列生成逻辑设计，PG方案多样性不足。

## 本文解决方案
### 1 序列式PG结构生成器
定义交错、直列等柱型模板，以双字符序列表征多层上下堆叠逻辑；通过锚层偏移控制各类金属间距，快速生成海量合法供电拓扑。
### 2 MLHS均衡采样策略
兼顾数值、分类PG特征，最大化样本最小距离，少量样本即可覆盖完整结构空间，大幅减少商用Voltus真值仿真开销。
### 3 PGTransformer压降预测模型
多层PG参数编码为序列，多头自注意力捕获跨层电阻/通孔耦合；引入隐藏状态距离构建置信度惩罚项，修正外推样本预测偏差。
### 4 多密度IR阈值缩放公式
基于功率密度比例动态调整压降约束，一套模型适配高低功耗IP多场景需求。
### 5 改进NSGA-II帕累托优化
以PG资源占用、带置信修正IR偏差为双目标；序列交叉+锚点变异迭代，输出多组折中最优供电方案。

## 实验分析
1. 测试平台：TSMC N3E、N2工艺CPU/SoC工业设计，基准包含人工量产PG方案，对比U-Net、XGBoost、LSTM。
2. 预测精度：PGTransformer平均MAE相较基线降低51%，最大压降百分比平均误差仅0.011%，推理速度微秒级。
3. 供电优化收益：帕累托最优PG平均金属占用下降15%，最差时序裕度提升34%，芯片面积仅小幅增加0.5%。
4. 效率对比：人工PG迭代需2~3周，本框架平均65分钟完成完整结构搜索。
5. 消融验证：序列表征+注意力机制是跨层精准预测核心，MLHS显著减少真值仿真算力消耗。

## 研究启发
1. 多层供电网络具备天然层序依赖，序列+Transformer架构比图像模型更适合IR压降精准预测。
2. 完整PG优化不能局限局部微调，需从底层柱型模板全局生成海量堆叠拓扑扩大解空间。
3. 模型隐藏状态距离可量化预测可信度，能有效修正外推结构的压降预估偏差。
4. 多目标帕累托优化可同时平衡供电完整性与布线资源，给后端提供多套落地方案。
5. 功率密度自适应阈值缩放机制，一套训练模型可复用至不同功耗IP，降低重复建模成本。
