---
title: "Easz: An Agile Transformer-based Image Compression Framework for Resource-constrained IoTs"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Easz: An Agile Transformer-based Image Compression Framework for Resource-constrained IoTs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132645">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132645</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>图像压缩，擦除与挤压，基于Transformer的自编码器 </p>
</div>

---

## 研究概要
本文提出面向资源受限IoT的非对称Transformer图像压缩框架Easz，将计算负载转移至服务端。边缘端设计条件均匀擦除压缩算法，服务端采用两级分块轻量化Transformer重建。可灵活调节压缩率，Jetson TX2实测功耗、内存大幅降低，重建PSNR优于超分方案，兼容JPEG/BPG等传统编码器。

## 背景和动机
1. 工业、无人机IoT设备算力内存有限，现有神经网络编解码对称架构在边缘编码时延超十秒，无法实时传输图像。
2. 切换压缩等级需加载不同模型，模型切换开销远超图像传输时延，压缩粒度调节僵硬。
3. 传统下采样超分压缩比例固定，大面积连续删除区域易造成严重图像失真，重建细节丢失明显。
4. 原生像素级Transformer注意力计算复杂度极高，单张图算力消耗大，服务端推理成本高昂。
5. 现有深度学习压缩无法复用JPEG、BPG成熟编码链路，落地改造成本高。

## 相关工作
1. 传统图像编码（JPEG/BPG）：算力友好但压缩增益有限，高压缩率下视觉质量衰减快。
2. 端侧对称神经网络压缩（MBT、Cheng-Anchor）：编解码均部署边缘，算力/内存消耗巨大，切换码率需更换模型。
3. 下采样+超分方案（ESRGAN/SwinIR）：压缩比例固定，随机删除易产生连片空白，重建细节缺失。
4. Transformer视觉重建：原生逐像素注意力复杂度O((hw)²)，高分辨率图像无法在通用GPU运行。
5. 传感器端ROI压缩：仅局部优化，全局动态码率适配能力不足。

## 本文解决方案
### 1 边缘端擦除压缩（Erase-and-Squeeze）
行约束均匀采样生成擦除掩码，增加行列间隔约束避免连片擦除；过滤保留像素生成压缩小图，仅产生极小掩码传输开销，边缘无GPU计算，耗时仅占总时延0.7%。支持连续无级调节压缩比例，无需多套模型。
### 2 两级分块复杂度削减机制
图像先切大patch，再细分子patch；注意力仅在patch内部计算，将原始O((hw)²)复杂度降至O(hw·n²)，256×256图像计算量降低4096倍。
### 3 轻量Transformer重建网络
仅8.7MB双编码器-解码器架构，融合零向量补全擦除区域；采用L1+LPIPS感知损失训练，一套模型适配全部擦除比例，并行子patch推理加速。
### 4 通用兼容接口
擦除压缩输出可直接接入JPEG、BPG、主流神经编码器，无需修改原有编码链路，实现即插即用增强压缩效果。
### 5 端-服务器非对称架构
边缘仅执行轻量级像素筛选，高开销Transformer重建全部交由云端GPU执行，彻底释放IoT硬件压力。

## 实验分析
1. 测试平台：Jetson TX2边缘、RTX2080Ti服务端，数据集Kodak/CLIC/CIFAR10，对比JPEG、MBT、Cheng-Anchor、SwinIR等。
2. 边缘资源：相比神经压缩基线，功耗降低71.3%、内存减少45.8%，边缘全程无需GPU运算。
3. 时延性能：端到端平均时延相比MBT/Cheng下降89%，擦除步骤几乎无额外耗时。
4. 重建质量：同码率下PSNR 28.96、SSIM 0.96，显著优于各类超分模型；嵌入传统编码器后无参考画质指标大幅优化。
5. 消融验证：带间隔约束的均匀掩码优于纯随机擦除；2×2子patch平衡推理速度与重建精度；预训练微调可稳定降低重建损失。

## 研究启发
1. 资源受限IoT图像压缩适合非对称架构，将重型重建任务上移至服务端，从根源解决边缘算力瓶颈。
2. 均匀带间隔像素擦除优于随机删除，可避免大面积空白区域，大幅提升重建图像细节完整度。
3. 两级分块局部注意力是降低Transformer算力的高效手段，无需模型量化剪枝即可实现轻量推理。
4. 单一重建模型适配多压缩比例，可消除多模型切换带来的巨大时延开销，适配动态带宽场景。
5. 新型预处理压缩层可兼容现有成熟编解码器，无需完全重构编码链路，工程落地门槛更低。