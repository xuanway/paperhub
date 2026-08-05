---
title: "Automated Generation of Decoders for Irregular Instruction Sets Using Information-Theoretic Decision Trees Construction Algorithms"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Automated Generation of Decoders for Irregular Instruction Sets Using Information-Theoretic Decision Trees Construction Algorithms

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132513">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132513</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 自动解码器生成，决策树算法，不规则指令集，信息论指标 </p>
</div>


---

## 研究概要
本文提出基于信息论决策树的不规则指令集解码器自动生成算法，支持带字段不等式、嵌套特化的ARMv7/MIPS32/SPARC复杂ISA。定义掩码/条件两类决策函数，采用卡方、基尼、熵、信息增益四大分裂指标，分单/多掩码两种构造模式，生成解码器功能完备、译码速度优于主流同类生成方案。

## 背景和动机
1. 现代ISA存在非统一操作码、字段逻辑命题、多长度指令、嵌套特化等不规则特征，传统解码器生成工具无法完整兼容，易产生功能错误译码树。
2. 现有生成算法仅基于固定比特掩码，不能将字段比较式作为分裂依据，处理复杂命题时需指数级展开编码，内存与耗时开销巨大。
3. 多数方案缺少标准化最优分裂评估指标，依赖简易贪心策略，生成译码树深度/分支规模失衡，实时译码延迟高。
4. 缺少统一形式化编码描述语法，无法统一表示相等、不等、区间类多字段约束，难以自动化处理主流商用指令集。
5. 现有工具仅适配简单RISC架构，ARM/MIPS等带SIMD、变长指令集需大量人工修正译码逻辑，开发成本高。

## 相关工作
1. Theiling基础比特树算法：仅测试固定比特，不支持逻辑命题、非统一Opcode，复杂ISA直接失效。
2. PART/EFF基于BDD展开方案：将命题枚举为所有合法编码，预处理指数爆炸，运行效率极低。
3. Okuda改进算法：可处理部分不规则编码，但表达式表达能力不足，易生成错误译码分支。
4. Qin掩码约束算法：限制掩码连续，最优解被剔除，译码性能反而下降，代价模型失真。
5. 简易贪心生成器：无信息论最优分裂标准，树深度不可控，译码吞吐差，仍大量依赖人工手写解码器。

## 本文解决方案
### 1 统一一阶逻辑编码形式化语法
设计兼容比特、多字段比较（等于/不等/区间）的BNF描述，无需枚举所有编码；区分掩码函数、条件函数两类分裂算子，支持单比特与复合命题作为分裂条件。
### 2 三段式匹配化简机制
定义完全匹配、部分匹配、不匹配三态规则；递归简化分支内编码约束，消除冗余命题，避免编码数量指数膨胀。
### 3 四类信息论最优分裂指标
集成卡方、基尼系数、熵、信息增益比；基于指令执行概率计算列联表，量化分支分类效果，自动筛选最优分裂点。
### 4 单/多掩码双构造模式
单模式每次选取最优单比特/命题；多模式迭代拼接最优比特构成复合掩码，控制掩码长度上限，平衡树深度与分支宽度。
### 5 完整递归译码树生成流程
递归拆分指令集合，记录累积约束；叶子节点补全剩余未判定命题，基于TRAP-Gen工具实现解码器自动生成。

## 实验分析
1. 实验环境：改造TRAP-Gen工具，测试SPARC、MIPS32 R6、ARMv7三类ISA，PolyBench测试集统计译码耗时，对比Theiling、Qin、PART等7种基线算法。
2. 功能验证：仅本文与Wary方案可全自动生成无错译码器，其余工具处理ARM/MIPS会产生功能缺陷。
3. 译码性能：单模式生成译码树平均深度更低，整体译码速度优于绝大多数贪心与传统优化算法；多模式树节点更少但深度更高，适合低分支硬件译码场景。
4. 生成开销：相比PART等BDD展开方法，峰值内存与生成时间大幅下降，复杂ARM指令集生成耗时可控。
5. 指标对比：卡方与基尼指标在多掩码场景表现稳定，熵/增益比在单分裂任务效果更突出。

## 研究启发
1. 不规则ISA不能仅依靠比特掩码分裂，必须将字段逻辑命题作为一等分裂条件，才能避免人工修正译码逻辑。
2. 信息论分类指标可量化分支优劣，是平衡译码树深度、分支数量、实时译码延迟的核心手段。
3. 区分单/多掩码两种构造模式，可适配软件模拟器、硬件译码器两类不同性能约束场景。
4. 形式化一阶逻辑编码描述可规避编码枚举爆炸，大幅降低解码器生成的内存与时间开销。
5. 仅追求树规模最小不一定提升译码速度，需结合指令运行概率设计分裂评价标准。