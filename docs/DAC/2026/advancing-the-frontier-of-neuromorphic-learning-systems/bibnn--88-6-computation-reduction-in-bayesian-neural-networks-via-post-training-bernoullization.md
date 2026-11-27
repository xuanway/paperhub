BiBNN: 88.6% Computation Reduction in Bayesian Neural Networks via Post-Training Bernoullization
Authors：
[Xiaotao Jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=50441278158873404281)，[Bohan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=19365094319135596401)，[Xueyan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=851443)，[Jianlei Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=144143)，[Weisheng Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=061443)

## 中文标题

BiBNN：通过训练后伯努利化将贝叶斯神经网络的计算量降低 88.6%

## 英文摘要

Deep neural networks often produce overconfident predictions on unseen data, posing risks in safety-critical applications. Bayesian neural networks (BayesNNs) address this by modeling weight uncertainty to provide reliable uncertainty estimation, yet suffer from high computational cost due to repeated sampling at inference. This work proposes BiBNN, a binarized BayesNN that reduces computational cost to only 11.4% of standard BayesNNs while retaining comparable uncertainty quantification capability. Through post-training Model Distribution Bernoullization (MDB), BiBNN enables full 1-bit inference without retraining. Experiments show that BiBNN outperforms deterministic binary neural networks by 1.6% on CIFAR-10 and 1.2% on EuroSAT in accuracy, with 9× lower computational cost.

## 中文摘要

深度神经网络在未见数据上往往会产生过度自信的预测，这在安全关键应用中带来风险。贝叶斯神经网络（BayesNN）通过对权重不确定性建模来提供可靠的不确定性估计，从而解决这一问题，但其推理时需要重复采样，因而计算开销高昂。本工作提出 BiBNN，一种二值化的贝叶斯神经网络，可将计算开销降至标准贝叶斯神经网络的仅 11.4%，同时保持相当的不确定性量化能力。通过训练后的模型分布伯努利化（MDB），BiBNN 无需重新训练即可实现完整的 1 比特推理。实验表明，BiBNN 在 CIFAR-10 上比确定性二值神经网络高出 1.6%、在 EuroSAT 上高出 1.2% 的准确率，且计算开销降低 9 倍。

## 英文关键词

Bayesian Neural Network, Quantization, Bernoulli Distribution, Uncertainty

## 中文关键词

贝叶斯神经网络、量化、伯努利分布、不确定性
