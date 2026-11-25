---
title: "A High-Precision and Low-Cost Approximate Transform Accelerator for Video Coding"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# A High-Precision and Low-Cost Approximate Transform Accelerator for Video Coding

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11133124">https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11133124</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 视频编码，变换加速器，近似架构，稀疏性优化，面积高效</p>
</div>

---

## 研究概要
针对VVC多变换硬件资源开销大问题，本文挖掘DCT2与DST7矩阵对角聚集特性，最小二乘稀疏优化转换矩阵，搭配矩阵分解优化DCT2，复用移位加法单元构建统一流水线加速器。支持4~32点三类变换，28nm工艺下硬件资源降低44%，码率损失仅0.53%，可实时处理8K@57fps视频编码。

## 背景和动机
1. VVC引入DCT2、DST7、DCT8三类变换提升压缩率，但各类变换独立电路造成巨大硬件面积开销。
2. DST7与DCT8架构可复用，但DCT2和DST7矩阵计算完全独立，难以硬件共享，现有方案无法兼顾编码精度与芯片成本。
3. 现有联合近似变换要么精度损失严重，要么需要正反变换耦合，解码器改动大，不适合编码硬件落地。
4. DCT2传统蝶形算法后子矩阵元素类型多，不同尺寸无法共用计算单元，乘法器数量居高不下。

## 相关工作
1. DCT2独立优化：蝶形分解、无乘法移位架构、分层复用矩阵，但仅针对单一变换，无法兼容DST7。
2. DST7独立优化：基于RAG-n算法、FPGA DSP资源缩减加法器，未实现与DCT2硬件融合。
3. 联合近似变换方案：一类修改矩阵系数造成明显码率损耗；另一类需要前向流水线嵌入逆变换，硬件实现成本翻倍，工程实用性差。
4. 现有多变换加速器只能小规模复用，归一化门控、功耗指标劣于本文设计。

## 本文解决方案
### 1. DST7稀疏近似转换算法
推导DCT2到DST7的转换矩阵TF，利用对角幅值聚集特性，采用最小二乘做列稀疏约束优化，选取每列保留7个系数的最优方案，32点场景乘法器减少79.3%，码率损耗极低。
### 2. 矩阵分解DCT2轻量化计算
蝶形分解后将DCT子矩阵拆分为Q、R两个低幅值矩阵，统一轻量化移位加法单元SA生成全部乘积，多尺寸变换共用同一套SA电路，大幅复用硬件。
### 3. 六级深度流水线统一硬件架构
包含奇偶分解、SA计算、选择树、加法树、DCT2整合、转换计算六级流水线；配套数据重排电路兼容4/8/16/32多尺寸，单周期并行32点运算；仅最后一级完成DCT2向DST7近似转换，无需改动解码端。
### 4. 多层次硬件复用策略
分解电路、SA单元、加法树跨尺寸复用；转换阶段稀疏矩阵乘法替代完整DST7矩阵运算，整体门电路开销显著下降。

## 实验分析
1. 编码性能：VTM17.0全帧内测试，平均BD-BR仅上升0.53%，远低于同类近似变换方案的1%以上损耗。
2. 硬件指标：28nm工艺、769MHz，单周期32点并行，总门数184.4K，相较同规格主流设计资源降低44%；归一化门数、归一化功耗均优于对比文献。
3. 实时性能：最高吞吐支撑8K分辨率57fps实时编码，功率仅58.7mW，动态功耗优化幅度超40%。
4. 参数消融：对比r=5/7/9三种稀疏保留系数，r=7在乘法开销与编码质量间取得最优平衡。

## 研究启发
1. 多标准变换硬件融合可通过矩阵转换近似实现，无需两套完整计算通路，是面积优化核心思路。
2. 利用变换矩阵对角稀疏固有特征，搭配最小二乘约束优化，能以极小编码代价削减乘法器规模。
3 蝶形分解+矩阵分层拆分可统一多尺寸DCT计算单元，最大化移位加法硬件复用率。
4. 流水线分层解耦通用DCT计算与DST转换，仅在末尾增加转换电路，不会改动编码整体数据流。
5. 视频变换加速器需并行度、复用度、近似精度三者协同权衡，才能同时满足8K高实时与低芯片成本需求。