---
title: "SynGPU: Synergizing CUDA and Bit-Serial Tensor Cores for Vision Transformer Acceleration on GPU"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SynGPU: Synergizing CUDA and Bit-Serial Tensor Cores for Vision Transformer Acceleration on GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132753">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132753</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 视觉Transformer加速，位稀疏性，张量核心协同，算法-硬件协同设计 </p>
</div>

---

## 研究概要
本文提出SynGPU软硬件协同框架，面向ViT挖掘token间比特稀疏，设计IBA差分稀疏提取与BSDP位串行点积算法；配套新型数据映射与BSTC位串行张量核，解决CUDA/Tensor核寄存器带宽争抢、浮点指数不统一难题。对比A100，图像/视频ViT平均提速2.15~3.95倍，计算密度提升2.49~3.81倍。

## 背景和动机
1. ViT自注意力存在二次时空复杂度，现有加速仅裁剪数值稀疏token，完全未利用像素差分带来大量零比特的比特级冗余。
2. A100流式多处理器内CUDA核与Tensor核共享寄存器堆，张量核占用91.6%寄存器带宽时CUDA核闲置，并行能力无法释放。
3. 传统张量核并行点积无法适配比特稀疏计算，浮点数向量指数差异大，固定点位串行架构难以统一支持浮点/定点乘累加。
4. 原生张量核数据复用差，重复读写寄存器加剧带宽拥堵，比特稀疏硬件算力利用率偏低。
5. 缺少算法与GPU微架构协同方案，无法同时挖掘比特稀疏并实现两类计算单元全并行。

## 相关工作
1. Token剪枝类ViT加速(DynamicViT/ViTCoD)：仅利用数值层面token冗余，忽略差分比特稀疏，算力上限有限。
2. Bitlet位串行硬件：支持低位宽浮点，但定点场景硬件利用率低，未适配ViT token差分特征。
3. 标准A100张量核：并行全比特计算，无法跳过零比特，稀疏场景周期无缩减。
4. 通用位稀疏加速器：无GPU CUDA/Tensor核协同设计，不兼容现有GPU微架构。
5. 低比特量化推理：仅压缩权重，不挖掘注意力中间特征的动态比特稀疏。

## 本文解决方案
### 1 IBA跨token比特稀疏提取算法
间隔选取关键token，计算其余token与最相似关键token的差分矩阵，大幅提升矩阵零比特占比；乘累加后依据线性特性无损还原原始注意力输出，全程无精度损失。
### 2 BSDP位串行点积算法
定点模式将数据转为比特索引，移位累加跳过所有零比特；浮点模式新增指数对齐模块，统一向量最大尾数位宽后执行位串行乘，最后合并全局指数恢复标准浮点结果。
### 3 寄存器友好数据映射机制
扩大张量核片上缓存，单次载入完整计算分块，串行位计算阶段释放寄存器带宽给CUDA核；矩阵分块并行计算，消除重复寄存器读写，解决带宽竞争。
### 4 BST位串行张量核
浮点预处理单元完成指数对齐、比特编码；BSDP阵列并行执行移位累加；增设重排模块均衡矩阵比特密度，消除稠密比特行拖慢整体计算的瓶颈。
### 5 完整软硬件协同流水线
CUDA核执行IBA差分稀疏提取，BSTC负责稀疏乘累加，两类单元并行工作；重排模块实时均衡输入稀疏度，兼顾吞吐与访存效率。

## 实验分析
1. 实验环境：28nm工艺综合，Accel-Sim周期级仿真；测试DeiT、TimeSformer等图像/视频ViT，基线A100原生张量核。
2. 稀疏增益：token差分后FP16比特稀疏度50.19%→65.98%，INT8达50.48%→75.82%，零比特计算大量省略。
3. 速度指标：无重排平均提速2.15~2.2倍，搭配矩阵重排最高3.95倍；INT8计算密度3.81倍优于A100。
4. 能效表现：FP1能效提升1.84倍，带重排INT8能效提升2.68倍，零比特跳过削减动态功耗。
5. 硬件开销：BSTC总面积仅小幅高于原生张量核，重排模块面积占比不足1.5%，硬件成本可控。

## 研究启发
1. ViT加速不止局限token数值剪枝，相邻token差分带来的比特稀疏具备更大算力优化空间。
2. GPU内CUDA与Tensor核寄存器资源冲突是关键瓶颈，重构数据复用逻辑才能实现两类单元完全并行。
3. 位串行计算需配套浮点指数对齐，才可同时兼容浮点、定点稀疏乘累加，适配ViT混合精度推理。
4. 比特密度不均衡会严重拖累位串行阵列，轻量级矩阵重排模块可低成本均衡负载、大幅提速。
5. 面向GPU的ViT优化必须算法与微架构协同，仅做软件稀疏无法释放张量核硬件算力潜力。
