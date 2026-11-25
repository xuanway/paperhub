---
title: "ReaLM: Reliable and Efficient Large Language Model Inference with Statistical Algorithm-Based Fault Tolerance"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# ReaLM: Reliable and Efficient Large Language Model Inference with Statistical Algorithm-Based Fault Tolerance

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS6: Time-Critical and Fault-Tolerant System Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.24053">https://arxiv.org/abs/2503.24053</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/PKU-SEC-Lab/ReaLM_DAC25">https://github.com/PKU-SEC-Lab/ReaLM_DAC25</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>大语言模型，基于算法的容错，算法-电路协同设计 </p>
</div>

---

## 研究概要
本文提出软硬件协同容错框架ReaLM，面向 systolic阵列LLM加速器。先大规模故障注入量化LLM固有容错特性，区分敏感/弹性计算单元；设计统计型ABFT机制，仅对临界误差触发重计算。14nm综合面积开销1.42%、功耗1.79%，最低电压场景困惑度退化从18.54降至0.29，最高节能35.83%。

## 背景和动机
1. 先进工艺LLM systolic加速器受老化、工艺偏差影响，低压时序瞬态故障频发，传统大电压裕度方案能耗极高。
2. 现有DMR、Razor电路容错硬件开销巨大；模型重微调成本高昂，无法适配大语言模型。
3. 传统ABFT只要检测误差就触发全部重计算，无视LLM天然抗误差能力，恢复开销严重浪费能效。
4. LLM含归一化层单元误差敏感度差异极大，现有容错未区分组件特性，统一保护带来冗余计算。
5. 误差幅值、频次对模型性能影响存在特殊权衡关系，现有近似ABFT仅依靠总MSD指标，无法精准判定有害故障。

## 相关工作
1. 电路级容错：DMR双模冗余、Razor时序检测，面积功耗开销高，大规模systolic阵列扩展性差。
2. 算法级容错：故障感知微调，LLM参数量巨大，重训练算力成本不可接受。
3. 经典ABFT：基于校验和逐误差触发重计算，未利用模型容错，恢复能耗居高不下。
4. ApproxABFT：仅依靠总MSD阈值过滤误差，不区分误差频次与模型组件差异，误触发大量恢复。
5. CNN专用容错方案：模型结构与LLM Transformer、KV缓存、归一化机制差异大，无法直接迁移。

## 本文解决方案
### 1 大规模故障注入评测体系
基于OPT/LLaMA系列搭建位翻转注入仿真，区分Prefill/Decode两阶段，量化各网络单元、不同比特、误差幅值频次对困惑度/准确率的影响，划分敏感、弹性组件。
### 2 LLM容错核心规律提炼
归一化前置单元（O/Down）为敏感单元，少量误差即严重劣化指标；其余弹性单元可容忍零星大误差或大量微小误差；Prefill阶段故障危害远高于Decode。
### 3 统计型ABFT自适应判定策略
同时引入MSD、误差幅值mag、有效频次freq三维指标，拟合临界误差区域；仅落入临界区间才触发重计算，其余微小误差直接放行。
### 4 低开销统计检测硬件单元
适配权重/输出驻留两种systolic数据流，在阵列边缘增设校验行列；新增统计单元完成MSD计算、幅值频次统计、阈值判定，仅增加极低硬件代价。
### 5 分层组件差异化保护
针对敏感单元收紧误差阈值，弹性单元放宽约束，在性能无损前提下最大化电压降额度，挖掘节能空间。

## 实验分析
1. 实验平台：256×256 systolic阵列，14nm工艺综合，对比无保护、DMR、ThunderVolt、经典ABFT、ApproxABFT。
2. 硬件开销：输出驻留架构面积仅增1.42%，功耗提升1.79%，远优于各类冗余、传统容错方案。
3. 模型性能：0.72V低压下OPT困惑度退化从18.54降至0.29，LLaMA推理准确率损失控制在0.47%内。
4. 能效收益：不同LLM组件节能区间不同，弹性单元最高节能35.83%，敏感单元节能幅度有限。
5. 消融验证：同时舍弃幅值/频次统计后，重计算次数提升2~4倍，能耗优势完全消失。

## 研究启发
1. LLM各计算单元容错能力差异根源是归一化层对异常离群值的放大效应，容错保护必须分层差异化设计。
2. 仅依靠总误差MSD不足以判断故障危害，误差幅值、出现频次是不可或缺的判定维度。
3. 无需对所有检测误差执行重计算，利用模型固有容错放行无害微小故障，是低压节能核心路径。
4. ABFT可与systolic阵列原生数据流深度融合，轻量统计硬件即可实现自适应容错，硬件代价可控。
5. Prefill阶段KV缓存决定整轮推理基础，容错阈值需比Decode阶段更严格，分阶段优化可进一步平衡可靠性与能耗。