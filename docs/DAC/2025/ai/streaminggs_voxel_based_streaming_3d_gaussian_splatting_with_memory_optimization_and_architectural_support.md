---
title: "StreamingGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# StreamingGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2506.09070">https://arxiv.org/abs/2506.09070</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 3D高斯泼溅，渲染，加速器 </p>
</div>


---

## 研究概要
本文提出软硬件协同STREAMINGGS框架，针对传统分块式3DGS渲染片外DRAM流量过高、移动端无法达到90FPS VR实时需求问题，改用体素为中心流式渲染范式，搭配双层分层过滤、向量量化与边界微调算法；配套专用加速器含VSU体素排序单元、HFU分层滤波单元。在多场景测试，渲染PSNR几乎无损，相比Orin NX移动GPU提速45.7倍、能耗降低62.9%，超越SOTA GSCore加速器2.1倍速度、2.3倍能效。

## 背景和动机
1. 3D高斯溅射(3DGS)是主流神经渲染方案，但Jetson Orin NX等移动设备仅能跑到2~9FPS，达不到VR/AR 90帧实时标准。
2. 传统瓦片中心渲染范式，投影、排序阶段反复读写片外内存，中间数据DRAM流量占总流量85%，远超移动端带宽上限。
3. 现有3DGS加速器仅优化计算吞吐，未解决访存瓶颈，真实复杂场景带宽依然溢出。
4. 单瓦片处理跨体素高斯会产生深度排序错乱，直接体素渲染存在渲染顺序失真问题。
5. 同一体素内存在大量无关高斯，完整加载全部体素数据会带来额外DRAM传输开销。

## 相关工作
1. 原生3DGS/MiniSplatting/LightGaussian：仅优化高斯数量、轻量化模型，未重构渲染访存流水线，片外流量瓶颈未解决。
2. GSCore：首个3DGS专用加速器，优化排序与渲染计算单元，但仍采用瓦片渲染，中间数据频繁读写DRAM。
3. 神经渲染加速器(Seele/Potamoi)聚焦NeRF类模型，不兼容高斯椭球稀疏表示的3DGS管线。
4. 高斯压缩算法：仅离线压缩模型参数，运行时投影排序访存冗余依旧存在，无法缓解推理带宽压力。
5. 移动端GPU渲染管线：无片上分层滤波、体素级调度硬件，大量无效高斯参与完整计算，带宽浪费严重。

## 本文解决方案
### 1 体素中心全流式渲染范式
将场景切分三维体素，按体序逐批处理，投影/排序/渲染中间结果全部驻留片上SRAM，消除阶段间片外读写；最终仅写完整像素结果回DRAM，根除85%中间流量。
### 2 边界感知微调修复跨体素排序失真
新增跨边界惩罚损失，约束高斯尺寸、朝向，减少跨体素高斯占比至0.4%，避免体素遍历造成深度混合渲染失真，PSNR损失控制在0.04dB以内。
### 3 双层分层高斯过滤机制
粗过滤仅加载4维坐标尺度快速剔除无关高斯；通过向量量化压缩剩余特征，仅从DRAM读取码本索引，体素加载流量降低92.3%，整体待处理高斯减少76.3%。
### 4 分两段高斯数据存储布局
轻量定位参数单独存放用于粗过滤；旋转、SH等海量参数做码本压缩，片上常驻码本完成解码，兼顾过滤速度与带宽节省。
### 5 STREAMINGGS专用加速器架构
1）VSU体素排序单元：构建DAG拓扑排序确定全局体素渲染顺序，重映射空体素ID缩减查表开销；
2）HFU分层滤波单元：多组粗/细滤波并行单元，提前丢弃无效高斯，削减MAC运算量；
3）复用优化排序、渲染单元，搭配分层片上缓存适配流式数据。

## 实验分析
1. 实验环境：32nm工艺综合，1GHz时钟，对比Orin NX、GSCore；测试合成/真实多类场景，评测PSNR、推理速度、系统能耗、芯片面积。
2. 画质表现：整套流式渲染相比原生3DGS平均PSNR仅下降0.04dB，部分场景画质小幅提升，视觉无明显损失。
3. 性能指标：相较移动GPU平均提速45.7倍；对比GSCore提速2.1倍；分层过滤是核心加速来源，无过滤时速度减半。
4. 能耗收益：相比Orin NX能耗降低62.9%，较GSCore节能2.3倍，带宽削减是能耗下降主因。
5. 消融与灵敏度：体素尺寸取2平衡画质与带宽；HFU粗滤波单元数量对性能提升最显著，向量量化增益次之；芯片总面积5.37mm²与GSCore接近。

## 研究启发
1. 3DGS实时瓶颈不在计算而是片外DRAM访存，重构渲染处理粒度（从瓦片改为体素）可从根源消除阶段间中间数据传输。
2. 算法与硬件必须协同：仅靠软件压缩无法解决运行时投影排序的重复读写，配套专用滤波、排序硬件才能释放带宽收益。
3. 分层渐进过滤是低成本带宽优化思路，先用少量轻量参数筛除大量无效数据，再加载压缩高精度特征。
4. 体素渲染存在深度排序缺陷，通过微调损失约束高斯分布，无需大幅改动渲染硬件即可修复画质。
5. 移动端神经渲染加速器设计优先级：访存优化＞计算并行，优先削减DRAM流量再提升MAC吞吐。
