CPA-BNN: A Secure and Efficient CIM and PUF Architecture for BNN Accelerator
Authors：
[Li Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=23419171826700470911)，[Jinwei Pu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7059746803458451121)，[Xijun Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=45682878205892770181)，[Wenhong Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4744318334127858852)，[Zhenyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2528844226615396419)，[Lei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8813595147727092869)，[Wanli Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=432143)，[You Meng](https://63dac.conference-program.com/?post_type=page&p=15&uid=8167050542845908912)

## 中文标题

CPA-BNN：一种面向 BNN 加速器的安全高效 CIM 与 PUF 架构

## 英文摘要

Binary neural networks (BNNs) have emerged as promising models for lightweight intelligent inference by binarizing inputs and weights. Compute in memory (CIM) architectures, which reduce data movements through in-situ operations, have become a strong candidate for BNN accelerators. However, prior works often overlook the security of the model, leaving BNN weights exposed in memory cells and vulnerable to threats such as cloning, tampering, and reverse engineering. This work proposes CPA-BNN, a secure BNN CIM architecture based on resistive random access memory (RRAM). We propose a 4T2R RRAM cell design which implements in-situ encryption and ciphertext convolution operations to protect the weights. In addition, an in-memory batch normalization (BN) scheme is proposed to optimize area overhead and improve compute density. Besides, we propose an intrinsic physical unclonable function (PUF) entropy extraction method and a current tilt-based masking stratege, enabling reliable key extraction within a unified array. The results show that CPA-BNN achieves ∼100% key reliability and effectively prevents model attacks. Compared to state-of-the-art SRAM/NVM BNN schemes, CPA-BNN achieves >1.4× compute density and >1.6× storage density improvement.

## 中文摘要

二值神经网络（BNN）通过将输入与权重二值化，已成为轻量级智能推理颇具前景的模型。存内计算（CIM）架构通过原位运算减少数据搬运，已成为 BNN 加速器的有力候选方案。然而，已有工作往往忽视模型的安全性，使 BNN 权重暴露在存储单元中，易受克隆、篡改和逆向工程等威胁。本文提出 CPA-BNN，一种基于阻变存储器（RRAM）的安全 BNN 存内计算架构。我们提出一种 4T2R RRAM 单元设计，实现原位加密与密文卷积运算以保护权重。此外，提出存内批归一化（BN）方案，以优化面积开销并提升计算密度。我们还提出一种内禀物理不可克隆函数（PUF）熵提取方法以及基于电流倾斜的掩码策略，可在统一阵列内实现可靠的密钥提取。结果表明，CPA-BNN 达到约 100% 的密钥可靠性，并有效抵御模型攻击。与先进的 SRAM/NVM BNN 方案相比，CPA-BNN 的计算密度提升超过 1.4 倍，存储密度提升超过 1.6 倍。

## 英文关键词

Hardware Security, Computing-in-Memory, Physical Unclonable Functions, Resistive Random Access Memory (RRAM)

## 中文关键词

硬件安全、存内计算、物理不可克隆函数、阻变存储器（RRAM）
