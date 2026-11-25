WFH-BFs: Dynamic Defense Against DNN Bit-Flips via a Weight Function Hierarchy
Authors：
[Jie Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3714726598106034743)，[hao ying](https://63dac.conference-program.com/?post_type=page&p=15&uid=56528063378315973321)，[Aizhu Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=55465313989732911851)，[jiajun guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1308129650607908302)，[Zhanhui Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=94517439243632870201)，[Jungang Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=78086481300823999421)，[Fuli Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=98747383429135759861)

## 中文标题

WFH-BFs：通过权重函数层级实现针对 DNN 比特翻转的动态防御

## 英文摘要

Defending DNNs against bit-flip attacks (BFAs) typically incurs prohibitive computational overhead, a critical barrier for deployment in safety-critical systems. We challenge this “one-size-fits-all” defense paradigm by introducing the Weight Function Hierarchy (WFH), a framework that deconstructs DNNs into functionally distinct tiers: a compact Anchor Core for foundational representation, a Class-Sensitive layer for decision-making, and a Reservoir for redundancy. Based on WFH, our synergistic framework, WFH-BFs, couples offline preparation with online adaptation. Offline, we differentially harden the Anchor Core while embedding pruning tolerance elsewhere. Online, a lightweight integrity checker safeguards the core, while a dynamic pruning mechanism reconfigures the network to neutralize attacks. Experiments show WFH-BFs increases BFAs cost by 17.5× and maintains near-original accuracy (< 1.4%drop) under high-rate random errors(1 × 10−3 BER). Critically, our dynamic defense achieves this robust security while simultaneously reducing the overall computational load (GFLOPs), breaking the security-efficiency trade-off.

## 中文摘要

防御 DNN 免受比特翻转攻击（BFA）通常会带来难以承受的计算开销，这是其在安全关键系统中部署的关键障碍。我们通过引入权重函数层级（WFH）来挑战这种“一刀切”的防御范式，该框架将 DNN 解构为功能上彼此不同的层次：用于基础表示的紧凑锚定核心（Anchor Core）、用于决策的类敏感层（Class-Sensitive 层），以及用于冗余的储备层（Reservoir）。基于 WFH，我们的协同框架 WFH-BFs 将离线准备与在线自适应相结合。离线阶段，我们对锚定核心进行差异化加固，同时在其余部分嵌入剪枝容忍性。在线阶段，轻量级完整性检查器守护核心，而动态剪枝机制则重配置网络以消解攻击。实验表明，WFH-BFs 将 BFA 的攻击成本提高 17.5 倍，并在高速率随机错误（1×10⁻³ BER）下保持接近原始精度（下降小于 1.4%）。关键的是，我们的动态防御在实现这种鲁棒安全性的同时降低了整体计算负载（GFLOPs），打破了安全-效率折衷。

## 英文关键词

Deep Neural Networks, Bit-Flip Attacks, Model Robustness, Dynamic Defense

## 中文关键词

深度神经网络、比特翻转攻击、模型鲁棒性、动态防御
