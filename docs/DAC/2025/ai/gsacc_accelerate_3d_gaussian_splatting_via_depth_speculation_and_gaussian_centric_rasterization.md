---
title: "GSAcc: Accelerate 3D Gaussian Splatting via Depth Speculation and Gaussian-centric Rasterization"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# GSAcc: Accelerate 3D Gaussian Splatting via Depth Speculation and Gaussian-centric Rasterization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133032">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133032</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 3D高斯泼溅，软硬件协同设计，加速器架构，辐射场渲染 </p>
</div>

---

## 研究概要
本文提出软硬件协同加速器GSAcc面向压缩3DGS渲染，设计帧深度推测复用时序信息，高斯中心数据流消除中间存储，搭配并行排序与瓦片驻留光栅硬件。16nm工艺综合，相比RTX8000 PPA提升16600倍、节能48.7倍；超越SOTA GSCore，PPA提升2.3倍、单帧能耗降低2.9倍。

## 背景和动机
1. 原始3DGS分为预处理、排序、光栅串行三阶段，阶段间需存储海量高斯中间数据，片外访存开销巨大，不适合AR/VR边缘低功耗设备。
2. GPU与GSCore加速器流水线串行度高，预处理未完成无法启动光栅，并行度不足，吞吐受限。
3. 传统瓦片中心光栅遍历每图块全部高斯，访存冗余；相邻帧相机小幅运动时深度排序信息可复用，但现有方案未利用时序相关性。
4. 主流GSCore仅拆分排序阶段并行，仍需等待整帧预处理完成，无法实现全流程并发。
5. 高斯覆盖图块数量极少，但现有硬件未利用瓦片重叠局部性，片上缓存利用率偏低。

## 相关工作
1. GPU优化方案（FlashGS、CompGS）：仅软件层面压缩高斯、优化CUDA核，受通用GPU架构限制，能效、面积表现差。
2. 专用硬件GSCore：首个3DGS独立加速器，仅拆分排序分块并行，预处理与光栅仍串行，无帧时序复用优化。
3. 3DGS压缩算法（LightGaussian、CompGS）：侧重模型参数量量化压缩，不解决渲染流水线硬件瓶颈。
4. NeRF专用加速器：面向体素积分渲染，高斯椭圆投影、Alpha混合逻辑不兼容，无法迁移至3DGS。
5. 传统图形光栅硬件：仅适配三角形原语，无高斯协方差、球面谐波着色专用计算通路。

## 本文解决方案
### 1 高斯深度推测机制
复用前一帧高斯深度与排序结果作为当前帧预排序基准；相机4倍标准运动下画质衰减低于1%，预处理、排序可同步启动，打破串行依赖。
### 2 高斯中心交错数据流
摒弃瓦片中心遍历，按单个高斯处理所有相交图块，无需缓存整帧预处理结果，消除海量中间存储开销；相邻高斯瓦片重叠度11.4%。
### 3 两级流水线排序硬件
32路双调排序+四路归并排序架构，搭配片上归并缓冲区，分块流水排序，减少DRAM读写。
### 4 瓦片驻留光栅优化
设计专用瓦片缓存，保留相邻高斯重叠瓦片像素数据，大幅降低重复片外访存；16路并行光栅核单周期输出16像素。
### 5 模块化GSAcc硬件架构
分为预处理单元、剔除排序单元、16核光栅单元与共享高斯缓存，集成4组MAC树、指数/平方根专用算术单元，适配压缩码本解码全流程。

## 实验分析
1. 实验环境：Intel 16nm工艺500MHz，RTL综合，对比RTX8000、GSCore；评测Train/Truck/Playroom/Drjohnson四类CompGS压缩场景。
2. PPA指标：相较GPU平均PPA提升13500倍，最高达16600倍；对比GSCore平均提升1.41倍，峰值2.3倍。
3. 能耗表现：单帧能耗相较GPU平均降低39.8倍，最高48.7倍；比GSCore节能1.74~2.9倍。
4. 消融实验：深度推测提速4%~5%；预处理光栅交错带来最大增益；瓦片驻留额外提升5%性能并减少访存能耗。
5. 硬件开销：总芯片面积0.3913mm²，总功耗0.4085W，光栅模块占面积功耗主体。

## 研究启发
1. 沉浸式3D渲染帧间时序相关性极强，复用前帧深度排序信息可彻底打破流水线串行壁垒，实现全阶段并行。
2. 原语中心数据流远优于瓦片中心，可省去全量中间特征存储，大幅降低片外内存压力。
3. 相邻高斯瓦片局部性可通过小型片上缓存挖掘，是低功耗边缘加速器关键优化点。
4. 排序是3DGS核心瓶颈，两级分层片上排序硬件可显著降低外部DRAM交换频次。
5. 面向AR/VR边缘场景，不能复用通用GPU架构，算法数据流与硬件单元协同设计才能极致平衡PPA。
