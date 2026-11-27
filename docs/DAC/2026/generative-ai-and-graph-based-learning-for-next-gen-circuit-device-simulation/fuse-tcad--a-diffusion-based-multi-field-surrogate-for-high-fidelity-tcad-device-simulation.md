FUSE-TCAD: A Diffusion-Based Multi-Field Surrogate for High-Fidelity TCAD Device Simulation
Authors：
[Xulin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=15010629741560570731)，[Yupeng Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1255135015413225661)，[Zhuoran Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=92792859262361042411)，[Shucheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314800951181612359)，[Qi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=073843)

## 中文标题

FUSE-TCAD：一种面向高保真 TCAD 器件仿真的基于扩散的多场代理模型

## 英文摘要

Technology Computer-Aided Design (TCAD) solves coupled partial differential equations (PDEs) to obtain spatially resolved physical fields that are essential for comprehending device behavior. However, the computationally intensive numerical solution procedures in traditional TCAD make the iterative simulation-optimization loop prohibitively costly. Existing machine learning surrogates typically regress scalar metrics directly from device conditions, consequently discarding the field-level physical information crucial for further analysis. To address this challenge, we propose FUSE-TCAD, a diffusion-based surrogate that generates the joint distribution of physical fields while supporting continuous control over geometry and bias through conditional injection mechanisms. By leveraging the probabilistic generative formulation of diffusion models, FUSE-TCAD captures the underlying statistics of coupled physical fields and preserves cross-field consistency, thereby achieving highly accurate field predictions across diverse device conditions. A physics-aware Sobolev-edge regularization strategy enforces gradient consistency to ensure high fidelity in junction regions during sampling. On SOI-FET datasets, FUSE-TCAD demonstrates robust transferability and produces high-fidelity fields using only 20% target-domain data through efficient transfer learning. Extensive experiments demonstrate that FUSE-TCAD achieves more than 30× speedup over commercial TCAD tools and maintains relative error within 0.8%, thereby supporting scalable, near-real-time device design exploration.

## 中文摘要

技术计算机辅助设计（TCAD）通过求解耦合偏微分方程（PDE）获得空间分辨的物理场，而这些物理场对于理解器件行为至关重要。然而，传统 TCAD 中计算密集的数值求解流程使得仿真—优化迭代环路代价过高。现有的机器学习代理模型通常直接从器件条件回归标量指标，因而丢弃了对进一步分析至关重要的场级物理信息。为应对这一挑战，我们提出 FUSE-TCAD，一种基于扩散的代理模型，它生成物理场的联合分布，同时通过条件注入机制支持对几何与偏置的连续控制。借助扩散模型的概率生成式建模，FUSE-TCAD 刻画了耦合物理场的潜在统计特性并保持跨场一致性，从而在多样的器件条件下实现高精度的场预测。一种物理感知的 Sobolev 边缘正则化策略强制梯度一致性，以确保采样过程中结区的高保真度。在 SOI-FET 数据集上，FUSE-TCAD 展现出良好的可迁移性，并借助高效迁移学习仅使用 20% 的目标域数据即生成高保真场。大量实验表明，FUSE-TCAD 相较商用 TCAD 工具实现 30 倍以上加速，并将相对误差保持在 0.8% 以内，从而支撑可扩展、近实时的器件设计探索。
