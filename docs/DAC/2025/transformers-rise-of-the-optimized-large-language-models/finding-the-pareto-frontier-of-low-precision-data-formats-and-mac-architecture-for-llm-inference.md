---
title: "Finding the Pareto Frontier of Low-Precision Data Formats and MAC Architecture for LLM Inference"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Finding the Pareto Frontier of Low-Precision Data Formats and MAC Architecture for LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132989">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132989</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 低精度数据格式，MAC架构，帕累托优化，大语言模型推理 </p>
</div>


---

## 研究概要
本文系统遍历25000+种MAC硬件设计，对比INT/FP/Posit/LNS/MX/VSQ六类低精度数值格式，以SQNR、面积、能效为指标求解LLM推理帕累托前沿。同等精度下LNS16、MXINT8、VSQINT4相较FP系列能效分别提升1.8×、2.2×、1.9×，同时给出内积、累加位宽等硬件最优配置规律。

## 背景和动机
1. LLM推理算力需求爆炸，低精度量化与定制MAC加速器是核心优化路径，但数值格式、硬件参数组合空间庞大，缺乏统一公平对比框架。
2. 现有研究仅单独测试某一种数据格式，未在统一5nm工艺下横向对比，难以确定不同精度下帕累托最优方案。
3. 块量化MX/VSQ、对数L、Posit新型格式缺少完整硬件面积/功耗量化评估，无法量化精度与能效权衡关系。
4. MAC关键参数（内积尺寸、累加位宽、流水线、块大小）对硬件效率影响巨大，缺乏系统性扫参分析。
5. 多数工作仅测硬件指标，未关联LLM下游任务精度，SQNR与模型准确率的对应关系未得到验证。

## 相关工作
1. 传统定点/浮点MAC：仅评估INT/FP单一格式，无新型对数、块量化格式对比，未系统扫参寻优。
2. Posit/LNS算术单元设计：仅做单格式硬件实现，缺少跨格式公平对标，未面向LLM负载验证。
3. MX/VS块量化算法研究：侧重软件量化效果，未集成到MAC硬件测算面积功耗开销。
4. 商用Tensor Core类加速器：固定FP8/FP4架构，未探索LNS、块量化等更优数值方案。
5. 低精度硬件协同研究：缺少大规模多设计点帕累托前沿挖掘，无法给出通用最优硬件配置准则。

## 本文解决方案
### 1 统一多格式MAC硬件建模框架
对INT、FP、Posit、LNS、MX、VSQ全部格式参数化Verilog建模，统一5nm 1GHz工艺综合，标准化面积、功耗、SQNR评测流程。
### 2 多维设计空间遍历扫参
批量遍历内积长度、外积矩阵尺寸、累加位宽、流水线级数、块量化粒度五大关键参数，生成超25000组MAC硬件设计。
### 3 融合块缩放的融合点积架构
将MX共享指数、VS线性缩放硬件嵌入MAC流水线，在对齐阶段完成块尺度补偿，消除软件缩放额外访存开销。
### 4 LNS专用对数乘加通路
利用对数域乘法转加法特性，设计基于定点指数分段LUT的低功耗MAC，省去大规模乘法阵列。
### 5 SQNR-任务精度关联评测方法
以FP32矩阵乘结果为基准计算SQNR，在OpenELM、Llama、BERT四类LLM上验证数值信噪比与下游分类/匹配精度单调性关联。
### 6 帕累托前沿筛选算法
以TOP/W、TOP/mm²、SQNR三维指标筛选非支配最优硬件设计，区分4/8/16bit三档精度给出最优数值格式。

## 实验分析
1. 实验环境：5nm CMOS，Synopsys综合/PrimePower功耗仿真；LLM测试集Hellaswag、STSB；25000+MAC设计点。
2. 格式横向对比：同等SQNR下16bit最优为LNS16，8bit为MXINT8，4bit为VSQINT4，能效分别优于FP16/FP8/FP4 1.8/2.2/1.9倍；Posit解码面积过高整体次优。
3. MAC参数规律：增大内积尺寸摊销归一化逻辑开销；FP4采用定点累加可提升17%能效；块尺寸32平衡精度与硬件开销。
4. 硬件开销拆解：乘法单元、归一化、寄存器是面积功耗三大来源；Posit独有的Posit-to-FP转换带来近一倍面积损耗。
5. 模型精度验证：SQNR与LLM任务精度单调正相关，MX/VSQ低比特格式可将任务精度损失控制在1%以内。

## 研究启发
1. 单纯FP/INT并非最优选择，LNS、块量化MX/VSQ在LLM推理精度-能效权衡上具备显著优势。
2. MAC内积长度、累加位宽是决定硬件效率核心参数，大尺寸内积能大幅摊销归一化电路成本。
3. 块量化缩放逻辑必须集成进MAC硬件，软件端缩放会引入不可接受的访存延迟与功耗。
4. Posit动态编码带来高动态范围优势，但解码硬件开销过大，工业落地性价比低于LNS/MX。
5. 做低精度加速器选型不能只看算法指标，必须统一工艺完成完整硬件面积功耗扫参，才能找到帕累托最优数值格式与MAC配置。
