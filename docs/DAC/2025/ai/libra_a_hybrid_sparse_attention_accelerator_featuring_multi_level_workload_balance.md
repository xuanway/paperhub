---
title: "Libra: A Hybrid-Sparse Attention Accelerator Featuring Multi-Level Workload Balance"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Libra: A Hybrid-Sparse Attention Accelerator Featuring Multi-Level Workload Balance

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133063">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133063</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合稀疏注意力加速器，多级工作负载平衡，滤波位组稀疏化，动态位组量化 </p>
</div>


---

## 研究概要
本文提出软硬件协同混合稀疏注意力加速器Lib，设计FBS权重分组稀疏、DBQ动态激活量化算法挖掘数值+比特混合稀疏；硬件引入任务池实现多层负载均衡，适配多比特并行运算。TSMC28nm工艺实测，相比Sanger等主流加速器提速1.49~5.89倍，能效提升2.65~10.82倍，精度损失低于1%。

## 背景和动机
1. Transformer注意力计算存在大量数值与比特级冗余，现有加速器仅利用数值稀疏，忽略极高比特稀疏带来加速潜力。
2. 比特串行架构原生适配CNN，无法直接迁移至Transformer注意力不规则计算流程。
3. 混合稀疏下0比特分布极不均匀，PE间、单元内严重负载失衡，大量计算单元空闲抵消稀疏提速收益。
4. 现有单层级负载均衡方案仅优化通道或单元内部调度，无法同时解决多层级算力闲置问题。
5. 注意力QK预测与重计算存在多比特宽度运算，传统固定位宽PE硬件利用率低。

## 相关工作
1. 数值稀疏注意力加速器（Sanger、DTQAtten、DEQ）：仅过滤零数值，未挖掘比特层稀疏，算力削减有限。
2. CNN比特串行BSA架构（Laconic、Adas）：面向卷积规整数据流，不兼容注意力动态激活特征。
3. BitBalance：通道聚类平衡比特负载，仅适配权重静态稀疏，无法处理动态激活不规则比特分布。
4. BSViT：视觉Transformer稀疏方案，针对图像分块量化，不适配NLP序列注意力计算。
5. 单层级负载均衡硬件：仅单元内或通道级调度，无法同时解决PE阵列、BMU内部双重 stall 问题。

## 本文解决方案
### 1 比特分组混合稀疏算法
FBS权重分组稀疏：将权重拆高低比特组，约束每组有效比特数量，迭代误差补偿提升Booth编码稀疏度；DBQ动态激活量化：低相关性token用单比特组预测，高相关性做高精度重算，大幅削减QK矩阵计算量。
### 2 自适应位宽BMU计算单元
基于Booth编码设计比特组乘法单元，原生支持1×1、2×1、2×2多比特并行运算，自动跳过全零比特任务消除无效乘法。
### 3 任务池多层负载均衡机制
每个BMU内置深度8任务池，细粒度任务乱序调度；单元内空闲BMU抢占剩余任务，PE阵列间共享输入栈均衡批次算力，双层调度消除流水线停顿。
### 4 完整Libra硬件流水线
包含8×8自适应PE阵列、DBQ预测引擎、分层片上缓存；分离低精度预测、高精度重算数据流，搭配专用Softmax/LayerNorm非线性单元。
### 5 软硬件协同适配
算法输出分组稀疏张量，硬件直接解析比特组任务，无需额外转译开销，兼容BERT类NLP模型全注意力流程。

## 实验分析
1. 实验环境：TSMC 28nm 500MHz Verilog综合，BERT-base+GLUE八大文本任务，对比Sanger、DTQAtten、DEQ。
2. 算法收益：FBS使权重Booth稀疏度平均提升15.92%；DBQ在r=0.8时可削减超93%QK冗余计算，全方案精度损失<1%。
3. 硬件PPA：总芯片面积1.13mm²，功耗376.66mW，片上SRAM共408KB。
4. 性能对比：相对DE/Sanger分别提速1.49×、5.89×，能效提升2.65×~10.82倍。
5. 消融验证：任务池关闭性能下降1.73倍，深度8为面积与均衡最优折中配置；多层调度是抵消混合稀疏负载失衡核心。

## 研究启发
1. Transformer存在数值+比特两级混合稀疏，仅做单一层稀疏无法释放全部加速潜力，需软硬件联合挖掘两类冗余。
2. 比特稀疏天然带来负载不均，仅单层调度不足以优化，单元内+PE阵列双层任务池均衡可大幅减少流水线stall。
3. 注意力高低相关性token算力需求差异巨大，轻量低比特预测可过滤绝大多数冗余计算，仅少量高关联做高精度运算。
4. 自适应多比特PE可统一处理预测/重算两类位宽运算，避免分设硬件造成面积浪费。
5. 面向NLP注意力加速器不能直接复用CNN比特串行架构，需针对动态激活不规则比特分布定制分组稀疏与调度逻辑。
