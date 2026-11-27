PD-Net: Learning Device-Invariant Representations for Heterogeneous Cross-Device Side-Channel Attacks
Authors：
[Dalin He](https://63dac.conference-program.com/?post_type=page&p=15&uid=45941763529665320551)，[Wei Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=4725184390245949157)，[Yuejun Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4463207861172792359)，[Jingdian Ming](https://63dac.conference-program.com/?post_type=page&p=15&uid=9347126404928734953)，[Yongbin Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=3549020096504304078)

## 中文标题

PD-Net：面向异构跨设备侧信道攻击的设备不变表征学习

## 英文摘要

Heterogeneous cross-device side-channel attacks remain a critical yet underexplored challenge, as models trained on one device often fail to generalize across architectures. This paper presents PD-Net, a domain generalization framework that learns device-invariant features by disentangling algorithmic content from device-specific style and aligning feature distributions using prototypical and Maximum Mean Discrepancy (MMD) losses. PD-Net is trained on nine heterogeneous source domains spanning ARM/AVR/FPGA and power/electromagnetic leakage modalities, including 32-bit ARM Cortex-M0/M1/M3/M4, 8-bit AVR ATmega (three series), and 128-bit Xilinx Virtex-5 FPGA, and evaluated in a zero-shot setting without target-specific adaptation. Experimental results demonstrate robust zero-shot cross-architecture transfers between 8-bit and 32-bit devices, with consistent gains over existing generalization and transfer-learning approaches. In particular, PD-Net delivers 29 successful attacks with only 10 divergences across 70 settings, markedly outperforming the state of the art, which succeeds in only 4 cases and diverges 19 times. To the best of our knowledge, this is the first domain generalization (DG)-based deep learning framework to systematically demonstrate practical zero-shot heterogeneous cross-device side-channel attacks.

## 中文摘要

异构跨设备侧信道攻击仍是一项关键但研究不足的挑战，因为在一个设备上训练的模型往往难以跨体系结构泛化。本文提出 PD-Net，一个领域泛化框架，通过将算法内容与设备特定风格解耦，并利用原型损失和最大均值差异（MMD）损失对齐特征分布，来学习设备不变特征。PD-Net 在涵盖 ARM/AVR/FPGA 以及功耗/电磁泄露模态的九个异构源域上训练，包括 32 位 ARM Cortex-M0/M1/M3/M4、8 位 AVR ATmega（三个系列）与 128 位 Xilinx Virtex-5 FPGA，并在无目标特定适配的零样本设置下评估。实验结果表明，8 位与 32 位设备之间可实现稳健的零样本跨体系结构迁移，相比现有泛化与迁移学习方法取得一致增益。特别地，PD-Net 在 70 个设置中仅用 10 次发散便完成 29 次成功攻击，显著优于仅在 4 种情形成功、19 次发散的最优方法。据我们所知，这是首个基于领域泛化（DG）的深度学习框架，系统性地展示了实用的零样本异构跨设备侧信道攻击。

## 英文关键词

Side-Channel Attacks, Cross-Device Attack, Domain Generalization

## 中文关键词

侧信道攻击、跨设备攻击、领域泛化
