---
title: "GauRast: Enhancing GPU Triangle Rasterizers to Accelerate 3D Gaussian Splatting"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# GauRast: Enhancing GPU Triangle Rasterizers to Accelerate 3D Gaussian Splatting

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.16681">https://arxiv.org/abs/2503.16681</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件架构，图形处理器，3D高斯泼溅 </p>
</div>


---

## 研究概要
本文提出GauRast增强型GPU光栅器，复用现有三角形渲染硬件适配3DGS高斯光栅瓶颈运算。仅新增少量专用逻辑，芯片总面积开销仅0.2%。在Jetson Orin边缘平台测试，高斯核心运算提速23倍、能效提升24倍，原版3DGS端到端6倍加速，优化版4倍加速，分别达到24FPS、46FPS。

## 背景和动机
1. 3D高斯溅射(3DGS)渲染画质远超网格/NeRF，但10W级边缘GPU仅2~5FPS，无法满足AR/VR、自动驾驶实时需求。
2. 性能剖析显示高斯光栅步骤占总耗时80%以上，是核心瓶颈；现有加速方案均设计独立专用加速器，硬件成本、集成开销大。
3. 现代GPU内置高度优化三角形固定光栅单元，高斯与三角形光栅数据流高度相似，但原生硬件无法支持椭圆覆盖、多层色彩累加。
4. 独立加速器需配套专属存储与软件栈，难以兼容现有CUDA图形生态，无法复用成熟渲染管线。
5. 低功耗边缘SoC面积、功耗约束严苛，新增大规模专用硬件不具备落地可行性。

## 相关工作
1. 3DGS专用加速器GSCore：独立硬件架构，面积开销大，无法复用GPU原生光栅资源，兼容性差。
2. NeRF专用硬件：面向神经辐射场体渲染，与3DGS高斯原语计算逻辑不兼容，不能迁移。
3. GPU软件优化3DGS：完全依赖CUDA核心做高斯光栅，并行效率低，边缘设备算力受限。
4. 传统三角形光栅器设计：仅支持三角边界检测、单一深度保留，无高斯指数运算与多像素累加通路。
5. 通用图形硬件扩展研究：未针对3DGS高斯椭圆、透明叠加两大核心特性做定制改造。

## 本文解决方案
### 1 高斯/三角双模式可重构PE单元
复用光栅原有加法、乘法器，仅新增指数运算单元等少量高斯专用逻辑；三角、高斯渲染模式动态切换，完全兼容传统图形负载。
### 2 乒乓瓦片缓存架构
Tile A/B双缓冲交替存储高斯原语与像素数据，消除片外内存频繁访问，匹配两类光栅访存模式。
### 3 CUDA协同分层调度
投影、深度排序等轻量预处理交由CUDA核，耗时占比最高的高斯光栅全部卸载至GauRast硬件，软硬分工平衡负载。
### 4 统一输入输出数据通路
高斯与三角形原语输入均为9浮点参数，复用原有光栅存储、对齐模块，无需修改顶层GPU GPC架构。
### 5 极简硬件增量设计
单PE仅增加2加法、1乘法、1指数单元；整体增强逻辑仅占光栅单元21%，全SoC面积开销仅0.2%。

## 实验分析
1. 实验配置：28nm工艺，1GHz RTL综合，对标Jetson Orin NX基线、GSCore专用加速器，采用NeRF-360七类真实场景。
2. 核心运算指标：原版3DGS高斯光栅提速23倍、能效24倍；Mini-Splat优化版提速20倍、能效22倍。
3. 端到端帧率：原生3DGS平均24FPS，轻量化3DGS达46FPS，满足边缘实时渲染标准。
4. 面积对比：同等FP16性能下GauRast面积仅0.16mm²，比GSCore提升24.7倍面积效率。
5. 消融验证：复用原有光栅存储与算术单元是低面积开销关键，指数单元为高斯渲染不可缺失核心模块。

## 研究启发
1. 新兴神经渲染硬件加速无需从零搭建专用芯片，挖掘现有固定图形单元复用潜力可大幅降低成本。
2. 3DGS瓶颈在于光栅叠加计算，分层软硬协同调度能充分分离轻重计算负载，最大化硬件收益。
3. 原语计算数据流相似性是硬件复用基础，仅针对差异化运算增加少量专用电路即可兼顾兼容性与性能。
4. 边缘AI硬件设计需严控全局SoC面积增量，增量式扩展架构比独立加速器更适合嵌入式场景。
5. 高斯多层透明色彩累加、椭圆概率计算是区别传统光栅核心差异，硬件改造需针对性补充指数与累加通路。
