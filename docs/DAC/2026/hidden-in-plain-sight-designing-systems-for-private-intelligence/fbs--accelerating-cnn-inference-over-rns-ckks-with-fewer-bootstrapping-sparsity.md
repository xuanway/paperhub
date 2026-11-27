FBS: Accelerating CNN Inference over RNS-CKKS with Fewer Bootstrapping Sparsity
Authors：
[Guiming Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=372143)，[Yuchen Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=24777408754451387731)，[Zhanhong Tan](https://63dac.conference-program.com/?post_type=page&p=15&uid=90327739536785674531)，[Muyang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=07473979949455068911)，[Dapeng Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8906890356107005462)，[Jingwei Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=48138663409659791271)，[Shuwen Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=1262253940436032888)，[Kaisheng Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=908243)

## 中文标题

FBS：基于更少自举稀疏性的 RNS-CKKS 上 CNN 推理加速

## 英文摘要

RNS-CKKS is a fully homomorphic encryption scheme supporting fixed-point arithmetic, widely used in privacy-preserving convolutional neural network (CNN) inference. However, its significant computational overhead, especially from bootstrapping—the most costly operation—raises deployment costs for CNN inference over RNS-CKKS. While sparsity has proven effective in reducing computational overhead for unencrypted CNN inference, its application to large datasets (e.g., ImageNet) with RNS-CKKS-based CNN inference remains under-explored, particularly in optimizing bootstrapping operations that dominate computation time. In this work, we observe that sparsity in CNN can be exploited to reduce the bootstrapping overhead in RNS-CKKS-based CNN inference. Based on this observation, we propose FBS, a framework that accelerates CNN inference over RNS-CKKS by leveraging Fewer Bootstrapping Sparsity to reduce bootstrapping costs. We propose two sparsity patterns: eliminate missing input sparsity pattern and channel sparsity pattern, to reduce the number of bootstrapping calls during CNN inference. An iterative latency optimization framework is then presented to identify the key layers for pruning and determine the sparsity patterns to achieve effective performance. Results show that FBS can accelerate CNN inference over RNS-CKKS by up to 1.91× with negligible accuracy loss. Publicly available at https://github.com/fhedl/FBS.

## 中文摘要

RNS-CKKS 是一种支持定点运算的全同态加密方案，被广泛用于隐私保护卷积神经网络（CNN）推理。然而其计算开销巨大，尤其是其中开销最高的自举（bootstrapping）操作，抬高了基于 RNS-CKKS 的 CNN 推理部署成本。尽管稀疏性已被证明可有效降低非加密 CNN 推理的计算开销，但其在 RNS-CKKS 加密 CNN 推理的大规模数据集（如 ImageNet）上的应用仍缺乏探索，尤其是在优化主导计算时间的自举操作方面。本文观察到，可利用 CNN 中的稀疏性来降低基于 RNS-CKKS 的 CNN 推理的自举开销。基于此，我们提出 FBS，一个利用更少自举稀疏性（Fewer Bootstrapping Sparsity）来降低自举成本的 CNN 推理加速框架。我们提出两种稀疏模式——输入缺失稀疏消除模式与通道稀疏模式，以减少 CNN 推理过程中的自举调用次数。随后给出一个迭代式延迟优化框架，用于确定关键剪枝层并选择稀疏模式，从而取得有效性能。结果表明，FBS 可将 RNS-CKKS 上的 CNN 推理加速最高 1.91 倍，且精度损失可忽略。代码已公开于 https://github.com/fhedl/FBS。

## 英文关键词

FHE; RNS-CKKS; CNN; Neural Network Sparsity; Bootstrapping

## 中文关键词

FHE、RNS-CKKS、CNN、神经网络稀疏性、自举
