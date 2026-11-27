TT-SEAL: TTD-Aware Selective Encryption for Adversarially-Robust and Low-Latency Edge AI
Authors：
[Kyeongpil Min](https://63dac.conference-program.com/?post_type=page&p=15&uid=6541288396540782693)，[Sangmin Jeon](https://63dac.conference-program.com/?post_type=page&p=15&uid=5697948303766213397)，[Jae-Jin Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=96796192455184504)，[Woojoo Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=6757680176186143614)

## 中文标题

TT-SEAL：面向对抗鲁棒与低延迟边缘 AI 的 TTD 感知选择性加密

## 英文摘要

Cloud–edge AI must jointly satisfy model compression and security under tight device budgets. While Tensor-Train Decomposition (TTD) shrinks on-device models, prior selective-encryption studies largely assume dense weights, leaving its practicality under TTD compression unclear. We present TT-SEAL, a selective-encryption framework for TT-decomposed networks. TT-SEAL ranks TT cores with a sensitivity-based importance metric, calibrates a one-time robustness threshold, and uses a value-DP optimizer to encrypt the minimum set of critical cores with AES. Under TTD-aware, transfer-based threat models—and on an FPGA-prototyped edge processor—TT-SEAL matches the robustness of full (black-box) encryption while encrypting as little as 4.89–15.92% of parameters across ResNet-18, MobileNetV2, and VGG-16, and drives the share of AES decryption in end-to-end latency to low single digits (e.g., 58% →2.76% on ResNet-18), enabling secure, low-latency edge AI.

## 中文摘要

云–边 AI 必须在紧张的设备预算下同时满足模型压缩与安全需求。张量列分解（TTD）虽可缩小端侧模型规模，但以往的选择性加密研究大多假设权重为稠密形式，使其在 TTD 压缩下的实用性尚不明确。本文提出 TT-SEAL，一种面向 TT 分解网络的选择性加密框架。TT-SEAL 采用基于敏感度的重要性度量对 TT 核排序，一次性校准鲁棒性阈值，并利用值域动态规划（value-DP）优化器，以 AES 加密最小的关键核集合。面向 TTD 感知的迁移式威胁模型，并在 FPGA 原型实现的边缘处理器上，TT-SEAL 在 ResNet-18、MobileNetV2 与 VGG-16 上仅加密 4.89–15.92% 的参数，即达到与全量（黑盒）加密相当的鲁棒性，同时将 AES 解密在端到端延迟中的占比降至个位数低位（例如 ResNet-18 上由 58% 降至 2.76%），从而支撑安全、低延迟的边缘 AI。

## 英文关键词

model compression, tensor-train decomposition, selective encryption, adversarial robustness, edge AI, FPGA prototyping

## 中文关键词

模型压缩、张量列分解、选择性加密、对抗鲁棒性、边缘 AI、FPGA 原型验证
