---
title: "3D-TokSIM: Stacking 3D Memory with Token-Stationary Compute-in-Memory for Speculative LLM Inference"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# 3D-TokSIM: Stacking 3D Memory with Token-Stationary Compute-in-Memory for Speculative LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132883">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132883</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，近存处理，存内计算  </p>
</div>


---

## 研究概要
本文提出3D-TokSIM，面向投机解码LLM的3D堆叠存内计算架构。采用混合键合3D DRAM堆叠与Token驻留数据流CIM，配套输出缓存消除、残差缓存压缩优化。TSMC 22nm流片验证，相比RTX309吞吐量提升15.1倍、能效提升324倍，优于脉动阵列型近存方案。

## 背景和动机
1. LLM自回归解码存在严重内存墙，传统2D GPU内存带宽不足，单次生成token需加载全部模型，算力利用率不足25%。
2. 混合键合3D堆叠DRAM带宽、密度远优于2D，但现有硬件未适配投机解码并行校验流程，带宽优势无法释放。
3. 主流权重驻留CIM需频繁读写片上缓存，数据搬运能耗高，无法适配多token并行校验场景。
4. 投机解码k值增大后计算负载激增，易从内存瓶颈转为计算瓶颈，缺少软硬件协同平衡架构。
5. MHA/FFN残差连接、矩阵运算需大容量临时缓存，约束CIM计算资源，限制并行校验token数量。

## 相关工作
1. 3D近存PNM架构：基于混合键合提升带宽，多用于推荐、视觉模型，无LLM投机解码专属数据流设计。
2. 权重驻留CIM加速器：权重固定、频繁搬运token嵌入，多token并行场景缓存开销爆炸。
3. 脉动阵列AI加速：Gemmini等通用阵列计算密度低，部署投机解码易陷入计算瓶颈。
4. 投机解码算法：仅优化draft模型与校验逻辑，未配套底层硬件架构协同优化。
5. LLM专用PIM：侧重单层内存带宽提升，未解决多token并行带来缓存与算力失衡问题。

## 本文解决方案
### 1 3D堆叠跨栈整体架构
多层DRAM通过混合键合堆叠于逻辑die，32并行LLM核心，每核配套4片32MB DRAM Bank，片上NoC互联实现分布式权重划分，支持W4A16量化Llama2系列模型。
### 2 Token驻留CIM数据流创新
将多并行token嵌入常驻CIM单元，权重从3D DRAM串行输入运算；消除反复读写token缓存，相比权重驻留降低1.12~1.18倍归一化能耗。
### 3 并行校验硬件适配设计
CIM宏列数量匹配并行draft token数k，位串行乘法+加法树架构，单宏支持k+1组token并行矩阵乘，匹配IwR无额外draft模型投机算法。
### 4 两级缓存优化
1）计算写回解耦机制，运算时直接覆盖CIM输出区，移除独立输出缓存，CIM面积仅增8.4%；2）环All-Reduce拆分残差计算，单核心残差缓存压缩至1/(k+1)。
### 5 带宽-算力均衡建模
建立DRAM吞吐与CIM算力匹配方程，通过调整CIM宏行列数、子阵列规模，使内存读取速率与MAC运算速率对齐，消除瓶颈切换。

## 实验分析
1. 硬件环境：TSMC 22nm工艺，32核架构，单CIM簇3.25TOPS、9.51TOPS/W能效，总堆叠带宽2TB/s。
2. 数据流对比：同等面积下Token驻留EDP持续优于权重驻留，各k值能耗降低12%~18%。
3. 缓存优化：输出缓存完全消除，k≥5时残差缓存占用降至原16.7%以内，释放大量CIM计算资源。
4. 多模型适配：Llama2/OPT 2~4bit量化模型EDP提升1.13~1.23倍，最优k区间10~12。
5. 性能对标：Llama2-7B投机解码TPS达2797，较RTX3090提升15.1倍，能效提升324倍；比脉动阵列PNM吞吐量高1.5倍、能效高6.4倍。

## 研究启发
1. LLM解码内存墙不能仅靠提升带宽，需结合投机解码算法定制专用存内数据流实现软硬件协同。
2. Token驻留数据流更适配多token并行校验场景，权重驻留不适合投机解码高并行需求。
3. 缓存是制约并行draft数量关键瓶颈，通过计算写回、规约拆分可大幅削减缓存硬件开销。
4. 3D混合键合硬件优势需要算力-带宽均衡建模，否则会出现内存/计算瓶颈切换。
5. 面向大模型加速器不能照搬CNN视觉CIM设计，需针对MHA、残差、KV缓存做架构定制。




