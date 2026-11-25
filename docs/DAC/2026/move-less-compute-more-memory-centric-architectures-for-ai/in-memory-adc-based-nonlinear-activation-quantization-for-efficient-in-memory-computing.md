In-Memory ADC-Based Nonlinear Activation Quantization for Efficient In-Memory Computing
Authors：
[Shuai Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=89118523642212871701)，[Junyi Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=82179837201212164871)，[Biyan Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=6106430355031674652)，[Hongyang Shang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6060950429199644512)，[Gourav Datta](https://63dac.conference-program.com/?post_type=page&p=15&uid=664843)，[Arindam Basu](https://63dac.conference-program.com/?post_type=page&p=15&uid=77558097807363534821)

## 中文标题

面向高效存内计算的基于存内 ADC 的非线性激活量化

## 英文摘要

In deep networks, operations such as ReLU and hardware-driven clamping often cause activations to accumulate near the edges of the distribution, leading to biased clustering and suboptimal quantization in existing nonlinear (NL) quantization methods. This paper introduces Boundary Suppressed K-Means Quantization (BS-KMQ), a novel NL quantization approach designed to reduce the resolution requirements of analog-to-digital converters (ADCs) in in-memory computing (IMC) systems. By suppressing boundary outliers before clustering, BS-KMQ achieves more balanced and informative NL quantization levels. The resulting NL references are implemented using a reconfigurable in-memory NL-ADC, achieving a 7× area improvement over prior NL-ADC designs. When evaluated on ResNet-18, VGG-16, Inception-V3, and DistilBERT, BS-KMQ achieves at least 3× lower quantization error compared to linear, Lloyd–Max, cumulative distribution function (CDF), and K-means methods. It also improves post-training quantization accuracy by up to 66.8%, 25.4%, 66.6%, and 67.7%, respectively, compared to linear quantization. After low-bit fine-tuning, BS-KMQ maintains competitive accuracy with significantly fewer NL-ADC levels (3/3/4/4b). System-level simulations on ResNet-18 (6/2/3b) demonstrate up to a 4× speedup and 24× energy efficiency improvement over existing IMC accelerators.

## 中文摘要

在深度网络中，ReLU 等操作以及硬件驱动的截断常常使激活值聚集在分布边缘，导致现有非线性（NL）量化方法出现有偏的聚类和次优的量化结果。本文提出边界抑制 K-Means 量化（BS-KMQ），一种新颖的 NL 量化方法，旨在降低存内计算（IMC）系统中模数转换器（ADC）的分辨率需求。通过在聚类前抑制边界离群点，BS-KMQ 获得了更均衡、信息量更大的 NL 量化电平。所得到的 NL 参考值由可重构的存内 NL-ADC 实现，相比此前的 NL-ADC 设计取得 7 倍的面积改善。在 ResNet-18、VGG-16、Inception-V3 和 DistilBERT 上的评估表明，与线性、Lloyd–Max、累积分布函数（CDF）以及 K-means 方法相比，BS-KMQ 的量化误差至少降低 3 倍；与线性量化相比，其训练后量化精度分别最高提升 66.8%、25.4%、66.6%和 67.7%。经过低比特微调后，BS-KMQ 在显著更少的 NL-ADC 电平（3/3/4/4b）下仍保持有竞争力的精度。在 ResNet-18（6/2/3b）上的系统级仿真表明，相比现有 IMC 加速器，最高可实现 4 倍加速和 24 倍的能效提升。

## 英文关键词

Nonlinear Quantization, In-memory nonlinear ADC, In-memory Computing, Neural Networks, SRAM

## 中文关键词

非线性量化、存内非线性 ADC、存内计算、神经网络、SRAM
