---
title: "Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rram"
  - "puf"
  - "reconfigurable"
  - "dnn-attack"
  - "side-channel"
---

# Re4PUF: A Reliable, Reconfigurable ReRAM-based PUF Resilient to DNN and Side Channel Attacks

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133290">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133290</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 阻变存储器，物理不可克隆函数，侧信道攻击，深度神经网络建模攻击，可重构 </p>
</div>


---

## 研究概要
本文提出Re⁴PUF，基于3T2R分压ReRAM单元的可重构物理不可克隆函数。互补双阻单元抑制温度、读噪声误差，通过调节逆变器电压实现无重编程轻量化重构。180nm流片验证，85℃下BER仅1%，抵御MLP/Transformer建模与探针侧信道攻击，建模成功率接近随机猜测。

## 背景和动机
1. 传统ReRAM PUF采用电流求和架构，受读噪声、高温电导漂移影响严重，85℃误码率可达11.5%，可靠性极差。
2. 现有可重构ReRAM PUF依赖反复SET/RESET改写阻态，带来巨大能耗、时延损耗，且器件耐久度有限。
3. 攻击者采集CRP对训练DNN（MLP/Transformer）可精准建模复刻PUF；探针读取电导的侧信道攻击同样极易破解。
4. 主流修复手段（时序投票、掩码）需额外外设，硬件开销大，且无法抵御建模与侧信道复合攻击。
5. 缺乏兼顾高可靠、低开销快速重构、双类攻击抗性一体化ReRAM PUF硬件方案。

## 相关工作
1. 电流求和型ReRAM PUF：依靠支路电流对比生成响应，温度噪声敏感，高温BER极高，无重构能力。
2. 可隐藏式ReRAM PUF：通过反复擦写阻态实现重构，编程能耗高、损耗器件耐久，可靠性无优化。
3. 时序投票/掩码加固PUF：仅降低误码，无法对抗DNN建模与探针侧信道窃取。
4. 3D堆叠ReRAM PUF：提升熵源但仍为电流比较架构，温度鲁棒性差，重构成本高。
5. 分压式基础存储单元：仅用于存内计算，未设计成支持挑战响应的PUF安全原语。

## 本文解决方案
### 1 3T2R互补分压基础单元
一对互补高低阻ReRAM构成分压电路，搭配晶体管与逆变器；单器件电导波动会相互抵消，从硬件底层抑制温度、读噪声带来响应偏差。
### 2 电压调控轻量化重构机制
不修改ReRAM阻态，仅切换源线逆变器供电电压（1.6/1.7/1.9/2.0V），改变分压判决阈值，生成全新CRP映射，重构无编程开销。
### 3 89位挑战分块译码架构
挑战分为块、行、列三段选择信号，并行激活两组存储块，两路输出多级异或生成单比特响应，扩大CRP熵空间。
### 4 三段标准化工作流
初始化随机置位所有ReRAM阻态；按需切换逆变器电压完成重构；输入挑战并行读取分压结果生成CRP对。
### 5 多维度安全评估指标
统一均匀度、唯一性、扩散度三大PUF标准评测维度，同时定义建模、侧信道两类攻击抗性量化指标。

## 实验分析
1. 流片平台：180nm工艺TaOx/HfOx ReRAM，Keysight半导体分析仪测试，对比主流电流型ReRAM PUF。
2. 可靠性：85℃高温下BER=1%，对比传统7.59%大幅下降；三万次读取仍保持稳定电导分布。
3. 重构性能：仅调节电压无需改写存储，消除SET/RESET能耗与时延，重构切换速度极快。
4. 安全抗性：MLP、Transformer建模准确率稳定50%（等同随机）；探针电导侧信道攻击预测准确率低于70%。
5. 标准指标：64/128bit密钥均匀度、唯一性、扩散度均贴近理想50%，PUF熵质量达标。

## 研究启发
1. 采用互补双阻分压单元可从硬件根源解决ReRAM PUF温度与读噪声可靠性痛点，无需复杂后处理电路。
2. 基于模拟电压阈值的重构方案，相比反复阻态擦写更轻量化，不损耗器件耐久，适合高频密钥更新场景。
3. 评估ReRAM PUF安全必须同时覆盖DNN建模与硬件探针侧信道两类威胁，单一防护存在漏洞。
4. 分压存内计算单元可复用改造为高可靠PUF，实现存储与安全原语硬件复用，缩减芯片面积。
5. 高温IoT设备硬件安全设计优先选用分压式ReRAM PUF，传统电流对比架构难以满足工业温区稳定性需求。