---
title: "DCDiff: Enhancing JPEG Compression via Diffusion-based DC Coefficients Estimation"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DCDiff: Enhancing JPEG Compression via Diffusion-based DC Coefficients Estimation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://netsec.ccert.edu.cn/files/papers/dac25-dcdiff.pdf">https://netsec.ccert.edu.cn/files/papers/dac25-dcdiff.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> JPEG，图像压缩，扩散模型 </p>
</div>

---

## 研究概要
本文提出DCDiff面向IoT低成本摄像头的JPEG增强方案，发送端丢弃全部DC系数仅保留四角块，接收端基于扩散模型端到端重建DC。设计掩码拉普拉斯损失与频率调制采样，规避传统迭代误差传播。多数据集测试PSNR提升3~6.7dB，压缩率平均提升25%，兼容Raspberry Pi、Cortex-A53低功耗设备，下游任务精度衰减仅0.49%。

## 背景和动机
1. 物联网监控、车载等低成本硬件算力受限，仅支持标准JPEG，学习型压缩算法无法部署，传输带宽压力大。
2. DC系数数值大、编码比特多，丢弃DC可显著降低传输量，但传统基于拉普拉斯分布迭代重建会产生误差并全局扩散。
3. 自然图像边缘、纹理区域像素突变，违背邻域拉普拉斯分布，传统逐块迭代修复易出现色彩溢出、伪影。
4. 现有两阶段方案先统计重建再CNN降噪，误差根源无法消除，图像细节易过度平滑失真。
5. 扩散模型擅长图像生成，但原生偏向高频细节，难以精准拟合DC低频均值特征，缺少专用约束策略。

## 相关工作
1. 基础DC迭代恢复：依靠邻域像素拉普拉斯假设逐块推算DC，突变区域误差持续扩散，画质劣化明显。
2. CNN后修复方案：迭代重建后使用残差网络降噪，但无法消除初始分布偏差带来的固有误差，易模糊纹理。
3. 多方向预测DC优化：调整邻域匹配方向缓解误差，仍依赖逐块迭代，高纹理图存在明显色彩失真。
4. 端侧学习压缩：基于神经网络DCT变换，编码器算力需求高，无法在ESP32、树莓派等设备运行。
5. 扩散图像压缩：通用生成压缩框架，未针对JPEG DC低频特征定制，重建DC一致性差。

## 本文解决方案
### 1 端到端扩散DC重建框架
发送端仅保留四角块DC，其余置0；接收端AC编码器提取高频特征，扩散潜变量模块生成DC对应低频特征，解码器融合双分支特征输出完整图像，无需逐块迭代。
### 2 掩码拉普拉斯分布损失(MLD)
依据AC幅值生成高频掩码，仅对平滑低频区域施加邻域像素约束，过滤突变纹理区域，抑制误差传播，保证图像色彩一致性。
### 3 频率调制采样策略(FMPP)
专用预测器自适应生成高低频缩放因子，推理阶段调整扩散跳跃连接权重，抑制高频生成倾向，强化DC对应的低频均值输出。
### 4 两阶段分层训练策略
阶段1联合训练AC/DC编码器与解码器，重构+感知+对抗损失优化基础画质；阶段2冻结编码模块，微调扩散网络，引入MLD损失约束DC分布。
### 5 零改动前端兼容设计
编码侧完全复用原生JPEG流程，仅将非四角DC置零，不增加摄像头计算开销，适配所有支持标准JPEG的低功耗硬件。

## 实验分析
1. 实验配置：OpenImages训练，Set5/Urban100/遥感6类测试集；对比3类SOTA DC恢复算法，评测PSNR/SSIM/MS-SSIM/LPIPS。
2. 图像质量：所有数据集PSNR提升3~6.7dB，无色彩溢出、边缘模糊伪影，LPIPS显著更低，视觉效果最优。
3. 压缩性能：同等Q50量化表平均压缩率提升25%；同等画质下相比激进量化JPEG仍多压缩10%~14%。
4. 设备适配：部署Raspberry Pi、Cortex-A53，编码吞吐与原生JPEG基本持平，无额外算力负担。
5. 消融验证：移除MLD损失出现严重色偏；FMPP模块可稳定提升低频重建质量，掩码阈值T=10综合效果最优；遥感分类下游精度仅下降0.49%。

## 研究启发
1. 低成本IoT设备无需修改编码端，仅在云端接收端引入生成模型即可大幅提升JPEG压缩收益，工程落地门槛极低。
2. 传统逐块迭代DC重建的核心缺陷是误差扩散，端到端全局生成方案可从根源规避该问题。
3. 扩散模型天然偏向高频细节，需专用频率调制机制才能适配DC低频均值重建任务。
4. 拉普拉斯分布约束不能全局施加，通过掩码隔离突变纹理区域，可兼顾分布先验与图像细节。
5. 压缩优化与编码标准解耦思路具备通用性，可拓展至各类硬件受限的图像传输场景。
