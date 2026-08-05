---
title: "PARO: Hardware-software Co-design with Pattern-aware Reorder-based Attention Quantization in Video Generation Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PARO: Hardware-software Co-design with Pattern-aware Reorder-based Attention Quantization in Video Generation Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/a4960209-c46c-4a78-aceb-1ea756a5fdac.pdf">https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/a4960209-c46c-4a78-aceb-1ea756a5fdac.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 视频生成模型，混合精度量化，硬件加速器 </p>
</div>

---

## 研究概要
本文面向3D全注意力视频生成模型提出软硬件协同PARO加速器。设计重排序分块混合精度量化，统一注意力为块对角结构，平均4.8bit无损压缩；配套输出位宽感知混合精度PE阵列。在CogVideoX测试，同等硬件下较A100最高提速2.71×，超同类ASIC加速器6.38~7.05倍，能效显著提升。

## 背景和动机
1. CogVideoX等3D全注意力视频模型token规模巨大，注意力矩阵达56.5GB，注意力计算占总时延67.93%，是推理核心瓶颈。
2. 传统逐行量化注意力存在极值离群，缩放因子过大，INT4量化生成视频出现明显噪点、画质崩塌。
3. 不同头/层注意力模式杂乱无章，无法统一分块量化，难以兼顾压缩率与生成质量。
4. 现有混合精度硬件仅基于输入位宽计算，无法利用输出低比特削减QK矩阵乘算力，算力浪费严重。
5. 主流加速方案仅优化AttnV，QK计算无对应优化，完整注意力链路加速不充分。

## 相关工作
1. ViT/扩散量化方法：仅量化Q/K，不处理注意力图，无法解决3D大矩阵存储压力。
2. SageAttention：仅8bit量化QK，缺少混合精度分块策略，低位宽画质衰减明显。
3. Sanger稀疏注意力：基于阈值裁剪，会丢失视频时空细节，生成质量受损。
4. ViTCoD专用ASIC：稀疏分块硬件，未适配视频3D注意力独特分布，加速上限低。
5. GPU量化推理：依赖统一精度算子，无法动态适配注意力块差异化位宽，访存与计算开销高。

## 本文解决方案
### 1 模式感知token重排序算法
离线为各注意力头筛选最优置换方案，在线重排QKV token，将多样局部注意力模式统一为规整块对角结构，块内数值波动大幅降低，天然适配分块量化。
### 2 重要性引导混合比特分配
融合块均值权重、量化误差构建敏感度指标，转化整数规划分配0/2/4/8bit，高敏感块分配高位宽，平均仅4.8bit且画质无损。
### 3 输出位宽感知混合精度PE
PE内置多路2bit乘法单元，支持2/4/8bit动态组合；新增前导零LD单元压缩K，匹配输出注意力低位宽做QK乘，同步加速QK与AttnV。
### 4 分层调度流水线
增设块调度器跳过0bit无效计算；浮点向量单元单独处理Softmax等非线性运算，与定点PE阵列流水并行。
### 5 完整软硬件协同链路
重排序-量化-混合精度计算-逆重排序端到端适配CogVideoX，重排序开销仅占总时延1%左右，可忽略不计。

## 实验分析
1. 实验环境：TSMC 12nm 1GHz RTL综合，CogVideoX-2B/5B，对比A100、Sanger、ViTCoD，FVD/VQA/CLIP等多视频指标评测。
2. 算法画质：PARO-MP(4.8bit)FVD、VQA与FP16基线几乎持平，远优于Naive INT4量化，无肉眼可见视频失真。
3. 硬件速度：同等资源相较A100最高提速2.71×；对比Sanger、ViTCoD最高提升7.05倍。
4. 消融验证：重排序是降低量化误差核心；输出感知PE可带来约3倍整体加速增益。
5. 能效指标：PARO能效3.46~3.61 TOPS/W，为A100的4.86~6.43倍；重排序运行开销极低。

## 研究启发
1. 视频3D注意力存在天然局部聚集特性，通过token重排序统一数据分布，是低位宽无损量化关键前置手段。
2. 混合精度不能均分比特，需结合块重要性与量化难度做优化分配，平衡存储与生成画质。
3. 传统混合硬件只看输入，可基于输出注意力低位宽反向压缩输入矩阵，双向优化QK与AttnV两大计算瓶颈。
4. 视频生成瓶颈集中在超大注意力矩阵，软硬件协同需同时优化量化算法与定制PE阵列，单一层面优化收益有限。
5. 可跳过0bit无贡献注意力块，调度器配合混合精度单元能进一步削减无效算力开销。
