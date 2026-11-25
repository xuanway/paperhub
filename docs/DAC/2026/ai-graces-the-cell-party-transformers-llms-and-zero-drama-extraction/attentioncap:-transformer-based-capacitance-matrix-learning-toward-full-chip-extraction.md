Attentioncap: Transformer Based Capacitance Matrix Learning Toward Full-Chip Extraction
Authors：
[Jiechen Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=65755042464577648571)，[Hector Rodriguez](https://63dac.conference-program.com/?post_type=page&p=15&uid=584507554548481261)，[Dingcheng Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=688143)，[Zuochang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=666343)，[Yibo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=227143)，[Wenjian Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=980243)

## 中文标题

AttentionCap：面向全芯片电容提取的基于 Transformer 的电容矩阵学习

## 英文摘要

As capacitance extraction accuracy of rule-based pattern matching becomes difficult to sustain at advanced nodes, a growing trend emerges to develop deep-learning-based 2D capacitance models. However, existing MLP-and CNN-based methods constrain their input to fixed metal-layer combinations in a specific process node, limiting their usability in practice. Recognizing the inherent similarity between capacitance matrix and the prevailing attention mechanism, we propose AttentionCap, a customized Transformer for capacitance matrix learning, with a Gram representation framework, a physics-aligned symmetric-attention output layer, and a novel normalized Laplacian loss. We also introduce a process-node embedding to enable multi-node learning. Trained on synthetic data, AttentionCap attains 0.67%/3.99% self/coupling-capacitance error on unseen real designs under a multi-layer and multi-node setting, surpassing the CNN-Cap baseline with 4.6×/5.7× lower self/coupling error and 192× faster inference speed. A pretrained AttentionCap accurately transfers to an unseen node with only 5K samples and 4K finetuning steps. With sufficient accuracy on unseen real designs and strong transferability to new process nodes, AttentionCap offers highly practical value for modern EDA workflows. Code and data are available at https://github.com/THU-numbda/AttentionCap.

## 中文摘要

随着基于规则图案匹配的电容提取精度在先进工艺节点下愈发难以维持，开发基于深度学习的二维电容模型成为日益明显的趋势。然而，现有的基于 MLP 与 CNN 的方法将其输入限制为特定工艺节点下固定的金属层组合，限制了其在实际中的可用性。鉴于电容矩阵与当前流行的注意力机制之间存在内在相似性，我们提出 AttentionCap，一种为电容矩阵学习而定制的 Transformer，其具备 Gram 表示框架、与物理对齐的对称注意力输出层以及一种新颖的归一化拉普拉斯损失。我们还引入工艺节点嵌入，以支持多节点学习。在合成数据上训练后，AttentionCap 在多金属层、多节点设置下对未见过的真实设计取得了 0.67%/3.99% 的自电容/耦合电容误差，相比 CNN-Cap 基线，自电容/耦合电容误差分别降低 4.6 倍/5.7 倍，推理速度提升 192 倍。预训练的 AttentionCap 仅需 5K 样本与 4K 微调步数即可准确迁移到未见过的工艺节点。凭借在未见过真实设计上的充分精度以及对新工艺节点的强迁移能力，AttentionCap 对现代 EDA 流程具有很高的实用价值。代码与数据见 https://github.com/THU-numbda/AttentionCap。

## 英文关键词

Capacitance Extraction, Cross-Sectional Pattern Matching, Transformer, Attention Mechanism

## 中文关键词

电容提取、截面图案匹配、Transformer、注意力机制
