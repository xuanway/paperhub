Light-Bound Transformers: Hardware-Anchored Robustness for Silicon-Photonic Computer Vision Systems
Authors：
[Xuming Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=2541047937269912011)，[Deniz Najafi](https://63dac.conference-program.com/?post_type=page&p=15&uid=0833931204233604074)，[Chengwei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=4101982256625903676)，[Pietro Mercati](https://63dac.conference-program.com/?post_type=page&p=15&uid=4229154621658791334)，[Arman Roohi](https://63dac.conference-program.com/?post_type=page&p=15&uid=642843)，[Mohsen Imani](https://63dac.conference-program.com/?post_type=page&p=15&uid=377143)，[Mahdi Nikdast](https://63dac.conference-program.com/?post_type=page&p=15&uid=102143)，[Shaahin Angizi](https://63dac.conference-program.com/?post_type=page&p=15&uid=246643)，[Gourav Datta](https://63dac.conference-program.com/?post_type=page&p=15&uid=664843)

## 中文标题

Light-Bound Transformer：硅光计算机视觉系统的硬件锚定鲁棒性

## 英文摘要

Deploying Vision Transformers (ViTs) on near-sensor analog accelerators demands training pipelines that are explicitly aligned with device-level noise and energy constraints. We introduce a compact framework for silicon-photonic execution of ViTs that integrates measured hardware noise, robust attention training, and an energy-aware processing flow. We first characterize bank-level noise in microring-resonator (MR) arrays, including fabrication variation, thermal drift, and amplitude noise, and convert these measurements into closed-form, activation-dependent variance proxies for attention logits and feed-forward activations. Using these proxies, we develop Chance-Constrained Training (CCT), which enforces variance-normalized logit margins to bound attention rank flips, and a noise-aware LayerNorm that stabilizes feature statistics without changing the optical schedule. These components yield a practical “measure → model → train → run” pipeline that optimizes accuracy under noise while respecting system energy limits. Hardware-in-the-loop experiments with MR photonic banks show that our approach restores near-clean accuracy under realistic noise budgets, with no in-situ learning or additional optical MACs.

## 中文摘要

在近传感器模拟加速器上部署视觉 Transformer（ViT）要求训练流程与器件级噪声和能耗约束显式对齐。我们提出一个用于 ViT 硅光执行的紧凑框架，它集成了实测硬件噪声、鲁棒注意力训练以及能耗感知的处理流程。我们首先刻画微环谐振器（MR）阵列中的 bank 级噪声，包括制造偏差、热漂移与幅度噪声，并将这些测量结果转化为针对注意力 logits 与前馈激活的闭式、依赖激活的方差代理量。利用这些代理量，我们开发了机会约束训练（CCT），通过施加方差归一化的 logit 裕度来约束注意力秩翻转，并提出一种噪声感知的 LayerNorm，在不改变光调度方案的前提下稳定特征统计量。这些组件构成一个实用的“测量 → 建模 → 训练 → 运行”流程，在遵守系统能耗限制的同时优化噪声下的精度。使用 MR 光子 bank 的硬件在环实验表明，我们的方法在真实噪声预算下恢复了接近无噪的精度，且无需原位学习或额外的光学 MAC。

## 英文关键词

ViT, photonic, microring-resonator, noise-aware, LayerNorm

## 中文关键词

ViT、光子、微环谐振器、噪声感知、LayerNorm
