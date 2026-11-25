RTL-Sequencer: Towards Scalable RTL Timing Prediction with the Sequence-Based Paradigm
Authors：
[Ziyan Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=2259987640179897564)，[Wenji Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0880747726699421348)，[Wenkai LI](https://63dac.conference-program.com/?post_type=page&p=15&uid=91566662620660660201)，[Yuchao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03438700010529625741)，[Shang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888404795171209433)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

RTL-Sequencer：基于序列范式的可扩展 RTL 时序预测

## 英文摘要

Accurate timing prediction at the register-transfer level (RTL) is a longstanding challenge in design automation. Existing graph-based methods struggle with limited receptive fields, high complexity, and a lack of signal directionality. We present RTL-Sequencer, a novel sequence-based paradigm that enables scalable RTL timing prediction via linearizing logic cones by breadth-first traversal and applying modern linear sequence models. Furthermore, sequence models are customized by four synergistic techniques, including sequence shuffling, bidirectional modeling, differentiable modeling, and a hybrid graph-sequence architecture. Extensive experiments demonstrate significant improvements of RTL-Sequencer over state-of-the-art baselines, advancing early-stage timing optimization.

## 中文摘要

在寄存器传输级（RTL）进行准确的时序预测，一直是设计自动化中长期存在的难题。现有基于图的方法受限于感受野有限、复杂度高以及缺乏信号方向性。我们提出 RTL-Sequencer，一种新颖的基于序列的范式：通过广度优先遍历将逻辑锥线性化，并采用现代线性序列模型，从而实现可扩展的 RTL 时序预测。此外，我们通过四项协同技术对序列模型进行定制，包括序列打乱、双向建模、可微建模以及图—序列混合架构。大量实验表明，RTL-Sequencer 相较当前最先进的基线取得显著提升，推动了早期时序优化。
