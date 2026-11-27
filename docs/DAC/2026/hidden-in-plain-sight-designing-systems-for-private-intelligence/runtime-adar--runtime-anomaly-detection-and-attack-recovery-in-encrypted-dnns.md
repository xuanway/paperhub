Runtime-ADAR: Runtime Anomaly Detection and Attack Recovery in Encrypted DNNs
Authors：
[Jie Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3714726598106034743)，[jiajun guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1308129650607908302)，[yuhao huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1599012913529342334)，[hao ying](https://63dac.conference-program.com/?post_type=page&p=15&uid=56528063378315973321)，[zhanhui shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=94517439243632870201)，[Jianping Mei](https://63dac.conference-program.com/?post_type=page&p=15&uid=56438735586977886001)，[Fan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314143)

## 中文标题

Runtime-ADAR：加密 DNN 中的运行时异常检测与攻击恢复

## 英文摘要

Fault injection attack (FIA) poses a severe threat to accelerators executing privacy-preserving homomorphic encryption (HE) neural networks. Defending against FIAs in the ciphertext domain is challenging due to opaque internal states and the difficulty of distinguishing inherent encryption noise from malicious perturbations. We propose Runtime-ADAR, a lightweight runtime framework enabling closed-loop detection and recovery fully within the ciphertext domain. By repurposing intrinsic HE noise as a high-fidelity diagnostic signal, Runtime-ADAR integrates a sparse-projection noise detector for statistical anomaly sensing and a gradient-field repair engine for in-situ weight compensation. This synergy transforms encryption noise from a vulnerability into a defensive asset. Evaluations on multiple encrypted models show that Runtime-ADAR mitigates over 90% of attack successes and restores up to 97% baseline accuracy with modest performance overhead on CNNs.

## 中文摘要

故障注入攻击（FIA）对执行隐私保护同态加密（HE）神经网络的加速器构成严重威胁。由于密文域内部状态不透明，且难以区分固有加密噪声与恶意扰动，在密文域防御 FIA 极具挑战。我们提出 Runtime-ADAR，一个轻量级运行时框架，可在密文域内完整实现闭环检测与恢复。Runtime-ADAR 将同态加密固有噪声重新用作高保真诊断信号，集成了用于统计异常感知的稀疏投影噪声检测器，以及用于原位权重补偿的梯度场修复引擎。这种协同将加密噪声由漏洞转变为防御资产。在多个加密模型上的评估表明，Runtime-ADAR 可抑制超过 90% 的攻击成功案例，并在 CNN 上以适度的性能开销恢复至多 97% 的基线精度。

## 英文关键词

Deep Neural Network, Homomorphic Encryption, Fault Injection Attack, Runtime Adaptive Defense

## 中文关键词

深度神经网络、同态加密、故障注入攻击、运行时自适应防御
