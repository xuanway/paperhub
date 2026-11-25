---
title: "SAGA: A Memory-Efficient Accelerator for GANN Construction via Harnessing Vertex Similarity"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SAGA: A Memory-Efficient Accelerator for GANN Construction via Harnessing Vertex Similarity

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133305">https://ieeexplore.ieee.org/document/11133305</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 图近似最近邻构建，内存高效加速器，顶点相似性，两级调度 </p>
</div>

---

## 研究概要
本文提出面向GANN图构建的内存高效加速器SAGA，利用顶点特征相似性设计聚类差分量化算法，搭配两级调度与串行进位PE硬件。针对动态建图场景规避传统预计算开销，在多ANN数据集验证，相较CPU/GPU/NDSearch平均提速9.30×/4.87×/4.15×，能耗分别降低35.46×/7.60×/5.15×，精度损耗极低。

## 背景和动机
1. 高维顶点GANN建图阶段图动态更新，距离计算占绝大多数耗时，且受DRAM带宽限制，存在严重内存瓶颈。
2. 现有NDSearch等加速器仅优化检索流程，动态建图需反复执行BFS重映射预处理，带来巨额时延开销，无法适配建图场景。
3. 顶点原始特征存储位宽高，邻近顶点差值数值范围窄，该数值冗余未被硬件架构利用，访存带宽浪费严重。
4. 图遍历存在空间局部性：相似顶点访问顶点集合高度重叠，现有架构顶点调度无序，片上缓存缺失率高。
5. 传统统一精度计算单元无法适配差分低位宽特征，缺少混合位宽距离计算专用硬件通路。

## 相关工作
1. NDSearch/SmartSSD：面向静态GANN检索加速器，依靠BFS离线重排优化SSD局部性，动态建图时预处理开销爆炸。
2 FAISS/cuHNSW：CPU/GPU通用ANN库，无专用硬件缓存与量化优化，高维数据访存瓶颈突出。
3. 通用图加速器：侧重图遍历、图神经网络，未针对ANN顶点差分、K近邻更新定制计算单元。
4. 低比特向量量化算法：仅软件层面压缩，无配套混合位宽距离计算硬件，压缩收益被计算开销抵消。
5. 近邻图优化算法：仅改进建图逻辑，不解决存储、访存硬件瓶颈，无法落地低功耗芯片。

## 本文解决方案
### 1 起点聚类相似度检测算法
复用建图起点选择中间结果，将共用同一起点的顶点划为一簇；起点设为关键顶点，其余为差分顶点，建立索引记录表区分两类顶点。
### 2 感知相似度差分混合量化
关键顶点8bit高精度存储，差分顶点仅存与关键顶点差值并压缩至2bit；重构内积、L2距离计算公式，复用关键顶点距离减少重复运算。
### 3 两级顶点调度优化
粗调度同簇顶点连续执行，提升缓存全局局部性；细调度交错差分计算，降低Delta Buffer替换缺失率，大幅削减DRAM访问。
### 4 混合位宽串行进位PE阵列
每个PE内置量化单元与距离引擎，配备局部部分和缓存PSB复用关键顶点距离；串行进位计算单元适配2bit差分、8bit关键特征混合运算。
### 5 完整SAGA硬件流水线
包含检测单元、4路PE阵列、图更新单元与分层片上缓存，支持聚类、量化、距离计算、K近邻双向连边全链路硬件加速。

## 实验分析
1. 实验环境：28nm 500MHz综合，cycle精准仿真；测试sift/gist/deep等5类ANN数据集，基线CPU FAISS、GPU cuHNSW、NDSearch。
2. 存储压缩：差分2bit量化，平均压缩比13~15倍，检索精度仅下降1%~1.8%，精度损失可控。
3. 速度与能耗：对比CPU平均提速9.30×，能耗降35.46倍；超越专用检索加速器NDSearch 4.15倍，能耗降低5.15倍。
4. 硬件开销：总面积1.26mm²，相比NDSearch缩减17.65%，功耗下降18.75%。
5. 消融实验：差分量化贡献3.04倍加速，两级调度提升1.92倍，二者协同可实现5.98倍整体提速。

## 研究启发
1. GANN建图与检索硬件需求完全割裂，检索优化方案不能直接迁移，需针对动态更新流程定制架构。
2. 利用图同质性挖掘顶点数值冗余，差分低位宽量化是缓解高维向量访存瓶颈低成本方案。
3. 相似顶点遍历路径高度重合，分层调度优化片上缓存局部性，可显著降低片外DRAM能耗。
4. 混合精度计算单元需配套重构距离公式，复用关键顶点中间结果抵消差分额外计算开销。
5. 复用算法原生中间步骤做相似度聚类，无需额外遍历预处理，避免动态图场景的重复计算损耗。
