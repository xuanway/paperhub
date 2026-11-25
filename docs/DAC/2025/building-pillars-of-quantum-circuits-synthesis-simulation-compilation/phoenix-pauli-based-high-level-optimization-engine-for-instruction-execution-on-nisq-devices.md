---
title: "Phoenix: Pauli-based High-level Optimization Engine for Instruction Execution on NISQ devices"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Phoenix: Pauli-based High-level Optimization Engine for Instruction Execution on NISQ devices

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.03529">https://arxiv.org/abs/2504.03529</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> Pauli基高层优化，Clifford变换，IR组排序，双量子门数量优化</p>
</div>



---

## 研究概要
本文提出面向NISQ设备VQA算法的PHOENIX高层编译引擎，基于二元辛形式BSF统一泡利IR，启发式克利福德变换批量简化泡利串，搭配俄罗斯方块式分组排序。兼容多量子指令集与硬件拓扑，UCCSD/QAOA测试相较主流编译器2Q门、电路深度大幅削减，算法保真误差更低。

## 背景和动机
1. NISQ时代VQE、QAOA等变分量子算法依赖大量泡利指数电路，2Q门与电路深度直接加剧硬件噪声，制约量子优势实现。
2. 现有编译器仅在子电路局部做门抵消优化，缺少全局泡利IR层面批量化简能力，优化上限低。
3. 传统编译方案绑定CNOT专属指令集，难以适配SU(4)等新型原生2Q门硬件，跨架构移植开销大。
4. 子电路组装未综合门抵消、布线开销、电路深度多维度代价，分组顺序不合理引入大量SWAP交换门。

## 相关工作
1. ZX图类编译器(TKET/PCOAST)：依托局部代数变换化简泡利模块，优化范围局限于子电路，缺乏全局批量化简手段。
2. Paulihedral/TETRIS：基于CNOT树做局部门抵消，仅适配CNOT指令集，布线优化优先牺牲高层化简潜力。
3. 2QAN：专门优化QAOA 2局部哈密顿，通用性差，无法覆盖UCCSD分子模拟等通用VQA任务。
4. 硬件感知映射工具(SABRE)：仅负责量子比特重排，不做高层泡利IR全局化简，前置电路规模大。

## 本文解决方案
### 1 BSF二元辛形式统一泡利IR表达
将每条泡利串编码为BSF表格行，利用2Q克利福德算子共轭变换同步降低多泡利串权重，实现全局批量化简，脱离单一CNOT指令集限制。
### 2 启发式BSF化简算法
设计综合代价函数遍历六类通用2Q克利福德算子，贪心选择最优变换迭代压缩泡利权重，直至全部算子权重≤2，剥离单量子泡利旋转减少冗余计算。
### 3 俄罗斯方块式IR分组排序
为每组子电路定义首尾端向量，综合电路深度、克利福德门抵消、量子交互图相似度构建统一代价函数，贪心选取最优拼接顺序，降低SWAP布线开销。
### 4 多指令集自适应重映射
化简后的高层IR可直接转换CNOT、SU(4)等各类原生2Q门电路，无需额外转译步骤，适配超导、离子阱等不同NISQ硬件拓扑。

## 实验分析
1. 测试负载：UCCSD分子模拟(CH₂/H₂O/LiH/NH)、随机/正则图QAOA，硬件采用全互联、IBM重六拓扑，基线TKET/Paulihedral/TETRIS/2QAN。
2. 逻辑层优化：相较原始电路平均减少80.47% CNOT、82.72% 2Q深度；优于全部对比编译器。
3. 硬件感知编译：重六拓扑下比Paulihedral少36.17% CNOT、43.85%深度，QAOA场景相较2QAN深度平均降40.8%。
4. 跨指令集：SU(4)原生门场景优化增益进一步提升，转译开销远低于基线工具。
5. 算法精度：相同演化时长下线路非保真误差低于TKET，BK编码体系优化效果更突出。

## 研究启发
1. VQA电路优化应从高层泡利IR全局入手，仅做底层门级局部化简存在显著性能天花板。
2. 克利福德共轭变换可批量化简多条泡利串，是区别传统逐个子电路优化的核心创新点。
3. 编译框架需解耦算法化简与硬件指令集，才能适配新一代多类型原生2Q门量子硬件。
4. 子电路排序不能仅关注门抵消，必须同时量化布线映射带来的SWAP开销实现多目标均衡。
5. 高层中间表示不仅用于电路编译，还可反向指导专用量子处理器控制单元设计。
