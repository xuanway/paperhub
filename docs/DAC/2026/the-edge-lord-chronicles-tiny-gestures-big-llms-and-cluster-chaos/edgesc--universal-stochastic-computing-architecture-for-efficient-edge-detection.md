Edgesc: Universal Stochastic Computing Architecture for Efficient Edge Detection
Authors：
[Xincheng Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=6473114596265800774)，[Wenyong Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=3259167542239798677)，[Taiqiang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2093097096281004189)，[Zhengwu Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=88592381613098896281)，[Meng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=414843)，[Ngai Wong](https://63dac.conference-program.com/?post_type=page&p=15&uid=127343)

## 中文标题

EdgeSC：面向高效边缘检测的通用随机计算架构

## 英文摘要

Stochastic computing (SC) processes data using stochastic bitstreams and offers substantial reductions in hardware complexity compared to conventional digital arithmetic, making it attractive for designs that benefit from simplified datapaths and multiplier-free execution. However, traditional SC designs are tailored to single operators, limiting reuse and incurring significant area overheads in multi-operator pipelines. We propose EdgeSC, a unified SC framework that performs edge detection fully in the stochastic domain. Pixel values are encoded as stochastic bitstreams, and spatial gradients are computed by ensembles of finite-state machines (FSMs) using a differentiable multiplexer (MUX)-based mapping that learns local neighborhood-to-edge relationships. Experiments show that EdgeSC reproduces Roberts, Sobel, and Canny-style operators and achieves higher ODS and OIS scores than traditional edge detection methods. Post-synthesis results in 28 nm CMOS further demonstrate that EdgeSC reduces total area by 11.7× and, across Roberts, Sobel, and Canny, delivers 2.3× lower power and 3.9× better area-delay product (ADP) than 8-bit fixed-point baselines that reflect standard hardware edge-processing practice, while maintaining comparable throughput.

## 中文摘要

随机计算（SC）利用随机比特流处理数据，相比传统数字算术可大幅降低硬件复杂度，因而对那些受益于简化数据通路与无乘法器执行的设计颇具吸引力。然而，传统 SC 设计针对单一算子定制，限制了复用，并在多算子流水线中带来显著的面积开销。我们提出 EdgeSC，一个统一的 SC 框架，完全在随机域内完成边缘检测。像素值被编码为随机比特流，空间梯度由有限状态机（FSM）集合计算得出，其采用基于可微多路复用器（MUX）的映射来学习局部邻域与边缘之间的关系。实验表明，EdgeSC 能够复现 Roberts、Sobel 与 Canny 风格的算子，并获得高于传统边缘检测方法的 ODS 与 OIS 分数。28 nm CMOS 的综合后结果进一步表明，EdgeSC 将总面积减少 11.7 倍；在 Roberts、Sobel 与 Canny 上，相较反映标准硬件边缘处理实践的 8 位定点基线，其功耗降低 2.3 倍、面积-延迟积（ADP）改善 3.9 倍，同时保持相当的吞吐率。

## 英文关键词

Stochastic computing, edge detection, finite-state machine, multi-operator generalization, low-power architecture

## 中文关键词

随机计算、边缘检测、有限状态机、多算子泛化、低功耗架构
