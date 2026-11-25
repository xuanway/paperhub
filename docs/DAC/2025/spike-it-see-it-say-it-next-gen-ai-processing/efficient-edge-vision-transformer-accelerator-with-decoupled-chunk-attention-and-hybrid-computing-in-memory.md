---
title: "Efficient Edge Vision Transformer Accelerator with Decoupled Chunk Attention and Hybrid Computing-In-Memory"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Efficient Edge Vision Transformer Accelerator with Decoupled Chunk Attention and Hybrid Computing-In-Memory


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132426">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132426</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 视觉Transformers，存内计算，边缘AI加速器，密集预测</p>
</div>

---

## 研究概要
本文面向边缘像素级密集预测任务，提出算法硬件协同ViT加速器。算法设计解分块注意力DCA降低访存；硬件融合RRAM+SRAM混合CIM，搭配串并行融合调度、双向可重构CIM宏。SegFormer测试最高提速217.1倍，访存缩减1.7~7.4倍，能效提升1.8倍，精度损失不足1%。

## 背景和动机
1. 密集预测ViT序列最长达16384，自注意力二次复杂度，片上存储不足，频繁片外读写带来巨大时延能耗。
2. 金字塔ViT各层矩阵尺寸差异大，固定硬件数据流资源利用率极低，现有CIM架构无法适配多变矩阵规模。
3. 纯SRAM-CIM权重需从片外加载，RRAM-CIM不适合动态注意力高精度计算，单一存储CIM各有短板。
4. 现有稀疏注意力、CIM加速器仅单独优化算法或硬件，未协同解决超长序列与金字塔负载失衡双重难题。

## 相关工作
1. 软件稀疏注意力（FlashAttention等）：仅分块优化访存，未适配金字塔ViT不均衡负载，无配套CIM硬件。
2. RRAM类Transformer CIM：高密度存权重，但随机动态注意力计算精度差，写开销高。
3. 纯SRAM数字CIM：计算无损但权重需片外载入，唤醒延迟高，缺少混合存储架构。
4. 现有ViT专用加速器：仅支持短序列图像分类，无法处理上万Patch密集预测任务，硬件复用率低。

## 本文解决方案
### 1. 解耦分块注意力DCA算法
重排图像Patch聚合空间相关Token，将注意力矩阵形成对角稀疏块；流水线分块计算QKV，注意力稀疏度87.1%，FLOPs减少56.9%，精度损耗<1%。
### 2. RRAM-SRAM混合CIM架构
4MB RRAM片上固化静态权重，SRAM-CIM负责动态注意力矩阵乘；彻底消除权重片外读取，片上缓存存储中间特征。
### 3. 串并行融合调度SPMF
依据各层矩阵尺寸动态切换串行/并行算子执行，并行转发中间结果消除缓存读写，均衡金字塔各层不均衡算力负载。
### 4. 双向可重构BE-TWR CIM宏
可切换单比特高并行/多比特低并行累加模式，适配大小矩阵运算，提升全层级硬件利用率。

## 实验分析
1. 实验配置：28nm工艺250MHz，SegFormer-B0，COCO/ADE20k/NYUDV2三大密集预测数据集，对比GPU、纯SRAM-CIM基线。
2. 算法效果：DCA仅平均精度下降0.7%，注意力计算量减半，大幅削减中间特征存储需求。
3. 性能加速：各模块提速18.5~217.1倍，片外访存完全消除，片上访存降低1.7~7.4倍。
4. 硬件指标：芯片面积10.54mm²，峰值功耗834mW，INT8算力6.55TOPS，相较TranCIM/P³ViT能效提升1.8倍。
5. 消融验证：DCA、混合存储、可重构宏、融合调度四模块叠加才能达到最优吞吐与能效。

## 研究启发
1. 面向边缘密集预测不能仅优化硬件，需从图像空间特性设计稀疏注意力，从源头降低计算与访存压力。
2. RRAM与SRAM具备互补优势，混合CIM架构可同时解决静态权重加载、动态高精度矩阵乘两大痛点。
3. 金字塔ViT负载天然不均衡，固定数据流会严重浪费算力，动态串并行融合调度是提升利用率关键。
4. CIM阵列需支持多尺寸矩阵可重构累加，才能适配分层变化的特征维度。
5. 超长视觉序列瓶颈是片上存储容量，空间感知分块稀疏是远优于通用注意力分块的优化思路。
