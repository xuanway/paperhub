---
title: "Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "rram"
  - "processing-in-memory"
  - "dnn-ip-protection"
  - "hardware-security"
---

# Guarder: A Stable and Lightweight Reconfigurable RRAM-based PIM Accelerator for DNN IP Protection

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133133">https://ieeexplore.ieee.org/document/11133133</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 知识产权保护，存内处理，可重构，对比训练</p>
</div>

---

## 研究概要
本文提出软硬件协同框架Guarder，面向RRAM存内DNN加速器解决权重IP窃取与器件随机噪声两大痛点。硬件设计3T2R单元抑制编程偏差，通过可调逆变器电压构建硬件密钥；配套对比训练算法，授权芯片精度损失<2%，未授权设备输出接近随机。180nm仿真相较1T1R架构面积缩减1.41倍、能耗降低2.28倍。

## 背景和动机
1. RRAM存内计算(PIM)可缓解冯诺依曼访存瓶颈，但RRAM存在循环/器件级编程随机噪声，直接导致MAC计算精度大幅衰减。
2. RRAM非易失特性使攻击者可物理探针读取权重，传统加密/混淆方案适配性差，且会加剧噪声带来的精度损失。
3. 现有1T1R交叉阵列依赖ADC读出，硬件面积、静态功耗开销巨大，噪声容忍度极低，30%噪声下深度模型精度下降超8%。
4. 现有RRAM安全方案仅做电路混淆，未协同训练算法，权重泄露后攻击者微调即可恢复有效推理结果。
5. 缺少噪声鲁棒+硬件原生加密一体化协同设计，无法同时兼顾推理稳定性与模型IP版权保护。

## 相关工作
1. 传统1T1R RRAM-PIM：依靠电流模ADC完成MAC，噪声敏感、硬件开销高，无内置安全加密机制。
2. RRAM权重加密方案：稀疏梯度扰动加密，未考虑器件噪声，多次编程带来巨大时延与能耗。
3. 交叉阵列电路混淆：修改行列连接关系，外设电路复杂，无法缓解RRAM固有编程偏差。
4. DNN软件IP保护：权重混沌、水印等纯软件方案，无法阻止硬件层面物理探针窃取权重。
5. 2T2等分压存内单元：仅优化噪声鲁棒，未集成硬件级模型加密密钥机制。

## 本文解决方案
### 1 3T2R鲁棒存内单元硬件
双RRAM互补分压搭配片上逆变器，通过二进制逻辑滤除编程噪声，支持最高30%器件偏差；去除ADC模块，大幅缩减外设面积与静态功耗。
### 2 逆变器电压硬件密钥机制
每条SL通路逆变器供电电压作为独立密钥，不同电压切换MAC判决阈值；密钥空间达14^128，暴力破解不可行，无需额外加密电路。
### 3 软硬件协同对比损失训练
构建联合损失：最小化授权密钥推理损失，最大化默认密钥下推理损失，拉大授权/未授权设备精度差距；动态调整平衡超参防止训练崩溃。
### 4 二值权重映射流水线
DNN权重二值化后映射至3T2R互补RRAM对，适配单元正负值计算逻辑，加密仅调整逆变器配置，无额外读写开销。
### 5 分层加密策略
支持单/多层模型加密，深层加密对IP保护增益更高，双层加密可进一步扩大未授权设备性能退化幅度。

## 实验分析
1. 实验平台：UMC 180nm SPICE仿真，测试MLP/ResNet/ViT/SegFormer/DiT多类视觉模型，覆盖分类、分割、图像生成任务。
2. 噪声鲁棒性：30%编程噪声下，3T2R架构模型精度下降不足1%；同等条件1T1R最高损失10%。
3. 硬件开销：相比标准1T1R阵列，整体面积缩减1.41倍、总能耗降低2.28倍，核心增益来自移除ADC。
4. IP保护效果：授权芯片精度仅下降1~2%；未授权设备分类准确率趋近随机，分割mIoU仅11.54，生成模型FID大幅恶化。
5. 安全验证：密钥空间规模极大，随机猜测百次推理效果均极差，无法恢复可用模型。

## 研究启发
1. RRAM存内安全必须硬件单元与训练算法协同，单一电路加密或纯软件防护难以同时解决噪声与IP窃取问题。
2 基于逆变器可调阈值的硬件密钥属于轻量化原生加密，无需专用加解密外设，适配边缘资源受限场景。
3. 互补分压式存内单元可天然抑制RRAM编程随机偏差，省去反复重编程带来的能耗与时延开销。
4. 对比式训练是低成本IP保护手段，通过拉大授权/非授权推理性能差，从算法层面杜绝窃取模型复用。
5. 去除ADC是RRAM PIM面积、能耗优化关键突破口，二值化DNN与分压单元高度适配，兼顾效率与安全。


### 相关资源

- **Nature Scientific Reports 后续论文**（2025）
- **RRAM PIM 综述**：Sebastian et al., Nature Nanotechnology 2020
- **PUF + RRAM**：Gao et al., "RRAM-based PUF" (IEEE TED)
