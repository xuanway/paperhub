Holocode: Hybrid Optical-Electronic Edge Encoding for Privacy-Preserving Cloud Training
Authors：
[Ruofan Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=145450599857638761)，[Arman Akbari](https://63dac.conference-program.com/?post_type=page&p=15&uid=255843)，[Weikai Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=045357536506062489)，[Adith Boloor](https://63dac.conference-program.com/?post_type=page&p=15&uid=731768838911876466)，[Alexander McNeil](https://63dac.conference-program.com/?post_type=page&p=15&uid=6061973681398678884)，[Michael Moebius](https://63dac.conference-program.com/?post_type=page&p=15&uid=3463065865661551967)，[Yongmin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8806377855667010298)，[Yuhao Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=414543)，[Xuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=144843)

## 中文标题

HoloCode：面向隐私保护云端训练的混合光电边缘编码

## 英文摘要

Privacy-preserving machine learning aims to defend against adversaries without sacrificing task accuracy. In latency-critical and resource-constrained settings, existing cryptographic and encoding approaches incur heavy overheads that translate into intolerable delays and energy costs. We present HoloCode, a hybrid optical–electronic encoding pipeline that delivers strong privacy with sub-5ms latency at a fraction of the energy of prior state-of-the-art. HoloCode encodes only task-relevant signals while shielding sensitive features, resists inversion attacks, and locks models with a private key to prevent misuse. HoloCode builds on an edge–cloud collaboration framework, where inference is pushed to the edge to cut latency, at the cost of higher edge energy. To break this trade-off, we adopt an optical–digital hybrid pipeline that leverages zero-energy optical processing to reduce latency and edge energy simultaneously. Against strong privacy-preserving baselines, HoloCode achieves 10 × faster inference and 50% lower edge energy, while preserving accuracy and resisting privacy feature leakage and reconstruction attacks.

## 中文摘要

隐私保护机器学习旨在于不牺牲任务精度的前提下防御攻击者。在延迟敏感且资源受限的场景中，现有密码学与编码方法开销沉重，转化为难以容忍的延迟与能耗。我们提出 HoloCode，一种混合光–电编码流水线，以远低于此前最优方案的能耗实现低于 5ms 的强隐私保护。HoloCode 仅编码与任务相关的信号并屏蔽敏感特征，能够抵御反演攻击，并以私钥锁定模型以防滥用。HoloCode 构建于边–云协同框架之上：将推理下沉至边缘以降低延迟，代价是边缘能耗升高。为打破这一权衡，我们采用光–数字混合流水线，利用零能耗的光学处理同时降低延迟与边缘能耗。与强隐私保护基线相比，HoloCode 在保持精度的同时实现 10 倍更快的推理与 50% 更低的边缘能耗，并能抵御隐私特征泄露与重建攻击。
