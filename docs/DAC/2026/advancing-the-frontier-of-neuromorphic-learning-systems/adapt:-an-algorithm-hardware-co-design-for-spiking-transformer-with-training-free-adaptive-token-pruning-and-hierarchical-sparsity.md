ADAPT: An Algorithm-Hardware Co-Design for Spiking Transformer with Training-Free Adaptive Token Pruning and Hierarchical Sparsity
Authors：
[Pinfeng Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=31701874294341785511)，[Yilong Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=32803676894194092061)，[Letian Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=90512273436974974061)，[Yi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=99086287652308169151)，[Mingde Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8585667368049294838)，[Xiangshui Miao](https://63dac.conference-program.com/?post_type=page&p=15&uid=490210146683911856)，[Xingsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8051446369445277502)

## 中文标题

ADAPT：面向脉冲 Transformer 的算法-硬件协同设计，采用免训练自适应令牌剪枝与层次化稀疏

## 英文摘要

Spiking neural networks (SNNs) represent a promising solution for emerging architectures due to high sparsity and low power consumption. Spiking Transformers extend these advantages to attention-based modeling and show strong potential for energy-efficient applications. However, their practical deployment remains difficult. Spiking transformers demand substantial computation and memory access because of long token sequences and heavy workloads in feed-forward networks. Moreover, existing sparse optimization methods provide limited benefit for spiking transformers since they either focus only on unstructured bit-level sparsity or require model retraining. This work presents ADAPT, an algorithm–hardware co-design that exploits the hierarchical sparsity of spiking transformers. At the algorithm level, we propose Adaptive Token Pruning (ATP), a training-free method that evaluates token diversity and spike activity to remove redundant tokens. At the hardware level, we design a hierarchical-sparse accelerator that introduces a block-sparsity compression format and a pattern processing unit to leverage repeated bit patterns inside non-zero blocks. Experiments on multiple spiking transformer models demonstrate that ATP prunes 50% of tokens with negligible accuracy loss. The ADAPT accelerator achieves average speedups of 3.1 × and 4.2 × over state-of-the-art SNN accelerators Prosperity and GPU, while reducing energy by 1.9 × and 149.4 ×. These results show that exploiting hierarchical sparsity with algorithm–hardware co-design enables efficient deployment of spiking transformers.

## 中文摘要

脉冲神经网络（SNN）凭借高稀疏性与低功耗，成为新兴架构中颇具前景的解决方案。脉冲 Transformer 将这些优势扩展到基于注意力的建模，在节能应用中展现出强大潜力。然而，其实际部署仍然困难。由于令牌序列长、前馈网络负载重，脉冲 Transformer 需要大量计算与内存访问。此外，现有稀疏优化方法对脉冲 Transformer 的收益有限，因为它们要么只关注非结构化的位级稀疏，要么需要模型重训练。本工作提出 ADAPT，这是一种利用脉冲 Transformer 层次化稀疏性的算法-硬件协同设计。在算法层面，我们提出自适应令牌剪枝（ATP），这是一种免训练方法，通过评估令牌多样性与脉冲活跃度来剔除冗余令牌。在硬件层面，我们设计了一种层次稀疏加速器，引入块稀疏压缩格式与模式处理单元，以利用非零块内重复出现的位模式。在多个脉冲 Transformer 模型上的实验表明，ATP 可剪枝 50% 的令牌而精度损失可忽略不计。ADAPT 加速器相较最先进的 SNN 加速器 Prosperity 与 GPU 分别实现平均 3.1 倍和 4.2 倍的加速，同时将能耗降低 1.9 倍和 149.4 倍。这些结果表明，借助算法-硬件协同设计利用层次化稀疏性，可实现脉冲 Transformer 的高效部署。

## 英文关键词

Spiking Neural Networks, Spiking Transformers, Hierarchical Sparsity, Accelerator, Algorithm-Hardware Co-Design

## 中文关键词

脉冲神经网络、脉冲 Transformer、层次化稀疏、加速器、算法-硬件协同设计
