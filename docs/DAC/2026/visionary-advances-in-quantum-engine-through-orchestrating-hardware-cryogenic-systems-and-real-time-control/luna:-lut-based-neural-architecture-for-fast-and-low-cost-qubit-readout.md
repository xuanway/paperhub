LUNA: LUT-Based Neural Architecture for Fast and Low-Cost Qubit Readout
Authors：
[Muhammad Ali Farooq](https://63dac.conference-program.com/?post_type=page&p=15&uid=13711085155292797511)，[Giuseppe Di Guglielmo](https://63dac.conference-program.com/?post_type=page&p=15&uid=461843)，[Abhi Rajagopala](https://63dac.conference-program.com/?post_type=page&p=15&uid=4811408565953252349)，[Nhan Tran](https://63dac.conference-program.com/?post_type=page&p=15&uid=8436392422537880479)，[Vidya A. Chhabria](https://63dac.conference-program.com/?post_type=page&p=15&uid=977643)，[Aman Arora](https://63dac.conference-program.com/?post_type=page&p=15&uid=634843)

## 中文标题

LUNA：用于快速低成本量子比特读出的基于 LUT 的神经网络架构

## 英文摘要

Qubit readout is a critical operation in quantum computing systems, which maps the analog response of qubits into discrete classical states. Deep neural networks (DNNs) have recently emerged as a promising solution to improve readout accuracy . Prior hardware implementations of DNN-based readout are resource-intensive and suffer from high inference latency, limiting their practical use in low-latency decoding and quantum error correction (QEC) loops. This paper proposes LUNA, a fast and efficient superconducting qubit readout accelerator that combines low-cost integrator-based preprocessing with Look-Up Table (LUT) based neural networks for classification. The architecture uses simple integrators for dimensionality reduction with minimal hardware overhead, and employs LogicNets (DNNs synthesized into LUT logic) to drastically reduce resource usage while enabling ultra-low-latency inference. We integrate this with a differential evolution based exploration and optimization framework to identify high-quality design points. Our results show up to a 10.95× reduction in area and 30% lower latency with little to no loss in fidelity compared to the state-of-the-art. LUNA enables scalable, low-footprint, and high-speed qubit readout, supporting the development of larger and more reliable quantum computing systems.

## 中文摘要

量子比特读出是量子计算系统中的关键操作，它将量子比特的模拟响应映射为离散的经典态。深度神经网络（DNN）近来成为提升读出精度的一种颇具前景的方案。此前基于 DNN 的读出硬件实现资源开销大且推理延迟高，限制了其在低延迟解码与量子纠错（QEC）回路中的实际应用。本文提出 LUNA，一个快速高效的超导量子比特读出加速器，它将低成本的基于积分器的预处理与基于查找表（LUT）的神经网络分类相结合。该架构使用简单积分器进行降维，硬件开销极小，并采用 LogicNets（综合为 LUT 逻辑的 DNN）大幅降低资源占用，同时实现超低延迟推理。我们将该架构与基于差分进化的探索与优化框架集成，以寻找高质量的设计点。结果表明，与最先进工作相比，面积最多减少 10.95 倍，延迟降低 30%，而保真度几乎没有损失。LUNA 使量子比特读出具备可扩展、低占用与高速的特性，支撑更大规模、更可靠的量子计算系统的发展。

## 英文关键词

Qubit Readout, Quantum Computer Architecture, Quantum Control Hardware

## 中文关键词

量子比特读出、量子计算机架构、量子控制硬件
