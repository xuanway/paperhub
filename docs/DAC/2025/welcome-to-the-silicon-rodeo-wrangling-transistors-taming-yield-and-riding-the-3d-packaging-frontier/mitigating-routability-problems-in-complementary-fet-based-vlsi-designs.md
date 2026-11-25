---
title: "Mitigating Routability Problems in Complementary-FET-based VLSI Designs"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Mitigating Routability Problems in Complementary-FET-based VLSI Designs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA8: Design for Manufacturing and Reliability</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133329">https://ieeexplore.ieee.org/document/11133329</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 互补场效应晶体管，可布线性优化，引脚扩展，局部放置阻挡 </p>
</div>


---

## 研究概要
本文面向5nm以下CFET垂直堆叠工艺，解决单元高度压缩带来引脚可达性、布线拥塞两大布线问题。设计强制M2、留白两类扩展单元，结合DBSCAN热点聚类与局部阻挡增量布局形成端到端流程。测试DRV最高削减71.3%，平均布线违规下降73.9%，同时保留CFET面积优势，时序功耗损失极小。

## 背景和动机
1. CFET垂直堆叠NMOS/PMOS大幅压缩单元高度至2~4轨，面积缩减40%，但BEOL布线轨道资源严重不足。
2. 单排CFET单元内部M2轨道稀缺，引脚接入点少，层间通孔易产生尖端包围DRV违规。
3. 单元密度大幅提升引发全局布线拥塞，传统P&R流程无法化解，设计违规数量激增。
4. 现有CFET库研究仅完成单元生成，未提出芯片级可布性优化完整流程。
5. 单纯加宽单元虽改善引脚，但会丢失CFET面积收益，需要兼顾面积与布线的折中方案。

## 相关工作
1. CFET器件与单元库设计：完成晶体管折叠、SMT自动单元生成，仅聚焦单单元版图，无芯片级布线优化。
2. 多排CFET单元方案：通过多行单元提升内部布线，但简单逻辑门只能单排实现，无法通用。
3. 传统先进节点P&R拥塞优化：面向FinFET/NSFET，未适配CFET极窄单元轨道约束。
4. 引脚访问优化研究：仅针对传统多轨标准单元，不适用于2~4轨CFET单层结构。
5. 增量布局技术：缺少基于早期全局布线拥塞的主动阻挡策略，被动修复DRV效率低。

## 本文解决方案
### 1 双类引脚扩展标准单元库
强制M2单元：在单元内部空闲M2轨道延伸引脚，不增加面积，搭配非对称通孔规避尖端违规；留白单元：利用单元上下空白区域垂直扩展M1引脚，大幅提升接入点，仅在有空位时替换。
### 2 拥塞感知局部阻挡布局流程
早期全局布线生成拥塞热力图，DBSCAN聚类识别拥塞热点；在热点区域插入局部阻挡框，保持整体利用率不变，执行增量布局疏散单元密度。
### 3 端到端CFET完整P&R流水线
综合→全部替换强制M2单元→早期全局布线+热点聚类+局部阻挡增量布局→CTS扫描空白区域动态切换留白单元→最终布线。
### 4 通孔包围冲突规避设计
强制M2单元采用非对称通孔版图，预留足够间距，消除M2走线与通孔的尖端DRV违规。
### 5 动态单元切换机制
CT阶段扫描单元上下空白，无重叠区域自动替换留白单元；存在相邻单元重叠则保留强制M2单元，平衡面积与可布性。

## 实验分析
1. 实验环境：Cadence Innovus、Design Compiler，CF_fp 2/4轨单元库，LDPC、VGA等OpenCore基准。
2. 拥塞优化效果：仅增量布局DRV下降47.1%，叠加局部阻挡后最高削减71.3%；利用率越高优化收益越弱。
3. 引脚违规优化：纯强制M2平均降80%DRV，纯留白单元降95%但面积膨胀；本文混合方案平均削减73.9%违规，面积增幅可控。
4. PPA影响：线长、功耗小幅波动，WNS轻微恶化但仍可时序收敛；流程运行开销仅增加10%~12%。
5. 对比消融：单一优化手段均存在短板，引脚扩展+拥塞阻挡组合才能兼顾面积与布线质量。

## 研究启发
1. CFET核心瓶颈是极低单元轨道资源，需从单元库源头改造引脚结构，而非仅后端布局补救。
2. 分层单元替换策略可在不牺牲CFET面积优势前提下，大幅提升引脚接入自由度。
3. 早期全局布线预判拥塞热点，主动插入局部阻挡比布线后修复DRV效率高得多。
4. 两类扩展单元各有取舍，动态按需切换是面积、布线质量的最优折中方案。
5. 先进垂直堆叠器件不能仅优化器件/单元，必须配套适配的完整P&R物理设计流程释放工艺优势。
