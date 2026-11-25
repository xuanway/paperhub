MXP: A Posit-Inspired Microscaling Format for Vision-Language Tasks
Authors：
[Dohyun Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=60228443813370602271)，[Byungkuk Yoon](https://63dac.conference-program.com/?post_type=page&p=15&uid=3768752245312726296)，[Jehun Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=182939904715315067)，[Juheun Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=15995351550252702831)，[Jae-Joon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=04856047519916349211)

## 中文标题

MXP：一种受 Posit 启发、面向视觉-语言任务的微缩放格式

## 英文摘要

Group-wise quantization is an effective strategy for low-bit inference, where a shared scale is assigned to each small group of tensor values. However, existing formats such as Microscaling (MX) struggle to capture the diverse value distributions found across modern workloads and tensor structures. In this work, we introduce MXP, a Posit-inspired microscaling format that incorporates tapered precision to dynamically adjust exponent and fraction bits at the element level. We first observe that directly integrating the Posit format into the MX framework leads to inefficiencies in precision. By addressing this limitation, MXP achieves a more optimal balance between precision and dynamic range, thereby reducing quantization errors. We further develop a hardware accelerator tailored to MXP, featuring a simplified decoding unit and a fused multiply–accumulate (MAC) array architecture. Experimental results demonstrate that MXP achieves higher accuracy, while reducing area by 11% and 33%, and power consumption by 12% and 40%, compared to a conventional MXFP and Posit-based designs, respectively.

## 中文摘要

分组量化是低比特推理的一种有效策略，它为每组较小的张量值分配一个共享缩放因子。然而，微缩放（MX）等现有格式难以刻画现代工作负载和张量结构中多样的数值分布。在本工作中，我们提出了 MXP，一种受 Posit 启发的微缩放格式，它引入渐变精度，在元素级别动态调整指数位和尾数位。我们首先观察到，将 Posit 格式直接集成到 MX 框架中会导致精度效率低下。通过解决这一局限，MXP 在精度和动态范围之间实现了更优平衡，从而降低量化误差。我们进一步开发了面向 MXP 的专用硬件加速器，具有简化的解码单元和融合乘累加（MAC）阵列架构。实验结果表明，与传统的 MXFP 和基于 Posit 的设计相比，MXP 分别将面积减少 11% 和 33%、功耗降低 12% 和 40%，同时实现了更高的精度。
