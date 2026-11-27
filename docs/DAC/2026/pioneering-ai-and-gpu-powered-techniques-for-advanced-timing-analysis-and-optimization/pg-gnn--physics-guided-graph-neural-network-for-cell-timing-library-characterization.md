PG-GNN: Physics-Guided Graph Neural Network for Cell Timing Library Characterization
Authors：
[Jason Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=14908545360850652161)，[Jeffery Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=9164791578558068475)，[Aaron Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6444536986799085177)，[Hung-Pin (Charles) Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=95982384704182032201)

## 中文标题

PG-GNN：面向单元时序库表征的物理引导图神经网络

## 英文摘要

Standard cell library characterization is a critical bottleneck for timing closure. Existing machine learning (ML) surrogates reduce SPICE costs but are constrained by labeled data requirements, limiting accuracy. This work introduces PG-GNN, a Physics-Guided Graph Neural Network (GNN) framework integrating residual learning with uncertainty-driven active learning. It simulates sparse anchor PVT corners, builds a physics-consistent reference, and trains a GNN on residual errors. Active learning then queries high-uncertainty points to minimize labeling. In experiments on TSMC 16 nm libraries, PG-GNN reduces SPICE effort by 98.7% with 1.67% MAPE. When applied to ISCAS’89 benchmarks, it achieves 0.74% critical path delay mismatch versus foundry libraries. PG-GNN offers orders-of-magnitude speedups in characterization runtime while maintaining signoff-level accuracy, presenting a scalable solution for next-generation IC design flows.

## 中文摘要

标准单元库表征是时序收敛的关键瓶颈。现有机器学习（ML）替代模型降低了 SPICE 开销，但受标注数据需求的制约，精度有限。本文提出 PG-GNN，一种物理引导的图神经网络（GNN）框架，将残差学习与不确定性驱动的主动学习相结合。该框架对稀疏锚点 PVT 工艺角进行仿真，构建物理一致的参考，并在残差误差上训练 GNN。随后，主动学习查询高不确定性点以最小化标注量。在 TSMC 16 nm 库上的实验中，PG-GNN 将 SPICE 工作量降低 98.7%，MAPE 为 1.67%。应用于 ISCAS’89 基准时，相较代工厂库其关键路径延迟失配为 0.74%。PG-GNN 在保持签核级精度的同时将表征运行时间缩短数个数量级，为下一代 IC 设计流程提供了可扩展的解决方案。

## 英文关键词

Cell library characterization, Graph neural networks, Active learning, Physics-guided machine learning

## 中文关键词

单元库表征、图神经网络、主动学习、物理引导机器学习
