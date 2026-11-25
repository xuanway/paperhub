---
title: "GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing Redundant Sorting while Preserving Rasterization Efficiency"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing Redundant Sorting while Preserving Rasterization Efficiency


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2509.00911">https://arxiv.org/abs/2509.00911</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高斯泼溅，渲染，加速器</p>
</div>


---

## 研究概要
本文提出GS-TG瓦片分组3D高斯渲染加速器，解决瓦片尺寸带来的排序与光栅化性能权衡问题。采用大组排序、小瓦片光栅化+比特掩码复用排序结果，无损无需重训，可兼容现有优化。28nm硬件测试相较SOTA最高提速1.54倍，能效提升2.12倍。

## 背景和动机
1. 3D高斯溅射(3D-GS)渲染帧率难以满足AR/VR实时高帧需求，GPU运行速度存在明显瓶颈。
2. 瓦片渲染存在固有权衡：大瓦片减少冗余排序，但光栅化无效计算增多；小瓦片光栅化高效，排序重复计算严重。
3. 现有优化仅优化高斯包围盒判定，未解决该瓦片尺寸权衡矛盾，缺少软硬件协同的平衡方案。
4. GPU的SIMT架构难以并行完成掩码生成与分组排序，需要专用硬件加速器释放性能。

## 相关工作
1. 压缩类优化：量化、剪枝、稠密化等，需重训练补偿画质损失，属于有损优化。
2. 高斯包围盒优化：GSCore采用OBB、FlashGS使用椭圆边界，仅降低瓦片判定数量，未处理排序冗余。
3. 3D-GS硬件加速器GSCore：仅优化瓦片筛选，无法解决排序与光栅化的性能冲突，无瓦片分组复用机制。
4. 传统瓦片渲染：固定单一瓦片尺寸，无法同时兼顾排序与光栅化阶段效率。

## 本文解决方案
### 1. 瓦片分组渲染算法流水线
- 分组识别：将多个小瓦片合并为大分组，仅对分组整体做高斯筛选，大幅削减重复排序；
- 比特掩码生成：为每个高斯生成16bit掩码，标记分组内受影响小瓦片；
- 分层渲染：分组级深度排序，光栅化阶段依靠掩码复用排序结果，保留小瓦片光栅化优势。
### 2. GS-TG专用硬件架构
由预处理模块与GS-TG核心组成，核心包含三大并行单元：
1. BGM掩码生成单元：并行计算高斯覆盖瓦片，输出掩码；
2. GSM分组排序单元：多比较器并行完成分组深度排序；
3. RM光栅化单元：按掩码筛选高斯，多并行渲染单元完成α计算与融合。
### 3. 兼容特性
完全无损、无需模型微调，可搭配AABB/OBB/椭圆任意高斯边界算法使用。

## 实验分析
1. 软件GPU仿真：16小瓦片+64分组组合综合性能最优，椭圆边界搭配方案增益最高。
2. 硬件综合（28nm/1GHz）：总面积3.984mm²，功耗1.063W，多模块并行掩盖掩码生成开销。
3. 性能对比：相较基线几何平均提速1.33倍，最高1.58倍；优于GSCore最高1.54倍。
4. 能效提升：相比基线平均能效提升2.12倍，高分辨率场景优化幅度可达2.97倍。
5. 流水线收益：分组排序等价大瓦片开销，光栅化维持小瓦片高效水平，解决固有权衡矛盾。

## 研究启发
1. 3D-GS优化不能仅聚焦高斯边界判定，瓦片粒度带来的跨阶段性能权衡是核心优化靶点。
2. 分层分离计算思路：排序采用粗粒度分组、光栅化使用细粒度瓦片，配合掩码实现结果复用，兼顾两端性能。
3. GPU架构存在并行执行限制，针对渲染流水线定制专用硬件可充分释放分组算法收益。
4. 无损、兼容现有优化的设计具备工程落地优势，无需改动预训练模型，适配各类场景。
5. 渲染加速器模块化并行设计（掩码/排序/光栅分离），可单独扩展单元提升并行吞吐。