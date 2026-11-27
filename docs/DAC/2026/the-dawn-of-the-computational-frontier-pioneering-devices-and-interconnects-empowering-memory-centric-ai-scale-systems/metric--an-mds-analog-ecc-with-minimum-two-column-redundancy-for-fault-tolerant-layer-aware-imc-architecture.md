METRIC: An MDS-Analog ECC with Minimum Two-Column Redundancy for Fault-Tolerant, Layer-Aware IMC Architecture
Authors：
[Jiajun Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8212245922524449064)，[Chengping He](https://63dac.conference-program.com/?post_type=page&p=15&uid=8373369889983320739)，[Haozheng Wan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4846860214859505855)，[Zhanzhi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6000458394022318072)，[Mingrui Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=84414816593973596311)，[Can Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=036843)

## 中文标题

METRIC：一种面向容错、层感知 IMC 架构的最小双列冗余 MDS 模拟纠错码

## 英文摘要

Analog In-Memory Computing using analog-grade memory devices promises significant speed and energy efficiency for neural network inference, but its wide-spread deployment is challenged by the unexpected computing outliers from device to circuit non-idealities. While recent efforts like defect-aware training and ensemble methods address static variation, and conventional error correcting codes (ECC) protects the stored weights, neither can detect or correct dynamic, runtime errors that occur during the analog computation itself. In this work, we propose METRIC, a Maximum Distance Separable (MDS) Error Correction Code for analog computing, which encodes the redundancy output together with the intended output using a crossbar, with a theoretical minimum of two redundancy columns. Recognizing that neural network layers have varying error sensitivities, we introduce a layer-wise deployment strategy that adaptively allocates protection, minimizing hardware overhead while maintaining target model accuracy. Furthermore, we present a complete hardware implementation, including encoder and syndrome decoder circuits that performs error detection and correction entirely in the analog domain with minimal latency. Based on experimentally measured device and circuit non-idealities, METRIC restores inference accuracy to near-baseline levels on typical CNN and Transformer models, increasing 57% and 31% accuracy compared with unprotected analog computing respectively. Evaluations show that METRIC can achieve >1000× improved area and energy efficiency over the conventional analog ECC systems, showing its great potential for building reliable and efficient IMC accelerators.

## 中文摘要

基于模拟级存储器件的模拟存内计算为神经网络推理带来了显著的能效与速度优势，但其大规模部署仍受制于由器件至电路的非理想性所引发的、难以预料的计算离群值。已有工作如缺陷感知训练与集成方法针对的是静态偏差，传统纠错码（ECC）保护的是已存储的权重，二者均无法检测或纠正模拟计算过程本身出现的动态运行时错误。本文提出 METRIC，一种面向模拟计算的最大距离可分（MDS）纠错码：它借助 crossbar 将冗余输出与期望输出一并编码，理论上仅需两列冗余。鉴于神经网络各层对误差的敏感度各不相同，我们引入逐层部署策略，自适应地分配保护强度，在维持目标模型精度的同时最小化硬件开销。此外，我们给出了完整的硬件实现，包括编码器与校验子解码器电路，可在模拟域内以极低延迟完成错误的检测与纠正。基于实验测得的器件与电路非理想性数据，METRIC 在典型 CNN 与 Transformer 模型上将推理精度恢复到接近基线水平，相比无保护的模拟计算分别提升 57% 和 31% 的精度。评估表明，METRIC 相比传统模拟 ECC 系统可实现超过 1000 倍的面积与能效改善，展现出其在构建可靠、高效 IMC 加速器方面的巨大潜力。
