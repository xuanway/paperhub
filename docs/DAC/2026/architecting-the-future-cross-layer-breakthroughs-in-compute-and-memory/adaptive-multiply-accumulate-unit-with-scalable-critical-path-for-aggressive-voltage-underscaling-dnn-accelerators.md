Adaptive Multiply-Accumulate Unit with Scalable Critical Path for Aggressive Voltage Underscaling DNN Accelerators
Authors：
[Tongjing Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4310331524435890429)，[Siting Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2045291533381948683)，[Tong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=334543)，[Hui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26491562959622173821)，[Zhigang Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=155343)，[Jie Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=273343)，[Honglan Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=91048570719084638371)

## 中文标题

面向激进欠压 DNN 加速器的可扩展关键路径自适应乘累加单元

## 英文摘要

Deep neural network (DNN) accelerators have widely been investigated for efficient inference, where matrix multiplication commonly implemented by multiply-accumulate (MAC) units dominates the power consumption. Underscaling the supply voltage of MACs can effectively reduce the power dissipation of DNN accelerators yet induces timing errors that may degrade the inference accuracy. In this paper, we propose a bit-width adjustment circuit (denoted as ADA) for arbitrary MAC units under aggressive voltage underscaling, which adaptively tunes the critical path as per input data patterns. Incurring 16.1% area overhead, the proposed ADA enables a MAC array to achieve zero accuracy loss under voltage underscaling ratios of 0.71 and 0.72 in the inferences of multi-layer perceptron (MLP) and convolutional neural network (CNN), respectively. While preserving accuracy, the MAC array equipped with ADA achieves up to 50.89% power reduction compared to that without ADA under nominal voltage operation. Furthermore, we propose ADA-Plus to specifically optimize the MACs in output stationary systolic arrays, which reduces the area of ADA by 23%. Compared with state-of-the-art error resilient circuit designs for voltage underscaling, to achieve a similar accuracy, the proposed adaptive MAC achieves the highest voltage underscaling ratio, resulting in 14.26%–48.44% power savings for the MAC array.

## 中文摘要

深度神经网络（DNN）加速器已被广泛研究用于高效推理，其中通常由乘累加（MAC）单元实现的矩阵乘法主导了功耗。降低 MAC 的供电电压可有效减少 DNN 加速器的功耗，但会引入时序错误，可能降低推理准确率。本文提出一种位宽调整电路（记为 ADA），用于在激进欠压下工作的任意 MAC 单元，它能够根据输入数据模式自适应地调整关键路径。所提 ADA 仅带来 16.1% 的面积开销，却使 MAC 阵列在多层感知机（MLP）与卷积神经网络（CNN）推理中分别于 0.71 与 0.72 的欠压比例下实现零准确率损失。在保持准确率的同时，配备 ADA 的 MAC 阵列在标称电压工作下相比未配备 ADA 的版本可实现最高 50.89% 的功耗降低。此外，我们提出 ADA-Plus，专门优化输出驻留式脉动阵列中的 MAC，使 ADA 的面积减少 23%。与面向欠压的最先进容错电路设计相比，在达到相近准确率的情况下，所提出的自适应 MAC 实现了最高的欠压比例，为 MAC 阵列带来 14.26%–48.44% 的功耗节省。

## 英文关键词

DNN accelerator, multiply-accumulate (MAC) unit, voltage underscaling, low-power

## 中文关键词

DNN 加速器、乘累加（MAC）单元、欠压、低功耗
