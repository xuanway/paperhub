---
title: "A Cross-model Fusion-aware Framework for Optimizing (gather-matmul-scatter)s Workload"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# A Cross-model Fusion-aware Framework for Optimizing (gather-matmul-scatter)s Workload

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dai.sjtu.edu.cn/my_file/pdf/a5764a0c-bde6-46df-b884-92e89c8e9cbf.pdf">https://dai.sjtu.edu.cn/my_file/pdf/a5764a0c-bde6-46df-b884-92e89c8e9cbf.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 聚集，分散，矩阵乘法 </p>
</div>

---

## 研究概要
本文提出Efficient-GMS跨模型优化框架，统一RGCN、SpConv、MoE共享的gather-matmul-scatter计算模式。设计四类算子融合数据流，性能模型剪枝超90%配置空间，轻量XGBoost自适应选择数据流。在RTX3090/A100验证，RGCN端到端提速1.32x，SpConv提速1.46x，MoE提速1.15x。

## 背景和动机
1. RGCN、稀疏卷积、MoE均以g-mm-s为核心算子，但现有优化均为模型专用，跨场景迁移会出现大幅性能衰减，通用性差。
2. g-mm-s配置参数维度极高，原始搜索空间可达上万组，暴力遍历耗时长达数千秒，调参成本过高。
3. 图、点云、MoE输入稀疏度、维度动态变化，固定静态数据流无法适配多变负载，最差性能下降14.77倍。
4. 现有方案仅单独优化matmul，忽略gather/scatter之间访存冲突、并行度耦合，整体加速上限低。
5. 缺乏统一抽象框架，无法复用优化策略，每种模型需单独开发内核，开发效率低下。

## 相关工作
1. 图学习优化（PyG/Fasten）：仅面向RGCN分段矩阵乘，不兼容点云稀疏卷积、MoE门控路由，跨模型迁移失效。
2. 点云稀疏算子（TorchSparse）：针对空间邻域g-mm-s设计，图多关系数据下访存冲突严重。
3. MoE加速（HuggingFace）：仅优化专家并行计算，未统一提取g-mm-s公共计算模式。
4. 分段矩阵乘Cutlass：侧重稠密矩阵并行，未考虑gather不规则访存、scatter原子写冲突。
5. 算子融合研究：仅单一G-M或M-S融合，缺少四类融合模式对比与动态选择机制。

## 本文解决方案
### 1 融合感知跨模型统一框架
抽象三类模型共享g-mm-s计算原语，设计4种分段融合数据流：G-Mseg-S、(GM)seg-S、G-(MS)seg、(GMS)seg；区分水平算子融合、垂直分段并行两类优化策略，支持策略跨模型复用。
### 2 性能模型驱动配置剪枝
构建并行效率、计算访存比双维度性能预测模型，量化分块大小、线程数等参数影响；过滤性能后60%~90%配置，搜索时长缩短5.26倍，缓存相似数据最优配置避免重复搜索。
### 3 自适应数据流选择模块
提取输入维度、稀疏度等特征，SVD降维后送入训练好的XGBoost分类器，动态匹配最优融合数据流；(GM)seg-S、(GMS)seg覆盖96.5%最优场景，大幅简化推理开销。
### 4 访存与并行冲突优化
分析融合利弊：GM融合提升数据复用但降低并行；MS融合减少访存但加剧原子写冲突；根据硬件SM共享内存容量动态切换细/粗粒度调度。
### 5 通用内核实现
基于CUDA实现统一g-mm-s内核，兼容图、点云、MoE三类输入，支持动态分块、多线程调度，无缝对接PyG、TorchSparse、HuggingFace生态。

## 实验分析
1. 实验平台：RTX3090、A100；测试数据集含图(AIFB/IMDB)、点云(KITTI/ModelNet)、MoE混合专家。基线为PyG、TorchSparse、HuggingFace原生实现。
2. 内核加速：SpConv算子平均提速1.44~1.60倍，RGCN相比原生循环最高提速14.05倍。
3. 端到端效果：SpConv平均1.43~1.46x，RGCN 1.25~1.32x，MoE 1.15x，A100大卡收益更显著。
4. 消融实验：配置剪枝削减60%~90%搜索空间；自适应数据流带来1.14~6.03倍增益；跨模型融合策略相比直接移植提升1.86倍。
5. 数据流分布：(GM)seg-S占最优场景52.5%，全融合(GMS)seg占44%，剩余两种仅极少数场景最优。

## 研究启发
1. 不同深度学习模型可提炼公共计算原语，基于统一算子框架能实现优化策略跨模型复用，降低开发成本。
2. 算子融合存在访存、并行度、原子写多重权衡，不存在全局最优固定数据流，必须根据输入动态切换。
3. 建立轻量性能解析模型可替代暴力网格搜索，大幅降低算子调参时间，适合工业编译场景。
4. 稀疏不规则计算瓶颈不只在矩阵乘，gather不规则读取、scatter原子更新是关键性能短板。
5. 优先覆盖主流最优融合模式，少量备选模式兜底，可在极小推理开销下获得绝大多数性能收益。
