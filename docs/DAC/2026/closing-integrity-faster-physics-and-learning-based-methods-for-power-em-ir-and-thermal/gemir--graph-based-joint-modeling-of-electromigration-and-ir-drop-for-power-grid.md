GEMIR: Graph-Based Joint Modeling of Electromigration and IR Drop for Power Grid
Authors：
[Feng Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3624322913214613253)，[Yueyue Xi](https://63dac.conference-program.com/?post_type=page&p=15&uid=4956810517571335483)，[Jingyu Jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=2030981397372736682)，[Jiawei Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4896896750017244892)，[Tianshu Hou](https://63dac.conference-program.com/?post_type=page&p=15&uid=0485291662464877328)，[Yuyang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=8432721704885972621)，[Jianwang Zhai](https://63dac.conference-program.com/?post_type=page&p=15&uid=36525870277041148421)，[Kang Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=31063505926127256031)，[Chuan Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=6490758306758888738)

## 中文标题

GEMIR：面向电源网络的电迁移与 IR Drop 联合图建模

## 英文摘要

The combined effects of electromigration (EM) and IR drop critically affect the reliability and power integrity of power grids (PGs). Existing numerical methods are computationally prohibitive for large-scale designs, while most machine learning (ML) approaches analyze EM and IR drop in isolation, overlooking their shared physical structure and correlations in practical flows. To address this limitation, we propose GEMIR, a graph-based multi-task learning framework for the joint prediction of node-level static IR drop and edge-level EM-induced stress. GEMIR employs a cross-layer node-edge attention mechanism to effectively capture the mutual dependence between these two physical fields and integrates a physics-informed neural network (PINN) to enhance physical consistency in the EM path. Furthermore, we establish a composite optimization objective by incorporating physics-informed constraints that embed Kirchhoff’s current law (KCL) and Korhonen’s PDE to enhance model interpretability. To manage the inherently coupled yet sometimes conflicting optimization dynamics resulting from these constraints, we then develop a Conflict-Gated (CG) multitask optimization that adaptively fuses or decouples task gradients based on their alignment, thereby achieving mutual optimality. Extensive experiments demonstrate that GEMIR outperforms existing single-task and multi-task baselines in accuracy and generalization.

## 中文摘要

电迁移（EM）与 IR Drop 的耦合效应严重影响电源网络（PG）的可靠性与电源完整性。现有的数值方法对大规模设计而言计算代价过于高昂，而大多数机器学习（ML）方法孤立地分析 EM 与 IR Drop，忽略了二者共享的物理结构以及实际流程中的相关性。为解决这一局限，我们提出 GEMIR，一个基于图的多任务学习框架，用于联合预测节点级静态 IR Drop 与边级 EM 引起的应力。GEMIR 采用跨层节点—边注意力机制来有效捕捉这两个物理场之间的相互依赖，并集成物理信息神经网络（PINN）以增强 EM 路径上的物理一致性。此外，我们通过引入嵌入基尔霍夫电流定律（KCL）与 Korhonen 偏微分方程的物理信息约束，构建了复合优化目标，以增强模型的可解释性。为应对这些约束所带来的本质耦合但有时相互冲突的优化动态，我们进一步提出冲突门控（CG）多任务优化方法，根据任务梯度的对齐程度自适应地融合或解耦它们，从而实现相互最优。大量实验表明，GEMIR 在精度与泛化性上均优于现有的单任务与多任务基线。

## 英文关键词

Power Grid, IR Drop, Electromigration

## 中文关键词

电源网络、IR Drop、电迁移
