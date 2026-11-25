---
title: "LLMShare: Optimizing LLM Inference Serving with Hardware Architecture Exploration"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# LLMShare: Optimizing LLM Inference Serving with Hardware Architecture Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://shipxu123.github.io/papers/C15-DAC2025-LLMShare.pdf">https://shipxu123.github.io/papers/C15-DAC2025-LLMShare.pdf</a></p>
<p class="paper-seo-summary__meta"><strong>海报链接:</strong> <a href="https://www.cse.cuhk.edu.hk/~byu/papers/C270-DAC2025-LLMShare-poster.pdf">https://www.cse.cuhk.edu.hk/~byu/papers/C270-DAC2025-LLMShare-poster.pdf</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型推理服务，硬件架构探索，设计空间探索，帕累托优化 </p>
</div>


---

## 研究概要
本文提出LLMShare硬件探索框架，针对Prefill、解码两阶段算力/内存需求差异，构建服务仿真器与多目标贝叶斯DSE。设计内存导向初始化、分层树核GP代理，以EHVI寻帕累托硬件配置。相比商用H100集群，成本降低13%，吞吐量提升4倍以上。

## 背景和动机
1. LLM推理分为计算密集Prefill、访存密集解码两阶段，统一GPU集群资源严重错配，硬件利用率低、部署成本高。
2. 现有LLM优化聚焦调度、KV内存软件优化，缺少面向整机硬件参数的自动化空间探索方案。
3. 设计空间规模达9×10¹⁴量级，暴力遍历硬件参数耗时极高，传统采样代理模型适配性差。
4. 通用DSE方法未感知大模型内存约束，初始样本代表性不足，代理无法建模硬件层级关联。
5. 商用A100/H10固定集群并非最优帕累托解，缺少分阶段异构硬件搭配的自动寻优工具。

## 相关工作
1. LLM软件调度优化（Orca、PagedAttention）：仅做批处理、KV内存管理，不探索底层硬件架构参数。
2. 分阶段推理Splitwise：提出Prefill/解码硬件分离思路，但无自动化硬件搜索框架。
3. LLMCompass：单硬件性能仿真工具，缺少多服务器集群联合寻优能力。
4. 传统架构DSE（DAC/ICCAD基线）：随机/TED初始化、通用核GP，不匹配LLM分层硬件树结构。
5. 通用贝叶斯优化SVR/XGBoost：无层级感知核函数，高维集群空间预测误差大。

## 本文解决方案
### 1 端到端LLM服务仿真器
分层建模服务器、GPU、片上缓存、脉动阵列全硬件参数；集成请求调度、批处理、KV缓存传输逻辑，仿真误差低于5%，输出时延与硬件总成本双指标。
### 2 内存导向初始化MCI
以集群总内存为分层划分依据，按内存分箱结合TED采样，生成覆盖成本-吞吐区间的代表性初始样本，解决随机采样分布失衡问题。
### 3 深度树核（DTK）高斯代理
针对服务器-设备-核-阵列树形硬件结构，自底向上递归嵌入各层级参数，精准建模硬件层级依赖，提升高维空间预测精度。
### 4 多目标贝叶斯优化
采用EHVI采集函数最大化帕累托超体积，迭代采样仿真更新GP代理，自动输出时延、成本均衡的最优硬件集群配置。
### 5 分池异构硬件搜索
分别独立搜索Prefill池、解码池硬件参数，支持两类池采用不同算力/内存规格加速器，匹配两阶段差异化负载。

## 实验分析
1. 实验环境：Azure真实2454条请求轨迹，GPT3-175B模型，对比SVR、DAC16、ASPDAC20、ICCAD21等DSE基线。
2. DSE指标：LLMShare相较基线ADRS降低7%~23%，帕累托超体积提升2%~5%，寻优解集更贴近真实最优前沿。
3. 消融实验：MCI初始化大幅降低前期ADRS；深度树核DTK显著减少预测偏差，两者缺一不可。
4. 集群对比：最优LLMShare异构配置对比统一H100集群，成本下降13%，吞吐量提升4.11倍。
5. 泛化性：海量硬件空间下仅少量仿真迭代即可收敛，无需暴力枚举全部硬件组合。

## 研究启发
1. LLM两阶段负载硬件需求完全割裂，分开搜索Prefill/解码硬件池是降本提吞吐核心思路。
2. 硬件参数具备天然树形层级关系，通用核函数无法刻画依赖，定制分层嵌入核可大幅提升代理预测精度。
3. HBM内存是LLM成本与吞吐核心变量，以内存分布指导初始采样，能大幅减少无效仿真开销。
4. 仅靠软件调度优化存在性能天花板，硬件架构空间探索可实现量级级吞吐量提升。
5. 多目标贝叶斯优化搭配EHVI适合集群硬件寻优，可自动平衡服务时延与硬件采购运维成本。