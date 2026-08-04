---
title: "DBC: Drift-aware Binary Code for Drift-tolerant Deep Neural Networks"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DBC: Drift-aware Binary Code for Drift-tolerant Deep Neural Networks


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132851">https://ieeexplore.ieee.org/document/11132851</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>深度神经网络，新兴存储器，相变存储器，电导漂移，容错 </p>
</div>


---

## 研究概要
本文提出DBC漂移感知二进制编码，适配真实IBM MLC PCM器件。将小数值映射至低漂移可靠单元层级，搭配SCSR单符号单元支持有符号DNN权重，无需辅助比特，可兼容ECC。多视觉、NLP、大模型测试，相比传统格雷码最高提升55.18倍漂移耐受度。

## 背景和动机
1. MLC PCM具备高密度优势，但电导漂移会改变存储权重，引发DNN推理精度大幅衰减。
2. 现有容错编码基于理论PCM解析模型，与IBM实测真实器件漂移特性完全不符，高电导高层误差最严重。
3. DNN权重服从高斯分布，绝大多数为小幅值数值，传统编码未利用该分布优化存储层级分配。
4. 已有Flipcy、DynaPAT方案需要额外辅助比特，带来存储、编解码硬件额外开销，难以和ECC协同。

## 相关工作
1. Tri-level-cell：删减易出错中间电平，仅适配理论PCM模型，真实器件高层漂移问题无法解决。
2. Flipcy：通过比特取反重分配数据，依赖辅助比特，不适用于真实PCM高电平漂移场景。
3. DynaPAT：动态权重层级映射，同样需要辅助存储单元，硬件开销大，适配理论模型。
4. 传统反射格雷码RBC：均等分配数值至各存储层级，大量小权重存入高漂移高层，漂移容错极差。

## 本文解决方案
### 1. DBC分层编码生成算法
按单元可靠性优先级分配数值：低漂移低层存储小十进制数，高层分配大数；分三阶段生成完整码字，保证漂移仅让数值单向变小，契合DNN容错特性。
### 2. SCSR单单元符号编码
新增1个PCM单元表征正负号，低层代表正数，高层代表负数，漂移不会出现正负翻转，大幅降低符号位错误概率。
### 3. 无辅助比特编解码硬件
内存控制器集成8bit粒度编解码单元，64B缓存线并行处理，无需额外存储辅助位，可后置串联ECC纠错模块。
### 4. 真实PCM器件仿真建模
基于IBM实测噪声、漂移参数构建仿真器，精准复现高层电导持续衰减的真实器件特征。

## 实验分析
1. 测试模型：VGG/ViT/RoBERTa/Llama/Gemma等8bit量化网络，采用真实PCM漂移仿真平台，28nm综合硬件。
2. 精度保持：RBC基准下降5%精度仅百秒左右，DBC在QQP任务漂移耐受提升55.18倍，视觉模型平均提升7倍，LLM提升3.08倍。
3. 错误率：相同时长下DBC单元软错误率仅7.16%，远低于RBC、Flipcy、DynaPAT；同等精度阈值下可承受更高单元错误率。
4. 硬件开销：编解码面积、能耗高于RBC，但低于Flipcy；无辅助比特节省系统级存储开销，延迟优于同类容错方案。

## 研究启发
1. PCM容错编码不能依赖理论器件模型，必须基于真实硬件漂移特性设计层级映射策略。
2. DNN权重高斯分布是核心优化抓手，把占比最高的小权重分配至低漂移底层可大幅降低整体错误。
3. 让漂移仅造成权重数值单向衰减，相比数值随机跳变能显著缓解精度损失。
4. 舍弃辅助比特的编码方案，虽小幅增加编解码电路开销，但系统存储收益更大，且兼容ECC。
5. 符号位单独分配可靠低层单元，可避免漂移引发正负权值翻转这一灾难性推理错误。