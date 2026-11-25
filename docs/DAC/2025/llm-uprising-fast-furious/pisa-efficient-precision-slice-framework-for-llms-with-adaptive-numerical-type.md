---
title: "PISA: Efficient Precision-Slice Framework for LLMs with Adaptive Numerical Type"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PISA: Efficient Precision-Slice Framework for LLMs with Adaptive Numerical Type

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132980">https://ieeexplore.ieee.org/document/11132980</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 精度切片框架，早期预测机制，大语言模型，硬件加速器 </p>
</div>

---

## 研究概要
本文提出PISA精度切片LLM推理框架，将16bit数据拆分为4bit高位+12bit低位，利用高位天然稀疏设计Early Bird早停机制，可跳过低贡献计算。硬件采用无编解码交错脉动阵列，兼容传统加速器。在BERT、LLaMA等模型测试，较主流方案提速1.3~4.3倍，能耗降低14.3%~66.7%，精度损失极小。

## 背景和动机
1. LLM激活存在少量幅值离群值，直接4bit量化精度暴跌，传统混合精度需分离存储离群，带来复杂编解码与非对齐访存开销。
2. INT16权重/激活高位存在大量零稀疏，现有量化方案未挖掘比特层级冗余，存储与算力浪费严重。
3. OLAccel、GOBO、OliVe等离群加速器依赖专用编解码模块，编解码耗时占总推理20%，抵消压缩收益。
4. 现有混合精度硬件需区分正常/离群两条计算通路，控制逻辑复杂、芯片面积开销大。
5. 缺少比特拆分+动态计算跳过协同的软硬件协同方案，无法同时兼顾精度、硬件规整度与算力削减。

## 相关工作
1. GO/OLAccel：分离存储离群与普通数值，使用坐标索引列表，内存访问不连续，控制逻辑复杂。
2. OliVe：离群-配对局部存储优化访存对齐，但硬件需全域拓展高精度通路，面积损耗高。
3. AdaFloat：层级动态裁剪数值范围，依赖浮点计算，低位算力收益有限。
4. ANT：基于2的幂自适应数值类型，未挖掘高位稀疏，无动态计算跳过机制。
5. 通用LLM后量化算法（GPTQ/SmoothQuant）仅优化数值分布，无配套硬件协同加速设计。

## 本文解决方案
### 1 4-12比特非均衡精度切片算法
统一量化至INT16后拆分4bit高位段、12bit低位段；高位具备超高稀疏度，12bit可三等分4bit单元，天然适配4bitPE阵列，无需复杂对齐转换。
### 2 Early Bird早停计算机制
优先执行高位乘累加，与阈值对比；结果低于阈值直接使用层优化预设值，跳过全部低位计算，大幅削减无效乘加操作。
### 3 层级阈值与预设值调优
离线验证集二分搜索每层最优阈值、特征均值附近微调预设值，平衡跳过比例与困惑度损失，线性层可统一设0简化部署。
### 4 无编解码交错存储硬件架构
高低比特分段独立缓存，计算时交错送入PE；仅增加简单比较器，舍弃编解码单元，适配标准脉动阵列，硬件改动极小。
### 5 分层流水线执行流程
数据切片→权重预分片缓存→高位先行计算+阈值判断→有效项完整四则累加→分段归并输出，全程规整4bit并行运算。

## 实验分析
1. 实验环境：45nm 500MHz RTL综合，CACTI建模缓存；测试BERT、GPT2、OPT、LLaMA，基线AdaFloat/GOBO/OliVe/ANT。
2. 精度表现：各类模型困惑度仅小幅上涨，截断离群精度衰减问题得到显著缓解。
3. 性能加速：相较OliVe平均提速1.3×，对比GOBO达2.19×，最大提升4.31×。
4. 能耗与面积：平均能耗比OliVe低14.3%，比GOBO低44.5%；仅新增少量比较器，核心面积优于同类加速器。
5. 消融验证：Early Bird是提速核心，层级调优阈值可提升90%+计算跳过率，几乎无损精度。

## 研究启发
1. LLM量化优化不能只关注数值分布，比特高位天然稀疏是极易被忽视的算力压缩突破口。
2. 传统离群分离方案的编解码开销抵消加速收益，无额外编解码的比特拆分架构硬件更友好。
3. 高位乘加结果可表征计算重要性，提前阈值判断动态跳过低贡献运算是高效轻量优化手段。
4. 非均衡4/12bit拆分兼顾稀疏利用与硬件4bit计算单元适配，平衡压缩率与PE并行效率。
5. 分层定制阈值、预设值可精准平衡推理速度与生成/分类精度，统一固定参数会造成明显性能损耗。