Tsetlinwisard: On-Chip Training of Weightless Neural Networks Using Tsetlin Automata on FPGAs
Authors：
[Shengyu Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8169167705581762254)，[Marcos Sartori](https://63dac.conference-program.com/?post_type=page&p=15&uid=6085370133645017808)，[Rishad Shafik](https://63dac.conference-program.com/?post_type=page&p=15&uid=570343)，[Alex Yakovlev](https://63dac.conference-program.com/?post_type=page&p=15&uid=870343)

## 中文标题

TsetlinWiSARD：在 FPGA 上利用 Tsetlin 自动机实现无权重神经网络的片上训练

## 英文摘要

Increasing demands for adaptability, privacy, and security at the edge have persistently pushed the frontiers for a new generation of machine learning (ML) algorithms with training and inference capabilities on-chip. Weightless Neural Network (WNN) is such an algorithm that is principled on lookup table based simple neuron structures. As a result, it offers architectural benefits, such as low-latency, low-complexity inference, compared to deep neural networks that depend heavily on multiply–accumulate operations. However, traditional WNNs rely on memorization-based one-shot training, which either leads to overfitting and reduced accuracy or requires tedious post-training adjustments, limiting their effectiveness for efficient on-chip training. In this work, we propose TsetlinWiSARD, a training approach for WNNs that leverages Tsetlin Automata (TAs) to enable probabilistic, feedback-driven learning. It overcomes the overfitting of WiSARD’s one-shot training with iterative optimization, while maintaining simple, continuous binary feedback for efficient on-chip training. Central to our approach is a field programmable gate array (FPGA)- based training architecture that delivers state-of-the-art accuracy while significantly improving hardware efficiency. Our approach provides over 1000× faster training when compared with the traditional WiSARD implementation of WNNs. Further, we demonstrate 22% reduced resource usage, 93.3% lower latency, and 64.2% lower power consumption compared to FPGA-based training accelerators implementing other ML algorithms.

## 中文摘要

边缘侧对适应性、隐私和安全性的需求不断增长，持续推动着具备片上训练与推理能力的新一代机器学习（ML）算法的发展。无权重神经网络（WNN）正是这样一种算法，它以基于查找表的简单神经元结构为原理。因此，与严重依赖乘累加运算的深度神经网络相比，它具备低延迟、低复杂度推理等架构优势。然而，传统 WNN 依赖基于记忆的一次性训练，这要么导致过拟合并降低精度，要么需要繁琐的训练后调整，从而限制了其在高效片上训练中的效果。在本工作中，我们提出 TsetlinWiSARD，一种利用 Tsetlin 自动机（TA）实现概率化、反馈驱动学习的 WNN 训练方法。它通过迭代优化克服了 WiSARD 一次性训练的过拟合问题，同时保持简单、连续的二元反馈以实现高效的片上训练。我们方法的核心是一个基于现场可编程门阵列（FPGA）的训练架构，它在提供最先进精度的同时显著提升硬件效率。与传统 WiSARD 实现的 WNN 相比，我们的方法训练速度提升超过 1000×。此外，与实现其他 ML 算法的基于 FPGA 的训练加速器相比，我们展示了 22% 的资源占用降低、93.3% 的延迟降低和 64.2% 的功耗降低。

## 英文关键词

Machine learning, Weightless neural networks, FPGA, Tsetlin automata, On-chip training

## 中文关键词

机器学习、无权重神经网络、FPGA、Tsetlin 自动机、片上训练
