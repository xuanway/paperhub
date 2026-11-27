Ciphershield: Safeguarding DNN Inputs from Ciphertext Side-Channels in TEE
Authors：
[Hui Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=68688212801010039001)，[Yuntao Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3722949728716555633)，[Qian Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=346843)

## 中文标题

CipherShield：保护 TEE 中 DNN 的输入免受密文侧信道攻击

## 英文摘要

Confidential environments such as Trusted Execution Environments (TEEs) are increasingly used to protect the data and models of machine learning applications from unauthorized access and leakage. Frameworks that run neural networks inside TEEs have been deployed for secure cloud-based inference. However, recent studies have revealed ciphertext side-channel attacks that exploit the encryption process within TEE environments, known as CipherSteal attacks. Specifically, when data is transferred into a TEE using encryption such as AES, the ciphertext patterns can be used to infer input data. In this paper, we propose CipherShield to mitigate the ciphertext side-channel leakage and protect sensitive input data. It is a set of lightweight transformations that diffuse and decorrelate ciphertext without the underlying cryptographic scheme. Our defenses, including block-based encryption, sparsity, and quantization, disrupt the per-address mapping patterns these attacks rely on, while maintaining TEE compatibility and high throughput. CipherShield reduces ciphertext hit rates from 50–80% to nearly zero across all evaluated datasets. On MNIST, CipherShield reduces classification accuracy from about 68% to as low as 2%, with similar reductions on Chest X-ray and CelebA datasets. Also, prototyping the block-based encryption in a TEE environment achieves markedly lower runtime than the original trace-based method, reducing encryption time by over 20×.

## 中文摘要

诸如可信执行环境（TEE）之类的机密环境正越来越多地被用于保护机器学习应用的数据与模型免遭未授权访问与泄露。在 TEE 内运行神经网络的框架已被部署用于安全的云端推理。然而，近期研究揭示了利用 TEE 环境内加密过程的密文侧信道攻击，即 CipherSteal 攻击。具体而言，当数据通过 AES 等加密方式传入 TEE 时，密文模式可被用于推断输入数据。本文提出 CipherShield，以缓解密文侧信道泄漏并保护敏感输入数据。它是一组轻量级变换，可在不改变底层密码方案的情况下对密文进行扩散与去相关。我们的防御手段包括基于分块的加密、稀疏化与量化，它们破坏了此类攻击所依赖的逐地址映射模式，同时保持 TEE 兼容性与高吞吐。在所有评估数据集上，CipherShield 将密文命中率从 50-80%降至接近零。在 MNIST 上，CipherShield 将分类准确率从约 68%降至低至 2%，在 Chest X-ray 与 CelebA 数据集上也有类似降幅。此外，在 TEE 环境中对基于分块的加密进行原型实现，其运行时间显著低于原始基于轨迹的方法，加密时间缩短超过 20 倍。

## 英文关键词

Ciphertext Side-Channel, Trust Execution Environment, Neural Networks

## 中文关键词

密文侧信道、可信执行环境、神经网络
