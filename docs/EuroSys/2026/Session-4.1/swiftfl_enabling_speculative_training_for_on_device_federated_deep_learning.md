---
title: "SwiftFL: Enabling Speculative Training for On-Device Federated Deep Learning"
description: "EuroSys 2026 · On-Device & Federated Learning · Yuhui Zhang (State Key Laboratory of Information Security, Institute of Informat"
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# SwiftFL: Enabling Speculative Training for On-Device Federated Deep Learning

**中文标题：** SwiftFL：为端侧联邦深度学习实现投机训练

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Yuhui Zhang (State Key Laboratory of Information Security, Institute of Information Engineering, CAS and University of Chinese Academy of Sciences), Guang Yan (None), Xin Zhang (Peking University), Zimu Guo (Institute of Information Engineering, CAS), Lutan Zhao (Institute of Information Engineering, CAS), Jiangfeng Cao (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS), Dan Meng (Institute of Information Engineering, CAS), Rui Hou (Institute of Information Engineering, CAS)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803605)

## 英文摘要

Federated deep learning (FDL) is a promising privacy-preserving approach for training deep neural networks on distributed datasets without raw data sharing. But the classical synchronous FDL faces straggler problem: slow trainers severely impede overall efficiency. Inspired by speculative execution techniques in modern processors, this paper proposes SwiftFL, a novel and efficient speculative training system for FDL. Instead of simply waiting for slower trainer, SwiftFL proactively updates the global model with predicted gradients, enabling faster trainers to speculatively initiate the next training round. Furthermore, a gradient compensation technique is proposed to correct mispredicted training without re-training. Finally, to overcome the model-drift problem caused by fast trainers perform more local training rounds, we propose a client selection strategy. This strategy determines whether trainers should perform speculative training by striking a balance between two metrics: model drift degree and local training efficiency. In the evaluation, we compare SwiftFL with four state-of-the-art FDL systems and demonstrate that SwiftFL achieves an average speedup of 6.08× while maintaining consistent final model accuracy.

## 中文摘要

联邦深度学习（FDL）是一种有前景的隐私保护方法，可在不共享原始数据的情况下于分布式数据集上训练深度神经网络。但经典的同步 FDL 面临掉队者问题：较慢的训练者会严重拖累整体效率。受现代处理器中投机执行技术的启发，本文提出 SwiftFL，一种新颖高效的 FDL 投机训练系统。SwiftFL 不再单纯等待较慢的训练者，而是用预测的梯度主动更新全局模型，使较快的训练者能够投机性地启动下一轮训练。此外，我们提出一种梯度补偿技术，无需重新训练即可纠正预测错误的训练。最后，为克服快训练者执行更多本地训练轮次所导致的模型漂移问题，我们提出一种客户端选择策略。该策略通过在模型漂移程度与本地训练效率这两个指标之间取得平衡，来决定训练者是否应执行投机训练。在评估中，我们将 SwiftFL 与四种最先进的 FDL 系统进行比较，结果表明 SwiftFL 平均取得 6.08 倍加速，同时保持一致的最优模型精度。

**英文关键词：** Federated Deep Learning, Speculative Training

**中文关键词：** 联邦深度学习、投机训练

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
