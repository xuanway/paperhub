---
title: "MambaOPU: An FPGA Overlay Processor for State-space-duality-based Mamba Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# MambaOPU: An FPGA Overlay Processor for State-space-duality-based Mamba Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132895">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132895</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 状态空间对偶性，FPGA加速器，算子融合，稀疏计算 </p>
</div>


---

## 研究概要
本文面向Mamba2（SSD状态空间模型）提出FPGA覆盖处理器MambaOPU，软硬件协同优化算子融合与稀疏计算，设计可重构脉动阵列与稀疏预取单元，实现片上SSD全计算。在多款Mamba2模型验证，相较A100、Xeon CPU归一化吞吐量最高提升880.79×、1812×，能效最高提升24.27×、12908×。

## 背景和动机
1. Mamba2基于SSD机制存在大量广播逐元素运算，张量扩张带来巨大片外内存开销，峰值内存最高达41.55GB。
2. GPU张量核面向稠密矩阵乘优化，逐元素、分段稀疏计算硬件适配差，SSD阶段耗时占总推理83.88%。
3. SpMM/SDMM存在结构化零稀疏，现有硬件无专用跳过机制，大量无效乘加浪费算力。
4. 已有Mamba加速器MARCA无法适配SSD双分支（注意力/递推）混合计算流程，缺少多模式统一阵列。
5. 现有优化仅单一软件或硬件改进，未构建算子融合+稀疏重排+多模式阵列完整协同流水线。

## 相关工作
1. Transformer专用FPGA/ASIC加速器：面向注意力稀疏，无法适配SSD分段递推、三角稀疏运算逻辑。
2. MARCA Mamba加速器：仅支持基础SSM，未针对Mamba2广播扩张、双分支SSD做定制优化。
3 GPU加速Mamba方案：依赖张量核，逐元素与稀疏计算效率极低，长序列内存瓶颈突出。
4 通用稀疏矩阵硬件：仅标准SpMM，不兼容SSD特有的分段乘积、因果三角掩码稀疏模式。
5 算子融合编译工具：仅软件图优化，无配套可重构硬件阵列支撑融合后混合运算。

## 本文解决方案
### 1 软硬件协同算子融合框架
算子合并：广播乘与求和融合为单一描述符，消除中间张量存储；算子后移：将分段乘法嵌入后续运算，缩短SSD计算路径，大幅降低片外访存。
### 2 张量重排分组稀疏加速算法
针对因果三角稀疏做张量重排分组，配合稀疏预取单元识别零区块，跳过全部无效SpMM/SDMM计算，削减近50%冗余运算。
### 3 稀疏预取数据获取单元
地址生成器动态生成稀疏访问序列，分模式适配SSD多阶段计算，压缩稀疏张量传输量，匹配脉动阵列输入时序。
### 4 四模式可重构32×32脉动阵列
单阵列分时支持GEMM、逐元素运算、SpMM、分段乘四种计算，多路多路选择器切换数据流，统一处理线性层与SSD双分支运算。
### 5 全片上SSD内存调度
区分FusedOps与EleOps缓存，序列分块并行计算，94%数据在片上BRAM完成读写，规避DDR高延迟带宽瓶颈，配套SFU处理RMSNorm/EXP非线性算子。

## 实验分析
1. 实验环境：Xilinx U200 FPGA，130M~2.8B五档Mamba2 FP1模型，对比A100/A80 GPU、Xeon Gold CPU。
2 资源情况：四核MambaOPU LUT占用74.03%、BRAM 92.70%，单核心长序列能效更优，多核并行提速3.67倍。
3 性能指标：单芯吞吐量较A100最高提升880.79倍、CPU提升1812倍；能效相较A100最高24.27倍、CPU超万倍。
4 消融验证：算子融合削减大量中间访存；稀疏预取减少近半无效计算；片上存储是吞吐提升核心来源。
5 瓶颈分析：大模型线性特征投影为主要剩余瓶颈，SSD经多重优化延迟大幅下降。

## 研究启发
1. Mamba2核心瓶颈是广播张量扩张带来的内存爆炸，算子融合是低成本削减中间张量的核心软件手段。
2 SSD独有的因果三角稀疏不能复用通用稀疏硬件，必须定制重排分组与专用预取单元才能释放稀疏收益。
3 单一脉动阵列通过多路控制信号重构，可统一稠密、逐元素、稀疏、分段四类运算，减少硬件冗余。
4 片上BRAM带宽远高于DDR，将SSD全部计算放置片上可彻底消除访存瓶颈，是FPGA加速Mamba关键思路。
5 长短序列硬件最优配置存在差异：短序列单核能效更高，长序列多核心并行可显著降低推理延迟。