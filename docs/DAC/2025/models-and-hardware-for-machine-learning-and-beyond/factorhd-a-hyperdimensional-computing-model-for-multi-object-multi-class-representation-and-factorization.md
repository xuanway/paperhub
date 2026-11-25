---
title: "FactorHD: A Hyperdimensional Computing Model for Multi-Object Multi-Class Representation and Factorization"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# FactorHD: A Hyperdimensional Computing Model for Multi-Object Multi-Class Representation and Factorization


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2507.12366">https://arxiv.org/abs/2507.12366</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>超维计算，类-子类关系，因子分解，符号编码，神经符号人工智能 </p>
</div>


---

## 研究概要
本文提出FactorHD超维计算模型，面向多对象多层级类-子类分层表征与因式分解。设计捆绑-绑定三层编码规避叠加灾难、二值问题，配套阈值筛选分解算法，复杂度降至O(N_M)。基准测试最高提速5667倍，结合ResNet-18在Cifar-10上因式精度达92.48%。

## 背景和动机
1. 现有HDC分为C-I、C-C两类，仅支持单层类关系，无法处理多层级类-子类分层结构。
2. 多对象编码时存在“叠加灾难”“二值问题”，子类向量混合无法区分，造成信息丢失。
3. 传统因式分解需遍历全部子类组合，复杂度呈指数级，规模扩大后算力爆炸。
4. 现有模型必须完整分解全部子类，无法按需提取目标子集，存在大量无效相似度计算。

## 相关工作
1. C-I类HDC模型：绑定类与实例，局部分解高效，但多对象叠加会发生叠加灾难。
2. C-C类HDC（谐振网络、IMC因式器）：支持多对象，但分解需遍历全部组合，指数复杂度，效率极低。
3. 通用向量符号架构：仅单层编码，不支持多级子类分层，适配复杂分层推理能力弱。
4. 神经符号融合网络（MIMOConv）：侧重图像叠加训练，无分层超维编码优化。

## 本文解决方案
### 1. 三层捆绑-绑定符号编码
新增冗余类标签，同层子类捆绑、不同大类绑定、多对象外层捆绑；内置NULL空向量，无需预知对象所含类别，从根源解决叠加灾难与二值问题。
### 2. 分层阈值式因式分解算法
先解绑无关大类，仅对相似度高于阈值的子类做组合匹配；逐层向下检索，重建目标对象向量并剔除，无需全局穷举。
### 3. 最优阈值拟合公式
基于向量维度、对象数、子类规模拟合最优TH阈值，稳定控制分解精度，规避基线模型阈值调参难题。
### 4. 神经符号融合流水线
ResNet-18提取图像特征后映射为超向量，FactorHD完成分层因式推理，适配图像分类、类比推理数据集。

## 实验分析
1. 对比基准：谐振网络、IMC因式器、传统C-I模型；测试Rep1/2/3三类分层表征，RAVEN/CIFAR10/100数据集。
2. 算力性能：问题规模10⁹时相对IMC提速5667倍，复杂度由指数降为线性，精度维持99%以上。
3. 分层表征：单对象多层D=1000精度近100；双对象多层需更高维度，仍显著优于基线。
4. 数据集效果：RAVEN多图推理最高100%精度；Cifar-10单输入因式精度92.48%，相比原生ResNet仅损失2.41%。
5. 消融对比：缺少冗余类标签或阈值筛选，叠加灾难复现，分解算力暴涨、精度大幅下滑。

## 研究启发
1. 传统两层绑定/捆绑结构不足以表达多级类层次，三层嵌套编码是解决分层表征的核心思路。
2. 指数穷举分解是HDC性能瓶颈，阈值筛选+逐层检索可把复杂度压缩至线性区间。
3. 固定阈值泛化性差，通过维度、样本规模拟合最优阈值能稳定兼顾分解速度与准确率。
4. 冗余类标签可作为分离标识，有效抑制多对象叠加带来的向量混淆失真。
5. HDC可与CNN深度融合，用超维因式替代传统分类器，实现可解释神经符号分层推理。
