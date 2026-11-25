Capbench: A Multi-PDK Dataset for Machine-Learning-Based Post-Layout Capacitance Extraction
Authors：
[Hector Rodriguez](https://63dac.conference-program.com/?post_type=page&p=15&uid=584507554548481261)，[Jiechen Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=65755042464577648571)，[Wenjian Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=980243)

## 中文标题

CapBench：面向基于机器学习的版图后电容提取的多 PDK 数据集

## 英文摘要

We present CapBench, a fully reproducible, multi-PDK dataset for capacitance extraction. The dataset is derived from open-source designs, including single-core CPUs, Systems-on-Chip, and media accelerators. All designs are fully placed and routed using 14 independent OpenROAD flow runs spanning three technology nodes: ASAP7, NanGate45, and Sky130HD. From these layouts, we extract 61,855 3D windows across three size tiers to enable transfer learning and scalability studies. High-fidelity capacitance labels are generated using RWCap, a state-of-the-art random-walk solver, and validated against the industry-standard Raphael, achieving a mean absolute error of 0.64% for total capacitance. Each window is pre-processed into density maps, graph representations, and point clouds. We evaluate 10 machine learning architectures that illustrate dataset usage and serve as baselines, including convolutional neural networks (CNNs), point cloud transformers, and graph neural networks (GNNs). CNNs demonstrate the lowest errors (1.75%), while GNNs are up to 41.4× faster but exhibit the larger errors (10.2%), illustrating a clear accuracy–speed trade-off. Code and dataset are available at https://github.com/THU-numbda/CapBench.

## 中文摘要

我们提出 CapBench，一个完全可复现、支持多 PDK 的电容提取数据集。该数据集源自开源设计，涵盖单核 CPU、片上系统（SoC）与媒体加速器等。所有设计均通过 14 次独立的 OpenROAD 流程运行完成完整的布局与布线，覆盖 ASAP7、NanGate45 与 Sky130HD 三个工艺节点。我们从这些版图中提取了 61,855 个 3D 窗口，并划分为三个尺寸层级，以支持迁移学习与可扩展性研究。高保真电容标签由先进的随机行走求解器 RWCap 生成，并与工业标准工具 Raphael 进行校验，总电容的平均绝对误差为 0.64%。每个窗口均被预处理为密度图、图表示与点云三种形式。我们评估了 10 种机器学习架构，用以说明该数据集的使用方式并提供基准，其中包括卷积神经网络（CNN）、点云 Transformer 与图神经网络（GNN）。CNN 的误差最低（1.75%），GNN 最高可提速 41.4×，但误差较大（10.2%），清晰地体现了精度与速度之间的权衡。代码与数据集见 https://github.com/THU-numbda/CapBench。

## 英文关键词

Capacitance Extraction, Machine Learning, Dataset, EDA, Open Source PDKs

## 中文关键词

电容提取、机器学习、数据集、EDA、开源 PDK
