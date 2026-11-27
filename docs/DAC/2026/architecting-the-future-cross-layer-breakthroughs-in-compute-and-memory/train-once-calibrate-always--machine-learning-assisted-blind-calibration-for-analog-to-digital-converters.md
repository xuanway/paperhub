Train Once, Calibrate Always: Machine-Learning-Assisted Blind Calibration for Analog-to-Digital Converters
Authors：
[Shamma Nasrin](https://63dac.conference-program.com/?post_type=page&p=15&uid=54746428600591363721)，[Matt Kinsinger](https://63dac.conference-program.com/?post_type=page&p=15&uid=136725949537752227)，[Anoop Bengaluru](https://63dac.conference-program.com/?post_type=page&p=15&uid=9491169183901882332)，[Jia-Ching Chuang](https://63dac.conference-program.com/?post_type=page&p=15&uid=70535033669815227721)，[Sumukh Bhanushali](https://63dac.conference-program.com/?post_type=page&p=15&uid=800843)，[Arindam Sanyal](https://63dac.conference-program.com/?post_type=page&p=15&uid=2102406258078701969)

## 中文标题

一次训练，持续校准：机器学习辅助的模数转换器盲校准

## 英文摘要

This work introduces a machine-learning (ML)-based calibration framework for analog-to-digital converters (ADCs) that is demonstrated on an over-sampled, time-interleaved band-pass delta-sigma ADC (TI-BPADC) test-chip in 65nm and a nyquist, successive approximation register (SAR) ADC test-chip in 28 nm. The proposed framework employs two models: a hybrid convolutional-recurrent network (ConvRec) and a residual convolutional network (ResConv) for suppressing both static and dynamic errors in ADCs, and presents trade-offs between the two models in terms of calibration accuracy and hardware cost. The proposed models improve signal-to-noise-and-distortion ratio (SNDR) and spurious-free-dynamic range (SFDR) by more than 20 dB on the ADC test chips without requiring prior knowledge of circuit architecture, error mechanism or input statistics. This is in contrast to existing calibration techniques which are either algorithmic and require prior knowledge of errors for calibration, or leverage ML for calibration but need knowledge of input statistics. Input and error agnostic property of the proposed ML framework is the key differentiation of this work over others and allows correction of errors, including errors that are unforeseen during design time.

## 中文摘要

本工作提出一种基于机器学习（ML）的模数转换器（ADC）校准框架，并在 65nm 的过采样时间交织带通 delta-sigma ADC（TI-BPADC）测试芯片和 28nm 的奈奎斯特型逐次逼近寄存器（SAR）ADC 测试芯片上进行了验证。该框架采用两种模型：混合卷积-循环网络（ConvRec）与残差卷积网络（ResConv），用于抑制 ADC 中的静态与动态误差，并给出了两种模型在校准精度与硬件开销之间的权衡。所提模型在无需事先了解电路架构、误差机理或输入统计特性的情况下，将 ADC 测试芯片的信噪失真比（SNDR）与无杂散动态范围（SFDR）提升 20 dB 以上。这与现有校准技术形成对比：现有方法要么属于算法类方法、需要先验的误差知识才能校准，要么借助 ML 进行校准但需要了解输入统计特性。所提 ML 框架对输入与误差均不可知（agnostic）的特性，是本工作区别于其他工作的关键，使其能够纠正包括设计阶段未曾预见的误差在内的各类误差。

## 英文关键词

analog-to-digital converter, machine learning, calibration, convolution, recurrent neural network

## 中文关键词

模数转换器、机器学习、校准、卷积、循环神经网络
