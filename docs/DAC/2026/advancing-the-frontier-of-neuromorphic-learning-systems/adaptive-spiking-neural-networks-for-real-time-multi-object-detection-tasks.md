Adaptive Spiking Neural Networks for Real-Time Multi-Object Detection Tasks
Authors：
[Donghwa Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=07321970907263279331)，[Woojin Shin](https://63dac.conference-program.com/?post_type=page&p=15&uid=4615148467142322757)，[Cheol-Ho Hong](https://63dac.conference-program.com/?post_type=page&p=15&uid=7748588293611351895)，[Byunghoon Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=17260050367866669931)，[Jinkyu Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=9418521988749642266)，[Hyeongboo Baek](https://63dac.conference-program.com/?post_type=page&p=15&uid=6717306765547088242)

## 中文标题

面向实时多目标检测任务的自适应脉冲神经网络

## 英文摘要

Providing deterministic timing guarantees, beyond merely optimizing the accuracy-latency trade-off, is a critical yet unaddressed challenge for ultra-low-power spiking neural networks (SNNs) in resource-limited, safety-critical systems. We propose RT-SNN, an adaptive SNN method integrating a system-level scheduling framework for multi-object detection. For the first time, it co-optimizes inference accuracy while providing strict timing guarantees. RT-SNN orchestrates inference at frame and timestep levels, introducing flexible timestep control and a membrane potential reuse mechanism to enhance accuracy without increasing latency. Evaluations on the KITTI dataset demonstrate RT-SNN significantly improves accuracy and energy efficiency compared to state-of-the-art SNNs and traditional ANNs. Furthermore, a case study on a ROS-based F1/10 autonomous vehicle testbed validates its real-time efficacy for practical deployment.

## 中文摘要

除优化准确率与延迟的权衡之外，提供确定性的时序保证是超低功耗脉冲神经网络（SNN）在资源受限的安全关键系统中一项关键但尚未解决的挑战。我们提出 RT-SNN，一种集成系统级调度框架的自适应 SNN 方法，用于多目标检测。它首次在提供严格时序保证的同时协同优化推理准确率。RT-SNN 在帧级与时间步级编排推理，引入灵活的时间步控制与膜电位复用机制，从而在不增加延迟的情况下提升准确率。在 KITTI 数据集上的评估表明，相较于最先进的 SNN 与传统 ANN，RT-SNN 显著提升了准确率与能效。此外，在基于 ROS 的 F1/10 自动驾驶车辆测试平台上开展的案例研究验证了其在实际部署中的实时有效性。

## 英文关键词

Multi-object detection, spiking neural network, timing guarantee

## 中文关键词

多目标检测、脉冲神经网络、时序保证
