---
title: "From Flatland to Forest: Exploring Pareto-optimal Design through RTL Hierarchy Trees"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# From Flatland to Forest: Exploring Pareto-optimal Design through RTL Hierarchy Trees

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132533">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132533</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 设计空间探索，RTL层次树，多目标优化 </p>
</div>


---

## 研究概要
本文提出基于RTL层次树的微架构DSE框架，摒弃传统扁平参数向量建模，设计加权WL子树核量化硬件结构相似度，搭配核K-means聚类实现并行采样。理论证明该方法样本复杂度优于RBF核；Gemmini RISC-V SoC测试，超体积指标相较SOTA最高提升29.3%，聚类大幅缩短评估耗时。

## 背景和动机
1. Chisel参数化生成器带来百亿级设计空间，现有DSE将架构压缩为一维扁平向量，丢失模块层级、数据流拓扑等关键结构信息。
2. 扁平参数空间维度爆炸，存在大量无效参数组合，形成搜索死区，整数/布尔/分类混合参数建模难度高。
3. 传统RBF高斯核仅匹配参数数值，无法识别结构近似、参数差异大的同类架构，代理模型预测精度差。
4. 单次RTL综合仿真耗时数小时，串行评估迭代缓慢，缺少按架构模式分组的并行采样策略。
5. 各模块功耗面积贡献差异巨大，现有核函数均等看待所有子模块，无法区分关键硬件单元影响力。

## 相关工作
1. 基于统计/Adaboost的DSE：仅对参数做统计采样，不利用硬件层级结构，高维空间收敛慢。
2. XGBoost、强化学习DSE：代理模型输入仍是扁平参数，丢失拓扑关联，小样本预测偏差大。
3. GNN嵌入类微架构探索：图编码开销高，无专用层次核度量架构相似度，未支持并行聚类评估。
4. 传统RBF高斯过程DSE：数值距离不代表架构相似，样本复杂度随参数维度线性增长。
5. 标准WL图核算法：通用图相似度计算，未结合EDA综合报告赋予模块权重，不适配PPA多目标优化。

## 本文解决方案
### 1 RTL层次树统一表征
将Chisel配置编译转换为模块层级树，节点代表硬件模块、边代表实例从属关系，完整保留存储阵列、运算单元等分层拓扑，替代扁平参数向量输入。
### 2 加权Weisfeiler-Lehman子树核
迭代重标记子树提取多层级结构特征；从综合报告提取模块面积/功耗权重加权特征向量，证明加权核半正定，适配高斯过程回归。
### 3 低样本复杂度GPR代理
理论推导WL核样本复杂度远低于RBF；基于加权WL核构建多目标高斯过程，同时预测周期、功耗、面积三类PPA指标。
### 4 层次感知核K-means聚类
利用WL相似度做架构聚类，每簇选取代表性初始样本；优化EHVI采集函数，每簇并行生成候选设计，实现多组RTL同步仿真评估。
### 5 完整迭代DSE流水线
参数采样→生成RTL层次树→聚类分组→GPR预测→并行综合仿真→更新数据集循环迭代，输出帕累托最优微架构配置。

## 实验分析
1. 实验环境：Chipyard+Gemmini RISC-V AI加速器，ASAP7nm工艺，Spike仿真，对比Adaboost、XGB、GNN、RL四类SOTA。
2. 理论验证：现代SoC参数d≈200，WL核VC维度仅约42，样本复杂度显著更低。
3. 多目标指标：同等40次评估配额，归一HV相比最优基线提升8.2%，相较传统方法最高提升29.3%。
4. 消融测试：小训练集下层次GPR的R²、MAE全面优于普通GPR；聚类轮廓系数0.597，分组效果远优于RBF-Kmeans。
5. 效率收益：3簇并行策略将总评估时间降低约2/3，海量参数设计空间探索速度大幅提升。

## 研究启发
1. 微架构DSE不能扁平化处理硬件参数，RTL原生层级树是保留架构拓扑信息的高效表征方式。
2. 图核可精准度量硬件结构相似度，结合综合PPA权重能进一步提升代理模型预测可靠性。
3. 传统RBF核受维度灾难限制，基于子树的WL核在高维硬件设计空间具备更强泛化能力。
4. 架构聚类是解决仿真耗时瓶颈的有效手段，分组并行可充分利用计算资源加速帕累托寻优。
5. 硬件EDA领域机器学习建模应优先复用设计原生分层结构，而非简单转为数值向量。
