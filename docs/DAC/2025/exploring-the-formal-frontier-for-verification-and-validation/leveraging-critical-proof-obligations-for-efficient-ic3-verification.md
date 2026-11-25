---
title: "Leveraging Critical Proof Obligations for Efficient IC3 Verification"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Leveraging Critical Proof Obligations for Efficient IC3 Verification

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132734">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132734</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模型检验，关键证明义务，假设核心一致性 </p>
</div>


---

## 研究概要
本文提出关键证明义务CPO概念，配套两套IC3优化技术：CPO驱动UNSAT核心生成、CPO导向证明义务传播。基于IC3ref、MCer两套求解器实现，在786个HWMCC基准测试，优化后多解决15~20例，CPO识别率、引理传播成功率显著提升，大幅缩短硬件安全模型校验耗时。

## 背景和动机
1. IC3(PDR)是主流SAT硬件模型检验算法，迭代依赖证明义务PO队列与引理传播，低效PO处理会引发海量冗余SAT调用，验证速度严重下滑。
2. 传统PO无优先级区分，无差别处理全部反例，大量无关PO生成冗余引理，拖累帧收敛速度。
3. 标准UNSAT核心生成采用固定假设排序，难以产出利于引理泛化的紧凑核心，降低跨帧传播效率。
4. 现有传播策略无条件推送所有PO，产生大量无效引理堆积，增加SAT求解内存与时间开销。
5. 缺少可量化指标判定对引理传播起决定性的关键PO，无法针对性优化SAT查询与队列调度。

## 相关工作
1. 通用IC3引理优化：聚焦泛化规则、i-good引理挖掘，未从PO优先级与UNSAT核心生成层面优化。
2. QUIP算法：基于新增may-PO促进传播，不区分现有PO关键程度，无CPO筛选机制。
3. PO泛化综述：覆盖提升立方体压缩手段，但缺少PO选择性传播策略。
4. 底层SAT启发式（VSIDS）：面向冲突变量打分，未结合IC证明义务上下文定制假设排序。
5. 各类PDR衍生求解器（ABC、CAV23、DAC24）：缺少PO分层调度，冗余计算问题未解决。

## 本文解决方案
### 1 关键证明义务CPO定义与判定
定义若帧Fi存在引理¬c且c⊆PO立方体s，则(s,i)为CPO；证明仅全部CPO被阻塞，对应引理才能跨帧传播，作为算法优化理论依据。
### 2 CPO驱动UNSAT核心生成
提出ACC一致性打分指标，依据CPO历史频次重排SAT假设字面顺序；优先将高贡献变量放入UNSAT核心，生成更利于泛化的前驱立方体，提升CPO产出概率。
### 3 CPO导向选择性PO传播
遍历PO队列时仅对CP执行跨帧推送，普通PO直接丢弃；减少无效引理堆积，降低各帧冗余约束规模，加速收敛判定。
### 4 两套求解器原生集成优化
在IC3ref、MCer(基于CaDiCaL)分别实现-uc核心优化、-pr传播优化双开关，兼容主流AIGER硬件验证基准，无框架侵入性改动。
### 5 CPO识别率、引理传播成功率双评估指标
量化优化前后PO筛选、引理跨帧推送效果，直观衡量两套技术的加速收益。

## 实验分析
1. 测试环境：HWMCC2019/20/24共786个AIGER基准，5000s时间、8GB内存上限，对比ABC、CAV23、DAC24基线。
2. 求解数量：IC3ref双优化多解决20例，MCer多解决15例；优于全部对比SOTA工具。
3. 指标提升：CPO识别率基线0.26~0.49，优化后达0.31~0.54；引理传播成功率同步上涨。
4. 时效对比：CDF曲线显示同等时间内优化版本可求解更多案例，绝大多数实例验证时长显著缩短。
5. 消融验证：单独启用uc/pr均有收益，二者组合效果最优，少量实例出现性能损耗但整体收益占优。

## 研究启发
1. IC3性能瓶颈根源是无差别处理全部证明义务，基于CPO做优先级筛选可大幅削减冗余SAT查询。
2. SAT假设输入顺序直接决定UNSAT核心质量，结合IC3上下文定制打分机制能产出更优前驱立方体。
3. 引理跨帧传播存在硬性CPO前置约束，仅推送关键PO而非全体，可控制帧约束膨胀。
4. 底层SAT启发式与上层模型检验算法可协同定制，领域专属变量排序比通用VSIDS效果更好。
5. 轻量化PO调度优化无需重构IC3核心逻辑，易集成到现有主流硬件形式验证工具。