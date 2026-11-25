E³-CODE: Embedded and Efficient Error-Correcting Code for Error-Resilient Neural Networks
Authors：
[Venkata Nithin Kamineni](https://63dac.conference-program.com/?post_type=page&p=15&uid=4599961094570203768)，[Habibur Rahaman](https://63dac.conference-program.com/?post_type=page&p=15&uid=27082043273856353611)，[Ovishake Sen](https://63dac.conference-program.com/?post_type=page&p=15&uid=79360696645658105171)，[Baibhab Chatterjee](https://63dac.conference-program.com/?post_type=page&p=15&uid=1513248964279980705)，[SWARUP BHUNIA](https://63dac.conference-program.com/?post_type=page&p=15&uid=146143)，[Rickard Ewetz](https://63dac.conference-program.com/?post_type=page&p=15&uid=6428789118971238973)

## 中文标题

E³-CODE：面向抗错神经网络的内嵌高效纠错码

## 英文摘要

Neural networks are widely deployed at the edge to process high-dimensional sensor data, but they are susceptible to burst errors that can corrupt weights and degrade inference accuracy. Conventional error-correcting codes (ECC) mitigate errors but incur significant memory overhead. Recent ECC methods for neural networks overwrite the least significant bits of the model weights with parity bits, providing zero-overhead resilience at the expense of slightly reduced inference accuracy. In this paper, we propose a framework for Embedded and Efficient Error-Correcting Code for Error-Resilient Neural Networks called (E3-CODE). The proposed method embeds multi-bit parity within the entire weight representation, which is different from only modifying the LSBs of the weights. To minimize the negative impact from the parity embedded ECC, weight and parity assignments are jointly optimized via a mixed-integer linear programming (MILP) formulation. We also propose a hybrid ECC scheme that combines the embedded ECC with conventional ECC to trade-off minor memory overhead for significantly improved resilience. The experimental evaluation on the ImageNet and CIFAR-10 datasets using ResNet, MobileNetV2, and EfficientNet-B0 demonstrates that E3-CODE maintains software-level accuracy in the presence of burst errors with varying Bit Error Rates (BERs). Compared with the best prior methods, the lifetime of an edge system is extended by 4.3𝑋 with no memory overhead and 10𝑋 with less than 2% memory overhead. The code is publicly available at https://github.com/Nithin-Kamineni/E3-Codes.

## 中文摘要

神经网络被广泛部署在边缘端以处理高维传感器数据，但它们易受突发错误影响，这些错误会破坏权重并降低推理精度。传统的纠错码（ECC）能够缓解错误，但会带来显著的内存开销。近期面向神经网络的 ECC 方法用校验位覆写模型权重的最低有效位，以略微降低推理精度为代价提供了零开销的容错能力。本文提出一个面向抗错神经网络的内嵌高效纠错码框架，称为（E3-CODE）。所提方法在整个权重表示中嵌入多位校验位，这与仅修改权重最低有效位（LSB）的做法不同。为最小化嵌入校验位所带来的负面影响，通过混合整数线性规划（MILP）形式对权重与校验位的分配进行联合优化。我们还提出一种混合 ECC 方案，将内嵌 ECC 与传统 ECC 相结合，以少量内存开销换取显著提升的容错能力。在 ImageNet 和 CIFAR-10 数据集上使用 ResNet、MobileNetV2 和 EfficientNet-B0 进行的实验评估表明，在不同误码率（BER）的突发错误存在时，E3-CODE 仍能保持软件层面的精度。与最佳的先有方法相比，在无内存开销的情况下边缘系统的寿命延长了 4.3×，在内存开销小于 2% 的情况下延长了 10×。代码已公开于 https://github.com/Nithin-Kamineni/E3-Codes。
