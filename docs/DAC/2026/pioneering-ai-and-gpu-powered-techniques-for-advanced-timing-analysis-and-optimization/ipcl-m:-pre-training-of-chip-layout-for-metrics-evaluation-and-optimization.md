iPCL-M: Pre-Training of Chip Layout for Metrics Evaluation and Optimization
Authors：
[Xinhua Lai](https://63dac.conference-program.com/?post_type=page&p=15&uid=5552270592072392628)，[He Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=799243)，[Weiguo Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6953682769165296883)，[Yihang Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=28088831492518410171)，[Miao Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5631387700555107486)，[Simin Tao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5285629983100155188)，[Xingquan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=599243)，[Jungang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0036757289451890431)

## 中文标题

iPCL-M：面向指标评估与优化的芯片布局预训练

## 英文摘要

Physical design is a critical step in the electronic design automation (EDA) process, where the gate-level netlist from logic synthesis is converted into a GDS-II file. Recently, AI methods have been increasingly employed to address challenges in physical design. This paper proposes a new paradigm that integrates routing metric evaluation and optimization on chip layouts, forming a “Generate–Evaluate–Optimize –Generate” (GEOG) closed-loop. In our experiments, the pre-routing generation model achieves a mean relative error (MRE) of only 1%, with a mean absolute error (MAE) below one movement unit. Post-processing reduces both MRE and MAE to zero while ensuring connectivity. The evaluation model performs comparably to iSTA on the test set, with a 336× speedup. Furthermore, the optimization strategy effectively improves wirelength, delay, slew, R, and C by 10.49%, 13.03%, 14.85%, 10.51%, and 6.46%, respectively, and produces routing results superior to commercial tools in key metrics.

## 中文摘要

物理设计是电子设计自动化（EDA）流程中的关键环节，其任务是将逻辑综合得到的门级网表转换为 GDS-II 文件。近年来，AI 方法被越来越多地用于应对物理设计中的各类挑战。本文提出一种新范式，将布线指标评估与优化集成于芯片布局之上，形成“生成—评估—优化—生成”（GEOG）闭环。在实验中，布线前生成模型的平均相对误差（MRE）仅为 1%，平均绝对误差（MAE）低于一个移动单位。后处理在保证连通性的同时将 MRE 与 MAE 均降至零。评估模型在测试集上与 iSTA 表现相当，并取得 336× 加速。此外，优化策略有效改善了线长、延迟、转换时间、R 和 C，分别提升 10.49%、13.03%、14.85%、10.51% 和 6.46%，并在关键指标上产生优于商业工具的布线结果。

## 英文关键词

Metric evaluation, timing optimization, foundation model for layout, pre-training for routing generation

## 中文关键词

指标评估、时序优化、布局基础模型、布线生成预训练
