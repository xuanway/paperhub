---
title: "MIRACLE: Multimodal Information Retrieval via a Combined In-Memory Processing and Content Addressable Memory Approach"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MIRACLE: Multimodal Information Retrieval via a Combined In-Memory Processing and Content Addressable Memory Approach

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132973">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132973</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>多模态信息检索，哈希，存内处理，内容可寻址存储器 </p>
</div>

---

## 研究概要
本文提出MIRACLE混合架构，融合STT-MRAM存内计算(PIM)与内容寻址存储器(CAM)实现多模态检索。利用器件固有随机性实现三元LSH哈希，分段CAM粗筛后余弦精排。在MSCOCO等数据集验证，检索精度与CPU基线持平，延迟降低9.45倍、能耗减少30.2倍。

## 背景和动机
1. 冯诺依曼架构多模态检索存在海量数据搬运，余弦排序时延、能耗极高；传统哈希降维易造成跨模态精度损失。
2. 通用LSH随机矩阵乘计算量大，硬件ADC转换带来巨大功耗开销，难以低功耗部署。
3. 纯CAM检索仅靠汉明距离，长哈希串区分能力差，多模态场景召回率大幅下滑。
4. 现有PIM、CAM方案仅适配单模态图像检索，缺少面向图文跨模态协同硬件流水线。
5. 缺少两级检索分层架构，无法兼顾CAM并行高速过滤与余弦相似度高精度重排。

## 相关工作
1. 传统CPU多模态检索：基于CLIP提取特征后全量余弦排序，数据搬运开销巨大，实时性差。
2. 通用哈希检索：LSH/学习哈希压缩特征，但跨模态下精度衰减，硬件实现能耗高。
3. 单模态CAM加速：仅处理图像哈希匹配，不支持图文异构多模态，长码区分度不足。
4. STT-MRAM PIM计算：多用于CNN推理，未针对LSH哈希做器件级随机向量生成优化。
5. 单阶段存内检索：仅汉明距离匹配，放弃余弦精排，多模态召回指标偏低。

## 本文解决方案
### 1 三层完整检索流水线
CLIP Transformer提取768维多模态特征→PIM模拟阵列生成512位三元TLSH哈希→CAM分段粗筛候选集→小规模余弦相似度精排输出结果。
### 2 器件原生随机TLSH哈希PIM阵列
利用MTJ工艺波动生成零均值随机向量；差分电导编码替代外部矩阵，省去高功耗ADC，仅通过电流比较输出0/1/X三元哈希码。
### 3 分段阈值CAM过滤机制
512位哈希拆分为8段64位子阵列，分段计算汉明距离并加权总分；设置三级距离阈值筛选，仅保留13.9%候选进入精排。
### 4 STT-MRAM双器件单元
PIM采用1T-1MTJ模拟阵列完成点积；CAM双MTJ单元编码哈希，并行匹配实现O(1)检索，硬件无缝对接TLSH输出电压格式。
### 5 分层精度平衡策略
CAM做低代价粗筛缩减搜索空间，仅对少量候选执行高精度余弦重排，兼顾硬件效率与多模态召回指标。

## 实验分析
1. 仿真环境：Brinkman/LLG器件建模、Cadence电路仿真，MSCOCO/Flickr8K/Flickr30K多模态数据集，R@1/R@5/R@10为指标。
2. 精度对比：MIRACLE召回率与CPU全量余弦基线几乎一致，远高于纯CAM汉明检索方案。
3. 硬件效率：相较CPU基线，检索延迟降低9.45倍，能耗下降30.2倍；PIM哈希几乎无额外存储开销。
4. 阈值消融：主阈值220、分段总分9可平衡精度与搜索量，仅约13.9%条目进入精排阶段。
5. 架构消融：移除PIM器件随机哈希或CAM分段过滤，时延/能耗优化效果大幅衰减。

## 研究启发
1. STT-MRAM器件固有工艺随机性可替代外部随机矩阵，省去海量存储与ADC功耗，是哈希计算轻量化新思路。
2. 纯CAM汉明匹配无法满足多模态精度需求，分层“粗筛+余弦精排”是硬件效率与检索精度的最优折中。
3. 长哈希串需分段并行CAM匹配，通过多阈值加权打分可缓解MRAM TMR比值带来的区分缺陷。
4. 存内计算与CAM硬件协同流水线，能从根源消除冯诺依曼数据搬运瓶颈，适配海量多模态实时检索场景。
5. 跨模态检索优化不能只聚焦特征提取网络，检索后端硬件加速同样存在巨大性能与能耗优化空间。
