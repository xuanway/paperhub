---
title: "Generative Model Based Standard Cell Timing Library Characterization"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Generative Model Based Standard Cell Timing Library Characterization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA3: Timing Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133303">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133303</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 库表征，工艺角爆炸，机器学习，生成式模型，工艺角选择 </p>
</div>


---

## 研究概要
本文提出基于条件对抗自编码器CAAE的标准单元时序库表征生成模型，解决PVT角点爆炸、SPICE仿真耗时过长问题。以锚点角点时序数据训练，仅需少量仿真样本即可预测增量角完整时序表，无需厂商涉密晶体管网表。SAED14nm等测试，MAE低至0.38ps，整体表征时长缩减42.8%。

## 背景和动机
1. 先进工艺细分PVT角点数量激增，传统Siliconsmart全SPICE仿真计算量爆炸，库表征周期长达数百小时。
2. 商用SPICE工具依赖厂商加密晶体管参数、单元网表，外部设计人员无法完整复现标准单元时序仿真流程。
3. 现有FFN、线性回归模型泛化能力弱，不同单元/时序弧需单独训练，外推增量角误差大。
4. GNN类表征方法必须读取单元内部拓扑，涉密网表场景无法落地使用。
5. 传统模型难以拟合时序表高维连续曲面，电压/温度变化时预测结果断层不平滑，影响STA精度。

## 相关工作
1. 线性回归时序插值：结构简单，但跨PVT外推误差极高，仅适用于少量邻近角点。
2. FFN时序表征（Aadam）：单模型适配范围窄，每种单元/时序弧需独立网络，易过拟合。
3. 图神经网络GNN库建模：依赖单元网表拓扑，涉密工艺场景不可用。
4. 传统GAN时序模型：生成输出存在随机噪声，时序表连续性差。
5. 商用Siliconsmart：全量SPICE仿真，精度高但算力、时间成本极高。

## 本文解决方案
### 1 条件对抗自编码器CAAE混合生成架构
融合自编码器消除GAN随机噪声，搭配z判别器、时序表双判别器；输入PVT、负载、时序表中值枢特征，输出完整M×N时序查找表。
### 2 标准化时序特征工程
定义枢值（时序表中位数）作为条件输入，编码工艺/电压/温度、输入转换、输出电容等多维特征，统一长短时序向量格式。
### 3 分层平衡训练策略
编码器-生成器多轮反向传播后更新判别器，动态均衡MSE拟合损失与BCE对抗损失，稳定GAN纳什均衡。
### 4 HDBSCAN锚点角点自动筛选
对海量PVT角聚类，选取覆盖工艺温压极值的代表性锚点，仅1/3数量SPICE样本即可完成训练。
### 5 完整库表征流水线
锚点SPICE仿真→CAAE模型训练→增量角时序批量生成，支持上升/下降、转换多类时序弧统一预测。

## 实验分析
1. 实验数据集：CAD竞赛400单元、SAED14nm 835单元，覆盖ff/tt/ss多工艺、宽温压区间PVT角。
2. 精度指标：对比线性回归、FFN，平均MAE降至0.38ps，14nm工艺时序达标通过率97.12%，MAP仅1.5%。
3. 效率对比：全量SPICE需302.83小时，本框架仅133秒完成增量角预测，锚点取6/12时总耗时分别缩减42.8%、32.8%。
4. 曲面特性：连续改变电压，生成时序表光滑无断层，适配STA静态时序分析需求。
5. 扩展性：锚点数量提升至18后精度趋于饱和，海量105角场景仍稳定预测。

## 研究启发
1. 时序表可抽象为高维连续曲面，生成式模型比判别式FFN更擅长跨PVT外推预测。
2. 引入枢值作为条件特征，能大幅统一不同单元时序分布，实现单模型兼容全部时序弧。
3. 对抗自编码器可消除原生GAN随机噪声，保证时序数值连续性，满足EDA工业精度约束。
4. 基于聚类的锚点筛选能大幅削减SPICE仿真样本量，缓解角点爆炸算力瓶颈。
5. 仅使用公开时序查表、无需涉密晶体管网表，是第三方EDA时序表征可行技术路线。
