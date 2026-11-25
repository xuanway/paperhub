Signing Crossbar Columns Instead of Neural Network Weights in Compute-in-Memory Accelerators
Authors：
[Jun Pei](https://63dac.conference-program.com/?post_type=page&p=15&uid=13070936084807993071)，[Shaocong Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=25710633120223055031)，[Yian Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7544448956251878784)，[Jiukai Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=95370294535979720341)，[Jiuxian Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2596146758295178854)，[Yuliang Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=5527934826343054954)，[Yujian Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=766675754918597378)，[Yan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0388111020337446111)，[Yuchao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2470983435883587473)

## 中文标题

存内计算加速器中以 Crossbar 列为单位而非以神经网络权重为单位赋予符号

## 英文摘要

Weights in neural networks (NNs) are signed. Resistive Random Access Memory (RRAM), though a promising computing in-memory (CiM) for NN acceleration, is inherently unipolar as the conductance can only be positive, making it challenging to represent signed weights. Existing mainstream solutions utilize a differential pair of RRAM cells for representing a signed weight, which double the array size and significantly increase peripheral circuit cost, limiting the scalability and energy efficiency of CiM accelerators. In this work, instead of assigning a specific sign to each weight, we treat each column of the CiM crossbar as a unit and assign an identical sign to the entire column. To do this, we propose a Sign-Align Training and Mapping (SATM) framework that regularizes the network during training so that all weights mapped to the same column of a CiM crossbar share an identical sign. A Per-column Sign Register (PSR) is added to the array’s periphery to store the learned 1-bit sign configuration for each respective column. The experimental results show that the proposed SATM achieves up to 49.3% reduction in area overhead and up to 60.7% reduction in energy consumption for AlexNet, ResNet18, VGG16, ResNet50, and vision transformer models compared to differential-pair implementations.

## 中文摘要

神经网络（NN）中的权重是有符号的。阻变存储器（RRAM）虽是用于 NN 加速的一种颇具前景的存内计算（CiM）技术，但其本质上是单极性的——电导只能为正，因此难以表示有符号权重。现有主流方案采用一对差分 RRAM 单元来表示一个有符号权重，这使阵列尺寸翻倍并显著增加外围电路成本，从而限制了 CiM 加速器的可扩展性与能效。在本工作中，我们不再为每个权重单独指定符号，而是将 CiM crossbar 的每一列视为一个单位，为整列赋予相同的符号。为此，我们提出符号对齐训练与映射（SATM）框架，在训练过程中对网络进行正则化，使映射到 CiM crossbar 同一列的所有权重共享相同的符号。在阵列外围加入逐列符号寄存器（PSR），用于存储各列学习到的 1 比特符号配置。实验结果表明，与差分对实现相比，所提出的 SATM 在 AlexNet、ResNet18、VGG16、ResNet50 和 vision transformer 模型上最高可减少 49.3%的面积开销，并最高可降低 60.7%的能耗。
