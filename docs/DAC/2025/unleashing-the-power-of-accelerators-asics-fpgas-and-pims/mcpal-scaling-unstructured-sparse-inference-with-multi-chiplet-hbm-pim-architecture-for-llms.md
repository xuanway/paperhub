---
title: "McPAL: Scaling Unstructured Sparse Inference with Multi-Chiplet HBM-PIM Architecture for LLMs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# McPAL: Scaling Unstructured Sparse Inference with Multi-Chiplet HBM-PIM Architecture for LLMs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132914">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132914</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高带宽存储器，芯粒，大语言模型，非结构化稀疏性，存内处理</p>
</div>


---


## 研究概要
本文提出McPAL多芯粒HBM存算一体架构，面向大语言模型非结构化稀疏推理。设计稀疏矩阵分解与双缓冲蝶形网络适配无规则权重，结合3D垂直、2.5D水平分层芯粒扩展方案。在Llama系列模型测试中，相较A100最高提速3.12倍、能效提升35.66倍，优于现有主流加速器。

## 背景和动机
1. 大模型推理访存密集，GPU受内存墙制约；PIM存算一体可缓解带宽瓶颈，但单片容量无法承载超大LLM权重。
2. 现有PIM仅支持块/通道结构化稀疏，结构化剪枝会损害模型精度，非结构化稀疏无法适配规整交叉阵列，硬件利用率低。
3. 现有多芯粒PIM采用环形广播同步KV缓存，长序列下片间传输开销巨大，且无法均衡稀疏任务负载，缺少分层协同优化方案。

## 相关工作
1. 单芯片PIM加速器：仅支持结构化稀疏，难以处理无规则权重，未针对LLM线性层稀疏计算做硬件适配。
2. 早期HBM-PIM（TransPIM）：权重全复制、环形同步KV缓存，长文本下片间数据传输开销极高。
3. 通用芯粒加速器：面向稠密矩阵运算，未设计稀疏负载均衡与专用片间同步机制。
4. GPU稀疏方案：稀疏张量核仅支持规则稀疏，解码阶段硬件利用率不足1%。

## 本文解决方案
### 1. 非结构化稀疏存算内核
- 稀疏矩阵分解(SMD)：拆分任意稀疏矩阵为标准M:N稀疏向量，匹配蝶形网络带宽上限；
- 双缓冲蝶形网络DB²FLY：双通路并行调度稀疏通道，解决高稀疏度下MAC利用率不足问题；
- 统一稀疏解码流水线，无需修改PIM基础交叉阵列。

### 2. 3D垂直HBM分层扩展
四层堆叠HBM架构，存储、计算分层排布；在存储裸片内置PE、全局总线控制器，KV缓存本地复用，减少TSV长距离传输，内置RoPE、量化、累加单元。

### 3. 2.5D IO芯粒水平扩展
专用IO芯粒负责跨芯粒同步与负载均衡：单发射多路广播替代环形传输降低D2D开销；交叉置换网络重排稀疏输出，均衡各HBM-PIM计算负载，统一完成归一化、残差等辅助运算。

## 实验分析
1. 硬件开销：28nm工艺，PIM内核仅增加6.8%HBM裸片面积，单芯粒峰值2.048TOPS，D2D采用256Gb/s UCIe标准。
2. 稀疏收益：50%非结构化稀疏下接近2倍理论加速，稀疏度越高DB²FLY优化效果越明显。
3. 对比A100：稠密版平均提速1.57~1.95倍，稀疏版最高3.12倍；能效提升10.43~35.66倍，解码阶段优势极大。
4. 对比SOTA（CXL-PNM、AttAcc）：稀疏McPAL吞吐量1.08~2.15倍，能效1.65~5.14倍，无需GPU协同，片间通信开销更低。
5. 芯粒规模：超过4颗HBM-PIM时，IO芯粒广播同步能耗远优于环形拓扑。

## 研究启发
1. LLM存算一体不能仅优化稠密矩阵，必须配套硬件原生非结构化稀疏处理机制，兼顾压缩率与推理精度。
2. 超大模型需要3D堆叠+2.5D芯粒混合分层扩展，分层分担KV缓存、线性层、归一化等不同算子，降低跨层传输。
3. 环形同步不适用于长序列KV缓存，专用IO芯粒集中广播可大幅削减芯粒间通信能耗。
4. 稀疏负载天然不均衡，需在片间增加置换重排硬件，避免单芯粒拖慢整体推理吞吐。
5. 算子下沉至HBM存储裸片本地处理，减少逻辑裸片与存储裸片间TSV数据搬运，显著提升能效。