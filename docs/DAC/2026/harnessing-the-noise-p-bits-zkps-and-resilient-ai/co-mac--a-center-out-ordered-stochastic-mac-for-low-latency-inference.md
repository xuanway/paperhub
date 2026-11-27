CO-MAC: A Center-Out Ordered Stochastic MAC for Low-Latency Inference
Authors：
[Hwangyu Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=38177140324507800301)，[Tong Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=10640896951512431271)，[Younghyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=221843)

## 中文标题

CO-MAC：面向低延迟推理的中心向外有序随机 MAC

## 英文摘要

Stochastic computing offers efficient approximate arithmetic that aligns well with error-tolerant machine learning workloads, but its deployment is limited by long bitstream latency in stochastic multiply-accumulate (MAC) units. Prior work reduces MAC latency through deterministic bitstream generation and differential accumulation, but these methods do not fully exploit the statistical properties of convolution weights. This work presents a novel stochastic MAC architecture named CO-MAC, which employs center-out weight ordering and an enhanced convolution engine design to reduce effective computation cycles while maintaining high accuracy. The method sorts weights by magnitude, reuses the incremental differences in magnitude, and applies sign handling after accumulation. This shortens the counter activity, maintains accuracy with long effective bitstreams, and simplifies the MAC hardware by avoiding bidirectional counters. Across convolutional neural network workloads, CO-MAC decreases MAC latency by up to 54.8% compared to prior stochastic MAC architectures, while preserving accuracy and hardware simplicity.

## 中文摘要

随机计算提供了高效的近似算术，与容错机器学习负载高度契合，但其在随机乘累加（MAC）单元中的长比特流延迟限制了其部署。已有工作通过确定性比特流生成与差分累加来降低 MAC 延迟，但这些方法并未充分利用卷积权重的统计特性。本文提出一种新颖的随机 MAC 架构 CO-MAC，它采用中心向外的权重排序与增强的卷积引擎设计，在保持高精度的同时减少有效计算周期。该方法按幅值对权重排序，复用幅值的增量差值，并在累加之后进行符号处理。这缩短了计数器活动时间，在长有效比特流下维持精度，并通过避免双向计数器简化了 MAC 硬件。在卷积神经网络负载中，CO-MAC 相比先前的随机 MAC 架构将 MAC 延迟最多降低 54.8%，同时保持精度与硬件简洁性。

## 英文关键词

Stochastic Computing, Convolutional Neural Network, Multiply-Accumulate

## 中文关键词

随机计算、卷积神经网络、乘累加
